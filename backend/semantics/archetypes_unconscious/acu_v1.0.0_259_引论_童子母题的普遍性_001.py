"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.535570
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
    semantic_id="acu_v1.0.0_259_引论_童子母题的普遍性_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 259引论童子母题的普遍性(SemanticEntry):
    """
    **原文** (¶259, 行4324-4368):

> [259] The author of the companion essay on the mythology of the "child...
    """
    
    original_text: str = """**原文** (¶259, 行4324-4368):

> [259] The author of the companion essay on the mythology of the "child" or the child god has asked me for a psychological commentary on the subject of his investigations. The customary treatment of mythological motifs so far in separate departments of science, such as philology, ethnology, the history of civilization, and comparative religion, was not exactly a help to us in recognizing their universality. Adolf Bastian's ideas met with little success in their day. Although the psychological knowledge of that time included myth-formation in its province—witness Wundt's Völkerpsychologie—it was not in a position to demonstrate this same process as a living function actually present in the psyche of civilized man. True to its history, when psychology was metaphysics first of all, then the study of the senses, then of conscious mind, psychology identified its proper subject with the conscious psyche and completely overlooked the existence of a nonconscious psyche. It was C. G. Carus, the authority whom Eduard von Hartmann followed, who pointed to the unconscious as the essential basis of the psyche.

**英文释义**：
- 童子母题的跨文化普遍性未被各学科充分认识
- 过去心理学局限于意识心灵，忽视非意识心灵
- Carus首先指出无意识是心灵的本质基础
- 典型神话元素在不知任何此类知识的个体中被观察到
- 必须假设无意识心灵中存在"形成神话"的结构元素

**中文诠释**：
- 童子母题的跨文化普遍性 → 原型的存在证据
- 心理学史：形而上学 → 感官研究 → 意识心灵 → 无意识
- Carus和Hartmann → 无意识作为心灵本质基础
- 在无相关知识的个体中发现神话元素 → "自生"复活假说
- 无意识心灵中存在形成神话的结构元素 = 原型

**Narrative Snippets**:
- `[ns_cw9i_IV_259]` `[trigger: child_motif]` `[factor_trigger: jung_child AND jung_archetype]` `[role: 主干]` Child motif's universality was obscured by disciplinary fragmentation—psychology overlooked the nonconscious psyche until Carus. → ¶259"""
    normalized_text_zh: str = """"""
    subject: str = "¶259 引论：童子母题的普遍性"
    factor_refs: list = []
    
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
        l1_anchor="acu_v1.0.0_259_引论_童子母题的普遍性_001_L1",
    )
    version: str = "1.0.0"
