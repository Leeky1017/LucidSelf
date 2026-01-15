"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238395
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
    semantic_id="ap_v1.0.0_epilogue_entry_2__astrology_an_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class EpilogueEntry2AstrologyAn(SemanticEntry):
    """
    **Source Text** (Lines 15967-15984):
> The main difference between the astrological and the psycholo...
    """
    
    original_text: str = """**Source Text** (Lines 15967-15984):
> The main difference between the astrological and the psychological approaches is that while the latter sees nothing but the "process of becoming whole" as it unfolds... the former claims that the ultimate wholeness reached at the end of the process is already there at the very beginning of the process, but only as an abstract ideal and a mere potentiality.
>
> Quality or monad at the beginning relates to... substantial elements which slowly organize themselves as organic bodies through an evolutionary process... Thus the beginning and the end are identical as far as the quality is concerned; but in the end this quality is fully manifest in a substantial body, while in the beginning it is only an abstract potentiality.

**Key Term Analysis**:
- **Psychology**: `sees process of becoming whole` / `duration` / `empirical`
- **Astrology**: `wholeness already there at beginning` / `abstract ideal` / `potentiality`
- **Beginning = End**: `identical in quality` / `end = manifest` / `beginning = potential`
- **Monad**: `quality at beginning` / `Self at end` / `exteriorization`

**English Paraphrase (Primary Language)**:
Key difference: Psychology = "process of becoming whole" unfolding in duration. Astrology = "ultimate wholeness already there at the beginning, but only as abstract ideal and potentiality."

"Beginning and end are identical as far as quality is concerned"—but end = fully manifest, beginning = abstract potentiality.

Monad at beginning → evolves through process → Self at end. "Quality is fully manifest in substantial body."

**Complete Chinese Interpretation (Secondary Language)**:
关键区别：心理学 = 在持续中展开的"成为整体的过程"。占星学 = "终极整体性在开始时就已经存在，但只是作为抽象理想和潜能"。

"就品质而言，开始和结束是相同的"——但结束 = 完全显化，开始 = 抽象潜能。

开始时的单子 → 通过过程进化 → 结束时的自性。"品质在实体身体中完全显化。"

**Narrative Snippets**:
- `[ns_aop_225]` `[trigger: astro_psych_diff]` `[factor_trigger: astro_approach_diff AND astro_view AND astro_psych]` `[role: 主干]` Psychology = becoming process; Astrology = wholeness already at beginning as potentiality. → L15967-15973
- `[ns_aop_226]` `[trigger: begin_end_same]` `[factor_trigger: astro_quality_identity AND astro_view]` `[role: 总结]` Beginning = End in quality; end = manifest, beginning = potential; monad → Self. → L15976-15984"""
    normalized_text_zh: str = """"""
    subject: str = "Epilogue Entry 2: Astrology and Psychology Correlated"
    factor_refs: list = ['becoming_proc', 'begin_potential']
    
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
        l1_anchor="ap_v1.0.0_epilogue_entry_2__astrology_an_001_L1",
    )
    version: str = "1.0.0"
