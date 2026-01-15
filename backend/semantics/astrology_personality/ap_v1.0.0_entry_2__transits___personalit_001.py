"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238347
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
    semantic_id="ap_v1.0.0_entry_2__transits___personalit_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry2TransitsPersonalit(SemanticEntry):
    """
    **Source Text** (Lines 14619-14703):
> Transits: According to the concepts formulated in our last ch...
    """
    
    original_text: str = """**Source Text** (Lines 14619-14703):
> Transits: According to the concepts formulated in our last chapter, transits do not differ fundamentally from progressions or directions. They are constituted by planetary motion along the 370-year cycle of personality-fulfillment...
>
> The point to remember is always that such positions and the aspects formed refer to the realm of personality... the "concrete man," the man attempting to actualize... the totality of his being.

**Key Term Analysis**:
- **Transits nature**: `same procedure as progressions` / `370-year cycle` / `personality realm`
- **Two methods**: `transiting-to-transiting` (world conditions) / `transiting-to-radical` (individual)
- **Transiting Sun on Node**: `North Node = destiny influx` / `maximum power`
- **Mussolini example**: `March on Rome` / `Sun on North Node` / `Moon-Uranus conjunction`

**English Paraphrase (Primary Language)**:
Transits = "planetary motion along 370-year cycle of personality-fulfillment." Same procedure as secondary progressions.

Two methods: "transiting-to-transiting" = world conditions (not personal); "transiting-to-radical" = individual destiny.

Example: Mussolini's "March on Rome"—transiting Sun exactly conjunct radical North Node = "the one day when it would operate with maximum power."

**Complete Chinese Interpretation (Secondary Language)**:
过境 = "沿370年人格实现周期的行星运动"。与次限推运相同的程序。

两种方法："过境-过境" = 世界状况（非个人）；"过境-本命" = 个人命运。

例：墨索里尼的"进军罗马"——过境太阳精确合相本命北交点 = "它将以最大力量运作的那一天"。

**Narrative Snippets**:
- `[ns_aop_215]` `[trigger: transits_nature]` `[factor_trigger: astro_transit_method AND astro_transit_rad AND astro_transit_trans]` `[role: 主干]` Transits = 370-year personality cycle; two methods: transit-transit (world) vs transit-radical (individual). → L14621-14657
- `[ns_aop_216]` `[trigger: transit_example]` `[factor_trigger: astro_mussolini_transit]` `[role: 主干依赖]` Example: Mussolini March on Rome; transiting Sun conjunct North Node = maximum power. → L14680-14686"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 2: Transits - Personality Conditioning"
    factor_refs: list = ['transit_radical', 'transit_transit']
    
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
        book_id="astrology_personality",
        chapter="",
        l1_anchor="ap_v1.0.0_entry_2__transits___personalit_001_L1",
    )
    version: str = "1.0.0"
