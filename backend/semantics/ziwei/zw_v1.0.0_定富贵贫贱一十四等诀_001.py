"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.778553
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
    semantic_id="zw_v1.0.0_定富贵贫贱一十四等诀_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 定富贵贫贱一十四等诀(SemanticEntry):
    """
    - 分字分词释义：

  - **定富贵贫贱一十四等**：将人命划分为14个等级，从极贵到极贱。
  - **夹贵格**：吉星从两侧夹持命宫，形成贵气环护。
  - **夹败格**：凶星从两侧夹持命宫...
    """
    
    original_text: str = """- 分字分词释义：

  - **定富贵贫贱一十四等**：将人命划分为14个等级，从极贵到极贱。
  - **夹贵格**：吉星从两侧夹持命宫，形成贵气环护。
  - **夹败格**：凶星从两侧夹持命宫，形成困厄包围。
  - **日月并明**：太阳太阴同时明亮，三方照命。
  - **日照雷门**：太阳在卯宫（东方震位），日出之象。
  - **月朗天门**：太阴在亥宫（天门），月明之象。
  - **紫府朝垣**：紫微天府从三方来朝命宫。
  - **甲第登庸**：科举登第、受朝廷任用。
  - **商贾命**：适合经商的命格。
  - **术艺命**：适合工艺技术的命格。
  - **僧道命**：适合出家修道的命格。
  - **孤克命**：刑克六亲、孤独无依的命格。

#### 5.1 夹格系列（上等9格）

##### 5.1.1 夹贵格（6种）

- 六种夹贵：
  1. 紫府夹命
  2. 日月夹命
  3. 昌曲夹命
  4. 魁钺夹命
  5. 左右夹命
  6. 科权禄夹命

- 核心要点：
  - 六吉夹命，不贵即富
  - 前后二宫吉星夹命为夹贵
  - 需无凶杀冲破

##### 5.1.2 夹败格（3种）

- 三种夹败：
  1. 劫空夹命
  2. 火铃夹命
  3. 羊陀夹命

- 核心要点：
  - 凶星夹命主孤寒刑克
  - 命化忌加夹败更凶
  - 禄存在命庙旺+羊陀夹可解

##### 5.1.3 日月并明格

- 原文（断句）：

  论日月并明格者，财官迁移，三方守照者是也。如日月同居丑未宫安命者，三方无吉星合照，反为不美。如子午辰戌在命身尤好。

- 规范化释义（primary_lang_explained）：

  论日月并明格者财官迁移三方守照者是也。如日月同居丑未宫安命者三方无吉星合照反为不美。如子午辰戌在命身尤好。

- 核心要点：
  - 日月三方守照命宫
  - 子午辰戌命身尤好
  - 丑未同宫需三方吉照

##### 5.1.4 日照雷门格

- 原文（断句）：

  论太阳坐卯宫，为日照雷门格，卯宫安命，日生人合局。

- 规范化释义（primary_lang_explained）：

  论太阳坐卯宫为日照雷门格，卯宫安命日生人合局。

- 核心要点：太阳卯宫安命，日生人合格，主富贵双全

##### 5.1.5 月朗天门格

- 原文（断句）：

  论太阴居于亥宫，为月朗天门格，亥宫安命，夜生人合局。

- 规范化释义（primary_lang_explained）：

  论太阴居于亥宫为月朗天门格，亥宫安命夜生人合局。

- 核心要点：太阴亥宫安命，夜生人合格，主早扳仙桂

##### 5.1.6 紫府加会格

- 原文（断句）：

  论紫府加会格，三合照身命是也。天枢天库，位居一品之荣，又得暗禄逢迎，富贵双全之命。

- 规范化释义（primary_lang_explained）：

  论紫府加会格三合照身命是也。天枢天库位居一品之荣，又得暗禄逢迎富贵双全之命。

- 核心要点：紫府三合照命，位登一品，富贵双全

##### 5.1.7 府相朝垣格

- 原文（断句）：

  论府相朝垣格，三合照身命是也。命坐寅申者，上格，余次之。

- 规范化释义（primary_lang_explained）：

  论府相朝垣格三合照身命是也。命坐寅申者上格，余次之。

- 核心要点：府相三合照命，寅申最佳，主职位高迁

##### 5.1.8 仰面朝斗格

- 原文（断句）：

  论仰面朝斗格，子午宫安命者是也。

- 规范化释义（primary_lang_explained）：

  论仰面朝斗格子午宫安命者是也。

- 核心要点：子午宫安命，权贵荣身

##### 5.1.9 甲第登庸格

- 原文（断句）：

  论甲第登庸格，科星在命，权星或禄来朝是也。

- 规范化释义（primary_lang_explained）：

  论甲第登庸格科星在命权星或禄来朝是也。

- 核心要点：科星守命，权禄来朝，金榜题名

- 完整对等诠释（secondary_lang_full）：

  The fourteen grades of wealth and nobility open with nine 'upper' patterns that define the highest possible ceiling of status and resources in a chart.
  First are six flanking-noble formations, in which benefic stars stand on both sides of the Life or Body palace: Ziwei with Tianfu, the Sun with the Moon, Wenchang with Wenqu, Tiankui with Tianyue, Zuofu with Youbi, or the triad of Transformation-Examination, Transformation-Authority and Transformation-Salary. When these are cleanly formed and free from heavy affliction they always indicate either high office or great wealth.
  Next are three flanking-defeat formations, where malefic stars such as Jie and Kong, Huoxing and Lingxing, or Qingyang and Tuoluo press the Life palace from both sides. These speak of poverty, isolation and entanglement with punishments and lawsuits. In a few charts a strong Lucun placed in its own dignified position and supported by other benefics can ease the damage, but it cannot remove the underlying danger.
  Other upper patterns involve the Sun and Moon shining together in strength and mutually illuminating the Life or Body palace, especially when the Life or Body falls in Zi, Wu, Chen or Xu. Variants such as the Sun in Mao for daytime births, or the Moon in Hai for night births, are singled out for brilliant examination success, rapid promotion and enduring reputation.
  Finally, there are formations where Ziwei and Tianfu converge on the Life or Body palace, where Tianfu and Tianxiang face the Life palace from three directions, where the Life palace in Zi or Wu turns upward toward the Dipper, or where the star of academic success sits at the Life palace while Authority and Salary come to pay court. Taken together these describe the true summit of wealth-and-nobility potential: if the stars are dignified and not broken by heavy malefics, the native can attain first-rank posts, real power and honors that extend across generations.

- 叙事素材（narrative_snippets）：

  - **上等九格天花板**：六种夹贵、日月并明、日照雷门、月朗天门、紫府朝垣、仰面朝斗、甲第登庸，共同勾勒出命局可达的“权贵天花板”。
  - **六吉夹命**：紫府、日月、昌曲、魁钺、左右、科权禄等六种贵星前后夹命，只要不被重杀冲破，非富即贵。
  - **日月雷门与天门**：日坐卯宫为日照雷门、月居亥宫为月朗天门，配合日生/夜生时辰，常见科举题名、少年成名。
  - **紫府朝垣与甲第登庸**：紫微天府三合照命、科星守命而权禄来朝，象征“天枢天库开朝堂”，一举登庸。
  - **中等五格的厚实人生**：暗禄、对面朝斗、科权禄主、左右朝垣、兼文武，多主稳健富足而非极端显赫。
  - **特殊命格谱系**：商贾命、术艺命、僧道命、孤克命等，将职业道路与命运等级交织成一套“人生分层+分流”的图谱。

- L2-术语对齐（Term Glossary·5.1）：

  | 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
  |---------|---------|---------|---------|-----------|--------|
  | 夹贵格 | Flanking-Noble Pattern | 吉星夹命宫的上等格局 | Supreme pattern with benefics flanking Life Palace | combo_jiagui | existing |
  | 夹败格 | Flanking-Defeat Pattern | 凶星夹命宫的凶险格局 | Malefic pattern with malefics flanking Life Palace | combo_jiabai | new_candidate |
  | 日月并明 | Sun-Moon Co-Brightness | 日月三方守照命宫 | Sun-Moon three-directionally illuminating Life | combo_riyuebingming | new_candidate |
  | 日照雷门 | Sun Illuminating Thunder Gate | 太阳卯宫安命的吉格 | Auspicious pattern with Sun in Mao guarding Life | combo_rizhaolemen | new_candidate |
  | 月朗天门 | Moon Clarifying Heaven Gate | 太阴亥宫安命的吉格 | Auspicious pattern with Moon in Hai guarding Life | combo_yuelangtianmen | new_candidate |
  | 紫府朝垣 | Ziwei-Tianfu Facing Court | 紫府三合照命的上品格局 | Supreme pattern of Ziwei-Tianfu illuminating Life | combo_zifuchaoyuan | existing |
  | 甲第登庸 | First-Rank Imperial Appointment | 科权禄来朝的金榜题名格 | Examination-triumph pattern with transformations approaching | combo_jiadidengyang | new_candidate |

<!-- L2.5_BEGIN -->
#### L2.5 桥接层（5.1 上等九格）

**因子关系层**：

| 关系ID | 关系类型 | 因子A | 因子B | 关系性质 | 条件约束 | 效果方向 | source_ref |
|-------|---------|-------|-------|---------|---------|---------|-----------|
| rel_shangjiu_001 | flanking_pattern | jixing_jiage | geju_cengci | 夹星定格局 | 六吉夹命 | 增益 | 《定富贵贫贱诀》 |
| rel_shangjiu_002 | luminous_pattern | riyue_zuhe | geju_cengci | 日月定格局 | 日月三方照 | 增益 | 《定富贵贫贱诀》 |
| rel_shangjiu_003 | imperial_pattern | zifuzhaohe | geju_cengci | 紫府定格局 | 三合照命 | 增益 | 《定富贵贫贱诀》 |

**推理溯源层**：

| 证据ID | 原文锚点 | 涉及因子 | 推理步骤 | 结论方向 | 置信度 | 可生成规则 | 目标规则ID |
|-------|---------|---------|---------|---------|-------|----------|-----------|
| evi_shangjiu_001 | "六吉夹命，不贵即富" | combo_jiagui | 六吉夹命→贵气环护→不贵即富 | 夹贵主吉 | 高 | ✅ | rule_liuji_jiagui |
| evi_shangjiu_002 | "日月并明，财官迁移三方守照" | combo_riyuebingming | 日月三方照→光明普照→富贵双全 | 日月主贵 | 高 | ✅ | rule_riyuebingming |
| evi_shangjiu_003 | "紫府加会，位居一品之荣" | combo_zifuchaoyuan | 紫府三合→帝相朝垣→位至一品 | 紫府主贵 | 高 | ✅ | rule_zifuchaoyuan |

**跨体系概念映射层**：

| 概念ID | 共通语义 | 八字对应 | 占星对应 | 梦学对应 | 心理学对应 | 备注 |
|-------|---------|---------|---------|---------|-----------|------|
| concept_upper_grade | 上等格局 | 大格局成格 | 王族相位 | - | 成就顶峰 | 权贵天花板 |
| concept_flanking_blessing | 夹格祝福 | 夹拱贵人 | 夹角吉相 | - | 环境支持 | 外部资源 |
| concept_luminous_fortune | 日月光辉 | 日月并明 | 日月相位 | - | 光明前景 | 理想配置 |
<!-- L2.5_END -->

<!-- FACTOR_BEGIN -->

- 语义因子提取（因子层·八列表·5.1）：

  | 因子类型 | 因子标签（人话） | 因子ID | 因子来源 | 角色/位置 | 取值/约束 | engine_id | 备注 |
  |----------|-----------------|--------|----------|----------|----------|-----------|------|
  | 结构类 | 上等格局类型 | geju_cengci | new_candidate | 格局分类 | 夹贵/日月/紫府等 | ziwei_rule_engine | 权贵天花板 |
  | 关系类 | 夹星组合 | jixing_jiage | existing | 前后二宫 | 六吉夹/四凶夹 | ziwei_calculator | 夹格成败 |
  | 关系类 | 日月组合 | riyue_zuhe | existing | 日月配置 | 三方照/反背/同宫 | ziwei_calculator | 光照强度 |
  | 关系类 | 紫府组合 | zifuzhaohe | existing | 帝相配置 | 同宫/三合/朝垣 | ziwei_calculator | 帝相强度 |
  | 状态类 | 生人配合 | shengren_peihe | existing | 日生/夜生 | 日生/夜生/平常 | ziwei_rule_engine | 时辰匹配 |
  | 状态类 | 宫位强度 | gonwei_qiangdu | existing | 宫位等级 | 上格/次格/平常 | ziwei_calculator | 位置优劣 |
  | 结果类 | 格局成局度 | geju_chengjudu | existing | 成格评估 | 成格/半成/不成 | ziwei_rule_engine | 上限能否兑现 |

<!-- FACTOR_END -->

---

#### 5.2 中等格局（5格）

##### 5.2.1 暗禄格

- 原文（断句）：

  论暗禄格：禄存逢禄主，三合照命是也。俱在命宫尤妙。为明禄暗禄格。

- 规范化释义（primary_lang_explained）：

  论暗禄格禄存逢禄主三合照命是也。俱在命宫尤妙为明禄暗禄格。

- 核心要点：禄存+化禄同宫或三合，堆金积玉

##### 5.2.2 对面朝斗格

- 原文（断句）：

  论对面朝斗格，子午宫逢禄存是也。

- 规范化释义（primary_lang_explained）：

  论对面朝斗格子午宫逢禄存是也。

- 核心要点：子午宫禄存在迁移对照，双金富贵

##### 5.2.3 科权禄主格

- 核心要点：三化齐全，入相为王朝之功

##### 5.2.4 左右朝垣格

- 核心要点：辅弼三方照命，文武双显

##### 5.2.5 兼文武格

- 原文（断句）：

  论兼文武格，文曲、武曲在身命是也。

- 规范化释义（primary_lang_explained）：

  论兼文武格文曲武曲在身命是也。

- 核心要点：文武二曲守命，百事通达

---

#### 5.3 特殊命格判断

##### 5.3.1 商贾命

- 原文（断句）：

  论人有无商贾之命，如人命有巨，日紫府守照，为人安分，有仁德耿直之心，作事无私，不行邪僻，不肯妄求，为士为官，主有廉洁。如值月贪同杀忌星，心多机关，贪财无厌，暮夜求利之辈。

- 规范化释义（primary_lang_explained）：

  论人有无商贾之命。如人命有巨日紫府守照为人安分有仁德耿直之心作事无私不行邪僻不肯妄求，为士为官主有廉洁。如值月贪同杀忌星心多机关贪财无厌暮夜求利之辈。

- 核心要点：
  - 贪月同杀会机梁：因财计利作经商
  - 紫府遇擎羊+武曲迁移：利市场
  - 杀破廉贞同左右：远传扬

##### 5.3.2 术艺命

- 原文（断句）：

  论人命有无术艺者，寅申巳亥安命，或辰戌丑未，遇有贪狼。武曲在命化忌加杀，必作细巧艺术之人也。

- 规范化释义（primary_lang_explained）：

  论人命有无术艺者寅申巳亥安命或辰戌丑未遇有贪狼。武曲在命化忌加杀必作细巧艺术之人也。

- 核心要点：
  - 闲宫贪狼：屠人打铁、诸般巧艺
  - 破武未宫、巳亥破军：多巧艺
  - 天机天相：平生作奇工

##### 5.3.3 僧道命

- 原文（断句）：

  论出家僧道之命，紫微居卯酉，遇劫空者，看命无正星，又兼羊火劫空化忌者，更看父母、妻子三宫有杀者，方可断。及寅年申月巳日亥时，四正杀凑化，忌男僧道，女尼姑。

- 规范化释义（primary_lang_explained）：

  论出家僧道之命紫微居卯酉遇劫空者，看命无正星又兼羊火劫空化忌者更看父母妻子三宫有杀者方可断。及寅年申月巳日亥时四正杀凑化忌男僧道女尼姑。

- 核心要点：
  - 极居卯酉遇劫空：十人九为僧
  - 命坐空宫定出家
  - 天机七杀破梁同：羽客僧流

##### 5.3.4 孤克命

- 原文（断句）：

  论人命内犯孤克者，如克妻克子、克父母，内犯一二，不为僧道，亦作贫贱之人。第一看父母在庙旺地，有无吉凶星辰，如在陷加杀化忌，必主刑克。第二又看妻妾宫，三看子女宫，庙陷之地，有无吉凶星辰，如在陷加杀化忌，必鳏寡孤克论断可也。

- 规范化释义（primary_lang_explained）：

  论人命内犯孤克者如克妻克子克父母内犯一二不为僧道亦作贫贱之人。第一看父母在庙旺地有无吉凶星辰如在陷加杀化忌必主刑克。第二又看妻妾宫三看子女宫庙陷之地有无吉凶星辰如在陷加杀化忌必鳏寡孤克论断可也。

- 核心要点：
  - 依次看父母、妻妾、子女三宫
  - 陷地加杀化忌主刑克
  - 必鳏寡孤克

##### 5.3.5 寿夭淫荡

- 原文（断句）：

  贪狼入庙最高强，南极天同寿命长。北斗帝星无恶杀，绵上老耄衍祯祥。七杀临身终是夭，贪狼入庙定为娼。若于三合相临照，也学韩君去窃香。

- 规范化释义（primary_lang_explained）：

  贪狼入庙最高强南极天同寿命长。北斗帝星无恶杀绵上老耄衍祯祥。七杀临身终是夭贪狼入庙定为娼。若于三合相临照也学韩君去窃香。

- 核心要点：
  - 贪狼入庙+天同：寿命长
  - 七杀临身：终是夭
  - 贪狼入庙+凶杀：定为娼

##### 5.3.6 残疾破相

- 原文（断句）：

  论定人残疾，先看命宫星落陷，加羊陀火铃劫空忌宿，又看疾厄宫星庙陷，吉凶而断可也。

- 规范化释义（primary_lang_explained）：

  论定人残疾先看命宫星落陷加羊陀火铃劫空忌宿，又看疾厄宫星庙陷吉凶而断可也。

- 核心要点：
  - 命宫落陷+羊陀火铃劫空忌
  - 疾厄宫加杀
  - 主残疾破相

- 完整对等诠释（secondary_lang_full）：

  The 'middle five' patterns rank just below the upper nine and usually describe solid, dependable success rather than extreme eminence. Hidden-Salary refers to charts where Lucun and the star receiving Transformation-Salary guard or threefold aspect the Life palace, steadily accumulating pay, savings and property. Opposite-Facing Dipper appears when Lucun sits in the Migration palace of Zi or Wu facing the Life palace, doubling the symbols of metal and wealth. The Transformation-Triad Master pattern requires Examination, Authority and Salary all to be present and linked to the Life palace, pointing to ministerial achievement. When Zuofu and Youbi approach the Life palace from three directions it is called Assistants Facing the Court, giving both literary and martial distinction. When Wenchang and Wuqu guard the Life palace together, the person combines civil talent and martial capability and can handle many kinds of affairs.
  Beyond wealth and rank, this section also gives a group of 'special life-path' configurations. Merchant Destiny belongs to charts where stars such as Tanlang, Taiyin and Qisha dominate and incline the mind toward calculation and profit seeking, while combinations like Jumen, the Sun, Ziwei and Tianfu emphasize integrity and upright service in office, distinguishing the roles of trader and official. Craft-Artisan Destiny appears when Tanlang falls in idle or marginal palaces such as Yin, Shen, Si, Hai, Chen, Xu, Chou or Wei and is joined by Wuqu and other hard stars, describing butchers, metal workers and highly skilled artisans; Pojun with Wuqu in Wei or in Si or Hai, or Tianji paired with Tianxiang, points to people who spend their whole life creating unusual works. Monastic Destiny is seen when Ziwei in Mao or You is struck by void stars, or when the Life palace is empty or heavily configured with Tianji, Qisha, Pojun and Tianliang, and the houses of parents, spouse and children are also afflicted, so that one naturally turns toward the Daoist or Buddhist path.
  There are also patterns of Solitary-Affliction, where the houses of parents, spouse and children are successively fallen, afflicted and tabooed, so that the person is neither monk nor official yet lives in poverty and isolation. Other formulas distinguish longevity from premature death, and upright sensuality from destructive licentiousness: for example Tanlang in dignity together with Tiantong can indicate long life; Qisha at the Body can shorten life; Tanlang strongly configured with harsh malefics can show a life deeply entangled with the sex trade. Taken together, the middle-five and special life-path patterns refine the graded system of this section: they show not only how high or low one may rise, but also the concrete way in which one lives, works, profits or suffers within that range.

- L2-术语对齐（Term Glossary·5.2-5.3）：

  | 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
  |---------|---------|---------|---------|-----------|--------|
  | 暗禄格 | Hidden-Salary Pattern | 禄存化禄三合或同宫 | Lucun-transformation-Salary convergence | combo_anlu | new_candidate |
  | 商贾命 | Merchant Destiny | 因财计利的经商命格 | Destiny of profit-seeking commerce | career_shangjia | new_candidate |
  | 术艺命 | Craft-Artisan Destiny | 精于技艺的工匠命格 | Destiny of skilled craftsmanship | career_shuyi | new_candidate |
  | 僧道命 | Monastic Destiny | 出家僧道的命格配置 | Destiny configuration for clergy | fate_sengdao | new_candidate |
  | 孤克命 | Solitary-Affliction Destiny | 刑克亲缘的孤独命格 | Destiny afflicting familial bonds | fate_gukeming | new_candidate |
  | 鳏寡孤克 | Widowhood Loneliness Affliction | 丧偶孤独刑克的命运 | Fate of spousal loss and loneliness | state_guanguaguke | new_candidate |"""
    normalized_text_zh: str = """"""
    subject: str = "定富贵贫贱一十四等诀"
    factor_refs: list = ['source_ref', 'rel_14deng_001', 'geju_dengji', 'rel_14deng_002', 'zhiye_mingge', 'rel_14deng_003', 'guke_xingke', 'evi_14deng_001', 'combo_jiagui', 'rule_jiaguige', 'evi_14deng_002', 'fate_sengdao', 'rule_sengdaoming', 'evi_14deng_003', 'state_guanguaguke', 'rule_gukeming', 'concept_grade_system', 'concept_career_path', 'concept_affliction']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_定富贵贫贱一十四等诀_001_L1",
    )
    version: str = "1.0.0"
