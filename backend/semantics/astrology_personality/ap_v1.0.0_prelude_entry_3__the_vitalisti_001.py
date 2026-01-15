"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237611
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
    semantic_id="ap_v1.0.0_prelude_entry_3__the_vitalisti_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class PreludeEntry3TheVitalisti(SemanticEntry):
    """
    **Source Text** (Lines 795-904):
> According to the vitalistic conception, Life is in everything, in...
    """
    
    original_text: str = """**Source Text** (Lines 795-904):
> According to the vitalistic conception, Life is in everything, interpenetrates every entity, every substance. It is a vast, universal ocean of energy in which all that is "moves and has its being." This world-viewpoint originates in mankind when the primordial fear of nature is somewhat overcome, when what we may call symbolically the "jungle" is left behind, and men become either cattle-breeders or agriculturists...
>
> Animism reveals man as merely one among the myriads of entities struggling for subsistence... On the other hand, vitalism presupposes that at least a part of nature—within man as well as without—is conquered and utilized. Security of a sort has been attained...
>
> At this stage of human development astrology becomes supremely important. It does not deal any longer exclusively with celestial entities as separate beings to be worshipped and placated... The new astrology of the vitalistic period deals especially with an understanding of the periodicity of life-processes...
>
> Astrology becomes a study of the universal mystery of periodical dynamic transformations, which is seen to be the very essence of Life itself. The ancient Chinese symbolized this law of natural transformation in their series of hexagrams constituting the Yi King, the Book of Changes...
>
> The Law of Analogy presupposes a universal agent permeating the entire universe—a life-substance or life-force filling in all space... The tribal home becomes a small replica of the universal home bound by the spheres of the stars. The Earth is the microcosm; the universe, the macrocosm.

**Key Term Analysis**:
- **Vitalism**: `Life in everything` / `universal energy ocean` / `domesticated nature`
- **Periodicity of life-processes**: `cyclic understanding` / `Sun-Moon seasons` / `Yi King`
- **Law of Analogy**: `microcosm-macrocosm` / `universal correspondence` / `occult foundation`
- **Agricultural/pastoral shift**: `jungle → domestication` / `fear → production` / `property orientation`
- **Yang-Yin dualism**: `Chinese symbolism` / `waxing-waning` / `male-female`
- **State as microcosm**: `not individual` / `collective focus` / `Emperor as Sun`

**English Paraphrase (Primary Language)**:
The second stage—vitalism—emerges when humanity leaves the jungle and domesticates nature through agriculture or cattle-breeding. Fear is replaced by production as the keynote. Life is now understood as a universal force pervading everything, with predictable cycles that can be worked with.

Astrology transforms: no longer worship of separate celestial spirits, but understanding of life-process periodicity. The Sun-Moon cycles become foundational because they correlate with vegetation and animal breeding cycles. This generates the "Law of Analogy"—microcosm-macrocosm correspondence. The Chinese Yi King (Book of Changes) represents this stage's abstracted wisdom.

Crucially, at this stage the Earth (or State/community) is the microcosm, not the individual. The Emperor is the Sun-center of the social organism. Individual natal astrology comes later, in Alexandria and the Middle Ages. Chinese and Chaldean astrology addressed collective/state concerns, not personal destinies.

The Yang-Yin dualism (male-female, day-night, Sun-Moon) becomes the fundamental pattern for understanding all life transformations.

**Complete Chinese Interpretation (Secondary Language)**:
第二阶段——生机论——出现于人类离开丛林并通过农业或畜牧驯化自然时。恐惧被生产取代为主要基调。生命现在被理解为渗透一切的普遍力量，具有可预测的周期可以与之合作。

占星学转变了：不再是对分离天体精灵的崇拜，而是对生命过程周期性的理解。太阳-月亮周期成为基础，因为它们与植被和动物繁殖周期相关。这产生了"类比法则"——微观宇宙与宏观宇宙的对应。中国的《易经》代表了这一阶段抽象化的智慧。

关键的是，在这一阶段，地球（或国家/社会）是微观宇宙，而非个人。皇帝是社会有机体的太阳中心。个人本命占星学后来才出现，在亚历山大和中世纪。中国和迦勒底占星学处理集体/国家关切，而非个人命运。

阴阳二元（男-女、日-夜、太阳-月亮）成为理解所有生命转化的基本模式。

**Core Points**:
- Vitalism emerges with agriculture/pastoralism (domesticated nature)
- Life as universal force with predictable cycles
- Fear → production as keynote shift
- Astrology becomes study of periodicity
- Sun-Moon cycles correlate with earthly life-cycles
- Law of Analogy: microcosm-macrocosm correspondence
- Yi King as vitalistic wisdom abstraction
- Earth/State as microcosm (not individual)
- Emperor = Sun-center of social organism
- Yang-Yin dualism as fundamental pattern

**Narrative Snippets**:
- `[ns_aop_029]` `[trigger: vitalism_definition]` `[factor_trigger: astro_vitalistic]` `[role: 主干]` Vitalism: Life interpenetrates everything as universal energy ocean—emerges when jungle fear is overcome through domestication. → Source Text L797-806
- `[ns_aop_030]` `[trigger: periodicity_study]` `[factor_trigger: life_periodicity AND astro_periodicity_focus]` `[role: 主干依赖]` Vitalistic astrology studies periodicity of life-processes—universal mystery of dynamic transformations as essence of Life. → Source Text L854-857
- `[ns_aop_031]` `[trigger: law_of_analogy]` `[factor_trigger: universe AND earth_state AND astro_analogy_function]` `[role: 条件分支]` Law of Analogy: universal life-force fills all space; Earth/State = microcosm, universe = macrocosm. → Source Text L871-881
- `[ns_aop_032]` `[trigger: yang_yin]` `[factor_trigger: astro_yang_yin]` `[role: 总结]` Yang-Yin dualism (Sun-Moon, day-night, male-female) becomes fundamental pattern for understanding life transformations. → Source Text L893-904

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: Rudhyar's framing of Chinese astrology as vitalistic (collective, state-centered) contrasts with Ptolemaic individual focus. Modern scholarship supports this distinction between mundane and natal astrology origins.
- **中文**: Rudhyar将中国占星学定位为生机论的（集体、以国家为中心）与托勒密的个人焦点形成对比。现代学术支持这种世俗占星与本命占星起源的区分。"""
    normalized_text_zh: str = """"""
    subject: str = "Prelude Entry 3: The Vitalistic Stage"
    factor_refs: list = ['astro_vitalistic_stage', 'astro_law_analogy', 'astro_yang_yin', 'astro_periodicity']
    
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
        l1_anchor="ap_v1.0.0_prelude_entry_3__the_vitalisti_001_L1",
    )
    version: str = "1.0.0"
