"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.568738
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
    semantic_id="acu_v1.0.0_2_archetype_form_and_projectio_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 2ArchetypeFormAndProjectio(SemanticEntry):
    """
    **Source Text** (¶142-143, Lines 2253-2276):

> [142] When projected, the anima always has a feminin...
    """
    
    original_text: str = """**Source Text** (¶142-143, Lines 2253-2276):

> [142] When projected, the anima always has a feminine form with definite characteristics. This empirical finding does not mean that the archetype is constituted like that in itself. The male-female syzygy is only one among the possible pairs of opposites, albeit the most important one in practice. It has numerous connections with other pairs which do not display any sex differences at all. When one considers this data, it begins to seem probable that an archetype in its quiescent, unprojected state has no exactly determinable form but is in itself an indefinite structure which can assume definite forms only in projection.
>
> [143] This seems to contradict the concept of a "type." Empirically, we are dealing with "types," definite forms that can be named and distinguished. But the basic psychic elements are infinitely varied and ever changing. The empiricist must therefore content himself with a theoretical "as if."

**English Paraphrase**: Anima when projected = feminine form with definite characteristics. But archetype in itself = no exactly determinable form, indefinite structure. Male-female syzygy = one among possible opposites (most important in practice). Archetype assumes definite form only in projection. Empirically = types; metaphysically = infinitely varied. Empiricist uses theoretical "as if."

**中文诠释**: 阿尼玛投射时 = 有确定特征的女性形式。但原型本身 = 无确切可定形式，不确定结构。男女配对 = 可能对立面之一（实践中最重要）。原型只在投射中呈现确定形式。经验上 = 类型；形而上学 = 无限变化。经验主义者使用理论性"好像"。

**Narrative Snippets**:
- `[ns_cw9i_II_142]` `[trigger: archetype_form]` `[factor_trigger: jung_archetype AND jung_projection]` `[role: 主干]` Archetype in quiescent state has no determinable form—assumes definite form only in projection. → ¶142
- `[ns_cw9i_II_143]` `[trigger: empirical_types]` `[factor_trigger: jung_archetype AND jung_method]` `[role: 主干依赖]` Empirically = types; but basic psychic elements infinitely varied—empiricist uses theoretical "as if." → ¶143"""
    normalized_text_zh: str = """"""
    subject: str = "2 Archetype Form and Projection (¶142-143)"
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
        l1_anchor="acu_v1.0.0_2_archetype_form_and_projectio_001_L1",
    )
    version: str = "1.0.0"
