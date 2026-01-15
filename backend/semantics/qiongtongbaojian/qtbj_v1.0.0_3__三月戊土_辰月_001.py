"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.596985
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
    semantic_id="qtbj_v1.0.0_3__三月戊土_辰月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 3三月戊土辰月(SemanticEntry):
    """
    - **原文（source_text）**：
  三月戊土司令，不见丙甲癸者，愚而且贱。甲癸透者，科甲。丙癸透者、生员。甲癸俱藏者，只可云富，有癸异途。
  若丙多无癸，旱田无水，不能种苗，旧谷已没，...
    """
    
    original_text: str = """- **原文（source_text）**：
  三月戊土司令，不见丙甲癸者，愚而且贱。甲癸透者，科甲。丙癸透者、生员。甲癸俱藏者，只可云富，有癸异途。
  若丙多无癸，旱田无水，不能种苗，旧谷已没，新谷未登，此先富后贫之造。或火多有壬透者，先贫后富。癸透先贱后荣。壬藏不过食足，癸藏不过名传，即此亦须运美。
  或支成火局，得癸透者，富贵天然。壬透富贵辛苦，何也？癸乃天上甘霖，壬乃江河波浪，所以有劳逸之殊。
  支成木局，又甲乙出干，此名官杀会党，官杀无去留之义，得一庚透，扫除官杀，亦主富贵。无庚乃浅薄之人，宜用火泄木气。有一命、丁未、癸卯、戊寅、乙卯。癸丁透干，加以戊癸化火，将甲木暗焚，反得武科探花。
  或有比印，耑看癸透，取癸而成贵格。无癸、无火、无金，名为土木自战，主腹中疾病，忧愁艰苦。

- **分字分词释义**：
  - **戊土司令**：戊土当令掌权 / 辰月 / 身旺
  - **旱田无水**：干旱田地无水灌溉 / 火多无癸 / 凶象
  - **旧谷已没**：旧年收成已尽 / 先有后无 / 凶象
  - **新谷未登**：新年收成未到 / 后继无力 / 凶象
  - **天上甘霖**：天降甘甜雨水 / 癸水特点 / 吉象
  - **江河波浪**：江河波涛 / 壬水特点 / 辛苦
  - **官杀会党**：官杀聚集成党 / 木局甲乙透 / 凶象
  - **扫除官杀**：清除官杀 / 庚金制木 / 救应
  - **土木自战**：土木互相争斗 / 无通关 / 凶象
  - **腹中疾病**：腹部疾病 / 脾胃受损 / 凶象

- **规范化释义（primary_lang_explained）**：
  If there are Parallels/Seals, focus on Gui revealing; Gui forms a noble pattern. Without Gui/Fire/Metal, it is "Earth and Wood Fighting"; implies abdominal disease, worry, and hardship.

- **核心要点**：
  - **辰月三宝**：甲疏、癸润、丙暖。
  - **旱田无水**：火多无水，先富后贫。
  - **癸壬之别**：癸主逸（甘霖），壬主劳（江河）。
  - **官杀会党**：喜庚制，或火泄。
  - **土木自战**：无通关（火）无制约（金），主病。

- **详细解说**：
  - 辰月戊土最实，也最燥（若火多）。
  - “旱田无水”比喻极妙，土燥不能生金（收成），故贫。
  - 癸水是天降甘霖，最为珍贵。壬水需人力引灌，故辛苦。
  - “土木自战”：辰月土旺木有余气，若无火化木生土，也无金制木护土，两者相战，脾胃（土）受损。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_307]` `[trigger: 三月戊土司令]` `[factor_trigger: month_chen AND tiangan_wu AND tiangan_bing AND tiangan_jia AND tiangan_gui AND wu_chen_command]` `[role: 主干]` 三月戊土司令，不见丙甲癸者，愚而且贱。甲癸透者科甲，丙癸透者生员。 → 《穷通宝鉴·三春戊土》#21.3
  - `[ns_qttbj_308]` `[trigger: 旱田无水]` `[factor_trigger: month_chen AND tiangan_wu AND tiangan_bing_multiple AND NOT tiangan_gui AND drought_field]` `[role: 例外处理]` 丙多无癸，旱田无水，旧谷已没，新谷未登，此先富后贫之造。 → 《穷通宝鉴·三春戊土》#21.3
  - `[ns_qttbj_309]` `[trigger: 癸霖壬波]` `[factor_trigger: tiangan_gui AND tiangan_ren AND gui_rain_ren_wave]` `[role: 主干依赖]` 癸乃天上甘霖，壬乃江河波浪，所以有劳逸之殊。 → 《穷通宝鉴·三春戊土》#21.3
  - `[ns_qttbj_310]` `[trigger: 土木自战]` `[factor_trigger: month_chen AND tiangan_wu AND NOT tiangan_gui AND NOT tiangan_huo AND NOT tiangan_jin AND earth_wood_fighting]` `[role: 例外处理]` 无癸、无火、无金，名为土木自战，主腹中疾病，忧愁艰苦。 → 《穷通宝鉴·三春戊土》#21.3"""
    normalized_text_zh: str = """"""
    subject: str = "3. 三月戊土（辰月）"
    factor_refs: list = ['drought_field', 'earth_wood_fighting', 'officer_killing_party']
    
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
        l1_anchor="qtbj_v1.0.0_3__三月戊土_辰月_001_L1",
    )
    version: str = "1.0.0"
