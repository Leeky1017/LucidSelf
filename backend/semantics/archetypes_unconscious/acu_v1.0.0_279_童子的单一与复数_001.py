"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.535830
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
    semantic_id="acu_v1.0.0_279_童子的单一与复数_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 279童子的单一与复数(SemanticEntry):
    """
    **原文** (¶279, 行4703-4714):

> [279] In the manifold phenomenology of the "child" we have to distingu...
    """
    
    original_text: str = """**原文** (¶279, 行4703-4714):

> [279] In the manifold phenomenology of the "child" we have to distinguish between the unity and plurality of its respective manifestations. Where, for instance, numerous homunculi, dwarfs, boys, etc., appear, having no individual characteristics at all, there is the probability of a dissociation. Such forms are therefore found especially in schizophrenia, which is essentially a fragmentation of personality. The many children then represent the products of its dissolution. But if the plurality occurs in normal people, then it is the representation of an as yet incomplete synthesis of personality. The personality (viz., the "self") is still in the plural stage, i.e., an ego may be present, but it cannot experience its wholeness within the framework of its own personality, only within the community of the family, tribe, or nation; it is still in the stage of unconscious identification with the plurality of the group. The Church takes due account of this widespread condition in her doctrine of the corpus mysticum, of which the individual is by nature a member.

**英文释义（主语言）**:

**单一与复数的区分**：
在童子的多样现象学中，必须区分其显现的单一性和复数性。

**复数童子的病理学意义**：
当众多小人、侏儒、男孩等出现，且无任何个体特征时，可能存在**解离**。
- 这种形式特别见于精神分裂症（本质上是人格碎片化）
- 众多童子代表人格瓦解的产物

**正常人中的复数童子**：
如果复数出现在正常人身上，则代表**尚未完成的人格综合**：
- 人格（即"自性"）仍处于复数阶段
- 自我可能存在，但无法在自身人格框架内体验整体性
- 只能在家庭、部落或民族的社群中体验
- 仍处于与群体复数性的无意识认同阶段

**教会的智慧**：
教会在其**神秘身体(corpus mysticum)**教义中适当考虑了这种普遍状况——个体天生是神秘身体的成员。

**完整中文诠释（次语言）**:

**区分单一与复数**：
在"童子"的多样现象学中，我们必须区分其各自显现的单一性和复数性。

**复数童子的病理学意义**：
例如，当众多小人、侏儒、男孩等出现，且完全没有任何个体特征时，可能存在**解离**。因此这种形式特别见于精神分裂症，精神分裂症本质上是人格的碎片化。众多童子代表人格瓦解的产物。

**正常人中的复数童子**：
但如果复数出现在正常人身上，则代表**尚未完成的人格综合**。人格（即"自性"）仍处于复数阶段，即自我可能存在，但无法在自身人格框架内体验整体性，只能在家庭、部落或民族的社群中体验；仍处于与群体复数性的无意识认同阶段。

**教会的神秘身体教义**：
教会在其**神秘身体(corpus mysticum)**教义中适当考虑了这种普遍状况，个体天生是神秘身体的成员。这解释了为什么集体宗教形式对于尚未完全个体化的人如此重要。

**核心要点**:
- 需区分童子的单一vs复数显现
- 复数+无个体特征 = 解离可能 = 精神分裂症
- 众多童子 = 人格瓦解产物
- 正常人复数 = 尚未完成的人格综合
- 自性仍在复数阶段 = 无法独立体验整体性
- 只能在群体中体验整体性 = 无意识认同
- 教会神秘身体教义回应此状况

**叙事片段**:
- `[ns_cw9i_IV_279_001]` `[trigger: child_plurality]` `[factor_trigger: jung_child_archetype AND jung_plurality]` `[role: 主干]` 复数童子无个体特征=解离可能，见于精神分裂症——众多童子代表人格瓦解产物。→ ¶279
- `[ns_cw9i_IV_279_002]` `[trigger: incomplete_synthesis]` `[factor_trigger: jung_self AND jung_group]` `[role: 主干依赖]` 正常人复数童子=尚未完成的人格综合——自性仍在复数阶段，只能在群体中体验整体性。→ ¶279"""
    normalized_text_zh: str = """"""
    subject: str = "¶279 童子的单一与复数"
    factor_refs: list = ['engine_id', 'unity_plurality', 'psych_semantic', 'schizophrenia', 'psych_semantic', 'incomplete_synthesis', 'psych_semantic', 'corpus_mysticum', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_279_童子的单一与复数_001_L1",
    )
    version: str = "1.0.0"
