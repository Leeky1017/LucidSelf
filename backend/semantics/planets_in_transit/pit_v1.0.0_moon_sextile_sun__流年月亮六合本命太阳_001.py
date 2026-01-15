"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.301132
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
    semantic_id="pit_v1.0.0_moon_sextile_sun__流年月亮六合本命太阳_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonSextileSun流年月亮六合本命太阳(SemanticEntry):
    """
    **Source Text** (Lines 3824-3840):
> Time of inner and outer equanimity. You can stop and take stock...
    """
    
    original_text: str = """**Source Text** (Lines 3824-3840):
> Time of inner and outer equanimity. You can stop and take stock of yourself without feeling caught up in usual turmoil. Even if affairs aren't going smoothly, this provides breathing space. Relationships with groups and friends quite good—understand others' needs without losing sight of your own. Relations with opposite sex good—able to make friends and establish emotional communion. Opportunities may arise from unexpected corners through friends.

**English Paraphrase**: Inner and outer equanimity—breathing space. Can take stock of self. Good with groups and friends—understand others without losing yourself. Opposite sex relations good. Opportunities through friends.

**Complete Chinese Interpretation**: 内外平衡——喘息空间。可以盘点自我。与群体和朋友相处良好——理解他人而不失去自己。与异性关系好。通过朋友的机会。

**Narrative Snippets**:
- `[ns_pit_m026]` `[trigger: transit_moon_sextile_natal_sun]` `[factor_trigger: astro_transit_moon SEXTILE natal_sun]` `[role: 主干]` Inner and outer equanimity—breathing space. Good with groups and friends. → PIT Ch5 Moon⚹Sun"""
    normalized_text_zh: str = """"""
    subject: str = "Moon Sextile Sun (流年月亮六合本命太阳)"
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
        l1_anchor="pit_v1.0.0_moon_sextile_sun__流年月亮六合本命太阳_001_L1",
    )
    version: str = "1.0.0"
