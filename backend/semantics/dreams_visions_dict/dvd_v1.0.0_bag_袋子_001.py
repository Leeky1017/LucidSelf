"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.424293
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
    semantic_id="dvd_v1.0.0_bag_袋子_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Bag袋子(SemanticEntry):
    """
    ### Source Text

> Bag = finance and provision. **Positive**: Full bag = provision, David's shepherd...
    """
    
    original_text: str = """### Source Text

> Bag = finance and provision. **Positive**: Full bag = provision, David's shepherd bag. **Negative**: Bag with holes = financial loss, curse (Haggai 1:6).

### English Paraphrase

Bag = finance. **Positive**: Full = provision. **Negative**: Holes = financial curse, money slipping through fingers.

### Chinese Interpretation（完整对等诠释）

袋子 = 财务。**正面**：满 = 供应。**负面**：有洞 = 财务咒诅，钱财从指缝溜走。

### Narrative Snippets

- `[ns_dav_b007]` `[trigger: 梦袋子]` `[factor_trigger: dream_symbol_bag]` `[role: 主干]` Bag = finance—full = blessing, holes = curse and loss. → Dreams Dictionary #Bag
- `[ns_dav_b008]` `[trigger: 破洞袋子]` `[factor_trigger: dream_symbol_bag AND bag_condition]` `[role: 条件分支]` Bag with holes = generational financial curse. → Dreams Dictionary #Bag"""
    normalized_text_zh: str = """"""
    subject: str = "Bag 袋子"
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
        l1_anchor="dvd_v1.0.0_bag_袋子_001_L1",
    )
    version: str = "1.0.0"
