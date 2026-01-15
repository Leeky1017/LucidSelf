"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237634
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
    semantic_id="ap_v1.0.0_prelude_entry_5__the_sixth_cen_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class PreludeEntry5TheSixthCen(SemanticEntry):
    """
    **Source Text** (Lines 988-1101):
> Then man began to develop a new basis for living and to know him...
    """
    
    original_text: str = """**Source Text** (Lines 988-1101):
> Then man began to develop a new basis for living and to know himself as an individual, a free being; and a new jungle arose at a higher level, the psycho-mental level. This meant the start of a new cycle of human development, calling for a New Astrology, a new understanding of Order, of Cosmos, of God.
>
> This momentous change occurred, archetypally as it were, during the sixth century B.C.; the time of Gautama the Buddha, followed by Lao-Tze and Confucius, the last Zoroaster and Gushapt, Pythagoras and, later, Plato—to mention only the most outstanding spiritual figures of this critical time which marked a potential reversal of all human values...
>
> The main significance of the change... is that the emphasis which had so far been exclusively placed on physiological matters began to be transferred to psychological values. Everything before 600 B.C. was based upon the human "body." Since then, more and more, a new foundation has been raised, and almost everything is sooner or later to be focussed upon the human "psyche"...
>
> It seems to us a mistake to believe that the old Kundalini Yoga and similar methods of development referred to psychological facts—as C.G. Jung apparently believes. If it did, it was only after the reforms of the Buddha. For then the chaos of the world was shown not to be overcomeable through means which were almost entirely psychological and rational...
>
> Alchemy, when not perverted or materialized, is an attempt to do with the human psyche what the Chinese Emperor was supposed to do as supreme Ruler of Agriculture... Its purpose is to raise psychological crops and to domesticate the wild herd of human desires.

**Key Term Analysis**:
- **Sixth century B.C.**: `axial age` / `Buddha, Lao-Tze, Confucius, Pythagoras, Plato` / `value reversal`
- **Individual as free being**: `new self-consciousness` / `psycho-mental jungle` / `new cycle`
- **Body to Psyche shift**: `physiological → psychological` / `pre-600 B.C. vs after` / `foundation change`
- **Kundalini Yoga**: `body-based originally` / `not psychological until post-Buddha` / `Jung's misreading`
- **Alchemy**: `psychological agriculture` / `domesticating desires` / `inner Emperor function`
- **New Astrology**: `responding to individual consciousness` / `psychological Order` / `new Cosmos`

**English Paraphrase (Primary Language)**:
Rudhyar identifies the sixth century B.C. as the pivotal transformation point: the emergence of individual self-consciousness. Buddha, Lao-Tze, Confucius, Zoroaster, Pythagoras, Plato—all appeared within this concentrated period, marking "a potential reversal of all human values."

The key shift: from body to psyche. Before 600 B.C., everything centered on the physiological; after, increasingly on the psychological. This created a "new jungle at the psycho-mental level"—chaos now manifested in the mind rather than in elemental nature. A New Astrology was required.

Rudhyar critiques Jung's psychological interpretation of Kundalini Yoga: originally, it was body-based, not psychological. Only after Buddha's reforms did psychological methods emerge. Alchemy represents the psychological parallel to vitalistic agriculture: instead of tilling external earth, the alchemist cultivates the inner psyche, domesticating the "wild herd of human desires."

This transition explains why astrology needed to evolve: the old vitalistic, collective, state-centered astrology could not address individual psychological needs.

**Complete Chinese Interpretation (Secondary Language)**:
Rudhyar确定公元前6世纪为关键转变点：个人自我意识的出现。佛陀、老子、孔子、琐罗亚斯德、毕达哥拉斯、柏拉图——都在这一集中时期出现，标志着"所有人类价值的潜在逆转"。

关键转变：从身体到心灵。公元前600年之前，一切以生理为中心；之后，越来越以心理为中心。这创造了"心理-精神层面的新丛林"——混沌现在表现在心灵而非元素自然中。需要一种新占星学。

Rudhyar批评了Jung对昆达里尼瑜伽的心理学解读：最初它是以身体为基础的，而非心理的。只有在佛陀改革之后，心理方法才出现。炼金术代表了与生机论农业的心理学平行：炼金术士不是耕种外在土地，而是培养内在心灵，驯化"人类欲望的野兽群"。

这一转变解释了为什么占星学需要演变：旧的生机论、集体、以国家为中心的占星学无法满足个人心理需求。

**Core Points**:
- Sixth century B.C. = axial age of human consciousness
- Buddha, Lao-Tze, Confucius, Pythagoras, Plato in same period
- Emergence of individual as free, self-conscious being
- New "psycho-mental jungle" replacing elemental chaos
- Shift from body-centered to psyche-centered
- Pre-600 B.C. = physiological; Post = psychological
- Kundalini Yoga originally body-based, not psychological
- Jung's psychological reading anachronistic for archaic yoga
- Alchemy = psychological agriculture (domesticating desires)
- New Astrology required for individual consciousness

**Narrative Snippets**:
- `[ns_aop_037]` `[trigger: sixth_century_change]` `[factor_trigger: astro_axial_age AND astro_axial_transform AND astro_animistic_stage]` `[role: 主干]` Sixth century B.C. marked potential reversal of all human values—Buddha, Lao-Tze, Confucius, Pythagoras, Plato. → Source Text L995-1001
- `[ns_aop_038]` `[trigger: body_psyche_shift]` `[factor_trigger: body_focus AND psyche_focus AND astro_body AND astro_body_psyche_func]` `[role: 主干依赖]` Everything before 600 B.C. based on body; since then, increasingly on psyche—foundation change. → Source Text L1012-1016
- `[ns_aop_039]` `[trigger: alchemy_psychology]` `[factor_trigger: depth_alchemy AND agriculture AND astro_psych_alchemy_func]` `[role: 条件分支]` Alchemy attempts to do with psyche what Emperor did with agriculture—raise psychological crops, domesticate desires. → Source Text L1048-1051
- `[ns_aop_040]` `[trigger: new_astrology_needed]` `[factor_trigger: new_astrology AND individual_consciousness AND astro_individual_consc]` `[role: 总结]` New cycle of development calls for New Astrology—new understanding of Order, Cosmos, God for individual consciousness. → Source Text L992-993

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: Rudhyar's "axial age" concept parallels Karl Jaspers's later formulation. His critique of Jung's psychological reading of yoga anticipates debates in transpersonal psychology.
- **中文**: Rudhyar的"轴心时代"概念与Karl Jaspers后来的表述相似。他对Jung瑜伽心理学解读的批评预见了超个人心理学的争论。"""
    normalized_text_zh: str = """"""
    subject: str = "Prelude Entry 5: The Sixth Century Transformation"
    factor_refs: list = ['astro_axial_age', 'astro_body_psyche_shift', 'astro_psych_jungle', 'astro_psych_alchemy']
    
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
        l1_anchor="ap_v1.0.0_prelude_entry_5__the_sixth_cen_001_L1",
    )
    version: str = "1.0.0"
