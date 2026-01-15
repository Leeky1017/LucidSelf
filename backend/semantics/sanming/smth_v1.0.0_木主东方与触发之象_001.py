"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227454
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
    semantic_id="smth_v1.0.0_木主东方与触发之象_001",
    book_id="sanming",
    engine_id="bazi"
)
class 木主东方与触发之象(SemanticEntry):
    """
    - **原文（source_text）**：
  木主于东，应春。木之为言触也，阳气触动，冒地而生也。水流趋东以生木也；木上发而覆下，乃自然之质也。

- 分字分词释义：
  - **触**：触发、触...
    """
    
    original_text: str = """- **原文（source_text）**：
  木主于东，应春。木之为言触也，阳气触动，冒地而生也。水流趋东以生木也；木上发而覆下，乃自然之质也。

- 分字分词释义：
  - **触**：触发、触动之意，指阳气一来，草木破土而出。
  - **冒地而生**：从地下冒出地面，象征生机勃发。

- **规范化释义（primary_lang_explained）**：
  木属东方，对应春季。所谓「触」，就是阳气一来，草木就从地里冒出来。水气东行以滋养木，木则向上发生、向下覆荫，这是木的自然形质。

- **完整对等诠释（secondary_lang_full）**：

  Wood belongs to the East and corresponds to spring. The character "chu" (touch) points to the instant when Yang Qi stirs and plants push up through the soil. Water flows eastward to nourish Wood; Wood in turn grows upward and spreads its canopy downward. In destiny terms, Wood represents beginnings, growth and initiative: the moment when something latent is triggered into visible life. For Wood to function well it needs a source of moisture and the right seasonal timing; without Water or in the wrong season, even abundant Wood can become withered or distorted, and if Metal cuts it harshly when there is no Water to mediate, its vitality is easily damaged.

- **核心要点**：
  - 命局之木，象征生发、伸展、触机而动，多与成长、启始、规划相关；
  - 木得水滋、逢春令，则生发有源；若无水承、反被金伐，则生机受损。

- **详细解说**：
  本节阐述木的东方属性与触发机能。木主东方应春，其义为「触」——阳气触动，万物破土而出。水气东行以滋养木，木则向上发生、向下覆荫，此为木的自然形质。论命时，木旺而有水承、逢春令，则生发有源；若无水承、反被金伐，则生机受损。在职业与事件分析中，木常与新项目、新领域、新学习有关，可作为触发节点而非终局。

- **应用推演（操作顺序）**：
  1) 解命时先看「木」所处之地支与节令：在东方、春令而得水，则为顺势生发；
  2) 将「触」理解为「触发点」：在职业与事件分析中，木常与新项目、新领域、新学习有关，可作为触发节点而非终局；
  3) 在看用神时，若木为用，宜配合水与适度之火，使其有源、有方向；若木为忌，则需考量以金节木、以土制水等方案，避免一味克伐损及整体生机；
  4) 在系统设计中，可把「木」相关规则集中归类为「成长与启动模块」，与财务、成果类（金）规则区分层级。

- **反例与边界**：
  - 见木旺便一味称吉，忽视木过旺亦可为病，如过度扩张、计划过多而执行不足；
  - 将所有与教育、文化、技术相关的职业都简单归于木，而不考虑其中金（水）气的成分（如制度、算法、资金），导致职业映射过粗；
  - 在工程化中，把「木主东方」简单理解为现实空间的东边，而不结合命局整体方位结构和具体场景，可能失之僵硬；
  - 反之，只按现实行业分类，不回到五行象意的源头，容易让命理系统与传统经典完全脱节。

- **小例（示意）**：
  - 某命局木旺而水足，生于春初，从事产品策划与课程研发，每逢行木火运时常有新项目启动；系统可据此把「木旺 + 春令 + 水承」与「适宜承接启动型工作」建立关联，用于职业/阶段性任务推荐；
  - 在企业命盘或项目运势分析中，将关键启动时点映射到木气较旺的时间窗口（例如立春后若干日），以顺应「木之触发」之象，而非随意择期。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_041]` `[trigger: 木主东方]` `[factor_trigger: direction=east AND wuxing=wood]` `[role: 主干]` 木主于东，应春。木之为言触也，阳气触动，冒地而生也。 → 《三命通会》卷一#论五行生成
  - `[ns_smth_042]` `[trigger: 水生木]` `[factor_trigger: wuxing_shengke=water_generates_wood]` `[role: 主干依赖]` 水流趋东以生木也；木上发而覆下，乃自然之质也。 → 《三命通会》卷一#论五行生成
  - `[ns_smth_800]` `[trigger: 贵人]` `[factor_trigger: guiren]` `[role: 主干]` 贵人主有贵气。 → 《三命通会》卷一
  - `[ns_smth_801]` `[trigger: 贵人带财官]` `[factor_trigger: guiren_dai_caiguan]` `[role: 条件分支]` 贵人带财官主大贵。 → 《三命通会》卷一
  - `[ns_smth_802]` `[trigger: 贵人化刑评分]` `[factor_trigger: guiren_huaxing_score]` `[role: 条件分支]` 贵人化刑评分定解厄。 → 《三命通会》卷一
  - `[ns_smth_803]` `[trigger: 贵人力量强度]` `[factor_trigger: guiren_liliang_qiangdu]` `[role: 条件分支]` 贵人力量强度定作用。 → 《三命通会》卷一
  - `[ns_smth_804]` `[trigger: 过度风险]` `[factor_trigger: guodu_fengxian]` `[role: 条件分支]` 过度风险主失衡。 → 《三命通会》卷一
  - `[ns_smth_805]` `[trigger: 过旺失衡风险]` `[factor_trigger: guowang_shiheng_risk]` `[role: 条件分支]` 过旺失衡有风险。 → 《三命通会》卷一
  - `[ns_smth_806]` `[trigger: 骨肉离散风险]` `[factor_trigger: gurou_lisan_risk]` `[role: 条件分支]` 骨肉离散有风险。 → 《三命通会》卷一
  - `[ns_smth_807]` `[trigger: 孤僧道风险]` `[factor_trigger: gusengdao_risk]` `[role: 条件分支]` 孤僧道有风险。 → 《三命通会》卷一
  - `[ns_smth_808]` `[trigger: 亥卯未组合]` `[factor_trigger: hai_mao_wei_combo]` `[role: 条件分支]` 亥卯未组合定木局。 → 《三命通会》卷一
  - `[ns_smth_809]` `[trigger: 亥卯未木局]` `[factor_trigger: haimaoweimu_ju]` `[role: 条件分支]` 亥卯未木局主木旺。 → 《三命通会》卷一
  - `[ns_smth_810]` `[trigger: 亥水忌火]` `[factor_trigger: haishui_jihuo]` `[role: 条件分支]` 亥水忌火主相战。 → 《三命通会》卷一
  - `[ns_smth_811]` `[trigger: 亥未鼠牛]` `[factor_trigger: haiwei_shuniu]` `[role: 条件分支]` 亥未鼠牛主组合。 → 《三命通会》卷一
  - `[ns_smth_812]` `[trigger: 亥月水局泛滥]` `[factor_trigger: haiyue_shuiju_fanlan]` `[role: 条件分支]` 亥月水局泛滥主过旺。 → 《三命通会》卷一
  - `[ns_smth_813]` `[trigger: 亥子入格]` `[factor_trigger: haizi_ruge]` `[role: 条件分支]` 亥子入格主有力。 → 《三命通会》卷一
  - `[ns_smth_814]` `[trigger: 亥子天时风险]` `[factor_trigger: haizi_tianshi_risk]` `[role: 条件分支]` 亥子天时有风险。 → 《三命通会》卷一
  - `[ns_smth_815]` `[trigger: 豪雨难极]` `[factor_trigger: haoyu_nanji]` `[role: 条件分支]` 豪雨难极主极端。 → 《三命通会》卷一
  - `[ns_smth_816]` `[trigger: 土多木少崩溃]` `[factor_trigger: heavy_earth_little_wood_collapse]` `[role: 条件分支]` 土多木少崩溃有风险。 → 《三命通会》卷一
  - `[ns_smth_817]` `[trigger: 合格成立]` `[factor_trigger: hege_chengli]` `[role: 条件分支]` 合格成立主有力。 → 《三命通会》卷一
  - `[ns_smth_818]` `[trigger: 合化成功]` `[factor_trigger: hehua_chenggong]` `[role: 条件分支]` 合化成功主变质。 → 《三命通会》卷一
  - `[ns_smth_819]` `[trigger: 合局暗合稳固]` `[factor_trigger: heju_anhe_wengu]` `[role: 条件分支]` 合局暗合稳固主有力。 → 《三命通会》卷一
  - `[ns_smth_820]` `[trigger: 合身冲破风险]` `[factor_trigger: heshen_chongpo_risk]` `[role: 条件分支]` 合身冲破有风险。 → 《三命通会》卷一
  - `[ns_smth_821]` `[trigger: 合身羁绊风险]` `[factor_trigger: heshen_jiban_risk]` `[role: 条件分支]` 合身羁绊有风险。 → 《三命通会》卷一
  - `[ns_smth_822]` `[trigger: 合住禄马]` `[factor_trigger: hezhu_luma]` `[role: 条件分支]` 合住禄马主有力。 → 《三命通会》卷一
  - `[ns_smth_823]` `[trigger: 合住禄马程度]` `[factor_trigger: hezhu_luma_chengdu]` `[role: 条件分支]` 合住禄马程度定强度。 → 《三命通会》卷一
  - `[ns_smth_824]` `[trigger: 暗藏需冲激活]` `[factor_trigger: hidden_needs_clash_activate]` `[role: 条件分支]` 暗藏需冲激活方显。 → 《三命通会》卷一"""
    normalized_text_zh: str = """"""
    subject: str = "木主东方与触发之象"
    factor_refs: list = ['wood', 'trigger', 'sprouting', 'upward_downward_cover']
    
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
        l1_anchor="smth_v1.0.0_木主东方与触发之象_001_L1",
    )
    version: str = "1.0.0"
