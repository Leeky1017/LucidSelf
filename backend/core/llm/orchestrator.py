"""
LLM Orchestrator

统一 LLM 编排层，为各场景提供标准化的调用入口。

设计原则:
1. 推送型系统：调用次数天然克制，无需复杂缓存
2. 质量优先：每次输出都要有理有据
3. TOON + NarrativeSnippet：标准化上下文注入

场景支持:
- Playbook: Daily/Weekly/Monthly/Yearly 生成
- Dream: 梦境解读
- LifeVersion: 人生版本校准结算
"""

import logging
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Optional

from backend.core.contracts import FusionResult
from backend.core.llm import LLMLayer, LLMRequest, get_layered_router
from backend.core.llm.toon_serializer import TOONSerializer
from backend.services.narrative.snippet_service import get_snippet_service

logger = logging.getLogger(__name__)

# WP-01: User Prompt 强制长度限制
MAX_USER_PROMPT_LENGTH = 4000
# 各部分预算分配（优先级从高到低）
PROMPT_BUDGET = {
    "header": 200,           # 时间信息 + 结构头
    "profile": 1200,         # 盘面块（核心）
    "rules": 800,            # 规则分析
    "insights": 600,         # 用户洞察
    "snippets": 800,         # 典籍素材
    "context": 300,          # 用户/额外上下文
    "footer": 100,           # 结尾指令
}


class ScenarioType(str, Enum):
    """LLM 调用场景类型"""
    PLAYBOOK_DAILY = "playbook_daily"
    PLAYBOOK_WEEKLY = "playbook_weekly"
    PLAYBOOK_MONTHLY = "playbook_monthly"
    PLAYBOOK_YEARLY = "playbook_yearly"
    DREAM = "dream"
    LIFE_VERSION = "life_version"


@dataclass
class ScenarioConfig:
    """场景配置"""
    scenario: ScenarioType
    layer: LLMLayer
    max_tokens: int
    temperature: float
    system_prompt_key: str


# 场景配置表
SCENARIO_CONFIGS = {
    ScenarioType.PLAYBOOK_DAILY: ScenarioConfig(
        scenario=ScenarioType.PLAYBOOK_DAILY,
        layer=LLMLayer.LAYER_B_CN,
        max_tokens=500,  # ~200字
        temperature=0.7,
        system_prompt_key="playbook_daily",
    ),
    ScenarioType.PLAYBOOK_WEEKLY: ScenarioConfig(
        scenario=ScenarioType.PLAYBOOK_WEEKLY,
        layer=LLMLayer.LAYER_B_CN,
        max_tokens=1200,
        temperature=0.7,
        system_prompt_key="playbook_weekly",
    ),
    ScenarioType.PLAYBOOK_MONTHLY: ScenarioConfig(
        scenario=ScenarioType.PLAYBOOK_MONTHLY,
        layer=LLMLayer.LAYER_B_CN,
        max_tokens=2000,
        temperature=0.7,
        system_prompt_key="playbook_monthly",
    ),
    ScenarioType.PLAYBOOK_YEARLY: ScenarioConfig(
        scenario=ScenarioType.PLAYBOOK_YEARLY,
        layer=LLMLayer.LAYER_B_CN,
        max_tokens=3000,
        temperature=0.6,
        system_prompt_key="playbook_yearly",
    ),
    ScenarioType.DREAM: ScenarioConfig(
        scenario=ScenarioType.DREAM,
        layer=LLMLayer.LAYER_B_CN,
        max_tokens=1500,
        temperature=0.7,
        system_prompt_key="dream",
    ),
    ScenarioType.LIFE_VERSION: ScenarioConfig(
        scenario=ScenarioType.LIFE_VERSION,
        layer=LLMLayer.LAYER_B_COMPLEX,
        max_tokens=2000,
        temperature=0.5,
        system_prompt_key="life_version",
    ),
}


