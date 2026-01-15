"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654159
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
    semantic_id="zw_v1.0.0_天空地劫诀_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 天空地劫诀(SemanticEntry):
    """
    **主题**：论本生时安天空地劫。

#### 原文（断句）：

亥上起子顺安劫，逆回便是天空乡。

#### 分字分词释义：

- **亥上起子**：以亥宫为起点，从子时开始计算。
- **顺安劫*...
    """
    
    original_text: str = """**主题**：论本生时安天空地劫。

#### 原文（断句）：

亥上起子顺安劫，逆回便是天空乡。

#### 分字分词释义：

- **亥上起子**：以亥宫为起点，从子时开始计算。
- **顺安劫**：顺时针数到生时，安放地劫。
- **逆回**：逆时针方向数。
- **天空乡**：天空所在的位置。
- **地劫**：六煞星之一，主耗散、破财、突发损失。
- **天空**：六煞星之一，主虚无、落空、不切实际。

#### 安星规则：

- **地劫**：亥宫起子时，顺时针数至生时
- **天空**：亥宫起子时，逆时针数至生时

#### 示例：
- 子时生：地劫亥、天空亥（同宫）
- 丑时生：地劫子、天空戌
- 午时生：地劫巳、天空巳（同宫）

#### 规范化释义（primary_lang_explained）：

 天空、地劫的安星以亥宫为轴心：先在亥宫标记子时，一路顺数到本生时安地劫星，再从同一亥宫起子时逆数到本生时安天空星。一顺一逆，使二星始终围绕同一宫位展开，对应哪一宫的"根基被侵蚀"（地劫）与哪一宫的"上层支持抽离"（天空）。

#### 完整对等诠释（secondary_lang_full·14天空地劫）：

 The Tiankong–Dijie placement rule uses Hai as a fixed anchor. First, mark Zi hour at Hai and count clockwise to the native's birth hour; that palace receives Dijie, the star of erosion and loss. Then, from the same Hai anchor, count counter-clockwise to the birth hour; that palace receives Tiankong, the star of void and withdrawal. This paired, one-forward-one-backward motion keeps the two stars symmetrically arranged around a single axis, clarifying which houses show weakened foundations and which show support being pulled away from above.

#### L2-术语对齐（Term Glossary·六列）：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 天空 | Tiankong | 亥宫逆数安置主落空抽离 | Counter-clockwise from Hai void withdrawal | star_tiankong | existing |
| 地劫 | Dijie | 亥宫顺数安置主侵蚀耗损 | Clockwise from Hai erosion loss | star_dijie | existing |
| 空劫轴心 | Void-Robbery Axis | 以亥宫为中心一顺一逆 | Symmetry axis at Hai | algo_kongjiezhouxin | new_candidate |

#### 详细解说：

天空与地劫是紫微斗数六煞星中的最后两颗，专主空亡与耗散。它们依据生时安放，以亥宫为轴心，一顺一逆，形成对称结构。

**算法原理**：
- 亥宫是天空地劫的共同起点，象征"海"与"虚空"
- 地劫顺行，代表向下的侵蚀与物质层面的损失
- 天空逆行，代表向上的抽离与精神层面的落空

**天空与地劫的性质区别**：
- **地劫**：主物质层面的损失，如财物被劫、投资失败、意外破财。性质偏"实"，损失可见可量化。
- **天空**：主精神层面的落空，如期望落空、计划泡汤、支持撤离。性质偏"虚"，损失难以量化但影响深远。

**重要格局**：
- **空劫夹命**：天空、地劫分别在命宫前后，主一生多有落空与破财
- **空劫入财帛宫**：主财运不稳，容易破财或投资失利
- **空劫逢吉化**：可转化为创意、艺术、宗教方面的发展

**现代应用**：
空劫在现代可理解为投资风险、创业失败、计划落空等。但空劫也有正面意义：空劫入命的人往往思维开阔，不拘泥于物质，适合从事艺术、哲学、宗教等领域。

#### 校勘与字词辨析（bilingual）：

- **"亥上起子"**：以亥宫为子时的起点。英文："starting from Hai palace at Zi hour"。
- **"劫"**：劫夺、抢夺之意，引申为损失。英文："robbery, deprivation, loss"。
- **"空乡"**：空虚之地，指天空所在的宫位。英文："territory of void, position of emptiness"。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："亥上起子顺安劫，逆回便是天空乡。空劫入命多落空，纵有奇谋也枉然。"此诀警示空劫的破财与落空特性。
- **空门悟道**：古人认为空劫入命者"宜僧道"，现代可理解为适合从事不以物质回报为核心的工作，如艺术、研究、公益等。
- **现代应用**：空劫在现代投资理财中可理解为风险指标。空劫入财帛宫的人需要更谨慎的理财策略，避免高风险投资。"""
    normalized_text_zh: str = """"""
    subject: str = "天空地劫诀"
    factor_refs: list = ['source_ref', 'rel_kongjie_001', 'algo_kongjiezhouxin', 'rel_kongjie_002', 'algo_kongjiezhouxin', 'rel_kongjie_003', 'star_tiankong', 'evi_kongjie_001', 'star_dijie', 'rule_dijie_dingwei', 'evi_kongjie_002', 'star_tiankong', 'rule_tiankong_dingwei', 'concept_void_star', 'concept_robbery_star']
    
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
        l1_anchor="zw_v1.0.0_天空地劫诀_001_L1",
    )
    version: str = "1.0.0"
