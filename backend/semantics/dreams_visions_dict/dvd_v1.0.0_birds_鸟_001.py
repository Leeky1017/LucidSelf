"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.424584
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
    semantic_id="dvd_v1.0.0_birds_鸟_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Birds鸟(SemanticEntry):
    """
    ### Source Text

> Birds = **Positive**: Joy, freedom, new season (Song 2:12; Matt 6:26). Eagle = Ho...
    """
    
    original_text: str = """### Source Text

> Birds = **Positive**: Joy, freedom, new season (Song 2:12; Matt 6:26). Eagle = Holy Spirit. **Negative**: Black birds = demonic attack, carnivorous = destruction (Ezek 39:4).

### English Paraphrase

Birds = **Positive**: Joy, spring, freedom. Eagle = Holy Spirit. **Negative**: Black/carnivorous = demonic.

### Chinese Interpretation（完整对等诠释）

鸟 = **正面**：喜乐、春天、自由。鹰 = 圣灵。**负面**：黑鸟/食肉 = 魔鬼的。

### Narrative Snippets

- `[ns_dav_b034]` `[trigger: 梦鸟]` `[factor_trigger: dream_symbol_birds]` `[role: 主干]` Birds = joy/freedom or demonic—type determines meaning. → Dreams Dictionary #Birds"""
    normalized_text_zh: str = """"""
    subject: str = "Birds 鸟"
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
        l1_anchor="dvd_v1.0.0_birds_鸟_001_L1",
    )
    version: str = "1.0.0"