# 系统 Prompt 模板库 - 精确版
SYSTEM_PROMPTS = {
    "playbook_daily": """# 角色
你是 LucidSelf 每日指引师，根据用户的命理盘面数据，生成今日行动建议。

# 输入数据说明
- **分析数据**: 用户的八字、紫微、西占等命理因子及规则匹配结果
- **典籍素材**: 可引用的传统命理文献表述，优先使用

# 输出要求
1. **今日主题**: 一句话概括今日能量特点（15字内）
2. **宜做**: 1-2件今日适合做的事，简述理由
3. **慎做**: 1件今日需谨慎的事，简述理由
4. **一句话建议**: 给用户的核心提醒

# 风格
- 温和智慧，不做绝对判断
- 具体可行，避免空泛
- 总字数约150-200字""",

    "playbook_weekly": """# 角色
你是 LucidSelf 周度策略师，根据用户的命理盘面和本周运势，生成一周规划建议。

# 输入数据说明
- **分析数据**: 用户的八字、紫微、西占等命理因子及规则匹配结果
- **典籍素材**: 可引用的传统命理文献表述

# 输出要求
1. **本周主题**: 一句话概括本周能量走势
2. **关键节点**: 本周需要关注的2-3个时间点（如周二适合决策、周五适合社交）
3. **核心策略**: 2-3条可执行的周度行动方向
4. **风险提示**: 本周需避开的1件事

# 风格
- 积极正面，务实可行
- 总字数约300-400字""",

    "playbook_monthly": """# 角色
你是 LucidSelf 月度规划师，根据用户的命理盘面和本月运势，生成月度规划建议。

# 输入数据说明
- **分析数据**: 用户的八字、紫微、西占等命理因子及规则匹配结果
- **典籍素材**: 可引用的传统命理文献表述

# 输出要求
1. **本月主题**: 概括本月整体运势特点
2. **机会领域**: 本月最有利的2-3个方向（事业/感情/财运/健康）
3. **挑战领域**: 本月需警惕的1-2个方面
4. **分周建议**: 按上中下旬给出简要策略
5. **月度关键词**: 3个本月核心提醒词

# 风格
- 全面但不冗长，重点突出
- 总字数约500-700字""",

    "playbook_yearly": """# 角色
你是 LucidSelf 年度展望师，根据用户的命理盘面和流年运势，生成年度全景规划。

# 输入数据说明
- **分析数据**: 用户的八字、紫微、西占等命理因子及规则匹配结果
- **典籍素材**: 可引用的传统命理文献表述

# 输出要求
1. **年度主题**: 本年的核心关键词和整体基调
2. **四季策略**: 按春夏秋冬分别给出侧重方向
3. **重点领域分析**: 事业、财运、感情、健康各一段
4. **年度机遇**: 本年最大的2-3个发展机会
5. **年度警示**: 本年需持续关注的1-2个风险点
6. **年度寄语**: 送给用户的一句话

# 风格
- 深度全面，有高度
- 总字数约800-1200字""",

    "dream": """# 角色
你是 LucidSelf 解梦师，结合用户的命理背景解读梦境符号。

# 输入数据说明
- **梦境内容**: 用户描述的梦境原文
- **分析数据**: 用户的命理背景因子
- **典籍素材**: 梦境相关的传统文献表述

# 输出要求
1. **核心符号**: 提取梦境中的2-3个关键意象
2. **符号解读**: 每个符号的传统含义和可能指向
3. **命理关联**: 结合用户当前运势的深层解读
4. **行动启示**: 梦境可能暗示的现实方向

# 风格
- 温和引导，不恐怖化
- 启发性而非定论式
- 总字数约300-400字""",

    "life_version": """# 角色
你是 LucidSelf 人生导航师，帮助用户在实际选择与命理建议之间找到平衡。

# 输入数据说明
- **分析数据**: 用户的命理背景
- **偏离描述**: 用户实际选择与命理建议的差异点

# 输出要求
1. **偏离识别**: 明确用户选择与命理建议的差异点
2. **风险分析**: 这种偏离可能带来的挑战
3. **机会分析**: 这种偏离可能带来的独特机会
4. **调和建议**: 如何在坚持选择的同时降低风险
5. **支持寄语**: 无论选择如何，给予用户的肯定和鼓励

# 风格
- 温和不评判，像智慧的朋友
- 尊重用户的自主选择
- 总字数约400-600字""",
}


