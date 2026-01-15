"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.424360
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
    semantic_id="dvd_v1.0.0_baptism_洗礼_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Baptism洗礼(SemanticEntry):
    """
    ### Source Text

> Baptism = leaving old behind, new life. **Positive**: Buried with Christ, raised ...
    """
    
    original_text: str = """### Source Text

> Baptism = leaving old behind, new life. **Positive**: Buried with Christ, raised in resurrection (Rom 6:4-5). **Negative**: Baptism unto death = death to flesh, painful Cross/Fire.

### English Paraphrase

Baptism = new life. **Positive**: Resurrection, pressing forward. **Negative**: Death to flesh, painful process.

### Chinese Interpretation（完整对等诠释）

洗礼 = 新生命。**正面**：复活、向前迈进。**负面**：向肉体死，痛苦过程。

### Narrative Snippets

- `[ns_dav_b016]` `[trigger: 梦洗礼]` `[factor_trigger: dream_symbol_baptism]` `[role: 主干]` Baptism = leaving old, walking in resurrection—new beginning. → Dreams Dictionary #Baptism"""
    normalized_text_zh: str = """"""
    subject: str = "Baptism 洗礼"
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
        l1_anchor="dvd_v1.0.0_baptism_洗礼_001_L1",
    )
    version: str = "1.0.0"
