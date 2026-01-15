"""
Daily Extract Job

每日 22:00 提取 TO-DO/DONE 生成 Insight。

流程:
1. 查询所有用户当日 TO-DO/DONE 条目
2. 使用 LLM 提取用户行为意图
3. 生成 Insight 写入记忆层
4. 更新 TODO 条目的 extracted_intent 和 linked_insight_id
5. 记录执行日志
"""

import json
import logging
import secrets
from datetime import date, datetime, timedelta
from typing import Any, Dict, List, Optional

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from backend.db.session import async_session_maker
from backend.models.todo import TodoEntry
from backend.core.llm import select_layer, LLMLayer, LLMRequest

logger = logging.getLogger(__name__)

# 批处理配置
BATCH_SIZE = 100  # 每批处理用户数
MAX_RETRIES = 3   # 最大重试次数
MAX_LLM_CONCURRENT = 5  # LLM 并发限制

# LLM 意图解析 Prompt
INTENT_ANALYSIS_PROMPT = """分析以下用户行为，提取意图和模式。

## 今日计划 (TODO)
{todo_list}

## 今日完成 (DONE)
{done_list}

请以 JSON 格式返回（不要包含任何标记，只返回纯 JSON）：
{{
  "intents": [
    {{
      "content": "原文内容",
      "type": "plan或action",
      "category": "work|learning|health|social|leisure|other",
      "depth_intent": "深层意图描述"
    }}
  ],
  "patterns": ["行为模式1", "行为模式2"],
  "emotion_tendency": "积极|中性|消极",
  "summary": "一句话总结今日行为特征"
}}
注意：category 只能是 work/learning/health/social/leisure/other 之一。
"""


async def run_daily_extract() -> dict:
    """
    执行每日 TO-DO/DONE 意图提取
    
    Returns:
        执行报告 {
            "date": "2024-01-01",
            "total_users": 100,
            "processed_users": 95,
            "total_entries": 500,
            "extracted_entries": 480,
            "failed_users": ["user_id_1", ...],
            "duration_seconds": 120.5,
        }
    """
    start_time = datetime.utcnow()
    today = date.today()
    
    logger.info(f"Starting daily extract for {today}")
    
    report = {
        "date": today.isoformat(),
        "total_users": 0,
        "processed_users": 0,
        "total_entries": 0,
        "extracted_entries": 0,
        "failed_users": [],
        "duration_seconds": 0,
    }
    
    try:
        # 获取有今日条目的用户列表
        user_ids = await _get_users_with_today_entries(today)
        report["total_users"] = len(user_ids)
        
        if not user_ids:
            logger.info("No users with entries today, skipping")
            return report
        
        # 分批处理
        for i in range(0, len(user_ids), BATCH_SIZE):
            batch = user_ids[i:i + BATCH_SIZE]
            
            for user_id in batch:
                try:
                    entries_count = await _process_user(user_id, today)
                    report["total_entries"] += entries_count
                    report["extracted_entries"] += entries_count
                    report["processed_users"] += 1
                except Exception as e:
                    logger.error(f"Failed to process user {user_id}: {e}")
                    report["failed_users"].append(user_id)
            
            logger.info(f"Processed batch {i // BATCH_SIZE + 1}, "
                       f"users: {report['processed_users']}/{report['total_users']}")
    
    except Exception as e:
        logger.error(f"Daily extract failed: {e}")
        raise
    
    finally:
        report["duration_seconds"] = (datetime.utcnow() - start_time).total_seconds()
        logger.info(f"Daily extract completed: {report}")
    
    return report


async def _get_users_with_today_entries(today: date) -> List[str]:
    """
    获取今日有 TO-DO/DONE 条目的用户列表
    """
    start_of_day = datetime.combine(today, datetime.min.time())
    end_of_day = datetime.combine(today, datetime.max.time())
    
    async with async_session_maker() as session:
        # 查询今日有条目的用户（去重）
        result = await session.execute(
            select(TodoEntry.user_id)
            .where(TodoEntry.created_at >= start_of_day)
            .where(TodoEntry.created_at <= end_of_day)
            .where(TodoEntry.extracted_intent.is_(None))  # 只处理未提取的
            .distinct()
        )
        user_ids = [row[0] for row in result.fetchall()]
    
    logger.info(f"Found {len(user_ids)} users with today's entries")
    return user_ids


async def _process_user(user_id: str, today: date) -> int:
    """
    处理单个用户的今日条目
    
    Returns:
        处理的条目数量
    """
    # 1. 查询用户今日条目
    entries = await _get_user_today_entries(user_id, today)
    if not entries:
        return 0
    
    # 2. 使用 LLM 提取意图
    compiled_result = await _compile_entries(user_id, entries)
    
    # 3. 写入记忆层
    insight_id = await _save_to_memory(user_id, compiled_result)
    
    # 4. 更新条目
    await _update_entries(entries, compiled_result, insight_id)
    
    return len(entries)


