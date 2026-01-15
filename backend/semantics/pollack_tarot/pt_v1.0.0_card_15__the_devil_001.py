"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.994584
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
    semantic_id="pt_v1.0.0_card_15__the_devil_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class Card15TheDevil(SemanticEntry):
    """
    ### Shadow, Repression, and the Power of Desire

#### Key Term Analysis

| Term | Definition | Signi...
    """
    
    original_text: str = """### Shadow, Repression, and the Power of Desire

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Number 15 | Reduces to 6 | Lovers perverted |
| Materialism | Nothing beyond senses | Primary illusion |
| Loose Chains | Easily removed | Self-imposed bondage |
| Sexual-Spiritual | Same energy | Transformation path |

**Source Text**: The Devil introduces the last line. In order to understand the esoteric value of the Devil we must first consider its more usual meanings as a force of illusion and oppression. The main illusion is materialism, the view that nothing exists beyond the world of the senses. However, if the Devil signifies release of repressed energy then the way to spirit leads through the desires. By embracing the Devil we set the psyche on a violent course leading to the explosion of the Tower.

**English Paraphrase**:

**The Devil** = **Shadow Self**, **Materialism**, **Repressed Energy** — illusion that must be faced, or power that must be embraced, to reach enlightenment.

**Core Symbolism**:
- **Number 15**: Reduces to 6 (Lovers) — Devil as **perversion** of Lovers
- **15 introducing Third Line**: Provides vital energy for archetypal work

**Visual Elements** (Rider-Waite-Smith):
- **Devil figure** with bat wings, horns = Greek god Pan + competitors of Christ
- **Reversed pentacle** on forehead = black magic, genitals over head (desire over reason)
- **One hand up, one down** (like Magician) but torch points **down** = materialism
- **Saturn glyph** on palm = limitations, restrictions, not evil but bondage
- **Open palm** (5 fingers) = recalls Hierophant but opposite meaning (nothing beyond visible)
- **Two chained figures** (Adam/Eve) = loose chains easily removed
- **Stone block** (half cube) = incomplete knowledge vs. Emperor's full cube
- **Black background** = darkness, depression, inability to see truth
- **Tails with flames** = kundalini fire, sexual energy inflamed

**Traditional Meanings**:

**1. Materialism/Illusion**:
- Nothing exists beyond world of senses
- Pursuing only personal desires (money, sex, power)
- Narrowness leads to misery
- **But**: Chained figures show no discomfort — **power rests in illusion** nothing else exists
- People become unhappy only when realize alternatives exist

**2. Sexual Obsession**:
- Reversed pentacle = desires overpower judgement
- Fire burning inside (destructive sexuality)
- Flame on man's tail = overwhelming need
- Traditional Christian: Reason should rule desires

**Esoteric/Occult Meanings**:

**The Paradox**: Why Devil so late? Why after Temperance's balance?

**Answer**: **Dante goes through Hell before Purgatory and Paradise**
- Blake: Devil = true hero of *Paradise Lost*
- **Path to enlightenment REQUIRES facing darkness**

**Sexual-Spiritual Energy Unity**:

**Occult belief**: Sex and spirit = **same energy**
- Scorpio's double image: Scorpion (lower/sexual) + Eagle (higher/spiritual)
- Average person: Sex urge dominant in popular culture
- **Occultist**: Tap this energy, raise it, **transform** into enlightenment

**Evidence**:
- Dreaming = always accompanied by sexual arousal (erect genitals)
- Dream = unconscious manifesting as images
- **Indication**: Unconscious is sexual in nature
- "Unconscious" really = **great pool of energy** sustaining us

**Celibacy reconsidered**:
- Not contamination avoidance
- **Turn that energy in another direction**
- India: Shiva's symbol = phallus, Tantra rites = copulation charges body
- Gnostics: Satan = true hero of Eden (giving knowledge)

**The Danger**:

**Why repress? Why keep secret?**
- **Terrible power** of sexual-spiritual energy
- **If transformed**: Frees from duality limitations
- **If NOT transformed**: Obsessions, violence, personality destruction
- Greek mysteries: Worshippers whip/mutilate themselves when overwhelmed
- **Not just sexual politics** — real danger in uncontrolled release

**Devil as Necessary**:

**Position above Strength (8)**:
- Strength: Lion energy raised and tamed
- Devil: **Untamed energy must be faced**

**Waite worked backwards**: Devil → designed Lovers
- Devil with captured demons = perversion of Lovers
- **But**: Woman in Lovers looks to angel (like Devil's symbolism)
- Pentacle over head = sex organs over head in Lovers' symbolism

**Snake = Messiah** (Hebrew numerology):

**Narrative Snippets**:
- `[ns_78deg_150]` `[trigger: devil_major]` `[factor_trigger: tarot_major_devil AND parallel_devil_lovers AND state_materialism AND tarot_number_15 AND symbol_reversed_pentacle AND psych_shadow]` `[role: 主干]` The Devil represents shadow self and repressed energy—materialism and illusion that must be faced; introduces Third Line of Major Arcana. → English Paraphrase
- `[ns_78deg_151]` `[trigger: loose_chains]` `[factor_trigger: symbol_loose_chains]` `[role: 主干]` Chained figures with loose chains—self-imposed bondage easily removed; the illusion of captivity that could end at any moment. → English Paraphrase
- `[ns_78deg_152]` `[trigger: capricorn_ruler]` `[factor_trigger: sign_capricorn]` `[role: 主干依赖]` Capricorn rules Devil—material, structure, Saturn's limitations; earth element of manifestation without spirit. → English Paraphrase
- `[ns_78deg_153]` `[trigger: third_line]` `[factor_trigger: framework_third_line]` `[role: 条件分支]` Devil introduces Third Line of Major Arcana (cards 15-21)—archetypal confrontation and spiritual transformation. → English Paraphrase
- `[ns_78deg_154]` `[trigger: sexual_spiritual_energy]` `[factor_trigger: principle_sexual_spiritual]` `[role: 条件分支]` Sexual-spiritual energy as same force—if transformed, frees from duality; if not, leads to obsession and destruction. → English Paraphrase
- `[ns_78deg_366]` `[trigger: devil_lovers_perversion]` `[factor_trigger: tarot_major_devil AND tarot_major_lovers]` `[role: 条件分支]` Number 15 reduces to 6 (Lovers)—Devil as perversion of Lovers; reversed pentacle = desires overpower judgment; genitals over head. → Core Symbolism
- `[ns_78deg_367]` `[trigger: dante_path]` `[factor_trigger: tarot_major_devil AND principle_facing_shadow]` `[role: 条件分支]` Dante goes through Hell before Paradise—path to enlightenment requires facing darkness; Blake saw Devil as true hero of Paradise Lost. → Esoteric Meaning
- `[ns_78deg_368]` `[trigger: scorpio_transformation]` `[factor_trigger: tarot_major_devil AND sign_scorpio]` `[role: 条件分支]` Scorpio's double image: Scorpion (lower/sexual) + Eagle (higher/spiritual)—same energy can be tapped, raised, transformed into enlightenment. → Sexual-Spiritual Unity
- `[ns_78deg_369]` `[trigger: devil_necessity]` `[factor_trigger: tarot_major_devil AND principle_transformation]` `[role: 总结]` Devil above Strength (8)—untamed energy must be faced; by embracing the Devil we set psyche on violent course leading to Tower's liberation. → Devil as Necessary

---"""
    normalized_text_zh: str = """"""
    subject: str = "Card 15: The Devil"
    factor_refs: list = ['tarot_major_devil', 'tarot_number_15', 'psych_shadow', 'principle_sexual_spiritual', 'symbol_loose_chains', 'state_materialism']
    
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
        book_id="pollack_tarot",
        chapter="",
        l1_anchor="pt_v1.0.0_card_15__the_devil_001_L1",
    )
    version: str = "1.0.0"
