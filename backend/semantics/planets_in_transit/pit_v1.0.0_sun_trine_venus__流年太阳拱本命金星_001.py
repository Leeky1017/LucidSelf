"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224345
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
    semantic_id="pit_v1.0.0_sun_trine_venus__流年太阳拱本命金星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunTrineVenus流年太阳拱本命金星(SemanticEntry):
    """
    **Source Text** (Lines 2490-2512):
> Very positive transit—feel good physically and emotionally. Des...
    """
    
    original_text: str = """**Source Text** (Lines 2490-2512):
> Very positive transit—feel good physically and emotionally. Desire for complete self-expression through creative activity, love, good times. Influence so light-hearted that serious projects are difficult. This is a recreational transit. Great sensitivity to beauty; good for buying clothing, art, redecorating. Strong desire to gratify senses without being compulsive. Relationships positively affected—might start new romantic interest. Very affectionate with loved ones; smooth out difficulties.

**English Paraphrase**: Very positive—feel good physically and emotionally. Desire creative self-expression, love, good times. Light-hearted—recreational transit. Sensitivity to beauty; good for buying/redecorating. Relationships positive; possible new romance. Very affectionate; smooth out difficulties.

**Complete Chinese Interpretation**: 非常积极——身心感觉良好。渴望通过创意、爱、美好时光自我表达。轻松——休闲行运。对美敏感；适合购物/装饰。关系积极；可能有新恋情。非常深情；平息困难。

**Narrative Snippets**:
- `[ns_pit_078]` `[trigger: transit_sun_trine_natal_venus]` `[factor_trigger: astro_transit_sun TRINE natal_venus]` `[role: 主干]` Very positive—feel good, desire creative self-expression, love, good times. Recreational transit. → PIT Ch4 Sun△Venus
- `[ns_pit_079]` `[trigger: transit_sun_trine_natal_venus]` `[factor_trigger: astro_transit_sun TRINE natal_venus]` `[role: 主干依赖]` Relationships positively affected. Sensitivity to beauty—good for buying, redecorating. → PIT Ch4 Sun△Venus"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Trine Venus (流年太阳拱本命金星)"
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
        l1_anchor="pit_v1.0.0_sun_trine_venus__流年太阳拱本命金星_001_L1",
    )
    version: str = "1.0.0"
