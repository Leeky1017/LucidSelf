"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238190
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
    semantic_id="ap_v1.0.0_entry_3__planets_of_the_uncons_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry3PlanetsOfTheUncons(SemanticEntry):
    """
    **Source Text** (Lines 9034-9288):
> Planets Referring to the Unconscious: A. THE PERSONAL UNCONSCIO...
    """
    
    original_text: str = """**Source Text** (Lines 9034-9288):
> Planets Referring to the Unconscious: A. THE PERSONAL UNCONSCIOUS... The way in which the planets Neptune and Pluto have been discovered serves as a symbolical illustration of the relationship between conscious and unconscious...
>
> Retrograde planets symbolize the turning back of the libido (psychic energy or life-force) from the conscious into the unconscious. If a planet is retrograde, the function it represents is not activated for conscious operation...
>
> Saturn retrograde will direct this pattern-crystallizing and wall-making power inward. Self-assertion will be against inner influences... He will fortify himself spontaneously against impacts coming from the collective unconscious.

**Key Term Analysis**:
- **Personal unconscious**: `repressed/submerged contents` / `Freud's realm`
- **Retrograde meaning**: `libido turns back to unconscious` / `function not consciously activated`
- **Saturn retrograde**: `inner fortification` / `resistance to collective unconscious`
- **Jupiter retrograde**: `soul-compensation through dreams` / `Uranian projections`
- **Mars retrograde**: `unconscious motivation for action` / `sublimation attempts`

**English Paraphrase (Primary Language)**:
Retrograde planets = "turning back of libido from conscious to unconscious." The function isn't activated consciously; energy flows inward.

Saturn retrograde: "Self-assertion against inner influences... fortifies against collective unconscious impacts" but "defenseless against outer world."

Jupiter retrograde: compensation operates through dreams and unconscious projections.

Mars retrograde: actions arise from "unconscious motivation" rather than spontaneous conscious impulses.

**Complete Chinese Interpretation (Secondary Language)**:
逆行行星 = "力比多从意识转回无意识。"功能不被意识激活；能量向内流动。

土星逆行："对内在影响的自我主张……抵御集体无意识的冲击"但"对外部世界无防御。"

木星逆行：补偿通过梦和无意识投射运作。

火星逆行：行动源于"无意识动机"而非自发的意识冲动。

**Narrative Snippets**:
- `[ns_aop_180]` `[trigger: retrograde_meaning]` `[factor_trigger: astro_retrograde_general AND astro_personal_uncon AND astro_retrograde]` `[role: 主干]` Retrograde = libido turns back from conscious to unconscious; function not consciously activated. → L9139-9148
- `[ns_aop_181]` `[trigger: saturn_retrograde]` `[factor_trigger: astro_saturn_rx AND astro_saturn_moon]` `[role: 主干依赖]` Saturn Rx: inner fortification against collective unconscious; defenseless outer world. → L9171-9194"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 3: Planets of the Unconscious - Retrograde and Personal Unconscious"
    factor_refs: list = ['retrograde_gen', 'personal_uncon']
    
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
        l1_anchor="ap_v1.0.0_entry_3__planets_of_the_uncons_001_L1",
    )
    version: str = "1.0.0"
