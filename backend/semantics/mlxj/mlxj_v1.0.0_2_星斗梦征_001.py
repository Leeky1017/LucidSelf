"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.783965
Version: 1.0.0

对照 Requirements 6.4 - 带 @SemanticRegistry.register 装饰器的 Python 模块
"""

from backend.semantics.core.base import SemanticEntry, SemanticRegistry, NarrativeSnippetExtended
from backend.core.contracts import (
    SnippetRole,
    SourceMetadata,
    ConfigRelation,
    EvidenceChainEntry,
    RelationType,
    EffectDirection,
    ConfidenceLevel,
)


@SemanticRegistry.register(
    semantic_id="mlxj_v1.0.0_2_星斗梦征_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2星斗梦征(SemanticEntry):
    """
    | 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 宋 | 黄亢母 | 吞星 | 亢名显于宋代 |
| 元 | 黄溍母 | 怀星 | 溍业著于元...
    """
    
    original_text: str = """| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 宋 | 黄亢母 | 吞星 | 亢名显于宋代 |
| 元 | 黄溍母 | 怀星 | 溍业著于元朝 |
| 齐 | 高欢 | 步履星枢 | 显贵 |
| 唐 | 伍乔 | 名符星号 | 登进士 |"""
    normalized_text_zh: str = """"""
    subject: str = "2 星斗梦征"
    factor_refs: list = ['source_ref']
    
    # 叙事素材（包含 trigger_human）
    narrative_snippets: list = [

    ]
    
    # L2.5 因子关系
    related_semantics: list = [

    ]
    
    # L2.5 证据链
    evidence_refs: list = [

    ]
    
    metadata: SourceMetadata = SourceMetadata(
        book_id="mlxj",
        chapter="",
        l1_anchor="mlxj_v1.0.0_2_星斗梦征_001_L1",
    )
    version: str = "1.0.0"
