"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.152237
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
    semantic_id="ca_v1.0.0_correcting_the_birth_time_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class CorrectingTheBirthTime(SemanticEntry):
    """
    #### Source Text
(Lilly Book III, pp. 500-509): "Divers ways of rectifying Nativities. The Trutine o...
    """
    
    original_text: str = """#### Source Text
(Lilly Book III, pp. 500-509): "Divers ways of rectifying Nativities. The Trutine of Hermes: If the Moon at birth be above the earth, take the degree she is in for the Ascendant at conception; if below, take her degree for the Descendant. The Animodar method uses the nearest New or Full Moon before birth."

#### English Paraphrase (Primary Language)

**Chart Rectification** corrects uncertain birth times using astronomical and life-event correlations:

**1. Trutine of Hermes** (Conception Method):
- Moon above horizon at birth → Moon's degree = ASC at conception
- Moon below horizon at birth → Moon's degree = DSC at conception
- Gestation period: 273 days ± variations by Moon position

**2. Animodar Method** (Prenatal Lunation):
- Find nearest New/Full Moon before birth
- Ruler of that lunation degree relates to ASC degree

**3. Rectification by Accidents**:
- Use known life events (marriage, death of parent, illness)
- Work backward using directions to find correct birth time
- Most reliable method when events are accurately dated

#### Complete Chinese Interpretation (Secondary Language)

**天宫图校正**使用天文和生活事件关联修正不确定的出生时间：**1. 赫尔墨斯真理**（受孕法）：出生时月亮在地平线上→月亮度数=受孕时上升度数；月亮在地平线下→月亮度数=受孕时下降度数。**2. 动物方法**（产前朔望）：找出出生前最近的新月/满月，该朔望度数的守护星与上升度数相关。**3. 通过事件校正**：使用已知生活事件（婚姻、父母去世、疾病），通过推运反推找到正确出生时间——事件日期准确时最可靠。

**Narrative Snippets**:
- `[ns_lilly_rect_001]` `[trigger: trutine]` `[factor_trigger: astro_birth_time_correction]` `[role: 主干]` Trutine of Hermes: Moon above earth at birth = Moon degree is ASC at conception. → CA III #Rectification
- `[ns_lilly_rect_002]` `[trigger: accidents]` `[factor_trigger: astro_life_event]` `[role: 主干依赖]` Rectification by accidents: Use known life events and work backward via directions. → CA III #Rectification
- `[ns_lilly_rect_003]` `[trigger: rectification_accuracy]` `[factor_trigger: astro_rectification_accuracy]` `[role: 总结]` Rectification by known events is most reliable method when dates are accurately recorded. → English Paraphrase
- `[ns_lilly_rect_004]` `[trigger: moon_birth]` `[factor_trigger: astro_moon_position_birth]` `[role: 主干依赖]` Moon position at birth (above/below horizon) determines conception Ascendant degree. → English Paraphrase
- `[ns_lilly_rect_005]` `[trigger: event_timing]` `[factor_trigger: astro_life_event_timing]` `[role: 条件分支]` Known life event dates provide anchor points for birth time rectification. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "Correcting the Birth Time"
    factor_refs: list = ['rectification', 'trutine_hermes', 'animodar']
    
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
        book_id="christian_astrology",
        chapter="",
        l1_anchor="ca_v1.0.0_correcting_the_birth_time_001_L1",
    )
    version: str = "1.0.0"
