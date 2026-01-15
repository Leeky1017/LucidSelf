"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.116184
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
    semantic_id="tis_v1.0.0_mars___will___assertiveness_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class MarsWillAssertiveness(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Warrior Energy | Action ...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Warrior Energy | Action capacity | Core role |
| Mars vs Sun | Execute vs identity | Distinction |
| Courage | Face fear | Function |
| Sexuality | Physical desire | Expression |

#### Source Text

"Mars symbolizes **courage, assertiveness, and the capacity for action**. It represents the warrior in us—not mindless aggression, but the ability to fight for what we want, to assert our will, to take risks, to move forward despite fear."

#### English Paraphrase

**Mars** represents the **action and will function**—courage, assertiveness, sexuality, and the capacity to overcome obstacles. It's the warrior energy enabling us to act decisively.

**Primary Functions**:
- Willpower: Capacity to assert oneself and take action
- Courage: Ability to face fear and move forward anyway
- Sexuality: Physical desire and sexual expression
- Conflict navigation: How we handle confrontation and competition

**Mars vs Sun**:
- **Sun** = identity and purpose ("who I am")
- **Mars** = action and will ("what I do")
- Sun is the general; Mars is the soldier executing

**Dysfunction**: Aggression, violence, impulsiveness, anger, recklessness, domination

**Feeding**: Mars by sign reveals how to channel warrior energy constructively (e.g., Mars in Capricorn needs disciplined challenges, Mars in Pisces needs spiritual/artistic battles)

**Mars Retrograde**: Warrior energy directed inward, passive-aggressive tendencies, difficulty asserting openly

#### Complete Chinese Interpretation

**火星**代表**行动和意志功能**——勇气、果断、性欲和克服障碍的能力。它是使我们果断行动的战士能量。

**主要功能**：意志力（自我主张和采取行动的能力）、勇气（面对恐惧仍前进的能力）、性欲（身体欲望和性表达）、冲突导航（我们如何处理对抗和竞争）

**火星vs太阳**：
- **太阳** = 身份和目的（"我是谁"）
- **火星** = 行动和意志（"我做什么"）
- 太阳是将军；火星是执行的士兵

**功能失调**：攻击性、暴力、冲动、愤怒、鲁莽、支配

**喂养**：火星星座揭示如何建设性地引导战士能量（如摩羯火星需纪律挑战，双鱼火星需精神/艺术战斗）

**火星逆行**：战士能量向内，被动攻击倾向，难以公开自我主张

#### Core Points

- Mars = action/will/courage function
- Warrior energy for overcoming obstacles
- Executor of Sun's will (soldier vs general)
- Shadow = aggression and recklessness
- East parallel: Mars ≈ 七杀/羊刃 (assertive force)

#### Detailed Explanation

Mars is the **warrior**—the planet of action, courage, will, and desire. It enables decisive action and overcoming obstacles through directed force. Where the Sun is the general (knowing what we want), Mars is the **soldier** (executing the will).

Without Mars, we know our desires but cannot act on them. With healthy Mars, **desire becomes deed**. Mars governs sexuality as **assertive desire** (versus Venus's receptive attraction)—the penetrating, pursuing aspect of sexual energy.

**Dysfunction** appears as aggression, recklessness, or violence—Mars energy without wisdom or restraint. Alternatively, blocked Mars creates passivity, inability to assert, or passive-aggressive expression. **Healthy Mars** means courage and decisive action in service of the Sun's vision.

#### Narrative Snippets

- `[ns_innersky_mars_001]` `[trigger: planet_mars]` `[factor_trigger: planet_mars AND mars_will_function]` `[role: 主干]` Mars is the warrior of the birthchart—the planet of action, courage, will, and desire. It enables decisive action and overcoming obstacles through directed force. → The Inner Sky Ch.6 #Mars
- `[ns_innersky_mars_002]` `[trigger: planet_mars AND astro_function]` `[factor_trigger: planet_mars AND planet_sun]` `[role: 主干依赖]` Mars is the soldier to the Sun's general—it executes the will. Without Mars, we know what we want but cannot act. With Mars, desire becomes deed. → The Inner Sky Ch.6 #Mars
- `[ns_innersky_mars_003]` `[trigger: planet_mars AND astro_sexuality]` `[factor_trigger: astro_planet_mars]` `[role: 条件分支]` Mars governs sexuality as assertive desire (vs Venus's receptive attraction). It represents the aggressive, penetrating aspect of sexual energy. → The Inner Sky Ch.6 #Mars
- `[ns_innersky_mars_004]` `[trigger: planet_mars AND astro_shadow]` `[factor_trigger: astro_planet_mars AND astro_state_dysfunction]` `[role: 总结]` Dysfunction: aggression (uncontrolled anger), recklessness (action without thought), violence (force without purpose), cowardice (Mars denied). → The Inner Sky Ch.6 #Mars"""
    normalized_text_zh: str = """"""
    subject: str = "Mars - Will & Assertiveness"
    factor_refs: list = ['planet_mars', 'mars_will_function', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="tis_v1.0.0_mars___will___assertiveness_001_L1",
    )
    version: str = "1.0.0"
