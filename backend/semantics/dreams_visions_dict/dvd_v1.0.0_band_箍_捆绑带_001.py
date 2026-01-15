"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.424342
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
    semantic_id="dvd_v1.0.0_band_箍_捆绑带_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Band箍捆绑带(SemanticEntry):
    """
    ### Source Text

> Band of iron/brass around tree stump = restricted growth, stifled, held back. **P...
    """
    
    original_text: str = """### Source Text

> Band of iron/brass around tree stump = restricted growth, stifled, held back. **Positive (rare)**: Lord saying step back for a season. **Negative**: Stunt growth, curse preventing progress (Dan 4:15).

### English Paraphrase

Band = restricted growth. **Negative**: Curse preventing spiritual advancement. Like Nebuchadnezzar's band.

### Chinese Interpretation（完整对等诠释）

箍 = 限制成长。**负面**：咒诅阻止属灵进步。如尼布甲尼撒的铁箍。

### Narrative Snippets

- `[ns_dav_b014]` `[trigger: 梦箍]` `[factor_trigger: dream_symbol_band]` `[role: 主干]` Band = restricted growth—usually negative, stunting progress. → Dreams Dictionary #Band"""
    normalized_text_zh: str = """"""
    subject: str = "Band 箍/捆绑带"
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
        l1_anchor="dvd_v1.0.0_band_箍_捆绑带_001_L1",
    )
    version: str = "1.0.0"
