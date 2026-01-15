"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.620026
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
    semantic_id="qtbj_v1.0.0_2__正月乙木_寅月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 2正月乙木寅月(SemanticEntry):
    """
    - **原文（source_text）**：
  正月乙木，必须用丙，因天气尤有余寒，非丙不暖，虽有癸水，恐凝寒气，故以丙火为先，癸水次之。
  丙癸两透，科甲定然，或有丙无癸，门户阐扬。或丙多乏癸，...
    """
    
    original_text: str = """- **原文（source_text）**：
  正月乙木，必须用丙，因天气尤有余寒，非丙不暖，虽有癸水，恐凝寒气，故以丙火为先，癸水次之。
  丙癸两透，科甲定然，或有丙无癸，门户阐扬。或丙多乏癸，名曰春旱。独阳不长，浊富之人。或丙少癸多，又为困丙，终为寒士。或癸己多见，为湿土之木皆下格。
  用丙者，木妻火子。用癸水见火多者，金妻水子。

- **分字分词释义**：
  - **尤有余寒**：还有残留的寒气 / 寅月特征 / 初春
  - **恐凝寒气**：恐怕凝聚寒气 / 癸多之害 / 忌水多
  - **门户阐扬**：门庭光大扬名 / 有丙无癸 / 次贵
  - **春旱**：春季干旱 / 丙多癸少 / 浊富
  - **独阳不长**：单独的阳气不能生长 / 无阴配合 / 凶象
  - **困丙**：困住丙火 / 癸多克丙 / 寒士
  - **湿土之木**：生长在湿土中的木 / 己癸多 / 下格

- **规范化释义（primary_lang_explained）**：
  正月（寅月）的乙木，必须用丙火，因为天气还有余寒，没有丙火就不暖。虽然需要癸水滋养，但怕凝结寒气（水多则冻），所以以丙火为先，癸水次之。
  如果丙火和癸水都透出，科甲功名是一定的。如果有丙火而没有癸水，也能光大门庭（门户阐扬）。
  如果丙火多而缺乏癸水，这叫“春旱”，独阳不长，是浊富（有钱无贵）的人。
  如果丙火少而癸水多，这又是“困丙”（水克火），终身是个贫寒的读书人（寒士）。
  如果癸水和己土多见，这是“湿土之木”（己土卑湿，癸水阴寒），都是下等格局。
  用丙火的人，木为妻火为子。用癸水（因火多而用）的人，金为妻水为子。

- **完整对等诠释（secondary_lang_full）**：
  Yi Wood in the 1st Month (Tiger Month) must use Bing Fire, because the weather still has residual coldness; without Bing, it is not warm. Although Gui Water is present, there is fear of congealing coldness; thus take Bing Fire as primary and Gui Water as secondary.
  If both Bing and Gui are revealed, Civil Service success is certain. If there is Bing but no Gui, one can still expand the family gate (fame).
  If Bing is abundant but Gui is lacking, it is called "Spring Drought"; solitary Yang cannot grow, denoting a person of "Turbid Wealth" (rich but unrefined).
  If Bing is scarce and Gui is abundant, it is "Trapping Bing", making one a poor scholar for life.
  If Gui and Ji are seen frequently, it is "Wood in Wet Soil", all lower patterns.
  Those using Bing take Wood as Wife and Fire as Child. Those using Gui (when Fire is excessive) take Metal as Wife and Water as Child.

- **核心要点**：
  - **首要用神**：丙火（解寒）。
  - **次要用神**：癸水（润根），但不可多。
  - **格局**：
    - 丙癸双透：贵。
    - 有丙无癸：名（门户阐扬）。
    - 丙多无癸：春旱（浊富）。
    - 癸多困丙：寒士。
    - 癸己多：湿土之木（下格）。

- **详细解说**：
  寅月乙木，藤萝系甲（月令寅中甲木），根基稳固。
  - 关键在于寒暖。初春寒气重，无丙火则乙木蜷缩不发。
  - “春旱”：指火太旺而无水，花草枯黄，虽有发荣之象（富），但缺乏生机（贵/长久）。
  - “湿土之木”：己土湿寒，根烂叶腐。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_173]` `[trigger: 寅月乙木]` `[factor_trigger: month_yin AND tiangan_yi AND tiangan_bing AND tiangan_gui]` `[role: 主干]` 正月乙木，必须用丙，因天气尤有余寒，非丙不暖，故以丙火为先，癸水次之。 → 《穷通宝鉴·三春乙木》#7.2
  - `[ns_qttbj_174]` `[trigger: 春旱]` `[factor_trigger: month_yin AND tiangan_yi AND bing_excessive AND NOT tiangan_gui]` `[role: 条件分支]` 丙多乏癸，名曰春旱，独阳不长，浊富之人。 → 《穷通宝鉴·三春乙木》#7.2
  - `[ns_qttbj_175]` `[trigger: 困丙寒士]` `[factor_trigger: month_yin AND tiangan_yi AND gui_excessive AND NOT tiangan_bing]` `[role: 条件分支]` 丙少癸多，又为困丙，终为寒士。 → 《穷通宝鉴·三春乙木》#7.2
  - `[ns_qttbj_176]` `[trigger: 湿土之木]` `[factor_trigger: month_yin AND tiangan_yi AND gui_revealed AND ji_revealed AND wood_wet_soil]` `[role: 例外处理]` 癸己多见，为湿土之木皆下格。 → 《穷通宝鉴·三春乙木》#7.2"""
    normalized_text_zh: str = """"""
    subject: str = "2. 正月乙木（寅月）"
    factor_refs: list = ['spring_drought', 'solitary_yang_cannot_grow', 'poor_scholar', 'wood_wet_soil']
    
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
        book_id="qiongtongbaojian",
        chapter="",
        l1_anchor="qtbj_v1.0.0_2__正月乙木_寅月_001_L1",
    )
    version: str = "1.0.0"
