"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.636708
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
    semantic_id="zw_v1.0.0_财帛宫诸星论_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 财帛宫诸星论(SemanticEntry):
    """
    #### 原文（断句）：

财帛宫诸星论。凡看财帛，先看本宫星曜庙旺陷弱，以定一生财运之厚薄；次看吉星、煞星、禄权科忌加会，以别守成、白手、横发、闹中、九流诸般财路；又看三方四正，究其实能聚则富，不能...
    """
    
    original_text: str = """#### 原文（断句）：

财帛宫诸星论。凡看财帛，先看本宫星曜庙旺陷弱，以定一生财运之厚薄；次看吉星、煞星、禄权科忌加会，以别守成、白手、横发、闹中、九流诸般财路；又看三方四正，究其实能聚则富，不能聚则空。若羊陀火铃空劫耗忌重重，会于财帛宫，则主财来财去，东来西去，难以久守。

#### 分字分词释义：

- **财帛宫**：十二宫之一，主钱财收入、财富积累方式、理财习惯与用财观念。
- **丰足仓厢/仓箱**：仓库满溢，比喻家中钱财充裕、积蓄丰厚。
- **白手生财**：并非继承祖业，而是靠自身努力从零开始积累财富。
- **横发/横进之财**：出乎意料、短期暴增的财富，如投机、暴利、意外之财。
- **闹中求财/闹中生财**：在人多事杂、竞争激烈的环境中求财，如市井、商场、市场、演艺场所等。
- **九流人生财**：以非正统、边缘行业或辛杂工作求财，古代指九流技艺、江湖行当等。
- **东来西去/先无后有**：财来财去、财运起伏大，前期辛苦难聚，后期渐有起色。
- **富足仓厢堆金积玉**：财富充盈且能聚守，如同仓库堆满金银财宝。
- **耗忌**：耗星与忌星，主破财消耗、财不聚守。
- **横发横破**：财虽来得突然，亦可能很快破散，难以久留。

#### 规范化释义（primary_lang_explained）：

财帛宫专门论断命主一生的财运格局：有无财、财从何来、易不易聚、何时发、发得快慢稳不稳。判断时，第一要看财帛宫主星庙旺或陷弱，决定基本财运厚薄；第二要看吉星（禄存、左右、昌曲、魁钺等）与煞星（羊陀火铃空劫等）同宫或加会，以分守成、白手、横发、闹中、九流之别；第三要看三方四正与对宫的生克制化，判断财来财去与能否久守。

原文中各星入财帛宫，多有固定象意：
- 紫微、天府等帝星守财帛，多主"丰足仓厢"，一生财源稳定，能聚能守；
- 天机、巨门等主劳心费力求财，多属"劳碌成财"；
- 贪狼、七杀、破军等主"闹中""横发"，财来去猛、起伏极大；
- 禄存、昌曲左右会合，则主堆金积玉、不劳而获或少劳多得；
- 羊陀火铃空劫等煞星会合，则财多成败反复，甚至破祖、贫困。
 
#### 完整对等诠释（secondary_lang_full·4财帛宫）：

The Wealth Palace maps out how a person relates to money across an entire lifetime: whether resources tend to be thick or thin, where income usually comes from, how turbulent the cashflow is, and whether wealth can be accumulated or only passes through the hands. The main star here sets the backbone of the story. Dignified imperial and treasury stars describe charts with solid financial foundations, steady income and the possibility of long‑term accumulation. Hard, combative stars point toward making money through risk, toil, competition or physically demanding work, where earnings may be large but rarely feel effortless. Quick, thinking stars often indicate "earning by using the head and tongue": planning, negotiating, teaching, mediating or running information‑driven businesses.

Auxiliary stars then sort the native’s money path into familiar patterns. Strong, well‑placed benefics support "inherit and keep" or "self‑made but able to store", where savings, assets and buffers gradually build up. Malefic clusters and heavy loss stars, by contrast, underline stories of dramatic rises and falls: sudden windfalls followed by equally sudden collapses, or constant leakage through expenses, relatives, bad deals or lifestyle. Some configurations prefer earning in crowded, noisy, high‑flow environments such as markets, trading floors or entertainment venues; others lean toward more marginal or unconventional trades that demand careful ethical and legal navigation. In a modern reading, the Wealth Palace becomes less a verdict of rich versus poor and more a description of financial style—how much uncertainty one must live with, what kinds of work match the chart’s temperament, and which phases of life are best suited for building, consolidating or restructuring one’s material base.

#### 核心要点（整理）：

1. **财运旺衰**：以主星庙旺陷弱为骨架——庙旺主财厚、基础好；陷弱主财薄、起点低，需要更多努力与机遇。
2. **财源类型**：根据星曜组合分为守成（继承祖业）、白手（靠自身起家）、横发（暴利与投机）、闹中（市井买卖与商场生意）、九流（边缘行业谋财）。
3. **聚散规律**：吉星多则主聚守有力、财可积累；煞星重则主散破，财来财去难以久存。
4. **发财时机**：部分星曜主早发（少年得财）、部分主晚发（中晚年财运渐佳）、部分主前破后成（"先无后有"、"先难后易"）。
5. **得财方式**：除自身劳心劳力外，还包括因贵得财（贵人相助）、因妻得财（妻财同旺）、技艺生财、九流谋财等多种路径。

#### 详细解说：

财帛宫的判断，实质是在描绘命主与金钱的关系模式：

1. **从主星看"有无"与"厚薄"**：
   - 紫微、天府、太阴等庙旺守财帛，多主家中有底子、财源稳定；
   - 武曲、七杀、破军等刚烈之星守财帛，多主以辛勤、冒险、搏杀之道求财；
   - 天机、巨门等多动多思之星，则以智谋、口舌、信息流通求财，"劳心费力生财"。

2. **从吉凶星看"聚散"**：
   - 禄存、左右、昌曲、魁钺等吉星会合时，往往"富足仓厢堆金积玉"，不待多劳财自来；
   - 羊陀火铃空劫等煞星会合时，即便一度横发，往往"横发横破"，大起大落，难以久守。

3. **从环境看"闹静"与"九流"**：
   - "闹中求财"代表需要在复杂、人多、竞争激烈的环境中求财，如商场、市场、投机买卖等；
   - "九流人生财"则提示行业属性偏边缘或不被主流社会认可，需要注意风险与声誉问题。

4. **从时间看"早晚"与"先破后成"**：
   - 贪狼同守、火星会合等，常见"三十年前成败、后三十年横发"的时间结构；
   - 破军、廉贞等多主"先难后易"，需要经历一段破耗、试错之后，方能见财成家。

5. **现代应用的转化**：
   - 古代重视"堆金积玉"与"继承祖业"，现代可转化为财务安全感、资产配置能力；
   - "白手生财"可理解为创业、职业发展、自由职业等多元收入路径；
   - 对"九流人生财"要从合规与道德角度重新审视，避免违法违规的求财方式。

#### 校勘与字词辨析：

- "丰足仓厢/仓箱"中的"仓厢/仓箱"均指储物之所，本稿统一作"仓厢"理解为仓库。
- "闹中求取/闹中生财"中的"闹中"指环境繁杂、人多事众之地，与"清高"相对。
- "白手生财"原义为从零起家，不依赖祖业或他人资助，非"白拿"之意。
- "横发横破"中的"横"指出人意料、非常规路径，既可大赚亦可大亏。
- "九流人"为古代社会对部分技艺者、江湖人士等的统称，现代使用需去除歧视色彩，可理解为"非主流职业"。
- "东来西去"是对财运起伏不定的形象比喻，非真实地理方位。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："紫府武曲守财乡，金银满屋仓厢盈，禄存相会更添喜，一生富足过公卿。"此句常用于财帛宫庙旺吉星聚的上等财格描述，象征财富丰厚、稳定有余。
- **反面叙事**："贪狼火铃临财帛，虽有横财来亦破，东来西去如水流，到老空囊徒劳作。"此句警示贪狼火铃同守财帛宫的"横发横破"特性。
- **现代转化**：某投资人命主财帛宫武曲天府同宫加会禄存，从事金融投资二十余年，资产稳健增长。其理财风格保守稳健，验证"金库星守财能聚"的论断。而另一命主财帛宫贪狼火星同宫，早年创业暴富后因扩张过快破产，后又东山再起，验证"横发横破、闹中求财"的特性。

**L2 叙事素材层（规范格式）**：

- `[ns_zwds_j4_027]` `[trigger: 财帛宫论断]` `[factor_trigger: palace_caibo]` `[role: 主干]` 财帛宫主论财运厚薄与求财方式。 → 《卷四》财帛宫
- `[ns_zwds_j4_028]` `[trigger: 财富丰厚]` `[factor_trigger: caifu_fenghou]` `[role: 结果]` 财富丰厚为财帛宫吉星庙旺的富裕结果。 → 《卷四》"金银满屋仓厢盈"
- `[ns_zwds_j4_029]` `[trigger: 横发横破]` `[factor_trigger: caifu_hengfahengpo]` `[role: 条件分支]` 横发横破为贪狼火铃同守财帛的财运特性。 → 《卷四》"虽有横财来亦破"
- `[ns_zwds_j4_030]` `[trigger: 闹中求财]` `[factor_trigger: qiucai_naozhong]` `[role: 主干]` 闹中求财为在繁杂环境中求财的方式。 → 《卷四》"闹中求财"
- `[ns_zwds_j4_031]` `[trigger: 白手生财]` `[factor_trigger: qiucai_baishouchengcai]` `[role: 主干]` 白手生财为从零起家不依赖祖业的求财方式。 → 《卷四》"白手生财"
- `[ns_zwds_j4_032]` `[trigger: 九流生财]` `[factor_trigger: qiucai_jiuliu]` `[role: 条件分支]` 九流生财为非主流职业求财的方式。 → 《卷四》"九流人生财"
- `[ns_zwds_j4_033]` `[trigger: 结果贵显]` `[factor_trigger: result_gui]` `[role: 结果]` 结果贵显为命盘主贵人扶持地位显达的判断。 → 《卷四》
- `[ns_zwds_j4_034]` `[trigger: 结果寿终]` `[factor_trigger: result_shouzhong]` `[role: 结果]` 结果寿终为寿命长短的判断结果。 → 《卷四》
- `[ns_zwds_j4_035]` `[trigger: 结果命旺]` `[factor_trigger: result_mingwang]` `[role: 结果]` 结果命旺为命格强旺的判断结果。 → 《卷四》"""
    normalized_text_zh: str = """"""
    subject: str = "财帛宫诸星论"
    factor_refs: list = ['palace_wealth', 'pattern_baishoucai', 'pattern_naozhongcai', 'pattern_hengfahengpo', 'pattern_jiuliucai', 'source_ref', 'rel_caibo_001', 'star_tianfu', 'rel_caibo_002', 'group_liusha', 'rel_caibo_003', 'star_tanlang', 'evi_caibo_001', 'star_ziwei', 'rule_caibo_ziwei', 'evi_caibo_002', 'pattern_hengfahengpo', 'rule_caibo_hengfa', 'concept_wealth', 'concept_income_pattern']
    
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
        l1_anchor="zw_v1.0.0_财帛宫诸星论_001_L1",
    )
    version: str = "1.0.0"
