"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.424504
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
    semantic_id="dvd_v1.0.0_bear_熊_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Bear熊(SemanticEntry):
    """
    ### Source Text

> Bear = generally negative, destruction. **Positive**: Protects young (2 Sam 17:8)...
    """
    
    original_text: str = """### Source Text

> Bear = generally negative, destruction. **Positive**: Protects young (2 Sam 17:8). **Negative**: Curse, devouring, destruction (2 Kgs 2:24).

### English Paraphrase

Bear = destruction. **Positive (rare)**: Protective mother. **Negative**: Curse, attack, devouring.

### Chinese Interpretation（完整对等诠释）

熊 = 毁灭。**正面（罕见）**：保护幼崽的母亲。**负面**：咒诅、攻击、吞噬。

### Narrative Snippets

- `[ns_dav_b028]` `[trigger: 梦熊]` `[factor_trigger: dream_symbol_bear]` `[role: 主干]` Bear = destruction—rarely protective, usually curse/attack. → Dreams Dictionary #Bear"""
    normalized_text_zh: str = """"""
    subject: str = "Bear 熊"
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
        l1_anchor="dvd_v1.0.0_bear_熊_001_L1",
    )
    version: str = "1.0.0"
