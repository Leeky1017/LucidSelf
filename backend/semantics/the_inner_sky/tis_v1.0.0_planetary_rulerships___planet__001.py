"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.134242
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
    semantic_id="tis_v1.0.0_planetary_rulerships___planet__001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class PlanetaryRulershipsPlanet(SemanticEntry):
    """
    **Source Text**:
"Planetary Rulerships
Planets and signs are entirely different kinds of mental mach...
    """
    
    original_text: str = """**Source Text**:
"Planetary Rulerships
Planets and signs are entirely different kinds of mental machinery. As we have seen, planets represent the ten basic functions into which the mind is divided: ego formation, feelings and imagination, aggressiveness, and so on. Signs are psychological processes with distinct goals and methods for attaining them: the development of courage or the development of an ability to break up routines, for example. Each psychological process, with its particular aim and methodology, can condition any of the ten functions, flavoring it with tone and purpose. Any planet, in other words, can lie in any sign.
Certain sign-planet combinations are more harmonious than others. Fiery Mars loves being in Aries, the sign of the Warrior. And it has trouble relating to gentle, courteous Libra. Each sign-planet configuration has meaning. Each can produce behaviors of positive value. And each can be corrupted. No configuration is inherently good or bad. That is not the point. What we are observing is only that certain planets facilitate the expression of certain signs more easily than others.
Each planet has a special relationship with a sign or two. Due to a similarity in their natures, when that planet lies in that sign, little friction is generated. We are presented with a very clear expression of both. Medieval astrology has given us a name for that special bond: a planet that has a particular affinity for a sign is said to be the ruler of that sign.
Rulership. The word is unfortunate. It is really not a question of dominance or submission. That is just medieval thinking. It would be more accurate to say that the planet and the sign 'like each other.' But modern astrology has retained the medieval expression.
Complementing rulerships, there is a parallel notion describing a particularly difficult sign-planet interaction. When a planet lies in a sign whose how and why are especially alien to it, that planet is said to be in its fall. There, both planet and sign must bend a great deal to achieve any common ground for their joint expression.
Planetary rulerships and falls are linked to the most tense of all aspects, the opposition. The sign of a planet’s fall is always opposed to the sign of its rulership. If we know one, we know the other. ... We have now accounted for all twelve signs. Each has a planetary ruler. Each is a planet’s fall.
Through the eighteenth century, that was all there was to planetary rulerships. But then we began discovering new planets, and suddenly everything became more complicated. ... Astrologers are divided about how to handle the invisible planets. Some think they function as 'co-rulers' of certain signs, sharing authority with the sign’s traditional ruler. Others think that the discovery of Uranus, Neptune, and Pluto has done away with three of the traditional rulerships. ... I myself lean toward the shared-rulership notion. ... The old rulerships make sense. They work. No need to do away with them. And yet each of the three invisible planets also has an obvious, face-value connection with a particular sign. No need to deny that either. ... And that is what rulership is all about in the first place—not authority, but harmony.
PLANETARY RULERSHIPS How do rulerships help us with the task of interpretation? Primarily, they help us gauge the relative strengths of all the phrases. Even when a planet is in its fall, it is still significant. We must still understand it. But a planet in its own sign is in a particularly influential position. That mental circuit—that what—plays a central role in the individual’s psychology. ... Such knowledge helps us keep perspective on the birth-chart. ... Knowing which 'bits' are most influential enables us to know which side of the inner argument is going to be acted out behaviorally and which side is likely to be forced to express itself in less-obvious ways."

**Key Term Analysis**:
- `planetary rulership`: special affinity between a planet and sign, giving clear expression of both.
- `fall`: placement where a sign’s style clashes with a planet’s function, requiring extra adjustment.
- `rulership vs authority`: rulership as harmony/liking, not dominance or submission.
- `phrase strength`: using rulerships/falls to gauge relative weight of different bits in a chart.

**English Paraphrase (Primary Language)**:
Forrest first reminds us that planets and signs are different symbolic machines. Planets are basic functions of the mind—identity, feeling, thinking, desire. Signs are psychological processes with specific aims and methods—developing courage, cultivating stability, breaking up routines, and so on. Any planet can be colored by any sign; every combination has meaning and can be lived well or badly.

Still, some pairings are especially smooth. When a planet’s nature fits a sign’s goals and style, expression is easy and clear. Medieval astrologers called such sign–planet affinities "rulerships": the planet is said to rule the sign. Forrest dislikes the connotation of dominance; he prefers to say the planet and sign simply "like each other." The opposite condition is a planet in its **fall**—a sign whose how and why are alien to the planet’s function. There, both sides must bend a lot in order to cooperate.

Rulerships and falls relate to oppositions: the sign of a planet’s fall always lies opposite the sign it rules. Classically, each of the twelve signs has both a ruler and a planet that falls there. The discovery of Uranus, Neptune, and Pluto complicated this picture: should we reassign rulerships, or add co‑rulers? Forrest opts for shared rulerships: keep the traditional rulers, but recognize obvious face‑value links between the new planets and certain signs.

Practically, rulerships help us judge which bits in a chart carry the most weight. A planet in its own sign marks a strongly emphasized function; even a planet in fall remains important, but less effortlessly expressed. Combined with aspect patterns, rulerships let us see which inner voices are loudest and which are more likely to operate in subtle or indirect ways.

**Complete Chinese Interpretation (Secondary Language)**:
Forrest 先区分了「行星」与「星座」这两套符号机器：行星代表心灵被分割成的十种基本功能——自我形成、情感与想象、攻击性等等；星座则是一系列「具有特定目标与方法的心理过程」——例如发展勇气、培养稳定、打破惯例。任何行星都可以落入任何星座，每一种组合都有其意义，也都既能正向发挥，也可能被扭曲，没有天然「好/坏」。

但在经验上，有些组合明显更顺畅。当某颗行星的本性与某个星座的目标与风格高度相投时，这颗行星在该星座里就更容易把自己表达清楚。传统占星把这种亲和关系叫作「守护/主宰」（rulership），Forrest 不太认同「统治」的字面含义，更倾向于理解成「行星与星座互相喜欢」。与之相对，当一颗行星落入某个与自己功能格格不入的星座时，被称为该行星在此星座「失势/落陷」（fall），双方都要大幅调整才能找到共同运作的空间。

守护与失势之间，通过最紧绷的相位——对分——联系起来：某行星的落陷星座必定与其守护星座成 180° 对分。经典体系中，每个星座既有一颗行星守护，也对应一颗行星在此失势。后来的天王、海王、冥王发现之后，问题变复杂：究竟要不要把部分星座改由新行星单独主宰？还是采用「共辖/共守护」模型？Forrest 倾向后者：传统守护逻辑仍然好用，无需废弃；同时，新行星与部分星座之间明显存在直观的性格呼应，也不必刻意否认。

在解读层面，守护/失势的主要用途，是帮助我们评估命盘中各个 bit 的**相对权重**。落在自己守护星座中的行星，象征这一心理功能在个体人格中占据极为核心的位置；即便落在失势星座，依然重要，只是表达更吃力、更需要自觉调整。当我们再结合相位网络，就能看清：在一段内心拉扯中，哪些「声音」更有机会主导外在行为，哪些则更可能退居幕后、以隐性的方式发挥影响。

**Core Points**:
- Planets = functions; signs = processes; rulerships mark special affinity between them.
- Rulership is about harmony/liking, not dominance.
- Falls mark sign–planet pairings that require extra adjustment from both sides.
- Rulerships and falls help rank the relative strength of bits in a chart.
- Shared rulerships for outer planets preserve old rulers while acknowledging new links.

**Detailed Explanation**:
This rulership framework adds a "signal strength" dimension to earlier grammar. A planet in its own sign is like a function broadcasting on its preferred channel: clearer, louder, and more confident. In fall, the signal runs through a medium that does not suit it; expression is possible, but takes more work and can invert or distort the function if handled unconsciously.

For interpretation and engine design, that means we can weight bits differently instead of treating all placements as equal. A dignified planet in heavy aspect contact might become a primary driver of behavior; a fallen planet may still be a key growth edge but less likely to dominate without support. The shared‑rulership stance also keeps the system flexible: we can model both classical and modern affinities without forcing an either‑or decision, as long as we remember that the essence of rulership is resonance, not political authority.

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: Forrest’s critique of "medieval" rulership language is kept, but softened into a functional definition—liking/resonance rather than rule. The interpretive question "Which bits are strongest?" is foregrounded because it is directly useful for chart reading and engine weighting.
- **中文**：对 rulership 统一译为「守护/主宰」并在正文中反复强调其本质是「和谐共振」而非「上下支配」，以防中文读者再次把它理解成权力结构。对「fall」用「失势/落陷」并解释为「表达吃力、需额外调适」，避免简化成「凶」.

**Narrative Snippets**:
- `[ns_innersky_007]` `[trigger: explaining_rulership]` `[factor_trigger: rulership]` `[role: 主干]` Rulership is not about dominance—it would be more accurate to say the planet and sign "like each other." → Source Text
- `[ns_innersky_008]` `[trigger: planet_in_own_sign]` `[factor_trigger: planetary_rulership]` `[role: 主干依赖]` When a planet lies in its own sign, we are presented with a very clear expression of both. → Source Text
- `[ns_innersky_009]` `[trigger: planet_in_fall]` `[factor_trigger: planetary_fall]` `[role: 条件分支]` In its fall, both planet and sign must bend a great deal to achieve any common ground for expression. → Source Text
- `[ns_innersky_010]` `[trigger: weighting_chart_factors]` `[factor_trigger: phrase_strength]` `[role: 总结]` Rulerships help us gauge the relative strengths of all the phrases—which bits are most influential. → Source Text
- `[ns_innersky_011]` `[trigger: mars_in_aries]` `[factor_trigger: planet_sign_affinity]` `[role: 主干]` Fiery Mars loves being in Aries, the sign of the Warrior—and has trouble relating to gentle Libra. → Source Text
- `[ns_innersky_012]` `[trigger: outer_planet_rulership]` `[factor_trigger: outer_planet]` `[role: 主干依赖]` The old rulerships work; no need to do away with them. Yet Uranus, Neptune, Pluto also have obvious links to certain signs. → Source Text"""
    normalized_text_zh: str = """"""
    subject: str = "Planetary Rulerships – Planet–Sign Affinity and Phrase Strength"
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
        book_id="the_inner_sky",
        chapter="",
        l1_anchor="tis_v1.0.0_planetary_rulerships___planet__001_L1",
    )
    version: str = "1.0.0"
