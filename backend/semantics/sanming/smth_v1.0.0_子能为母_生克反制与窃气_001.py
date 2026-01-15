"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227505
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
    semantic_id="smth_v1.0.0_子能为母_生克反制与窃气_001",
    book_id="sanming",
    engine_id="bazi"
)
class 子能为母生克反制与窃气(SemanticEntry):
    """
    - **原文（source_text）**：
  五行相克，子皆能为母，复雠也。木克土，土之子金反克木；金克木，木之子火反克金；火克金，金之子水反克火；水克火，火之子土反克水；土克水，水之子木反克土。...
    """
    
    original_text: str = """- **原文（source_text）**：
  五行相克，子皆能为母，复雠也。木克土，土之子金反克木；金克木，木之子火反克金；火克金，金之子水反克火；水克火，火之子土反克水；土克水，水之子木反克土。互能相生，乃其始也；互能相克，乃其终也，皆出乎天之性也。《素问》所谓水生木，木复生火，是木受窃气，故水怒而克火。即子逢窃气，母乃力争，与母被鬼伤，子来力救，其义一也。强可攻弱，土得木而达；实可胜虚，水得土而绝；阴可消阳，火得水而灭；烈可敌刚，金得火而缺；坚可制柔，木得金而伐。故五者流行而更转，顺则相生，逆则相克，如是则各各为用，以成其道而已。

- 分字分词释义：
  - **子皆能为母，复雠**：本克制的母行，有时反被其所生之子行反制，等于「替母报仇」。
  - **窃气**：本应生扶之气被子行夺去，致使母行受损。

- **规范化释义（primary_lang_explained）**：
  本段说明五行生克并非单线条：木本克土，但土之子金又能克木；如此类推，形成一整套「子为母用」的反制系统。互相生扶是开始，互相克制是终局，皆出于天性。《素问》所谓水生木、木复生火，是说木从水受了过多之气，反致水怒而克火，像是子被夺气后替母出头。又以强弱、虚实、阴阳、刚柔诸观，说明何以土能通达、火能灭金、水能绝土、金能伐木等。总之，五行在流行转化中，顺则相生、逆则相克，各行其用，以成其道。

- **完整对等诠释（secondary_lang_full）**：

  This section explains that Five‑Element relations are not just simple one‑step controls. Wood overcomes Earth, yet Earth's child Metal can in turn control Wood; likewise through the whole cycle, creating a system in which the "child can act on behalf of the mother". Mutual generation marks the beginning of a process, mutual control its end; both belong to heaven's nature. The Suwen remark that "Water generates Wood and Wood in turn generates Fire" can, in certain contexts, describe Wood receiving so much Qi from Water that Water is effectively drained, and then "becomes angry" and moves to control Fire—like a child who has had its vitality stolen and stands up to defend the mother. By looking at strength vs. weakness, fullness vs. emptiness, Yin vs. Yang and hardness vs. softness, we can understand why in some situations Earth can penetrate, Fire can melt Metal, Water can eradicate Earth, and Metal can cut down Wood. For interpretation this means that within apparent help there may be hidden damage, and within apparent restriction there may be protection: generation can conceal control, and control can contain new possibilities of generation.

- **核心要点**：
  - 命局分析不能只看简单「谁生谁、谁克谁」，还要看子母之间的反制与窃气关系；
  - 在判断吉凶时，要结合强弱、虚实、阴阳、刚柔等层面，理解何时「生中有克」「克中有生」。

- **详细解说**：
  本节阐述五行生克的非线性机制。五行相克并非单向，子行能为母行复仇。木克土，但土之子金反克木；金克木，但木之子火反克金。互相生扶是开始，互相克制是终局，皆出于天性。窃气现象说明：子行过旺，泄尽母气，反致母行虽表面得生，实则元气受损。论命时，需识别母子关系、强弱配置、是否存在窃气，以及子行能否有效反制外敌。在职业与事件分析中，这反映了系统内部的自我调节与代际补偿机制。

- **应用推演（操作顺序）**：
  1) 在命局中为每一对母子五行标注关系：记录其生克方向、强弱与是否存在窃气现象；
  2) 推断吉凶时，先看「母行」再看「子行」：若子行夺气过度，则母行虽表面得生，实则元气受损；
  3) 在岁运分析中，注意运来之子行对原局母行的影响：有时看似助用，实则因窃气与反制而引发反向结果；
  4) 在系统设计中，为子母关系建立专门的权重与阈值逻辑，使模型能识别「过度生扶反致损伤」这种非线性效应。

- **反例与边界**：
  - 只按传统「生我者为印、我生者为食」等静态关系打分，而不看其在全局中的窃气与反制，造成「分高而实弱」的误判；
  - 遇到母行受制就简单断凶，不看到其子行仍可反制对方，为局中提供转机；
  - 在工程实现中，不建模子母窃气，只用线性加减法处理生克，难以解释许多「看似有生实则无力」或「表面被克实则有救」的命例；
  - 反过来，若过度依赖复杂窃气规则而不做验证，也可能让系统变得难以解释与维护，需要在理论与数据之间不断校正。

- **小例（示意）**：
  - 某命局中木克土为用，但土亦生金，金又有力克木。若行金运，则表面看是扶起子行，实则可能因子金过强而反伐用木；系统可通过子母关系的建模，提醒「此运虽有助，实含反制风险」。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_053]` `[trigger: 子能为母]` `[factor_trigger: wuxing_relation=child_for_mother AND counter_control=active]` `[role: 主干]` 五行相克，子皆能为母，复雠也。木克土，土之子金反克木。 → 《三命通会》卷一#论五行生成
  - `[ns_smth_054]` `[trigger: 窃气]` `[factor_trigger: wuxing_relation=stealing_qi AND mother_child_imbalance=true]` `[role: 主干依赖]` 水生木，木复生火，是木受窃气，故水怒而克火。即子逢窃气，母乃力争。 → 《三命通会》卷一#论五行生成
  - `[ns_smth_925]` `[trigger: 冲叠干支检查]` `[factor_trigger: chongdie_ganzhi_check]` `[role: 条件分支]` 冲叠干支检查定结构。 → 《三命通会》卷一
  - `[ns_smth_926]` `[trigger: 冲合类型]` `[factor_trigger: chonghe_leixing]` `[role: 条件分支]` 冲合类型定变化。 → 《三命通会》卷一
  - `[ns_smth_927]` `[trigger: 冲合气贯评分]` `[factor_trigger: chonghe_qiguan_score]` `[role: 条件分支]` 冲合气贯评分定强度。 → 《三命通会》卷一
  - `[ns_smth_928]` `[trigger: 冲合岁君风险]` `[factor_trigger: chonghe_suijun_risk]` `[role: 条件分支]` 冲合岁君有风险。 → 《三命通会》卷一
  - `[ns_smth_929]` `[trigger: 冲合刑破]` `[factor_trigger: chonghe_xingpo]` `[role: 条件分支]` 冲合刑破主变化。 → 《三命通会》卷一
  - `[ns_smth_930]` `[trigger: 冲开程度]` `[factor_trigger: chongkai_chengdu]` `[role: 条件分支]` 冲开程度定激活。 → 《三命通会》卷一
  - `[ns_smth_931]` `[trigger: 冲开发财]` `[factor_trigger: chongkai_facai]` `[role: 条件分支]` 冲开发财主有利。 → 《三命通会》卷一
  - `[ns_smth_932]` `[trigger: 冲开十神库]` `[factor_trigger: chongkai_shishenku]` `[role: 条件分支]` 冲开十神库主激活。 → 《三命通会》卷一
  - `[ns_smth_933]` `[trigger: 冲开显贵]` `[factor_trigger: chongkai_xiangui]` `[role: 条件分支]` 冲开显贵主有贵。 → 《三命通会》卷一
  - `[ns_smth_934]` `[trigger: 冲禄力量]` `[factor_trigger: chonglu_liliang]` `[role: 条件分支]` 冲禄力量定强度。 → 《三命通会》卷一
  - `[ns_smth_935]` `[trigger: 冲禄路径配置]` `[factor_trigger: chonglu_lujing_config]` `[role: 条件分支]` 冲禄路径配置定格局。 → 《三命通会》卷一
  - `[ns_smth_936]` `[trigger: 冲破身弱风险]` `[factor_trigger: chongpo_shenruo_risk]` `[role: 条件分支]` 冲破身弱有风险。 → 《三命通会》卷一
  - `[ns_smth_937]` `[trigger: 冲提纲]` `[factor_trigger: chongtigang]` `[role: 条件分支]` 冲提纲主冲击。 → 《三命通会》卷一
  - `[ns_smth_938]` `[trigger: 冲刑横流风险]` `[factor_trigger: chongxing_hengliu_risk]` `[role: 条件分支]` 冲刑横流有风险。 → 《三命通会》卷一
  - `[ns_smth_939]` `[trigger: 冲刑太过风险]` `[factor_trigger: chongxing_taiguo_risk]` `[role: 条件分支]` 冲刑太过有风险。 → 《三命通会》卷一
  - `[ns_smth_940]` `[trigger: 丑月混气态]` `[factor_trigger: chou_month_mixed_qi_state]` `[role: 条件分支]` 丑月混气态定状态。 → 《三命通会》卷一
  - `[ns_smth_941]` `[trigger: 丑未冲]` `[factor_trigger: chou_wei_chong]` `[role: 条件分支]` 丑未冲主冲突。 → 《三命通会》卷一
  - `[ns_smth_942]` `[trigger: 丑刑破巳]` `[factor_trigger: chou_xingpo_si]` `[role: 条件分支]` 丑刑破巳主损伤。 → 《三命通会》卷一
  - `[ns_smth_943]` `[trigger: 丑遥巳禄有无]` `[factor_trigger: chouyao_silu_presence]` `[role: 条件分支]` 丑遥巳禄有无定格局。 → 《三命通会》卷一
  - `[ns_smth_944]` `[trigger: 丑子损墓风险]` `[factor_trigger: chouzi_sunmo_risk]` `[role: 条件分支]` 丑子损墓有风险。 → 《三命通会》卷一
  - `[ns_smth_945]` `[trigger: 创业倾向]` `[factor_trigger: chuangye_qingxiang]` `[role: 条件分支]` 创业倾向定方向。 → 《三命通会》卷一
  - `[ns_smth_946]` `[trigger: 初吉后吉修]` `[factor_trigger: chuji_houjixiu]` `[role: 条件分支]` 初吉后吉修定时序。 → 《三命通会》卷一
  - `[ns_smth_947]` `[trigger: 纯从条件]` `[factor_trigger: chuncong_condition]` `[role: 条件分支]` 纯从条件定格局。 → 《三命通会》卷一
  - `[ns_smth_948]` `[trigger: 春冬月]` `[factor_trigger: chundong_yue]` `[role: 条件分支]` 春冬月定时令。 → 《三命通会》卷一
  - `[ns_smth_949]` `[trigger: 纯而无用]` `[factor_trigger: chuner_wuyong]` `[role: 条件分支]` 纯而无用主虚名。 → 《三命通会》卷一

<!-- L2_BEGIN -->
- **语义提取（L2）**：
  - **主题**：五行生克中的非线性机制：子能为母复仇与窃气
  - **自然属性**：
    - 象征：母被伤，子报仇
    - 特性：生克循环，强弱转化
    - 元素：母行、子行、鬼（克母者）
  - **功能象义**：
    - 解释反制机制：弱者（母）通过后代（子）制衡强者（鬼）
    - 揭示窃气原理：生多反损，气被盗泄
    - 完善生克逻辑：从单向生克走向循环平衡
  - **条件结构**：
    - **必要条件**：母子关系确立
    - **增强条件**：子行有力，能制伏鬼
    - **失效条件**：子行太弱，反被鬼伤
  - **多层解释**：
    - 字面层：木克土，土子金克木
    - 象征层：系统内部的自我调节与纠错
    - 实践层：论命需看子母救应，不可只看直克
    - 心理层：代际补偿，弱势反击

- **L2-术语对齐（Term Glossary）**：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 子能为母 | Child Acts for Mother | 子行能制伏克母之行 | Child element can control the element that controls its mother | child_for_mother | new_candidate |
| 复雠 | Revenge | 子克鬼，报母之仇 | Child controls Ghost, avenging Mother | revenge | new_candidate |
| 窃气 | Stealing Qi | 子行过旺，泄尽母气 | Child element too strong, draining Mother's Qi completely | stealing_qi | new_candidate |
| 反制 | Counter-Control | 被克者通过子行反克制行 | The controlled element counter-controls the controller via Child | counter_control | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| 因子类型 | 因子标签（人话） | 因子ID（必填） | 因子来源 | 角色/位置 | 取值/约束 | engine_id | 备注 |
|----------|------------------|--------------------|----------|----------|----------|-----------|------|
| 机制类 | 子能为母 | child_for_mother | existing | 救应机制 | 反制/复仇 | bazi_semantic | 母子链 |
| 关系类 | 生克反制 | counter_control | existing | 互动模式 | 循环/平衡 | bazi_semantic | 非线性 |
| 状态类 | 窃气 | stealing_qi | existing | 能量状态 | 泄耗/失衡 | bazi_semantic | 母虚子实 |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
- **因子关系层（Factor Relation）**：

| 关系ID | 关系类型 | 因子A | 因子B | 关系性质 | 条件约束 | 效果方向 | source_ref |
|--------|----------|-------|-------|----------|----------|----------|------------|
| rel_smth_033 | 生成 | mother | child | 母生子 | 五行链 | 正向 | 卷一#论五行生成 |
| rel_smth_034 | 反制 | child | enemy | 子克敌 | 母受伤 | 正向 | 卷一#论五行生成 |
| rel_smth_035 | 窃气 | child | mother | 子窃母气 | 过旺 | 负向 | 卷一#论五行生成 |

- **证据链层（Evidence Chain）**：

| 证据ID | 原文锚点 | 涉及因子 | 推理步骤 | 结论方向 | 置信度 | 可生成规则 | 目标规则ID |
|--------|----------|----------|----------|----------|--------|------------|------------|
| evi_smth_037 | 子皆能为母，复雠 | child, mother, enemy | 母被克→子反制 | 正向 | 高 | 是 | L3_CANDIDATE |
| evi_smth_038 | 木受窃气，故水怒 | child, stealing_qi | 子过旺→泄母气 | 负向 | 高 | 是 | L3_CANDIDATE |
| evi_smth_039 | 强可攻弱，实可胜虚 | strength, weakness | 强弱转化 | 中性 | 高 | 是 | L3_CANDIDATE |

- **跨系统映射层（Cross-System Mapping）**：

| 概念ID | 共通语义 | 八字对应 | 占星对应 | 梦学对应 | 心理学对应 | 备注 |
|--------|----------|----------|----------|----------|------------|------|
| concept_child_for_mother | 代际补偿 | child_for_mother | generational_aspect | family_rescue_dreams | intergenerational_support | 家族原型 |
| concept_stealing_qi | 能量失衡 | stealing_qi | energy_drain | depletion_dreams | resource_depletion | 失衡原型 |
<!-- L2.5_END -->

---

## 论支干源流

### 1. 干支之象与十干十二支

- **原文（source_text）**：
  夫干犹木之干，强而为阳；支犹木之枝，弱而为阴。昔盘古氏明天地之道，达阴阳之变为三才。首君以天地既分之后，先有天而后有地，由是气化而人生焉，故天皇氏一姓十三人，继盘古氏以治，是曰天灵淡泊，无为而俗自化，始制干支之名，以定岁之所在。其十干曰：于逢、旃蒙、柔兆、疆圉、著雍、屠维、上章、重光、玄??、昭阳；十二支曰：困敦、赤奋若、摄提格、单于、执徐、大荒落、敦洋、协洽、??滩、作噩、阉茂、大渊献。蔡邕独断曰：「干，干也，其名有十，亦曰十母，即今甲乙丙丁戊己庚辛壬癸是也；支，枝也，其名十有二，亦曰十二子，即今子丑寅卯辰已午未申酉戍亥是也。」

- 分字分词释义：
  - **干/支**：
    - 干如木干，主中枢、纲纪，属阳；
    - 支如木枝，主分支、末节，属阴。
  - **十母/十二子**：古人称十干为「十母」、十二支为「十二子」，意在强调干为本、支为末、干支相属的关系。
  - **十干、十二支古名**：于逢等十名、困敦等十二名，为传说中三皇时代所立的最早干支名号。

- **规范化释义（primary_lang_explained）**：
  本段先用树干、树枝作比喻，说明「干」如树干、主干强而为阳，「支」如树枝、末梢弱而为阴。又以盘古、天皇氏等传说叙述：最初圣王明白天地阴阳之道，于是创制干支之名，用以标定岁序。十干被称作「十母」，十二支被称作「十二子」，并各有一套古名。蔡邕进一步解释「干」「支」字义，指出今之甲乙丙丁……与子丑寅卯……，皆承此系统而来。

- **完整对等诠释（secondary_lang_full）**：

  Here the origins of the stem–branch system are explained through the image of a tree: the stem is like the trunk—strong and central, belonging to Yang; the branch is like the limbs—peripheral and relatively weak, belonging to Yin. Early sage‑kings, having grasped the workings of heaven and earth, created names for the Heavenly Stems and Earthly Branches to mark the sequence of years. The Ten Stems were called the "Ten Mothers" and the Twelve Branches the "Twelve Children", each with its own archaic designation. Later commentators such as Cai Yong clarified that our present Jia, Yi, Bing, Ding… and Zi, Chou, Yin, Mao… all inherit from this same structure. In practice this underpins the idea that stems are the guiding backbone while branches supply detailed outgrowth, and that every pillar in a chart consists of a mother–child pair rather than a single undifferentiated sign.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_ganzhi_001]` `[trigger: 干支之象]` `[factor_trigger: gan_mu_zhi_zi AND ganzhi_yuanliu]` `[role: 主干]` 干犹木之干，强而为阳；支犹木之枝，弱而为阴。 → 《三命通会》卷一#干支之象
  - `[ns_smth_01_ganzhi_002]` `[trigger: 十母十二子]` `[factor_trigger: shimu_shierzi AND ganzhi_mingming]` `[role: 主干依赖]` 十干亦曰十母，十二支亦曰十二子。 → 《三命通会》卷一#干支之象
  - `[ns_smth_01_ganzhi_003]` `[trigger: 天皇始制]` `[factor_trigger: tianhuang_shizhi AND ganzhi_suozai]` `[role: 条件分支]` 天皇氏始制干支之名，以定岁之所在。 → 《三命通会》卷一#干支之象
  - `[ns_smth_01_ganzhi_004]` `[trigger: 纲目层级]` `[factor_trigger: gan_weigang_zhi_weimu AND jiegouxing]` `[role: 总结]` 干为纲，支为目，是命局结构中本体与分支的基本区分。 → 《三命通会》卷一#干支之象
  - `[ns_smth_950]` `[trigger: 纯全程度]` `[factor_trigger: chunquan_chengdu]` `[role: 条件分支]` 纯全程度定格局。 → 《三命通会》卷一
  - `[ns_smth_951]` `[trigger: 春旺木气]` `[factor_trigger: chunwang_muqi]` `[role: 条件分支]` 春旺木气主木旺。 → 《三命通会》卷一
  - `[ns_smth_952]` `[trigger: 出身卑微]` `[factor_trigger: chushen_beiwei]` `[role: 条件分支]` 出身卑微主低微。 → 《三命通会》卷一
  - `[ns_smth_953]` `[trigger: 出身根基配置]` `[factor_trigger: chushen_genji_config]` `[role: 条件分支]` 出身根基配置定格局。 → 《三命通会》卷一
  - `[ns_smth_954]` `[trigger: 次官清秀]` `[factor_trigger: ciguan_qingxiu]` `[role: 条件分支]` 次官清秀主有品。 → 《三命通会》卷一
  - `[ns_smth_955]` `[trigger: 气候热湿指数]` `[factor_trigger: climate_heat_moist_index]` `[role: 条件分支]` 气候热湿指数定时令。 → 《三命通会》卷一
  - `[ns_smth_956]` `[trigger: 当令标签]` `[factor_trigger: commanding_season_label]` `[role: 条件分支]` 当令标签定位置。 → 《三命通会》卷一
  - `[ns_smth_957]` `[trigger: 条件因子]` `[factor_trigger: cond_factor]` `[role: 条件分支]` 条件因子定条件。 → 《三命通会》卷一
  - `[ns_smth_958]` `[trigger: 从财程度]` `[factor_trigger: congcai_chengdu]` `[role: 条件分支]` 从财程度定格局。 → 《三命通会》卷一
  - `[ns_smth_959]` `[trigger: 从格格局有无]` `[factor_trigger: congge_ge_presence]` `[role: 条件分支]` 从格格局有无定格局。 → 《三命通会》卷一
  - `[ns_smth_960]` `[trigger: 从格之身旺]` `[factor_trigger: congge_zhi_shenwang]` `[role: 条件分支]` 从格之身旺定强度。 → 《三命通会》卷一
  - `[ns_smth_961]` `[trigger: 从清入浊]` `[factor_trigger: congqing_ruzhuo]` `[role: 条件分支]` 从清入浊主变化。 → 《三命通会》卷一
  - `[ns_smth_962]` `[trigger: 从势配置]` `[factor_trigger: congshi_config]` `[role: 条件分支]` 从势配置定格局。 → 《三命通会》卷一
  - `[ns_smth_963]` `[trigger: 核心因子]` `[factor_trigger: core_factor]` `[role: 条件分支]` 核心因子定主干。 → 《三命通会》卷一
  - `[ns_smth_964]` `[trigger: 宇宙阶段太初]` `[factor_trigger: cosmic_stage_taichu]` `[role: 条件分支]` 宇宙阶段太初定起源。 → 《三命通会》卷一
  - `[ns_smth_965]` `[trigger: 宇宙阶段太始]` `[factor_trigger: cosmic_stage_taishi]` `[role: 条件分支]` 宇宙阶段太始定起源。 → 《三命通会》卷一
  - `[ns_smth_966]` `[trigger: 宇宙阶段太素]` `[factor_trigger: cosmic_stage_taisu]` `[role: 条件分支]` 宇宙阶段太素定起源。 → 《三命通会》卷一
  - `[ns_smth_967]` `[trigger: 宇宙阶段太易]` `[factor_trigger: cosmic_stage_taiyi]` `[role: 条件分支]` 宇宙阶段太易定起源。 → 《三命通会》卷一
  - `[ns_smth_968]` `[trigger: 宇宙论无名]` `[factor_trigger: cosmology_wuming]` `[role: 条件分支]` 宇宙论无名定起源。 → 《三命通会》卷一
  - `[ns_smth_969]` `[trigger: 宇宙论有名]` `[factor_trigger: cosmology_youming]` `[role: 条件分支]` 宇宙论有名定起源。 → 《三命通会》卷一
  - `[ns_smth_970]` `[trigger: 大昌志在]` `[factor_trigger: dachang_zhizai]` `[role: 条件分支]` 大昌志在主有志。 → 《三命通会》卷一
  - `[ns_smth_971]` `[trigger: 大富]` `[factor_trigger: dafu]` `[role: 条件分支]` 大富主富贵。 → 《三命通会》卷一
  - `[ns_smth_972]` `[trigger: 大贵人符合]` `[factor_trigger: daguiren_fuhe]` `[role: 条件分支]` 大贵人符合主有贵。 → 《三命通会》卷一
  - `[ns_smth_973]` `[trigger: 带合组合类型]` `[factor_trigger: daihe_zuhe_leixing]` `[role: 条件分支]` 带合组合类型定格局。 → 《三命通会》卷一
  - `[ns_smth_974]` `[trigger: 带孝早刑风险]` `[factor_trigger: daixiao_zaoxing_risk]` `[role: 条件分支]` 带孝早刑有风险。 → 《三命通会》卷一"""
    normalized_text_zh: str = """"""
    subject: str = "子能为母：生克反制与窃气"
    factor_refs: list = ['child_for_mother', 'revenge', 'stealing_qi', 'counter_control']
    
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
        l1_anchor="smth_v1.0.0_子能为母_生克反制与窃气_001_L1",
    )
    version: str = "1.0.0"
