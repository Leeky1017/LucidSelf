"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.119270
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
    semantic_id="tis_v1.0.0_the_sun___identity___ego_forma_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class TheSunIdentityEgoForma(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Gravitational Center | E...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Gravitational Center | Ego organizer | Core metaphor |
| Ego Formation | Creating "I am" | Primary function |
| Solar Feeding | Sign-specific nourishment | Development |
| Unconscious Assumptions | Bedrock beliefs | Mechanism |

#### Source Text

"The sun is the gravitational center of the human personality. It is the focal point of all the varied functions that coexist in each person: our sense of identity, our sense of being a distinct person with certain ways of feeling and seeing, of shaping a life. The sun organizes the nine remaining planetary functions through its psychological 'gravity': ego."

#### English Paraphrase

**The Sun** represents the **core identity function**—the gravitational center creating **ego** (sense of "I am"). Just as the physical Sun organizes the solar system, the psychological Sun organizes all mental functions through ego-formation.

**Primary Functions**:
- Identity development: Creating coherent self-image
- Willpower focus: Directing conscious intention
- Ego construction: Establishing awareness focal point
- Purpose definition: Installing core life assumptions

**How It Works**: The Sun creates ego by implanting unconscious assumptions about what matters, forming the unspoken bedrock beneath every thought.

**Dysfunction**: Egocentrism, tyranny, rigidity, vanity

**Feeding**: Sun's sign reveals experiences that nourish ego (e.g., Sun in Aries needs conquests, Sun in Cancer needs emotional connections)

#### Complete Chinese Interpretation

**太阳**代表**核心身份功能**——创建**自我**（"我是谁"感觉）的引力中心。正如物理太阳组织太阳系，心理太阳通过自我形成组织所有心智功能。

**主要功能**：身份发展（创建连贯自我形象）、意志聚焦（引导有意识意图）、自我建构（建立意识焦点）、目的定义（植入核心生命假设）

**运作方式**：太阳通过在无意识层植入关于什么重要的假设来创建自我，形成每个思想下的无言基石。

**功能失调**：自我中心主义、专制、僵化、虚荣

**喂养**：太阳星座揭示滋养自我的经验（如白羊太阳需征服，巨蟹太阳需情感连接）

#### Core Points

- Sun = ego center creating identity through unconscious assumptions
- Sign = vitamin prescription for ego strength
- Shadow = egocentrism and blindness
- East parallel: Sun ≈ 日主 (Day Master)

#### Detailed Explanation

The Sun represents the **gravitational center** of the personality—the ego that creates a coherent sense of identity from the chaos of competing drives. Forrest's key insight is that the Sun works by implanting **unconscious assumptions** about what matters. We don't consciously choose our identity; the Sun creates it by making certain things seem automatically important.

The Sun's **sign** acts as a "vitamin prescription" for ego health. Different signs need different experiences to feel strong. Sun in Aries needs conquests and challenges; Sun in Cancer needs emotional connections and belonging. Without the experiences matching the sign, the ego weakens and identity becomes fragile.

**Dysfunction** appears as egocentrism: confusing one's own center for **the** center. The starved Sun produces either inflation (tyrant, narcissist) or deflation (weak identity, no center). The healthy Sun creates a strong but permeable identity—confident without being rigid.

#### Narrative Snippets

- `[ns_innersky_sun_001]` `[trigger: planet_sun]` `[factor_trigger: planet_sun AND sun_ego_function]` `[role: 主干]` The sun is the gravitational center of the human personality—the focal point of all varied functions that coexist in each person: our sense of identity, of being a distinct person with certain ways of feeling and seeing. → The Inner Sky Ch.6 #Sun
- `[ns_innersky_sun_002]` `[trigger: planet_sun AND astro_function]` `[factor_trigger: zodiac_sign AND sun_ego_function]` `[role: 主干依赖]` The sun organizes the nine remaining planetary functions through its psychological 'gravity': ego. It creates identity by implanting unconscious assumptions about what matters. → The Inner Sky Ch.6 #Sun
- `[ns_innersky_sun_003]` `[trigger: planet_sun AND astro_feeding]` `[factor_trigger: astro_planet_sun]` `[role: 条件分支]` Sun's sign reveals experiences that nourish ego—like a vitamin prescription. Sun in Aries needs conquests, Sun in Cancer needs emotional connections. → The Inner Sky Ch.6 #Sun
- `[ns_innersky_sun_004]` `[trigger: planet_sun AND astro_shadow]` `[factor_trigger: astro_planet_sun AND astro_state_dysfunction]` `[role: 总结]` Dysfunction: egocentrism (confusing one's center for the center), tyranny, rigidity, vanity. When the Sun is starved, identity weakens. → The Inner Sky Ch.6 #Sun"""
    normalized_text_zh: str = """"""
    subject: str = "The Sun - Identity & Ego Formation"
    factor_refs: list = ['planet_sun', 'sun_ego_function', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="tis_v1.0.0_the_sun___identity___ego_forma_001_L1",
    )
    version: str = "1.0.0"
