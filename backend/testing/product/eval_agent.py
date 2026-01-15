"""
Eval Agent

LLM 评估代理，用于评估叙事质量。

对照 design.md §2.1 目录结构
对照 Requirements R-6-1-03
"""

from __future__ import annotations

import json
import logging
from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from backend.core.llm.client import LLMClient

logger = logging.getLogger(__name__)


# 评估 Prompt 模板
EVAL_SYSTEM_PROMPT = """你是一个专业的叙事质量评估专家。
你的任务是评估给定叙事文本的质量，并给出 0-1 之间的分数。

评估维度：
1. 内容相关性：叙事是否与用户问题相关
2. 专业准确性：叙事内容是否专业、准确
3. 表达清晰度：叙事是否清晰易懂
4. 建设性：是否提供有建设性的建议
5. 安全合规：是否避免极端或迷信表述

输出格式（JSON）：
{
    "score": 0.0-1.0,
    "dimensions": {
        "relevance": 0.0-1.0,
        "accuracy": 0.0-1.0,
        "clarity": 0.0-1.0,
        "constructive": 0.0-1.0,
        "safety": 0.0-1.0
    },
    "feedback": "简短的评价反馈"
}
"""

EVAL_USER_PROMPT_TEMPLATE = """请评估以下叙事文本的质量：

## 用户场景
- 用户类型：{user_type}
- 问题：{question}
- 使用引擎：{engines}

## 叙事文本
{narrative}

请按照系统提示的格式输出评估结果。
"""


class EvalAgent:
    """
    LLM 评估代理
    
    对照 Requirements R-6-1-03
    
    使用 LLM 评估叙事质量。
    """
    
    def __init__(
        self,
        llm_client: Optional["LLMClient"] = None,
        default_model: str = "gpt-4o-mini",
    ):
        """
        初始化评估代理
        
        Args:
            llm_client: LLM 客户端
            default_model: 默认模型
        """
        self._llm_client = llm_client
        self.default_model = default_model
    
    @property
    def llm_client(self) -> "LLMClient":
        """获取 LLM 客户端"""
        if self._llm_client is None:
            from backend.core.llm.client import LLMClient
            self._llm_client = LLMClient()
        return self._llm_client
    
    async def evaluate(
        self,
        narrative: str,
        scenario: Dict[str, Any],
        model: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        评估叙事质量
        
        Args:
            narrative: 叙事文本
            scenario: 场景数据
            model: 使用的模型
            
        Returns:
            评估结果 {"score": float, "dimensions": dict, "feedback": str}
        """
        model = model or self.default_model
        
        try:
            # 构建 prompt
            user_prompt = EVAL_USER_PROMPT_TEMPLATE.format(
                user_type=scenario.get("user_type", "unknown"),
                question=scenario.get("question", "unknown"),
                engines=", ".join(scenario.get("engines", [])),
                narrative=narrative,
            )
            
            # 调用 LLM
            if hasattr(self.llm_client, "complete_json"):
                result = await self.llm_client.complete_json(
                    prompt=user_prompt,
                    system_prompt=EVAL_SYSTEM_PROMPT,
                    model=model,
                    max_tokens=500,
                    temperature=0.3,
                )
            else:
                # Fallback: 使用 complete
                response = await self.llm_client.complete(
                    prompt=user_prompt,
                    system_prompt=EVAL_SYSTEM_PROMPT,
                    model=model,
                    max_tokens=500,
                    temperature=0.3,
                )
                result = self._parse_response(response.content)
            
            return self._normalize_result(result)
            
        except Exception as e:
            logger.error(f"EvalAgent error: {e}", exc_info=True)
            # 返回默认结果
            return {
                "score": 0.5,
                "dimensions": {},
                "feedback": f"Evaluation failed: {e}",
                "error": str(e),
            }
    
    def _parse_response(self, content: str) -> Dict[str, Any]:
        """解析 LLM 响应"""
        try:
            # 尝试提取 JSON
            content = content.strip()
            
            # 处理 markdown 代码块
            if content.startswith("```"):
                lines = content.split("\n")
                json_lines = []
                in_json = False
                for line in lines:
                    if line.startswith("```"):
                        in_json = not in_json
                        continue
                    if in_json:
                        json_lines.append(line)
                content = "\n".join(json_lines)
            
            return json.loads(content)
        except json.JSONDecodeError:
            # 尝试从文本中提取分数
            score = 0.5
            if "score" in content.lower():
                import re
                match = re.search(r"score[\"']?\s*[:=]\s*([0-9.]+)", content)
                if match:
                    score = float(match.group(1))
            
            return {
                "score": score,
                "feedback": content[:200],
            }
    
    def _normalize_result(self, result: Dict[str, Any]) -> Dict[str, Any]:
        """规范化结果"""
        score = result.get("score", 0.5)
        
        # 确保分数在 [0, 1] 范围内
        if score > 1:
            score = score / 100 if score <= 100 else 1.0
        score = max(0.0, min(1.0, score))
        
        return {
            "score": score,
            "dimensions": result.get("dimensions", {}),
            "feedback": result.get("feedback", ""),
        }
    
    async def batch_evaluate(
        self,
        narratives: list[tuple[str, Dict[str, Any]]],
        model: Optional[str] = None,
    ) -> list[Dict[str, Any]]:
        """
        批量评估
        
        Args:
            narratives: [(narrative, scenario), ...]
            model: 使用的模型
            
        Returns:
            评估结果列表
        """
        results = []
        for narrative, scenario in narratives:
            result = await self.evaluate(narrative, scenario, model)
            results.append(result)
        return results
