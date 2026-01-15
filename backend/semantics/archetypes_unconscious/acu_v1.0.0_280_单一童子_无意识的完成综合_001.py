"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.535840
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
    semantic_id="acu_v1.0.0_280_单一童子_无意识的完成综合_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 280单一童子无意识的完成综合(SemanticEntry):
    """
    **原文** (¶280, 行4716-4718):

> [280] If, however, the child motif appears in the form of a unity, we ...
    """
    
    original_text: str = """**原文** (¶280, 行4716-4718):

> [280] If, however, the child motif appears in the form of a unity, we are dealing with an unconscious and provisionally complete synthesis of the personality, which in practice, like everything unconscious, signifies no more than a possibility.

**英文释义（主语言）**:

**单一童子的意义**：
如果童子母题以单一形式出现，我们处理的是人格的**无意识且暂时完成的综合**。在实践中，如同一切无意识的东西，这仅意味着一种**可能性**。

**完整中文诠释（次语言）**:

如果童子母题以单一形式出现，我们处理的是人格的**无意识且暂时完成的综合**。

然而，在实践中，如同一切无意识的东西，这仅意味着一种**可能性**——尚未实现为意识的现实。

这个简短的段落与前一段形成对比：复数童子代表未完成综合或病理解离，而单一童子代表已完成但仍无意识的综合——一种有待实现的潜能。

**核心要点**:
- 单一童子 = 无意识且暂时完成的人格综合
- 如一切无意识 = 仅意味着可能性
- 与复数童子对比：完成vs未完成

**叙事片段**:
- `[ns_cw9i_IV_280_001]` `[trigger: child_unity]` `[factor_trigger: jung_child_archetype AND jung_unity]` `[role: 主干]` 单一童子=无意识且暂时完成的人格综合——如一切无意识，仅意味着可能性。→ ¶280"""
    normalized_text_zh: str = """"""
    subject: str = "¶280 单一童子=无意识的完成综合"
    factor_refs: list = ['engine_id', 'child_unity', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_280_单一童子_无意识的完成综合_001_L1",
    )
    version: str = "1.0.0"
