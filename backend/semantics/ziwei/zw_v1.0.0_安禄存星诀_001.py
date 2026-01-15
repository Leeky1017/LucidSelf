"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654111
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
    semantic_id="zw_v1.0.0_安禄存星诀_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 安禄存星诀(SemanticEntry):
    """
    **主题**：论本生年干安禄存。

#### 原文（断句）：

甲生禄存在寅寫，乙生在卯，丙戊巳，丁己禄存停午方，庚禄居申，辛禄酉，壬禄在亥，癸禄子。

#### 分字分词释义：

- **禄存**：...
    """
    
    original_text: str = """**主题**：论本生年干安禄存。

#### 原文（断句）：

甲生禄存在寅寫，乙生在卯，丙戊巳，丁己禄存停午方，庚禄居申，辛禄酉，壬禄在亥，癸禄子。

#### 分字分词释义：

- **禄存**：紫微斗数中主正财俸禄的福禄星，是财运的核心指标。
- **甲生禄存在寅宫**：甲年生人，禄存安放在寅宫。
- **丙戊巳**：丙年和戊年生人，禄存都在巳宫。
- **丁己禄存停午方**：丁年和己年生人，禄存安放在午宫。
- **庚禄居申**：庚年生人，禄存在申宫。
- **辛禄酉**：辛年生人，禄存在酉宫。
- **壬禄在亥，癸禄子**：壬年禄存在亥宫，癸年禄存在子宫。

#### 规范化释义（primary_lang_explained）：

甲生禄存在寅宫乙生在卯丙戊巳丁己禄存停午方庚禄居申辛禄酉壬禄在亥癸禄子。

#### 安星规则：

| 生年天干 | 禄存宫位 |
|---------|---------|
| 甲 | 寅 |
| 乙 | 卯 |
| 丙 | 巳 |
| 丁 | 午 |
| 戊 | 巳 |
| 己 | 午 |
| 庚 | 申 |
| 辛 | 酉 |
| 壬 | 亥 |
| 癸 | 子 |

#### 完整对等诠释（secondary_lang_full·10禄存）：

The Lucun rule fixes the wealth‑salary star directly from the birth‑year stem. Each of the ten stems has a designated “salary position”: Jia years place Lucun in Yin, Yi in Mao, Bing and Wu in Si, Ding and Ji in Wu, Geng in Shen, Xin in You, Ren in Hai and Gui in Zi. Once the stem is known, Lucun’s palace is constant and becomes a structural reference for other techniques.

Lucun represents orthodox income, stipends, food, clothing and stable resources. Where it sits in the chart shows the field through which dependable wealth is most likely to flow. When it combines with Tianma, the celebrated “salary and horse galloping together” configuration describes fortunes made in motion—through travel, trade, transport or any work that thrives on movement. When Lucun occupies the Wealth Palace or receives further benefics it often signals solid finances and the capacity to accumulate; under heavy affliction it can instead mark anxiety about livelihood. In many schools the position of Lucun is also used as the anchor for placing malefic stars such as Qingyang and Tuoluo, so its location quietly shapes both opportunity and risk.

#### L2-术语对齐（Term Glossary·六列）：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 禄存 | Lucun | 主正财俸禄的福禄星 | Fortune-salary orthodox wealth | star_lucun | existing |
| 十干禄位 | Ten-Stems Salary-Positions | 十天干各有禄位 | Each stem has salary position | principle_shiganluweu | existing |
| 禄马交驰 | Salary-Horse Galloping | 禄存天马交会的大吉格 | Supreme wealth Lucun-Tianma | combo_lumajiaochi | existing |
| 双禄重逢 | Dual-Salary Convergence | 禄存遇化禄加倍财运 | Amplified prosperity | combo_shuangluchongfeng | new_candidate |
| 禄前羊禄后陀 | Sheep-Before Tuoluo-After | 擎羊陀罗的定位基准 | Positioning for Qingyang-Tuoluo | principle_luqianyanghoutuo | existing |

#### 详细解说：

禄存是紫微斗数中最重要的财禄星，依据生年天干直接定位。禄存的位置不仅代表财运的来源，还是六煞星中擎羊、陀罗的定位基准。

**算法原理**：
- 每个天干都有其固定的"禄位"，即该天干所"禄"的地支
- 这一规则与八字命理中的"禄神"完全相同
- 甲禄在寅、乙禄在卯……体现的是天干与地支的本气关系

**禄存的主要象征**：
- **正财象征**：稳定收入、俸禄薪水、正当财源、衣食无忧
- **福禄象征**：福分、寿禄、安稳的物质基础
- **守护象征**：禄存所在宫位往往受到保护，不易破败

**重要格局**：
- **禄马交驰**：禄存与天马同宫或会照，主动中生财，是大吉格局
- **双禄重逢**：禄存与化禄同宫或会照，财运加倍
- **禄存入财帛宫**：主一生财运稳定，不愁衣食

**禄存与羊陀的关系**：
禄存是擎羊、陀罗的定位基准。擎羊在禄存前一宫，陀罗在禄存后一宫，形成"禄前羊、禄后陀"的格局。

#### 校勘与字词辨析（bilingual）：

- **"禄"**：指官员的俸禄，引申为财富、福分。英文："salary, fortune, blessing"。
- **"停午方"**：安放在午宫。英文："placed in Wu palace"。
- **"十干禄位"**：十个天干各自对应的禄位。英文："salary positions for the ten heavenly stems"。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："甲禄寅兮乙禄卯，丙戊禄巳丁己午，庚禄申兮辛禄酉，壬禄亥兮癸禄子。"此为最常见的十干禄位口诀，与八字命理共用。
- **禄马交驰**：古人云"禄马最喜交驰，主人发福"，形容禄存与天马同宫时财运亨通的特点。
- **现代应用**：现代解读中，禄存可延伸为固定工资、稳定收入、不动产收益等"正财"类型的财富来源。"""
    normalized_text_zh: str = """"""
    subject: str = "安禄存星诀"
    factor_refs: list = ['source_ref', 'rel_lucun_001', 'principle_shiganluweu', 'rel_lucun_002', 'star_lucun', 'rel_lucun_003', 'star_lucun', 'evi_lucun_001', 'star_lucun', 'rule_lucun_jia', 'evi_lucun_002', 'star_lucun', 'rule_lucun_bingwudingji', 'concept_salary_star', 'concept_orthodox_wealth']
    
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
        l1_anchor="zw_v1.0.0_安禄存星诀_001_L1",
    )
    version: str = "1.0.0"
