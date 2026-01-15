"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237536
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
    semantic_id="ap_v1.0.0_preface_to_the_third_edition___003",
    book_id="astrology_personality",
    engine_id="astro"
)
class PrefaceToTheThirdEdition(SemanticEntry):
    """
    **Source Text** (Lines 173-220):
> To this science-oriented group the approach to astrology promoted...
    """
    
    original_text: str = """**Source Text** (Lines 173-220):
> To this science-oriented group the approach to astrology promoted by the Irish astrologer and scholar, Cyril Fagan, and popularized by his monthly articles in American Astrology for the last twenty years, has a great appeal. It is Mr. Fagan's contention that the zodiac which has been in use in Europe since the days of the Greco-Latin civilization—the tropical zodiac—is inaccurate. He claims that the only true zodiac is the sidereal zodiac.
>
> The tropical zodiac is based on the apparent motion of the Sun in the sky from one vernal equinox to the next. It refers to the annual cycle of the ever-changing relationship of the earth-globe to the Sun, source of all energies on this earth—that is, to the cycle of the seasons. The "sidereal" zodiac also deals with the annual apparent motion of the Sun, but with reference to the constellations, i.e. to actual groupings of stars...
>
> What is at stake behind the controversy concerning the validity of a tropical or a sidereal zodiac is the basic attitude one takes toward astrology. The "siderealists" consider astrology an empirical science, whose one basic function is to predict the statistically measurable probability of precise events.

**Key Term Analysis**:
- **Tropical zodiac**: `equinox-based` / `seasonal cycle` / `Western tradition since Greco-Latin era`
- **Sidereal zodiac**: `constellation-based` / `star-referenced` / `Cyril Fagan's advocacy`
- **Precession of equinoxes**: `backward shift` / `tropical-sidereal divergence` / `~25,800 year cycle`
- **Empirical science**: `statistical prediction` / `event-probability` / `siderealist goal`
- **Cyril Fagan**: `Irish astrologer` / `sidereal advocate` / `American Astrology columnist`

**English Paraphrase (Primary Language)**:
Rudhyar addresses the tropical vs sidereal zodiac controversy—a technical debate with profound philosophical implications. The tropical zodiac (Western standard) is based on the seasons: the Sun's apparent movement from vernal equinox to vernal equinox, defining the relationship between Earth and Sun. The sidereal zodiac references actual star constellations. Due to precession, these zodiacs no longer align (they coincided somewhere between 300 BC and 500 AD).

But Rudhyar sees the real issue as philosophical, not technical. Siderealists like Cyril Fagan view astrology as empirical science aimed at predicting statistically measurable events. Rudhyar rejects this orientation entirely. For him, the choice of zodiac reflects one's fundamental attitude toward astrology's purpose: is it event-prediction or self-knowledge? The tropical zodiac, rooted in Earth-Sun seasonal relationship, aligns with a person-centered, psychological approach.

**Complete Chinese Interpretation (Secondary Language)**:
Rudhyar讨论了回归黄道与恒星黄道的争论——一个具有深刻哲学含义的技术辩论。回归黄道（西方标准）基于季节：太阳从春分点到春分点的视运动，定义地球与太阳的关系。恒星黄道参照实际的恒星星座。由于岁差，这两个黄道不再对齐（它们在公元前300年至公元500年间某处重合）。

但Rudhyar认为真正的问题是哲学性的，而非技术性的。像Cyril Fagan这样的恒星派将占星学视为旨在预测统计可测量事件的经验科学。Rudhyar完全拒绝这种取向。对他而言，黄道的选择反映了对占星学目的的根本态度：是事件预测还是自我认知？回归黄道植根于地球-太阳的季节关系，与以人为中心的心理学方法相一致。

**Core Points**:
- Tropical zodiac: equinox-based, seasonal, Western standard
- Sidereal zodiac: constellation-based, star-referenced, Fagan's advocacy
- Precession causes divergence between the two
- Real debate is philosophical: empirical science vs self-knowledge tool
- Siderealists want statistical event-prediction
- Rudhyar: zodiac choice reflects fundamental attitude toward astrology
- Tropical zodiac aligns with person-centered approach

**Detailed Explanation**:
This passage reveals Rudhyar's philosophical sophistication. He refuses to engage the tropical-sidereal debate purely on technical grounds because he recognizes that technical choices embody deeper philosophical commitments. The sidereal movement (Fagan, modern Western siderealists) seeks to make astrology "respectable" by aligning it with empirical science—star-positions, statistical correlations, event-prediction. Rudhyar sees this as a category error: astrology is not and should not become an empirical science. Its value lies precisely in its symbolic, meaning-making function for the individual person seeking self-understanding.

The tropical zodiac, anchored in the Earth-Sun relationship (the source of life on Earth), symbolically connects the individual to their cosmic environment in a way the arbitrary star-constellations cannot. It is "person-centered" because it refers to the individual's relationship to the life-giving Sun, not to distant star-groups.

**Narrative Snippets**:
- `[ns_aop_008]` `[trigger: tropical_sidereal_debate]` `[factor_trigger: astro_tropical_system AND astro_sidereal_system AND astro_precession_effect]` `[role: 主干]` The tropical zodiac is based on the seasonal Earth-Sun cycle; the sidereal on star constellations—they no longer coincide due to precession. → Source Text L180-191
- `[ns_aop_009]` `[trigger: philosophical_stake]` `[factor_trigger: astro_person_centered AND astro_symbolic AND astro_philosophy_orient]` `[role: 主干依赖]` What is at stake is the basic attitude toward astrology: siderealists want empirical event-prediction; Rudhyar wants person-centered meaning. → Source Text L196-200
- `[ns_aop_010]` `[trigger: fagan_approach]` `[factor_trigger: astro_empirical AND astro_systems]` `[role: 条件分支]` Cyril Fagan and siderealists consider astrology an empirical science for predicting statistically measurable events. → Source Text L199-200

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: The tropical-sidereal debate continues today. Rudhyar's position (tropical for psychological astrology) remains standard in humanistic practice. Vedic/Jyotish astrology uses sidereal, but with different philosophical foundations than Western siderealists.
- **中文**: 回归与恒星之争至今仍在继续。Rudhyar的立场（心理占星用回归黄道）在人本实践中仍是标准。吠陀/印度占星使用恒星黄道，但其哲学基础与西方恒星派不同。"""
    normalized_text_zh: str = """"""
    subject: str = "Preface to the Third Edition: Tropical vs Sidereal Zodiac Debate"
    factor_refs: list = ['astro_tropical_zodiac', 'astro_sidereal_zodiac', 'astro_precession', 'astro_cyril_fagan']
    
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
        l1_anchor="ap_v1.0.0_preface_to_the_third_edition___003_L1",
    )
    version: str = "1.0.0"
