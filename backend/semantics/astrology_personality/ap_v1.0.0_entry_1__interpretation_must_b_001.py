"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238356
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
    semantic_id="ap_v1.0.0_entry_1__interpretation_must_b_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry1InterpretationMustB(SemanticEntry):
    """
    **Source Text** (Lines 15170-15210):
> Interpretation, in order to be fully significant and creative...
    """
    
    original_text: str = """**Source Text** (Lines 15170-15210):
> Interpretation, in order to be fully significant and creative, must needs be individual. No man, therefore, should tell another man how to interpret his experience or any life-structure...
>
> The interpretation of a birth-chart is no different from the interpretation of any life-situation, nor from the interpretation of a work of art or of a personality which one meets for the first time...
>
> Every potential interpreter must decide for himself—according to the nature of his own understanding. Some will go from the whole to the parts... Others will just as wisely analyze parts, then relations between parts...

**Key Term Analysis**:
- **Individual interpretation**: `no man tells another` / `creative` / `according to own understanding`
- **Same as life interpretation**: `birth-chart = life-situation = work of art`
- **Two approaches**: `whole to parts` vs `parts to whole` / `focal determinator`
- **Organic relationship**: `not sum of factors` / `relationship of relations`

**English Paraphrase (Primary Language)**:
"Interpretation, in order to be fully significant and creative, must needs be individual."

Birth-chart interpretation = interpretation of "any life-situation" or "work of art."

Two valid approaches: "from the whole to the parts" (holistic) OR astro_"analyze parts, then relations" (analytic)—both arriving at "focal determinator."

Human beings = "organic relationship of relations between factors," not "sum totals of separate factors."

**Complete Chinese Interpretation (Secondary Language)**:
"解读，为了充分有意义和创造性，必须是个体的。"

出生图解读 = 解读"任何生活情境"或"艺术作品"。

两种有效方法：从"整体到部分"（整体论）或"分析部分，然后关系"（分析论）——两者都达到"焦点决定因子"。

人类 = "因素之间关系的有机关系"，不是"独立因素的总和"。

**Narrative Snippets**:
- `[ns_aop_217]` `[trigger: individual_interp]` `[factor_trigger: astro_interp_individual AND astro_interp_indiv]` `[role: 主干]` Interpretation must be individual; birth-chart = life-situation = work of art interpretation. → L15170-15190
- `[ns_aop_218]` `[trigger: interp_methods]` `[factor_trigger: astro_interp_approach]` `[role: 主干依赖]` Two approaches: whole-to-parts or parts-to-relations; humans = relationship of relations. → L15206-15210"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 1: Interpretation Must Be Individual"
    factor_refs: list = ['interp_indiv', 'organic_rel']
    
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
        l1_anchor="ap_v1.0.0_entry_1__interpretation_must_b_001_L1",
    )
    version: str = "1.0.0"
