"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237600
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
    semantic_id="ap_v1.0.0_prelude_entry_2__the_animistic_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class PreludeEntry2TheAnimistic(SemanticEntry):
    """
    **Source Text** (Lines 696-793):
> Primitive man lives still in the womb of Nature. His entire life ...
    """
    
    original_text: str = """**Source Text** (Lines 696-793):
> Primitive man lives still in the womb of Nature. His entire life is an experience which is at the same time psychological and physiological, because he is as yet hardly able to differentiate the outer world from the inner, the objective from the subjective. He is so completely one with Nature that he constantly finds himself dissolved into natural phenomena...
>
> Levy Bruhl has used the term "participation mystique" to describe this or a similar process of psychological identification with objects. It corresponds to an attitude to life which can also be designated by the word animism.
>
> Animism makes of all material objects "spirits," and materializes psychic facts into objective entities. Everything is animated by a spirit, whether it be a tree, a mountain, the sun, a star...
>
> At the animistic stage of development, man refers everything to himself and to his fears or his desires. He projects his reactions to things into the things themselves, which become personified images of his impressions...
>
> The Sun and the Moon are known as the givers of light. Light and life become inseparable, for darkness and night but too often mean death. Sunlight dispels fear, brings to the senses a clearer perception of objects. Thus the Sun is the great life-giver. As to the Moon, it hides a mystery. It waxes and wanes...
>
> Then it is not, as later, the motions of the celestial bodies which are the most important, but the life-quality, with which every single one of them is endowed.

**Key Term Analysis**:
- **Participation mystique**: `Levy-Bruhl concept` / `psychological identification` / `subject-object fusion`
- **Animism**: `spirits in all objects` / `psychic-material confusion` / `primitive worldview`
- **Projection**: `inner reactions → outer entities` / `fear/desire externalized` / `psychological mechanism`
- **Sun as life-giver**: `light = life` / `dispels fear` / `primal archetype`
- **Moon as mystery**: `waxing/waning` / `periodicity discovered` / `magic power`
- **Life-quality vs motion**: `essence over movement` / `animistic priority` / `star's character`

**English Paraphrase (Primary Language)**:
Rudhyar describes the first stage of astrological consciousness: animism. Primitive humans lived in undifferentiated unity with Nature—unable to distinguish inner from outer, psychological from physiological. Levy-Bruhl's "participation mystique" captures this state of psychological identification with objects.

In animism, everything possesses spirit: trees, mountains, stars. Conversely, inner feelings are externalized as entities that can be expelled by magic. Fear dominates—the jungle mentality where survival is paramount. Evil must be propitiated or overcome by sympathetic magic (identifying with the feared object to gain power over it).

The Sun becomes the primal life-giver: light dispels fear, darkness brings death. The Moon reveals mystery: its waxing and waning introduce periodicity and time-consciousness. Crucially, at this stage, the life-quality of celestial bodies matters more than their motions—each star has its essence, experienced through its light's quality (remarkably analogous to modern spectrum analysis!).

**Complete Chinese Interpretation (Secondary Language)**:
Rudhyar描述了占星意识的第一阶段：泛灵论。原始人类生活在与自然未分化的统一中——无法区分内在与外在、心理与生理。Levy-Bruhl的"神秘参与"捕捉了这种与客体心理认同的状态。

在泛灵论中，一切都拥有灵魂：树木、山脉、星星。相反，内在感受被外化为可以通过魔法驱逐的实体。恐惧主导一切——丛林心态，生存至上。邪恶必须被安抚或通过感应魔法克服（与被恐惧的对象认同以获得对它的力量）。

太阳成为原始的生命赋予者：光驱散恐惧，黑暗带来死亡。月亮揭示神秘：其盈亏引入周期性和时间意识。关键的是，在这一阶段，天体的生命品质比其运动更重要——每颗星都有其本质，通过其光的品质来体验（与现代光谱分析惊人相似！）。

**Core Points**:
- Primitive humans undifferentiated from Nature (participation mystique)
- Animism: spirits in all objects; psychic facts materialized
- Fear dominates jungle-state consciousness
- Sympathetic magic: identification with feared object
- Sun = life-giver (light = life)
- Moon = mystery, periodicity, magic power
- Life-quality of stars more important than motions
- Totemic identification parallels star-worship
- Subjective experience of starlight = proto-spectrum analysis

**Narrative Snippets**:
- `[ns_aop_026]` `[trigger: participation_mystique]` `[factor_trigger: astro_animistic AND participation_mystique AND astro_participation AND astro_projection]` `[role: 主干]` Primitive man lives in participation mystique—undifferentiated from Nature, projecting reactions into objects as spirits. → Source Text L698-707
- `[ns_aop_027]` `[trigger: sun_moon_primal]` `[factor_trigger: sun_moon_cycles AND fear AND astro_fear_state]` `[role: 主干依赖]` Sun is great life-giver (light dispels fear); Moon hides mystery (waxing/waning introduces periodicity). → Source Text L751-759
- `[ns_aop_028]` `[trigger: life_quality]` `[factor_trigger: life_quality AND celestial_attribution]` `[role: 总结]` At animistic stage, life-quality of celestial bodies matters more than motions—essence over movement. → Source Text L779-786

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: Rudhyar draws on Levy-Bruhl's "participation mystique" which Jung also adopted. Modern anthropology has critiqued this concept but its psychological insight remains valuable.
- **中文**: Rudhyar借用了Levy-Bruhl的"神秘参与"概念，Jung也采用过。现代人类学批评了这一概念，但其心理学洞见仍有价值。"""
    normalized_text_zh: str = """"""
    subject: str = "Prelude Entry 2: The Animistic Stage"
    factor_refs: list = ['psych_participation_mystique', 'astro_animism', 'astro_sympathetic_magic', 'astro_life_quality']
    
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
        l1_anchor="ap_v1.0.0_prelude_entry_2__the_animistic_001_L1",
    )
    version: str = "1.0.0"
