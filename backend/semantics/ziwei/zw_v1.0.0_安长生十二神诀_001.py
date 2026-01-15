"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654250
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
    semantic_id="zw_v1.0.0_安长生十二神诀_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 安长生十二神诀(SemanticEntry):
    """
    **主题**：长生、沐浴、冠带、临官、帝旺、衰、病、死、墓、绝、胎、养十二神。

#### 原文（断句）：

男命顺，女命逆。火局命寅起长生，木局命亥起长生，土局命申起长生，金局命巳起长生，水局命申起...
    """
    
    original_text: str = """**主题**：长生、沐浴、冠带、临官、帝旺、衰、病、死、墓、绝、胎、养十二神。

#### 原文（断句）：

男命顺，女命逆。火局命寅起长生，木局命亥起长生，土局命申起长生，金局命巳起长生，水局命申起长生。

#### 分字分词释义：

- **长生十二神**：描述生命周期十二个阶段的神煞系统。
- **男命顺**：男命从长生起点顺时针排布。
- **女命逆**：女命从长生起点逆时针排布。
- **火局命**：纳音五行属火的命盘。
- **寅起长生**：从寅宫开始安放长生。
- **木局命亥起**：纳音五行属木的命盘从亥宫起长生。
- **土局命申起**：纳音五行属土的命盘从申宫起长生。
- **金局命巳起**：纳音五行属金的命盘从巳宫起长生。
- **水局命申起**：纳音五行属水的命盘从申宫起长生。

#### 安星规则（男命顺、女命逆）：

| 纳音五行 | 长生起点 | 顺序 |
|---------|---------|------|
| 火局 | 寅 | 寅卯辰巳午未申酉戌亥子丑 |
| 木局 | 亥 | 亥子丑寅卯辰巳午未申酉戌 |
| 土局 | 申 | 申酉戌亥子丑寅卯辰巳午未 |
| 金局 | 巳 | 巳午未申酉戌亥子丑寅卯辰 |
| 水局 | 申 | 申酉戌亥子丑寅卯辰巳午未 |

#### 十二神含义：

1. 长生：新生开始
2. 沐浴：桃花位
3. 冠带：成长阶段
4. 临官：事业起步
5. 帝旺：最旺盛
6. 衰：开始衰退
7. 病：疾病困顿
8. 死：死绝之地
9. 墓：入墓封藏
10. 绝：绝地无生
11. 胎：孕育萌芽
12. 养：休养生息

#### 完整对等诠释（secondary_lang_full·23长生十二神）：

The Changsheng Twelve Phases system tracks how vital qi rises, flourishes, declines and returns to incubation as it circulates through the twelve Earth Branches. For each elemental frame of the natal chart—Fire, Wood, Earth, Metal or Water—it designates one branch as the starting palace of Changsheng, or Birth, and then walks through a fixed cycle of twelve stages: Bath, Sash and Cap, Official Rank, Sovereign Prosperity, Decline, Sickness, Death, Tomb, Extinction, Womb and Nurture. Projected onto the houses of the chart, this sequence shows whether a given area of life is just beginning, at full strength, exhausted, sealed away or quietly gestating something new.

Placement is determined by the Nayin five-element frame and by gender. Fire-frame charts take Yin as the Changsheng starting point, Wood charts start from Hai, Earth charts from Shen, Metal charts from Si, and Water charts again from Shen. From that starting branch, male charts count forward around the zodiac, while female charts count in reverse. In practice, the practitioner first identifies the elemental frame, locates the appropriate starting branch, and then, by counting along the ring of twelve Branches, assigns one of the twelve phases to each house or star cluster.

Each of the twelve names signals a distinct life-stage metaphor. Changsheng marks the first emergence of vitality; Bath is both a tender, vulnerable phase and a peach-blossom position associated with attraction and entanglement; Sash and Cap describe growth and social presentation; Official Rank marks the first assumption of responsibility; Sovereign Prosperity is the peak of power and visibility. Decline, Sickness, Death and Tomb describe the waning and cessation of force; Extinction is a place where a cycle has truly run out; Womb and Nurture describe new seeds hidden below the surface and the quiet recuperation that prepares the next turn of the wheel. In delineation, Changsheng, Official Rank and Sovereign Prosperity are treated as especially fortunate positions, Extinction, Death and Tomb as harsh, Bath as alluring but risky, while Womb and Nurture emphasise transition, incubation and rest.

#### L2-术语对齐（Term Glossary·六列）：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 长生 | Changsheng | 新生开始的阶段 | Initial stage of new life | phase_changsheng | existing |
| 沐浴 | Miyu | 桃花位易招桃花 | Peach-blossom romantic entanglements | phase_muyu | existing |
| 冠带 | Guandai | 成长阶段易有成就 | Growth stage achievements | phase_guandai | existing |
| 临官 | Linguan | 事业起步易有官禄 | Career starting point | phase_linguan | existing |
| 帝旺 | Diwang | 最旺盛的阶段 | Most prosperous stage | phase_diwang | existing |
| 衰 | Shuai | 开始衰退的阶段 | Initial decline stage | phase_shuai | existing |
| 病 | Bing | 疾病困顿的阶段 | Sickness hardship stage | phase_bing | existing |
| 死 | Si | 死绝之地 | Death extinction stage | phase_si | existing |
| 墓 | Mu | 入墓封藏的阶段 | Burial sealing stage | phase_mu | existing |
| 绝 | Jue | 绝地无生的阶段 | Extinction stage | phase_jue | existing |
| 胎 | Tai | 孕育萌芽的阶段 | Incubation stage | phase_tai | existing |
| 养 | Yang | 休养生息的阶段 | Rest recuperation stage | phase_yang | existing |

#### 详细解说：

长生十二神是紫微斗数中描述生命周期的重要系统，它将生命分为十二个阶段，从"长生"到"养"循环往复，象征万物生长消亡的自然规律。

**算法原理**：
- 首先确定命主的纳音五行（火、木、土、金、水）
- 根据五行确定长生起点：火寅、木亥、土申、金巳、水申
- 男命从起点顺时针排布，女命从起点逆时针排布
- 依次安放：长生、沐浴、冠带、临官、帝旺、衰、病、死、墓、绝、胎、养

**十二阶段的吉凶分类**：
- **吉阶**：长生（新生）、冠带（成长）、临官（事业起步）、帝旺（最旺盛）
- **凶阶**：病（疾病）、死（死绝）、墓（封藏）、绝（绝地）
- **中性/特殊**：沐浴（桃花位）、衰（开始衰退）、胎（孕育）、养（休养）

**沐浴位的特殊含义**：
沐浴又称"桃花位"，象征情感魅力与吸引力，但也容易招惹是非。入命的人往往人缘好但情感复杂。

**现代应用**：
长生十二神可用于评估人生各阶段的能量状态，如事业发展期、瓶颈期、转型期等。

#### 校勘与字词辨析（bilingual）：

- **"长生"**：生命的开始阶段，象征新生与活力。英文："Changsheng, Birth phase, symbolizing new life and vitality"。
- **"沐浴"**：洗浴之象，引申为桃花位。英文："Miyu, Bath phase, also known as Peach Blossom position"。
- **"帝旺"**：帝王般的旺盛，最强盛的阶段。英文："Diwang, Sovereign Prosperity, the peak of power"。
- **"纳音五行"**：六十甲子纳音所属的五行属性。英文："Nayin Five Elements, the elemental frame derived from the sexagenary cycle"。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："长生沐浴冠带临，帝旺衰病死墓循，胎养复回长生位，生死循环永不停。"此诀概括了长生十二神的完整周期。
- **桃花沐浴**：古人云"沐浴桃花最风流，人缘好来是非多"，形容沐浴位的双面性。
- **生旺死绝**：古人以"长生临官帝旺"为三吉，"死墓绝"为三凶，"沐浴"为桃花，其余为中性。
- **现代应用**：长生十二神在现代可用于评估人生周期与能量状态。帝旺期适合扩张，墓绝期适合收敛转型。"""
    normalized_text_zh: str = """"""
    subject: str = "安长生十二神诀"
    factor_refs: list = ['source_ref', 'rel_changsheng_001', 'principle_nayinwuxing', 'rel_changsheng_002', 'principle_nannvshunni', 'rel_changsheng_003', 'phase_changsheng', 'evi_changsheng_001', 'system_changsheng12', 'rule_changsheng_huo', 'evi_changsheng_002', 'system_changsheng12', 'rule_changsheng_direction', 'concept_life_cycle', 'concept_peach_blossom']
    
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
        l1_anchor="zw_v1.0.0_安长生十二神诀_001_L1",
    )
    version: str = "1.0.0"
