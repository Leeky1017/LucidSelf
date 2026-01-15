"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.994757
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
    semantic_id="pt_v1.0.0_nine_of_wands__defensive_stren_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class NineOfWandsDefensiveStren(SemanticEntry):
    """
    **Visual Elements**:
- Figure with bandaged head holding wand
- Eight wands arranged behind like def...
    """
    
    original_text: str = """**Visual Elements**:
- Figure with bandaged head holding wand
- Eight wands arranged behind like defensive wall
- Watchful, wary posture
- Battle-worn but standing firm

**English Paraphrase**:

The **Nine of Wands** represents **defensive strength** born from past struggles. This is someone who has fought many battles and now guards against further attack. The figure is **wounded but unbowed**, experienced but wary.

**Core Symbolism**:
- **Bandaged head**: Wounded by past conflicts
- **Eight wands as barrier**: Defensive posture, prepared for next challenge
- **Standing alone**: Self-reliance through necessity
- **Wary stance**: Experience teaches caution

**Upright Meaning**:
- **Resilience**: Ability to endure and continue despite hardship
- **Defensive readiness**: Prepared for challenge, not seeking it
- **Hard-won strength**: Power through experience of struggle
- **Last stand**: Final reserves of energy, holding position
- **Paranoia risk**: Seeing threats everywhere from past trauma
- **Battle fatigue**: Exhaustion from constant vigilance

**Reversed/Challenged**:
- **Walls come down**: Unable to maintain defensive posture
- **Overwhelmed**: Defenses breached, last strength fails
- **Surrender**: Giving up the fight, sometimes wisely
- **Paranoia justified**: Real threats emerge when defenses drop

**完整中文诠释**:
**权杖九**=通过过去斗争而生的**防御力量**。这是打过多次战斗的人，现在防范进一步攻击。**受伤但不屈服**，经验丰富但警惕。**图像元素**：**绷带头部**=被过去冲突所伤；**八权杖如屏障**=防御姿态，准备迎接下次挑战；**独自站立**=必要的自力更生；**警惕姿态**=经验教导谨慎。**正位含义**：**韧性**（承受并继续的能力），**防御准备**（为挑战做准备，非寻求它），**艰苦赢得的力量**（通过斗争经验获得力量），**最后防线**（最后能量储备，坚守阵地），**偏执风险**（从过去创伤看到处处威胁），**战斗疲劳**（持续警惕的疲惫）。**逆位/挑战**：**防线倒塌**（无法维持防御姿态），**不堪重负**（防御被突破，最后力量失败），**投降**（放弃战斗，有时是明智的），**偏执被证实**（防御下降时真实威胁出现）。**心理层面**：**幸存者姿态**——来自坚韧的力量但承载慢性防御的代价。不同于骑士渴望战斗，权杖九出于必要和疲惫而战。

**Psychological Layer**: The **survivor's stance** - strength that comes from endurance but carries cost of chronic defensiveness. Unlike Knight's eager battle-seeking, Nine fights from necessity and exhaustion.

**Narrative Snippets**:
- `[ns_78deg_192]` `[trigger: nine_wands_defense]` `[factor_trigger: tarot_nine_wands AND state_defense]` `[role: 主干]` Nine of Wands represents defensive strength born from past struggles—wounded but unbowed, experienced but wary, guarding against further attack. → English Paraphrase
- `[ns_78deg_193]` `[trigger: bandaged_warrior]` `[factor_trigger: tarot_nine_wands AND symbol_bandage]` `[role: 条件分支]` Figure with bandaged head, eight wands as barrier—battle-worn but standing firm; experience teaches caution. → Visual Elements
- `[ns_78deg_194]` `[trigger: nine_wands_resilience]` `[factor_trigger: tarot_nine_wands AND state_resilience]` `[role: 主干]` Hard-won strength through experience of struggle—last stand, final reserves of energy, holding position against odds. → Upright Meaning
- `[ns_78deg_195]` `[trigger: nine_wands_reversed]` `[factor_trigger: tarot_nine_wands AND polarity_reversed]` `[role: 条件分支]` Reversed: walls come down, defenses breached, overwhelmed; or wise surrender—sometimes letting go is the answer. → Reversed Meaning
- `[ns_78deg_196]` `[trigger: survivor_archetype]` `[factor_trigger: tarot_nine_wands AND archetype_survivor]` `[role: 总结]` The survivor's stance—strength from endurance but at cost of chronic defensiveness; unlike Knight, fights from necessity not eagerness. → Psychological Layer
- `[ns_78deg_398]` `[trigger: paranoia_risk]` `[factor_trigger: tarot_nine_wands AND state_paranoia]` `[role: 例外处理]` Paranoia risk—seeing threats everywhere from past trauma; battle fatigue from constant vigilance; the shadow side of earned wariness. → Shadow Warning
- `[ns_78deg_399]` `[trigger: last_stand]` `[factor_trigger: tarot_nine_wands AND state_last_stand]` `[role: 条件分支]` Last stand—final reserves of energy, holding position against odds; the strength that remains when everything else is spent. → Upright Meaning
- `[ns_78deg_474]` `[trigger: eight_wands_barrier]` `[factor_trigger: tarot_nine_wands AND symbol_defensive_wall]` `[role: 条件分支]` Eight wands arranged behind like defensive wall—past battles become protection; experience forged into barrier; wounds transformed into armor. → Visual Elements
- `[ns_78deg_508]` `[trigger: watchful_stance]` `[factor_trigger: tarot_nine_wands AND state_vigilance]` `[role: 条件分支]` Watchful, wary posture—eyes scanning for the next threat; neither relaxed nor attacking, simply ready; the eternal guard who cannot rest. → Visual Elements"""
    normalized_text_zh: str = """"""
    subject: str = "Nine of Wands: Defensive Strength"
    factor_refs: list = ['quality', 'existing', 'state', 'existing', 'knowledge', 'existing', 'shadow', 'existing', 'archetype', 'existing']
    
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
        l1_anchor="pt_v1.0.0_nine_of_wands__defensive_stren_001_L1",
    )
    version: str = "1.0.0"
