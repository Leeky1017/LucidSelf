"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.162775
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
    semantic_id="tb_v1.0.0_mode_of_prediction_in_eclipses_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class ModeOfPredictionInEclipses(SemanticEntry):
    """
    **Source Text** (Lines 3500-3600):
> In the investigation of general events, eclipses of the luminar...
    """
    
    original_text: str = """**Source Text** (Lines 3500-3600):
> In the investigation of general events, eclipses of the luminaries are principally attended to, and particularly those capable of being seen... The first point requiring consideration is the place of the zodiac in which the eclipse happens, and what countries are in familiarity with that place... The second point is to determine the time when the effect will commence and how long it will continue... In solar eclipses, the effect begins as many years before as the eclipse happens hours after the Sun has risen; in lunar eclipses, as many months.

**English Paraphrase (Primary Language)**:
Ptolemy establishes the **methodology for eclipse-based mundane prediction**:

1. **Determine affected regions**: Find which countries have familiarity with the eclipse zodiacal degree
2. **Timing**: Solar eclipse effects begin in years equal to hours after sunrise; lunar eclipse effects in months
3. **Duration**: Effects last as long as the eclipse's duration in equinoctial hours (solar = years, lunar = months)
4. **Intensity**: Depends on eclipse magnitude and configurating planets

For **solar eclipses**: Each hour = 1 year of effect
For **lunar eclipses**: Each hour = 1 month of effect

The nature of effects depends on: (1) signs involved, (2) planets configurating with eclipse, (3) angles occupied.

**Complete Chinese Interpretation (Secondary Language)**:
托勒密建立了**基于日食月食的世俗预测方法论**：

1. **确定受影响地区**：找出哪些国家与日食黄道度数有亲和性
2. **时机**：日食效应在日出后等于小时数的年份开始；月食效应以月份计
3. **持续时间**：效应持续与日食分点小时数相等的时间（日食=年，月食=月）
4. **强度**：取决于日食幅度和配置的行星

**Core Points**:
- Eclipses are primary mundane indicators
- Solar eclipse: hours after sunrise = years before effect
- Lunar eclipse: hours = months
- Duration in hours = duration in years (solar) or months (lunar)
- Affected regions determined by zodiacal familiarity

**Narrative Snippets**:
- `[ns_tetra_ii005]` `[trigger: eclipse_methodology]` `[factor_trigger: astro_eclipse_solar OR astro_eclipse_lunar]` `[role: 主干]` Eclipse timing: solar effects in years, lunar in months; duration equals eclipse hours. → Source Text II.5
- `[ns_tetra_ii019]` `[trigger: solar_eclipse_timing]` `[factor_trigger: astro_eclipse_solar AND astro_timing]` `[role: 条件分支]` Solar eclipse effects begin as many years before as the eclipse happens hours after the Sun has risen. → Solar Rule
- `[ns_tetra_ii020]` `[trigger: eclipse_region]` `[factor_trigger: astro_eclipse AND astro_region]` `[role: 条件分支]` First determine which countries have familiarity with the eclipse zodiacal degree—those regions will be affected. → Region
- `[ns_tetra_ii_ed]` `[trigger: effect_duration]` `[factor_trigger: effect_duration]` `[role: 效果]` Effect duration equals eclipse duration in equinoctial hours: solar eclipse hours = years, lunar eclipse hours = months. → Source Text II.5"""
    normalized_text_zh: str = """"""
    subject: str = "Mode of Prediction in Eclipses (Chapter V)"
    factor_refs: list = ['eclipse_timing']
    
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
        l1_anchor="tb_v1.0.0_mode_of_prediction_in_eclipses_001_L1",
    )
    version: str = "1.0.0"
