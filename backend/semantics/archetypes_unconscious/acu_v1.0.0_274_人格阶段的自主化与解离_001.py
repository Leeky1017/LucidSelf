"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.535777
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
    semantic_id="acu_v1.0.0_274_人格阶段的自主化与解离_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 274人格阶段的自主化与解离(SemanticEntry):
    """
    **原文** (¶274, 行4604-4616):

> [274] We shall not go wrong if we take this statement for the time bei...
    """
    
    original_text: str = """**原文** (¶274, 行4604-4616):

> [274] We shall not go wrong if we take this statement for the time being historically, on the analogy of certain psychological experiences which show that certain phases in an individual's life can become autonomous, can personify themselves to the extent that they result in a vision of oneself—for instance, one sees oneself as a child. Visionary experiences of this kind, whether they occur in dreams or in the waking state, are, as we know, conditional on a dissociation having previously taken place between past and present. Such dissociations come about because of various incompatibilities; for instance, a man's present state may have come into conflict with his childhood state, or he may have violently sundered himself from his original character in the interests of some arbitrary persona more in keeping with his ambitions. He has thus become unchildlike and artificial, and has lost his roots. All this presents a favourable opportunity for an equally vehement confrontation with the primary truth.

**英文释义（主语言）**:

**人格阶段的自主化**：
某些心理经验显示，个体生活中的某些阶段可以变得自主，可以人格化到产生自我幻象的程度——例如，看到自己作为童子。

**幻象经验的条件**：
这种幻象经验（无论在梦中还是清醒状态）以过去与现在之间先前发生的**解离**为条件。

**解离的原因**：
- 现在状态与童年状态冲突
- 为了某种与野心相符的任意人格面具(persona)，强行切断与原初性格的联系
- 结果：变得不像孩子、人为，**失去根基**

**后果**：
这一切为与原初真理的同样激烈对抗提供了有利机会。

**完整中文诠释（次语言）**:

**历史性理解**：
如果我们暂时从历史角度理解这个陈述，类比某些心理经验，就不会出错。

**人格阶段的自主化与人格化**：
某些心理经验显示，个体生活中的某些阶段可以变得自主，可以人格化到产生自我幻象的程度——例如，一个人看到自己作为童子。

**幻象经验的前提条件**：
这种幻象经验（无论在梦中还是清醒状态）以过去与现在之间先前发生的**解离**为条件。

**解离产生的原因**：
这种解离因各种不相容而产生：
- 一个人的现在状态可能与其童年状态冲突
- 或者他可能为了某种与其野心更相符的任意人格面具(persona)，强行切断与原初性格的联系

**解离的后果**：
他因此变得不像孩子、人为，并且**失去了根基**。所有这一切为与原初真理的同样激烈对抗提供了有利机会。

**核心要点**:
- 人格阶段可自主化、人格化
- 看到自己作为童子 = 幻象经验
- 前提：过去与现在之间的解离
- 解离原因：现状vs童年冲突；为人格面具切断原初性格
- 后果：失去根基，变得人为
- 但也为对抗原初真理提供机会

**叙事片段**:
- `[ns_cw9i_IV_274_001]` `[trigger: dissociation]` `[factor_trigger: jung_dissociation AND jung_persona]` `[role: 主干]` 看到自己作为童子的幻象以解离为条件——为人格面具切断原初性格导致失去根基。→ ¶274"""
    normalized_text_zh: str = """"""
    subject: str = "¶274 人格阶段的自主化与解离"
    factor_refs: list = ['engine_id', 'phase_autonomy', 'psych_semantic', 'dissociation', 'psych_semantic', 'persona', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_274_人格阶段的自主化与解离_001_L1",
    )
    version: str = "1.0.0"
