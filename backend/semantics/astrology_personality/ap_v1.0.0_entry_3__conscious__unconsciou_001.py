"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237887
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
    semantic_id="ap_v1.0.0_entry_3__conscious__unconsciou_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry3ConsciousUnconsciou(SemanticEntry):
    """
    **Source Text** (Lines 3704-3785):
> Jung admits the existence of these repressed contents which in ...
    """
    
    original_text: str = """**Source Text** (Lines 3704-3785):
> Jung admits the existence of these repressed contents which in their sum total constitute what he calls the "personal unconscious"; but he also speaks of a "collective unconscious" which has an entirely different origin and significance: "Just as the human body shows a common anatomy over and above all racial differences, so too, does the psyche possess a common substratum. I have called the latter the collective unconscious. As a common human heritage it transcends all differences of culture and consciousness..."
>
> The main point to consider is that, while Freud gives to the unconscious a purely secondary and negative character, Jung sees it as a positive and primordial factor, in fact as the very matrix out of which the conscious grows by differentiation.

**Key Term Analysis**:
- **Personal unconscious**: `repressed contents` / `Freudian` / `secondary/negative`
- **Collective unconscious**: `common human heritage` / `transcends culture` / `primordial matrix`
- **Jung vs Freud**: `positive vs negative` / `matrix vs shadow` / `assimilate vs dissipate`

**English Paraphrase (Primary Language)**:
Jung distinguishes personal unconscious (repressed contents, Freudian) from collective unconscious—"a common human heritage transcending all differences of culture and consciousness." While Freud saw unconscious as secondary/negative (to be dissipated), Jung sees it as "positive and primordial... the very matrix out of which the conscious grows."

The collective unconscious contains archetypes/"primordial images"—"the deepest, most ancient and most universal thoughts of humanity." This is not to be eliminated but assimilated, integrated.

**Complete Chinese Interpretation (Secondary Language)**:
Jung区分个人无意识（被压抑的内容，弗洛伊德式）和集体无意识——"超越所有文化和意识差异的人类共同遗产"。弗洛伊德认为无意识是次要/消极的（待消散），而Jung认为它是"积极和原初的……意识由此分化而成长的母体"。

集体无意识包含原型/"原初意象"——"人类最深、最古老、最普遍的思想"。这不是要消除而是要同化、整合。

**Narrative Snippets**:
- `[ns_aop_115]` `[trigger: collective_unconscious]` `[factor_trigger: astro_coll_uncons AND astro_pos_matrix AND astro_coll_uncons_struct]` `[role: 主干]` Collective unconscious: common human heritage, transcends culture, primordial matrix of conscious. → L3706-3724
- `[ns_aop_116]` `[trigger: jung_vs_freud]` `[factor_trigger: astro_jung_freud AND astro_neg_uncons]` `[role: 总结]` Jung vs Freud: unconscious is positive/primordial (assimilate) vs negative/secondary (dissipate). → L3776-3785"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 3: Conscious, Unconscious, and Collective Unconscious"
    factor_refs: list = ['astro_coll_uncons', 'astro_primordial_img']
    
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
        l1_anchor="ap_v1.0.0_entry_3__conscious__unconsciou_001_L1",
    )
    version: str = "1.0.0"