@dataclass
class OrchestratorResult:
    """编排结果"""
    content: str
    scenario: ScenarioType
    model_used: str
    tokens_used: int
    latency_ms: float
    toon_context: str
    snippets_count: int


class LLMOrchestrator:
    """
    LLM 编排器
    
    统一入口，处理所有场景的 LLM 调用。
    
    使用方式:
        orchestrator = LLMOrchestrator()
        result = await orchestrator.generate(
            scenario=ScenarioType.PLAYBOOK_DAILY,
            fusion_result=fusion_result,
            user_context={"name": "张三"},
        )
    """
    
    # 支持的语言和对应的输出指令
    LANGUAGE_INSTRUCTIONS = {
        'zh': '请用中文回复。',
        'en': 'Please respond in English.',
        'es': 'Por favor responde en español.',
        'de': 'Bitte antworte auf Deutsch.',
        'ja': '日本語で回答してください。',
        'ko': '한국어로 답변해 주세요.',
        'fr': 'Veuillez répondre en français.',
        'ar': 'يرجى الرد باللغة العربية.',
        'it': 'Per favore rispondi in italiano.',
        'da': 'Svar venligst på dansk.',
        'pt': 'Por favor, responda em português.',
    }
    
    def __init__(self):
        self._router = get_layered_router()
        self._toon = TOONSerializer()
        self._snippet_service = get_snippet_service()
    
    async def generate(
        self,
        scenario: ScenarioType,
        fusion_result: FusionResult,
        user_context: Optional[Dict[str, Any]] = None,
        extra_context: Optional[str] = None,
        language: str = "zh",
        raw_factors: Optional[Dict[str, Any]] = None,
        user_insights: Optional[List[Any]] = None,
    ) -> OrchestratorResult:
        """
        生成内容
        
        Args:
            scenario: 场景类型
            fusion_result: 融合结果（包含因子和规则匹配）
            user_context: 用户上下文（如姓名、偏好等）
            extra_context: 额外上下文（如梦境原文）
            language: 输出语言
            raw_factors: 原始 Factors 对象 (BaziFactors, AstroFactors 等)
            user_insights: 用户历史洞察列表
            
        Returns:
            OrchestratorResult
        """
        config = SCENARIO_CONFIGS.get(scenario)
        if not config:
            raise ValueError(f"Unknown scenario: {scenario}")
        
        # 1. TOON 序列化 (v2 包含原始盘面数据)
        if raw_factors:
            toon_context = self._toon.serialize_full_v2(
                fusion=fusion_result,
                raw_factors=raw_factors,
                insights=user_insights,
            )
        else:
            toon_context = self._toon.serialize_fusion(fusion_result)
        
        # 2. 获取匹配的 NarrativeSnippet
        factors = self._extract_factors(fusion_result)
        snippets = self._snippet_service.find_by_factors(factors, max_results=10)
        snippets_text = self._snippet_service.format_for_prompt(snippets)
        
        # 3. 构建 Prompt（带语言指令）
        base_system_prompt = SYSTEM_PROMPTS.get(config.system_prompt_key, "")
        lang_instruction = self.LANGUAGE_INSTRUCTIONS.get(language, self.LANGUAGE_INSTRUCTIONS['en'])
        system_prompt = f"{base_system_prompt}\n\n**输出语言**: {lang_instruction}"
        user_prompt = self._build_user_prompt(
            toon_context=toon_context,
            snippets_text=snippets_text,
            fusion_result=fusion_result,
            user_context=user_context,
            extra_context=extra_context,
            raw_factors=raw_factors,
            user_insights=user_insights,
            language=language,
        )
        
        # 4. 选择模型并调用
        provider, model = self._router.select(config.layer)
        if not provider:
            return self._fallback_result(scenario, toon_context, len(snippets))
        
        request = LLMRequest(
            prompt=user_prompt,
            system_prompt=system_prompt,
            model=model,
            max_tokens=config.max_tokens,
            temperature=config.temperature,
        )
        
        try:
            response = await provider.complete(request)
            
            self._router.record_tokens(config.layer, response.usage.total_tokens)
            
            logger.info(
                f"Orchestrator generated {scenario.value}: "
                f"model={response.model_used}, "
                f"tokens={response.usage.total_tokens}, "
                f"latency={response.latency_ms:.1f}ms"
            )
            
            return OrchestratorResult(
                content=response.content,
                scenario=scenario,
                model_used=response.model_used,
                tokens_used=response.usage.total_tokens,
                latency_ms=response.latency_ms,
                toon_context=toon_context,
                snippets_count=len(snippets),
            )
        
        except Exception as e:
            logger.error(f"Orchestrator failed for {scenario.value}: {e}")
            return self._fallback_result(scenario, toon_context, len(snippets))
    
    def _extract_factors(self, fusion_result: FusionResult) -> List[str]:
        """从融合结果中提取因子"""
        factors = set()
        for evidence in fusion_result.evidence_chain[:10]:
            if evidence.evidence_factors:
                factors.update(evidence.evidence_factors)
        return list(factors)
    
    def _build_user_prompt(
        self,
        toon_context: str,
        snippets_text: str,
        fusion_result: FusionResult,
        user_context: Optional[Dict[str, Any]],
        extra_context: Optional[str],
        raw_factors: Optional[Dict[str, Any]] = None,
        user_insights: Optional[List[Any]] = None,
        language: str = "zh",
    ) -> str:
        """
        构建用户 Prompt - 增强版 (支持原始盘面数据)
        
        WP-01: 强制 ≤4000 字符，采用优先级截断策略
        """
        from datetime import datetime
        
        # 构建各部分内容
        sections = {}
        
        # 1. 时间上下文（优先级最高，不截断）
        now = datetime.now()
        header_parts = [
            "## 时间信息",
            f"- 日期: {now.strftime('%Y年%m月%d日')} ({['周一','周二','周三','周四','周五','周六','周日'][now.weekday()]})",
            f"- 时间: {now.strftime('%H:%M')}",
            "",
        ]
        sections["header"] = "\n".join(header_parts)
        
        # 2. 原始盘面数据（核心，按预算截断）
        profile_parts = []
        if raw_factors:
            for engine_id, factors in raw_factors.items():
                profile_text = self._format_factors_profile(engine_id, factors, language)
                if profile_text:
                    profile_parts.append(profile_text)
                    profile_parts.append("")
        sections["profile"] = "\n".join(profile_parts) if profile_parts else ""
        
        # 3. 规则分析结果
        rules_parts = ["## 规则分析结果"]
        if fusion_result.primary_themes:
            rules_parts.append(f"**当前主题**: {' | '.join(fusion_result.primary_themes[:5])}")
        if fusion_result.evidence_chain:
            rules_parts.append("**核心规则**:")
            for i, ev in enumerate(fusion_result.evidence_chain[:5]):
                if ev.matched and ev.description:
                    conf_pct = int(ev.confidence * 100) if ev.confidence else 0
                    rules_parts.append(f"  {i+1}. {ev.description} (置信度:{conf_pct}%)")
        rules_parts.append(f"**交叉验证分数**: {fusion_result.cross_validation_score:.2f}")
        if fusion_result.conflicts:
            rules_parts.append(f"**存在冲突**: {len(fusion_result.conflicts)}处")
        rules_parts.append("")
        sections["rules"] = "\n".join(rules_parts)
        
        # 4. 用户历史洞察（按条目截断）
        insights_parts = []
        if user_insights:
            insights_parts.append("## 用户历史洞察")
            for insight in user_insights[:5]:  # 最多5条，与 TOON INS 对齐
                dimension = getattr(insight, 'dimension', 'unknown')
                summary = getattr(insight, 'summary', '')
                strength = getattr(insight, 'strength', 0.0)
                insights_parts.append(f"- **{dimension}**: {summary} (置信度 {strength:.0%})")
            insights_parts.append("")
        sections["insights"] = "\n".join(insights_parts) if insights_parts else ""
        
        # 5. 典籍素材
        snippets_parts = [
            "## 可引用的典籍素材",
            snippets_text if snippets_text else "(暂无直接匹配的素材，请基于规则结果生成)",
            "",
        ]
        sections["snippets"] = "\n".join(snippets_parts)
        
        # 6. 用户/额外上下文
        context_parts = []
        if user_context:
            context_parts.append("## 用户信息")
            for key, value in user_context.items():
                if key != "user_id":
                    context_parts.append(f"- {key}: {value}")
            context_parts.append("")
        if extra_context:
            context_parts.append("## 补充信息")
            context_parts.append(extra_context)
            context_parts.append("")
        sections["context"] = "\n".join(context_parts) if context_parts else ""
        
        # 7. 结尾指令
        sections["footer"] = "---\n请根据以上信息，按照系统提示中的输出格式生成内容。"
        
        # WP-01: 强制截断逻辑
        return self._truncate_prompt_to_limit(sections)
    
    def _truncate_prompt_to_limit(self, sections: Dict[str, str]) -> str:
        """
        WP-01: 强制截断 User Prompt 到 ≤4000 字符
        
        截断优先级（从低到高，先截断低优先级）：
        1. context（用户/额外上下文）
        2. snippets（典籍素材）
        3. insights（用户洞察）
        4. rules（规则分析）
        5. profile（盘面数据）
        6. header/footer（不截断）
        """
        # 优先级顺序（越靠后优先级越高，越不容易被截断）
        truncation_order = ["context", "snippets", "insights", "rules", "profile"]
        
        # 计算初始长度
        def calc_total() -> int:
            return sum(len(s) for s in sections.values()) + len(sections) - 1  # 换行符
        
        original_length = calc_total()
        
        # 如果未超限，直接返回
        if original_length <= MAX_USER_PROMPT_LENGTH:
            return self._assemble_prompt(sections)
        
        # 需要截断
        logger.warning(
            f"User prompt exceeds limit: {original_length} > {MAX_USER_PROMPT_LENGTH}, "
            f"starting truncation"
        )
        
        # 按优先级逐个截断
        for section_key in truncation_order:
            if calc_total() <= MAX_USER_PROMPT_LENGTH:
                break
            
            section_content = sections[section_key]
            if not section_content:
                continue
            
            budget = PROMPT_BUDGET.get(section_key, 500)
            if len(section_content) > budget:
                # 截断该部分
                truncated = self._truncate_section(section_key, section_content, budget)
                sections[section_key] = truncated
                logger.info(
                    f"Truncated section '{section_key}': {len(section_content)} -> {len(truncated)}"
                )
        
        # 最终检查：如果仍然超限，强制裁剪（保留结构）
        final_length = calc_total()
        if final_length > MAX_USER_PROMPT_LENGTH:
            # 最后手段：按比例压缩所有可截断部分
            overflow = final_length - MAX_USER_PROMPT_LENGTH
            for section_key in truncation_order:
                if overflow <= 0:
                    break
                section_content = sections[section_key]
                if section_content and len(section_content) > 100:
                    cut = min(overflow, len(section_content) - 100)
                    sections[section_key] = section_content[:len(section_content) - cut - 20] + "\n...(已截断)"
                    overflow -= cut
                    logger.warning(f"Force-truncated section '{section_key}' by {cut} chars")
        
        final_prompt = self._assemble_prompt(sections)
        logger.info(
            f"User prompt truncated: {original_length} -> {len(final_prompt)} "
            f"(limit: {MAX_USER_PROMPT_LENGTH})"
        )
        
        return final_prompt
    
    def _truncate_section(self, section_key: str, content: str, budget: int) -> str:
        """按部分类型执行智能截断"""
        if len(content) <= budget:
            return content
        
        lines = content.split("\n")
        
        if section_key == "insights":
            # 洞察：保留标题 + 前N条
            if lines and lines[0].startswith("##"):
                header = lines[0]
                items = [l for l in lines[1:] if l.strip().startswith("- ")]
                # 计算能保留几条
                result = [header]
                current_len = len(header)
                for item in items:
                    if current_len + len(item) + 1 < budget - 20:
                        result.append(item)
                        current_len += len(item) + 1
                    else:
                        break
                if len(items) > len(result) - 1:
                    result.append(f"...(已截断 {len(items) - len(result) + 1} 条洞察)")
                return "\n".join(result)
        
        elif section_key == "snippets":
            # 素材：保留标题 + 截断正文
            if lines and lines[0].startswith("##"):
                header = lines[0]
                body = "\n".join(lines[1:])
                max_body = budget - len(header) - 30
                if len(body) > max_body:
                    body = body[:max_body] + "...(素材已截断)"
                return header + "\n" + body
        
        elif section_key == "profile":
            # 盘面：保留每个引擎的核心字段
            if lines and lines[0].startswith("##"):
                header = lines[0]
                body_lines = lines[1:]
                result = [header]
                current_len = len(header)
                for line in body_lines:
                    if current_len + len(line) + 1 < budget - 20:
                        result.append(line)
                        current_len += len(line) + 1
                    else:
                        result.append("...(盘面数据已截断)")
                        break
                return "\n".join(result)
        
        # 默认：简单截断
        return content[:budget - 15] + "\n...(已截断)"
    
    def _assemble_prompt(self, sections: Dict[str, str]) -> str:
        """按顺序组装最终 Prompt"""
        order = ["header", "profile", "rules", "insights", "snippets", "context", "footer"]
        parts = [sections.get(k, "") for k in order if sections.get(k)]
        return "\n".join(parts)
    
    def _format_factors_profile(
        self,
        engine_id: str,
        factors: Any,
        language: str = "zh",
    ) -> Optional[str]:
        """格式化原始盘面数据为人类可读格式"""
        try:
            if engine_id == "bazi-calculator":
                return self._format_bazi_profile(factors, language)
            elif engine_id == "astro-calculator":
                return self._format_astro_profile(factors, language)
            elif engine_id == "dream-extractor":
                return self._format_dream_profile(factors, language)
            elif engine_id == "tarot-interpreter":
                return self._format_tarot_profile(factors, language)
            elif engine_id == "ziwei-calculator":
                return self._format_ziwei_profile(factors, language)
            elif engine_id == "yijing-calculator":
                return self._format_yijing_profile(factors, language)
        except Exception as e:
            logger.warning(f"Failed to format {engine_id} profile: {e}")
        return None
    
    def _format_bazi_profile(self, factors: Any, language: str) -> str:
        """格式化八字盘面"""
        p = factors.four_pillars
        
        if language == "zh":
            # 四柱
            pillars = (f"{p['year']['stem']}{p['year']['branch']}年 "
                      f"{p['month']['stem']}{p['month']['branch']}月 "
                      f"{p['day']['stem']}{p['day']['branch']}日 "
                      f"{p['hour']['stem']}{p['hour']['branch']}时")
            
            # 五行中文映射
            element_cn = {"wood": "木", "fire": "火", "earth": "土", 
                         "metal": "金", "water": "水"}
            yinyang_cn = {"yin": "阴", "yang": "阳"}
            strength_cn = {"strong": "身强", "weak": "身弱", "neutral": "中和"}
            
            day_master_desc = (f"{factors.day_master}"
                              f"{element_cn.get(factors.day_master_element, '')} "
                              f"({yinyang_cn.get(factors.day_master_yinyang, '')}"
                              f"{element_cn.get(factors.day_master_element, '')})")
            
            # 十神
            ten_gods_str = " ".join([
                f"{god}{count}" for god, count in factors.ten_god_counts.items() 
                if count > 0
            ])
            
            # 大运
            dayun_str = ""
            if factors.dayun_list and len(factors.dayun_list) > 1:
                cd = factors.dayun_list[1]
                dayun_str = f"{cd['stem']}{cd['branch']}大运 ({cd['start_age']}-{cd['end_age']}岁)"
            
            # 季节中文
            season_cn = {"spring": "春季", "summer": "夏季", 
                        "autumn": "秋季", "winter": "冬季"}
            
            return f"""## 八字命盘

- **八字四柱**: {pillars}
- **日主**: {day_master_desc}
- **身强弱**: {strength_cn.get(factors.strength_category, factors.strength_category)} (强度 {factors.day_master_strength:.0%})
- **出生季节**: {season_cn.get(factors.birth_season, factors.birth_season)}
- **十神分布**: {ten_gods_str}
- **当前大运**: {dayun_str}"""
        else:
            return f"""## Bazi Chart

- **Four Pillars**: {p['year']['stem']}{p['year']['branch']} {p['month']['stem']}{p['month']['branch']} {p['day']['stem']}{p['day']['branch']} {p['hour']['stem']}{p['hour']['branch']}
- **Day Master**: {factors.day_master} ({factors.day_master_element}, {factors.day_master_yinyang})
- **Strength**: {factors.strength_category} ({factors.day_master_strength:.0%})"""
    
    def _format_astro_profile(self, factors: Any, language: str) -> str:
        """格式化占星盘面"""
        sign_cn = {
            "aries": "白羊座", "taurus": "金牛座", "gemini": "双子座",
            "cancer": "巨蟹座", "leo": "狮子座", "virgo": "处女座",
            "libra": "天秤座", "scorpio": "天蝎座", "sagittarius": "射手座",
            "capricorn": "摩羯座", "aquarius": "水瓶座", "pisces": "双鱼座"
        }
        
        if language == "zh":
            lines = ["## 星盘配置", ""]
            
            if hasattr(factors, 'planets'):
                if 'sun' in factors.planets:
                    sun = factors.planets['sun']
                    lines.append(f"- **太阳**: {sign_cn.get(sun.sign, sun.sign)} (第{sun.house}宫 {sun.degree_in_sign:.1f}°)")
                if 'moon' in factors.planets:
                    moon = factors.planets['moon']
                    lines.append(f"- **月亮**: {sign_cn.get(moon.sign, moon.sign)} (第{moon.house}宫 {moon.degree_in_sign:.1f}°)")
            
            if hasattr(factors, 'ascendant_sign'):
                lines.append(f"- **上升点**: {sign_cn.get(factors.ascendant_sign, factors.ascendant_sign)}")
            if hasattr(factors, 'midheaven_sign'):
                lines.append(f"- **中天**: {sign_cn.get(factors.midheaven_sign, factors.midheaven_sign)}")
            
            return "\n".join(lines)
        else:
            return "## Natal Chart\n\n(Astro profile in English)"
    
    def _format_dream_profile(self, factors: Any, language: str) -> str:
        """格式化解梦分析"""
        if language == "zh":
            lines = ["## 梦境分析", ""]
            
            if hasattr(factors, 'symbols') and factors.symbols:
                sym_strs = [s.symbol for s in factors.symbols[:5] if hasattr(s, 'symbol')]
                lines.append(f"- **识别符号**: {', '.join(sym_strs)}")
            
            if hasattr(factors, 'themes') and factors.themes:
                lines.append(f"- **梦境主题**: {', '.join(factors.themes)}")
            
            if hasattr(factors, 'emotions') and factors.emotions:
                lines.append(f"- **情绪基调**: {', '.join(factors.emotions)}")
            
            return "\n".join(lines)
        else:
            return "## Dream Analysis\n\n(Dream profile in English)"
    
    def _format_tarot_profile(self, factors: Any, language: str) -> str:
        """格式化塔罗牌阵"""
        spread_cn = {"single": "单牌", "three_card": "三牌阵", "celtic_cross": "凯尔特十字"}
        
        if language == "zh":
            lines = ["## 塔罗牌阵", ""]
            
            if hasattr(factors, 'spread_type'):
                lines.append(f"- **牌阵类型**: {spread_cn.get(factors.spread_type, factors.spread_type)}")
            
            if hasattr(factors, 'cards'):
                for card in factors.cards[:5]:
                    name = getattr(card, 'card_name', str(card))
                    is_reversed = getattr(card, 'reversed', False)
                    orientation = "逆位" if is_reversed else "正位"
                    position = getattr(card, 'position', '')
                    lines.append(f"- **{position}位**: {name} ({orientation})")
            
            if hasattr(factors, 'question') and factors.question:
                lines.append(f"- **问题**: {factors.question}")
            
            return "\n".join(lines)
        else:
            return "## Tarot Spread\n\n(Tarot profile in English)"
    
    def _format_ziwei_profile(self, factors: Any, language: str) -> str:
        """格式化紫微盘面"""
        if language == "zh":
            lines = ["## 紫微斗数盘面", ""]
            
            # 命宫
            if hasattr(factors, 'ming_palace_branch'):
                branch = factors.ming_palace_branch
                main_stars = ""
                if hasattr(factors, 'palaces') and '命宫' in factors.palaces:
                    palace = factors.palaces['命宫']
                    if palace.get('main_stars'):
                        main_stars = '、'.join(palace['main_stars'][:2])
                lines.append(f"- **命宫**: {branch}宫 ({main_stars})")
            
            # 身宫
            if hasattr(factors, 'body_palace_name'):
                lines.append(f"- **身宫**: {factors.body_palace_name}")
            
            # 五行局
            if hasattr(factors, 'five_element_type'):
                lines.append(f"- **五行局**: {factors.five_element_type}")
            
            # 四化
            if hasattr(factors, 'sihua_natal') and factors.sihua_natal:
                sihua_str = ' '.join([f"{k}{v}" for k, v in factors.sihua_natal.items()])
                lines.append(f"- **四化**: {sihua_str}")
            
            # 当前大限
            if hasattr(factors, 'current_decade') and factors.current_decade:
                cd = factors.current_decade
                lines.append(f"- **当前大限**: {cd.get('palace_name', '')}宫 ({cd.get('start_age', '')}-{cd.get('end_age', '')}岁)")
            
            return "\n".join(lines)
        else:
            return "## Ziwei Doushu Chart\n\n(Ziwei profile in English)"
    
    def _format_yijing_profile(self, factors: Any, language: str) -> str:
        """格式化易经卦象"""
        if language == "zh":
            lines = ["## 易经卦象", ""]
            
            # 主卦
            if hasattr(factors, 'main_hexagram') and factors.main_hexagram:
                hex = factors.main_hexagram
                name = getattr(hex, 'name_zh', '')
                number = getattr(hex, 'number', 0)
                lines.append(f"- **主卦**: {name}卦 (第{number}卦)")
            
            # 上下卦
            if hasattr(factors, 'main_hexagram') and factors.main_hexagram:
                hex = factors.main_hexagram
                upper = getattr(hex, 'upper_trigram', '')
                lower = getattr(hex, 'lower_trigram', '')
                if upper and lower:
                    lines.append(f"- **上下卦**: 上{upper}下{lower}")
            
            # 动爻
            if hasattr(factors, 'moving_lines') and factors.moving_lines:
                lines.append(f"- **动爻**: {'、'.join(str(m)+'爻' for m in factors.moving_lines)}")
            
            # 变卦
            if hasattr(factors, 'changed_hexagram') and factors.changed_hexagram:
                chg = factors.changed_hexagram
                lines.append(f"- **变卦**: {getattr(chg, 'name_zh', '')}卦")
            
            # 互卦
            if hasattr(factors, 'mutual_hexagram') and factors.mutual_hexagram:
                mut = factors.mutual_hexagram
                lines.append(f"- **互卦**: {getattr(mut, 'name_zh', '')}卦")
            
            # 起卦法
            if hasattr(factors, 'divination_method'):
                method_cn = {
                    "coin": "铜钱法", "yarrow": "蓍草法", 
                    "manual": "手动输入", "time": "时间起卦"
                }
                lines.append(f"- **起卦法**: {method_cn.get(factors.divination_method, factors.divination_method)}")
            
            return "\n".join(lines)
        else:
            return "## I Ching Hexagram\n\n(Yijing profile in English)"
    
    def _fallback_result(
        self,
        scenario: ScenarioType,
        toon_context: str,
        snippets_count: int,
    ) -> OrchestratorResult:
        """降级结果"""
        return OrchestratorResult(
            content="[系统繁忙，请稍后重试]",
            scenario=scenario,
            model_used="fallback",
            tokens_used=0,
            latency_ms=0,
            toon_context=toon_context,
            snippets_count=snippets_count,
        )


# 便捷函数
_orchestrator: Optional[LLMOrchestrator] = None


def get_orchestrator() -> LLMOrchestrator:
    """获取编排器单例"""
    global _orchestrator
    if _orchestrator is None:
        _orchestrator = LLMOrchestrator()
    return _orchestrator
