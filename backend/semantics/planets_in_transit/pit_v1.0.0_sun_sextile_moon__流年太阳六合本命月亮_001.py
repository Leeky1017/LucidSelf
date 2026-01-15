"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224160
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
    semantic_id="pit_v1.0.0_sun_sextile_moon__流年太阳六合本命月亮_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunSextileMoon流年太阳六合本命月亮(SemanticEntry):
    """
    **Source Text** (Lines 2165-2195):
> This is a time of psychological and emotional equilibrium, when...
    """
    
    original_text: str = """**Source Text** (Lines 2165-2195):
> This is a time of psychological and emotional equilibrium, when the different aspects of your personality are in tune with each other. You can face your daily life with less effort than usual.
> 
> Relations with friends will be harmonious. Relations with the opposite sex are smoother than usual. This is an especially good time to think about your personal and emotional life—strains can be corrected now because you are relatively at peace.

**English Paraphrase**: Psychological and emotional equilibrium; personality aspects in tune. Face daily life with less effort. Harmonious relations with friends. Smoother opposite-sex relations. Good time for personal/emotional life reflection—correct strains while at peace.

**Complete Chinese Interpretation**: 心理和情感的平衡；人格各方面协调。以更少努力面对日常生活。与朋友关系和谐。与异性关系更顺利。反思个人/情感生活的好时机——在平和时纠正紧张。

**Narrative Snippets**:
- `[ns_pit_057]` `[trigger: transit_sun_sextile_natal_moon]` `[factor_trigger: astro_transit_sun SEXTILE natal_moon]` `[role: 主干]` Psychological and emotional equilibrium—personality aspects in tune, face daily life with less effort. → PIT Ch4 Sun⚹Moon
- `[ns_pit_058]` `[trigger: transit_sun_sextile_natal_moon]` `[factor_trigger: astro_transit_sun SEXTILE natal_moon]` `[role: 主干依赖]` Good time for personal/emotional reflection—correct strains while relatively at peace. → PIT Ch4 Sun⚹Moon"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Sextile Moon (流年太阳六合本命月亮)"
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
        book_id="planets_in_transit",
        chapter="",
        l1_anchor="pit_v1.0.0_sun_sextile_moon__流年太阳六合本命月亮_001_L1",
    )
    version: str = "1.0.0"
