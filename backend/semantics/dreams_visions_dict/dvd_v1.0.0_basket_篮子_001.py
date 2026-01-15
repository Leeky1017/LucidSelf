"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.424425
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
    semantic_id="dvd_v1.0.0_basket_篮子_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Basket篮子(SemanticEntry):
    """
    ### Source Text

> Basket = financial blessing. **Positive**: Full = blessing (Deut 28:5; Phil 4:19)...
    """
    
    original_text: str = """### Source Text

> Basket = financial blessing. **Positive**: Full = blessing (Deut 28:5; Phil 4:19). **Negative**: Empty = lack, curse (Deut 28:17).

### English Paraphrase

Basket = provision. **Positive**: Full = blessing. **Negative**: Empty/rotten = curse.

### Chinese Interpretation（完整对等诠释）

篮子 = 供应。**正面**：满 = 祝福。**负面**：空/腐烂 = 咒诅。

### Narrative Snippets

- `[ns_dav_b024]` `[trigger: 梦篮子]` `[factor_trigger: dream_symbol_basket]` `[role: 主干]` Basket = financial provision—full = blessing, empty = curse. → Dreams Dictionary #Basket"""
    normalized_text_zh: str = """"""
    subject: str = "Basket 篮子"
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
        l1_anchor="dvd_v1.0.0_basket_篮子_001_L1",
    )
    version: str = "1.0.0"
