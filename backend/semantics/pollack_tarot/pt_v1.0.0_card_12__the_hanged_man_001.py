"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.994542
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
    semantic_id="pt_v1.0.0_card_12__the_hanged_man_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class Card12TheHangedMan(SemanticEntry):
    """
    ### Surrender, Reversal, and Peace Through Acceptance

#### Key Term Analysis

| Term | Definition |...
    """
    
    original_text: str = """### Surrender, Reversal, and Peace Through Acceptance

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Number 12 | 21 reversed | Almost World |
| Voluntary Surrender | Acceptance | Not defeat |
| Reversed Values | World upside down | New perspective |
| Odin Myth | 9 days hanging | Runic wisdom |

**Source Text**: After the crisis of seeing what you have made of your life comes the peace of acceptance; after Justice, the Hanged Man. The reversal of physical posture serves as a very direct symbol of the reversal of attitude and experience that comes through spiritual awakening. Where everyone else is frenzied, you will know peace. Where other people believe themselves to be free, but are actually pushed from one thing to another by forces they do not understand, you will achieve true freedom by understanding and embracing those forces.

**English Paraphrase**:

**The Hanged Man** = **Voluntary Surrender**, **Reversed Values**, **Spiritual Peace** — acceptance after crisis, liberation through understanding.

**Core Symbolism**:
- **Number 12**: 21 backwards (turn card upside down = almost World Dancer), 2×6 (High Priestess raising Lovers to higher level), 4×3 (earth/consciousness dissolved in water/unconscious)
- **Upside down**: Reversal of worldview, turning world on its head

**Visual Elements** (Rider-Waite-Smith):
- **Man hanging by one foot** from T-shaped tree/gallows
- **Serene expression** = peace, not suffering
- **Halo/nimbus** around head = spiritual enlightenment entered him
- **Crossed legs** = number 4 upside down (earth/material world reversed)
- **Arms behind back** forming triangle = downward-pointing water triangle (path to super-conscious through unconscious)
- **T-shaped tree** = Tau cross, bottom half of ankh (Egyptian symbol of life), **World Tree**
- **Green background** = life, growth continuing

**Occult/Mythological Background**:

**Odin's sacrifice** (Norse):
- Hung himself on Yggdrasil (World Tree) for 9 days
- Pierced by his own spear
- Gained runes (magical knowledge) through voluntary suffering
- **Self-sacrifice for wisdom**

**Alchemical interpretation**:
- Standing on head = literally inverting body
- Gravity pulls energy from genitals to brain
- **Sexual energy transformed to spiritual energy**
- Physical reversal = symbol of **attitude reversal**

**T.S. Eliot's "The Wasteland"**:
- Made Hanged Man famous in 1920s
- "Drowned Phoenician Sailor" = esoteric original title
- Fisher King healed by "moment's surrender which age of prudence can never retract"
- "Fear death by drowning" = ego sees surrender as dissolution
- Hero's card but **"I do not find the Hanged Man"** = denied destiny

**Philosophical Meaning**:

**The World Tree**:
- **Roots** in underworld (unconscious)
- **Trunk** through physical world (conscious)
- **Branches** in heaven (super-conscious)
- Lovers' diagram now **actually happening** (concepts become experience)
- Tree of Life = ankh = life eternal

**Halfway to the World**:

Not one but **three cards** form midpoint:
1. **Wheel (10)**: Vision shown
2. **Justice (11)**: Response required
3. **Hanged Man (12)**: **Surrender/acceptance** — a **process** not moment

**Parallel to World Dancer**:
- Dancer extends arms with wands = awareness maintained in outer activity
- Hanged Man crosses arms behind back = awareness only maintained through withdrawal
- Both upside down figures, but Hanged Man inverted
- 12 vs. 21: Same digits, opposite order

**Initiation Sequence Continuation**:

After Justice's response comes **surrender**:
- Not passive waiting but **actual step taken**
- Modern: Releasing emotions locked up for years
- Ancient: Joining rituals instead of watching
- **Act of surrender** = voluntary, conscious choice

**Reversed Values**:

**What changes**:
- Where others frenzied → **you know peace**
- Where others think they're free (but pushed by unknown forces) → **you achieve true freedom** through understanding
- World's values → **reversed** (what they value, you transcend; what they fear, you embrace)

**Number symbolism**:

**Narrative Snippets**:
- `[ns_78deg_135]` `[trigger: hanged_man_major]` `[factor_trigger: tarot_major_hanged_man AND parallel_hanged_world AND planet_neptune AND tarot_number_12 AND symbol_hanged_man_halo]` `[role: 主干]` The Hanged Man represents voluntary surrender bringing spiritual peace—reversal of worldly values; the halfway point to World (12 vs 21). → English Paraphrase
- `[ns_78deg_136]` `[trigger: odin_myth]` `[factor_trigger: myth_odin_sacrifice]` `[role: 主干依赖]` Odin's sacrifice on World Tree—nine days self-wounded for runes/wisdom; the archetype of voluntary suffering for knowledge. → English Paraphrase
- `[ns_78deg_137]` `[trigger: world_tree]` `[factor_trigger: symbol_world_tree]` `[role: 条件分支]` T-shaped tree is Yggdrasil/World Tree—roots in unconscious, trunk in world, branches in super-conscious; axis mundi connecting realms. → English Paraphrase
- `[ns_78deg_374]` `[trigger: hanged_man_number_12]` `[factor_trigger: tarot_major_hanged_man AND number_12]` `[role: 条件分支]` Number 12 = 21 backwards (turn card upside down = almost World Dancer); 2×6 (High Priestess raising Lovers); 4×3 (earth dissolved in water). → Core Symbolism
- `[ns_78deg_375]` `[trigger: serene_expression]` `[factor_trigger: tarot_major_hanged_man AND symbol_serenity]` `[role: 条件分支]` Serene expression, not suffering—halo around head = spiritual enlightenment entered; crossed legs form inverted 4 (earth/matter reversed). → Visual Elements
- `[ns_78deg_376]` `[trigger: wasteland_reference]` `[factor_trigger: tarot_major_hanged_man AND literature_eliot]` `[role: 条件分支]` T.S. Eliot's Wasteland: "moment's surrender which age of prudence can never retract"—Fisher King healed; "Fear death by drowning" = ego sees surrender as dissolution. → Literary Reference
- `[ns_78deg_377]` `[trigger: reversed_values]` `[factor_trigger: tarot_major_hanged_man AND principle_reversal AND principle_reversed_values AND principle_voluntary_surrender]` `[role: 总结]` Reversed values: where others frenzied, you know peace; where others think they're free but are pushed by unknown forces, you achieve true freedom through understanding. → Philosophical Meaning
- `[ns_78deg_476]` `[trigger: alchemical_inversion]` `[factor_trigger: tarot_major_hanged_man AND principle_alchemy]` `[role: 条件分支]` Alchemical interpretation: standing on head inverts body; gravity pulls energy from genitals to brain; sexual energy transformed to spiritual—physical reversal symbolizes attitude reversal. → Occult Background
- `[ns_78deg_546]` `[trigger: three_midpoint_cards]` `[factor_trigger: tarot_major_hanged_man AND structure_midpoint AND principle_response_required]` `[role: 条件分支]` Three cards form midpoint, not one: Wheel (vision shown), Justice (response required), Hanged Man (surrender/acceptance)—a process not a moment; the initiation sequence completes here. → Philosophical Meaning
- `[ns_78deg_547]` `[trigger: act_of_surrender]` `[factor_trigger: tarot_major_hanged_man AND state_voluntary_surrender]` `[role: 条件分支]` Act of surrender is voluntary, conscious choice—not passive waiting but actual step taken; modern: releasing locked emotions; ancient: joining rituals instead of watching. → Initiation Sequence"""
    normalized_text_zh: str = """"""
    subject: str = "Card 12: The Hanged Man"
    factor_refs: list = ['tarot_major_hanged_man', 'tarot_number_12', 'principle_voluntary_surrender', 'symbol_world_tree', 'principle_reversed_values', 'myth_odin_sacrifice']
    
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
        l1_anchor="pt_v1.0.0_card_12__the_hanged_man_001_L1",
    )
    version: str = "1.0.0"
