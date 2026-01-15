"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.552766
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
    semantic_id="acu_v1.0.0_319_320_积极想象方法_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 319320积极想象方法(SemanticEntry):
    """
    **原文** (§319-320, 行5367-5404):

> [319] ...These "visions" are far from being hallucinations or ecst...
    """
    
    original_text: str = """**原文** (§319-320, 行5367-5404):

> [319] ...These "visions" are far from being hallucinations or ecstatic states; they are spontaneous, visual images of fantasy or so-called active imagination. The latter is a method (devised by myself) of introspection for observing the stream of interior images. One concentrates one's attention on some impressive but unintelligible dream-image, or on a spontaneous visual impression, and observes the changes taking place in it. Meanwhile, of course, all criticism must be suspended and the happenings observed and noted with absolute objectivity...
>
> [320] Under these conditions, long and often very dramatic series of fantasies ensue. The advantage of this method is that it brings a mass of unconscious material to light. Drawing, painting, and modelling can be used to the same end.

**英文释义（主语言）**:

**积极想象的定义**：
这些"幻象"远非幻觉或狂喜状态；它们是**自发的、幻想的视觉图像**或所谓的**积极想象**。后者是荣格自创的**内省方法**，用于观察**内在图像流**。

**方法步骤**：
1. 将注意力集中于某个印象深刻但难以理解的**梦意象**，或自发的视觉印象
2. 观察其中发生的**变化**
3. 同时必须**悬置所有批评**
4. 以**绝对客观性**观察和记录发生的事情

**方法的优势**：
在这些条件下，会产生长而常常非常戏剧化的幻想系列。这个方法的优势是它能将**大量无意识材料**带到光明中。绘画、雕塑也可用于同样目的。

**方法的风险**：
对于轻微病态的个体，特别是在潜在精神分裂症的不少见案例中，这个方法在某些情况下可能相当危险，因此需要**医学监督**。

**完整中文诠释（次语言）**:

**积极想象不是幻觉**：
这些"幻象"远非幻觉或狂喜状态；它们是自发的、幻想的视觉图像或所谓的积极想象。后者是荣格自创的内省方法，用于观察内在图像流。

**积极想象的操作步骤**：
1. 将注意力集中于某个印象深刻但难以理解的梦意象，或自发的视觉印象
2. 观察其中发生的变化
3. 同时必须悬置所有批评
4. 以绝对客观性观察和记录发生的事情
5. 也必须搁置"整个事情是'任意的'或'想出来的'"这类反对，因为它源于自我意识的焦虑——不容许自己家里有除自己以外的主人
6. 换言之，这是意识心智对无意识施加的抑制

**方法的效果与应用**：
在这些条件下，会产生长而常常非常戏剧化的幻想系列。这个方法的优势是它能将大量无意识材料带到光明中。绘画、雕塑也可用于同样目的。一旦视觉系列变得戏剧化，它可以轻易过渡到听觉或语言领域，产生对话等。

**核心要点**:
- 积极想象 ≠ 幻觉或狂喜状态
- 积极想象 = 自发视觉图像 = 内省方法
- 步骤：集中注意→观察变化→悬置批评→客观记录
- 需搁置"任意"或"想出来"的反对
- 优势：带出大量无意识材料
- 绘画、雕塑也可用
- 对病态个体可能危险，需医学监督

**叙事片段**:
- `[ns_cw9i_V_319_001]` `[trigger: active_imagination]` `[factor_trigger: jung_method AND jung_unconscious]` `[role: 主干]` 积极想象=观察内在图像流的内省方法——集中注意、观察变化、悬置批评、客观记录。→ §319-320"""
    normalized_text_zh: str = """"""
    subject: str = "§319-320 积极想象方法"
    factor_refs: list = ['engine_id', 'active_imagination', 'psych_semantic', 'concentrate', 'psych_semantic', 'suspend_criticism', 'psych_semantic', 'bring_unconscious', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_319_320_积极想象方法_001_L1",
    )
    version: str = "1.0.0"
