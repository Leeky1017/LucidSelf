"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.535808
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
    semantic_id="acu_v1.0.0_277_补偿症状与进步_保守的对立_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 277补偿症状与进步保守的对立(SemanticEntry):
    """
    **原文** (¶277, 行4653-4673):

> [277] The symptoms of compensation are described, from the progressive...
    """
    
    original_text: str = """**原文** (¶277, 行4653-4673):

> [277] The symptoms of compensation are described, from the progressive point of view, in scarcely flattering terms. Since, to the superficial eye, it looks like a retarding operation, people speak of inertia, backwardness, scepticism, fault-finding, conservatism, timidity, pettiness, and so on... The retarding ideal is always more primitive, more natural (in the good sense as in the bad), and more "moral" in that it keeps faith with law and tradition. The progressive ideal is always more abstract, more unnatural, and less "moral" in that it demands disloyalty to tradition. Progress enforced by will is always convulsive...
>
> Now it is an axiom of psychology that when a part of the psyche is split off from consciousness it is only apparently inactivated; in actual fact it brings about a possession of the personality... Viable progress only comes from the co-operation of both.

**英文释义（主语言）**:

**补偿症状的负面标签**：
从进步观点看，补偿症状被贬为：惰性、落后、怀疑、吹毛求疵、保守、胆怯、狭隘等。

**保守与进步的对比**：
- **保守理想**：更原始、更自然（好坏皆有）、更"道德"（忠于法律和传统）
- **进步理想**：更抽象、更不自然、更"不道德"（要求背叛传统）
- **意志强制的进步总是痉挛性的**

**心理学公理**：
当心灵的一部分从意识分裂出去时，它只是表面上被去活化；实际上它会**占据人格**，导致个体目标被歪曲以服务于分裂部分的利益。

**后果**：
如果集体心灵的童年状态被压抑到完全排除，无意识内容会压倒意识目标，抑制、歪曲甚至摧毁其实现。

**结论**：
**可行的进步只能来自两者的合作。**

**完整中文诠释（次语言）**:

**补偿症状被误解**：
从进步的观点看，补偿的症状几乎没有好名声。因为在肤浅的眼光看来，它像是一种延缓操作，人们说它是惰性、落后、怀疑、吹毛求疵、保守、胆怯、狭隘等等。

**保守与进步的辩证**：
但由于人类在很大程度上有切断自己根基的能力，他也可能被其危险的片面性不加批判地卷入灾难。

- **保守理想**总是更原始、更自然（好坏意义上都是）、更"道德"——因为它忠于法律和传统。
- **进步理想**总是更抽象、更不自然、更"不道德"——因为它要求背叛传统。

**意志强制的进步总是痉挛性的**。落后可能更接近自然，但它反过来总是受到痛苦觉醒的威胁。

**古老的智慧**：
古老的观点认识到进步只有在Deo concedente（神允许）时才可能，从而证明自己意识到了对立面。

**心理学公理**：
当意识越分化，与根基状态分离的危险就越大。完全分离发生在Deo concedente被遗忘时。

这是心理学的公理：当心灵的一部分从意识分裂出去时，它只是表面上被去活化；实际上它会**占据人格**，导致个体目标被歪曲以服务于分裂部分的利益。

**核心结论**：
如果集体心灵的童年状态被压抑到完全排除，无意识内容会压倒意识目标，抑制、歪曲甚至摧毁其实现。**可行的进步只能来自两者的合作。**

**核心要点**:
- 补偿被误解为惰性、落后、保守等
- 保守=更原始、自然、"道德"（忠于传统）
- 进步=更抽象、不自然、"不道德"（背叛传统）
- 意志强制的进步=痉挛性
- 心理学公理：分裂的心灵部分会占据人格
- 压抑童年状态→无意识压倒意识目标
- 可行的进步=两者合作

**叙事片段**:
- `[ns_cw9i_IV_277_001]` `[trigger: retarding_progressive]` `[factor_trigger: jung_compensation AND jung_progress]` `[role: 主干]` 保守理想更原始、自然、道德；进步理想更抽象、不自然——意志强制的进步总是痉挛性的。→ ¶277
- `[ns_cw9i_IV_277_002]` `[trigger: split_possession]` `[factor_trigger: jung_dissociation AND jung_possession]` `[role: 主干依赖]` 心理学公理：分裂的心灵部分并非去活化，而是占据人格——可行的进步只能来自两者合作。→ ¶277"""
    normalized_text_zh: str = """"""
    subject: str = "¶277 补偿症状与进步/保守的对立"
    factor_refs: list = ['engine_id', 'conservative_progressive', 'psych_semantic', 'split_possession', 'psych_semantic', 'cooperation_both', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_277_补偿症状与进步_保守的对立_001_L1",
    )
    version: str = "1.0.0"
