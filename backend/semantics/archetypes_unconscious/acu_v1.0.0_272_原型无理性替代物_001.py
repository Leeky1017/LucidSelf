"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.535759
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
    semantic_id="acu_v1.0.0_272_原型无理性替代物_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 272原型无理性替代物(SemanticEntry):
    """
    **原文** (¶272, 行4588-4594):

> [272] There is no "rational" substitute for the archetype any more tha...
    """
    
    original_text: str = """**原文** (¶272, 行4588-4594):

> [272] There is no "rational" substitute for the archetype any more than there is for the cerebellum or the kidneys. We can examine the physical organs anatomically, histologically, and embryologically. This would correspond to an outline of archetypal phenomenology and its presentation in terms of comparative history. But we only arrive at the meaning of a physical organ when we begin to ask teleological questions. Hence the query arises: What is the biological purpose of the archetype? Just as physiology answers such a question for the body, so it is the business of psychology to answer it for the archetype.

**英文释义（主语言）**:

**原型无理性替代物**：
原型没有"理性"替代物——正如小脑或肾脏没有替代物一样。

**类比：身体器官与原型**：
- 我们可以解剖学地、组织学地、胚胎学地检查身体器官
- 这对应于原型现象学的概述及其比较历史学的呈现

**目的论问题**：
- 只有当我们开始问目的论问题时，才能达到身体器官的意义
- 因此产生问题：**原型的生物学目的是什么？**
- 正如生理学为身体回答这个问题，心理学的任务是为原型回答它

**完整中文诠释（次语言）**:

**原型无理性替代物**：
荣格在此强调：原型没有"理性"替代物——正如小脑或肾脏没有替代物一样。这意味着我们不能用理性概念或抽象理论来取代原型的功能。

**器官学与原型学的类比**：
我们可以解剖学地、组织学地、胚胎学地检查身体器官。这对应于：
- 原型现象学的概述
- 原型的比较历史学呈现

**目的论的必要性**：
但我们只有当开始问目的论问题时，才能达到身体器官的意义。因此产生问题：**原型的生物学目的是什么？**

正如生理学为身体回答这个问题，心理学的任务是为原型回答它。这意味着心理学必须探索原型在人类心理生活中的功能和目的。

**核心要点**:
- 原型没有理性替代物（如小脑、肾脏）
- 原型现象学 ≈ 器官解剖学
- 必须问目的论问题：原型的生物学目的是什么？
- 心理学的任务：回答原型的目的

**叙事片段**:
- `[ns_cw9i_IV_272_001]` `[trigger: no_rational_substitute]` `[factor_trigger: jung_archetype]` `[role: 主干]` 原型没有理性替代物——如小脑或肾脏不能被替代，必须问目的论问题：原型的生物学目的是什么？→ ¶272"""
    normalized_text_zh: str = """"""
    subject: str = "¶272 原型无理性替代物"
    factor_refs: list = ['engine_id', 'no_rational_substitute', 'psych_semantic', 'biological_purpose', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_272_原型无理性替代物_001_L1",
    )
    version: str = "1.0.0"
