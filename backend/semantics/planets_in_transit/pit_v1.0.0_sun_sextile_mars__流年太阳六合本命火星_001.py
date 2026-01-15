"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224388
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
    semantic_id="pit_v1.0.0_sun_sextile_mars__流年太阳六合本命火星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunSextileMars流年太阳六合本命火星(SemanticEntry):
    """
    **Source Text** (Lines 2564-2584):
> Excellent time for accomplishing all kinds of work. Energy high...
    """
    
    original_text: str = """**Source Text** (Lines 2564-2584):
> Excellent time for accomplishing all kinds of work. Energy high, faith in ability to achieve. Health usually good—favorable for physical activity. Very bad NOT to be physically active—these energies must have outlet. Can work well with others—ego energies well balanced. May create opportunity for leadership or authority over others. Derive most satisfaction through expressing needs of people you work with.

**English Paraphrase**: Excellent for work accomplishment. High energy, faith in ability. Health good—need physical activity. Work well with others—ego balanced. May create leadership opportunity. Satisfaction through expressing group needs.

**Complete Chinese Interpretation**: 对工作成就极好。高能量，对能力有信心。健康良好——需要体力活动。与他人合作良好——自我平衡。可能创造领导机会。通过表达群体需求获得满足。

**Narrative Snippets**:
- `[ns_pit_084]` `[trigger: transit_sun_sextile_natal_mars]` `[factor_trigger: astro_transit_sun SEXTILE natal_mars]` `[role: 主干]` Excellent for work—high energy, faith in ability. Health good; need physical activity. Work well with others. → PIT Ch4 Sun⚹Mars"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Sextile Mars (流年太阳六合本命火星)"
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
        l1_anchor="pit_v1.0.0_sun_sextile_mars__流年太阳六合本命火星_001_L1",
    )
    version: str = "1.0.0"
