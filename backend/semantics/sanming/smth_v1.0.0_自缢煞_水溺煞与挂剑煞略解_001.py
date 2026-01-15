"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101590
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
    semantic_id="smth_v1.0.0_自缢煞_水溺煞与挂剑煞略解_001",
    book_id="sanming",
    engine_id="bazi"
)
class 自缢煞水溺煞与挂剑煞略解(SemanticEntry):
    """
    - **原文（source_text）**：
  自缢煞。此煞取五行反系处，如戌人巳，巳人戌，辰人亥，亥人辰，寅人未，未人寅，卯人申，申人卯，午人丑，丑人午，子人酉，酉人子是也。大忌相克，天元是墓，更...
    """
    
    original_text: str = """- **原文（source_text）**：
  自缢煞。此煞取五行反系处，如戌人巳，巳人戌，辰人亥，亥人辰，寅人未，未人寅，卯人申，申人卯，午人丑，丑人午，子人酉，酉人子是也。大忌相克，天元是墓，更有天中、官符、大耗者，定凶。水溺煞。此煞取丙子、癸未、癸丑上带咸池、金刃、羊刃，盖丙子纳音水，又子为水旺之地，未为井宿之居，丑为三河之分，更纳音克身，决不可免。古歌云：「动煞克身名颠坠，金神羊刃防同位。要知自缢最凶神，戌巳辰亥并寅未，子酉一例为凶煞，卯申丑未依前是。大忌空亡兼墓鬼，官符大耗仍须避。丙子癸未并癸丑，咸池金煞羊刃畏。五行若更来克身，一死悬梁一溺水。」挂剑煞。此煞取巳酉丑申四柱纯全者是，或重带巳酉丑亦是，更犯官符、元辰、白虎、金神等类，五行刑克本命者，主凶暴杀人，或反为人所杀。诗曰：「巳酉丑申金气全，从革局多名挂剑。元亡金虎并克身，纵不杀人身岂免。」

- **分字分词释义**：
  - **自缢煞、水溺煞**：分别对应自缢与溺水等极端身亡之象，多在特定干支与凶煞重叠时应验。
  - **挂剑煞**：以巳酉丑申金气纯全为象，多主极端暴力或被暴力所及的风险。
  - **大忌相克、兼墓鬼、大耗等**：强调只有在多重不利结构叠加时，这些小煞才显示出极凶之力。

- **规范化释义（primary_lang_explained）**：
  自缢煞、水溺煞与挂剑煞均属极端凶煞，多涉及身体刑伤与意外。自缢煞取五行反系之位（如戌见巳、巳见戌），象征气机反悖，若再见官符、大耗、墓绝，主自缢或勒死。水溺煞取丙子、癸未、癸丑等纳音水旺或水墓之位，叠见咸池（桃花）、羊刃、金神，主溺水或投河。挂剑煞专指巳酉丑申金局全，又见白虎、元辰等凶星，象征兵器极盛，主凶暴杀人或被杀。这些煞的共同点是：单一出现未必致死，必须多重凶煞叠加且五行严重失衡（如克身、死绝）方应验。

- **次语种完整诠释（secondary_lang_full）**：
  Suicide Sha (Zi Yi), Drowning Sha (Shui Ni), and Hanging Sword Sha (Gua Jian) are extreme malefic stars associated with physical injury and accidental death. Suicide Sha is derived from the "reverse link" of five elements (e.g., Xu seeing Si), symbolizing conflicting qi; when combined with Officer Seal (Guan Fu) or Great Drain (Da Hao), it indicates hanging or strangulation. Drowning Sha involves water-heavy pillars like Bing Zi or Gui Wei meeting Peach Blossom or Goat Blade, indicating risk of drowning. Hanging Sword Sha refers to a complete Metal bureau (Si-You-Chou-Shen) meeting White Tiger, symbolizing extreme violence or weapon injury. The text emphasizes that these only manifest when multiple malefics overlap and the Five Elements are severely unbalanced.

- **核心要点**：
  - 自缢煞：五行反系 + 凶煞叠加
  - 水溺煞：水旺/水墓 + 桃花/羊刃
  - 挂剑煞：全金局 + 白虎/元辰
  - 共同条件：多重叠见 + 五行无救

- **详细解说**：
  此类神煞属于“高风险特例”，在普通命局中不轻易取用，仅在特定结构下生效。自缢煞关注的是“气机反悖与自我束缚”，水溺煞关注的是“情绪/欲望（桃花）与环境（水）的失控”，挂剑煞关注的是“金气过刚导致的物理伤害”。在现代应用中，它们更多作为“意外风险”或“心理危机”的预警信号，而非字面上的死法。

- **语义提取（L2）**：
  - **主题**：极端物理伤害与意外风险标记
  - **自然属性**：象征绳索（自缢）、深渊（水溺）、兵器（挂剑）；特性凶暴、极刑、横死；元素五行反系、水旺、金全
  - **功能象义**：为命局提供「高危风险」标签；区分自伤与外伤；强调多重叠加
  - **条件结构**：必要条件特定干支组合；增强条件见官符/大耗/白虎/羊刃；失效条件吉神解救、五行有气
  - **多层解释**：字面层自杀溺水刀伤；象征层自我困局/情绪淹没/冲突升级；实践层提示建模心理危机干预与高危环境规避；心理层鼓励识别毁灭冲动

- **L2-术语对齐（Term Glossary）**：
| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---|---|---|---|
| 自缢煞 | Suicide Sha (Zi Yi) | 五行反系主自缢或勒死 | Five Elements Reverse Link, indicates hanging or strangulation | - | new_candidate |
| 水溺煞 | Drowning Sha (Shui Ni) | 水旺遇桃花羊刃主溺水 | Water prosperity meets Peach Blossom/Goat Blade, indicates drowning | - | new_candidate |
| 挂剑煞 | Hanging Sword Sha (Gua Jian) | 金局全见白虎主凶暴杀伤 | Complete Metal Bureau meets White Tiger, indicates violent injury | - | new_candidate |
| 五行反系 | Five Elements Reverse Link | 互换相克之位 | Mutual restraining positions | - | new_candidate |


<!-- FACTOR_BEGIN -->
| 因子类型 | 因子标签（人话） | 因子ID（如已存在） | 因子来源 | 角色/位置 | 取值/约束 | engine_id | 备注 |
|---|---|---|---|---|---|---|
| 神煞类 | 自缢煞 | zi_yi_sha | existing | 组合 | 戌见巳/巳见戌等 | bazi_semantic | 五行反系 |
| 神煞类 | 水溺煞 | shui_ni_sha | existing | 组合 | 丙子/癸未+咸池/羊刃 | bazi_semantic | 水厄 |
| 神煞类 | 挂剑煞 | gua_jian_sha | existing | 组合 | 巳酉丑申全+白虎 | bazi_semantic | 金暴 |
| 条件类 | 凶煞叠加 | malefic_overlap | existing | 结构 | 官符/大耗/元辰 | bazi_semantic | 增强条件 |
<!-- FACTOR_END -->
<!-- L2_END -->

<!-- L2.5_BEGIN -->
#### L2.5 桥接层

**因子关系层**：

| 关系ID | 关系类型 | 因子A | 因子B | 关系性质 | 条件约束 | 效果方向 | source_ref |
|-------|---------|-------|-------|---------|---------|---------|-----------|
| rel_smth_ziyi_001 | mapping | wuxing_fanxi | ziyi_position | 五行反系查自缢位 | 戌见巳等 | 固定对应 | 《三命通会》卷三#自缢煞 |
| rel_smth_ziyi_002 | compound | ziyi_diedie | jiduan_fengxian | 自缢煞叠加极端风险 | 官符大耗墓鬼 | 极险 | 《三命通会》卷三#自缢煞 |
| rel_smth_ziyi_003 | compound | shuini_diedie | nishuie | 水溺煞叠加水厄 | 咸池羊刃克身 | 极险 | 《三命通会》卷三#水溺煞 |
| rel_smth_ziyi_004 | compound | guajian_diedie | baolie_fengxian | 挂剑煞叠加暴烈风险 | 白虎元辰克身 | 极险 | 《三命通会》卷三#挂剑煞 |

**推理溯源层**：

| 证据ID | 原文锚点 | 涉及因子 | 推理步骤 | 结论方向 | 置信度 | 可生成规则 | 目标规则ID |
|-------|---------|---------|---------|---------|-------|----------|-----------|
| evi_smth_ziyi_001 | "动煞克身名颠坠，官符大耗仍须避" | ziyi_diedie | 动煞克身→官符大耗→凶险叠加 | 叠加效应 | 高 | ✅ | rule_ziyi_diedie |
| evi_smth_ziyi_002 | "五行若更来克身，一死悬梁一溺水" | keshen_jizhong | 五行克身→极凶→悬梁溺水 | 极端后果 | 高 | ✅ | rule_keshen |
| evi_smth_ziyi_003 | "纵不杀人身岂免" | guajian_shuangxiang | 金局全见白虎→纵不杀人→身岂免 | 双向风险 | 高 | ✅ | rule_guajian |

**跨体系概念映射层**：

| 概念ID | 共通语义 | 八字对应 | 占星对应 | 梦学对应 | 心理学对应 | 备注 |
|-------|---------|---------|---------|---------|-----------|------|
| concept_self_destruction | 自我毁灭 | 自缢煞 | 冥王十二宫 | - | 自毁倾向 | 五行反系 |
| concept_emotional_overwhelm | 情绪淹没 | 水溺煞 | 海王相位 | - | 情绪失控 | 水厄象 |

<!-- L2.5_END -->

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_03_ziyishui_001]` `[trigger: 自缢煞] [factor_trigger: zi_yi_sha]` `[role: 主干]` 要知自缢最凶神，戌巳辰亥并寅未，子酉一例为凶煞。 → `《三命通会·卷三》#自缢煞`
  - `[ns_smth_03_ziyishui_002]` `[trigger: 动煞克身] [factor_trigger: 动煞克身]` `[role: 主干]` 动煞克身名颠坠，更见官符、大耗、墓鬼者，一死悬梁。 → `《三命通会·卷三》#自缢煞`
  - `[ns_smth_03_ziyishui_003]` `[trigger: 水溺煞] [factor_trigger: shui_ni_sha]` `[role: 主干]` 丙子、癸未、癸丑上带咸池、金刃、羊刃，又纳音来克身者，一溺水亡。 → `《三命通会·卷三》#水溺煞`
  天屠煞。此煞除子日午时，午日子时外，自余丑曰日亥时，亥日丑时，寅日戌时，戌日寅时，卯日酉时，酉日卯时，辰日申时，申日辰时，巳日未时，未日巳时，依次逐两位数之。君子犯者，主异疾，肠风脚气；小人折损肢体。重犯者，主徒配。
  天刑煞。此煞取子丑人乙时，寅人庚时，卯辰人辛时，巳人壬时，午未人癸时，甲人丙时，酉戌人丁时，亥人戊时，取时刑克本命。犯者遭刑有疾。
  雷霆煞。正七二八子寅方，三九四十辰午当；五十一申六二戌，必主雷轰虎咬亡。又云：“正七下加子，二八在寅方，三九居辰上，四十午位伤，五十一申位，六十二戌方。”正月起，子顺行六阳位。此煞人命遇之，如逢禄，贵；吉星临压，则吉，好行阴骘，为法官掌雷霆行符敕水之人，或成佛作祖之辈。如遇羊刃、的煞、飞廉等会，命限必凶，主堕于天真雷伤、虎啖、天谴、瘟疾或溺水、囹圄死。

- **分字分词释义**：
  - **吞陷煞**：从戌逆推至年宫，仅在财帛宫主富，余宫主灾，特定年份主水厄。
  - **天屠煞**：特定日时相冲相刑，主肢体折损与怪病。
  - **雷霆煞**：按月令顺行六阳位，主掌权或遭雷击天谴，吉凶两极。

- **规范化释义（primary_lang_explained）**：
  本节论述四种与天灾刑罚有关的神煞。天火煞指寅午戌三合火局全，且天干透丙丁而地支无水，主极易遭火灾，尤其在火旺运限。天屠煞按特定日时推算（如丑日亥时），犯者主怪病或肢体折损，重则刑徒。天刑煞取时干刑克年命（如子丑人见乙时），主刑伤疾病。雷霆煞按月令取位（如正七月见子），遇吉星禄马则主掌法官雷霆之权或成佛作祖；遇凶煞（羊刃、飞廉）则主雷击、虎咬、天谴等横死。

- **次语种完整诠释（secondary_lang_full）**：
  This section discusses four Sha related to celestial disasters and punishment. Sky Fire Sha (Tian Huo) occurs when the Yin-Wu-Xu Fire Bureau is complete, Heavenly Stems show Bing/Ding, and there is no Water; it indicates high risk of fire disasters. However, the text does not mention Sky Fire Sha in this section. Sky Slaughter Sha (Tian Tu) depends on specific Day-Hour combinations (e.g., Ox Day Pig Hour), indicating strange diseases or limb injuries. Sky Punishment Sha (Tian Xing) involves the Hour Stem clashing with the Year Stem, indicating punishment or illness. Thunder Sha (Lei Ting) is determined by the month (e.g., 1st/7th month seeing Rat); if meeting Auspicious Stars/Lu, it indicates spiritual authority or judicial power; if meeting Malefics (Goat Blade), it indicates death by thunder, tiger, or divine punishment.

- **核心要点**：
  - 天火煞：全火局无水 -> 火灾
  - 天屠/天刑：日时/时年相克 -> 刑伤疾病
  - 雷霆煞：吉凶两判 -> 掌权或横死

- **详细解说**：
  这组神煞突出了“极端五行与天道刑罚”的概念。

<!-- L2_BEGIN -->天火煞是典型的五行偏枯（火炎土燥），雷霆煞则带有浓厚的道教色彩，认为其具有“代天行道”的威能——善用则为法官/法师，恶用则遭天谴。这在现代可理解为“巨大的能量爆发点”，既可是权威的来源，也可是毁灭的根源。

- **语义提取（L2）**：
  - **主题**：自然灾害与天道刑罚标记
  - **自然属性**：象征烈火（天火）、屠刀（天屠）、刑法（天刑）、雷霆（雷霆）；特性爆裂、威严、两极化；元素三合火、六阳位
  - **功能象义**：为命局提供「爆发性风险」标签；区分物理灾害与社会刑罚；强调吉凶转化（雷霆）
  - **条件结构**：必要条件特定局势/日时；增强条件岁运引发；转化条件吉星临压（雷霆变权）
  - **多层解释**：字面层火灾雷击；象征层能量失控/天道审判；实践层提示建模突发事故与法律风险；心理层鼓励敬畏规则与积德行善

- **L2-术语对齐（Term Glossary）**：
| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---|---|---|---|
| 天火煞 | Sky Fire Sha | 寅午戌全透丙丁无水主火灾 | Yin-Wu-Xu complete with Bing/Ding and no Water, indicates fire disaster | - | new_candidate |
| 雷霆煞 | Thunder Sha | 正月起子顺行六阳位主掌权或天谴 | Starts from Rat in 1st month following Yang positions, indicates authority or divine punishment | - | new_candidate |
| 天刑煞 | Sky Punishment Sha | 时干刑克年命主刑伤 | Hour Stem clashes Year Life, indicates punishment/injury | - | new_candidate |

<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| 因子类型 | 因子标签（人话） | 因子ID（如已存在） | 因子来源 | 角色/位置 | 取值/约束 | engine_id | 备注 |
|---|---|---|---|---|---|---|
| 神煞类 | 天火煞 | tian_huo_sha | existing | 组合 | 寅午戌全+丙/丁+无水 | bazi_semantic | 火灾 |
| 神煞类 | 雷霆煞 | lei_ting_sha | existing | 月时 | 正七见子等 | bazi_semantic | 两极化 |
| 神煞类 | 天屠煞 | tian_tu_sha | existing | 日时 | 丑亥/寅戌等 | bazi_semantic | 肢体折损 |
| 神煞类 | 天刑煞 | tian_xing_sha | existing | 年时 | 子丑人见乙时等 | bazi_semantic | 刑伤 |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 桥接层

**因子关系层**：

| 关系ID | 关系类型 | 因子A | 因子B | 关系性质 | 条件约束 | 效果方向 | source_ref |
|-------|---------|-------|-------|---------|---------|---------|-----------|
| rel_smth_tianhuo_001 | trigger | yinwuxu_huoju | tian_huo_sha | 三合火局触发天火煞 | 透丙丁无水 | 火灾风险 | 《三命通会》卷三#天火煞 |
| rel_smth_tianhuo_002 | bipolar | lei_ting_sha | ji_xiong | 雷霆煞吉凶两极 | 吉星则权凶煞则死 | 两极转化 | 《三命通会》卷三#雷霆煞 |
| rel_smth_tianhuo_003 | trigger | rishi_chong | tian_tu_sha | 日时相冲触发天屠煞 | 特定日时 | 肢体折损 | 《三命通会》卷三#天屠煞 |
| rel_smth_tianhuo_004 | trigger | shigan_ke | tian_xing_sha | 时干克年命触发天刑煞 | 刑克关系 | 刑伤疾病 | 《三命通会》卷三#天刑煞 |

**推理溯源层**：

| 证据ID | 原文锚点 | 涉及因子 | 推理步骤 | 结论方向 | 置信度 | 可生成规则 | 目标规则ID |
|-------|---------|---------|---------|---------|-------|----------|-----------|
| evi_smth_tianhuo_001 | "寅午戌全而天干有丙丁、五位中全不见水者为天火煞" | huoju_wushui | 三合火全→透火干→无水制→天火煞成 | 火灾判定 | 高 | ✅ | rule_tianhuo_trigger |
| evi_smth_tianhuo_002 | "雷霆煞如逢禄贵吉星…为法官掌雷霆" | leiting_jixing | 雷霆煞→遇吉星→掌权威；遇凶煞→横死 | 两极判断 | 高 | ✅ | rule_leiting_bipolar |

**跨体系概念映射层**：

| 概念ID | 共通语义 | 八字对应 | 占星对应 | 梦学对应 | 心理学对应 | 备注 |
|-------|---------|---------|---------|---------|-----------|------|
| concept_elemental_explosion | 能量爆发 | 天火煞 | 火星T刑 | 火灾梦 | 情绪爆发 | 五行偏枯 |
| concept_divine_authority | 天道权威 | 雷霆煞 | 木星冥王 | 雷电梦 | 权威认同 | 代天行道 |

<!-- L2.5_END -->

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_03_tianhuo_001]` `[trigger: 天火煞] [factor_trigger: tian_huo_sha]` `[role: 主干]` 寅午戌全而天干有丙丁、五位中全不见水者为天火煞，年运至火气生旺处，当防火灾。 → `《三命通会·卷三》#天火煞`
  - `[ns_smth_03_tianhuo_002]` `[trigger: 天屠煞] [factor_trigger: tian_tu_sha]` `[role: 主干]` 丑日亥时、亥日丑时、寅日戌时等为天屠煞，君子犯之主异疾肠风脚气，小人折损肢体，重犯者主徒配。 → `《三命通会·卷三》#天屠煞`
  - `[ns_smth_03_tianhuo_003]` `[trigger: 雷霆煞吉象] [factor_trigger: lei_ting_sha]` `[role: 主干]` 雷霆煞人命遇之，如逢禄贵吉星，好行阴骘者，为法官掌雷霆行符敕水之人，或成佛作祖。 → `《三命通会·卷三》#雷霆煞`
  - `[ns_smth_03_tianhuo_004]` `[trigger: 雷霆煞凶象] [factor_trigger: lei_ting_sha]` `[role: 主干]` 若雷霆煞与羊刃、飞廉等会，命限必凶，主堕于雷轰、虎啖、天谴、瘟疾或溺水、囹圄死。 → `《三命通会·卷三》#雷霆煞`
  - `[ns_smth_03_tianhuo_005]` `[trigger: 天火有水则非] [factor_trigger: 天火有水则非]` `[role: 主干]` 天火煞以寅午戌全而无水为要，有水则火势受制，其凶象大减。 → `《三命通会·卷三》#天火煞`

---

### 5. 论日刑、流血与剑锋戟锋煞

- **原文（source_text）**：
  日刑煞。以本生日上数甲子，本日干住。阳干顺数，阴干逆数。若在命宫，主极刑；三合，主徒配；对宫，主外死。
  流血煞。以本生月起，子顺数至本年住。若在命宫、三合、对宫、主痈疽，庶人徒配，妇人产厄。
  剑锋煞。甲子旬剑辰锋戌，甲午旬剑戌锋辰，甲寅旬剑午锋申，甲申旬剑子锋寅，甲辰旬剑申锋午，甲戌旬剑寅锋子。随在各宫断，如第五宫露，损子；第四宫露，损田宅。
  戟锋煞。正月起甲，二月乙，三月戊，四月丙，五月丁，六月己，七月庚，八月辛，九月戊，十月壬，十一月癸，十二月巳，逐月旺干加临，日时带两重者，凶；更与悬针相见，主决配伤残。

- **分字分词释义**：
  - **日刑煞**：从日柱推算至命宫，主极刑或外死。
  - **流血煞**：从月支推算至流年，主脓疮、刑配或产难。
  - **剑锋/戟锋**：按旬或月推算，主损子、破家或刑伤。

- **规范化释义（primary_lang_explained）**：
  本节介绍四种与刑伤流血相关的神煞。日刑煞以日干为起点，阳干顺数、阴干逆数至命宫，若落命宫主极刑，落三合主徒配，落对宫主客死他乡。流血煞从月支顺数至流年，落命宫或三合主脓疮痈疽、刑配或产厄。剑锋煞按六甲旬分"剑"与"锋"两位，落各宫主对应损耗（如第五宫主损子）。戟锋煞按月令取旺干，日时重犯主刑配伤残。这组煞强调"刑伤"与"流血"，属于物理损伤的标记。

- **次语种完整诠释（secondary_lang_full）**：
  This section introduces four Sha related to punishment and bleeding. Day Punishment Sha (Ri Xing) calculates from Day Stem (Yang ascending, Yin descending) to Life Palace, indicating execution (Life Palace), exile (Triad), or death abroad (Opposition). Bleeding Sha (Liu Xue) counts from Month Branch to Current Year, indicating ulcers, exile, or childbirth difficulties. Sword Edge Sha (Jian Feng) assigns "Sword" and "Edge" positions per six Jia periods, indicating losses in corresponding palaces (e.g., 5th palace = loss of children). Halberd Edge Sha (Ji Feng) uses monthly prosperous Stems; double occurrence indicates exile and injury. These Sha emphasize physical harm and bleeding.

- **核心要点**：
  - 日刑：命宫/三合/对宫 -> 极刑/徒配/外死
  - 流血：脓疮产厄
  - 剑锋/戟锋：各宫损耗

- **详细解说**：
  这组煞是宫位推演系统的典型，将干支推算结果映射到"命宫十二宫"体系，根据落宫位置判断吉凶类型。现代应用中可理解为"特定时间窗口的伤害风险"，如日刑煞可标记"法律风险年"，流血煞可标记"健康风险年"（尤其外科手术或意外伤害），剑锋戟锋则标记"家庭/子女风险"。"""
    normalized_text_zh: str = """"""
    subject: str = "自缢煞、水溺煞与挂剑煞略解"
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
        l1_anchor="smth_v1.0.0_自缢煞_水溺煞与挂剑煞略解_001_L1",
    )
    version: str = "1.0.0"
