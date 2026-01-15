"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224486
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
    semantic_id="pit_v1.0.0_sun_conjunct_saturn__流年太阳合本命土星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunConjunctSaturn流年太阳合本命土星(SemanticEntry):
    """
    **Source Text** (estimated):
> A day of serious reflection. You examine your life and responsibiliti...
    """
    
    original_text: str = """**Source Text** (estimated):
> A day of serious reflection. You examine your life and responsibilities with more than usual concern. Energy may be low—not the best day for vigorous activity. Focus on what needs to be done, on duties and obligations. May feel limited or restricted. Good time to organize and structure your affairs. Discipline yourself and work on long-term projects. Don't start new ventures—consolidate existing ones.

**English Paraphrase**: Serious reflection day. Examine life and responsibilities. Energy may be low. Focus on duties and obligations. May feel limited. Good for organizing and structuring. Discipline yourself; work on long-term projects. Consolidate, don't start new.

**Complete Chinese Interpretation**: 严肃反思的一天。检视生活和责任。能量可能低落。专注于职责和义务。可能感到受限。适合组织和结构化。自律；进行长期项目。巩固而非开始新事物。

**Narrative Snippets**:
- `[ns_pit_099]` `[trigger: transit_sun_conjunct_natal_saturn]` `[factor_trigger: astro_transit_sun CONJUNCT natal_saturn]` `[role: 主干]` Serious reflection day—examine life and responsibilities. Focus on duties. May feel limited. → PIT Ch4 Sun☌Saturn
- `[ns_pit_100]` `[trigger: transit_sun_conjunct_natal_saturn]` `[factor_trigger: astro_transit_sun CONJUNCT natal_saturn]` `[role: 主干依赖]` Good for organizing, structuring, long-term projects. Consolidate existing ventures. → PIT Ch4 Sun☌Saturn"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Conjunct Saturn (流年太阳合本命土星)"
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
        l1_anchor="pit_v1.0.0_sun_conjunct_saturn__流年太阳合本命土星_001_L1",
    )
    version: str = "1.0.0"
