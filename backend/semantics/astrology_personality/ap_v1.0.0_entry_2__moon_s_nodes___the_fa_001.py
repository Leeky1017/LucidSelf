"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238228
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
    semantic_id="ap_v1.0.0_entry_2__moon_s_nodes___the_fa_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry2MoonSNodesTheFa(SemanticEntry):
    """
    **Source Text** (Lines 10041-10175):
> The Moon's Nodes... they differ from the planetary nodes in m...
    """
    
    original_text: str = """**Source Text** (Lines 10041-10175):
> The Moon's Nodes... they differ from the planetary nodes in many ways. First of all they are purely geocentric, and not heliocentric—being the nodes of a satellite...
>
> What is seen therefore through the Moon's nodes is the relation between the "human" will and the "divine" will, between the conscious efforts at integrating an ego-centered personality and the super-conscious guidance...
>
> At the Moon's North Node we see Destiny at work; at the South Node, human will... The South Node is always in any chart a wonderful index of the line of least resistance.

**Key Term Analysis**:
- **Moon's nodes**: `geocentric (not heliocentric)` / `satellite nodes` / `Moon orbit vs Earth orbit`
- **North Node**: `Destiny at work` / `future purpose` / `effort required` / `spiritual power reception`
- **South Node**: `human will` / `past achievement` / `line of least resistance` / `automatic performance`
- **Fate axis**: `Marc Jones term` / `past-future polarity`

**English Paraphrase (Primary Language)**:
Moon's nodes = geocentric (satellite), showing relation between "human will and divine will."

**North Node**: "Destiny at work"; the future, new faculty to develop, exertion brings power.
**South Node**: "human will"; the past, inherited gift, automatic performance, "line of least resistance."

"The South Node is always a wonderful index of the line of least resistance." Following it = "self-undoing."

**Complete Chinese Interpretation (Secondary Language)**:
月亮交点 = 地心的（卫星），显示"人类意志与神圣意志"之间的关系。

**北交点**："命运在运作"；未来，需要发展的新能力，努力带来力量。
**南交点**："人类意志"；过去，继承的天赋，自动表演，"最小阻力路线"。

"南交点始终是最小阻力路线的绝佳指标。"跟随它 = "自我毁灭"。

**Narrative Snippets**:
- `[ns_aop_189]` `[trigger: moon_nodes]` `[factor_trigger: astro_nodes_lunar AND astro_lunar_nodes]` `[role: 主干]` Moon's nodes: geocentric; North = Destiny/future; South = past/least resistance. → L10075-10097
- `[ns_aop_190]` `[trigger: south_node]` `[factor_trigger: astro_south_node_meaning]` `[role: 总结]` South Node = line of least resistance, inherited gift, automatic performance; following = self-undoing. → L10169-10197"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 2: Moon's Nodes - The Fate Axis"
    factor_refs: list = ['nodes_lunar', 'fate_axis', 'least_resistance']
    
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
        book_id="astrology_personality",
        chapter="",
        l1_anchor="ap_v1.0.0_entry_2__moon_s_nodes___the_fa_001_L1",
    )
    version: str = "1.0.0"
