"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224444
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
    semantic_id="pit_v1.0.0_sun_sextile_jupiter__流年太阳六合本命木_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunSextileJupiter流年太阳六合本命木(SemanticEntry):
    """
    **Source Text** (Lines 2708-2733):
> Extremely positive transit—useful aid in almost any activity. T...
    """
    
    original_text: str = """**Source Text** (Lines 2708-2733):
> Extremely positive transit—useful aid in almost any activity. Traditionally one of the "lucky" transits—gives positive frame of mind at root of most success. Almost anything you want should work out. Excellent day to be with friends—desire to participate in group consciousness. Can work harmoniously with others. Good time to reflect on life and examine goals and ideals. Relationship with authorities usually good.

**English Paraphrase**: Extremely positive—traditionally "lucky." Positive frame of mind = success. Almost anything works out. Excellent with friends—group consciousness. Work harmoniously with others. Reflect on life, examine goals. Good with authorities.

**Complete Chinese Interpretation**: 极为积极——传统上"幸运"。积极心态=成功。几乎任何事都顺利。与朋友相处极好——群体意识。与他人和谐工作。反思生活，审视目标。与权威关系良好。

**Narrative Snippets**:
- `[ns_pit_093]` `[trigger: transit_sun_sextile_natal_jupiter]` `[factor_trigger: astro_transit_sun SEXTILE natal_jupiter]` `[role: 主干]` Extremely positive—traditionally "lucky." Positive frame of mind at root of success. → PIT Ch4 Sun⚹Jupiter"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Sextile Jupiter (流年太阳六合本命木星)"
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
        l1_anchor="pit_v1.0.0_sun_sextile_jupiter__流年太阳六合本命木_001_L1",
    )
    version: str = "1.0.0"
