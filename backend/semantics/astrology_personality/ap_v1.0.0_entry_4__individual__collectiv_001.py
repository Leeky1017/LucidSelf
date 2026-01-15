"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237953
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
    semantic_id="ap_v1.0.0_entry_4__individual__collectiv_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry4IndividualCollectiv(SemanticEntry):
    """
    **Source Text** (Lines 4676-4744):
> Individual and Collective: All manifestations of life can be se...
    """
    
    original_text: str = """**Source Text** (Lines 4676-4744):
> Individual and Collective: All manifestations of life can be seen to involve a dualism of elements or tendencies. Where the Chinese spoke of Yang and Yin we shall use the terms: "individual" and "collective"; and we shall presently see that this dualism is resolved through the operation of a third principle: the "creative."...
>
> The first motion can be termed "individuation"—provided the word is taken in a much more general sense than the one given to it by Jung. The second motion can be termed "collectivation." The third term is "the creative." The crux of the whole matter lies in the correct understanding of this third term.

**Key Term Analysis**:
- **Individual**: `unique manner of combining elements` / `Yang-equivalent` / `spirit pole`
- **Collective**: `common properties of many` / `Yin-equivalent` / `substance pole`
- **Creative**: `resolves dualism` / `synthesis` / `third principle` / `neither motion but integration`
- **Individuation**: `elements gather into whole` / `integration`
- **Collectivation**: `individual features become group property` / `transmission`

**English Paraphrase (Primary Language)**:
Rudhyar replaces Yang-Yin with Individual-Collective. Individual = unique combination of elements; Collective = common properties of many. These are resolved through "the creative"—not a motion but synthesis.

"Individuation" = elements gather into whole. "Collectivation" = individual features become group property. The creative "is not a motion. There is no progress involved in it"—it is the timeless synthesis that enables both movements.

**Complete Chinese Interpretation (Secondary Language)**:
Rudhyar用个体-集体替代阴阳。个体=元素的独特组合；集体=众多事物的共同属性。这些通过"创造性"解决——不是运动而是综合。

"个体化"=元素聚集成整体。"集体化"=个体特征成为群体属性。创造性"不是运动。其中没有进展"——它是使两种运动成为可能的无时间的综合。

**Narrative Snippets**:
- `[ns_aop_129]` `[trigger: indiv_coll]` `[factor_trigger: astro_indiv_coll AND astro_cardinal AND astro_collective_state]` `[role: 主干]` Individual-Collective replaces Yang-Yin; resolved by third principle: the creative. → L4676-4691
- `[ns_aop_130]` `[trigger: creative_third]` `[factor_trigger: astro_creative AND astro_creative_factor AND astro_creative_synth]` `[role: 总结]` Creative = not motion but synthesis; crux of understanding; enables both individuation and collectivation. → L4741-4744"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 4: Individual, Collective, and Creative—The Triple Principle"
    factor_refs: list = ['astro_indiv_coll', 'astro_creative']
    
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
        book_id="astrology_personality",
        chapter="",
        l1_anchor="ap_v1.0.0_entry_4__individual__collectiv_001_L1",
    )
    version: str = "1.0.0"
