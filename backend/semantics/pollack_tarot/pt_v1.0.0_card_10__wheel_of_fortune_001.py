"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.994512
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
    semantic_id="pt_v1.0.0_card_10__wheel_of_fortune_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class Card10WheelOfFortune(SemanticEntry):
    """
    ### Fate, Cycles, and the Mystery of Existence

#### Key Term Analysis

| Term | Definition | Signif...
    """
    
    original_text: str = """### Fate, Cycles, and the Mystery of Existence

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Number 10 | First cycle complete | Midpoint |
| Sphinx/Horus | Resurrection | Above the wheel |
| Four Fixed Signs | Angel/Eagle/Lion/Bull | Corners |
| Karma/Fate | Why things happen | Mystery |

**Source Text**: With the Wheel, we come to the great question of how and why anything happens at all in the universe. The Wheel of Life does not become visible until we step away from it. When we are involved in it we see only the events immediately before and behind us. When we withdraw we can see the whole pattern. The sphinx on top of the Wheel represents Horus, god of resurrection. Life has triumphed over death. But the sphinx also signifies the mystery of life.

**English Paraphrase**:

**Wheel of Fortune** = **Fate**, **Cycles**, **Mystery of Causation** — vision of life's turning patterns revealed through withdrawal.

**Core Symbolism**:
- **Number 10**: Completion of first cycle (1-10), midpoint if Fool = 0
- **Wheel**: Eternal rotation, ups and downs, karma, cycles of life/death/rebirth

**Visual Elements** (Rider-Waite-Smith):
- **Spinning wheel** with Hebrew letters (YHVH, God's name) and alchemical symbols
- **Sphinx on top** = Horus, resurrection, mystery of life transcending wheel
- **Anubis ascending** (right) = jackal-headed guide to dead, giver of new life
- **Set/Typhon descending** (left) = snake, Egyptian god of death/darkness
- **Four creatures in corners** (reading books):
  - Angel (Aquarius, Air, Swords)
  - Eagle (Scorpio, Water, Cups)
  - Lion (Leo, Fire, Wands)
  - Bull (Taurus, Earth, Pentacles)
- **Clouds** = vision realm, unconscious revelation

**Historical Evolution**:

**Medieval homily version** (Visconti):
- King on top of wheel → crushed at bottom by Fortuna
- **Lesson**: Pride before fall, humility before God
- No matter your power, fate rests in God's hands

**Ancient origins**:
- **Fortuna = Great Goddess**
- Crushed king = **yearly sacrifice** (midwinter)
- Priestesses killed old king, chose new one
- **Purpose**: Humble to Goddess's power, suggest she create spring from winter

**Malory's interpretation** (King Arthur):
- **Luck vs. Fate**: Random events actually God's destiny
- Why rich/poor? Why kings fall? = God's incomprehensible plan
- **Holy Grail connection**: Holy Ghost within Grail gives meaning to "random" events

**Philosophical Meanings**:

**The Great Question**: Why does anything happen?
- Why does sun shine? Why gravity? Why spring after winter?
- **Surface answer**: Natural laws, atomic energy, physical causes
- **Deeper truth**: Spirit force unites universe (Magician's lightning manifested as Empress's nature)

**Limited Vision Problem**:
- We don't live long enough to see connections
- Short lives = miniscule portion of world = appears meaningless
- **Mystics' vision**: All things connect, everything fits together through spirit

**Fate as Illusion**:
- "It's fate" = **dodge to cover up** our inability to see inner connections
- **Karma** (Indian version): Actions in one life create psychic destiny for next
- **Both explanations** still mysteries due to limited understanding

**Enlightenment = Seeing Through**:
- Buddha's enlightenment: Remembered **every moment of every past life**
- **Memory WAS enlightenment** — saw all lives as forms created by desires
- Ended desires = **"got off the Wheel"**
- **Piercing outer events** to find spirit within = finding Holy Ghost within Wheel

**The Vision**:

**Why now?**
- Hermit withdrew from outer world
- **Unconscious shows vision** of life as turning wheel filled with symbols
- Wheel invisible until you **step away** from it
- Involved = see only daily concerns (ego's narrow view)
- Withdrawn = **see whole pattern**

**Psychological assessment**:
- Person evaluates where life has gone and is going
- Can see what you've made of particular life
- But **fate remains mysterious** (symbols help but don't fully reveal living force)

**Wheel vs. World** (Midpoint parallel):

| Aspect | Wheel (10) | World (21) |
|--------|-----------|-----------|
| Image | Wheel with symbols | Wreath with dancer |
| State | Vision | Embodiment |
| Creatures | Mythological (symbolic) | Real and alive |
| Understanding | See pattern, sense mystery | Truth embodied in being |
| Light | Veiled | Fully revealed |

**Egyptian Symbolism - Death/Rebirth Cycle**:

**Set (snake descending)**:
- God of death, darkness, "evil"
- Killed Osiris (god of life)
- **But**: Once hero god, snake sacred to Goddess
- **Darkness not evil** — ego fears dark because unconscious stirs
- Dissolution necessary for rebirth

**Anubis (jackal ascending)**:
- Guide to dead souls, giver of new life
- **Set's son** (some legends) = only death brings new life
- Fear of death = seeing partial truth
- **Psychological**: Only ego-death releases life energy within

**Horus (sphinx on top)**:
- Osiris's son, god of resurrection
- **Life triumphs over death**
- **Sphinx mystery**: Great secret to life beyond endless meaningless events
- Chariot controlled life with ego; now sphinx **risen above Wheel**

**The Four Creatures** (Ezekiel's vision):
- **Guardians of heaven** (Ezekiel 1:10, Revelations 4:7)
- Four elements (fire/water/air/earth)

**Narrative Snippets**:
- `[ns_78deg_123]` `[trigger: wheel_major]` `[factor_trigger: tarot_major_wheel AND parallel_wheel_world AND tarot_number_10]` `[role: 主干]` The Wheel of Fortune represents the vision of fate and cycles—the turning pattern that becomes visible only through withdrawal; midpoint of Major Arcana. → English Paraphrase
- `[ns_78deg_124]` `[trigger: jupiter_ruler]` `[factor_trigger: planet_jupiter]` `[role: 主干依赖]` Jupiter rules the Wheel of Fortune—expansion, fortune, luck; the planet of opportunity and cyclical change. → English Paraphrase
- `[ns_78deg_125]` `[trigger: death_rebirth]` `[factor_trigger: cycle_death_rebirth]` `[role: 主干]` Set descends (dissolution), Anubis ascends (renewal)—the death-rebirth cycle that is prerequisite for transformation. → English Paraphrase
- `[ns_78deg_126]` `[trigger: sphinx_symbol]` `[factor_trigger: symbol_sphinx]` `[role: 条件分支]` Sphinx (Horus) on top represents life triumphing over death—risen above the Wheel; the mystery that cannot be spoken. → English Paraphrase
- `[ns_78deg_127]` `[trigger: fixed_signs]` `[factor_trigger: system_fixed_signs]` `[role: 条件分支]` Four fixed signs in corners (Aquarius, Scorpio, Leo, Taurus)—elemental guardians stabilizing the turning wheel. → English Paraphrase
- `[ns_78deg_128]` `[trigger: major_arcana_framework]` `[factor_trigger: framework_major_arcana]` `[role: 条件分支]` Wheel at position 10 marks midpoint of 22 Major Arcana cards—first cycle complete, parallel to World (21) in vision form. → English Paraphrase
- `[ns_78deg_386]` `[trigger: wheel_visibility]` `[factor_trigger: tarot_major_wheel AND principle_withdrawal]` `[role: 条件分支]` Wheel invisible until you step away—involved we see only daily concerns; withdrawn we see whole pattern; Hermit's withdrawal enables the vision. → Source Text
- `[ns_78deg_387]` `[trigger: buddha_enlightenment]` `[factor_trigger: tarot_major_wheel AND state_enlightenment AND principle_karma]` `[role: 条件分支]` Buddha's enlightenment = remembering every moment of every past life; memory WAS enlightenment; ended desires = "got off the Wheel." → Philosophical Meaning
- `[ns_78deg_388]` `[trigger: wheel_vs_world]` `[factor_trigger: tarot_major_wheel AND tarot_major_world]` `[role: 总结]` Wheel vs World: Wheel shows vision with symbols, World embodies truth in being; creatures symbolic (Wheel) vs living (World); understanding vs embodiment. → Midpoint Parallel
- `[ns_78deg_555]` `[trigger: yhvh_wheel]` `[factor_trigger: tarot_major_wheel AND symbol_yhvh]` `[role: 条件分支]` Hebrew letters YHVH on spinning wheel—God's name interwoven with fate; divine causation underlying apparent randomness; the sacred embedded in fortune's turning. → Visual Elements"""
    normalized_text_zh: str = """"""
    subject: str = "Card 10: Wheel of Fortune"
    factor_refs: list = ['tarot_major_wheel', 'tarot_number_10', 'symbol_sphinx', 'cycle_death_rebirth', 'principle_karma', 'system_fixed_signs']
    
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
        l1_anchor="pt_v1.0.0_card_10__wheel_of_fortune_001_L1",
    )
    version: str = "1.0.0"
