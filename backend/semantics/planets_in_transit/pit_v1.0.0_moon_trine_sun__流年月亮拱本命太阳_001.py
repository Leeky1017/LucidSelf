"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.301152
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
    semantic_id="pit_v1.0.0_moon_trine_sun__流年月亮拱本命太阳_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonTrineSun流年月亮拱本命太阳(SemanticEntry):
    """
    **Source Text** (Lines 3859-3868):
> Usually very pleasant transit. Psychologically feel very much i...
    """
    
    original_text: str = """**Source Text** (Lines 3859-3868):
> Usually very pleasant transit. Psychologically feel very much in harmony with yourself, able to do whatever you have to do single-mindedly. Energies flow with less resistance, life seems easier. Consequently relate to people more easily—others perceive your inward harmony and are drawn to you. Good time for group activity—can relate your interests to group interests so everyone gains. Relations with opposite sex improved.

**English Paraphrase**: Very pleasant—harmony with self, single-minded ability. Energies flow easily, life seems easier. Relate to people easily—others drawn to your harmony. Good for group activity. Opposite sex relations improved.

**Complete Chinese Interpretation**: 非常愉快——与自己和谐，专注能力。能量轻松流动，生活似乎更容易。容易与人交往——他人被你的和谐吸引。适合群体活动。与异性关系改善。

**Narrative Snippets**:
- `[ns_pit_m029]` `[trigger: transit_moon_trine_natal_sun]` `[factor_trigger: astro_transit_moon TRINE natal_sun]` `[role: 主干]` Very pleasant—harmony with self. Energies flow easily. Others drawn to your inward harmony. → PIT Ch5 Moon△Sun"""
    normalized_text_zh: str = """"""
    subject: str = "Moon Trine Sun (流年月亮拱本命太阳)"
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
        l1_anchor="pit_v1.0.0_moon_trine_sun__流年月亮拱本命太阳_001_L1",
    )
    version: str = "1.0.0"
