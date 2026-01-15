"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224434
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
    semantic_id="pit_v1.0.0_sun_conjunct_jupiter__流年太阳合本命木_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunConjunctJupiter流年太阳合本命木(SemanticEntry):
    """
    **Source Text** (Lines 2675-2707):
> On the purely mundane level, you will feel very good, physicall...
    """
    
    original_text: str = """**Source Text** (Lines 2675-2707):
> On the purely mundane level, you will feel very good, physically and psychologically. Jupiter combined with Sun provides optimism and positive outlook. You want to include as much in your life as possible—desire experience and activity. On intellectual level: study or mind-expanding inquiry. On physical level: new experiences to broaden life.
> 
> Negative side: can be arrogant and domineering if you believe your growth comes at others' expense. The drive to incorporate may lead you to take on projects beyond your ability. Act with discipline—don't indulge every compulsive whim. Handle resources intelligently.

**English Paraphrase**: Feel good physically and psychologically. Optimism and positive outlook. Want to include much in life—desire experience. Intellectual: study, mind-expansion. Physical: new experiences. Negative: arrogance if growth at others' expense. May overextend. Act with discipline.

**Complete Chinese Interpretation**: 身心感觉良好。乐观和积极展望。想在生活中包含更多——渴望体验。智力：学习、心智扩展。身体：新体验。负面：如果成长以他人为代价则傲慢。可能过度扩张。有纪律地行动。

**Narrative Snippets**:
- `[ns_pit_091]` `[trigger: transit_sun_conjunct_natal_jupiter]` `[factor_trigger: astro_transit_sun CONJUNCT natal_jupiter]` `[role: 主干]` Feel very good—optimism and positive outlook. Want to include much in life, desire experience and activity. → PIT Ch4 Sun☌Jupiter
- `[ns_pit_092]` `[trigger: transit_sun_conjunct_natal_jupiter]` `[factor_trigger: astro_transit_sun CONJUNCT natal_jupiter]` `[role: 条件分支]` Negative: arrogance if growth at others' expense. May overextend—act with discipline. → PIT Ch4 Sun☌Jupiter"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Conjunct Jupiter (流年太阳合本命木星)"
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
        l1_anchor="pit_v1.0.0_sun_conjunct_jupiter__流年太阳合本命木_001_L1",
    )
    version: str = "1.0.0"
