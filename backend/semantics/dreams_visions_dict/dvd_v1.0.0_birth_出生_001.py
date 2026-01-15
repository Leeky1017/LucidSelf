"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.424597
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
    semantic_id="dvd_v1.0.0_birth_出生_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Birth出生(SemanticEntry):
    """
    ### Source Text

> Birth = new thing emerging. **Positive**: Season of preparation ended, walking in...
    """
    
    original_text: str = """### Source Text

> Birth = new thing emerging. **Positive**: Season of preparation ended, walking into calling (Gal 4:19). Painless = easy entry. **Negative**: Deformed/unclean birth = from sin (Ps 7:14; Jas 1:15). Premature = ran ahead of Lord.

### English Paraphrase

Birth = new emergence. **Positive**: Preparation ended, calling ready. **Negative**: Deformed = sin-conceived.

### Chinese Interpretation（完整对等诠释）

出生 = 新事物涌现。**正面**：预备结束，呼召预备好。**负面**：畸形 = 罪所怀的。

### Narrative Snippets

- `[ns_dav_b035]` `[trigger: 梦出生]` `[factor_trigger: dream_symbol_birth]` `[role: 主干]` Birth = new emergence—normal = calling ready, deformed = sin-conceived. → Dreams Dictionary #Birth"""
    normalized_text_zh: str = """"""
    subject: str = "Birth 出生"
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
        l1_anchor="dvd_v1.0.0_birth_出生_001_L1",
    )
    version: str = "1.0.0"
