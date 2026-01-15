"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.096781
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
    semantic_id="tis_v1.0.0_aries___the_warrior__cardinal__001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class AriesTheWarriorCardinal(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Cardinal Fire | Initiati...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Cardinal Fire | Initiating energy | Element |
| Annihilation Fear | Primal terror | What to face |
| Right War | Defend authentic self | Strategy |
| Existential Aloneness | Standing alone | Condition |

#### Source Text

"Aries is a newborn tumbling into physical existence. Every cell screaming: 'Am I going to make it?' Fear of annihilation: the basic Arian experience. The endpoint is fearlessness—not from stupidity but real courage: to be terrified and still step forward. The heart of Arian strategy is standing alone."

#### English Paraphrase

**Aries** = **Cardinal Fire** sign embodying **courage, independence, and pioneering spirit**. The Ram archetype: newborn facing primal terror of annihilation, forging fearlessness through direct confrontation.

**Core Drives**:
- **Face Fear Head-On**: Cultivate high-stress experience as warrior training
- **Stand Alone**: Maintain existential aloneness, defend inner self against conformity
- **Act Immediately**: Think with body, let adrenaline answer questions NOW
- **Fight Right War**: Defend authentic self, not random conflicts

**Arian Strengths**:
- **Speed**: Fast physically and mentally (into and out of trouble before others think)
- **Spontaneity**: Life in present tense, no mulling or strategizing
- **Courage**: Willingness to burn bridges, cut losses quickly
- **Impetuousness**: Race-car driver/boxer mentality—everything must be done now

**Shadow Manifestations**:
- **Chronic Fear**: Pathetic self-defeating terror when refusing to fight
- **Wrong War**: Lashing out randomly, creating pointless conflicts
- **Flight**: Obsessive caution, avoiding all risks
- **Self-Pity**: "Why does everyone become defensive?" (Fought wrong battle)

**Evolutionary Challenge**:
Become true warrior—choose to meet terrors head-on maintaining clarity. Fight for inner self, not against conformity pressure. Stand alone WITHOUT fighting wrong wars.

#### Complete Chinese Interpretation

**白羊座**=**基本火象**星座体现**勇气、独立和先锋精神**。公羊原型：面对湮灭原始恐惧的新生儿，通过直接对抗锻造无畏。

**核心驱力**：正面面对恐惧(培养高压经验作战士训练)；独自站立(保持存在孤独、捍卫内在自我抵抗从众)；立即行动(用身体思考、让肾上腺素现在回答问题)；打对的战(捍卫真实自我、非随机冲突)

**白羊优势**：速度(身体和心智快-在他人思考前进出麻烦)；自发性(当下生活、无深思或策略)；勇气(愿意烧桥、快速止损)；冲动性(赛车手/拳击手心态——一切必须现在做)

**阴影显化**：慢性恐惧(拒绝战斗时可怜自我毁灭恐怖)；错误战争(随机爆发、创造无意义冲突)；逃跑(痴迷谨慎、避免所有风险)；自怜("为何人人防御？"-打错了战)

**进化挑战**：成为真战士——选择正面遇见恐怖保持清晰。为内在自我战、非对抗从众压力。独自站立不打错误战争。

#### Core Points

- Cardinal Fire: pioneering courage through terror confrontation
- Archetype: newborn warrior facing annihilation fear
- Resources: speed, spontaneity, courage, impetuousness
- Shadow: chronic fear, wrong wars, flight, self-pity
- Challenge: fight RIGHT war (defend authentic self)
- East parallel: 白羊↔甲木阳刚/比肩独立 (yang wood independence)

#### Detailed Explanation

Aries is **Cardinal Fire**—initiating courage through confronting primal terror. The archetype is the **newborn warrior** tumbling into physical existence, every cell screaming "Am I going to make it?" Fear of annihilation is the basic Arian experience.

Aries' resources include **speed, spontaneity, courage, and impetuousness**—the willingness to act before fear paralyzes. The endpoint is **fearlessness**: not stupidity but real courage, to be terrified and still step forward.

**Dysfunction** appears as chronic fear (never confronting terror), fighting wrong wars (proving self to others instead of defending authentic self), flight (running rather than facing), or self-pity (wallowing in victimhood). The evolutionary challenge is to **fight the RIGHT war**—standing alone for the inner self.

#### Narrative Snippets

- `[ns_innersky_aries_001]` `[trigger: sign_aries]` `[factor_trigger: astro_sign_aries]` `[role: 主干]` Aries is a newborn tumbling into physical existence. Every cell screaming: 'Am I going to make it?' Fear of annihilation: the basic Arian experience. → The Inner Sky Ch.4 #Aries
- `[ns_innersky_aries_002]` `[trigger: sign_aries AND astro_strength]` `[factor_trigger: astro_sign_aries]` `[role: 主干依赖]` The endpoint is fearlessness—not from stupidity but real courage: to be terrified and still step forward. Speed, spontaneity, and willingness to burn bridges. → The Inner Sky Ch.4 #Aries
- `[ns_innersky_aries_003]` `[trigger: sign_aries AND astro_shadow]` `[factor_trigger: astro_sign_aries AND astro_state_dysfunction]` `[role: 条件分支]` Shadow: chronic fear (pathetic self-defeating terror when refusing to fight), wrong war (lashing out randomly), flight (obsessive caution avoiding all risks). → The Inner Sky Ch.4 #Aries
- `[ns_innersky_aries_004]` `[trigger: sign_aries AND astro_challenge]` `[factor_trigger: astro_sign_aries]` `[role: 总结]` The heart of Arian strategy is standing alone. Fight the RIGHT war: defend authentic self, not random conflicts. Become true warrior maintaining clarity. → The Inner Sky Ch.4 #Aries"""
    normalized_text_zh: str = """"""
    subject: str = "Aries - The Warrior (Cardinal Fire)"
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
        l1_anchor="tis_v1.0.0_aries___the_warrior__cardinal__001_L1",
    )
    version: str = "1.0.0"
