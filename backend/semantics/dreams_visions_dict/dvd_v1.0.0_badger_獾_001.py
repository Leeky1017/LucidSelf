"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.424284
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
    semantic_id="dvd_v1.0.0_badger_獾_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Badger獾(SemanticEntry):
    """
    ### Source Text

> Badger skin used for tabernacle covering. Speaks of wealth and prosperity. (Ezek ...
    """
    
    original_text: str = """### Source Text

> Badger skin used for tabernacle covering. Speaks of wealth and prosperity. (Ezek 16:10)

### English Paraphrase

Badger = wealth and prosperity. Biblical use: tabernacle covering. Associated with fine clothing, divine provision.

### Chinese Interpretation（完整对等诠释）

獾 = 财富和繁荣。圣经用途：会幕遮盖。与精美衣物、神圣供应相关。

### Narrative Snippets

- `[ns_dav_b006]` `[trigger: 梦獾]` `[factor_trigger: dream_symbol_badger]` `[role: 主干]` Badger = wealth and prosperity, tabernacle covering. → Dreams Dictionary #Badger"""
    normalized_text_zh: str = """"""
    subject: str = "Badger 獾"
    factor_refs: list = []
    
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
        book_id="dreams_visions_dict",
        chapter="",
        l1_anchor="dvd_v1.0.0_badger_獾_001_L1",
    )
    version: str = "1.0.0"
