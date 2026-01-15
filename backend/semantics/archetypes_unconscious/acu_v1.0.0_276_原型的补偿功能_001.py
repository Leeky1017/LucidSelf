"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.535797
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
    semantic_id="acu_v1.0.0_276_原型的补偿功能_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 276原型的补偿功能(SemanticEntry):
    """
    **原文** (¶276, 行4629-4651):

> [276] The child motif represents not only something that existed in th...
    """
    
    original_text: str = """**原文** (¶276, 行4629-4651):

> [276] The child motif represents not only something that existed in the distant past but also something that exists now; that is to say, it is not just a vestige but a system functioning in the present whose purpose is to compensate or correct, in a meaningful manner, the inevitable one-sidednesses and extravagances of the conscious mind. It is in the nature of the conscious mind to concentrate on relatively few contents and to raise them to the highest pitch of clarity. A necessary result and precondition is the exclusion of other potential contents of consciousness. The exclusion is bound to bring about a certain one-sidedness of the conscious contents...
>
> Our differentiated consciousness is in continual danger of being uprooted; hence it needs compensation through the still existing state of childhood.

**关键术语分析**:

| 术语 | 字面意义 | 象征意义 | 语境用法 |
|------|---------|---------|---------|
| Compensation (补偿) | 弥补 | 原型的核心功能 | 修正片面性 |
| One-sidedness (片面性) | 单边 | 意识的必然缺陷 | 需要补偿 |
| Promethean debt (普罗米修斯式债务) | 盗火者的代价 | 进步的代价 | 灾难性偿还 |

**英文释义（主语言）**:

**童子母题的双重时间性**：
童子母题不仅代表遥远过去存在的东西，也代表**现在存在的东西**——不仅是残余，而是**当下运作的系统**。

**原型的补偿功能**：
目的：以有意义的方式**补偿或修正**意识心智不可避免的片面性和极端性。

**意识的本性缺陷**：
- 意识心智的本性是集中于相对较少的内容，将其提升到最高清晰度
- 必要结果和前提是排除其他潜在意识内容
- 排除必然带来意识内容的某种片面性

**进步的代价**：
- 意志越训练，越可能迷失于片面性
- 进步主义虽带来愿望满足，却积累巨大的"普罗米修斯式债务"
- 这债务必须以可怕灾难的形式不时偿还
- 例：人类梦想飞行多少世纪，得到的却是地毯式轰炸！

**补偿的必要性**：
分化的意识持续面临被连根拔起的危险；因此需要通过仍然存在的童年状态来补偿。

**完整中文诠释（次语言）**:

**童子母题的当下功能**：
童子母题不仅代表遥远过去存在的东西，也代表**现在存在的东西**。也就是说，它不仅仅是残余，而是**当下运作的系统**，其目的是以有意义的方式**补偿或修正**意识心智不可避免的片面性和极端性。

**意识心智的本性缺陷**：
意识心智的本性是集中于相对较少的内容，将其提升到最高清晰度。这必然导致排除其他潜在意识内容，从而带来意识内容的某种片面性。

**文明人的危险**：
由于文明人的分化意识通过意志的动力获得了实现其内容的有效工具，他越训练意志，就越有迷失于片面性、越来越偏离其存在法则和根基的危险。

这意味着一方面是人类自由的可能性，但另一方面也是无尽违背本能的根源。

**进步的普罗米修斯式债务**：
我们的进步主义虽然可能带来许多令人愉快的愿望满足，却积累了同样巨大的"普罗米修斯式债务"，必须以可怕灾难的形式不时偿还。人类梦想飞行多少世纪，我们得到的却是地毯式轰炸！

**补偿的必要性**：
我们分化的意识持续面临被连根拔起的危险；因此需要通过仍然存在的童年状态来**补偿**。

**核心要点**:
- 童子母题 = 当下运作的系统，非仅残余
- 功能：补偿/修正意识的片面性和极端性
- 意识本性：集中少数内容 → 排除其他 → 片面性
- 意志越强 → 片面性越大 → 偏离根基
- 进步积累"普罗米修斯式债务" → 以灾难偿还
- 分化意识需要童年状态的补偿

**叙事片段**:
- `[ns_cw9i_IV_276_001]` `[trigger: compensation_function]` `[factor_trigger: jung_archetype AND jung_compensation]` `[role: 主干]` 童子母题是当下运作的系统——目的是补偿或修正意识心智不可避免的片面性和极端性。→ ¶276
- `[ns_cw9i_IV_276_002]` `[trigger: promethean_debt]` `[factor_trigger: jung_progress AND jung_catastrophe]` `[role: 主干依赖]` 进步积累"普罗米修斯式债务"——必须以可怕灾难偿还。人类梦想飞行，得到的是地毯式轰炸。→ ¶276"""
    normalized_text_zh: str = """"""
    subject: str = "¶276 原型的补偿功能"
    factor_refs: list = ['engine_id', 'compensation', 'psych_semantic', 'one_sidedness', 'psych_semantic', 'promethean_debt', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_276_原型的补偿功能_001_L1",
    )
    version: str = "1.0.0"
