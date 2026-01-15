"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.119307
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
    semantic_id="tis_v1.0.0_the_moon___emotional_soul_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class TheMoonEmotionalSoul(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Feeling Function | Emoti...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Feeling Function | Emotional response | Core role |
| Variability | Always changing | Nature |
| Soul vs Ego | Fluid vs fixed | Contrast |
| Lunar Feeding | Sign-specific needs | Development |

#### Source Text

"The moon symbolizes feelings. Its most striking quality is variability—always changing, always passing through phases. Luna symbolizes the part of consciousness that reacts and responds, that is sensitive to its surroundings. It represents the mood of the psyche—the way life feels."

#### English Paraphrase

**The Moon** represents the **feeling function**—emotional, responsive, subjective consciousness. Where Sun creates fixed ego, Moon creates fluid soul.

**Primary Functions**:
- Emotional development: Capacity to feel and respond
- Subjectivity formation: Impressionability and sensitivity
- Soul nourishment: Happiness and fulfillment
- Imagination: Dreams, fantasy, unconscious content

**Moon vs Sun**: Moon adjusts (responsive) vs Sun dominates (active); Moon feels vs Sun acts; Moon is variable vs Sun is stable

**Feeding**: Moon's sign reveals emotional needs (e.g., Moon in Leo needs applause, Moon in Scorpio needs intensity)

**Dysfunction**: Self-indulgence, moodiness, timidity, indecision, fantasy-escape

#### Complete Chinese Interpretation

**月亮**代表**感觉功能**——意识的情感、反应、主观维度。太阳创建固定自我，月亮创建流动灵魂。

**主要功能**：情感发展（感受和回应能力）、主观性形成（印象性和敏感性）、灵魂滋养（幸福和满足）、想象（梦境、幻想、无意识内容）

**月亮vs太阳**：月亮适应（回应性）vs太阳主导（主动）；月亮感受vs太阳行动；月亮可变vs太阳稳定

**喂养**：月亮星座揭示情感需求（如狮子月亮需掌声，天蝎月亮需强度）

**功能失调**：自我放纵、情绪化、胆怯、优柔寡断、幻想逃避

#### Core Points

- Moon = soul/feelings creating emotional response
- Variable nature: responsive not dominating
- Sign = emotional need prescription
- Shadow = overwhelm and indecision
- East parallel: Moon ≈ 心 (Heart-Mind)

#### Detailed Explanation

The Moon represents **feelings, soul, and emotional response**. Unlike the Sun's fixed ego, the Moon is inherently **variable**—always changing, always passing through phases. It symbolizes the part of consciousness that reacts and responds rather than initiating.

Where the Sun creates identity through unconscious assumptions, the Moon creates **mood**—the way life feels moment to moment. It generates happiness, emotional fulfillment, and the sense of being at home in oneself. The Moon's sign reveals emotional needs: Leo Moon needs applause, Scorpio Moon needs intensity.

**Dysfunction** appears as being overwhelmed by feelings, indecisiveness, or escapism into fantasy. The Moon's variability becomes problematic when there's no stable center (Sun) to contain it. **Healthy** lunar function means being emotionally responsive without being ruled by every passing feeling.

#### Narrative Snippets

- `[ns_innersky_moon_001]` `[trigger: planet_moon]` `[factor_trigger: planet_moon AND moon_feeling_function]` `[role: 主干]` The moon symbolizes feelings. Its most striking quality is variability—always changing, always passing through phases. Luna symbolizes the part of consciousness that reacts and responds. → The Inner Sky Ch.6 #Moon
- `[ns_innersky_moon_002]` `[trigger: planet_moon AND astro_function]` `[factor_trigger: astro_planet_moon]` `[role: 主干依赖]` The Moon represents the mood of the psyche—the way life feels. Where Sun creates fixed ego, Moon creates fluid soul. It generates happiness and emotional fulfillment. → The Inner Sky Ch.6 #Moon
- `[ns_innersky_moon_003]` `[trigger: planet_moon AND astro_feeding]` `[factor_trigger: astro_planet_moon]` `[role: 条件分支]` Moon's sign reveals emotional needs. Moon in Leo needs applause and recognition, Moon in Scorpio needs emotional intensity and depth. → The Inner Sky Ch.6 #Moon
- `[ns_innersky_moon_004]` `[trigger: planet_moon AND astro_shadow]` `[factor_trigger: astro_planet_moon AND astro_state_dysfunction]` `[role: 总结]` Dysfunction: self-indulgence, moodiness, timidity, indecision, fantasy-escape. Moon without healthy outlets becomes overwhelmed by feeling. → The Inner Sky Ch.6 #Moon"""
    normalized_text_zh: str = """"""
    subject: str = "The Moon - Emotional Soul"
    factor_refs: list = ['planet_moon', 'moon_feeling_function', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="tis_v1.0.0_the_moon___emotional_soul_001_L1",
    )
    version: str = "1.0.0"
