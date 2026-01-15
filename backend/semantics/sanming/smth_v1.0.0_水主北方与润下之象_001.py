"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227481
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
    semantic_id="smth_v1.0.0_水主北方与润下之象_001",
    book_id="sanming",
    engine_id="bazi"
)
class 水主北方与润下之象(SemanticEntry):
    """
    - **原文（source_text）**：
  水主于北，应冬。水之为言润也，阴气濡润，任养万物也。水西而东，金所生也。水流曲折，顺下而达，乃自然之性也。

- 分字分词释义：
  - **润**：...
    """
    
    original_text: str = """- **原文（source_text）**：
  水主于北，应冬。水之为言润也，阴气濡润，任养万物也。水西而东，金所生也。水流曲折，顺下而达，乃自然之性也。

- 分字分词释义：
  - **润**：滋润、濡养之意，主藏养而不显。
  - **顺下而达**：随势而下，曲折流行，是水的自然走势。

- **规范化释义（primary_lang_explained）**：
  水属北方，对应冬季。其义在「润」，以阴气濡养万物，使其潜藏、孕育。水由西向东流，自金所生，行走曲折而总是向下，这些都是水之本性。

- **完整对等诠释（secondary_lang_full）**：

  Water rules the North and corresponds to winter. Its essential action is to moisten and nourish: through gentle Yin it sustains life while things lie hidden and gestate. Water is said to flow from West to East, born from Metal, and to move in winding courses that always seek the lowest place—this expresses its compliant, downward‑reaching nature. In a chart, Water points to intelligence, flexibility, communication, fear and wandering. When fed by Metal, bounded by Earth and allowed to vent through Wood, it flows with measure and supports wisdom and connection. Without banks and structure it floods; oppressed by excessive Earth or Fire, it dries up and loses its capacity to nurture.

- **核心要点**：
  - 命局之水，多主智慧、流动、机巧、沟通，也主恐惧与漂荡；
  - 水得金生、土制、木泄，则流而有度；水无制则泛滥，受土太过则涸竭。

- **详细解说**：
  本节阐述水的北方属性与润下机能。水主北方应冬，其义为「润」——以阴气濡养万物，使其潜藏、孕育。水由西向东流，自金所生，行走曲折而总是向下。论命时，水旺而有金生、有土制、有木泄，则流而有度；水无制则泛滥，受土太过则涸竭。在职业与事件分析中，水主「智慧与流动」，对应信息流、资金流、沟通渠道等。

- **应用推演（操作顺序）**：
  1) 在命局中识别水的角色：是承担信息流、资金流，还是情绪与潜意识之流，据此调整其权重与解读；
  2) 观察水与金、土、木的配合：金生水则多见知识、资源输入；土制水则为结构与边界；木泄水则为创造与输出；
  3) 推岁运时，判断行水运究竟是「润下」还是「漂荡」：若原局已有良好土与金，则多为智慧流通与资源连接；若原局土弱金枯，则水运易成焦虑与漂泊；
  4) 在系统中，将与数据流、网络、沟通渠道、流动性相关的模块统摄为水象，便于从象意层面解释其行为模式。

- **反例与边界**：
  - 只见水旺便断为「聪明」，不看水是否有根、有制，忽略「聪明反被聪明误」的情况；
  - 将水象过度浪漫化，只谈灵感与感性，而不看到其与恐惧、逃避、散漫等阴暗面；
  - 在工程实现中，把所有与「流」有关的指标都算作吉象，而不区分有序流与无序泄，导致系统鼓励过度变动；
  - 反过来，将一切「稳定」都视作好事，不允许必要的流动与调整，也违背水的润下之道。

- **小例（示意）**：
  - 某命局水旺而金足、土亦中和，适合从事研究、咨询、金融中介、数据分析等「以流为用」的工作；系统可据此在职业画像中提高对「信息/资金流通类岗位」的评分；
  - 在产品与组织的生命周期分析中，以「水期」标记为信息收集、反馈汇总、调整方向的阶段，而非大规模冲刺，体现水的「润下孕育」功能。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_049]` `[trigger: 水主北方]` `[factor_trigger: direction=north AND wuxing=water]` `[role: 主干]` 水主于北，应冬。水之为言润也，阴气濡润，任养万物也。 → 《三命通会》卷一#论五行生成
  - `[ns_smth_050]` `[trigger: 金生水]` `[factor_trigger: wuxing_shengke=metal_generates_water]` `[role: 主干依赖]` 水西而东，金所生也。水流曲折，顺下而达，乃自然之性也。 → 《三命通会》卷一#论五行生成
  - `[ns_smth_875]` `[trigger: 金火土平衡]` `[factor_trigger: metal_fire_earth_balance]` `[role: 条件分支]` 金火土平衡主调和。 → 《三命通会》卷一
  - `[ns_smth_876]` `[trigger: 金火工具态]` `[factor_trigger: metal_fire_tool_state]` `[role: 条件分支]` 金火工具态定成器。 → 《三命通会》卷一
  - `[ns_smth_877]` `[trigger: 金性定义态]` `[factor_trigger: metal_nature_defined_state]` `[role: 条件分支]` 金性定义态主收敛。 → 《三命通会》卷一
  - `[ns_smth_878]` `[trigger: 金季节态]` `[factor_trigger: metal_season_state]` `[role: 条件分支]` 金季节态定时令。 → 《三命通会》卷一
  - `[ns_smth_879]` `[trigger: 金水土平衡]` `[factor_trigger: metal_water_earth_balance]` `[role: 条件分支]` 金水土平衡主调和。 → 《三命通会》卷一
  - `[ns_smth_880]` `[trigger: 金水富配置]` `[factor_trigger: metal_water_fortune_config]` `[role: 条件分支]` 金水富配置定格局。 → 《三命通会》卷一
  - `[ns_smth_881]` `[trigger: 金水工具滋养]` `[factor_trigger: metal_water_tool_nurture]` `[role: 条件分支]` 金水工具滋养主有力。 → 《三命通会》卷一
  - `[ns_smth_882]` `[trigger: 金木土平衡]` `[factor_trigger: jinmutu_pingheng]` `[role: 条件分支]` 金木土平衡主调和。 → 《三命通会》卷一
  - `[ns_smth_883]` `[trigger: 金强木弱风险]` `[factor_trigger: jinqiang_muruo_risk]` `[role: 条件分支]` 金强木弱有风险。 → 《三命通会》卷一
  - `[ns_smth_884]` `[trigger: 金水风险]` `[factor_trigger: jinshui_risk]` `[role: 条件分支]` 金水风险主不利。 → 《三命通会》卷一
  - `[ns_smth_885]` `[trigger: 金水土平衡]` `[factor_trigger: jinshuitu_pingheng]` `[role: 条件分支]` 金水土平衡主调和。 → 《三命通会》卷一
  - `[ns_smth_886]` `[trigger: 金水相生]` `[factor_trigger: jinshui_xiangsheng]` `[role: 条件分支]` 金水相生主有力。 → 《三命通会》卷一
  - `[ns_smth_887]` `[trigger: 金水夜间]` `[factor_trigger: jinshui_yejian]` `[role: 条件分支]` 金水夜间定时机。 → 《三命通会》卷一
  - `[ns_smth_888]` `[trigger: 金神格]` `[factor_trigger: jinshen_ge]` `[role: 条件分支]` 金神格主格局。 → 《三命通会》卷一
  - `[ns_smth_889]` `[trigger: 金土两行]` `[factor_trigger: jintu_lianghang]` `[role: 条件分支]` 金土两行主简约。 → 《三命通会》卷一
  - `[ns_smth_890]` `[trigger: 金旺土孤风险]` `[factor_trigger: jinwang_tugu_risk]` `[role: 条件分支]` 金旺土孤有风险。 → 《三命通会》卷一
  - `[ns_smth_891]` `[trigger: 己土甲木合]` `[factor_trigger: jitu_jiamu_he]` `[role: 条件分支]` 己土甲木合主合化。 → 《三命通会》卷一
  - `[ns_smth_892]` `[trigger: 聚类因子]` `[factor_trigger: julie_huanyun]` `[role: 条件分支]` 聚类因子定归类。 → 《三命通会》卷一
  - `[ns_smth_893]` `[trigger: 开冲要]` `[factor_trigger: kaichong_yao]` `[role: 条件分支]` 开冲要主引发。 → 《三命通会》卷一
  - `[ns_smth_894]` `[trigger: 开库合库时机]` `[factor_trigger: kaiku_heku_timing]` `[role: 条件分支]` 开库合库时机定时机。 → 《三命通会》卷一
  - `[ns_smth_895]` `[trigger: 看命层次]` `[factor_trigger: kanming_cengci]` `[role: 条件分支]` 看命层次定深度。 → 《三命通会》卷一
  - `[ns_smth_896]` `[trigger: 克禄风险]` `[factor_trigger: kelu_risk]` `[role: 条件分支]` 克禄有风险。 → 《三命通会》卷一
  - `[ns_smth_897]` `[trigger: 克中有克]` `[factor_trigger: kezhong_youke]` `[role: 条件分支]` 克中有克主复杂。 → 《三命通会》卷一
  - `[ns_smth_898]` `[trigger: 杀转印]` `[factor_trigger: killing_transforms_seal]` `[role: 条件分支]` 杀转印主化解。 → 《三命通会》卷一
  - `[ns_smth_899]` `[trigger: 空茫茫]` `[factor_trigger: kong_mangmang]` `[role: 条件分支]` 空茫茫主虚空。 → 《三命通会》卷一"""
    normalized_text_zh: str = """"""
    subject: str = "水主北方与润下之象"
    factor_refs: list = ['water', 'moistening_downward', 'nurturing', 'flowing_to_reach']
    
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_水主北方与润下之象_001_L1",
    )
    version: str = "1.0.0"
