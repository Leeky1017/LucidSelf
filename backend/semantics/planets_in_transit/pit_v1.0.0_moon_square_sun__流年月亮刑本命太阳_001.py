"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.301142
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
    semantic_id="pit_v1.0.0_moon_square_sun__流年月亮刑本命太阳_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonSquareSun流年月亮刑本命太阳(SemanticEntry):
    """
    **Source Text** (Lines 3841-3858):
> Usually represents some sort of challenge to structure of daily...
    """
    
    original_text: str = """**Source Text** (Lines 3841-3858):
> Usually represents some sort of challenge to structure of daily life—home life, intimate relations, routine contacts. Hidden tensions brought to surface. May feel ill at ease within yourself, more difficulty getting along with others, especially opposite sex. More irritable, others' eccentricities harder to take. Several small areas of life may simultaneously reach crisis—situations or persons you've been taking for granted. Take time to correct little problems. If everything running smoothly, may feel as burst of emotional and physical energy for creative use.

**English Paraphrase**: Challenge to daily life structure. Hidden tensions surface. Ill at ease, difficulty with others especially opposite sex. More irritable. Small crises in taken-for-granted areas. Correct little problems. If smooth, can be creative energy burst.

**Complete Chinese Interpretation**: 对日常生活结构的挑战。隐藏的紧张浮出水面。不自在，与他人尤其异性有困难。更易怒。被忽视领域的小危机。纠正小问题。如果顺利，可以是创意能量爆发。

**Narrative Snippets**:
- `[ns_pit_m027]` `[trigger: transit_moon_square_natal_sun]` `[factor_trigger: astro_transit_moon SQUARE natal_sun]` `[role: 主干]` Challenge to daily life structure—hidden tensions surface. More irritable. → PIT Ch5 Moon□Sun
- `[ns_pit_m028]` `[trigger: transit_moon_square_natal_sun]` `[factor_trigger: astro_transit_moon SQUARE natal_sun]` `[role: 条件分支]` Small crises in taken-for-granted areas. If smooth, can be creative energy burst. → PIT Ch5 Moon□Sun"""
    normalized_text_zh: str = """"""
    subject: str = "Moon Square Sun (流年月亮刑本命太阳)"
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
        book_id="planets_in_transit",
        chapter="",
        l1_anchor="pit_v1.0.0_moon_square_sun__流年月亮刑本命太阳_001_L1",
    )
    version: str = "1.0.0"
