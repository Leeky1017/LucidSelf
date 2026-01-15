"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.994728
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
    semantic_id="pt_v1.0.0_king_of_wands__mature_fire_aut_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class KingOfWandsMatureFireAut(SemanticEntry):
    """
    **Visual Elements**:
- King on throne leaning forward
- Salamander (fire creature) on robe and thron...
    """
    
    original_text: str = """**Visual Elements**:
- King on throne leaning forward
- Salamander (fire creature) on robe and throne
- Desert landscape
- Lion imagery (fire/Leo association)
- Confident, commanding posture

**English Paraphrase**:

The **King of Wands** embodies **mature fire energy** - leadership through force of will, natural authority, and unshakeable confidence. He represents someone who **leads by example**, expects others to follow because his vision is clear and his energy infectious.

**Core Symbolism**:
- **Leaning forward**: Despite authority, still eager for action/experience
- **Salamander**: Mastery of fire element (salamanders mythically live in flames)
- **Desert setting**: Fire without water's softening - can be harsh
- **Crown + cap of maintenance**: Authority with responsibility
- **Confidence**: Natural belief in own rightness

**Upright Meaning**:
- **Charismatic leadership**: Dominates through personality, not force
- **Vision & direction**: Sees path clearly, inspires others to follow
- **Entrepreneurial energy**: Builder, creator, doer
- **Honest & direct**: Sees no value in deception
- **Optimistic authority**: "If I can do it, you can" attitude
- **Controlled fire**: Wands energy harnessed for long-term goals

**Reversed/Challenged**:
- **Intolerance**: Unable to understand weakness, impatient with others
- **Harshness**: Fire tempered by obstacles, becomes severe
- **Dogmatism**: Certainty becomes rigidity
- **Burnt out**: Constant action exhausts even strong fire
- **Overbearing**: Dominance turns oppressive

**完整中文诠释**:
**权杖国王**=**成熟火能量化身**——通过意志力领导、自然权威、不可动摇信心。他代表**以身作则**的人，期待他人跟随因为他的愿景清晰、能量有感染力。**图像元素**：**前倾姿态**=尽管有权威仍渴望行动/经验；**火蜥蜴**=掌握火元素（神话中火蜥蜴住在火焰里）；**沙漠环境**=火无水之软化可显严酷；**王冠+加冕帽**=权威伴随责任；**自信姿态**=对自身正确性的自然信念。**正位含义**：**魅力领导**（通过人格而非武力统治），**愿景与方向**（清晰看到道路，激励他人跟随），**企业家能量**（建造者、创造者、实干家），**诚实直接**（看不到欺骗的价值），**乐观权威**（"我能做到你也能"的态度），**受控之火**（权杖能量被驾驭用于长期目标）。**逆位/挑战**：**不宽容**（无法理解弱点，对他人不耐烦），**严酷**（火被障碍淬炼变得严厉），**教条主义**（确信变成僵化），**倦怠**（持续行动耗尽即使强火），**专横**（主导变成压迫）。**人格类型**：**企业家**、**愿景领袖**、**教练**。对维持现状不感兴趣——总是在建造、总是向前。可以是激励导师或压倒性力量。

**Personality Type**: The **entrepreneur**, **visionary leader**, **coach**. Not interested in maintaining status quo - always building, always moving forward. Can be inspiring mentor or overwhelming force.

**In Readings**:
- Person: Strong-willed leader figure entering life
- Quality: Need to embody confident, decisive energy
- Advice: Lead by example, trust your vision
- Warning: Check for intolerance or harshness

**Narrative Snippets**:
- `[ns_78deg_182]` `[trigger: king_wands_leadership]` `[factor_trigger: tarot_king_wands AND state_leadership]` `[role: 主干]` King of Wands embodies mature fire energy—leadership through force of will, natural authority, unshakeable confidence; leads by example. → English Paraphrase
- `[ns_78deg_183]` `[trigger: salamander_mastery]` `[factor_trigger: tarot_king_wands AND symbol_salamander]` `[role: 条件分支]` Salamander on robe and throne—mythical fire creature living in flames; symbolizes complete mastery of fire element. → Core Symbolism
- `[ns_78deg_184]` `[trigger: king_wands_vision]` `[factor_trigger: tarot_king_wands AND state_vision]` `[role: 主干]` Charismatic leadership—dominates through personality not force; sees path clearly and inspires others to follow; entrepreneur, builder, doer. → Upright Meaning
- `[ns_78deg_185]` `[trigger: king_wands_reversed]` `[factor_trigger: tarot_king_wands AND polarity_reversed]` `[role: 条件分支]` Reversed: intolerance, harshness, dogmatism, burnt out from constant action, dominance becoming oppressive. → Reversed Meaning
- `[ns_78deg_186]` `[trigger: entrepreneur_archetype]` `[factor_trigger: tarot_king_wands AND archetype_entrepreneur]` `[role: 总结]` The entrepreneur, visionary leader, coach—not interested in maintaining status quo; always building, always moving forward. → Personality Type
- `[ns_78deg_400]` `[trigger: desert_landscape]` `[factor_trigger: tarot_king_wands AND symbol_desert]` `[role: 条件分支]` Desert setting—fire without water's softening, can be harsh; pure will untempered by emotion; the price of uncompromising vision. → Visual Elements
- `[ns_78deg_401]` `[trigger: forward_lean]` `[factor_trigger: tarot_king_wands AND state_eagerness]` `[role: 条件分支]` King leans forward despite authority—still eager for action and experience; mastery doesn't mean rest; controlled fire still burns bright. → Core Symbolism
- `[ns_78deg_479]` `[trigger: lion_salamander]` `[factor_trigger: tarot_king_wands AND symbol_lion]` `[role: 条件分支]` Lion imagery (Leo/fire association)—the solar king whose natural authority comes from within; salamanders on robe show fire that has become one's element, not merely controlled. → Visual Elements
- `[ns_78deg_510]` `[trigger: infectious_energy]` `[factor_trigger: tarot_king_wands AND state_inspiring]` `[role: 条件分支]` Infectious confident energy—expects others to follow because vision is clear; "If I can do it, you can" attitude; inspires through lived example not mere words. → Upright Meaning"""
    normalized_text_zh: str = """"""
    subject: str = "King of Wands: Mature Fire Authority"
    factor_refs: list = ['quality', 'existing', 'force', 'existing', 'presence', 'existing', 'attainment', 'existing', 'shadow', 'existing']
    
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
        l1_anchor="pt_v1.0.0_king_of_wands__mature_fire_aut_001_L1",
    )
    version: str = "1.0.0"
