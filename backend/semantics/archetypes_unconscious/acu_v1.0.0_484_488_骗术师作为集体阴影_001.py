"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.545124
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
    semantic_id="acu_v1.0.0_484_488_骗术师作为集体阴影_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 484488骗术师作为集体阴影(SemanticEntry):
    """
    **原文** (§484-488, 行7544-7608):

> The trickster is a collective shadow figure, a summation of all th...
    """
    
    original_text: str = """**原文** (§484-488, 行7544-7608):

> The trickster is a collective shadow figure, a summation of all the inferior traits of character in individuals. And since the individual shadow is never absent as a component of personality, the collective figure can construct itself out of it continually...
>
> [487] If, at the end of the trickster myth, the saviour is hinted at, this comforting premonition or hope means that some calamity or other has happened and been consciously understood...
>
> [488] As in its collective, mythological form, so also the individual shadow contains within it the seed of an enantiodromia, of a conversion into its opposite.

**英文释义（主语言）**:

**骗术师=集体阴影**：
骗术师是**集体阴影形象**，是个体中所有低劣性格特征的**总和**。由于个体阴影作为人格成分从不缺席，集体形象可以不断从中构建自身。

**阴影背后的形象序列**：
站在阴影最近背后的是**阿尼玛**——拥有相当的迷惑和附身力量。她常以过于年轻的形式出现，反过来隐藏着强大的**智慧老人**原型。

**救世主的暗示**：
如果在骗术师神话结尾暗示了救世主，这个安慰性的预感或希望意味着某种灾难已发生并被意识理解。只有从灾难中才能产生对救世主的渴望——换言之，对阴影的认识和不可避免的整合创造了如此痛苦的处境，只有救世主才能解开命运的缠结。

**个体问题的解决**：
在个体情况下，阴影提出的问题在阿尼玛层面即通过**关系**得到回答。在集体历史和个体历史中，一切都取决于**意识的发展**。这逐渐带来从"无意识"囚禁中的解放，因此既是光明的带来者也是治愈的带来者。

**向对立面的转化**：
正如在集体神话形式中，个体阴影内也包含**向对立面转化**(enantiodromia)的种子。

**完整中文诠释（次语言）**:

**骗术师是集体阴影的总和**：
骗术师是集体阴影形象，是个体中所有低劣性格特征的总和。由于个体阴影作为人格成分从不缺席，集体形象可以不断从中构建自身——不一定是神话形象，而是由于对原始神话的日益压抑和忽视，作为对其他社会群体和民族的相应投射。

**阴影背后的原型序列**：
如果将骗术师作为个体阴影的平行物，那么在骗术师神话中观察到的意义倾向是否也能在主观和个人阴影中观察到？阴影虽然定义为负面形象，有时有明确可辨的特征和联想指向完全不同的背景——仿佛他在不讨人喜欢的外表下隐藏着有意义的内容。站在阴影最近背后的是阿尼玛，她反过来隐藏着智慧老人原型。

**救世主与意识发展**：
如果在骗术师神话结尾暗示了救世主，这意味着某种灾难已发生并被意识理解。只有从灾难中才能产生对救世主的渴望。在个体情况下，阴影提出的问题在阿尼玛层面即通过关系得到回答。一切都取决于意识的发展——这逐渐带来从无意识囚禁中的解放，因此既是光明的带来者也是治愈的带来者。

**核心要点**:
- 骗术师 = 集体阴影 = 所有低劣特征的总和
- 个体阴影从不缺席→集体形象不断构建
- 阴影背后序列：阿尼玛→智慧老人
- 救世主暗示 = 灾难被意识理解
- 阴影问题在阿尼玛层面通过关系解决
- 一切取决于意识发展
- 个体阴影含向对立面转化的种子

**叙事片段**:
- `[ns_cw9i_VII_484_002]` `[trigger: collective_shadow]` `[factor_trigger: jung_trickster AND jung_shadow]` `[role: 主干]` 骗术师=集体阴影=所有低劣特征总和——个体阴影从不缺席，集体形象不断构建。→ §484
- `[ns_cw9i_VII_487_001]` `[trigger: saviour_hint]` `[factor_trigger: jung_trickster AND jung_saviour]` `[role: 主干依赖]` 救世主暗示=灾难被意识理解——阴影整合创造痛苦处境，只有救世主能解开。→ §487
- `[ns_cw9i_VII_488_001]` `[trigger: enantiodromia]` `[factor_trigger: jung_shadow AND jung_transformation]` `[role: 主干依赖]` 个体阴影含向对立面转化种子——意识发展带来从无意识囚禁的解放。→ §488"""
    normalized_text_zh: str = """"""
    subject: str = "§484-488 骗术师作为集体阴影"
    factor_refs: list = ['engine_id', 'collective_shadow', 'psych_semantic', 'shadow_sequence', 'psych_semantic', 'saviour_hint', 'psych_semantic', 'enantiodromia', 'psych_semantic', 'consciousness_development', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_484_488_骗术师作为集体阴影_001_L1",
    )
    version: str = "1.0.0"
