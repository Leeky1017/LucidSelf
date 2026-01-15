"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.801341
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
    semantic_id="mlxj_v1.0.0_2_寝媞类_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2寝媞类(SemanticEntry):
    """
    #### 原文摘要

若梦中妻妾奴婢，抱挟枕边，是人之常，无足怪者。而动静词色，声音笑貌，或其家之所无，或己身所不与，或理所不当与而尝与处者，或事所宜然而身未尝若是者，或心之所慕而未尝及者，或向之所为...
    """
    
    original_text: str = """#### 原文摘要

若梦中妻妾奴婢，抱挟枕边，是人之常，无足怪者。而动静词色，声音笑貌，或其家之所无，或己身所不与，或理所不当与而尝与处者，或事所宜然而身未尝若是者，或心之所慕而未尝及者，或向之所为而今久弗为者。若是者皆当以其细推之。

凡梦与妒嫉处，梦与娼妓处，梦与姥妪处，梦与童子处，皆非吉兆，而梦与尼姑同寝，或亡过妖魂者，大凶。

#### 寝媾占断要点

| 梦象 | 吉凶 | 主应 |
|------|------|------|
| 梦妻妾奴婢 | 平 | 人之常 |
| 梦与妒嫉处 | 凶 | 非吉 |
| 梦与娼妓处 | 凶 | 非吉 |
| 梦与姥妪处 | 凶 | 非吉 |
| 梦与童子处 | 凶 | 非吉 |
| 梦与尼姑同寝 | 大凶 | - |
| 梦与亡魂妖魂 | 大凶 | - |"""
    normalized_text_zh: str = """"""
    subject: str = "2 寝媞类"
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
        l1_anchor="mlxj_v1.0.0_2_寝媞类_001_L1",
    )
    version: str = "1.0.0"
