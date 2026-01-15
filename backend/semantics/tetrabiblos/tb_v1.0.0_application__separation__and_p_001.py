"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.182745
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
    semantic_id="tb_v1.0.0_application__separation__and_p_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class ApplicationSeparationAndP(SemanticEntry):
    """
    **Source Text** (Lines 2887-2947):
> In all cases when the distances between planets are but triflin...
    """
    
    original_text: str = """**Source Text** (Lines 2887-2947):
> In all cases when the distances between planets are but trifling, the planet which precedes is said to apply to that which follows; and that which follows to be separating from that which precedes... The influence of each planet is strengthened chiefly when it may be oriental, swift and direct in its proper course and motion—for it has then its greatest power: but, on the other hand, it loses strength when occidental and slow in motion or retrograde... if it be situated in the mid-heaven, or succedent to the mid-heaven, it is especially strong; likewise, if it be on the actual horizon, or succedent to the horizon, it is also powerful.

**English Paraphrase (Primary Language)**:
Ptolemy defines **application and separation** and summarizes **planetary strength factors**:

**Application**: The faster (more occidental) planet approaches the slower—forming aspect.
**Separation**: The faster planet moves away from the slower—aspect dissolving.

**Strength factors**:
- **Oriental** (rising before Sun): Strong
- **Swift and direct**: Strong
- **Occidental** (setting after Sun): Weaker
- **Slow or retrograde**: Weaker
- **Angular (MC, ASC, DSC, IC)**: Strongest
- **Succedent houses (2, 5, 8, 11)**: Strong
- **Cadent houses (3, 6, 9, 12)**: Weak
- **Below horizon, not aspecting ASC**: Entirely deprived of efficacy

**Complete Chinese Interpretation (Secondary Language)**:
托勒密定义了**入相位和离相位**并总结了**行星力量因素**：

**入相位**：较快（更西方）的行星接近较慢的——形成相位。
**离相位**：较快的行星离开较慢的——相位消解。

**力量因素**：
- **东方**（在太阳之前升起）：强
- **快速且顺行**：强
- **西方**（在太阳之后落下）：弱
- **缓慢或逆行**：弱
- **角宫（中天、上升、下降、天底）**：最强
- **续宫（2、5、8、11）**：强
- **果宫（3、6、9、12）**：弱
- **在地平线下，不与上升点相位**：完全失去效力

**Core Points**:
- Application = faster planet approaches slower
- Separation = faster planet departs slower
- Oriental position strengthens; occidental weakens
- Swift/direct = strong; slow/retrograde = weak
- Angular houses = strongest placement
- Succedent = strong; Cadent = weak
- Below horizon without ASC aspect = no efficacy

**Narrative Snippets**:
- `[ns_tetra_i060]` `[trigger: application_separation]` `[factor_trigger: astro_aspect_application AND aspect_separation]` `[role: 主干]` The preceding planet applies; the following separates—application forms aspect, separation dissolves it. → Source Text I.27
- `[ns_tetra_i061]` `[trigger: planetary_strength]` `[factor_trigger: astro_planet_strength AND house_angular]` `[role: 主干]` Planets are strongest when oriental, swift, direct, and angular; weakest when occidental, slow, retrograde, and cadent. → Source Text I.27

**Textual Criticism**: Orbs mentioned in footnote: Saturn 10°, Jupiter 12°, Mars 7°30', Sun 17°, Venus 8°, Mercury 7°30', Moon 12°30'."""
    normalized_text_zh: str = """"""
    subject: str = "Application, Separation, and Planetary Strength (Chapter XXVII)"
    factor_refs: list = ['engine_id', 'aspect_application', 'astrology_classical', 'aspect_separation', 'astrology_classical', 'planet_oriental', 'astrology_classical', 'house_angular', 'astrology_classical', 'source_ref', 'rel_i_024', 'aspect_application', 'connecting', 'rel_i_025', 'planet_oriental', 'enhancing', 'evi_i_020', 'planet_oriental', 'rule_planet_strength', 'concept_application', 'aspect_application', 'relationship_forming']
    
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
        book_id="tetrabiblos",
        chapter="",
        l1_anchor="tb_v1.0.0_application__separation__and_p_001_L1",
    )
    version: str = "1.0.0"
