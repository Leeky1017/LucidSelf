"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.156399
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
    semantic_id="ca_v1.0.0_prerequisites_for_chart_interp_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class PrerequisitesForChartInterp(SemanticEntry):
    """
    #### Source Text
(Lilly Book I, pp. 121-123): "Before you give judgment upon any question, observe w...
    """
    
    original_text: str = """#### Source Text
(Lilly Book I, pp. 121-123): "Before you give judgment upon any question, observe whether the Sign ascending be of those called, Mute Signs, viz. Cancer, Scorpio, Pisces... Consider whether the Ascendant be void of Planets... If Saturn be in the Ascendant, the matter will not easily be effected."

#### English Paraphrase (Primary Language)

**Considerations Before Judgment** are prerequisites ensuring a chart is fit for interpretation:

1. **Radical Chart Test**: Chart must be "radical" (fit for judgment)
   - ASC degree matches querent's appearance
   - Chart makes sense for the question asked

2. **Via Combusta Warning**: Moon between 15° Libra and 15° Scorpio is burned—unreliable

3. **Saturn in 7th Warning**: Saturn in 7th afflicts astrologer's judgment

4. **Void of Course Moon**: Moon making no aspects before leaving sign—nothing will come of matter

5. **Early or Late Degrees**: 0-3° = too early (matter premature); 27-30° = too late (matter past)

6. **Retrograde Considerations**: Retrograde significators = delays, reversals, returns

#### Complete Chinese Interpretation (Secondary Language)

**判断前的考虑事项**是确保盘适合解读的前提：1. **根本盘测试**=盘必须"根本"（适合判断）；2. **燃烧之路警告**=月亮在天秤15°至天蝎15°间不可靠；3. **土星在第7宫警告**=土星在第7宫损害占星师判断；4. **月亮空亡**=月亮离开星座前无相位=事情无结果；5. **早或晚度数**=0-3°太早（事情未成熟），27-30°太晚（事情已过）；6. **逆行考虑**=逆行象征星=延迟、逆转、回归。

**Narrative Snippets**:
- `[ns_lilly_consid_001]` `[trigger: void_of_course]` `[factor_trigger: astro_moon_void_of_course]` `[role: 主干]` Moon void of course = nothing will come of the matter asked. → CA I #Considerations
- `[ns_lilly_consid_002]` `[trigger: via_combusta]` `[factor_trigger: astro_moon_via_combusta AND astro_judgment_unreliable]` `[role: 条件分支]` Moon in Via Combusta (15° Libra to 15° Scorpio) renders judgment unreliable. → CA I #Considerations
- `[ns_lilly_consid_003]` `[trigger: early_late_degrees]` `[factor_trigger: astro_degree_position]` `[role: 条件分支]` Early degrees (0-3°) = matter premature; late degrees (27-30°) = matter past or ending. → CA I #Considerations
- `[ns_lilly_consid_004]` `[trigger: saturn_seventh]` `[factor_trigger: astro_saturn AND astro_house_7]` `[role: 条件分支]` Saturn in 7th afflicts the astrologer's judgment—error likely in interpretation. → CA I #Considerations"""
    normalized_text_zh: str = """"""
    subject: str = "Prerequisites for Chart Interpretation"
    factor_refs: list = ['radical_chart', 'moon_void_of_course', 'via_combusta', 'retrograde']
    
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
        l1_anchor="ca_v1.0.0_prerequisites_for_chart_interp_001_L1",
    )
    version: str = "1.0.0"
