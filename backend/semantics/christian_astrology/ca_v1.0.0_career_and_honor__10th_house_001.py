"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.152320
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
    semantic_id="ca_v1.0.0_career_and_honor__10th_house_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class CareerAndHonor10thHouse(SemanticEntry):
    """
    #### Source Text
(Lilly Book III, pp. 615-633): "Of the Honour or Dignity of the Native. The Sun and...
    """
    
    original_text: str = """#### Source Text
(Lilly Book III, pp. 615-633): "Of the Honour or Dignity of the Native. The Sun and Moon strong = honor. Lord of 10th angular and dignified = high position. Mars or Saturn afflicting MC = falls from grace."

#### English Paraphrase (Primary Language)

**Career and Honor indicators**:
- **Sun**: Day chart honor significator
- **Moon**: Night chart honor significator
- **Lord of 10th**: Career type and success
- **Planets in 10th**: Direct career influence
- **MC degree**: Fixed stars, aspects

**Profession** shown by planet ruling or aspecting 10th:
- Mercury strong = writing, trade, teaching
- Venus strong = arts, pleasure, beauty
- Mars strong = military, surgery, mechanics
- Jupiter strong = religion, law, philosophy
- Saturn strong = agriculture, building, government

**Timing of honor**: Directions to MC or L10 from benefics.

#### Complete Chinese Interpretation (Secondary Language)

**事业与荣誉指标**：太阳=日盘荣誉象征星；月亮=夜盘荣誉象征星；第10宫主=事业类型与成功；第10宫内行星=直接事业影响；天顶度数=恒星、相位。**职业**由守护或与第10宫相位的行星显示：水星强=写作/贸易/教学；金星强=艺术/娱乐/美容；火星强=军事/外科/机械；木星强=宗教/法律/哲学；土星强=农业/建筑/政府。**荣誉时机**：吉星推运至天顶或L10。

**Narrative Snippets**:
- `[ns_lilly_career_001]` `[trigger: honor]` `[factor_trigger: astro_honor_level]` `[role: 主干]` Sun and Moon strong = honor and recognition; afflicted = obscurity or disgrace. → CA III #Career
- `[ns_lilly_career_002]` `[trigger: profession]` `[factor_trigger: astro_profession_type]` `[role: 主干依赖]` Planet ruling 10th shows profession type: Mercury = trade; Jupiter = law/religion. → CA III #Career
- `[ns_lilly_career_003]` `[trigger: sun_moon]` `[factor_trigger: astro_sun_moon_dignity]` `[role: 主干依赖]` Sun (day) and Moon (night) dignity indicates honor and recognition level. → English Paraphrase
- `[ns_lilly_career_004]` `[trigger: lord_10th]` `[factor_trigger: astro_lord_10th_planet]` `[role: 条件分支]` Planet ruling 10th determines career type and profession signification. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "Career and Honor (10th House)"
    factor_refs: list = ['lord_10th', 'midheaven']
    
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
        l1_anchor="ca_v1.0.0_career_and_honor__10th_house_001_L1",
    )
    version: str = "1.0.0"
