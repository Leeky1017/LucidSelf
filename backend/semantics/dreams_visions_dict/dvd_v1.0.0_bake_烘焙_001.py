"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.424301
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
    semantic_id="dvd_v1.0.0_bake_烘焙_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Bake烘焙(SemanticEntry):
    """
    ### Source Text

> Baking = preparation for ministry. Raw dough = immature. Baked = ready. Must pass...
    """
    
    original_text: str = """### Source Text

> Baking = preparation for ministry. Raw dough = immature. Baked = ready. Must pass through fire. **Negative**: Unbaked = not following through (Hosea 7:4).

### English Paraphrase

Bake = ministry preparation. **Positive**: Baking = making ready. **Negative**: Unbaked = giving up, rejecting responsibility.

### Chinese Interpretation（完整对等诠释）

烘焙 = 事工预备。**正面**：烤 = 预备好。**负面**：未烤 = 放弃、拒绝责任。

### Narrative Snippets

- `[ns_dav_b009]` `[trigger: 梦烘焙]` `[factor_trigger: dream_symbol_bake]` `[role: 主干]` Bake = preparation for ministry—baking = ready, unbaked = giving up. → Dreams Dictionary #Bake"""
    normalized_text_zh: str = """"""
    subject: str = "Bake 烘焙"
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
        l1_anchor="dvd_v1.0.0_bake_烘焙_001_L1",
    )
    version: str = "1.0.0"
