"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.162802
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
    semantic_id="tb_v1.0.0_the_time_and_period_of_the_eve_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class TheTimeAndPeriodOfTheEve(SemanticEntry):
    """
    **Source Text** (Lines 3731-3806):
> The second point requiring attention relates to time, and indic...
    """
    
    original_text: str = """**Source Text** (Lines 3731-3806):
> The second point requiring attention relates to time, and indicates the date when the event will take place, and the period during which its effect will continue. It must be premised, that as an eclipse cannot happen in all climates at the same temporal hour, so neither will the magnitude of the obscuration be equal in all parts of the world. The effect will endure as many years as the obscuration lasted hours, provided the eclipse was solar; but if lunar, a like number of months is to be reckoned instead of years.

**English Paraphrase (Primary Language)**:
Ptolemy explains **timing of eclipse effects**:

1. **Duration Rule**: Solar eclipse hours = years of effect; Lunar eclipse hours = months
2. **Commencement**: Depends on eclipse position relative to angles:
   - Near Ascendant: Effects begin in first 4 months, peak in first third
   - Near MC: Begin in second 4 months, peak in middle third
   - Near Descendant: Begin in last 4 months, peak in final third
3. **Intensification**: Planetary transits to eclipse degree modify intensity

**Complete Chinese Interpretation (Secondary Language)**:
托勒密解释了**日食效应的时间**：

1. **持续规则**：日食小时数 = 效应年数；月食小时数 = 月数
2. **开始时间**：取决于食相对角度的位置：
   - 靠近上升点：效应在前4个月开始，在前三分之一达到高峰
   - 靠近中天：在第二个4个月开始，在中间三分之一达到高峰
   - 靠近下降点：在最后4个月开始，在最后三分之一达到高峰
3. **强化**：行星过境到食度会调节强度

**Core Points**:
- Solar eclipse: 1 hour = 1 year of effect
- Lunar eclipse: 1 hour = 1 month of effect
- Angular position determines commencement timing
- Transits modify intensity

**Narrative Snippets**:
- `[ns_tetra_ii_011]` `[trigger: eclipse_timing]` `[factor_trigger: astro_eclipse_duration]` `[role: 主干]` Eclipse duration in hours equals years (solar) or months (lunar) of effect. → Source Text II.7
- `[ns_tetra_ii_024]` `[trigger: angular_commencement]` `[factor_trigger: astro_eclipse AND astro_angle]` `[role: 条件分支]` Eclipse near ASC = effects begin in first 4 months; near MC = second 4 months; near DESC = last 4 months. → Commencement
- `[ns_tetra_ii_025]` `[trigger: transit_intensification]` `[factor_trigger: astro_transit AND astro_eclipse_degree]` `[role: 条件分支]` Planetary transits to the eclipse degree intensify or modify the predicted effects. → Intensification"""
    normalized_text_zh: str = """"""
    subject: str = "The Time and Period of the Event (Chapter VII)"
    factor_refs: list = ['engine_id', 'eclipse_duration', 'astrology_classical', 'source_ref', 'rel_ii_011', 'astro_eclipse_duration', 'determining', 'evi_ii_011', 'eclipse_duration', 'rule_eclipse_timing', 'concept_eclipse_time', 'eclipse_duration', 'temporal_sense']
    
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
        l1_anchor="tb_v1.0.0_the_time_and_period_of_the_eve_001_L1",
    )
    version: str = "1.0.0"
