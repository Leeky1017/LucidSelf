"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.192792
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
    semantic_id="tb_v1.0.0_form_and_temperament_of_the_bo_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class FormAndTemperamentOfTheBo(SemanticEntry):
    """
    **Source Text** (Lines 6236-6365):
> In regard to the body, therefore, it is in all cases requisite ...
    """
    
    original_text: str = """**Source Text** (Lines 6236-6365):
> In regard to the body, therefore, it is in all cases requisite to observe the oriental horizon, and to ascertain what planets may preside or have dominion over it... Saturn, when oriental, acts on the personal figure by producing a yellowish complexion and a good constitution; with black and curled hair... Jupiter ruling, when oriental, makes the person white or fair, with a clear complexion... Mars ascending gives a fair ruddiness... Venus operates in a manner similar to Jupiter, but more becomingly and gracefully.

**English Paraphrase (Primary Language)**:
**Physical form** is determined by:
1. **Planets ruling the ASC** and their oriental/occidental position
2. **The Moon** and her configurations
3. **Co-ascending fixed stars**

**Planetary effects on body** (Oriental vs Occidental):

| Planet | Oriental | Occidental |
|--------|----------|------------|
| Saturn | Yellow complexion, curly black hair, broad chest | Dark, thin, scanty hair |
| Jupiter | Fair, clear complexion, large eyes, dignified | Fair but less clear, baldness |
| Mars | Fair-ruddy, large, sturdy, blue/grey eyes | Simply ruddy, moderate, hairless |
| Venus | Graceful, beautiful, azure eyes | Similar but softer |
| Mercury | Yellow, proportionate, small eyes | White-fair, thin, squinting |

**Zodiacal quadrant effects**: Vernal = good complexion; Summer = ordinary, curly hair; Autumn = yellowish, slender; Winter = dark, straight hair.

**Complete Chinese Interpretation (Secondary Language)**:
**身体形态**由以下决定：
1. **主宰上升点的行星**及其东/西方位置
2. **月亮**及其配置
3. **共升恒星**

**行星对身体的影响**（东方 vs 西方）：

| 行星 | 东方 | 西方 |
|------|------|------|
| 土星 | 黄色肤色，卷曲黑发，宽胸 | 深色，瘦，稀发 |
| 木星 | 白皙，清澈肤色，大眼，尊贵 | 白皙但不太清澈，秃顶 |
| 火星 | 白皙-红润，高大，健壮，蓝/灰眼 | 简单红润，中等，无毛 |
| 金星 | 优雅，美丽，天蓝色眼睛 | 相似但更柔和 |
| 水星 | 黄色，匀称，小眼 | 白皙，瘦，斜视 |

**Core Points**:
- ASC ruler and Moon determine body
- Oriental planets = stronger physical influence
- Each planet produces specific complexion/build
- Zodiacal quadrants modify temperament
- Fixed stars co-ascending add features

**Narrative Snippets**:
- `[ns_tetra_iii018]` `[trigger: body_form]` `[factor_trigger: astro_planet_ruler_asc]` `[role: 主干]` Physical form is determined by planets ruling the ascendant—each planet produces distinctive features. → Source Text III.16
- `[ns_tetra_iii_bf]` `[trigger: body_form]` `[factor_trigger: body_form]` `[role: 效果]` Body form includes complexion, stature, hair, eyes—determined by ASC ruler's nature and oriental/occidental position. → Source Text III.16"""
    normalized_text_zh: str = """"""
    subject: str = "Form and Temperament of the Body (Chapter XVI)"
    factor_refs: list = ['body_form']
    
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
        book_id="tetrabiblos",
        chapter="",
        l1_anchor="tb_v1.0.0_form_and_temperament_of_the_bo_001_L1",
    )
    version: str = "1.0.0"
