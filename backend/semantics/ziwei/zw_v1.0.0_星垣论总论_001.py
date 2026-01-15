"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.725431
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
    semantic_id="zw_v1.0.0_星垣论总论_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 星垣论总论(SemanticEntry):
    """
    - 原文（source_text）：

  紫微帝座，以辅弼为佐贰，作数中之主星，乃有用之源流。是以南北二斗，集而成数，为万物之灵。盖以水淘溶，则阴阳既济；水盛阳伤，火盛阴灭，二者不可偏废，故得其中者...
    """
    
    original_text: str = """- 原文（source_text）：

  紫微帝座，以辅弼为佐贰，作数中之主星，乃有用之源流。是以南北二斗，集而成数，为万物之灵。盖以水淘溶，则阴阳既济；水盛阳伤，火盛阴灭，二者不可偏废，故得其中者，斯为美矣。寅乃木之垣，乃三阳交泰之时，草木萌芽之所；至于卯位，其木愈旺矣。贪狼、天机是庙乐，故得天相水到寅，为之旺相；巨门水得卯，为之疏通。木乃土栽培，加以水之浇灌三方，更得文曲水、破军水相会尤妙，又加禄存土，极美矣。巨门水到丑，天梁土到未，陀罗金到于四墓之所，苟或得擎羊金相会，以土为金墓，则金通不凝。加以天府土、天同金以生之，是为金趁土肥，顺其德以生成。未、巳、午乃火位，巳为水土所绝之地，更午垣之火余，气流于巳，水则倒流，火气逆炎，必归于巳。午属火德，能生于巳绝之土，所以廉贞木居焉。至于午火旺照离明，洞彻表里，而文曲水入庙，若会紫府，则魁星拱斗，加以天机木、贪狼火，谓之变景，愈加奇特。申酉金乃西方太白之气，武曲居申而好生，擎羊在酉而用杀，加以巨门、禄存、陀罗而助之愈急，须得逆行，逢善化恶，是为妙用。亥水属文曲、破军之庙地，乃文明清高之士，万里派源之洁，如大川之泽，不为焦枯；居于亥位，将入天河，是故为妙。破军水于子旺之乡，如巨海之浪澎汹涌，可远观而不可近倚，破军是以居焉。若四墓之克，充其弥漫，必得武曲之金，使其源流不绝，方为妙矣。其余诸星，以身命推之，无施不可，至玄至妙者矣。

- 原注（原文注解，可无则省略小节）：

  （本条为《星垣论》总纲，从十二垣位与星曜五行配合的角度，说明命盘“骨架”如何搭建，为后文格局与运限判断提供空间和元素基础。）

- 分字分词释义：

  - **星垣**：以十二地支为垣位，配合星曜庙旺、得地与否及五行属性，构成紫微斗数命盘的空间骨架。
  - **水淘溶，阴阳既济**：以水为媒介，调和阴阳；水盛则伤阳，火盛则伤阴，强调五行不过不及皆为病。
  - **寅乃木之垣……卯位其木愈旺**：寅为三阳交泰、草木萌芽之处，卯为木气极旺之位，为木火生发的主要门户。
  - **四墓之所**：丑、辰、未、戌四墓库，为万物归藏与蓄势之地，金水在此沉潜聚集，待运限激发而发用。
  - **金趁土肥**：金赖肥厚之土以生，命盘中金星得天府、天梁等土星生扶，方能既有锋芒又不致枯竭。
  - **变景**：文曲入庙会紫府、天机、贪狼等星，使原本平常格局在特定垣位与限运下突然跃迁为奇格。

- 规范化释义（primary_lang_explained）：

  本篇以“星垣”为中心，解释十二地支垣位与星曜五行之间的互相配合。紫微帝座居中，以辅弼为佐贰，统摄南北二斗之数，成为数中之主星、诸用之源流。水为阴阳之媒，既能淘溶万物，又能在过盛时伤阳或熄灭火德，因此水火得其中，才是最理想的气象。

  文中先举寅卯木垣为例：贪狼、天机在此庙乐，得天相与巨门之水相资，再得文曲、破军诸水星及禄存土之培植，便形成“木得水土而生发”的佳局，多主有学识、有行动力且能落实的格局。继而论四墓土垣中金水蓄势，若武曲、擎羊等金星得天府、天同等土星培育，则为“金趁土肥”，一方面藏锋，一方面在适当限运中爆发。再论巳午火垣中廉贞、文曲、紫府、天机、贪狼等星组合，构成“变景”之格，在适当时间出现显著的格局跃迁。申酉金垣与亥子水垣则分别体现太白之气与大川之泽，若能在逆行运程中逢善星制化，则可在表面险地中找到妙用。整条意在提醒读者：断命时不可只看星名，更要先看垣位与五行，理解命盘的地形与气候，再谈吉凶成败。

- 完整对等诠释（secondary_lang_full）：

  This chapter builds the notion of “star enclosures” (xingyuan) as the spatial framework of a Ziwei Doushu chart. Ziwei, seated as the imperial star and supported by assistant stars, stands at the centre as the source of all useful configurations, while the Northern and Southern Dippers provide the numerical structure from which myriad patterns arise. The twelve earthly‑branch sectors are treated as enclosures of Wood, Fire, Earth, Metal and Water. Water is described as the medium that washes and blends Yin and Yang: when balanced it brings completion, but when excessive it injures Yang, and when Fire is excessive it burns out Yin. The ideal is not one‑sided strength but a centred harmony where Water and Fire each hold their place.

  The text first uses the Wood enclosures of Yin and Mao as an example. Here Tanlang and Tianji enjoy temple dignity; with Tianxiang and Jumen providing Water support, and with Wenchang, Pojun and other Water stars plus Lu‑cun‑type Earth stars nurturing from below, the configuration becomes “Wood nourished by Water and Earth”, often seen in charts that combine learning, initiative and practical realisation. The four Earth “tombs” of Chou, Chen, Wei and Xu are then presented as storage zones where Metal and Water accumulate. If stars like Wuqu and Qingyang are supported by Earth stars such as Tianfu and Tiantong, this forms “Metal thriving on fertile Earth”: sharpness is hidden and then released at appropriate times rather than exhausted too early.

  Next the Fire enclosures of Si and Wu are discussed, where Lianzhen, Wenchang, Ziwei‑Tianfu, Tianji and Tanlang can combine into so‑called “pattern‑shift” (bianjing) structures. These tend to produce sudden leaps in status or circumstance when the timing is right. The Metal sector of Shen and You represents the western Venusian energy: Wuqu in Shen inclines toward productive action, while Qingyang in You carries killing force; aided by Jumen, Lu Cun and Tuoluo, these combinations are fierce yet can be turned to skilful use if reversed flows and benefic transformations are present. The Water sector of Hai and Zi, associated with Wenchang and Pojun in temple dignity, symbolises clear, cultured currents like a great river that does not dry up; Pojun in Zi is likened to surging ocean waves, impressive at a distance but dangerous up close. In all cases, the chapter insists that one must first read enclosure and element—terrain and climate—before pronouncing on the goodness or badness of any given star.

- 核心要点：

  - 命盘首先要看 **十二垣位与五行骨架**，星曜只是填入其上的“人物与事件”。
  - 水火是调和阴阳的关键因子，“水火得中”比单纯水多火多更重要。
  - 寅卯木垣、四墓土垣、巳午火垣、申酉金垣、亥子水垣，各自构成一套典型的“源星 + 用星 + 五行环境”组合。
  - 妙格常在墓库蓄势与逆行化恶之中，需要懂得"蓄势待发"与"以吉制凶"的用法。

- 叙事素材（narrative_snippets）：

  - **帝座源流**："紫微帝座，以辅弼为佐贰，作数中之主星，乃有用之源流。"此句确立了紫微为命盘核心、辅弼为佐助的基本架构。
  - **阴阳既济**："水淘溶，则阴阳既济；水盛阳伤，火盛阴灭，二者不可偏废。"强调五行平衡的重要性，水火过盛皆为病。
  - **木垣生发**："寅乃木之垣，乃三阳交泰之时，草木萌芽之所。"寅卯木垣为生发之地，贪狼天机得水土相资则格局极美。
  - **金趁土肥**："天府土、天同金以生之，是为金趁土肥，顺其德以生成。"金星得厚土培育，方能既有锋芒又不枯竭。
  - **变景之格**："文曲水入庙，若会紫府，则魁星拱斗，加以天机木、贪狼火，谓之变景，愈加奇特。"火垣组合可产生格局跃迁。
  - **现代应用**：本条可作为命盘"地形图"的解读框架——先看垣位五行，再看星曜组合，理解环境对星性的塑造作用。

  **L2 叙事素材层（规范格式）**：

  - `[ns_zwds_j1_088]` `[trigger: 十四主星体系]` `[factor_trigger: structure_shisizhuxing]` `[role: 主干]` 十四主星为紫微斗数核心星曜，统摄全盘格局。 → 《星垣论》"紫微帝座，以辅弼为佐贰，作数中之主星"
  - `[ns_zwds_j1_089]` `[trigger: 北斗七星]` `[factor_trigger: structure_beidouqixing]` `[role: 主干]` 北斗七星为紫微、贪狼、巨门、禄存、文曲、廉贞、武曲，主阳刚进取。 → 《星垣论》"南北二斗，集而成数"
  - `[ns_zwds_j1_090]` `[trigger: 南斗六星]` `[factor_trigger: structure_nandoliuxing]` `[role: 主干]` 南斗六星为天府、天机、天相、天梁、天同、七杀，主阴柔守成。 → 《星垣论》"南北二斗，集而成数"
  - `[ns_zwds_j1_091]` `[trigger: 紫微定位算法]` `[factor_trigger: algo_ziweidingwei]` `[role: 主干]` 紫微定位为安星之首要步骤，依生年月日定紫微所在宫位。 → 《星垣论》排盘法则
  - `[ns_zwds_j1_092]` `[trigger: 从寅起月算法]` `[factor_trigger: algo_congyinqiyue]` `[role: 主干]` 从寅起月为安命宫之基础算法，正月从寅宫起数。 → 《星垣论》排盘法则
  - `[ns_zwds_j1_093]` `[trigger: 逆数安命算法]` `[factor_trigger: algo_nishuanming]` `[role: 主干]` 逆数安命为定命宫之算法，从生月逆数至生时。 → 《星垣论》排盘法则
  - `[ns_zwds_j1_094]` `[trigger: 顺数安身算法]` `[factor_trigger: algo_shunshanshen]` `[role: 主干]` 顺数安身为定身宫之算法，从生月顺数至生时。 → 《星垣论》排盘法则
  - `[ns_zwds_j1_095]` `[trigger: 闰月处理算法]` `[factor_trigger: algo_runyuechuli]` `[role: 例外处理]` 闰月处理为特殊情况算法，闰月入下月计算。 → 《星垣论》排盘法则
  - `[ns_zwds_j1_096]` `[trigger: 逆序排列算法]` `[factor_trigger: algo_nishupaiilie]` `[role: 主干]` 逆序排列为十二宫安排之算法，命宫起逆时针排列。 → 《星垣论》排盘法则
  - `[ns_zwds_j1_097]` `[trigger: 起五寅算法]` `[factor_trigger: algo_qiwuyin]` `[role: 主干]` 起五寅为定月干之算法，依年干定月干起点。 → 《星垣论》排盘法则
  - `[ns_zwds_j1_098]` `[trigger: 天干五合原理]` `[factor_trigger: principle_tianganwuhe]` `[role: 主干]` 天干五合为甲己/乙庚/丙辛/丁壬/戊癸相合之原理。 → 《星垣论》五行原理
  - `[ns_zwds_j1_099]` `[trigger: 流荡格局]` `[factor_trigger: pattern_liudang]` `[role: 条件分支]` 流荡格局为七杀独守迁移，主一生漂泊流浪。 → 《星垣论》"七杀外出，流荡天涯"
  - `[ns_zwds_j1_100]` `[trigger: 横发横破]` `[factor_trigger: pattern_hengfahengpo]` `[role: 条件分支]` 横发横破为贪狼在财帛庙旺，主财来财去、暴涨暴跌。 → 《星垣论》
  - `[ns_zwds_j1_101]` `[trigger: 祖业格局]` `[factor_trigger: pattern_zuye]` `[role: 条件分支]` 祖业格局为破军在田宅，主破祖离乡、先破后成。 → 《星垣论》
  - `[ns_zwds_j1_102]` `[trigger: 刑克格局]` `[factor_trigger: pattern_xingke]` `[role: 条件分支]` 刑克格局为太阳在父母宫陷地，主先克父亲。 → 《星垣论》
  - `[ns_zwds_j1_103]` `[trigger: 晚年照格局]` `[factor_trigger: pattern_monianzhao]` `[role: 条件分支]` 晚年照格局为星曜组合主晚年得助力。 → 《星垣论》
  - `[ns_zwds_j1_104]` `[trigger: 月柱结构]` `[factor_trigger: structure_yuezhu]` `[role: 主干]` 月柱为八字四柱之一，用于起五寅定月干。 → 《星垣论》排盘结构"""
    normalized_text_zh: str = """"""
    subject: str = "星垣论总论"
    factor_refs: list = ['palace_xingyuan', 'frame_wuxing', 'balance_shuihuo', 'palace_mu', 'palace_huo', 'palace_muku']
    
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
        l1_anchor="zw_v1.0.0_星垣论总论_001_L1",
    )
    version: str = "1.0.0"
