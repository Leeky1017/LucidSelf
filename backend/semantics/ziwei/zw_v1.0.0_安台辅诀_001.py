"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654231
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
    semantic_id="zw_v1.0.0_安台辅诀_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 安台辅诀(SemanticEntry):
    """
    **主题**：论本生时安台辅。

#### 原文（断句）：

从午宫起子，顺数至本生时安之。

#### 分字分词释义：

- **台辅**：杂曜之一，象征辅政、台阁、贵显。
- **从午宫起子**：...
    """
    
    original_text: str = """**主题**：论本生时安台辅。

#### 原文（断句）：

从午宫起子，顺数至本生时安之。

#### 分字分词释义：

- **台辅**：杂曜之一，象征辅政、台阁、贵显。
- **从午宫起子**：以午宫作为子时的起点。
- **顺数**：顺时针方向数。
- **本生时**：命主出生的时辰。
- **安之**：安放此星。

#### 安星规则：

- 午宫起子时，顺数至生时

#### 规范化释义（primary_lang_explained）：

台辅是一颗专门依本生时安放的贵显辅政星，歌诀“从午宫起子，顺数至本生时安之”说明：先将午宫视为子时起点，再按十二时辰顺数到命主出生之时，落点所在宫位即为台辅之所。它不像主星那样直接主事业类型，而是标记命主在何处更有机会“贴近权力、以辅佐之姿参与决策”。

实务中，台辅落入官禄宫、命宫或迁移宫，多主易近权贵、居要津之职，适合在组织结构中担任枢纽角色，如幕僚、参谋、高层助理、项目统筹等；落入福德、田宅等宫，则台阁之气更多体现在生活资源与精神地位上，象征凭声望与人格赢得尊重。若与三台八座、魁钺、辅弼等同会，则“辅政大臣”的象意更浓，但仍需结合本命官禄格局与行运强弱判断能否真正承载高位责任，而不只是短暂靠近权力中心。

#### 完整对等诠释（secondary_lang_full·21台辅）：

Taifu is an assisting star placed purely by the birth hour. The rule reads “start from Wu and count from Zi to the native’s hour”, which means we treat the Wu palace as hosting Zi hour and then move forward through the twelve time branches until we reach the person’s birth hour; whichever house we land in becomes the seat of Taifu. Rather than defining career type on its own, this star marks where someone is more likely to stand close to power and participate in decisions from a supporting position.

In practice, Taifu in the Career, Life or Travel palaces often shows people who work as advisors, chiefs of staff, key coordinators or trusted intermediaries between leaders and the wider system. When it falls in the Fortune or Property palaces, its terrace-like quality appears more as social standing and quality of life, indicating resources and respect earned through reliability and competence. When Taifu joins Santai, Bazuo, Kui, Yue or the assistant stars, the pattern can correspond to roles akin to senior aides or policy shapers, but the actual weight of office still depends on the main career configuration and timing. The algorithm simply fixes where the “seat beside the throne” is drawn in each chart; whether someone truly occupies it is another question.

#### L2-术语对齐（Term Glossary·六列）：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 台辅 | Taifu | 午宫起子顺数生时主辅政贵显 | From Wu-Zi by hour supporting dignity | star_taifu | existing |
| 生时锚点 | Birth-Hour Anchor | 以本生时作为安星落点 | Birth hour as anchor for stars | principle_shengshimaodian | existing |
| 贵显系统 | Dignity System | 台辅三台八座等近权星系 | Taifu terraces near authority | system_guixian | new_candidate |
| 辅政角色 | Supporting-Governance Role | 参谋秘书统筹等辅助决策 | Advising coordinating implementing | concept_fuzheng | new_candidate |

#### 详细解说：

台辅是紫微斗数杂曜系统中与"辅政贵显"相关的星曜，它依据出生时辰定位，象征"靠近权力中心的辅助角色"。

**算法原理**：
- 以午宫为子时的起点
- 从午宫顺时针数到命主出生时辰
- 落点宫位即为台辅所在

**台辅的象征意义**：
- 台辅主"辅政"而非"主政"，象征参谋、幕僚、助理等角色
- 入命或官禄的人，容易成为领导身边的核心成员
- 象征凭专业能力和人格魅力赢得信任

**重要格局**：
- **台辅入命官禄**：主易近权贵，担任枢纽角色
- **台辅配三台八座**：台阁气息更浓，辅政之象明显
- **台辅配魁钺**：主得贵人提携，进入核心决策层

**现代应用**：
台辅可延伸为"成为核心团队成员"的指标，如CEO助理、项目经理、高级顾问等职位。

#### 校勘与字词辨析（bilingual）：

- **"台辅"**：古代指台阁辅臣，引申为辅政要员。英文："Taifu, Auxiliary Terrace Star, referring to supporting governance roles"。
- **"午宫起子"**：以午宫作为子时的参照点。英文："Wu palace as the anchor for Zi hour"。
- **"贵显"**：高贵显赫，指靠近权力中心的地位。英文："dignified prominence, referring to proximity to power"。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："台辅午宫起子时，顺数生时便安之，辅政贵人近君侧，幕僚参谋总相宜。"此诀概括了台辅的定位方法与辅政象征。
- **辅政之才**：古人云"台辅入命，辅政有方"，形容台辅入命的人有辅佐领导的才能。
- **现代应用**：台辅在现代可用于评估"成为高管助手"的潜力。入命或官禄的人，往往擅长在组织中担任枢纽角色，协调上下级关系。"""
    normalized_text_zh: str = """"""
    subject: str = "安台辅诀"
    factor_refs: list = ['source_ref', 'rel_taifu_001', 'principle_shengshimaodian', 'rel_taifu_002', 'star_taifu', 'evi_taifu_001', 'star_taifu', 'rule_taifu_dingwei', 'concept_auxiliary_dignity']
    
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
        l1_anchor="zw_v1.0.0_安台辅诀_001_L1",
    )
    version: str = "1.0.0"