async def _get_user_today_entries(user_id: str, today: date) -> List[TodoEntry]:
    """获取用户今日条目"""
    start_of_day = datetime.combine(today, datetime.min.time())
    end_of_day = datetime.combine(today, datetime.max.time())
    
    async with async_session_maker() as session:
        result = await session.execute(
            select(TodoEntry)
            .where(TodoEntry.user_id == user_id)
            .where(TodoEntry.created_at >= start_of_day)
            .where(TodoEntry.created_at <= end_of_day)
            .where(TodoEntry.extracted_intent.is_(None))
            .order_by(TodoEntry.created_at)
        )
        entries = list(result.scalars().all())
    
    return entries


async def _compile_entries(user_id: str, entries: List[TodoEntry]) -> dict:
    """
    编译条目，提取用户行为意图
    
    Phase 9 Task 9.1: 使用 Layer A (gemini-flash) 解析意图
    - 成功时返回 LLM 分析结果
    - 失败时降级到关键词匹配
    """
    # 提取内容
    todo_contents = []
    done_contents = []
    
    for entry in entries:
        if entry.entry_type == "todo":
            todo_contents.append(entry.content)
        else:
            done_contents.append(entry.content)
    
    # 尝试使用 LLM 解析
    llm_result = await _llm_analyze_intents(todo_contents, done_contents, user_id)
    
    if llm_result:
        # LLM 分析成功
        return {
            "user_id": user_id,
            "date": date.today().isoformat(),
            "entries_count": len(entries),
            "todo_count": len(todo_contents),
            "done_count": len(done_contents),
            "intents": llm_result.get("intents", []),
            "patterns": llm_result.get("patterns", []),
            "emotion_tendency": llm_result.get("emotion_tendency", "neutral"),
            "summary": llm_result.get("summary", f"今日计划 {len(todo_contents)} 项，完成 {len(done_contents)} 项"),
            "llm_analyzed": True,
        }
    
    # 降级到关键词匹配
    return await _compile_entries_fallback(user_id, entries, todo_contents, done_contents)


async def _llm_analyze_intents(
    todo_contents: List[str],
    done_contents: List[str],
    user_id: str,
) -> Optional[Dict[str, Any]]:
    """
    使用 Layer A (gemini-flash) 解析意图
    
    Phase 9 Task 9.1: LLM 意图解析
    """
    # 检查是否有内容需要分析
    if not todo_contents and not done_contents:
        return None
    
    try:
        # 选择 Layer A (解析层)
        provider, model = select_layer(LLMLayer.LAYER_A)
        
        if not provider:
            logger.warning("LLM provider not available, falling back to keyword")
            return None
        
        # 构建 Prompt
        todo_list = "\n".join(f"- {t}" for t in todo_contents) if todo_contents else "(无)"
        done_list = "\n".join(f"- {d}" for d in done_contents) if done_contents else "(无)"
        
        prompt = INTENT_ANALYSIS_PROMPT.format(
            todo_list=todo_list,
            done_list=done_list,
        )
        
        # 构建请求
        request = LLMRequest(
            prompt=prompt,
            model=model,
            max_tokens=500,
            temperature=0.3,
            response_format="json",
            user_id=user_id,
            timeout=15.0,  # 批处理设置较短超时
        )
        
        # 执行请求
        response = await provider.complete(request)
        
        # 解析 JSON
        content = response.content.strip()
        # 移除可能的 markdown 代码块标记
        if content.startswith("```"):
            content = content.split("\n", 1)[1] if "\n" in content else content[3:]
        if content.endswith("```"):
            content = content[:-3]
        content = content.strip()
        
        result = json.loads(content)
        
        logger.info(
            f"LLM intent analysis completed: user={user_id}, "
            f"intents={len(result.get('intents', []))}, "
            f"patterns={len(result.get('patterns', []))}, "
            f"model={response.model_used}"
        )
        
        return result
        
    except json.JSONDecodeError as e:
        logger.warning(f"LLM response JSON parse failed for user {user_id}: {e}")
        return None
    except Exception as e:
        logger.warning(f"LLM intent analysis failed for user {user_id}: {e}")
        return None


async def _compile_entries_fallback(
    user_id: str,
    entries: List[TodoEntry],
    todo_contents: List[str],
    done_contents: List[str],
) -> dict:
    """
    关键词匹配降级方案
    
    保留原有逻辑作为 LLM 失败时的 fallback
    """
    intents = []
    
    # 分析 TODO（计划）
    for content in todo_contents:
        intents.append({
            "type": "plan",
            "content": content,
            "category": _categorize_action(content),
        })
    
    # 分析 DONE（已完成）
    for content in done_contents:
        intents.append({
            "type": "action",
            "content": content,
            "category": _categorize_action(content),
        })
    
    return {
        "user_id": user_id,
        "date": date.today().isoformat(),
        "entries_count": len(entries),
        "todo_count": len(todo_contents),
        "done_count": len(done_contents),
        "intents": intents,
        "patterns": [],
        "emotion_tendency": "neutral",
        "summary": f"今日计划 {len(todo_contents)} 项，完成 {len(done_contents)} 项",
        "llm_analyzed": False,
    }


