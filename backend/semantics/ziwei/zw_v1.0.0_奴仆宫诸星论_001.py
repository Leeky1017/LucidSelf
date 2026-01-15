"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.636749
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
    semantic_id="zw_v1.0.0_奴仆宫诸星论_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 奴仆宫诸星论(SemanticEntry):
    """
    #### 原文（断句）：

奴仆宫诸星论。凡看奴仆，先看奴仆宫星曜庙旺、落陷，以定奴仆多寡、得力与否；次看吉星、煞星会照，以分忠诚、怨主、背主、盗财、逃走诸象；又看三方四正与对宫，推其一生得力之仆多寡...
    """
    
    original_text: str = """#### 原文（断句）：

奴仆宫诸星论。凡看奴仆，先看奴仆宫星曜庙旺、落陷，以定奴仆多寡、得力与否；次看吉星、煞星会照，以分忠诚、怨主、背主、盗财、逃走诸象；又看三方四正与对宫，推其一生得力之仆多寡与背主之人多少。星曜庙旺加吉者，奴仆成行，一呼百诺，助主卫家；陷地又逢羊陀火铃空劫等煞者，奴仆难招，即有亦多背主怨主，不得久留。

#### 分字分词释义：

- **奴仆宫**：十二宫之一，古代主家中仆从、佣人、部曲等，现代可引申为下属、团队成员、助理、服务提供者、外包伙伴等各种"助力"角色。
- **成行**：人数成列成行，形容仆从、部属众多。
- **得力**：能办事、可靠，做事有效率，能分担事务压力。
- **背主 / 怨主**：心怀怨气、不尽力，甚至在关键时刻反向消极、拆台或离职跳槽。
- **盗财而走**：以不正当方式取利后离开，如侵占资源、卷款跑路、带走客户或资料等。
- **末年招得**：早年难得助力，晚年才渐渐聚集可靠团队与下属。

#### 规范化释义（primary_lang_explained）：

奴仆宫在古代直接指"仆人、婢女"，现代社会可以视作命主与"下属、团队、服务者"之间的关系与资源。判断时，首先看奴仆宫主星的强弱与庙陷：

- 主星庙旺又有吉星会照，多主命主此生易得得力之人相助，"一呼百诺"，可以建立稳定可靠的团队或外部支持网络；
- 主星陷地又多煞星，则主奴仆少而难求，即使短暂聚集，也容易心怀怨气、背主而去，甚至有盗财、泄密等风险。

其次看吉凶星组合：左右、天魁天钺等吉星会奴仆宫，多主仆从忠厚、愿意护主卫家；羊陀火铃空劫等煞星会合，则多主背主、怨主、盗财而走。再结合时间层次，可见"早年无助、晚年渐得力"，或"初得良人、后遭背叛"等不同命运轨迹。

在现代语境下，奴仆宫可用于观察命主在组织合作中的"支持系统"：是否容易找到可靠的同事、助手与外包伙伴，团队是否稳定，是否容易遇到"猪队友"或被下属拖累。

#### 完整对等诠释（secondary_lang_full·7奴仆宫）：

The Servants Palace is no longer literally about maids and household retainers; in a modern chart it maps to colleagues, employees, collaborators, service providers and anyone who functions as support around the native. Strong, well‑aspected stars here describe someone who can gather capable, loyal helpers, build cohesive teams and benefit from outsourced expertise; when they call, people answer. Weaker or afflicted configurations suggest difficulty in finding reliable assistance: staff turnover is high, people help only halfway, or relationships with subordinates are coloured by resentment and mistrust.

This house also reflects how the native themselves manages and relates to those who assist them. Benefic patterns often correspond to fair treatment, clear expectations and a culture of mutual respect, so that even hard work feels shared. Heavy malefic clusters point to scenarios ranging from petty sabotage and gossip to outright theft of resources, clients or credit, especially when boundaries and systems are loose. In contemporary practice, the Servants Palace is a diagnostic lens for team dynamics and partnership risk: it hints at when to delegate boldly, when to tighten contracts and oversight, and when working lean or solo may be psychologically and financially safer.

#### 核心要点（整理）：

1. **数量多寡**：星曜庙旺加吉，多主助力人数充足；陷地加煞，则助力稀少，往往"各自为战"。
2. **得力程度**：奴仆宫吉者，多得可靠、能干的合作者；煞重者，即使有人相助，也多欠力或办事拖沓。
3. **忠诚与背叛**：吉星主忠诚卫主，煞星主怨主、背主、盗财而走，是团队风险的关键指标。
4. **时间结构**：有的命局早年难以得到支持，晚年才渐渐聚拢可靠伙伴；有的则是早年助力多、后期人心离散。
5. **现代延伸**：从"奴仆"延伸到"同事、下属、服务商"，重点转为团队合作与信任结构，而非阶级关系。

#### 详细解说（提要）：

1. **奴仆宫与事业宫的互动**：官禄宫看事业主线与职位高低，奴仆宫则看团队协作与支持度。事业宫再佳，若奴仆宫煞重，也容易"孤军奋战"，在组织或创业过程中缺乏可靠帮手。
2. **吉凶星对团队文化的影响**：吉星多者，团队氛围相对和谐，成员愿意分担压力、共同承担；煞星重者，团队易有内部矛盾、抱怨、不信任，甚至出现内耗与背叛行为。
3. **个人对下属/服务者的态度**：奴仆宫不仅反映"他人对你"，也折射"你如何对待他人"。部分"怨主"之象，可能源自命主对部属不公、苛责或忽视沟通。从现代视角看，应通过改善管理方式来化解部分凶象。
4. **外包与合作伙伴的风险**：现代许多支持不再是住家的"仆人"，而是短期合作、外包团队、供应商等。奴仆宫煞重，提示在签约、款项、信息安全等方面要做好边界与风控，不宜过度信任无保障的关系。

#### 校勘与字词辨析：

- **奴仆**：古义为仆从、婢女，现代不宜按字面使用，可理解为"下属/助力"。
- **一呼百诺**：形容声望高、号召力强，一声召唤，应者云集。
- **败主之奴**：为主带来损失或坏名声的部属，可泛指拖累团队的人。
- **盗财而走**：侵占财物或资源后离开，现代可指贪污、带走客户或资料等。
- **怨主**：对上位者心怀抱怨、情绪不满，易在暗中抵触。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："天府太阳守奴仆，奴仆成行助主荣，一呼百诺皆归顺，终身得力不须忧。"此句常用于吉星守奴仆宫的上佳格局描述，象征团队稳定、助力充足。
- **反面叙事**："七杀羊陀临奴仆，奴背主来仆欺君，盗财走物常有事，孤身独行难成功。"此句警示煞星重临奴仆宫的团队风险与背叛危机。
- **现代转化**：某创业者命主奴仆宫紫微左辅同宫，创业二十年来核心团队稳定，员工忠诚度高，多次危机皆因团队齐心而化解。另一命主奴仆宫破军火星同宫，创业期间屡遭合伙人背叛、员工携款潜逃，验证"背主盗财"的警示。"""
    normalized_text_zh: str = """"""
    subject: str = "奴仆宫诸星论"
    factor_refs: list = ['palace_servants', 'pattern_yihubainuo', 'pattern_beizhu', 'pattern_daocai', 'pattern_monianzhao', 'source_ref', 'rel_nupu_001', 'star_tianfu', 'rel_nupu_002', 'group_liusha', 'rel_nupu_003', 'pattern_monianzhao', 'evi_nupu_001', 'star_tianfu', 'rule_nupu_tianfu', 'evi_nupu_002', 'group_liusha', 'rule_nupu_sha', 'concept_support', 'concept_loyalty']
    
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
        l1_anchor="zw_v1.0.0_奴仆宫诸星论_001_L1",
    )
    version: str = "1.0.0"
