"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.521903
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
    semantic_id="acu_v1.0.0_第二节_曼陀罗作为自性象征___716_718_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 第二节曼陀罗作为自性象征716718(SemanticEntry):
    """
    **原文** (¶716-718, 行10850-10900):

> [716] 从心理学角度看，曼陀罗代表自性——人格的整体，包括意识和无意识...
>
> [717] 曼陀罗的中心通常是最神圣的...
    """
    
    original_text: str = """**原文** (¶716-718, 行10850-10900):

> [716] 从心理学角度看，曼陀罗代表自性——人格的整体，包括意识和无意识...
>
> [717] 曼陀罗的中心通常是最神圣的部分。它可能是空的（表示无形的神性），也可能包含神像、象征或几何图形...
>
> [718] 制作或冥想曼陀罗可以带来心理平衡和内心安宁。这不是偶然的——它是心灵自我调节机制的表达。

**英文释义**:

心理学角度：曼陀罗 = 自性（人格整体，意识+无意识）。中心 = 最神圣部分。中心可能：空（无形神性）或包含神像/象征/几何。制作/冥想曼陀罗 → 心理平衡+内心安宁。这是心灵自我调节机制的表达。

**完整中文诠释**:

**曼陀罗 = 自性**：
- 心理学定义：代表自性
- 自性 = 人格整体（意识+无意识）
- 是个体化的目标象征

**中心的意义**：
- 中心 = 最神圣部分
- 可能是空的（无形神性，bindu）
- 可能包含神像、象征或几何图形
- 代表自性的核心

**治疗效果**：
- 制作曼陀罗 → 心理平衡
- 冥想曼陀罗 → 内心安宁
- 非偶然——心灵自我调节机制

**心灵自我调节**：
- 曼陀罗是自我调节的表达
- 心灵自然趋向整合
- 补偿分裂和混乱
- 是内在的治愈力量

**核心要点**:
- 曼陀罗 = 自性 = 人格整体
- 中心是最神圣部分
- 制作/冥想带来平衡和安宁
- 是心灵自我调节机制的表达

**叙事片段**:
- `[ns_cw9i_XI_004]` `[trigger: 曼陀罗自性]` `[factor_trigger: jung_mandala AND jung_self]` `[role: 主干]` 曼陀罗代表自性——人格整体；制作或冥想带来平衡和安宁，是心灵自我调节机制。→ ¶716-718
- `[ns_cw9i_XI_005]` `[trigger: sacred_center]` `[factor_trigger: jung_mandala AND center_symbolism]` `[role: 条件分支]` Center = most sacred part; may be empty (formless divinity) or contain deity/symbol/geometry. → Structure
- `[ns_cw9i_XI_006]` `[trigger: self_regulation]` `[factor_trigger: jung_mandala AND therapeutic_effect]` `[role: 条件分支]` Creating/meditating on mandala → psychological balance + inner peace; expression of psyche's self-regulation. → Function"""
    normalized_text_zh: str = """"""
    subject: str = "第二节：曼陀罗作为自性象征 (¶716-718)"
    factor_refs: list = ['mandala_self', 'sacred_center', 'self_regulation', 'balance_peace']
    
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
        book_id="archetypes_unconscious",
        chapter="",
        l1_anchor="acu_v1.0.0_第二节_曼陀罗作为自性象征___716_718_001_L1",
    )
    version: str = "1.0.0"
