"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.424351
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
    semantic_id="dvd_v1.0.0_banquet_宴席_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Banquet宴席(SemanticEntry):
    """
    ### Source Text

> Banquet = blessing, abundance, unmerited favor. **Positive**: Lord's table, desir...
    """
    
    original_text: str = """### Source Text

> Banquet = blessing, abundance, unmerited favor. **Positive**: Lord's table, desires provided beyond needs (Ps 23:5; Song 2:4). **Negative**: Gluttony, excess, evil intentions.

### English Paraphrase

Banquet = favor. **Positive**: Abundance, royalty, seat of honor. **Negative**: Gluttony, excess.

### Chinese Interpretation（完整对等诠释）

宴席 = 恩惠。**正面**：丰盛、皇家待遇、尊位。**负面**：贪食、过度。

### Narrative Snippets

- `[ns_dav_b015]` `[trigger: 梦宴席]` `[factor_trigger: dream_symbol_banquet]` `[role: 主干]` Banquet = Lord's favor and abundance—blessing or gluttony. → Dreams Dictionary #Banquet"""
    normalized_text_zh: str = """"""
    subject: str = "Banquet 宴席"
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
        l1_anchor="dvd_v1.0.0_banquet_宴席_001_L1",
    )
    version: str = "1.0.0"
