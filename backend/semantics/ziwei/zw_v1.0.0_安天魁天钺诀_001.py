"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654089
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
    semantic_id="zw_v1.0.0_安天魁天钺诀_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 安天魁天钺诀(SemanticEntry):
    """
    **主题**：论本生年干安天魁天钺。

#### 原文（断句）：

甲戊庚牛羊，乙巳鼠猴乡。六辛逢马虎，壬癸兔蛇藏。丙丁猪鸡位，此是贵人方。

#### 分字分词释义：

- **甲戊庚牛羊**：甲年...
    """
    
    original_text: str = """**主题**：论本生年干安天魁天钺。

#### 原文（断句）：

甲戊庚牛羊，乙巳鼠猴乡。六辛逢马虎，壬癸兔蛇藏。丙丁猪鸡位，此是贵人方。

#### 分字分词释义：

- **甲戊庚牛羊**：甲年、戊年、庚年生人，天魁在丑（牛），天钺在未（羊）。
- **乙己鼠猴乡**：乙年、己年生人，天魁在子（鼠），天钺在申（猴）。
- **六辛逢马虎**：辛年生人，天魁在午（马），天钺在寅（虎）。
- **壬癸兔蛇藏**：壬年、癸年生人，天魁在卯（兔），天钺在巳（蛇）。
- **丙丁猪鸡位**：丙年、丁年生人，天魁在亥（猪），天钺在酉（鸡）。
- **贵人方**：贵人所在的位置，即天魁天钺安放的宫位。

#### 规范化释义（primary_lang_explained）：

甲戊庚牛羊乙巳鼠猴乡。六辛逢马虎壬癸兔蛇藏。丙丁猪鸡位此是贵人方。

#### 安星规则：

| 生年天干 | 天魁 | 天钺 |
|---------|------|------|
| 甲 | 丑(牛) | 未(羊) |
| 乙 | 子(鼠) | 申(猴) |
| 丙 | 亥(猪) | 酉(鸡) |
| 丁 | 亥(猪) | 酉(鸡) |
| 戊 | 丑(牛) | 未(羊) |
| 己 | 子(鼠) | 申(猴) |
| 庚 | 丑(牛) | 未(羊) |
| 辛 | 午(马) | 寅(虎) |
| 壬 | 卯(兔) | 巳(蛇) |
| 癸 | 卯(兔) | 巳(蛇) |

#### 完整对等诠释（secondary_lang_full·8天魁天钺）：

The Tiankui–Tianyue rule places a noble pair of stars from the birth‑year stem. It follows the traditional Heavenly Noble scheme that groups the ten stems into sets and assigns each set a fixed pair of houses: Jia, Wu and Geng years send Tiankui to Chou and Tianyue to Wei; Yi and Ji years send them to Zi and Shen; Bing and Ding years to Hai and You; Xin years to Wu and Yin; Ren and Gui years to Mao and Si. Once the year stem is known, the relevant pair of houses is determined immediately.

Taken together, Tiankui and Tianyue describe the presence of patrons, exam luck and hereditary blessing. Tiankui leans toward visible, yang‑style favour—success in competitive selection, high marks, public recognition—while Tianyue leans toward yin‑style protection, family backing, quiet sponsorship and doors that open because of lineage or connections. When they flank the Life Palace or join other benefics, they support scholarly achievement, dignified posts and a sense of being “born under a lucky star”. When heavily afflicted or placed in awkward houses, they instead show where expectations of help may be frustrated or where borrowed privilege comes with obligations.

#### L2-术语对齐（Term Glossary·六列）：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 天魁 | Tiankui | 主科举显达的阳贵星 | Yang-nobility examination prominence | star_tiankui | existing |
| 天钺 | Tianyue | 主荫封提携的阴贵星 | Yin-nobility hereditary promotion | star_tianyue | existing |
| 天乙贵人 | Heavenly-Yi Noble | 魁钺的定位依据 | Positioning basis for Tiankui-Tianyue | principle_tianyiguiren | existing |
| 坐贵向贵 | Sitting-Facing-Noble | 魁钺夹命的贵格 | Noble pattern flanking Life | combo_zuoguixianggui | new_candidate |
| 科甲福荫 | Exam-Blessings | 科名功名与福荫庇佑 | Scholarly and hereditary blessings | concept_kejiafuyin | new_candidate |

#### 详细解说：

天魁天钺是六吉星中专主科名与贵人的一对星曜。它们依据生年天干安放，体现了年干对命盘贵人运与考试运的影响。

**算法特点**：
- 天魁天钺的定位完全依据"天乙贵人"口诀
- 十个天干被分为五组，每组对应固定的两个宫位
- 天魁为阳贵，天钺为阴贵，两星总是成对出现在不同宫位

**天魁与天钺的区别**：
- **天魁**：主阳贵、科甲贵人，代表通过考试、竞争、公开选拔获得的功名与机会
- **天钺**：主阴贵、福荫贵人，代表通过家族背景、人脉关系、暗中提携获得的机会

**重要格局**：
- **坐贵向贵**：命宫与迁移宫分别有天魁天钺，主贵人缘极佳
- **魁钺夹命**：天魁天钺分别在命宫前后宫位，主一生得贵人扶持
- **魁钺会昌曲**：与文昌文曲同宫或会照，主科名显达

**与"天乙贵人"的关系**：
此歌诀与八字命理中的"天乙贵人"口诀相同，体现了紫微斗数与八字命理的共同根源。

#### 校勘与字词辨析（bilingual）：

- **"牛羊"**：指丑宫（牛）和未宫（羊），是十二地支的生肖表示法。英文："Chou (Ox) and Wei (Goat) palaces"。
- **"六辛"**：指辛年，"六"为虚词，表示强调。英文："Xin year (the sixth emphasis is rhetorical)"。
- **"贵人方"**：贵人所在的方位，即命盘中吉利的位置。英文："the direction where noble persons are located"。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："甲戊庚牛羊，乙己鼠猴乡，丙丁猪鸡位，壬癸兔蛇藏，六辛逢马虎，此是贵人方。"这是最常见的贵人口诀版本，与八字命理共用。
- **科举渊源**：天魁天钺的"科甲"之名源于古代科举制度，魁指"魁首"（第一名），钺指"恩荫"（靠关系获得官职）。
- **现代应用**：现代解读中，天魁可延伸为考试录取、公开选拔、竞争性机会；天钺可延伸为家族资源、人脉介绍、内部推荐等非竞争性机会。

**L2 叙事素材层（规范格式）**：

- `[ns_zwds_j3_049]` `[trigger: 魁钺定位算法]` `[factor_trigger: algo_kuiyuedingwei]` `[role: 主干]` 魁钺定位算法为根据生年天干安放天魁天钺的算法。 → 《安天魁天钺星例》
- `[ns_zwds_j3_050]` `[trigger: 天乙贵人原理]` `[factor_trigger: principle_tianyiguiren]` `[role: 主干]` 天乙贵人原理为魁钺定位的理论依据。 → 《安天魁天钺星例》
- `[ns_zwds_j3_051]` `[trigger: 坐贵向贵格]` `[factor_trigger: combo_zuoguixianggui]` `[role: 条件分支]` 坐贵向贵格为魁钺夹命的贵人格局。 → 《安天魁天钺星例》
- `[ns_zwds_j3_052]` `[trigger: 魁钺会昌曲]` `[factor_trigger: combo_kuiyuehuichangqu]` `[role: 条件分支]` 魁钺会昌曲为魁钺与昌曲同宫或会照的配置，主科名显达。 → 《安天魁天钺星例》
- `[ns_zwds_j3_053]` `[trigger: 科甲福荫]` `[factor_trigger: concept_kejiafuyin]` `[role: 主干]` 科甲福荫为科名功名与福荫庇佑的合称。 → 《安天魁天钺星例》
- `[ns_zwds_j3_054]` `[trigger: 甲戊庚年魁钺]` `[factor_trigger: algo_jiawugeng_kuiyue]` `[role: 条件分支]` 甲戊庚年天魁在丑、天钺在未。 → 《安天魁天钺星例》"甲戊庚牛羊""""
    normalized_text_zh: str = """"""
    subject: str = "安天魁天钺诀"
    factor_refs: list = ['source_ref', 'rel_kuiyue_001', 'principle_tianyiguiren', 'rel_kuiyue_002', 'principle_tianyiguiren', 'rel_kuiyue_003', 'star_tiankui', 'evi_kuiyue_001', 'star_tiankui', 'rule_kuiyue_jiawugeng', 'evi_kuiyue_002', 'star_tianyue', 'rule_kuiyue_bingding', 'concept_noble_star', 'concept_exam_luck', 'concept_hereditary']
    
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
        l1_anchor="zw_v1.0.0_安天魁天钺诀_001_L1",
    )
    version: str = "1.0.0"
