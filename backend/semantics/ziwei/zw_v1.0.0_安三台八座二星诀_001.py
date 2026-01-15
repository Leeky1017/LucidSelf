"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654202
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
    semantic_id="zw_v1.0.0_安三台八座二星诀_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 安三台八座二星诀(SemanticEntry):
    """
    **主题**：论本生日安三台八座。

#### 原文（断句）：

三台寻左辅将，初一日加在左辅宫，顺数至本生日安之。八座寻右弼将，初一加在右弼宫，逆数至本生日安之是也。

#### 分字分词释义：

...
    """
    
    original_text: str = """**主题**：论本生日安三台八座。

#### 原文（断句）：

三台寻左辅将，初一日加在左辅宫，顺数至本生日安之。八座寻右弼将，初一加在右弼宫，逆数至本生日安之是也。

#### 分字分词释义：

- **三台**：杂曜之一，象征台阁、高位、辅政。
- **寻左辅将**：以左辅所在宫位为起点。
- **初一日加在左辅宫**：每月初一对应左辅宫。
- **顺数至本生日**：顺时针数到命主出生日期。
- **八座**：杂曜之一，象征要职、朝班、职位。
- **逆数**：逆时针方向数。

#### 安星规则：

- **三台**：初一在左辅宫，顺数至生日
- **八座**：初一在右弼宫，逆数至生日

#### 规范化释义（primary_lang_explained）：

三台、八座是依附左辅、右弼而安放的两颗台阁贵星，象征“站在权力核心附近、辅佐主事”的位置。安星歌诀说：三台以左辅宫为起点，从每月初一顺数到本生日安星；八座以右弼宫为起点，从初一逆数到本生日安星。一顺一逆，仿佛在出生之日于命盘上画出一对高位辅佐之星，标记命主一生有无机会靠近决策中心。

实务中，三台八座落入命宫、官禄宫或迁移宫，多主易居要职、近权近贵，适合在组织中担任枢纽角色；落入福德、田宅等宫，则偏向生活品质与精神层面的“位置体面”。若再与魁钺、辅弼、禄权科等吉星同会，则台阁气息更重，象征凭专业与品格进入决策层。安星规则只是给出几何位置，是否真能成就“台阁之贵”，仍要视整盘格局与行运高低而定。

#### 完整对等诠释（secondary_lang_full·18三台八座）：

Santai and Bazuo are a pair of courtly stars that extend the influence of Zuo Fu and You Bi, pointing to proximity to power rather than power itself. The rule states that Santai is found by placing the first day of the month in the Zuo Fu palace and counting forward to the day of birth, while Bazuo is found by placing the first day in the You Bi palace and counting backward to the birthday. This one-forward, one-backward motion inscribes a pair of dignified support points into the chart, marking where the native is most likely to stand close to decision-makers.

In interpretation, Santai and Bazuo in the Life, Career or Travel palaces often describe people who circulate near authority—senior aides, specialists at the centre of complex projects or figures who bridge leaders and the wider organisation. When they fall in the Fortune or Property palaces, they lean more toward refined lifestyle, cultural capital and a sense of standing in a "good seat in the hall". When supported by stars such as Kui, Yue, Zuo, You or stars of rank and honours, the configuration can lift the native into positions where being articulate, poised and aesthetically sensitive is precisely what grants access to influential rooms.

#### L2-术语对齐（Term Glossary·六列）：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 三台 | Santai | 依左辅顺数生日主台阁辅政 | From Zuofu forward birthday terrace | star_santai | existing |
| 八座 | Bazuo | 依右弼逆数生日主要职 | From Youbi backward birthday office | star_bazuo | existing |
| 台阁清要 | High Court Dignity | 靠近决策核心兼具名望责任 | Near decision-making prestige | concept_taigeqingyao | new_candidate |
| 辅佐格局 | Supporting-Court Pattern | 台座与辅弼魁钺同会 | Santai-Bazuo with assistant honours | pattern_fuzuogeju | new_candidate |

#### 详细解说：

三台与八座是紫微斗数杂曜系统中的两颗"台阁星"，它们依附于左辅、右弼而定位，象征高位辅政、近权近贵的气象。

**算法原理**：
- 三台的位置依据左辅宫：初一在左辅宫，顺时针数到生日
- 八座的位置依据右弼宫：初一在右弼宫，逆时针数到生日
- 必须先确定左辅、右弼的位置，才能安放三台、八座

**三台与八座的象征意义**：
- **三台**：象征君侧之臣、台阁要员，主正面辅政、得君信任
- **八座**：象征朝班要职、列席高位，主侧面辅助、职位体面

**重要格局**：
- **台座入命**：三台或八座入命宫，主人有辅政之才，易近权贵
- **台座入官禄**：入官禄宫，主职场易居要职，得上司信任
- **台座配魁钺**：与天魁天钺同会，台阁气息更重，主凭专业进入核心圈

**现代应用**：
三台八座可延伸为"核心圈层"的指标。入命或官禄的人，往往容易成为团队的枢纽人物、领导的左膀右臂。

#### 校勘与字词辨析（bilingual）：

- **"三台"**：古代天文中的三台星，引申为朝廷高位。英文："Santai, Triple-Terrace Star, referring to high court position"。
- **"八座"**：古代八个高级官职的统称，引申为要职。英文："Bazuo, Eight-Seats Star, referring to important offices"。
- **"台阁"**：古代指中央政府的核心机构，引申为高级幕僚职位。英文："terrace and court, referring to central government elite"。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："三台寻左辅，八座觅右弼，台阁清要贵，辅政近君侧。"此诀概括了三台八座依附辅弼的定位方法。
- **台阁之贵**：古人云"台座入命，辅政有方"，形容三台八座入命的人有辅佐君主的才能与机会。
- **现代应用**：三台八座在现代可用于评估"成为核心团队成员"的潜力。入命或官禄的人，往往擅长在组织中担任枢纽角色，协调各方资源。"""
    normalized_text_zh: str = """"""
    subject: str = "安三台八座二星诀"
    factor_refs: list = ['source_ref', 'rel_taizuo_001', 'star_zuofu', 'rel_taizuo_002', 'star_youbi', 'rel_taizuo_003', 'star_santai', 'evi_taizuo_001', 'star_santai', 'rule_santai_dingwei', 'evi_taizuo_002', 'star_bazuo', 'rule_bazuo_dingwei', 'concept_terrace_star', 'concept_office_star']
    
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
        l1_anchor="zw_v1.0.0_安三台八座二星诀_001_L1",
    )
    version: str = "1.0.0"
