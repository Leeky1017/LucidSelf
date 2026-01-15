"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.116172
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
    semantic_id="tis_v1.0.0_venus___love___harmony_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class VenusLoveHarmony(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Love Function | Apprecia...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Love Function | Appreciation | Core role |
| Venus vs Moon | Value vs need | Distinction |
| Aesthetic Sense | Beauty recognition | Function |
| Values Formation | Worth criteria | Development |

#### Source Text

"Venus symbolizes the urge to unite with that which is outside oneself. It's the astrological symbol of **love**—not emotional neediness (Moon), but genuine **attraction** and **appreciation** of beauty, of people, of experience itself."

#### English Paraphrase

**Venus** represents the **relationship and aesthetic function**—love, attraction, harmony, beauty, and values. It governs what we appreciate and how we relate.

**Primary Functions**:
- Love capacity: Ability to appreciate and connect with others
- Aesthetic sense: Recognition of beauty, art, harmony
- Values formation: What we consider worthwhile and precious
- Relationship style: How we approach connection and partnership

**Venus vs Moon**:
- **Moon** = emotional need, dependency, "I need you"
- **Venus** = appreciation, attraction, "I value you"
- Moon seeks security; Venus seeks beauty

**Dysfunction**: Vanity, superficiality, people-pleasing, avoidance of conflict, laziness

**Feeding**: Venus by sign reveals what creates sense of beauty and connection (e.g., Venus in Aries loves conquest-romance, Venus in Libra loves partnership-harmony)

**Venus in Houses**: Shows where we seek beauty and love (1st = self-beautification, 7th = partnership focus, 10th = career as art form)

#### Complete Chinese Interpretation

**金星**代表**关系和审美功能**——爱、吸引、和谐、美和价值。它主管我们欣赏什么以及如何联系。

**主要功能**：爱的能力（欣赏和连接他人的能力）、审美感（识别美、艺术、和谐）、价值形成（我们认为有价值和珍贵的东西）、关系风格（我们如何接近连接和伙伴关系）

**金星vs月亮**：
- **月亮** = 情感需求、依赖、"我需要你"
- **金星** = 欣赏、吸引、"我珍视你"
- 月亮寻求安全；金星寻求美

**功能失调**：虚荣、肤浅、取悦他人、回避冲突、懒惰

**喂养**：金星星座揭示创造美感和连接的方式（如白羊金星爱征服浪漫，天秤金星爱伙伴和谐）

**金星宫位**：显示我们在哪里寻求美和爱（第一宫=自我美化，第七宫=伙伴关系焦点，第十宫=职业作为艺术形式）

#### Core Points

- Venus = love/beauty/values function
- Appreciation not neediness (vs Moon)
- Governs relationships and aesthetics
- Shadow = superficiality and conflict-avoidance
- East parallel: Venus ≈ 正官/正印 (harmonious relating)

#### Detailed Explanation

Venus represents **love, beauty, and values**—the function that creates relationships and appreciates aesthetics. Forrest's key distinction: Venus **appreciates** rather than **needs** (that's Moon). Venus says "how beautiful!" while Moon says "I need this."

Venus governs what we find worthy of love and how we attract it. It shapes our **aesthetic sense** and **relationship style**—both what we're drawn to and how we present ourselves to attract. Venus creates harmony, pleasure, and connection through appreciation rather than grasping.

**Dysfunction** appears as superficiality (valuing appearance over substance) or excessive conflict-avoidance (sacrificing truth for peace). Healthy Venus creates genuine appreciation and harmonious relationships without losing authenticity.

#### Narrative Snippets

- `[ns_innersky_venus_001]` `[trigger: planet_venus]` `[factor_trigger: planet_venus AND venus_love_function]` `[role: 主干]` Venus is the planet of love, beauty, and values—the function that creates relationships and appreciates aesthetics. It represents the capacity to connect not from neediness but from appreciation. → The Inner Sky Ch.6 #Venus
- `[ns_innersky_venus_002]` `[trigger: planet_venus AND astro_function]` `[factor_trigger: astro_planet_venus]` `[role: 主干依赖]` Venus governs what we find beautiful, valuable, and worthy of love. It forms our aesthetic sense and relationship style—how we attract and what attracts us. → The Inner Sky Ch.6 #Venus
- `[ns_innersky_venus_003]` `[trigger: planet_venus AND astro_contrast]` `[factor_trigger: astro_planet_venus]` `[role: 条件分支]` Venus vs Moon: Venus appreciates (active connection), Moon needs (passive reception). Venus says "how beautiful!" Moon says "I need this to be happy." → The Inner Sky Ch.6 #Venus
- `[ns_innersky_venus_004]` `[trigger: planet_venus AND astro_shadow]` `[factor_trigger: astro_planet_venus AND astro_state_dysfunction]` `[role: 总结]` Dysfunction: superficiality (appearance over substance), conflict-avoidance (peace at any cost), vanity (love of being loved rather than loving). → The Inner Sky Ch.6 #Venus"""
    normalized_text_zh: str = """"""
    subject: str = "Venus - Love & Harmony"
    factor_refs: list = ['planet_venus', 'venus_love_function', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="tis_v1.0.0_venus___love___harmony_001_L1",
    )
    version: str = "1.0.0"
