"""
Auto-generated semantic module for waite_tarot
Generated at: 2025-12-05T13:30:19.952807
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
    semantic_id="wt_v1.0.0_judgement__最后审判_001",
    book_id="waite_tarot",
    engine_id="tarot"
)
class Judgement最后审判(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Summons from Within | Inner trumpet | Not external |
| Twinkling of Eye | 1 Cor 15:52 | Instant |
| Card of Eternal Life | Like Temperance | Achievement |
| Dead Rising | Wonder/adoration | Response |

**Number**: XX | **Element**: Fire | **Path**: Hod to Malkuth

**Source Text** (condensed):
> "Angel blows trumpet... dead rising in wonder/adoration. The summons of Supernal is heard and answered from within. What is that within us which sounds a trumpet and all lower rises in response--almost in moment, twinkling of eye? (1 Cor 15:52). Card of eternal life, comparable to Temperance."

**Core**: **Inner Summons & Instant Transformation** – Trumpet from within, instantaneous transformation ("twinkling of eye"), eternal life like Temperance.

**Chinese**: **最后审判（内在号角与瞬间转化）**——从内在听到召唤，眨眼间瞬间转化（林前15:52），永生之牌（如节制）。

**Bilingual Terms**: Summons from Within (从内在召唤) | Twinkling of Eye (眨眼之间) | Card of Eternal Life (永生之牌)

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Waite asks: "What is that within us which sounds a trumpet and all lower rises in response?" Answer from within, not external. "Twinkling of eye" (1 Cor 15:52). "Card of eternal life, comparable to Temperance."
- **中文**: 韦特问："我们内在什么吹响号角，所有较低起身响应？"从内在回应，非外在。"眨眼之间"(林前15:52)。"永生之牌，可比节制"。

**Narrative Snippets**:
- `[ns_waite_076]` `[trigger: judgement_summons]` `[factor_trigger: tarot_judgement AND inner_trumpet]` `[role: 主干]` The summons of the Supernal is heard and answered from within—not external judgment but inner awakening. → Core
- `[ns_waite_077]` `[trigger: judgement_twinkling]` `[factor_trigger: tarot_judgement AND instant_transformation]` `[role: 条件分支]` Almost in a moment, in the twinkling of an eye (1 Cor 15:52)—instantaneous spiritual transformation. → Speed
- `[ns_waite_078]` `[trigger: judgement_eternal]` `[factor_trigger: tarot_judgement AND eternal_life]` `[role: 条件分支]` This is the card of eternal life, comparable to Temperance—achievement of immortality through inner response. → Achievement"""
    normalized_text_zh: str = """"""
    subject: str = "Judgement (最后审判)"
    factor_refs: list = ['tarot_judgement', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'tarot_judgement', 'tarot_semantic', 'new_candidate', 'tarot_semantic', 'new_candidate', 'tarot_semantic', 'new_candidate', 'tarot_semantic', 'new_candidate', 'tarot_semantic', 'source_ref', 'rel_waite_058', 'tarot_judgement', 'complementary', 'rel_waite_059', 'tarot_judgement', 'awakening', 'rel_waite_060', 'tarot_judgement', 'transforming', 'evi_waite_039', 'tarot_judgement', 'rule_waite_judgement_inner', 'evi_waite_040', 'tarot_judgement', 'rule_waite_judgement_eternal', 'concept_inner_summons', 'planet_pluto', 'self_calling', 'concept_instant_transformation', 'transformation_dream']
    
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
        book_id="waite_tarot",
        chapter="",
        l1_anchor="wt_v1.0.0_judgement__最后审判_001_L1",
    )
    version: str = "1.0.0"
