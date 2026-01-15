"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.559151
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
    semantic_id="acu_v1.0.0_第1_75节_曼陀罗象征的形式要素与早期案例___644_6_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 第175节曼陀罗象征的形式要素与早期案例6446(SemanticEntry):
    """
    **原文** (¶644-649, 行10005-10052):

> [646] The formal elements of mandala symbolism are: (1) Circular...
    """
    
    original_text: str = """**原文** (¶644-649, 行10005-10052):

> [646] The formal elements of mandala symbolism are: (1) Circular, spherical, or egg-shaped formation. (2) The circle elaborated into flower (rose, lotus) or wheel. (3) A centre expressed by sun, star, or cross, usually with four, eight, or twelve rays. (4) Circles, spheres, and cruciform figures often in rotation (swastika). (5) The circle represented by a snake coiled about centre, ring-shaped (uroboros) or spiral (Orphic egg). (6) Squaring of the circle. (7) Castle, city, and courtyard (temenos) motifs. (8) Eye (pupil and iris). (9) Besides tetradic figures, triadic and pentadic ones (rare)—"disturbed" totality pictures.
>
> [647-649] A middle-aged woman patient first saw her mandala in a dream: "One must go around and around the square until near the centre, then go in circles." The spiral is painted in red, green, yellow, and blue—the four basic colours. The square in the centre represents a stone with four facets. The inner spiral represents the snake that, like Kundalini, winds three and a half times round the centre. The dreamer had no notion of what was going on in her—the beginning of a new orientation. The parallels from Eastern symbolism were completely unknown to her.

**英文释义**：
- 曼陀罗形式要素：圆/球/蛋形；花（玫瑰/莲花）或轮；中心=太阳/星/十字（4/8/12射线）
- 旋转（卐）；蛇环绕中心（衔尾蛇/俄耳甫斯蛋）
- 圆的方化；城堡/城市/庭院（temenos）；眼睛
- 四元/三元/五元（稀有 = "扰乱的"整体图）
- 梦：绕方形走直到接近中心，然后转圈
- 螺旋四色（红/绿/黄/蓝）；中心方石四面
- 内螺旋 = 昆达里尼蛇，绕中心三圈半
- 做梦者不知道发生什么——新方向的开始
- 东方象征完全不知

**中文诠释**：
- 曼陀罗形式要素九点：
- 1.圆/球/蛋形 2.花（玫瑰/莲花）或轮
- 3.中心=太阳/星/十字（4/8/12射线）
- 4.旋转（卐） 5.蛇环绕中心
- 6.圆的方化 7.城堡/城市/temenos
- 8.眼睛 9.三元/五元（稀有=扰乱整体）
- 梦：绕方形走→转圈→接近中心
- 螺旋四基色；中心方石四面
- 昆达里尼蛇绕中心三圈半
- 做梦者不知道发生什么——新方向开始

**Narrative Snippets**:
- `[ns_cw9i_X_646]` `[trigger: mandala_formal]` `[factor_trigger: jung_jung_yantra]` `[role: 主干]` Mandala formal elements: circle/sphere/egg, flower/wheel, centre with rays, rotation, snake, squaring of circle, temenos, eye. → ¶646
- `[ns_cw9i_X_648]` `[trigger: kundalini_spiral]` `[factor_trigger: jung_mandala_center]` `[role: 条件分支]` The inner spiral = Kundalini snake winding three and a half times round the centre stone. → ¶648"""
    normalized_text_zh: str = """"""
    subject: str = "第1.75节：曼陀罗象征的形式要素与早期案例 (¶644-649)"
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
        book_id="archetypes_unconscious",
        chapter="",
        l1_anchor="acu_v1.0.0_第1_75节_曼陀罗象征的形式要素与早期案例___644_6_001_L1",
    )
    version: str = "1.0.0"
