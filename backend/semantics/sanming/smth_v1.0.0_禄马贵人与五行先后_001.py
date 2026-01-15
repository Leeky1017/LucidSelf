"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101388
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
    semantic_id="smth_v1.0.0_禄马贵人与五行先后_001",
    book_id="sanming",
    engine_id="bazi"
)
class 禄马贵人与五行先后(SemanticEntry):
    """
    - **原文（source_text）**：
  《天乙妙旨》云：「君不见，禄马贵人无准托，考究五行之恶，天元羸弱未为灾，地气坚牢足欢乐。」《源髓歌》云：「禄马更有多般说，自衰自死兼败绝；若无吉煞加助...
    """
    
    original_text: str = """- **原文（source_text）**：
  《天乙妙旨》云：「君不见，禄马贵人无准托，考究五行之恶，天元羸弱未为灾，地气坚牢足欢乐。」《源髓歌》云：「禄马更有多般说，自衰自死兼败绝；若无吉煞加助时，定知破祖多浮劣。」可见先论五行，后看禄马：五行要生旺，禄马怕衰绝。司马季主云：「禄多马少，使主神劳；禄少马多，能操善负。」

- **分字分词释义**：
  - **天元羸弱未为灾、地气坚牢足欢乐**：天干之气稍弱并非必灾，只要地支结构稳固，仍可安泰。
  - **禄马更有多般说，自衰自死兼败绝**：提示禄马格局变化繁多，其中不少带有衰、死、败绝之象。
  - **先论五行，后看禄马**：强调以全局五行旺衰为本，再看禄马贵人之增损，不可本末倒置。
  - **禄多马少 / 禄少马多**：禄象资源与位置，马象动与劳役；两者失衡则有不同问题。
 
- **规范化释义（primary_lang_explained）**：
  这一节用数条古文总结禄马与五行的关系：《天乙妙旨》指出，禄马贵人的吉凶没有固定模式，关键在于五行本身是否失衡：即便天干之「天元」有些羸弱，只要地支之「地气」坚牢，人生仍可安乐持久；若一味追逐禄马而忽视五行之恶，则易误判。《源髓歌》提醒，禄马说法甚多，其中不少格局自带衰、死、败绝之象，若不见吉煞相助，常常表现为破祖、漂泊与品行浮劣。作者因此强调：论命当先看五行气势是否生旺调和，禄马贵人只在其后锦上添花；若本局五行衰绝，则禄马难以挽回大局。司马季主所言「禄多马少，使主神劳；禄少马多，能操善负」，则从比例角度提示：禄多马少，主神（当令之五行）需独力承担过多资源与职责，易劳；禄少马多，则虽辛苦奔波，却能练就负荷之能，各有利弊。
 
- **核心要点**：
  - 禄、马、贵人皆为「配置层特征」，真正的根基在于五行整体的旺衰、中和与否。
   - 看禄马之前必须先审局中五行：若本局偏枯或极端，即便禄马众多，也可能成为「负担」「破祖」之源。
   - 工程建模时，应将五行平衡度作为一级指标，禄马贵人类特征作为二级修正项，避免模型被「神煞名目」主导而偏离五行本体。
 
- **详细解说**：
  1) 为每一命局先计算五行力量与平衡度指标（如用神得气度、偏枯指数、冷热燥湿等），形成基础状态向量；
   2) 在此基础上，提取禄、马、贵人等结构特征，并根据其是否落在用神宫、是否成局、有无空亡破败，对其作为「增益/负担」的方向和强度进行编码；
   3) 在综合评分与解释层中，始终先展示五行整体状况，再用禄马贵人对特定维度（迁移机会、职位平台、贵助程度等）做修正说明；
   4) 在训练和验证阶段，对比「仅用五行基线」与「五行 + 禄马贵人」两种模型的增益，防止后者在数据不足时反而引入噪音。
 
- 反例与边界：
  - 不宜在五行极端失衡（如从格未成、严重偏枯）时，仍以禄马贵人作为扭转结论的关键依据，容易高估神煞的修复能力；
   - 不能只因命局禄马繁多，就断定必然贵显富裕，而忽视现实中的教育、行业、社会资本等变量；
   - 工程实现中若将禄马贵人当作与五行同权的主特征，会导致模型在样本稀疏区域过度依赖神煞名目，解释虽华丽但稳定性差；
   - 反向误区是完全去掉禄马贵人，只保留五行强弱，使得模型缺少对「资源平台」「迁移机会」「贵人助力」等中观层面的刻画能力。
 
- 小例（示意）：
  - 某命局五行中和、用神得力，而禄马贵人结构一般，系统在解释中以「基础盘稳、资源与机会属常态」为主，不会因为少数神煞不足而给出过度悲观结论；
  - 另一命局五行偏枯、煞重，而禄马贵人看似繁多，系统则强调「结构负担与破祖漂泊风险」，并提示禄马更多只是放大既有失衡，而非凭空带来贵气。

<!-- L2_BEGIN -->
- **语义提取（L2）**：
  - **主题**：禄马贵人与五行先后关系的配置层与根基层判断框架
  - **自然属性**：象征先论五行后看禄马、天元羸弱地气坚牢、禄多马少神劳、禄少马多善负；特性配置层vs根基层、锦上添花vs本末、五行旺衰为根基；元素五行平衡度与禄马贵人配置
  - **功能象义**：为禄马贵人定位配置层；区分根基与修饰关系；强调五行为本不可倒置
  - **条件结构**：必要条件先审五行整体状况；增强条件禄马在用神宫有气；失效条件本末倒置或五行衰绝
  - **多层解释**：字面层描述先五行后禄马原则；象征层禄马为配置五行为根基；实践层提示建模优先级与权重；心理层鼓励识别本质与修饰

- **L2-术语对齐（Term Glossary）**：
| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---|---|---|---|
| 天元羸弱地气坚牢 | Heavenly-Stem Weak Earthly-Branch Firm | 天干之气稍弱并非必灾只要地支结构稳固仍可安泰 | Heavenly-stem qi slightly weak not必-disaster, as long as earthly-branch structure firm still peaceful | - | new_candidate |
| 先论五行后看禄马 | Five-Elements First Lu-Ma Second | 论命当先看五行气势禄马贵人只在其后锦上添花 | Destiny-reading should first see five-elements momentum, lu-ma nobles only后 add icing | - | new_candidate |
| 禄多马少神劳 | Much-Lu Less-Horse Spirit-Toil | 禄多马少主神需独力承担过多资源与职责易劳 | Much-lu less-horse, ruling-spirit needs独力 bear excessive resources-duties, easily toil | - | new_candidate |

- 完整对等诠释（secondary_lang_full）：

  This section presents "Lu-Horse-Nobles and Five Elements Priority":

  The Tianyi Miaozhi states: "Lu-Horse-Nobles have no fixed standard - investigate the Five Elements' flaws. Heavenly stem slightly weak is not disaster; Earthly branch firm brings lasting joy." The Yuansui Song warns: many Lu-Horse patterns carry decline, death, defeat, extinction - without auspicious sha support, they lead to ancestral ruin and drifting.

  Core principle: "First discuss Five Elements, then examine Lu-Horse." Five Elements must be prosperous and balanced; Lu-Horse fears decline and extinction. Sima Jizhu adds: "Much Lu, less Horse - ruling spirit toils alone; Less Lu, much Horse - develops burden-bearing capacity."

  Engineering note: Five Elements balance should be a primary indicator; Lu-Horse-Noble features should be secondary modifiers. Avoid models dominated by sha-names while ignoring Five Elements fundamentals.

<!-- FACTOR_BEGIN -->
| 因子类型 | 因子标签（人话） | 因子ID（如已存在） | 因子来源 | 角色/位置 | 取值/约束 | engine_id | 备注 |
|----------|------------------|--------------------|----------|----------|----------|------|
| 理论类 | 五行为本 | bazi_wuxing_2 | existing | 优先级原则 | 先五行后神煞 | bazi_semantic | 根基层 |
| 关系类 | 禄马配置层 | bazi_relation_config | existing | 修饰作用 | 锦上添花 | bazi_semantic | 非根基 |
| 状态类 | 禄多马少 | bazi_state_factor_115 | existing | 失衡状态 | 资源重动象轻 | bazi_semantic | 神劳 |
| 状态类 | 禄少马多 | bazi_state_factor_116 | existing | 失衡状态 | 动象重资源轻 | bazi_semantic | 善负 |
| 条件类 | 五行旺衰 | bazi_condition_wuxing_wangshuai | existing | 基础判断 | 生旺则吉 | bazi_semantic | 衰绝则凶 |
<!-- FACTOR_END -->
<!-- L2_END -->

<!-- L2.5_BEGIN -->
#### L2.5 桥接层

**因子关系层**：

| 关系ID | 关系类型 | 因子A | 因子B | 关系性质 | 条件约束 | 效果方向 | source_ref |
|-------|---------|-------|-------|---------|---------|---------|-----------|
| rel_smth_zonglun_001 | priority | wuxing_base | luma_modifier | 五行为本禄马为修饰 | 先五行后禄马 | 层级关系 | 《三命通会》卷三#总论禄马 |
| rel_smth_zonglun_002 | condition | wuxing_wangshuai | luma_effect | 五行旺衰决定禄马效果 | 生旺则吉衰绝则凶 | 条件依赖 | 《三命通会》卷三#总论禄马 |
| rel_smth_zonglun_003 | imbalance | lu_duo_ma_shao | shen_lao | 禄多马少神劳 | 资源重动象轻 | 失衡凶 | 《三命通会》卷三#总论禄马 |
| rel_smth_zonglun_004 | imbalance | lu_shao_ma_duo | shan_fu | 禄少马多善负 | 动象重资源轻 | 失衡吉 | 《三命通会》卷三#总论禄马 |

**推理溯源层**：

| 证据ID | 原文锚点 | 涉及因子 | 推理步骤 | 结论方向 | 置信度 | 可生成规则 | 目标规则ID |
|-------|---------|---------|---------|---------|-------|----------|-----------|
| evi_smth_zonglun_001 | "先论五行，后看禄马" | priority | 五行为根基→禄马为修饰→优先级明确 | 层级原则 | 高 | ✅ | rule_wuxing_first |
| evi_smth_zonglun_002 | "禄多马少，使主神劳" | imbalance | 禄多马少→承担过重→神劳 | 失衡预警 | 高 | ✅ | rule_lu_ma_balance |
| evi_smth_zonglun_003 | "天元羸弱未为灾，地气坚牢足欢乐" | condition | 天干弱地支稳→仍可安泰→地气为重 | 结构稳定 | 高 | ✅ | rule_diqi_jianlao |

**跨体系概念映射层**：

| 概念ID | 共通语义 | 八字对应 | 占星对应 | 梦学对应 | 心理学对应 | 备注 |
|-------|---------|---------|---------|---------|-----------|------|
| concept_foundation_modifier | 根基与修饰 | 五行/禄马 | 本命/过境 | - | 核心/附加 | 层级关系 |
| concept_resource_mobility_balance | 资源动象平衡 | 禄马比例 | 固定/变动 | - | 稳定/变化 | 比例调和 |

<!-- L2.5_END -->

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_03_zonglun_001]` `[trigger: 先论五行] [factor_trigger: 先论五行]` `[role: 主干]` 可见先论五行，后看禄马：五行要生旺，禄马怕衰绝。 → `《三命通会·卷三》#总论禄马`
  - `[ns_smth_03_zonglun_002]` `[trigger: 天元地气] [factor_trigger: 天元地气]` `[role: 主干]` 天元翪弱未为灾，地气坚牢足欢乐。 → `《三命通会·卷三》#总论禄马`
  - `[ns_smth_03_zonglun_003]` `[trigger: 禄多马少] [factor_trigger: bazi_state_factor_115]` `[role: 主干]` 禄多马少，使主神劳；禄少马多，能操善负。 → `《三命通会·卷三》#总论禄马`
  - `[ns_smth_03_zonglun_004]` `[trigger: 禄马贵人] [factor_trigger: 禄马贵人]` `[role: 主干]` 禄马贵人无准托，考究五行之恶。 → `《三命通会·卷三》#总论禄马`
  - `[ns_smth_03_zonglun_005]` `[trigger: 破祖浮劣] [factor_trigger: 破祖浮劣]` `[role: 主干]` 若无吉煖加助时，定知破祖多浮劣。 → `《三命通会·卷三》#总论禄马`

---

## 论天乙贵人

### 1. 天乙贵人本体与尊位

- **原文（source_text）**：
  论天乙贵人。天乙者，乃天上之神，在紫微垣、阊阖门外，与太乙并列，事天皇大帝，下游三辰。家在己丑斗牛之次，出乎己未井鬼之舍，执玉衡较量天人之事，名曰在乙也。其神最尊贵，所至之处，一切凶煞隐然而避。

- **分字分词释义**：
  - **天乙**：居紫微垣近畔、阊阖门外之神，与太乙并列，为天帝左右近臣。
  - **执玉衡**：握天衡以校量天人之事，象征裁量与平衡之权。
  - **所至凶煞隐避**：贵神临处，可压伏众煞，是「辟邪」「解厄」的核心象。

- **规范化释义（primary_lang_explained）**：
  本段先从星辰布局出发，交代天乙贵人的「职位」：在紫微宫附近、阊阖门之外，与太乙齐列，是天皇大帝的近侍大臣，负责执玉衡衡量天道人事。因为其位高权重，所以凡天乙所至之处，各种凶煞多半隐避，不敢正面作祟。因此，天乙贵人在命理中被视为「最尊贵之神」，常用以化解命局中部分凶煞之力。

- **完整对等诠释（secondary_lang_full）**：
  Tianyi Noble is described as a high celestial minister stationed near the Ziwei enclosure and the gate of Changhe, holding the jade balance with which heaven measures human affairs.
  Wherever it resides, harsh stars are said to hide or soften, not because disaster simply disappears but because authority, ethics and institutional support intervene.
  In reading charts it is therefore treated as the most exalted protective star and is mainly used to downgrade the raw intensity of afflictions around it.
- **核心要点**：
  - 天乙贵人的核心作用，是「以德压煞」：贵不在虚名，而在能压制部分凶星的发挥空间。
  - 在结构上，可视为对局中「凶煞强度」的折减因子，但前提是贵人自身要有气、不得落空亡或受重克。
 
- **详细解说**：
  1) 在系统中根据日干预先建立「天乙贵人表」，以日干为索引得到贵人所在地支（可按阳贵/阴贵分别存储基础表）；
   2) 对命局四柱逐一比对：凡地支等于贵位者，标记为天乙所在位置，并记录其所在宫（年、月、日、时）及与用神的关系；
   3) 在特征层，为每一个天乙实例计算「有效度」：综合生旺衰绝、是否空亡、是否被刑冲合害以及是否与主要凶煞同宫等维度，形成 `tianyi_effect_score`；
   4) 在解释层，当某宫位凶煞较重但天乙有效度高时，以「减压」「转危为机」的语气解释；若天乙无气或被重破，则仅保留为背景信息，不主动做过度粉饰。
 
- 反例与边界：
  - 不宜一见天乙便宣称「一切凶煞隐避」，尤其在现实中明显存在高风险职业或事件时，更应将天乙视为减缓因子而非免死金牌；
   - 若贵人落空亡、死绝或与重煞同宫，工程上应显著降低其权重，甚至在某些模型任务中视为无效，而不是机械加分；
   - 不可在没有足够样本支撑的前提下，将「有天乙」直接当作高学历、高职位的强预测因子，应以实际统计验证其相关性；
   - 反向误区是彻底忽略天乙，只看凶煞总量，从而失去对「有道德/制度保护」「有贵人协调」这类缓冲机制的描述能力。
 
- 小例（示意）：
  - 某命局日支见天乙且生旺，同时同宫有七煞，系统可解释为「高压环境下仍有制度与贵人协调」，在风险提示中强调「虽有冲突，但可通过正规渠道化解」；
  - 另一命局虽然年支见天乙，却落空亡且与多重刑冲并见，系统则仅在注脚中保留「有贵人名号」的信息，不据此下乐观结论，以免输出与现实明显不符的吉语。"""
    normalized_text_zh: str = """"""
    subject: str = "禄马贵人与五行先后"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_wuxing_2', 'bazi_semantic', 'bazi_relation_config', 'bazi_semantic', 'bazi_state_factor_115', 'bazi_semantic', 'bazi_state_factor_116', 'bazi_semantic', 'bazi_condition_wuxing_wangshuai', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_禄马贵人与五行先后_001_L1",
    )
    version: str = "1.0.0"
