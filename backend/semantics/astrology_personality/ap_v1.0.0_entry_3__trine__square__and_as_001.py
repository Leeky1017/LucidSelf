"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238291
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
    semantic_id="ap_v1.0.0_entry_3__trine__square__and_as_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry3TrineSquareAndAs(SemanticEntry):
    """
    **Source Text** (Lines 13006-13041):
> The polygonal forms with which we ordinarily deal in astrolog...
    """
    
    original_text: str = """**Source Text** (Lines 13006-13041):
> The polygonal forms with which we ordinarily deal in astrology are based either on the triangle or on the square. Trine, sextile, semi-sextile (and quincunx) are essentially triangular; square and semi-square (and sesquiquadrate) are quadrangular...
>
> The trine is an aspect of "vision" and "perspective." It refers to the birth of ideas or viewpoints, to the initial phase of a new plan...
>
> The square... is the power of incarnation, of birthing. It is indeed crucifixion, from the spirit's viewpoint.

**Key Term Analysis**:
- **Triangular series**: `trine, sextile, semi-sextile` / `creative ideation` / `"formation"`
- **Quadrangular series**: `square, semi-square` / `insubstantiation of forms` / `incarnation`
- **Trine**: `vision, perspective` / `birth of ideas` / `new plan`
- **Square**: `incarnation, birthing` / `crucifixion` / `mobilization`

**English Paraphrase (Primary Language)**:
Triangular aspects (trine/sextile) = "creative ideation, formation." Trine = "vision, perspective, birth of ideas."

Quadrangular aspects (square/semi-square) = "insubstantiation of forms." Square = "power of incarnation, birthing, crucifixion from spirit's viewpoint."

Quintile series = "operation of individual factor per se"; genius determination. "In between square (90°) and sextile (60°), the quintile (72°) shows creative freedom."

**Complete Chinese Interpretation (Secondary Language)**:
三角相位（三分/六分） = "创造性构思，形成"。三分 = "视野、透视、理念诞生"。

四角相位（四分/半四分） = "形式的实体化"。四分 = "化身、诞生、从精神角度的十字架苦刑"。

五分相系列 = "个体因素本身的运作"；天才的决定。"在四分（90°）和六分（60°）之间，五分（72°）显示创造自由。"

**Narrative Snippets**:
- `[ns_aop_203]` `[trigger: aspect_series]` `[factor_trigger: astro_aspect_classification AND astro_trine AND astro_square]` `[role: 主干]` Triangular = ideation (trine = vision); Quadrangular = incarnation (square = crucifixion). → L13006-13041
- `[ns_aop_204]` `[trigger: quintile_series]` `[factor_trigger: astro_quintile_meaning AND astro_quintile]` `[role: 主干依赖]` Quintile = individual genius; 72° = creative freedom between square and sextile. → L13043-13058"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 3: Trine, Square, and Aspect Series"
    factor_refs: list = ['aspect_trine', 'aspect_square', 'aspect_quintile']
    
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
        l1_anchor="ap_v1.0.0_entry_3__trine__square__and_as_001_L1",
    )
    version: str = "1.0.0"