def _categorize_action(content: str) -> str:
    """
    简单的行为分类
    
    后续可接入更智能的分类模型。
    """
    content_lower = content.lower()
    
    # 工作相关
    if any(kw in content_lower for kw in ["工作", "会议", "项目", "开发", "代码", "文档", "work", "meeting"]):
        return "work"
    
    # 学习相关
    if any(kw in content_lower for kw in ["学习", "看书", "课程", "练习", "study", "learn", "read"]):
        return "learning"
    
    # 健康相关
    if any(kw in content_lower for kw in ["运动", "健身", "跑步", "睡眠", "吃", "exercise", "sleep", "health"]):
        return "health"
    
    # 社交相关
    if any(kw in content_lower for kw in ["朋友", "家人", "聚会", "聊天", "social", "friend", "family"]):
        return "social"
    
    # 休闲相关
    if any(kw in content_lower for kw in ["休息", "娱乐", "游戏", "电影", "音乐", "relax", "game", "movie"]):
        return "leisure"
    
    return "other"


async def _save_to_memory(user_id: str, compiled_result: dict) -> Optional[str]:
    """
    保存到记忆层
    
    Phase 9 Task 9.2: 增强版 Insight 写入
    
    流程:
    1. 记录 Daily Summary 事件
    2. 为每个意图记录事件
    3. 创建聚合 Insight (置信度根据 llm_analyzed 调整)
    4. 如果有 patterns，额外创建模式 Insight
    
    Returns:
        insight_id 或 None（如果保存失败）
    """
    try:
        from backend.services.memory import MemoryService, PrivacyLevel
        
        memory_service = MemoryService()
        event_ids = []
        
        # 1. 记录每日汇总事件
        summary_event_id = await memory_service.record_event(
            user_id=user_id,
            event_type="daily_todo_summary",
            data={
                "date": compiled_result["date"],
                "todo_count": compiled_result["todo_count"],
                "done_count": compiled_result["done_count"],
                "summary": compiled_result["summary"],
                "llm_analyzed": compiled_result.get("llm_analyzed", False),
                "emotion_tendency": compiled_result.get("emotion_tendency", "neutral"),
            },
            privacy_level=PrivacyLevel.PRIVATE,
        )
        event_ids.append(summary_event_id)
        
        # 2. 为每个意图记录单独事件
        for intent in compiled_result.get("intents", []):
            intent_event_id = await memory_service.record_event(
                user_id=user_id,
                event_type="user_intent",
                data={
                    "date": compiled_result["date"],
                    "intent_type": intent.get("type"),
                    "content": intent.get("content"),
                    "category": intent.get("category"),
                    "depth_intent": intent.get("depth_intent"),  # LLM 深层意图
                },
                privacy_level=PrivacyLevel.SENSITIVE,  # 具体内容加密
            )
            event_ids.append(intent_event_id)
        
        # 3. 创建聚合 Insight (置信度根据 llm_analyzed 调整)
        llm_analyzed = compiled_result.get("llm_analyzed", False)
        confidence = 0.85 if llm_analyzed else 0.6  # LLM 分析结果置信度更高
        
        insight_id = await memory_service.create_insight(
            user_id=user_id,
            summary=compiled_result["summary"],
            source_events=event_ids,
            confidence=confidence,
            dimension="behavior",  # 行为维度
            privacy_level=PrivacyLevel.PRIVATE,
        )
        
        # 4. Phase 9 Task 9.2: 如果识别到模式，额外创建 Insight
        patterns = compiled_result.get("patterns", [])
        for pattern in patterns[:2]:  # 最多 2 个模式洞察
            if pattern and isinstance(pattern, str) and len(pattern) > 2:
                await memory_service.create_insight(
                    user_id=user_id,
                    summary=f"行为模式: {pattern}",
                    source_events=event_ids,
                    confidence=0.75,
                    dimension="behavior",
                    privacy_level=PrivacyLevel.PRIVATE,
                )
        
        logger.info(
            f"Saved to memory: user={user_id}, events={len(event_ids)}, "
            f"insight={insight_id}, patterns={len(patterns)}, llm={llm_analyzed}"
        )
        return insight_id
        
    except Exception as e:
        logger.error(f"Failed to save to memory for user {user_id}: {e}")
        # 降级处理：生成临时 ID，不阻塞主流程
        return f"insight_{secrets.token_hex(6)}"


async def _update_entries(
    entries: List[TodoEntry],
    compiled_result: dict,
    insight_id: Optional[str],
) -> None:
    """
    更新条目的 extracted_intent 和 linked_insight_id
    """
    if not entries:
        return
    
    async with async_session_maker() as session:
        for entry in entries:
            # 找到对应的意图
            intent_data = None
            for intent in compiled_result.get("intents", []):
                if intent.get("content") == entry.content:
                    intent_data = intent
                    break
            
            # 更新条目
            entry.extracted_intent = intent_data.get("category") if intent_data else "other"
            entry.linked_insight_id = insight_id
            session.add(entry)
        
        await session.commit()
    
    logger.info(f"Updated {len(entries)} entries with insight {insight_id}")
