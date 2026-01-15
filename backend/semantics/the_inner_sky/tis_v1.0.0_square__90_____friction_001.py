"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.109902
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
    semantic_id="tis_v1.0.0_square__90_____friction_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class Square90Friction(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Square | 90° aspect, perpendicular | Friction and challenge |
| Friction | Built-in discord | Growth through struggle |
| Natural enemies | Incompatible modalities | Fundamental tension |

#### Source Text

"With squares, the friction characteristic of the 90-degree aspect arises out of an absolute, built-in discord. The two planets have nothing in common. They are natural enemies. If the opposition is the aspect of rivals, then the square is the aspect of natural enemies."

#### English Paraphrase (Primary Language)

The **square** (90°) represents **fundamental friction**: two planetary energies with **nothing in common**. Unlike the opposition where planets share a polarity axis, squared planets operate from completely incompatible frameworks.

**Natural enemies**: Forrest distinguishes squares from oppositions: rivals (opposition) can understand each other; **natural enemies** (square) cannot even comprehend each other's language.

**Growth mechanism**: Squares force growth through persistent friction. The discomfort is **non-negotiable**—we cannot simply project it away. We must **work through** the conflict internally.

#### Complete Chinese Interpretation (Secondary Language)

**四分相**（90度）代表**根本性摩擦**：两种行星能量**毫无共同点**。不同于共享极性轴的对分相，四分相行星从完全不兼容的框架运作。

**天敌**：Forrest区分四分相与对分相：对手（对分相）可以理解彼此；**天敌**（四分相）甚至无法理解对方的语言。

**成长机制**：四分相通过持续摩擦强迫成长。这种不适是**不可协商的**——我们不能简单地投射它。我们必须在内部**穿越**冲突。

#### Core Points

- **90° aspect**: Perpendicular, built-in discord
- **Natural enemies**: Fundamentally incompatible energies
- **Non-negotiable friction**: Cannot project away
- **Growth through struggle**: Forces internal work

#### Detailed Explanation

The square is the aspect of **irreducible internal conflict**. Unlike the opposition where one pole can be projected outward, the square's tension is felt entirely within the psyche. The two planets are "natural enemies"—their principles genuinely clash in ways that cannot be smoothed over or externalized.

Forrest's distinction between squares and oppositions is crucial: oppositions are "rivals" who might negotiate or alternate; squares are "natural enemies" in perpetual conflict. Moon square Saturn doesn't just create emotional reserve—it creates a felt sense that emotional needs (Moon) and responsible structure (Saturn) are fundamentally at war. One cannot have both simultaneously.

**Growth through friction** is the square's gift. Because the conflict is unavoidable and internal, it forces psychological work. The person cannot escape into projection or avoidance—they must find ways to honor both planets even as those planets pull in incompatible directions. This often produces great character strength and competence, but only after considerable struggle.

The square's friction is **non-negotiable**—it doesn't relax with age or awareness. What changes is the person's skill at navigating between the conflicting demands. Integration doesn't eliminate the tension; it develops wisdom in managing it.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Forrest's square interpretation emphasizes the "natural enemies" distinction from opposition's "rivals." This clarifies why squares often feel more internally conflicted.
- **中文**: Forrest的四分相诠释强调与对分相"对手"不同的"天敌"区分。这澄清了为什么四分相常感觉更内在冲突。

**Narrative Snippets**:
- `[ns_forrest_asp_005]` `[trigger: square]` `[factor_trigger: square AND aspect_friction]` `[role: 主干]` The square represents built-in discord between natural enemies—planets with nothing in common. → Source Text
- `[ns_forrest_asp_006]` `[trigger: friction]` `[factor_trigger: aspect_square AND aspect_internal]` `[role: 主干依赖]` Unlike opposition's projection, square friction is non-negotiable and must be worked through internally. → English Paraphrase
- `[ns_forrest_asp_015]` `[trigger: natural_enemies]` `[factor_trigger: aspect_square AND aspect_incompatibility]` `[role: 条件分支]` If opposition is the aspect of rivals, square is the aspect of natural enemies who cannot even comprehend each other's language. → Distinction
- `[ns_forrest_asp_016]` `[trigger: growth_friction]` `[factor_trigger: aspect_square AND aspect_development]` `[role: 条件分支]` The square's gift is growth through friction—forcing psychological work that produces character strength after struggle. → Growth"""
    normalized_text_zh: str = """"""
    subject: str = "Square (90°) - Friction"
    factor_refs: list = ['aspect_square', 'new_candidate', 'new_candidate', 'engine_id', 'aspect_square', 'astro_semantic', 'new_candidate', 'astro_semantic', 'new_candidate', 'astro_semantic', 'source_ref', 'rel_forrest_sq_001', 'aspect_square', 'challenging', 'rel_forrest_sq_002', 'square', 'strengthening', 'evi_forrest_sq_001', 'rule_aspect_square', 'concept_square', 'xing_punishment', 'obstacle_dream']
    
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
        book_id="the_inner_sky",
        chapter="",
        l1_anchor="tis_v1.0.0_square__90_____friction_001_L1",
    )
    version: str = "1.0.0"
