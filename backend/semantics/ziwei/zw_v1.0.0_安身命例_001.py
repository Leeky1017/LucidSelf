"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.653975
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
    semantic_id="zw_v1.0.0_安身命例_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 安身命例(SemanticEntry):
    """
    **主题**：身命宫的安放规则，为紫微斗数排盘的第一步。

#### 原文（断句）：

大抵入命俱从寅上起，正月顺数至本生月止。又自人生月上起子时，逆至本生时安命，顺至本生时安身。假如正月生子时，就在...
    """
    
    original_text: str = """**主题**：身命宫的安放规则，为紫微斗数排盘的第一步。

#### 原文（断句）：

大抵入命俱从寅上起，正月顺数至本生月止。又自人生月上起子时，逆至本生时安命，顺至本生时安身。假如正月生子时，就在寅宫安命身。丑时逆转丑安命，顺去卯安身；寅时逆转，子安命，顺至辰安身。余宫仿此。又若闰正月生者，要在二月内起安身命，凡有闰月，俱要依此为例。

#### 分字分词释义：

- **入命**：确定命宫位置，即"安命"的起算过程。
- **从寅上起**：以寅宫为正月的起点，开始顺数月份。
- **本生月**：命主实际出生的月份（农历月份）。
- **起子时**：以子时为时辰计数的起点。
- **逆至本生时**：从子时开始逆时针数到命主出生的时辰。
- **顺至本生时**：从子时开始顺时针数到命主出生的时辰。
- **闰月**：农历中的闰月，一年十三个月时出现的附加月份。
- **二月内起**：闰正月生者，在二月宫位上开始计算身命。

#### 规范化释义（primary_lang_explained）：

大抵入命俱从寅上起正月顺数至本生月止。又自人生月上起子时逆至本生时安命顺至本生时安身。假如正月生子时就在寅宫安命身。丑时逆转丑安命顺去卯安身寅时逆转子安命顺至辰安身。余宫仿此。又若闰正月生者要在二月内起安身命凡有闰月俱要依此为例。

#### 核心要点：

1. **从寅起月**：正月从寅宫开始顺数至生月
2. **生月起时**：从生月宫位起子时
3. **逆数安命**：从子时逆数至生时安命
4. **顺数安身**：从子时顺数至生时安身
5. **闰月处理**：闰月生者在下月内起算

#### 步骤详解：

**步骤1**：确定生月宫位
- 正月=寅、二月=卯、三月=辰...依次顺推

**步骤2**：从生月起子时
- 在生月宫位上起子时

**步骤3**：安命宫
- 从子时逆时针数至生时，该宫为命宫

**步骤4**：安身宫
- 从子时顺时针数至生时，该宫为身宫

#### 示例：

- **正月子时生**：寅宫安命、寅宫安身（同宫）
- **正月丑时生**：丑宫安命、卯宫安身
- **正月寅时生**：子宫安命、辰宫安身

#### 特殊规则：

- **闰月**：闰正月生者，在二月内起算
- **重要性**：身命寫是全盘的核心，必须精确

#### 完整对等诠释（secondary_lang_full·1安身命例）：

Body–Life Palace placement establishes the fundamental coordinate grid of a Ziwei Doushu chart. First it fixes the month palace: treat the Yin palace as the seat of the first lunar month and move one house forward for each month until you arrive at the native’s birth month. Then it fixes the Life Palace: from that birth‑month palace mark Zi hour as the starting point and count counter‑clockwise through the twelve houses until you reach the birth hour; the house where you stop is the Life Palace. From the same starting point, count clockwise to the birth hour again; that house becomes the Body Palace. For people born in an intercalary first month, the counting is shifted to the following month so that leap months do not distort the scheme.

Together the Life and Body palaces act as a paired origin for all later star placements. The Life Palace describes core identity, temperament and fate‑pattern, while the Body Palace shows how those qualities are expressed through behaviour, posture and everyday choices. Because every other palace and star is interpreted relative to this dual anchor, accurate birth time and correct treatment of leap months are critical; a mistake here skews the coordinates of the entire chart.

#### L2-术语对齐（Term Glossary·六列）：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 命宫 | Life Palace | 代表自我本质的核心宫位 | Core palace representing self-essence | palace_ming | existing |
| 身宫 | Body Palace | 代表行为表达的辅助宫位 | Auxiliary palace behavioral expression | palace_shen | existing |
| 从寅起月 | Yin-Month Starting | 从寅宫开始按月顺数 | Starting from Yin by months | algo_congyinqiyue | new_candidate |
| 逆数安命 | Counter-Clockwise Life | 逆时针数至生时定命宫 | Counter-clockwise to birth hour | algo_nishuanming | new_candidate |
| 顺数安身 | Clockwise Body | 顺时针数至生时定身宫 | Clockwise to birth hour | algo_shunshanshen | new_candidate |
| 闰月处理 | Intercalary Adjust | 闰月生者在下月起算 | Intercalary in subsequent month | algo_runyuechuli | new_candidate |

#### 详细解说：

安身命例是紫微斗数排盘的第一步，也是最基础的一步。身命二宫的位置决定了整个命盘的坐标系统，所有后续的星曜安放都以此为基础。

**算法核心**：
1. **月份定位**：以寅宫为正月，卯宫为二月，辰宫为三月……依次类推。这是"从寅上起"的含义。
2. **命宫定位**：在生月宫位上起子时，然后逆时针数到生时所在的宫位，即为命宫。
3. **身宫定位**：同样在生月宫位上起子时，但顺时针数到生时所在的宫位，即为身宫。

**身命二宫的关系**：
- **命宫**：代表先天本质、性格根基、一生命运主线。
- **身宫**：代表后天表现、行为模式、人生选择倾向。
- 命宫与身宫可能同宫（如子时生人），也可能相隔多宫。同宫者表里如一，相隔者内外有别。

**闰月处理的原理**：
农历闰月是为了调和朔望月与回归年的差异而设的附加月份。在紫微斗数中，闰月生人的月份归属到下一个月，这样既保持了算法的一致性，也避免了闰月带来的歧义。

#### 校勘与字词辨析（bilingual）：

- **"入命"**：此处指"安命"的整个过程，非指星曜入命宫。英文可译为"establishing the Life Palace"。
- **"俱从寅上起"**：所有人都从寅宫开始计算，不分男女。英文："all charts begin counting from the Yin palace"。
- **"逆转"/"顺去"**：逆转指逆时针，顺去指顺时针。英文分别为"counter-clockwise"和"clockwise"。
- **"二月内起"**：指在二月的宫位（卯宫）上开始计算，而非二月份。英文："calculated within the second month palace"。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："身命安排第一功，寅宫正月顺推中，逆行安命顺安身，此法千金不换通。"此句强调身命安排是排盘首要步骤，算法精确方可后续推演。
- **实操口诀**："正月寅，二月卯，三月辰来四月巳。生月起时记分明，逆命顺身不可移。"此口诀帮助学习者快速记忆月份对应宫位的规则。
- **现代应用**：现代排盘软件已自动计算身命位置，但理解其原理对于验证软件结果、处理特殊情况（如闰月、跨夜子时）仍有重要价值。

**L2 叙事素材层（规范格式）**：

- `[ns_zwds_j3_001]` `[trigger: 安命算法]` `[factor_trigger: algo_anming]` `[role: 主干]` 安命算法为确定命宫位置的核心算法。 → 《安身命例》"逆行安命"
- `[ns_zwds_j3_002]` `[trigger: 安身算法]` `[factor_trigger: algo_anshen]` `[role: 主干]` 安身算法为确定身宫位置的核心算法。 → 《安身命例》"顺安身"
- `[ns_zwds_j3_003]` `[trigger: 从寅起月]` `[factor_trigger: algo_congyinqiyue]` `[role: 主干]` 从寅起月为月份定位的基础算法。 → 《安身命例》"寅宫正月顺推中"
- `[ns_zwds_j3_004]` `[trigger: 生月定位]` `[factor_trigger: algo_shengyuedingwei]` `[role: 主干]` 生月定位为根据生月确定起点的算法。 → 《安身命例》"顺数至本生月止"
- `[ns_zwds_j3_005]` `[trigger: 生时定位]` `[factor_trigger: algo_shengshidingwei]` `[role: 主干]` 生时定位为根据生时确定身命的算法。 → 《安身命例》"逆至本生时安命"
- `[ns_zwds_j3_006]` `[trigger: 闰月处理]` `[factor_trigger: algo_runyuechuli]` `[role: 例外处理]` 闰月处理为闰月归入下月的特殊算法。 → 《安身命例》"闰月入下月"
- `[ns_zwds_j3_007]` `[trigger: 跨夜子时]` `[factor_trigger: algo_kuayezishi]` `[role: 例外处理]` 跨夜子时为子时跨日的特殊处理算法。 → 《安身命例》
- `[ns_zwds_j3_008]` `[trigger: 十二宫序]` `[factor_trigger: structure_shiergongxu]` `[role: 主干]` 十二宫序为十二宫位的排列顺序。 → 《安身命例》
- `[ns_zwds_j3_009]` `[trigger: 寅宫起点]` `[factor_trigger: palace_yin]` `[role: 主干]` 寅宫为正月起点，十二宫排列的基准位置。 → 《安身命例》"寅宫正月"
- `[ns_zwds_j3_010]` `[trigger: 子时起点]` `[factor_trigger: time_zishi]` `[role: 主干]` 子时为十二时辰的起点，安身命的时间基准。 → 《安身命例》
- `[ns_zwds_j3_055]` `[trigger: 文星定位算法]` `[factor_trigger: algo_wenxingdingwei]` `[role: 主干]` 文星定位算法为根据生时安放文昌文曲的算法。 → 《安身命例》
- `[ns_zwds_j3_056]` `[trigger: 火铃定位算法]` `[factor_trigger: algo_huolingdingwei]` `[role: 主干]` 火铃定位算法为根据生年支安放火星铃星的算法。 → 《安身命例》
- `[ns_zwds_j3_057]` `[trigger: 紫微定位算法]` `[factor_trigger: algo_ziweidingwei]` `[role: 主干]` 紫微定位算法为根据五行局和生日确定紫微位置的算法。 → 《安身命例》
- `[ns_zwds_j3_058]` `[trigger: 天府定位算法]` `[factor_trigger: algo_tianfudingwei]` `[role: 主干]` 天府定位算法为根据紫微位置推算天府位置的算法。 → 《安身命例》
- `[ns_zwds_j3_059]` `[trigger: 擎羊定位算法]` `[factor_trigger: algo_qingyangdingwei]` `[role: 主干]` 擎羊定位算法为根据年干定位擎羊的算法。 → 《安身命例》
- `[ns_zwds_j3_060]` `[trigger: 陀罗定位算法]` `[factor_trigger: algo_tuoluodingwei]` `[role: 主干]` 陀罗定位算法为根据年干定位陀罗的算法。 → 《安身命例》
- `[ns_zwds_j3_061]` `[trigger: 禄存定位算法]` `[factor_trigger: algo_lucundingwei]` `[role: 主干]` 禄存定位算法为根据年干定位禄存的算法。 → 《安身命例》
- `[ns_zwds_j3_062]` `[trigger: 四化定位算法]` `[factor_trigger: algo_sihuadingwei]` `[role: 主干]` 四化定位算法为根据年干确定四化星的算法。 → 《安身命例》
- `[ns_zwds_j3_063]` `[trigger: 流年定位算法]` `[factor_trigger: algo_liuniandingwei]` `[role: 主干]` 流年定位算法为根据流年确定流年星曜的算法。 → 《安身命例》
- `[ns_zwds_j3_064]` `[trigger: 大限定位算法]` `[factor_trigger: algo_daxiandingwei]` `[role: 主干]` 大限定位算法为根据五行局确定大限起点的算法。 → 《安身命例》
- `[ns_zwds_j3_065]` `[trigger: 斗君定位算法]` `[factor_trigger: algo_doujundingwei]` `[role: 主干]` 斗君定位算法为根据生月和生时确定斗君的算法。 → 《安身命例》
- `[ns_zwds_j3_066]` `[trigger: 末年照格]` `[factor_trigger: pattern_monianzhao]` `[role: 条件分支]` 末年照格为晚年限运的格局配置。 → 《安身命例》
- `[ns_zwds_j3_067]` `[trigger: 文武类型]` `[factor_trigger: type_wenwu]` `[role: 主干]` 文武类型为文武职业的分类。 → 《安身命例》
- `[ns_zwds_j3_068]` `[trigger: 祖业格]` `[factor_trigger: pattern_zuye]` `[role: 条件分支]` 祖业格为继承祖业的格局配置。 → 《安身命例》
- `[ns_zwds_j3_069]` `[trigger: 刑克格]` `[factor_trigger: pattern_xingke]` `[role: 条件分支]` 刑克格为刑伤克害的格局配置。 → 《安身命例》
- `[ns_zwds_j3_070]` `[trigger: 逆数安命算法]` `[factor_trigger: algo_nishuanming]` `[role: 主干]` 逆数安命算法为逆时针数宫安命的算法。 → 《安身命例》"逆行安命"
- `[ns_zwds_j3_071]` `[trigger: 顺数安身算法]` `[factor_trigger: algo_shunshanshen]` `[role: 主干]` 顺数安身算法为顺时针数宫安身的算法。 → 《安身命例》"顺安身"
- `[ns_zwds_j3_072]` `[trigger: 月主结构]` `[factor_trigger: structure_yuezhu]` `[role: 主干]` 月主结构为月份主星的结构配置。 → 《安身命例》
- `[ns_zwds_j3_073]` `[trigger: 北斗七星结构]` `[factor_trigger: structure_beidouqixing]` `[role: 主干]` 北斗七星结构为北斗七星的排列结构。 → 《安身命例》
- `[ns_zwds_j3_074]` `[trigger: 南斗六星结构]` `[factor_trigger: structure_nandoliuxing]` `[role: 主干]` 南斗六星结构为南斗六星的排列结构。 → 《安身命例》
- `[ns_zwds_j3_075]` `[trigger: 七杀破军组合]` `[factor_trigger: star_qisha_pojun]` `[role: 条件分支]` 七杀破军组合为七杀与破军的凶星组合。 → 《安身命例》
- `[ns_zwds_j3_076]` `[trigger: 驿马对冲算法]` `[factor_trigger: algo_yimaduichong]` `[role: 主干]` 驿马对冲算法为天马驿马对冲的算法。 → 《安身命例》
- `[ns_zwds_j3_077]` `[trigger: 十干禄位原则]` `[factor_trigger: principle_shiganluweu]` `[role: 主干]` 十干禄位原则为十天干禄星定位的原则。 → 《安身命例》
- `[ns_zwds_j3_078]` `[trigger: 阴阳顺逆年行]` `[factor_trigger: algo_yinyangshuninianxing]` `[role: 主干]` 阴阳顺逆年行为阴阳年顺逆行的算法。 → 《安身命例》
- `[ns_zwds_j3_079]` `[trigger: 吉神群]` `[factor_trigger: group_jishen]` `[role: 主干]` 吉神群为吉利神煞的分组。 → 《安身命例》
- `[ns_zwds_j3_080]` `[trigger: 八座星]` `[factor_trigger: star_bazuo]` `[role: 主干]` 八座为辅佐星，与三台同会主贵显。 → 《安身命例》
- `[ns_zwds_j3_081]` `[trigger: 天虚星]` `[factor_trigger: star_tianxu]` `[role: 主干]` 天虚为耗星，主虚耗损失。 → 《安身命例》
- `[ns_zwds_j3_082]` `[trigger: 凤阁星]` `[factor_trigger: star_fengge]` `[role: 主干]` 凤阁为文星，主文采风华。 → 《安身命例》
- `[ns_zwds_j3_083]` `[trigger: 生时卯点原则]` `[factor_trigger: principle_shengshimaodian]` `[role: 主干]` 生时卯点原则为生时定位的基准原则。 → 《安身命例》
- `[ns_zwds_j3_084]` `[trigger: 生时顺数算法]` `[factor_trigger: algo_shengshishunshuf]` `[role: 主干]` 生时顺数算法为根据生时顺数的算法。 → 《安身命例》
- `[ns_zwds_j3_085]` `[trigger: 纳音五行原则]` `[factor_trigger: principle_nayinwuxing]` `[role: 主干]` 纳音五行原则为六十甲子纳音五行的原则。 → 《安身命例》
- `[ns_zwds_j3_086]` `[trigger: 男女顺逆原则]` `[factor_trigger: principle_nannvshunni]` `[role: 主干]` 男女顺逆原则为阳男阴女顺逆行的原则。 → 《安身命例》
- `[ns_zwds_j3_087]` `[trigger: 长生位]` `[factor_trigger: phase_changsheng]` `[role: 主干]` 长生位为十二长生之首，主生发旺盛。 → 《安身命例》
- `[ns_zwds_j3_088]` `[trigger: 养位]` `[factor_trigger: phase_yang]` `[role: 主干]` 养位为十二长生之养，主培养蓄积。 → 《安身命例》
- `[ns_zwds_j3_089]` `[trigger: 天喜星]` `[factor_trigger: star_tianxi]` `[role: 主干]` 天喜为喜星，主喜庆添丁。 → 《安身命例》
- `[ns_zwds_j3_090]` `[trigger: 年龄阶段吉凶原则]` `[factor_trigger: principle_nianlingjiexiong]` `[role: 主干]` 年龄阶段吉凶原则为不同年龄段吉凶判断的原则。 → 《安身命例》
- `[ns_zwds_j3_091]` `[trigger: 天同化忌格]` `[factor_trigger: pattern_tiantonghuaji]` `[role: 条件分支]` 天同化忌格为天同化忌的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_092]` `[trigger: 文曲化忌格]` `[factor_trigger: pattern_wenquhuaji]` `[role: 条件分支]` 文曲化忌格为文曲化忌的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_093]` `[trigger: 文昌化忌格]` `[factor_trigger: pattern_wenchanghuaji]` `[role: 条件分支]` 文昌化忌格为文昌化忌的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_094]` `[trigger: 天机化忌格]` `[factor_trigger: pattern_tianjihuaji]` `[role: 条件分支]` 天机化忌格为天机化忌的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_213]` `[trigger: 天梁化忌格]` `[factor_trigger: pattern_tianlianghuaji]` `[role: 条件分支]` 天梁化忌格为天梁化忌的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_214]` `[trigger: 贪狼化忌格]` `[factor_trigger: pattern_tanlanghuaji]` `[role: 条件分支]` 贪狼化忌格为贪狼化忌的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_215]` `[trigger: 破军化忌格]` `[factor_trigger: pattern_pojunhuaji]` `[role: 条件分支]` 破军化忌格为破军化忌的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_216]` `[trigger: 紫微化权格]` `[factor_trigger: pattern_ziweihuaquan]` `[role: 条件分支]` 紫微化权格为紫微化权的贵格配置。 → 《安身命例》
- `[ns_zwds_j3_217]` `[trigger: 天府化科格]` `[factor_trigger: pattern_tianfuhuake]` `[role: 条件分支]` 天府化科格为天府化科的贵格配置。 → 《安身命例》
- `[ns_zwds_j3_218]` `[trigger: 武曲化禄格]` `[factor_trigger: pattern_wuquhualu]` `[role: 条件分支]` 武曲化禄格为武曲化禄的富格配置。 → 《安身命例》
- `[ns_zwds_j3_219]` `[trigger: 太阳化禄格]` `[factor_trigger: pattern_taiyanghualu]` `[role: 条件分支]` 太阳化禄格为太阳化禄的贵格配置。 → 《安身命例》
- `[ns_zwds_j3_220]` `[trigger: 巨门化禄格]` `[factor_trigger: pattern_jumenhualu]` `[role: 条件分支]` 巨门化禄格为巨门化禄的富格配置。 → 《安身命例》
- `[ns_zwds_j3_221]` `[trigger: 天梁化禄格]` `[factor_trigger: pattern_tianlianghualu]` `[role: 条件分支]` 天梁化禄格为天梁化禄的贵格配置。 → 《安身命例》
- `[ns_zwds_j3_222]` `[trigger: 贪狼化禄格]` `[factor_trigger: pattern_tanlanghualu]` `[role: 条件分支]` 贪狼化禄格为贪狼化禄的富格配置。 → 《安身命例》
- `[ns_zwds_j3_223]` `[trigger: 破军化禄格]` `[factor_trigger: pattern_pojunhualu]` `[role: 条件分支]` 破军化禄格为破军化禄的变动富格。 → 《安身命例》
- `[ns_zwds_j3_224]` `[trigger: 廉贞化禄格]` `[factor_trigger: pattern_lianzhenhualu]` `[role: 条件分支]` 廉贞化禄格为廉贞化禄的富格配置。 → 《安身命例》
- `[ns_zwds_j3_225]` `[trigger: 天同化禄格]` `[factor_trigger: pattern_tiantonghualu]` `[role: 条件分支]` 天同化禄格为天同化禄的福格配置。 → 《安身命例》
- `[ns_zwds_j3_226]` `[trigger: 天机化禄格]` `[factor_trigger: pattern_tianjihualu]` `[role: 条件分支]` 天机化禄格为天机化禄的贵格配置。 → 《安身命例》
- `[ns_zwds_j3_227]` `[trigger: 太阴化禄格]` `[factor_trigger: pattern_taiyinhualu]` `[role: 条件分支]` 太阴化禄格为太阴化禄的富格配置。 → 《安身命例》
- `[ns_zwds_j3_228]` `[trigger: 日月并明格]` `[factor_trigger: pattern_riyuebingming]` `[role: 条件分支]` 日月并明格为日月同明的贵格。 → 《安身命例》
- `[ns_zwds_j3_229]` `[trigger: 日月反背格]` `[factor_trigger: pattern_riyuefanbei]` `[role: 条件分支]` 日月反背格为日月反背的凶格。 → 《安身命例》
- `[ns_zwds_j3_230]` `[trigger: 明珠出海格]` `[factor_trigger: pattern_mingzhuchuhai]` `[role: 条件分支]` 明珠出海格为太阳升海的贵格。 → 《安身命例》
- `[ns_zwds_j3_231]` `[trigger: 日照雷门格]` `[factor_trigger: pattern_rizhaoleimen]` `[role: 条件分支]` 日照雷门格为太阳在卯的贵格。 → 《安身命例》
- `[ns_zwds_j3_232]` `[trigger: 月朗天门格]` `[factor_trigger: pattern_yuelangtianmen]` `[role: 条件分支]` 月朗天门格为太阴在亥的贵格。 → 《安身命例》
- `[ns_zwds_j3_233]` `[trigger: 劫空财富凶]` `[factor_trigger: malefic_jiekong_caif]` `[role: 条件分支]` 劫空财富凶为地劫地空在财帛宫的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_234]` `[trigger: 劫空财府凶]` `[factor_trigger: malefic_jiekong_caifu]` `[role: 条件分支]` 劫空财府凶为地劫地空冲财帛的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_235]` `[trigger: 劫空冲命凶]` `[factor_trigger: malefic_jiekong_chongming]` `[role: 条件分支]` 劫空冲命凶为地劫地空冲命宫的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_118]` `[trigger: 巨同不得地凶]` `[factor_trigger: malefic_jumen_tiantong_budedi]` `[role: 条件分支]` 巨同不得地凶为巨门天同不得地的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_119]` `[trigger: 克命限凶]` `[factor_trigger: malefic_keming_xian]` `[role: 条件分支]` 克命限凶为限运克命的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_120]` `[trigger: 空劫并夹凶]` `[factor_trigger: malefic_kongjie_bingjia]` `[role: 条件分支]` 空劫并夹凶为空劫并夹的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_121]` `[trigger: 空劫冲照凶]` `[factor_trigger: malefic_kongjie_chongzhao]` `[role: 条件分支]` 空劫冲照凶为空劫冲照的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_122]` `[trigger: 空劫叠守凶]` `[factor_trigger: malefic_kongjie_dieshou]` `[role: 条件分支]` 空劫叠守凶为空劫叠守的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_123]` `[trigger: 空劫命垣凶]` `[factor_trigger: malefic_kongjie_mingyuan]` `[role: 条件分支]` 空劫命垣凶为空劫在命垣的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_124]` `[trigger: 空劫身命忌凶]` `[factor_trigger: malefic_kongjie_shenming_ji]` `[role: 条件分支]` 空劫身命忌凶为空劫在身命遇忌的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_125]` `[trigger: 廉贪陷地凶]` `[factor_trigger: malefic_liantan_xiandi]` `[role: 条件分支]` 廉贪陷地凶为廉贞贪狼陷地的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_126]` `[trigger: 廉贞化忌凶]` `[factor_trigger: malefic_lianzhen_huaji]` `[role: 条件分支]` 廉贞化忌凶为廉贞化忌的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_127]` `[trigger: 流羊流陀叠并凶]` `[factor_trigger: malefic_liuyang_liutuo_dibing]` `[role: 条件分支]` 流羊流陀叠并凶为流羊流陀叠加的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_128]` `[trigger: 禄倒马倒凶]` `[factor_trigger: malefic_ludao_madao]` `[role: 条件分支]` 禄倒马倒凶为禄倒马倒的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_129]` `[trigger: 命逢劫空凶]` `[factor_trigger: malefic_ming_jiekong]` `[role: 条件分支]` 命逢劫空凶为命宫逢劫空的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_130]` `[trigger: 命带忌星凶]` `[factor_trigger: malefic_mingdai_jixing]` `[role: 条件分支]` 命带忌星凶为命宫带忌星的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_131]` `[trigger: 女命昌独凶]` `[factor_trigger: malefic_nvming_changdu]` `[role: 条件分支]` 女命昌独凶为女命文昌独守的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_132]` `[trigger: 擎羊害位凶]` `[factor_trigger: malefic_qingyang_hai]` `[role: 条件分支]` 擎羊害位凶为擎羊在害位的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_133]` `[trigger: 擎羊忌宿凶]` `[factor_trigger: malefic_qingyang_jisu]` `[role: 条件分支]` 擎羊忌宿凶为擎羊忌宿的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_134]` `[trigger: 擎羊天伤凶]` `[factor_trigger: malefic_qingyang_tianshang]` `[role: 条件分支]` 擎羊天伤凶为擎羊与天伤的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_135]` `[trigger: 七杀福宫凶]` `[factor_trigger: malefic_qisha_fugong]` `[role: 条件分支]` 七杀福宫凶为七杀在福德宫的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_136]` `[trigger: 日月反背凶]` `[factor_trigger: malefic_riyue_fanbei]` `[role: 条件分支]` 日月反背凶为日月反背的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_137]` `[trigger: 三方星煞凶]` `[factor_trigger: malefic_sanfang_xingsha]` `[role: 条件分支]` 三方星煞凶为三方遇煞星的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_138]` `[trigger: 三方羊陀凶]` `[factor_trigger: malefic_sanfang_yangtuo]` `[role: 条件分支]` 三方羊陀凶为三方遇羊陀的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_139]` `[trigger: 丧门白虎凶]` `[factor_trigger: malefic_sangmen_baihu]` `[role: 条件分支]` 丧门白虎凶为丧门白虎的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_140]` `[trigger: 同梁中正格]` `[factor_trigger: pattern_tongliang_zhongzheng]` `[role: 条件分支]` 同梁中正格为天同天梁中正的贵格。 → 《安身命例》
- `[ns_zwds_j3_141]` `[trigger: 文昌科禄格]` `[factor_trigger: pattern_wenchang_kelu]` `[role: 条件分支]` 文昌科禄格为文昌与科禄的贵格。 → 《安身命例》
- `[ns_zwds_j3_142]` `[trigger: 文昌秀气格]` `[factor_trigger: pattern_wenchang_xiuqi]` `[role: 条件分支]` 文昌秀气格为文昌秀气的贵格。 → 《安身命例》
- `[ns_zwds_j3_143]` `[trigger: 文昌羊火铃忌格]` `[factor_trigger: pattern_wenchang_yanghuo_lingji]` `[role: 条件分支]` 文昌羊火铃忌格为文昌遇羊火铃忌的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_144]` `[trigger: 武生巨门子格]` `[factor_trigger: pattern_wusheng_jumen_zi]` `[role: 条件分支]` 武生巨门子格为武曲生巨门在子的格局。 → 《安身命例》
- `[ns_zwds_j3_145]` `[trigger: 先成后败格]` `[factor_trigger: pattern_xianchenghoubai]` `[role: 条件分支]` 先成后败格为先成后败的格局。 → 《安身命例》
- `[ns_zwds_j3_146]` `[trigger: 限克格]` `[factor_trigger: pattern_xianke]` `[role: 条件分支]` 限克格为限运相克的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_147]` `[trigger: 先贫后富格]` `[factor_trigger: pattern_xianpinhoufu]` `[role: 条件分支]` 先贫后富格为先贫后富的格局。 → 《安身命例》
- `[ns_zwds_j3_148]` `[trigger: 刑克父母格]` `[factor_trigger: pattern_xingkefumu]` `[role: 条件分支]` 刑克父母格为刑克父母的凶险配置。 → 《安身命例》
- `[ns_zwds_j3_149]` `[trigger: 羊铃同剑格]` `[factor_trigger: pattern_yanglingtongjian]` `[role: 条件分支]` 羊铃同剑格为擎羊铃星同剑的格局。 → 《安身命例》
- `[ns_zwds_j3_150]` `[trigger: 寅申文星格]` `[factor_trigger: pattern_yinshen_wenxing]` `[role: 条件分支]` 寅申文星格为寅申宫文星的格局。 → 《安身命例》
- `[ns_zwds_j3_151]` `[trigger: 右弼归垣化权格]` `[factor_trigger: pattern_youbi_guiyuan_huaquan]` `[role: 条件分支]` 右弼归垣化权格为右弼归垣化权的贵格。 → 《安身命例》
- `[ns_zwds_j3_152]` `[trigger: 志夫擎羊格]` `[factor_trigger: pattern_zhifu_qingyang]` `[role: 条件分支]` 志夫擎羊格为志夫与擎羊的配置。 → 《安身命例》
- `[ns_zwds_j3_153]` `[trigger: 紫府共朝格]` `[factor_trigger: pattern_zifu_gongchao]` `[role: 条件分支]` 紫府共朝格为紫府共朝的贵格。 → 《安身命例》
- `[ns_zwds_j3_154]` `[trigger: 紫府加会格]` `[factor_trigger: pattern_zifu_jiahui]` `[role: 条件分支]` 紫府加会格为紫府加会的贵格。 → 《安身命例》
- `[ns_zwds_j3_155]` `[trigger: 紫府守命格]` `[factor_trigger: pattern_zifu_shouming]` `[role: 条件分支]` 紫府守命格为紫府守命的贵格。 → 《安身命例》
- `[ns_zwds_j3_156]` `[trigger: 紫破围官格]` `[factor_trigger: pattern_zipo_weiguan]` `[role: 条件分支]` 紫破围官格为紫破围官的贵格。 → 《安身命例》
- `[ns_zwds_j3_157]` `[trigger: 紫微天府寅宫格]` `[factor_trigger: pattern_ziwei_tianfu_yingong]` `[role: 条件分支]` 紫微天府寅宫格为紫微天府在寅的贵格。 → 《安身命例》
- `[ns_zwds_j3_158]` `[trigger: 紫微镇财格]` `[factor_trigger: pattern_ziwei_zhencai]` `[role: 条件分支]` 紫微镇财格为紫微镇财的富格。 → 《安身命例》
- `[ns_zwds_j3_159]` `[trigger: 紫相昌曲格]` `[factor_trigger: pattern_zixiang_changqu]` `[role: 条件分支]` 紫相昌曲格为紫相与昌曲的贵格。 → 《安身命例》
- `[ns_zwds_j3_160]` `[trigger: 紫相朝垣格]` `[factor_trigger: pattern_zixiang_chaoyuan]` `[role: 条件分支]` 紫相朝垣格为紫相朝垣的贵格。 → 《安身命例》
- `[ns_zwds_j3_161]` `[trigger: 左辅文昌八位格]` `[factor_trigger: pattern_zuofu_wenchang_bawei]` `[role: 条件分支]` 左辅文昌八位格为左辅文昌八位的贵格。 → 《安身命例》
- `[ns_zwds_j3_162]` `[trigger: 坐贵向贵格2]` `[factor_trigger: pattern_zuogui_xianggui]` `[role: 条件分支]` 坐贵向贵格为坐贵向贵的贵格。 → 《安身命例》
- `[ns_zwds_j3_163]` `[trigger: 左右昌曲格]` `[factor_trigger: pattern_zuoyou_changqu]` `[role: 条件分支]` 左右昌曲格为左右与昌曲的贵格。 → 《安身命例》
- `[ns_zwds_j3_164]` `[trigger: 威德虽致结果]` `[factor_trigger: result_weide_suizhi]` `[role: 结果]` 威德虽致结果为威德虽致的判断。 → 《安身命例》
- `[ns_zwds_j3_165]` `[trigger: 威震结果]` `[factor_trigger: result_weizhen]` `[role: 结果]` 威震结果为威震的判断。 → 《安身命例》
- `[ns_zwds_j3_166]` `[trigger: 文垂结果]` `[factor_trigger: result_wenchui]` `[role: 结果]` 文垂结果为文垂的判断。 → 《安身命例》
- `[ns_zwds_j3_167]` `[trigger: 显达结果]` `[factor_trigger: result_xianda]` `[role: 结果]` 显达结果为显达的判断。 → 《安身命例》
- `[ns_zwds_j3_168]` `[trigger: 闲置结果]` `[factor_trigger: result_xianzhi]` `[role: 结果]` 闲置结果为闲置的判断。 → 《安身命例》
- `[ns_zwds_j3_169]` `[trigger: 刑死结果]` `[factor_trigger: result_xingsi]` `[role: 结果]` 刑死结果为刑死的判断。 → 《安身命例》
- `[ns_zwds_j3_170]` `[trigger: 凶结果]` `[factor_trigger: result_xiong]` `[role: 结果]` 凶结果为凶的判断。 → 《安身命例》
- `[ns_zwds_j3_171]` `[trigger: 虚命结果]` `[factor_trigger: result_xuming]` `[role: 结果]` 虚命结果为虚命的判断。 → 《安身命例》
- `[ns_zwds_j3_172]` `[trigger: 延寿结果]` `[factor_trigger: result_yanshou]` `[role: 结果]` 延寿结果为延寿的判断。 → 《安身命例》
- `[ns_zwds_j3_173]` `[trigger: 夭寿结果]` `[factor_trigger: result_yaoshou]` `[role: 结果]` 夭寿结果为夭寿的判断。 → 《安身命例》
- `[ns_zwds_j3_174]` `[trigger: 以士林出宫结果]` `[factor_trigger: result_yi_shilin_chugong]` `[role: 结果]` 以士林出宫结果为以士林出宫的判断。 → 《安身命例》
- `[ns_zwds_j3_175]` `[trigger: 寅宫紫府贵命结果]` `[factor_trigger: result_yingong_zifu_guiming]` `[role: 结果]` 寅宫紫府贵命结果为寅宫紫府贵命的判断。 → 《安身命例》
- `[ns_zwds_j3_176]` `[trigger: 英气结果]` `[factor_trigger: result_yingqi]` `[role: 结果]` 英气结果为英气的判断。 → 《安身命例》
- `[ns_zwds_j3_177]` `[trigger: 阴子破败结果]` `[factor_trigger: result_yinzi_pobai]` `[role: 结果]` 阴子破败结果为阴子破败的判断。 → 《安身命例》
- `[ns_zwds_j3_178]` `[trigger: 灾结果]` `[factor_trigger: result_zai]` `[role: 结果]` 灾结果为灾的判断。 → 《安身命例》
- `[ns_zwds_j3_179]` `[trigger: 灾除结果]` `[factor_trigger: result_zaichu]` `[role: 结果]` 灾除结果为灾除的判断。 → 《安身命例》
- `[ns_zwds_j3_180]` `[trigger: 掌三军结果]` `[factor_trigger: result_zhang_sanjun]` `[role: 结果]` 掌三军结果为掌三军的判断。 → 《安身命例》
- `[ns_zwds_j3_181]` `[trigger: 折翅结果]` `[factor_trigger: result_zhechi]` `[role: 结果]` 折翅结果为折翅的判断。 → 《安身命例》
- `[ns_zwds_j3_182]` `[trigger: 正禄结果]` `[factor_trigger: result_zhenglu]` `[role: 结果]` 正禄结果为正禄的判断。 → 《安身命例》
- `[ns_zwds_j3_183]` `[trigger: 贞玉结果]` `[factor_trigger: result_zhenyu]` `[role: 结果]` 贞玉结果为贞玉的判断。 → 《安身命例》
- `[ns_zwds_j3_184]` `[trigger: 中正结果]` `[factor_trigger: result_zhongzheng]` `[role: 结果]` 中正结果为中正的判断。 → 《安身命例》
- `[ns_zwds_j3_185]` `[trigger: 尊居八位结果]` `[factor_trigger: result_zunju_bawei]` `[role: 结果]` 尊居八位结果为尊居八位的判断。 → 《安身命例》
- `[ns_zwds_j3_186]` `[trigger: 日月组合]` `[factor_trigger: riyue_zuhe]` `[role: 主干]` 日月组合为太阳太阴的组合。 → 《安身命例》
- `[ns_zwds_j3_187]` `[trigger: 双禄双星]` `[factor_trigger: shuanglu_shuangxing]` `[role: 主干]` 双禄双星为双禄双星的配置。 → 《安身命例》
- `[ns_zwds_j3_188]` `[trigger: 水上甲午]` `[factor_trigger: shuishang_jiawu]` `[role: 主干]` 水上甲午为水上甲午的配置。 → 《安身命例》"""
    normalized_text_zh: str = """"""
    subject: str = "安身命例"
    factor_refs: list = ['source_ref', 'rel_ansm_001', 'algo_congyinqiyue', 'rel_ansm_002', 'algo_nishuanming', 'rel_ansm_003', 'algo_shunshanshen', 'rel_ansm_004', 'algo_runyuechuli', 'evi_ansm_001', 'algo_congyinqiyue', 'rule_yuefen_dingwei', 'evi_ansm_002', 'algo_nishuanming', 'rule_shenmig_dingwei', 'concept_life_palace', 'concept_body_palace', 'concept_coordinate']
    
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
        l1_anchor="zw_v1.0.0_安身命例_001_L1",
    )
    version: str = "1.0.0"
