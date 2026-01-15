"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578677
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
    semantic_id="qtbj_v1.0.0_1__三冬癸水_亥子丑月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1三冬癸水亥子丑月(SemanticEntry):
    """
    - **原文（source_text）**：
  **十月癸水**，旺中有弱，何也？因亥摇木，泄散元神，宜用庚辛为妙。得庚辛两透，不见丁伤者，功名有准。
  或支成木局，有丁出干，为木旺火相，制住庚辛...
    """
    
    original_text: str = """- **原文（source_text）**：
  **十月癸水**，旺中有弱，何也？因亥摇木，泄散元神，宜用庚辛为妙。得庚辛两透，不见丁伤者，功名有准。
  或支成木局，有丁出干，为木旺火相，制住庚辛不生水，必主清寒。或一派壬水，不见戊制，名冬水汪洋，奔波到老。若得戊透，清贵堪夸。
  **十一月癸水**，值冰冻之时，金水无交欢之象，专用丙火解冻，庶不致成冰，又要辛金滋扶。无丙有辛，不妙。有丙透解冻，则金温水暖，两两相生，要不见壬癸，自然登科及第。
  或一派壬水，无丙出干，寒困之士。一派癸水，孤贱之流。或支成水局，得丙火重出干者，又主蟒袍玉带之荣。
  **十二月癸水**，寒极成冰，万物不能舒泰，宜丙火解冻。或丙透年时，加以壬透，支中多戊，名水辅阳光，主显达名臣。
  或支见子丑，比肩出干，即有丙透，不能解冻，此属平常。或一片癸己会党，年透丁火，名雪后灯光，夜生者贵，日生者否。

- **分字分词释义**：
  - **旺中有弱**：旺相中有虚弱 / 亥月癸水 / 特殊状态
  - **亥摇木**：亥中甲木长生 / 泄水 / 忌讳
  - **冬水汪洋**：冬天水势浩大 / 壬多无制 / 凶象
  - **冰冻之时**：结冰时节 / 子月 / 调候背景
  - **解冻**：融化冰雪 / 丙火作用 / 首要用神
  - **金温水暖**：金暖水暖 / 丙火调候后 / 吉象
  - **蟒袍玉带**：高官服饰 / 水局丙重透 / 极贵
  - **水辅阳光**：水辅助阳光 / 丙壬戊配 / 显达格局
  - **雪后灯光**：雪后的灯火 / 癸己丁配 / 吉象

- **规范化释义（primary_lang_explained）**：
  十月（亥月）癸水，旺中有弱。因亥中甲木长生，泄散元神，宜用庚辛为妙。得庚辛两透，不见丁火伤害者，功名有准。
  若一派壬水，不见戊土制约，名"冬水汪洋"，奔波到老。若得戊透，清贵堪夸。
  十一月（子月）癸水，值冰冻之时，金水无交欢之象。专用丙火解冻，庶不致成冰，又要辛金滋扶。有丙透解冻，则金温水暖，两两相生，自然登科及第。
  十二月（丑月）癸水，寒极成冰，万物不能舒泰。宜丙火解冻。丙透年时，加壬透，支中多戊，名"水辅阳光"，主显达名臣。
  或癸己会党，年透丁火，名"雪后灯光"，夜生者贵。

- **完整对等诠释（secondary_lang_full）**：
  10th Month Gui Water: Prosperous yet weak. Hai contains Jia Wood long-life, draining spirit. Use Geng/Xin. Both revealing without Ding damage implies fame certain.
  If Ren Water massive without Wu controlling, named "Winter Water Vast", wandering until old. Wu revealing implies pure nobility.
  11th Month Gui Water: Time of freezing. Metal/Water no mutual joy. Exclusively use Bing Fire to unfreeze. With Bing unfreezing, Metal warm Water warm, naturally passing exams.
  12th Month Gui Water: Extreme cold turns to ice. Use Bing to unfreeze. Bing revealed in Year/Hour, plus Ren, branch Wu many, named "Water Assisting Sunlight", implies famous minister.
  Or Gui/Ji party, Ding in year, named "Lamp after Snow", night birth noble.

- **核心要点**：
  - **十月**：庚辛两透，戊制壬水。
  - **十一月**：专用丙火解冻，辛金滋扶。
  - **十二月**：丙火解冻，水辅阳光，雪后灯光。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_410]` `[trigger: 癸生亥月]` `[factor_trigger: month_hai AND tiangan_gui AND tiangan_geng AND tiangan_xin]` `[role: 主干]` 十月癸水，旺中有弱，宜用庚辛为妙。 → 《穷通宝鉴·三冬癸水》#40.1
  - `[ns_qttbj_411]` `[trigger: 癸生子月]` `[factor_trigger: month_zi AND tiangan_gui AND tiangan_bing]` `[role: 主干]` 十一月癸水，冰冻之时，专用丙火解冻。 → 《穷通宝鉴·三冬癸水》#40.1
  - `[ns_qttbj_412]` `[trigger: 癸生丑月]` `[factor_trigger: month_chou AND tiangan_gui AND tiangan_bing AND tiangan_ren]` `[role: 主干]` 十二月癸水，寒极成冰，宜丙火解冻，名水辅阳光。 → 《穷通宝鉴·三冬癸水》#40.1
  - `[ns_qttbj_413]` `[trigger: 雪后灯光]` `[factor_trigger: month_chou AND tiangan_gui AND tiangan_ji AND tiangan_ding AND night_birth]` `[role: 条件分支]` 癸己会党，年透丁火，名雪后灯光，夜生者贵。 → 《穷通宝鉴·三冬癸水》#40.1
  - `[ns_qttbj_599]` `[trigger: 秋土火]` `[factor_trigger: autumn_earth_fire]` `[role: 条件分支]` 秋土喜火暖燥，主调候。 → 《穷通宝鉴》
  - `[ns_qttbj_600]` `[trigger: 秋火]` `[factor_trigger: autumn_fire]` `[role: 条件分支]` 秋火渐衰，需木生助。 → 《穷通宝鉴》
  - `[ns_qttbj_601]` `[trigger: 秋甲]` `[factor_trigger: autumn_jia]` `[role: 条件分支]` 秋甲木衰，需水滋养。 → 《穷通宝鉴》
  - `[ns_qttbj_602]` `[trigger: 平衡]` `[factor_trigger: balance]` `[role: 条件分支]` 平衡为五行调和的状态。 → 《穷通宝鉴》
  - `[ns_qttbj_603]` `[trigger: 丙火]` `[factor_trigger: bing]` `[role: 条件分支]` 丙火为太阳之火，主光明威烈。 → 《穷通宝鉴》
  - `[ns_qttbj_604]` `[trigger: 丙辰]` `[factor_trigger: bing_chen]` `[role: 条件分支]` 丙辰为丙火坐辰土。 → 《穷通宝鉴》
  - `[ns_qttbj_605]` `[trigger: 丙丑]` `[factor_trigger: bing_chou]` `[role: 条件分支]` 丙丑为丙火坐丑土。 → 《穷通宝鉴》
  - `[ns_qttbj_606]` `[trigger: 丙丁]` `[factor_trigger: bing_ding]` `[role: 条件分支]` 丙丁为火的阴阳两干。 → 《穷通宝鉴》
  - `[ns_qttbj_607]` `[trigger: 丙过]` `[factor_trigger: bing_excess]` `[role: 条件分支]` 丙过为丙火太旺的状态。 → 《穷通宝鉴》
  - `[ns_qttbj_608]` `[trigger: 丙癸甲透]` `[factor_trigger: bing_gui_jia_reveal]` `[role: 条件分支]` 丙癸甲透为三干俱显。 → 《穷通宝鉴》
  - `[ns_qttbj_609]` `[trigger: 丙癸透]` `[factor_trigger: bing_gui_reveal]` `[role: 条件分支]` 丙癸透为丙癸二干显现。 → 《穷通宝鉴》
  - `[ns_qttbj_610]` `[trigger: 丙癸辛透]` `[factor_trigger: bing_gui_xin_reveal]` `[role: 条件分支]` 丙癸辛透为三干俱显。 → 《穷通宝鉴》
  - `[ns_qttbj_611]` `[trigger: 丙亥]` `[factor_trigger: bing_hai]` `[role: 条件分支]` 丙亥为丙火坐亥水。 → 《穷通宝鉴》
  - `[ns_qttbj_612]` `[trigger: 丙甲癸全]` `[factor_trigger: bing_jia_gui_all]` `[role: 条件分支]` 丙甲癸全为调候三要素齐备。 → 《穷通宝鉴》
  - `[ns_qttbj_613]` `[trigger: 丙甲透]` `[factor_trigger: bing_jia_reveal]` `[role: 条件分支]` 丙甲透为丙甲二干显现。 → 《穷通宝鉴》
  - `[ns_qttbj_614]` `[trigger: 丙卯]` `[factor_trigger: bing_mao]` `[role: 条件分支]` 丙卯为丙火坐卯木。 → 《穷通宝鉴》
  - `[ns_qttbj_615]` `[trigger: 丙壬组合]` `[factor_trigger: bing_ren_combo]` `[role: 条件分支]` 丙壬组合为水火既济。 → 《穷通宝鉴》
  - `[ns_qttbj_616]` `[trigger: 丙壬戊]` `[factor_trigger: bing_ren_wu]` `[role: 条件分支]` 丙壬戊为水辅阳光的配置。 → 《穷通宝鉴》
  - `[ns_qttbj_617]` `[trigger: 丙杀]` `[factor_trigger: bing_sha]` `[role: 条件分支]` 丙杀为丙火为七杀的情况。 → 《穷通宝鉴》
  - `[ns_qttbj_618]` `[trigger: 丙申]` `[factor_trigger: bing_shen]` `[role: 条件分支]` 丙申为丙火坐申金。 → 《穷通宝鉴》
  - `[ns_qttbj_619]` `[trigger: 丙巳]` `[factor_trigger: bing_si]` `[role: 条件分支]` 丙巳为丙火坐巳火。 → 《穷通宝鉴》
  - `[ns_qttbj_620]` `[trigger: 丙夺光]` `[factor_trigger: bing_steals_light]` `[role: 条件分支]` 丙夺光为丙火夺丁火之光。 → 《穷通宝鉴》
  - `[ns_qttbj_621]` `[trigger: 丙暖]` `[factor_trigger: bing_warm]` `[role: 条件分支]` 丙暖为丙火暖局的作用。 → 《穷通宝鉴》
  - `[ns_qttbj_622]` `[trigger: 丙未]` `[factor_trigger: bing_wei]` `[role: 条件分支]` 丙未为丙火坐未土。 → 《穷通宝鉴》
  - `[ns_qttbj_623]` `[trigger: 丙午]` `[factor_trigger: bing_wu]` `[role: 条件分支]` 丙午为丙火坐午火。 → 《穷通宝鉴》
  - `[ns_qttbj_624]` `[trigger: 丙辛]` `[factor_trigger: bing_xin]` `[role: 条件分支]` 丙辛为丙辛合水的组合。 → 《穷通宝鉴》
  - `[ns_qttbj_625]` `[trigger: 丙辛化]` `[factor_trigger: bing_xin_transform]` `[role: 条件分支]` 丙辛化为丙辛合化水。 → 《穷通宝鉴》
  - `[ns_qttbj_626]` `[trigger: 丙戌]` `[factor_trigger: bing_xu]` `[role: 条件分支]` 丙戌为丙火坐戌土。 → 《穷通宝鉴》
  - `[ns_qttbj_627]` `[trigger: 丙寅]` `[factor_trigger: bing_yin]` `[role: 条件分支]` 丙寅为丙火坐寅木。 → 《穷通宝鉴》
  - `[ns_qttbj_628]` `[trigger: 丙酉]` `[factor_trigger: bing_you]` `[role: 条件分支]` 丙酉为丙火坐酉金。 → 《穷通宝鉴》
  - `[ns_qttbj_629]` `[trigger: 丙子]` `[factor_trigger: bing_zi]` `[role: 条件分支]` 丙子为丙火坐子水。 → 《穷通宝鉴》
  - `[ns_qttbj_630]` `[trigger: 身全]` `[factor_trigger: body_complete]` `[role: 条件分支]` 身全为日主根基完整。 → 《穷通宝鉴》
  - `[ns_qttbj_631]` `[trigger: 身无依]` `[factor_trigger: body_no_reliance]` `[role: 条件分支]` 身无依为日主无根无助。 → 《穷通宝鉴》
  - `[ns_qttbj_632]` `[trigger: 支金]` `[factor_trigger: branch_metal]` `[role: 条件分支]` 支金为地支含金。 → 《穷通宝鉴》
  - `[ns_qttbj_633]` `[trigger: 支火局]` `[factor_trigger: branches_fire_frame]` `[role: 条件分支]` 支火局为地支成火局。 → 《穷通宝鉴》
  - `[ns_qttbj_634]` `[trigger: 支金局]` `[factor_trigger: branches_metal_frame]` `[role: 条件分支]` 支金局为地支成金局。 → 《穷通宝鉴》
  - `[ns_qttbj_635]` `[trigger: 支水局]` `[factor_trigger: branches_water_frame]` `[role: 条件分支]` 支水局为地支成水局。 → 《穷通宝鉴》
  - `[ns_qttbj_636]` `[trigger: 支木局]` `[factor_trigger: branches_wood_frame]` `[role: 条件分支]` 支木局为地支成木局。 → 《穷通宝鉴》
  - `[ns_qttbj_637]` `[trigger: 铸印格]` `[factor_trigger: casting_seal]` `[role: 条件分支]` 铸印格为金火全备的格局。 → 《穷通宝鉴》
  - `[ns_qttbj_638]` `[trigger: 辰月]` `[factor_trigger: chen_month]` `[role: 条件分支]` 辰月为三月，土旺之时。 → 《穷通宝鉴》
  - `[ns_qttbj_639]` `[trigger: 色母]` `[factor_trigger: color_mother]` `[role: 条件分支]` 色母为印星的比喻。 → 《穷通宝鉴》
  - `[ns_qttbj_640]` `[trigger: 色标准]` `[factor_trigger: color_standard]` `[role: 条件分支]` 色标准为正格的标准配置。 → 《穷通宝鉴》
  - `[ns_qttbj_641]` `[trigger: 争合]` `[factor_trigger: competing_combination]` `[role: 条件分支]` 争合为多干争合一干。 → 《穷通宝鉴》
  - `[ns_qttbj_642]` `[trigger: 争合]` `[factor_trigger: competing_combine]` `[role: 条件分支]` 争合为争夺合化的情况。 → 《穷通宝鉴》
  - `[ns_qttbj_643]` `[trigger: 覆金]` `[factor_trigger: cover_metal]` `[role: 条件分支]` 覆金为金被埋覆的状态。 → 《穷通宝鉴》
  - `[ns_qttbj_644]` `[trigger: 丁辰]` `[factor_trigger: ding_chen]` `[role: 条件分支]` 丁辰为丁火坐辰土。 → 《穷通宝鉴》
  - `[ns_qttbj_645]` `[trigger: 丁制辛]` `[factor_trigger: ding_control_xin]` `[role: 条件分支]` 丁制辛为丁火克制辛金。 → 《穷通宝鉴》
  - `[ns_qttbj_646]` `[trigger: 丁亥]` `[factor_trigger: ding_hai]` `[role: 条件分支]` 丁亥为丁火坐亥水。 → 《穷通宝鉴》
  - `[ns_qttbj_647]` `[trigger: 丁隐]` `[factor_trigger: ding_hidden]` `[role: 条件分支]` 丁隐为丁火藏于地支。 → 《穷通宝鉴》
  - `[ns_qttbj_648]` `[trigger: 丁甲丙]` `[factor_trigger: ding_jia_bing]` `[role: 条件分支]` 丁甲丙为木火相生的配置。 → 《穷通宝鉴》"""
    normalized_text_zh: str = """"""
    subject: str = "1. 三冬癸水（亥子丑月）"
    factor_refs: list = ['winter_water_vast', 'water_assist_sun', 'snow_lamp']
    
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
        l1_anchor="qtbj_v1.0.0_1__三冬癸水_亥子丑月_001_L1",
    )
    version: str = "1.0.0"
