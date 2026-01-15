"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224272
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
    semantic_id="pit_v1.0.0_sun_sextile_venus__流年太阳六合本命金星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunSextileVenus流年太阳六合本命金星(SemanticEntry):
    """
    **Source Text** (Lines 2444-2464):
> Feel good and affectionate toward everyone around you. Spend ti...
    """
    
    original_text: str = """**Source Text** (Lines 2444-2464):
> Feel good and affectionate toward everyone around you. Spend time with friends, try to make new ones. Appreciate how much love you give and receive. If tensions in relationships, smooth them over now. You'll be quite popular—use positive energies to make good impressions. Friendships important—opportunities may arise from friendship. Good transit for most financial matters.

**English Paraphrase**: Feel good and affectionate. Spend time with friends; appreciate love given/received. Smooth over relationship tensions. Popular—make good impressions. Friendship opportunities. Good for financial matters.

**Complete Chinese Interpretation**: 感觉良好且充满感情。与朋友共度时光；欣赏给予/接受的爱。平息关系紧张。受欢迎——留下好印象。友谊机会。对财务事项有利。

**Narrative Snippets**:
- `[ns_pit_075]` `[trigger: transit_sun_sextile_natal_venus]` `[factor_trigger: astro_transit_sun SEXTILE natal_venus]` `[role: 主干]` Feel good and affectionate—smooth over relationship tensions, quite popular. Friendship opportunities. → PIT Ch4 Sun⚹Venus"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Sextile Venus (流年太阳六合本命金星)"
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
        l1_anchor="pit_v1.0.0_sun_sextile_venus__流年太阳六合本命金星_001_L1",
    )
    version: str = "1.0.0"
