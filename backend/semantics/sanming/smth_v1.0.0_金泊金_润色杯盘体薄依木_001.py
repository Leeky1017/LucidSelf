"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228774
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
    semantic_id="smth_v1.0.0_金泊金_润色杯盘体薄依木_001",
    book_id="sanming",
    engine_id="bazi"
)
class 金泊金润色杯盘体薄依木(SemanticEntry):
    """
    - **原文（source_text）**：
  壬寅、癸卯金泊金。金泊金者，润色杯盘，增光宫室。打薄须藉乎别金，描彩必假乎水力。此金甚微，非木则无所依。木以平地为上，有此不宜见火。

- **规范化...
    """
    
    original_text: str = """- **原文（source_text）**：
  壬寅、癸卯金泊金。金泊金者，润色杯盘，增光宫室。打薄须藉乎别金，描彩必假乎水力。此金甚微，非木则无所依。木以平地为上，有此不宜见火。

- **规范化释义（primary_lang_explained）**：
  壬寅、癸卯是金泊金。金泊金，是用来装饰杯盘、增光宫室的薄金箔，打薄需要借助其他金，描绘需要水的力量。这种金极为微薄，没有木就无处依附。以平地木最好，有了木就不宜见火。

- **完整对等诠释（secondary_lang_full）**：
  Renyin and Guimao are Gold-Foil Metal. Gold-Foil Metal is for embellishing cups and plates, adding luster to palaces; beating thin requires other metals, painting requires water's force. This metal is extremely thin, without wood has nowhere to attach. Flat-Earth Wood is best; having wood, should not see fire.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_101]` `[trigger: 金泊金]` `[factor_trigger: renyin_guimao AND jinbo_jin]` `[role: 主干]` 金泊金者，润色杯盘，增光宫室。打薄须藉乎别金，描彩必假乎水力。此金甚微，非木则无所依。 → 《三命通会》卷一#金泊金

<!-- L2_BEGIN -->
 - **语义提取（L2）**：
   - **主题**：金泊金纳音的性质与依附条件
   - **自然属性**：
     - 象征：薄金箔、器物表面的装饰光泽
     - 特性：体薄、无根、自身难以独立成器
     - 元素：壬寅癸卯金、平地木、水力辅助
   - **功能象义**：
     - 说明金泊金须依附木质载体方能成器
     - 用于界定金泊金宜木水、不宜重火的取用原则
   - **条件结构**：
     - **成器条件**：柱中有木为基、得水助描绘
     - **失效条件**：无木可依或烈火焚灼则易破败
   - **多层解释**：
     - 字面层：薄金箔贴覆于杯盘宫室表面
     - 象征层：借他物之势而增辉、非独立之贵体
     - 实践层：命局中金泊金需看所依之木与水是否得力
     - 应用层：在取用神时多从木水入手，不以火为先

 - **L2-术语对齐（Term Glossary）**：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|  
| 金泊金 | Gold-Foil Metal | 壬寅癸卯纳音 | Renyin Guimao Nayin | - | new_candidate |
| 平地木 | Flat-Earth Wood | 最适配金泊金 | Best match for Gold-Foil | - | new_candidate |
| 薄金箔 | Thin Gold Leaf | 贴附器物表面之薄金层 | Thin metal layer attached to object surface | - | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| 因子类型 | 因子标签（人话） | 因子ID（如已存在） | 因子来源 | 角色/位置 | 取值/约束 | engine_id | 备注 |
|----------|------------------|--------------------|----------|----------|----------|------|
| 纳音性质类 | 金泊金润色杯盘 | gold_foil_embellish_cups | existing | 性质层 | 壬寅癸卯 | bazi_semantic | 金泊金 |
| 规则类 | 金泊金依木不宜火 | gold_foil_depends_wood_no_fire | existing | 规则层 | 体薄依附 | bazi_semantic | 成器规则 |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 桥接层

**因子关系层**：

| 关系ID | 关系类型 | 因子A | 因子B | 关系性质 | 条件约束 | 效果方向 | source_ref |
|-------|---------|-------|-------|---------|---------|---------|-----------|
| rel_smth_jbj_001 | depend | jinbo | pingdimu | 依木成器 | 体薄无根 | 依附 | 卷一#金泊金 |
| rel_smth_jbj_002 | assist | shui | jinbo | 水助描彩 | 打薄须水 | 辅助 | 卷一#金泊金 |
| rel_smth_jbj_003 | weaken | huo | jinbo | 火克薄金 | 体薄易伤 | 忌 | 卷一#金泊金 |

**推理溯源层**：

| 证据ID | 原文锚点 | 涉及因子 | 推理步骤 | 结论方向 | 置信度 | 可生成规则 | 目标规则ID |
|-------|---------|---------|---------|---------|-------|----------|-----------|
| evi_smth_jbj_001 | "此金甚微非木则无所依" | jinbojin | 体薄→需木→依附成器 | 依附 | 高 | ✅ | rule_jbj |

**跨体系概念映射层**：

| 概念ID | 共通语义 | 八字对应 | 占星对应 | 梦学对应 | 心理学对应 | 备注 |
|-------|---------|---------|---------|---------|-----------|------|
| concept_dependent_beauty | 依附之美 | 金泊金 | 金星相位 | 装饰梦 | 借力成就 | 附属光华 |

<!-- L2.5_END -->

---

### 160. 白镴金：昆山片玉喜火炼

- **原文（source_text）**：
  庚辰、辛巳白镴金。白镴金者，昆山片玉，洛浦遗珍，交栖日月之光，凝聚阴阳之气，形明体洁，乃金之正色也。此金惟喜火炼，须炉中炎火。

- **规范化释义（primary_lang_explained）**：
  庚辰、辛巳是白镴金。白镴金，如昆山的片玉、洛水的遗珍，交融日月之光，凝聚阴阳之气，形体明亮洁净，是金的正色。这种金只喜欢火炼，需要炉中的炎火。

- **完整对等诠释（secondary_lang_full）**：
  Gengchen and Xinsi are White-Wax Metal. White-Wax Metal is like Kunshan jade-shard, Luopu left-treasure, mingling sun-moon light, condensing yin-yang qi, form bright body pure, being metal's true color. This metal only loves fire-refining, requires furnace intense-fire.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_bailajin_001]` `[trigger: 白镒金]` `[factor_trigger: gengchen_xinsi AND baila_jin]` `[role: 主干]` 白镒金者，昆山片玉，洛浦遗珍，交栖日月之光，凝聚阴阳之气，形明体洁，乃金之正色也。 → 《三命通会》卷一#白镒金
  - `[ns_smth_01_bailajin_002]` `[trigger: 喜火炼]` `[factor_trigger: xi_huolian AND luzhong_yanhuo]` `[role: 主干依赖]` 此金惟喜火炼，须炉中炎火。 → 《三命通会》卷一#白镒金
  - `[ns_smth_01_bailajin_003]` `[trigger: 金之正色]` `[factor_trigger: jin_zhengse AND mingti_jiejing]` `[role: 总结]` 形明体洁，乃金之正色也。 → 《三命通会》卷一#白镒金

<!-- L2_BEGIN -->
 - **语义提取（L2）**：
   - **主题**：白镴金的纯正金性与火炼条件
   - **自然属性**：
     - 象征：昆山片玉、洛浦遗珍、明亮金泽
     - 特性：质地纯正、色泽清亮、喜火炼成器
     - 元素：庚辰辛巳金、炉中火、水为辅
   - **功能象义**：
     - 突出白镴金需经烈火淬炼方显其贵
     - 说明火炼过度而无水济则易贫困劳苦
   - **条件结构**：
     - **成器条件**：得炉中火适度锻炼，并有清水调和
     - **失效条件**：无火难成器，火烈无水则燥裂伤身
   - **多层解释**：
     - 字面层：如玉如珍的白色金属，经火炼更显光洁
     - 象征层：经磨炼而成的正色之金，象征清白与正直
     - 实践层：命局见白镴金宜配火水协调，忌土多埋没
     - 应用层：在格局判断中视作经锻炼后可用之财与权力载体

 - **L2-术语对齐（Term Glossary）**：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|  
| 白镴金 | White-Wax Metal | 庚辰辛巳纳音 | Gengchen Xinsi Nayin | - | new_candidate |
| 炉中火 | Furnace Fire | 炼金之火 | Metal-refining fire | - | new_candidate |
| 昆山片玉 | Kunshan Jade Shard | 比喻白镴金之清洁光润 | Metaphor for the purity and luster of White-Wax Metal | - | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| 因子类型 | 因子标签（人话） | 因子ID（如已存在） | 因子来源 | 角色/位置 | 取值/约束 | engine_id | 备注 |
|----------|------------------|--------------------|----------|----------|----------|------|
| 纳音性质类 | 白镴金昆山片玉 | white_wax_kunshan_jade | existing | 性质层 | 庚辰辛巳 | bazi_semantic | 白镴金 |
| 规则类 | 白镴金喜炉中火炼 | white_wax_loves_furnace_fire | existing | 规则层 | 成器需火 | bazi_semantic | 成器规则 |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 桥接层

**因子关系层**：

| 关系ID | 关系类型 | 因子A | 因子B | 关系性质 | 条件约束 | 效果方向 | source_ref |
|-------|---------|-------|-------|---------|---------|---------|-----------|
| rel_smth_blj_001 | refine | luzhonghuo | bailajin | 炉中火炼白镴金 | 喜火炼 | 成器 | 卷一#白镴金 |
| rel_smth_blj_002 | symbol | kunshan | bailajin | 昆山片玉象 | 日月光凝聚 | 纯正 | 卷一#白镴金 |

**推理溯源层**：

| 证据ID | 原文锚点 | 涉及因子 | 推理步骤 | 结论方向 | 置信度 | 可生成规则 | 目标规则ID |
|-------|---------|---------|---------|---------|-------|----------|-----------|
| evi_smth_blj_001 | "此金惟喜火炼须炉中炎火" | bailajin | 白镴金→喜火炼→炉中火 | 成器 | 高 | ✅ | rule_blj |

**跨体系概念映射层**：

| 概念ID | 共通语义 | 八字对应 | 占星对应 | 梦学对应 | 心理学对应 | 备注 |
|-------|---------|---------|---------|---------|-----------|------|
| concept_pure_refinement | 纯正淬炼 | 白镴金火炼 | 太阳金星 | 提纯梦 | 自我完善 | 金之正色 |

<!-- L2.5_END -->

---

### 161. 砂中金：刚形布地淘洗为珍

- **原文（source_text）**：
  甲午、乙未，砂中金。砂中金者，刚形布地，宝质藏砂，直教淘洗为珍，必须因人始贵。此金非炉火则不能制。

- **规范化释义（primary_lang_explained）**：
  甲午、乙未是砂中金。砂中金，刚硬的形态散布在地上，宝贵的质地藏在砂中，需要淘洗才能成为珍宝，必须靠人工才能显贵。这种金非炉火不能制成器。

- **完整对等诠释（secondary_lang_full）**：
  Jiawu and Yiwei are Sand-Center Metal. Sand-Center Metal has firm form spread on earth, treasure quality hidden in sand; requires washing to become gem, must rely on human-effort to be noble. This metal requires furnace-fire to be forged.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_102]` `[trigger: 砂中金]` `[factor_trigger: jiawu_yiwei AND shazhong_jin]` `[role: 主干]` 砂中金者，刚形布地，宝质藏砂，直教淘洗为珍，必须因人始贵。此金非炉火则不能制。 → 《三命通会》卷一#砂中金

<!-- L2_BEGIN -->
 - **语义提取（L2）**：
   - **主题**：砂中金的原矿性质与淘洗成器逻辑
   - **自然属性**：
     - 象征：散布于砂中的金砂、尚未提炼的矿藏
     - 特性：刚而未成器、需人力与火炼方显价值
     - 元素：甲午乙未金、砂土、炉火与清水
   - **功能象义**：
     - 体现砂中金须经历淘洗与锻炼才能成珍
     - 用于说明环境与后天造化对其成败的决定作用
   - **条件结构**：
     - **成器条件**：得炉火冶炼、清水洗涤、环境不再重砂埋没
     - **失效条件**：重逢砂土或火少水乏，则埋没劳苦
   - **多层解释**：
     - 字面层：金质藏于砂中，需淘洗炼制
     - 象征层：先天资质尚好但环境粗糙、需后天打磨
     - 实践层：命局砂中金多者，要看运中火水与出砂之机
     - 应用层：取用时重视去浊留清，避免再叠砂土之象

 - **L2-术语对齐（Term Glossary）**：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|  
| 砂中金 | Sand-Center Metal | 甲午乙未纳音 | Jiawu Yiwei Nayin | - | new_candidate |
| 采精金于黄碛 | Extract Essence-Metal from Yellow-Sand | 从黄沙中提炼精金之贵格 | Noble pattern of extracting fine metal from yellow sand | - | new_candidate |
| 砂土埋金 | Sand-Buried Metal | 砂土过重以致金被埋没 | Excess sand burying and suppressing the metal | - | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| 因子类型 | 因子标签（人话） | 因子ID（如已存在） | 因子来源 | 角色/位置 | 取值/约束 | engine_id | 备注 |
|----------|------------------|--------------------|----------|----------|----------|------|
| 纳音性质类 | 砂中金宝质藏砂 | sand_metal_treasure_in_sand | existing | 性质层 | 甲午乙未 | bazi_semantic | 砂中金 |
| 格局类 | 采精金于黄碛格 | extract_metal_yellow_sand | existing | 格局层 | 甲午己巳 | bazi_semantic | 贵格 |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 桥接层

**因子关系层**：

| 关系ID | 关系类型 | 因子A | 因子B | 关系性质 | 条件约束 | 效果方向 | source_ref |
|-------|---------|-------|-------|---------|---------|---------|-----------|
| rel_smth_szj_001 | refine | luzhonghuo | shazhongjin | 淘洗炼制 | 必须因人 | 成器 | 卷一#砂中金 |
| rel_smth_szj_002 | pattern | jiawu | jisi | 采精金于黄碛 | 甲午己巳 | 贵格 | 卷一#砂中金 |

**推理溯源层**：

| 证据ID | 原文锚点 | 涉及因子 | 推理步骤 | 结论方向 | 置信度 | 可生成规则 | 目标规则ID |
|-------|---------|---------|---------|---------|-------|----------|-----------|
| evi_smth_szj_001 | "刚形布地宝质藏砂淘洗为珍" | shazhongjin | 藏砂→淘洗→成珍 | 成器 | 高 | ✅ | rule_szj |

**跨体系概念映射层**：

| 概念ID | 共通语义 | 八字对应 | 占星对应 | 梦学对应 | 心理学对应 | 备注 |
|-------|---------|---------|---------|---------|-----------|------|
| concept_hidden_potential | 潜藏潜力 | 砂中金 | 冥王星 | 挖掘梦 | 潜能开发 | 待淘洗 |

<!-- L2.5_END -->

---

### 162. 剑锋金：白帝司权刚由百炼

- **原文（source_text）**：
  壬申癸酉剑锋金。剑锋金者，白帝司权，刚由百炼。红光射于斗牛，白刃凝于霜雪。此金造化，非水不能生。

- **规范化释义（primary_lang_explained）**：
  壬申、癸酉是剑锋金。剑锋金，是白帝掌权、经过百炼而成的刚金。红光射向斗牛星宿，白刃凝结着霜雪之气。这种金的造化，非水不能生养。

- **完整对等诠释（secondary_lang_full）**：
  Renshen and Guiyou are Sword-Edge Metal. Sword-Edge Metal: White-Emperor holds authority, hardness from hundred-refinings. Red light shoots to Dipper-Ox stars, white blade condenses frost-snow. This metal's creation requires water to generate.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_jianfeng_001]` `[trigger: 剑锋金]` `[factor_trigger: renshen_guiyou AND jianfeng_jin]` `[role: 主干]` 剑锋金者，白帝司权，刚由百炼。红光射于斗牛，白刃凝于霜雪。 → 《三命通会》卷一#剑锋金
  - `[ns_smth_01_jianfeng_002]` `[trigger: 非水不生]` `[factor_trigger: feishui_busheng AND jinshui_xiangsheng]` `[role: 主干依赖]` 此金造化，非水不能生。 → 《三命通会》卷一#剑锋金
  - `[ns_smth_01_jianfeng_003]` `[trigger: 百炼成钢]` `[factor_trigger: bailian_chenggang AND jue_duanli]` `[role: 总结]` 剑锋经百炼而成，主决断力与删断力。 → 《三命通会》卷一#剑锋金

<!-- L2_BEGIN -->
 - **语义提取（L2）**：
   - **主题**：剑锋金的锐利本性与生养条件
   - **自然属性**：
     - 象征：利剑锋刃、白帝执权、霜雪之气
     - 特性：刚利、决断、需清水润之方不致枯裂
     - 元素：壬申癸酉金、水为生养主力、少火点炼
   - **功能象义**：
     - 体现剑锋金在命局中主决断力与斩断力
     - 说明水润则为良器、火刑过度则为凶器
   - **条件结构**：
     - **成器条件**：得长流水或大海等清水相生
     - **失效条件**：寅巳三刑全、火多而无水救
   - **多层解释**：
     - 字面层：剑锋经百炼而成，非水不生
     - 象征层：权柄与杀伐并存，需要节制
     - 实践层：用在格局中，多为用神则贵、为忌则凶
     - 应用层：结合水火多少判断其为器或为祸

 - **L2-术语对齐（Term Glossary）**：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|  
| 剑锋金 | Sword-Edge Metal | 壬申癸酉纳音 | Renshen Guiyou Nayin | - | new_candidate |
| 剑气冲斗 | Sword-Qi Clashes-Dipper | 剑气上冲斗牛星之贵格 | Noble pattern where sword qi clashes with Dipper stars | - | new_candidate |
| 白帝司权 | White-Emperor Holds Authority | 象征金之尊贵与主杀之权柄 | Symbolizes Metal's nobility and authority over judgment | - | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| 因子类型 | 因子标签（人话） | 因子ID（如已存在） | 因子来源 | 角色/位置 | 取值/约束 | engine_id | 备注 |
|----------|------------------|--------------------|----------|----------|----------|------|
| 纳音性质类 | 剑锋金刚由百炼 | sword_metal_hundred_refined | existing | 性质层 | 壬申癸酉 | bazi_semantic | 剑锋金 |
| 规则类 | 剑锋金非水不生 | sword_metal_requires_water | existing | 规则层 | 生养需水 | bazi_semantic | 成器规则 |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 桥接层

**因子关系层**：

| 关系ID | 关系类型 | 因子A | 因子B | 关系性质 | 条件约束 | 效果方向 | source_ref |
|-------|---------|-------|-------|---------|---------|---------|-----------|
| rel_smth_jfj_001 | generate | shui | jianfengjin | 非水不生 | 清水润剑 | 生养 | 卷一#剑锋金 |
| rel_smth_jfj_002 | symbol | baidi | jianfengjin | 白帝司权 | 刚由百炼 | 决断 | 卷一#剑锋金 |
| rel_smth_jfj_003 | pattern | jianchong | douniu | 剑气冲斗 | 红光射斗牛 | 贵格 | 卷一#剑锋金 |

**推理溯源层**：

| 证据ID | 原文锚点 | 涉及因子 | 推理步骤 | 结论方向 | 置信度 | 可生成规则 | 目标规则ID |
|-------|---------|---------|---------|---------|-------|----------|-----------|
| evi_smth_jfj_001 | "此金造化非水不能生" | jianfengjin | 剑锋金→需水→生养 | 成器 | 高 | ✅ | rule_jfj |

**跨体系概念映射层**：

| 概念ID | 共通语义 | 八字对应 | 占星对应 | 梦学对应 | 心理学对应 | 备注 |
|-------|---------|---------|---------|---------|-----------|------|
| concept_decisive_power | 决断之力 | 剑锋金 | 火星金星 | 利器梦 | 决策力 | 百炼成钢 |

<!-- L2.5_END -->

---

### 163. 钗钏金：美容首饰惟宜静水

- **原文（source_text）**：
  庚戌辛亥钗钏金。钗钏金者，美容首饰，增光腻肌，猥红倚翠之珍，枕玉眠香之宝。此金藏之闺阁，惟宜静水。

- **规范化释义（primary_lang_explained）**：
  庚戌、辛亥是钗钏金。钗钏金，是美化容貌的首饰，增添光彩使肌肤细腻，红颜翠羽的珍宝，枕玉眠香的宝物。这种金藏在闺阁之中，只宜见清静之水。

- **完整对等诠释（secondary_lang_full）**：
  Gengxu and Xinhai are Hairpin-Bracelet Metal. Hairpin-Bracelet Metal: beautifying ornament, adding luster to delicate skin, rouge-red jade-green treasure, pillow-jade sleep-fragrance jewel. This metal hidden in boudoir, only suitable for still-water.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_103]` `[trigger: 钗钏金]` `[factor_trigger: gengxu_xinhai AND chaichuan_jin]` `[role: 主干]` 钗钏金者，美容首饰，增光腻肌，猥红倚翠之珍，枕玉眠香之宝。此金藏之闺阁，惟宜静水。 → 《三命通会》卷一#钗钏金

<!-- L2_BEGIN -->
 - **语义提取（L2）**：
   - **主题**：钗钏金的首饰属性与用水之道
   - **自然属性**：
     - 象征：钗环手镯、闺阁珍宝、肌肤光泽
     - 特性：重在装饰与润色，喜静水而忌泛滥
     - 元素：庚戌辛亥金、井泉溪涧等清水
   - **功能象义**：
     - 强调钗钏金在命局中偏向富贵享受与审美
     - 说明金白水清时为佳格，水浊或火烈则伤其美
   - **条件结构**：
     - **成器条件**：有静水滋润而不泛、火不过旺
     - **失效条件**：泛海水漂荡或火局太炎
   - **多层解释**：
     - 字面层：首饰金藏于闺阁，遇清水增辉
     - 象征层：富贵闲雅之象，多主享乐与品味
     - 实践层：命局多钗钏金者，行运得水火调匀则吉
     - 应用层：用于区分同为金命而偏重生活质量的一类

 - **L2-术语对齐（Term Glossary）**：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|  
| 钗钏金 | Hairpin-Bracelet Metal | 庚戌辛亥纳音 | Gengxu Xinhai Nayin | - | new_candidate |
| 金白水清 | Metal-White Water-Clear | 金色洁白水质清澈之佳格 | Noble pattern where metal is bright and water clear | - | new_candidate |
| 闺阁 | Boudoir | 藏放首饰的内室，象征隐秘享受 | Inner chamber storing ornaments, symbolizing private enjoyment | - | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| 因子类型 | 因子标签（人话） | 因子ID（如已存在） | 因子来源 | 角色/位置 | 取值/约束 | engine_id | 备注 |
|----------|------------------|--------------------|----------|----------|----------|------|
| 纳音性质类 | 钗钏金美容首饰 | hairpin_metal_beauty_ornament | existing | 性质层 | 庚戌辛亥 | bazi_semantic | 钗钏金 |
| 规则类 | 钗钏金宜静水 | hairpin_metal_suitable_still_water | existing | 规则层 | 喜静恶动 | bazi_semantic | 成器规则 |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 桥接层

**因子关系层**：

| 关系ID | 关系类型 | 因子A | 因子B | 关系性质 | 条件约束 | 效果方向 | source_ref |
|-------|---------|-------|-------|---------|---------|---------|-----------|
| rel_smth_ccj_001 | enhance | jingshui | chaichuanjin | 静水增辉 | 惟宜静水 | 吉 | 卷一#钗钏金 |
| rel_smth_ccj_002 | symbol | guige | chaichuanjin | 闺阁藏珍 | 美容首饰 | 享受 | 卷一#钗钏金 |

**推理溯源层**：

| 证据ID | 原文锚点 | 涉及因子 | 推理步骤 | 结论方向 | 置信度 | 可生成规则 | 目标规则ID |
|-------|---------|---------|---------|---------|-------|----------|-----------|
| evi_smth_ccj_001 | "此金藏之闺阁惟宜静水" | chaichuanjin | 闺阁→静水→増辉 | 吉 | 高 | ✅ | rule_ccj |

**跨体系概念映射层**：

| 概念ID | 共通语义 | 八字对应 | 占星对应 | 梦学对应 | 心理学对应 | 备注 |
|-------|---------|---------|---------|---------|-----------|------|
| concept_aesthetic_enjoyment | 审美享受 | 钗钏金 | 金星二宫 | 饰品梦 | 自我表达 | 闺阁珍宝 |

<!-- L2.5_END -->

---

### 164. 霹雳火：电掣金蛇须资风水雷

- **原文（source_text）**：
  戊子己丑霹雳火。霹雳火者，一缕毫光，九天号令，电掣金蛇之势，云驱铁马之奔。此火须资风水雷，方为变化。

- **规范化释义（primary_lang_explained）**：
  戊子、己丑是霹雳火。霹雳火，是一缕毫光、九天号令，电闪如金蛇之势，云卷如铁马奔驰。这种火需要借助风水雷，才能产生变化。

- **完整对等诠释（secondary_lang_full）**：
  Wuzi and Jichou are Thunder-Bolt Fire. Thunder-Bolt Fire: one ray brilliant-light, nine-heavens command, lightning-flash golden-snake momentum, cloud-drive iron-horse gallop. This fire requires wind-water-thunder to transform.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_pili_001]` `[trigger: 霹雳火]` `[factor_trigger: wuzi_jichou AND pili_huo]` `[role: 主干]` 霹雳火者，一缕毫光，九天号令，电掣金蛇之势，云驱铁马之奔。 → 《三命通会》卷一#霹雳火
  - `[ns_smth_01_pili_002]` `[trigger: 须资风水雷]` `[factor_trigger: xuzi_fengshuilei AND bianhua]` `[role: 主干依赖]` 此火须资风水雷，方为变化。 → 《三命通会》卷一#霹雳火
  - `[ns_smth_01_pili_003]` `[trigger: 电掣金蛇]` `[factor_trigger: dianche_jinshe AND tufa_zhenhan]` `[role: 总结]` 电掣金蛇之势，云驱铁马之奔，象征突发性的变化与震撼。 → 《三命通会》卷一#霹雳火

<!-- L2_BEGIN -->
 - **语义提取（L2）**：
   - **主题**：霹雳火的爆发性与风水雷配合
   - **自然属性**：
     - 象征：电掣金蛇、风雷骤起、暴雨倾盆
     - 特性：来去迅疾、声势猛烈、需配合水风方吉
     - 元素：戊子己丑火、风木、各类水源
   - **功能象义**：
     - 表示突发性的变化与启示，含灵动与惊扰双面
     - 在既济格中与天河水相配，为显贵之象
   - **条件结构**：
     - **成器条件**：同时得风、水、雷三者相资
     - **失效条件**：火燥无水或木风不济则仅为扰动
   - **多层解释**：
     - 字面层：霹雳伴随风雨而发
     - 象征层：剧烈转折、顿悟与震动
     - 实践层：命局见霹雳火，要看是否有水风配合
     - 应用层：用在判断突发机遇或灾祸的象意背景

 - **L2-术语对齐（Term Glossary）**：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|  
| 霹雳火 | Thunder-Bolt Fire | 戊子己丑纳音 | Wuzi Jichou Nayin | - | new_candidate |
| 烈风雷雨格 | Fierce-Wind Thunder-Rain | 霹雳火得风雨相资之贵格 | Noble pattern where thunder-bolt fire is aided by wind and rain | - | new_candidate |
| 九天号令 | Command of Nine Heavens | 霹雳火自天而下之威势 | The heavenly authority embodied in thunder-bolt fire | - | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| 因子类型 | 因子标签（人话） | 因子ID（如已存在） | 因子来源 | 角色/位置 | 取值/约束 | engine_id | 备注 |
|----------|------------------|--------------------|----------|----------|----------|------|
| 纳音性质类 | 霹雳火电掣金蛇 | thunderbolt_fire_lightning_snake | existing | 性质层 | 戊子己丑 | bazi_semantic | 霹雳火 |
| 规则类 | 霹雳火须资风水雷 | thunderbolt_requires_wind_water_thunder | existing | 规则层 | 变化需风水雷 | bazi_semantic | 成器规则 |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 桥接层

**因子关系层**：

| 关系ID | 关系类型 | 因子A | 因子B | 关系性质 | 条件约束 | 效果方向 | source_ref |
|-------|---------|-------|-------|---------|---------|---------|-----------|
| rel_smth_plh_001 | assist | fengshuilei | pilihuo | 风水雷相资 | 须资风水雷 | 变化 | 卷一#霹雳火 |
| rel_smth_plh_002 | symbol | jiutian | pilihuo | 九天号令 | 电掣金蛇 | 威势 | 卷一#霹雳火 |

**推理溯源层**：

| 证据ID | 原文锚点 | 涉及因子 | 推理步骤 | 结论方向 | 置信度 | 可生成规则 | 目标规则ID |
|-------|---------|---------|---------|---------|-------|----------|-----------|
| evi_smth_plh_001 | "此火须资风水雷方为变化" | pilihuo | 霹雳火→风水雷→变化 | 成器 | 高 | ✅ | rule_plh |

**跨体系概念映射层**：

| 概念ID | 共通语义 | 八字对应 | 占星对应 | 梦学对应 | 心理学对应 | 备注 |
|-------|---------|---------|---------|---------|-----------|------|
| concept_sudden_transformation | 骤变 | 霹雳火 | 天王星 | 雷电梦 | 顿悟 | 突发变化 |

<!-- L2.5_END -->

---

### 165. 炉中火：天地为炉阴阳为炭

- **原文（source_text）**：
  丙寅、丁卯炉中火。炉中火者，天地为炉，阴阳为炭，腾光辉于宇宙，成陶冶于乾坤。此火炎上，喜得木生，惟平地之木为上。

- **规范化释义（primary_lang_explained）**：
  丙寅、丁卯是炉中火。炉中火，以天地为炉、阴阳为炭，光辉腾耀于宇宙，陶冶万物于乾坤。这种火性炎上，喜欢得到木生，以平地木最好。

- **完整对等诠释（secondary_lang_full）**：
  Bingyin and Dingmao are Furnace-Center Fire. Furnace-Center Fire: heaven-earth as furnace, yin-yang as charcoal, radiating brilliance to universe, forging-refining in cosmos. This fire flames upward, loves wood-generation, Flat-Earth Wood best.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_104]` `[trigger: 炉中火]` `[factor_trigger: bingyin_dingmao AND luzhong_huo]` `[role: 主干]` 炉中火者，天地为炉，阴阳为炭，腾光辉于宇宙，成陶冶于乾坤。此火炎上，喜得木生，惟平地之木为上。 → 《三命通会》卷一#炉中火

<!-- L2_BEGIN -->
 - **语义提取（L2）**：
   - **主题**：炉中火的陶冶功能与木火关系
   - **自然属性**：
     - 象征：天地为炉、阴阳为炭、冶炼之火
     - 特性：火势集中、持续燃烧、须木为薪
     - 元素：丙寅丁卯火、平地木、水为调剂
   - **功能象义**：
     - 体现炉中火在命局中主教化、锻炼与成材
     - 说明得木则旺而可用、无木则虚炎而凶
   - **条件结构**：
     - **成器条件**：有适量之木为薪，兼得水以调和
     - **失效条件**：缺木或火势太盛而无水制
   - **多层解释**：
     - 字面层：炉火以木为炭，久燃不熄
     - 象征层：通过磨炼使人事物成熟
     - 实践层：用作命局中学习、技艺锻炼之象
     - 应用层：判断某人是否经得住考验并终成器

 - **L2-术语对齐（Term Glossary）**：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|  
| 炉中火 | Furnace-Center Fire | 丙寅丁卯纳音 | Bingyin Dingmao Nayin | - | new_candidate |
| 天地为炉 | Heaven-Earth as Furnace | 象征陶冶之力 | Symbolizes forging power | - | new_candidate |
| 阴阳为炭 | Yin-Yang as Charcoal | 以阴阳之气为炉火之材 | Yin and Yang as the fuel of furnace fire | - | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| 因子类型 | 因子标签（人话） | 因子ID（如已存在） | 因子来源 | 角色/位置 | 取值/约束 | engine_id | 备注 |
|----------|------------------|--------------------|----------|----------|----------|------|
| 纳音性质类 | 炉中火天地为炉 | furnace_fire_heaven_earth_furnace | existing | 性质层 | 丙寅丁卯 | bazi_semantic | 炉中火 |
| 规则类 | 炉中火喜木生 | furnace_fire_loves_wood_generation | existing | 规则层 | 喜平地木 | bazi_semantic | 成器规则 |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 桥接层

**因子关系层**：

| 关系ID | 关系类型 | 因子A | 因子B | 关系性质 | 条件约束 | 效果方向 | source_ref |
|-------|---------|-------|-------|---------|---------|---------|-----------|
| rel_smth_lzh_001 | generate | pingdimu | luzhonghuo | 木生火 | 喜平地木 | 生旺 | 卷一#炉中火 |
| rel_smth_lzh_002 | symbol | tiandiweilu | luzhonghuo | 天地为炉 | 阴阳为炭 | 陶冶 | 卷一#炉中火 |

**推理溯源层**：

| 证据ID | 原文锚点 | 涉及因子 | 推理步骤 | 结论方向 | 置信度 | 可生成规则 | 目标规则ID |
|-------|---------|---------|---------|---------|-------|----------|-----------|
| evi_smth_lzh_001 | "此火炎上喜得木生" | luzhonghuo | 炉中火→木生→炎上 | 生旺 | 高 | ✅ | rule_lzh |

**跨体系概念映射层**：

| 概念ID | 共通语义 | 八字对应 | 占星对应 | 梦学对应 | 心理学对应 | 备注 |
|-------|---------|---------|---------|---------|-----------|------|
| concept_forging_refinement | 锦炼成器 | 炉中火 | 火星太阳 | 炼金梦 | 自我磨练 | 陶冶乾坤 |

<!-- L2.5_END -->

---

### 166. 覆灯火：金盏衔光玉台吐艳

- **原文（source_text）**：
  甲辰乙巳覆灯火。覆灯火者，金盏衔光，玉台吐艳，照日月不照之处，明天地未明之时。此火乃人间夜明之火，以木为心，以水为油，遇阴则吉，遇阳则不利。

- **规范化释义（primary_lang_explained）**：
  甲辰、乙巳是覆灯火。覆灯火，金盏托着光芒、玉台吐出光艳，照亮日月照不到的地方，点明天地未明的时刻。这种火是人间夜晚的明火，以木为灯芯，以水为灯油，遇阴则吉，遇阳则不利。

- **完整对等诠释（secondary_lang_full）**：
  Jiachen and Yisi are Covered-Lamp Fire. Covered-Lamp Fire: gold-dish holds light, jade-platform emits brilliance, illuminating where sun-moon cannot, brightening when heaven-earth unlit. This fire is human-realm night-light, wood as wick, water as oil; meeting yin auspicious, meeting yang unfavorable.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_fudeng_001]` `[trigger: 覆灯火]` `[factor_trigger: jiachen_yisi AND fudeng_huo]` `[role: 主干]` 覆灯火者，金盏衔光，玉台吐艳，照日月不照之处，明天地未明之时。 → 《三命通会》卷一#覆灯火
  - `[ns_smth_01_fudeng_002]` `[trigger: 以木为心]` `[factor_trigger: yimu_weixin AND yishui_weiyou]` `[role: 主干依赖]` 此火乃人间夜明之火，以木为心，以水为油。 → 《三命通会》卷一#覆灯火
  - `[ns_smth_01_fudeng_003]` `[trigger: 遇阴则吉]` `[factor_trigger: yuyin_zeji AND yuyang_zebuli]` `[role: 总结]` 遇阴则吉，遇阳则不利，在困暗环境中提供指引与温暖。 → 《三命通会》卷一#覆灯火

<!-- L2_BEGIN -->
 - **语义提取（L2）**：
   - **主题**：覆灯火的夜明性质与阴阳环境
   - **自然属性**：
     - 象征：金盏、玉台、暗室之灯
     - 特性：光力有限但能照幽暗，喜阴不喜烈阳
     - 元素：甲辰乙巳火、木芯、水油
   - **功能象义**：
     - 表示在困暗环境中提供指引与温暖
     - 说明需不断添油加木方可长久明照
   - **条件结构**：
     - **成器条件**：有木为芯、水为油、环境偏阴
     - **失效条件**：风大翻覆或阳火太盛将其吹灭
   - **多层解释**：
     - 字面层：覆灯借油木而燃，照人不照天
     - 象征层：小范围的庇护与启蒙
     - 实践层：命局覆灯火多者，宜稳中求进、忌躁烈
     - 应用层：用于分析微弱但持续的助力来源

 - **L2-术语对齐（Term Glossary）**：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|  
| 覆灯火 | Covered-Lamp Fire | 甲辰乙巳纳音 | Jiachen Yisi Nayin | - | new_candidate |
| 暗灯添油格 | Dark-Lamp Add-Oil | 在暗处添油使灯长明之贵格 | Noble pattern of sustaining lamp-light by adding oil in darkness | - | new_candidate |
| 金盏玉台 | Golden Cup and Jade Stand | 承托灯火之器物，象征精致载体 | Vessels supporting the lamp, symbolizing refined carriers | - | new_candidate |
| 规则类 | 覆灯火以木为心水为油 | lamp_fire_wood_wick_water_oil | new_candidate | 规则层 | 木水相资 | bazi_semantic | 成器规则 |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 桥接层

**因子关系层**：

| 关系ID | 关系类型 | 因子A | 因子B | 关系性质 | 条件约束 | 效果方向 | source_ref |
|-------|---------|-------|-------|---------|---------|---------|-----------|
| rel_smth_fdh_001 | fuel | mu | fudenghuo | 木为灯心 | 以木为心 | 燃烧 | 卷一#覆灯火 |
| rel_smth_fdh_002 | fuel | shui | fudenghuo | 水为灯油 | 以水为油 | 润燃 | 卷一#覆灯火 |
| rel_smth_fdh_003 | condition | yin | fudenghuo | 遇阴则吉 | 照幽暗 | 吉 | 卷一#覆灯火 |

**推理溯源层**：

| 证据ID | 原文锚点 | 涉及因子 | 推理步骤 | 结论方向 | 置信度 | 可生成规则 | 目标规则ID |
|-------|---------|---------|---------|---------|-------|----------|-----------|
| evi_smth_fdh_001 | "此火乃人间夜明之火以木为心以水为油" | fudenghuo | 灯火→木心水油→夜明 | 照幽 | 高 | ✅ | rule_fdh |

**跨体系概念映射层**：

| 概念ID | 共通语义 | 八字对应 | 占星对应 | 梦学对应 | 心理学对应 | 备注 |
|-------|---------|---------|---------|---------|-----------|------|
| concept_guiding_light | 引导之光 | 覆灯火 | 月亮十二宫 | 灯火梦 | 内在指引 | 照日月不照之处 |

<!-- L2.5_END -->

---

### 167. 天上火：温暖山河辉光宇宙

- **原文（source_text）**：
  戊午、己未，天上火。天上火者，温暖山河，辉光宇宙，阳德丽天之照，阴精离海之明。戊午为太阳则刚，己未为太阴则柔。

- **规范化释义（primary_lang_explained）**：
  戊午、己未是天上火。天上火，温暖山河，辉耀宇宙，是阳德丽天的照耀，是阴精离海的光明。戊午为太阳则刚健，己未为太阴则柔和。

- **完整对等诠释（secondary_lang_full）**：
  Wuwu and Jiwei are Sky-Above Fire. Sky-Above Fire: warming mountains-rivers, illuminating universe, yang-virtue heaven-adorning radiance, yin-essence departing-sea brightness. Wuwu as sun is firm, Jiwei as moon is soft.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_105]` `[trigger: 天上火]` `[factor_trigger: wuwu_jiwei AND tianshang_huo]` `[role: 主干]` 天上火者，温暖山河，辉光宇宙，阳德丽天之照，阴精离海之明。戊午为太阳则刚，己未为太阴则柔。 → 《三命通会》卷一#天上火

<!-- L2_BEGIN -->
 - **语义提取（L2）**：
   - **主题**：天上火的日月光辉与温煦特质
   - **自然属性**：
     - 象征：日光、月华、普照山河之火
     - 特性：光大而不局部，刚柔并济，有温暖与干燥两面
     - 元素：戊午太阳火、己未太阴火、配合戌亥天门
   - **功能象义**：
     - 表示外在名声与光环，也主照拂众生
     - 说明格局得位时主贵显，不得位时反有灼伤之虞
   - **条件结构**：
     - **成器条件**：得戌亥为天门、卯酉为出入之门，水木相资
     - **失效条件**：水盛损明或土重壅遏光辉
   - **多层解释**：
     - 字面层：天上火温暖山河、辉光宇宙
     - 象征层：君王之明、权势之耀
     - 实践层：命局天上火旺而得门户配置，则主科名显达
     - 应用层：用于判断一个格局是普照众人还是灼人自焚

 - **L2-术语对齐（Term Glossary）**：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|  
| 天上火 | Sky-Above Fire | 戊午己未纳音 | Wuwu Jiwei Nayin | - | new_candidate |
| 日月分秀格 | Sun-Moon Divide-Excellence | 日月各得其位之贵格 | Noble pattern where sun and moon each gain distinguished position | - | new_candidate |
| 阳德丽天 | Yang-Virtue Adorning-Heaven | 天上火所代表的阳刚光明之德 | The bright yang virtue represented by sky fire | - | new_candidate |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| 因子类型 | 因子标签（人话） | 因子ID（如已存在） | 因子来源 | 角色/位置 | 取值/约束 | engine_id | 备注 |
|----------|------------------|--------------------|----------|----------|----------|------|
| 纳音性质类 | 天上火温暖山河 | sky_fire_warming_mountains_rivers | existing | 性质层 | 戊午己未 | bazi_semantic | 天上火 |
| 规则类 | 天上火太阳刚太阴柔 | sky_fire_sun_firm_moon_soft | existing | 规则层 | 刚柔并济 | bazi_semantic | 阴阳特性 |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 桥接层

**因子关系层**：

| 关系ID | 关系类型 | 因子A | 因子B | 关系性质 | 条件约束 | 效果方向 | source_ref |
|-------|---------|-------|-------|---------|---------|---------|-----------|
| rel_smth_tsh_001 | radiate | taiyang | tianshanghuo | 太阳普照 | 戊午刚 | 温暖 | 卷一#天上火 |
| rel_smth_tsh_002 | radiate | taiyin | tianshanghuo | 太阴柔照 | 己未柔 | 润泽 | 卷一#天上火 |

**推理溯源层**：

| 证据ID | 原文锚点 | 涉及因子 | 推理步骤 | 结论方向 | 置信度 | 可生成规则 | 目标规则ID |
|-------|---------|---------|---------|---------|-------|----------|-----------|
| evi_smth_tsh_001 | "温暖山河辉光宇宙" | tianshanghuo | 天上火→温暖→普照 | 威仪 | 高 | ✅ | rule_tsh |

**跨体系概念映射层**：

| 概念ID | 共通语义 | 八字对应 | 占星对应 | 梦学对应 | 心理学对应 | 备注 |
|-------|---------|---------|---------|---------|-----------|------|
| concept_universal_illumination | 普照 | 天上火 | 太阳 | 光明梦 | 自我实现 | 辉光宇宙 |

<!-- L2.5_END -->

---

### 168. 山下火：萤火照水与风木增辉

- **原文（source_text）**：
  丙申丁酉山下火。山下火者，草间熠燿，花𫟚荧煌，寒林缀叶之光，隔幔点衣之彩。方朔以萤火名之，故妙选有萤火照水格，遇秋生则贵为卿监，是以此火喜水，地支逢亥子，或纳音水，更遇申酉月是也。或以山下之火最喜木与山，更得风来增辉为贵，又不以荧火论矣。大林木有辰巳为风，桑柘木有癸丑为山，松柏平地最吉，更得风助主贵。若风多吹散，王夭。水爱井泉涧下，有水相资，主爵位崇显。大海水不宜，然有山亦应贵格。寅卯为东方木旺火生之地，只甲寅水吉。乙卯为震，有风见之不佳，若无火无山，更加霹火，主夭。天上水为骤雨，此火不宜相见，若先得山水滋助，亦无大害。

- **规范化释义（primary_lang_explained）**：
  丙申、丁酉为山下火。山下火像草间的萤光、花间的荧煌，是在山脚、林间闪烁的小火光，能点亮暗处的衣物与树叶。妙选称之为"萤火照水格"，秋生而又见亥子或纳音属水，更逢申酉月，则小火得水相映而贵，可至卿监。此火最喜有山、有木，又有风来助，便不只是萤火，而成山脚映照之光：大林木配辰巳为风、桑柘木配癸丑为山、松柏和平地木为根基，风来则增辉，但风多易吹散，反主夭折。水以井泉、涧下等清水最吉，大海水本不宜，若有山作依托，犹可成贵格。寅卯为东方木旺火生之地，其中甲寅见水为吉，乙卯属震有风，若风大而又无山火为依，则加上霹雳火反主夭亡。天上水如骤雨，直对山下火多有损伤，除非先有山水滋助方不为大害。

- **完整对等诠释（secondary_lang_full）**：
  Bingshen and Dingyou belong to Hillside-Beneath Fire. This Fire resembles the glow of fireflies among grass and the flicker of blossoms—glimmer on cold forest leaves, color upon garments behind curtains. Dongfang Shuo likened it to firefly light; therefore Wonderful-Selection names the pattern "Fireflies-Illuminating-Water"—if born in autumn and encountering Hai or Zi branches or Water Nayin, further meeting Shen-You months, then this small Fire, reflected by Water, attains rank up to censorial offices. This Fire delights most in having mountains and Wood, with wind to enhance its brilliance: Great-Forest Wood with Chen-Si as wind, Mulberry-Zelkova Wood with Guichou as mountain, Pine-Cypress and Flat-Earth Wood as rooting; when wind assists, nobility arises, yet excess wind scatters the flame and brings early death. Water prefers well and stream water, where support from Water grants high office and honor. Ocean-Water is generally unsuitable; yet with mountains as backing it may still form noble patterns. Yin-Mao mark the eastern Wood-prosperous Fire-generating region; Jia-Yin encountering Water is auspicious. Yi-Mao corresponds to Zhen (Thunder); with strong wind but without mountain or Fire to rely on, then adding Thunder-Bolt Fire leads to fatality. Heavenly River Water manifests as sudden rain; such Water should not directly meet Hillside-Beneath Fire, unless mountain and water nourishment are already present, in which case no great harm ensues.

- **核心要点**：
  - 山下火为萤火之象，小而灵动，喜水喜风木
  - 井泉涧下清水相资，可成"萤火照水"贵格
  - 需山与木作根基，风可增辉，风多则吹散致夭
  - 忌骤雨天河水、大海水直冲，须先得山水护持

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_106]` `[trigger: 山下火]` `[factor_trigger: bingshen_dingyou AND shanxia_huo]` `[role: 主干]` 山下火者，草间熠燿，花𫟚荧煌，寒林缀叶之光，隔幔点衣之彩。方朔以萤火名之，故妙选有萤火照水格。 → 《三命通会》卷一#山下火

- **详细解说**：
  本条将丙申丁酉山下火形容为草间萤光，强调其光力有限却能点亮幽暗，因此取象为"萤火"。命理上，小火若要成格，必须倚赖山与木为体，再得风与水为用：山与木提供依托与燃料，风令火势摇曳生姿，水则形成"萤火照水"的对映之美，由此才有卿监之贵。若只有风而无山水，则风多吹散，反成飘摇不定、短寿之兆；若遇骤雨天河水或大海水，则小火被浇熄。因而山下火的吉凶，全看是否具备山、木、风、水四者的协调布局。

- **校勘与字词辨析（双语）**：
  - **中文**："山下火"为六十甲子纳音之一，古注多以萤火喻之；"萤火照水"为妙选中专名格局，指小火映水而成贵象。
  - **English**: "Hillside-Beneath Fire" is one of the sixty Jiazi Nayin, traditionally compared to fireflies. The pattern "Fireflies-Illuminating-Water" in Wonderful-Selection refers to small fire reflecting on water, forming a noble configuration."""
    normalized_text_zh: str = """"""
    subject: str = "金泊金：润色杯盘体薄依木"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_金泊金_润色杯盘体薄依木_001_L1",
    )
    version: str = "1.0.0"
