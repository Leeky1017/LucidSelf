"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237916
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
    semantic_id="ap_v1.0.0_entry_6__birth_chart_as_mandal_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry6BirthChartAsMandal(SemanticEntry):
    """
    **Source Text** (Lines 4276-4288):
> The great symbol of individuation is the mandala: that is, a ma...
    """
    
    original_text: str = """**Source Text** (Lines 4276-4288):
> The great symbol of individuation is the mandala: that is, a magic circle containing a cross or some other basically four-fold formation. Such a symbol is the zodiac—and the typical quadrature of an astrological chart (the 4 angles). All natal astrology is the practical application of this "squaring of the circle"—the conscious Way: Tao. Fourfold T-A-O gives the 12 signs or houses of astrology (3 × 4 = 12). Every birth-chart is the mandala of an individual life. It is the blue-print of the process of individuation for this particular individual. To follow it understandingly is to follow the "conscious way;" the way of "operative wholeness;" that is, the way of the active fulfillment of the wholeness of being that is Self.

**Key Term Analysis**:
- **Mandala**: `symbol of individuation` / `magic circle with cross` / `4-fold formation`
- **Zodiac as mandala**: `4 angles` / `squaring circle` / `Tao` / `3×4=12`
- **Birth-chart**: `mandala of individual life` / `blueprint of individuation` / `conscious way`

**English Paraphrase (Primary Language)**:
Jung's individuation symbol is the mandala—"magic circle containing a cross or some other basically four-fold formation." The zodiac is such a symbol; the 4 angles constitute its cross. "All natal astrology is the practical application of this 'squaring of the circle'—the conscious Way: Tao."

"Every birth-chart is the mandala of an individual life. It is the blue-print of the process of individuation for this particular individual." Following the chart = following "operative wholeness"—the active fulfillment of Self.

**Complete Chinese Interpretation (Secondary Language)**:
Jung的个体化符号是曼荼罗——"包含十字或其他基本四重结构的魔法圆"。黄道是这样一个符号；四角构成其十字。"所有本命占星学都是这种'化圆为方'的实践应用——有意识之道：道。"

"每张出生图都是一个个体生命的曼荼罗。它是这个特定个体的个体化过程的蓝图。"遵循星图=遵循"运作的整体性"——自性之存在的整体性的积极实现。

**Narrative Snippets**:
- `[ns_aop_121]` `[trigger: mandala_zodiac]` `[factor_trigger: astro_mandala AND astro_mandala_zodiac]` `[role: 主干]` Mandala = individuation symbol; zodiac = mandala with 4 angles, 3×4=12. → L4276-4284
- `[ns_aop_122]` `[trigger: chart_blueprint]` `[factor_trigger: astro_blueprint]` `[role: 总结]` Birth-chart = mandala of individual life, blueprint of individuation, conscious way to Self. → L4284-4288"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 6: Birth-Chart as Mandala—Tao and Individuation"
    factor_refs: list = ['astro_mandala', 'astro_chart_blueprint']
    
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
        book_id="astrology_personality",
        chapter="",
        l1_anchor="ap_v1.0.0_entry_6__birth_chart_as_mandal_001_L1",
    )
    version: str = "1.0.0"
