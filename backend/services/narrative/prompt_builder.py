"""
Prompt Builder

构建 LLM Prompt。

对照 tasks.md 9.2:
- Requirements: 3.2.1-3.2.3
- ⚠️ 陷阱: prompt 太长会超 context window

设计原则:
- Token 预算控制
- TOON 压缩复用
- inline_sources 可追溯
"""

import logging
from typing import Dict, List, Optional

from backend.core.contracts import FusionResult, RuntimeRuleResult
from backend.core.llm.toon_serializer import TOONSerializer

logger = logging.getLogger(__name__)

# Lazy import to avoid circular dependency
_snippet_service = None

def _get_snippet_service():
    """延迟导入 snippet_service"""
    global _snippet_service
    if _snippet_service is None:
        from backend.services.narrative.snippet_service import get_snippet_service
        _snippet_service = get_snippet_service()
    return _snippet_service


class PromptBuilder:
    """
    Prompt 构建器
    
    功能:
    - 从 FusionResult 构建 prompt
    - TOON 压缩融合结果
    - 控制 Token 预算
    - 多语言支持
    
    ⚠️ 重要:
    - 必须控制 prompt 长度
    - 使用 TOON 压缩节省 token
    """
    
    # Token 预算 (估算)
    MAX_PROMPT_TOKENS = 3000
    MAX_TOON_TOKENS = 500
    MAX_CONTEXT_TOKENS = 1000
    
    # System Prompt 模板
    SYSTEM_PROMPTS = {
        "zh": """你是一位专业的命理分析师，基于提供的分析数据生成解读报告。

要求:
1. 语言风格专业但易懂
2. 结构清晰，分点阐述
3. 只基于提供的数据进行解读，不要编造
4. 如有不确定性，请明确指出
5. 结尾可以提供建议，但要标注"仅供参考"

输出格式:
- 总体概述 (1-2段)
- 分维度解读 (事业/财富/感情/健康)
- 建议与提醒""",
        "en": """You are a professional analyst generating interpretation reports based on provided analysis data.

Requirements:
1. Professional but accessible language
2. Clear structure with bullet points
3. Only interpret based on provided data, do not fabricate
4. Clearly indicate any uncertainties
5. Provide advice at the end, but note "for reference only"

Output format:
- Overall Summary (1-2 paragraphs)
- Dimension-specific Analysis (career/wealth/relationships/health)
- Suggestions and Reminders""",
    }
    
    # User Prompt 模板 - 包含 TOON 和 NarrativeSnippet
    USER_PROMPT_TEMPLATES = {
        "zh": """请基于以下分析数据生成解读报告:

## 融合分析结果 (TOON格式)
{toon_data}

## 精校典籍素材 (请优先使用这些素材组织叙事)
{narrative_snippets}

## 主要主题
{themes}

## 交叉验证分数
{cross_validation_score:.2f}

## 用户问题 (如有)
{question}

请生成详细的解读报告。要求:
1. 优先使用"精校典籍素材"中的表述
2. 在关键结论处注明典籍来源
3. 不要编造典籍中不存在的内容""",
        "en": """Please generate an interpretation report based on the following analysis data:

## Fusion Analysis Results (TOON format)
{toon_data}

## Reference Texts from Classics (prioritize these in your narrative)
{narrative_snippets}

## Main Themes
{themes}

## Cross-Validation Score
{cross_validation_score:.2f}

## User Question (if any)
{question}

Please generate a detailed interpretation report. Requirements:
1. Prioritize using the "Reference Texts from Classics"
2. Cite classical sources for key conclusions
3. Do not fabricate content not present in the classics""",
    }
    
    def __init__(self, language: str = "zh"):
        """
        初始化 Prompt 构建器
        
        Args:
            language: 语言 ("zh" 或 "en")
        """
        self.language = language
        self._toon_serializer = TOONSerializer()
    
    def build(
        self,
        fusion_result: FusionResult,
        question: Optional[str] = None,
        max_tokens: Optional[int] = None,
    ) -> Dict[str, str]:
        """
        构建 Prompt
        
        Args:
            fusion_result: 融合结果
            question: 用户问题
            max_tokens: 最大 token 数
            
        Returns:
            {"system_prompt": ..., "user_prompt": ...}
        """
        max_tokens = max_tokens or self.MAX_PROMPT_TOKENS
        
        # 1. 序列化 FusionResult 为 TOON
        toon_data = self._toon_serializer.serialize_fusion(fusion_result)
        
        # 2. 检查长度，必要时截断
        if len(toon_data) > self.MAX_TOON_TOKENS * 4:  # 估算 4 字符/token
            logger.warning(
                "TOON data too long (%d chars), truncating",
                len(toon_data),
            )
            toon_data = toon_data[:self.MAX_TOON_TOKENS * 4]
        
        # 3. 准备主题
        themes = "\n".join(f"- {t}" for t in fusion_result.primary_themes)
        
        # 4. 获取 NarrativeSnippets (基于证据链中的因子)
        narrative_snippets = self._get_narrative_snippets(fusion_result)
        
        # 5. 构建 user prompt
        user_template = self.USER_PROMPT_TEMPLATES.get(
            self.language,
            self.USER_PROMPT_TEMPLATES["en"],
        )
        
        user_prompt = user_template.format(
            toon_data=toon_data,
            narrative_snippets=narrative_snippets,
            themes=themes,
            cross_validation_score=fusion_result.cross_validation_score,
            question=question or "无" if self.language == "zh" else "None",
        )
        
        # 6. 获取 system prompt
        system_prompt = self.SYSTEM_PROMPTS.get(
            self.language,
            self.SYSTEM_PROMPTS["en"],
        )
        
        return {
            "system_prompt": system_prompt,
            "user_prompt": user_prompt,
        }
    
    def _get_narrative_snippets(
        self,
        fusion_result: FusionResult,
        max_snippets: int = 8,
    ) -> str:
        """
        从证据链中提取因子，查询匹配的叙事素材
        
        Args:
            fusion_result: 融合结果
            max_snippets: 最大素材数量
            
        Returns:
            格式化的叙事素材字符串
        """
        try:
            snippet_service = _get_snippet_service()
        except Exception as e:
            logger.warning(f"Failed to get snippet service: {e}")
            return "(暂无精校素材)" if self.language == "zh" else "(No reference texts available)"
        
        # 从证据链中收集因子
        factors = set()
        for evidence in fusion_result.evidence_chain[:10]:  # 限制处理数量
            if evidence.evidence_factors:
                factors.update(evidence.evidence_factors)
        
        if not factors:
            return "(暂无匹配素材)" if self.language == "zh" else "(No matching texts)"
        
        # 查询匹配的素材
        snippets = snippet_service.find_by_factors(
            list(factors),
            max_results=max_snippets,
        )
        
        if not snippets:
            return "(暂无匹配素材)" if self.language == "zh" else "(No matching texts)"
        
        # 格式化
        return snippet_service.format_for_prompt(snippets, include_source=True)
    
    def estimate_tokens(self, text: str) -> int:
        """
        估算 token 数
        
        简单估算：中文约 2 字符/token，英文约 4 字符/token
        """
        if not text:
            return 0
        
        chinese_chars = sum(1 for c in text if '\u4e00' <= c <= '\u9fff')
        other_chars = len(text) - chinese_chars
        
        return (chinese_chars // 2) + (other_chars // 4) + 1
    
    def build_with_context(
        self,
        fusion_result: FusionResult,
        context: str,
        question: Optional[str] = None,
    ) -> Dict[str, str]:
        """
        带上下文构建 Prompt
        
        Args:
            fusion_result: 融合结果
            context: 上下文信息 (如历史对话)
            question: 用户问题
            
        Returns:
            {"system_prompt": ..., "user_prompt": ...}
        """
        base = self.build(fusion_result, question)
        
        # 添加上下文，但控制长度
        if context:
            context_tokens = self.estimate_tokens(context)
            if context_tokens > self.MAX_CONTEXT_TOKENS:
                logger.warning(
                    "Context too long (%d tokens), truncating",
                    context_tokens,
                )
                # 保留最后部分
                target_chars = self.MAX_CONTEXT_TOKENS * 3  # 估算
                context = "..." + context[-target_chars:]
            
            context_header = (
                "\n\n## 历史上下文\n" if self.language == "zh" 
                else "\n\n## Historical Context\n"
            )
            base["user_prompt"] = base["user_prompt"] + context_header + context
        
        return base
