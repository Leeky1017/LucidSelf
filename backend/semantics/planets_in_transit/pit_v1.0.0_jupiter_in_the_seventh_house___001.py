"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.309799
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
    semantic_id="pit_v1.0.0_jupiter_in_the_seventh_house___001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class JupiterInTheSeventhHouse(SemanticEntry):
    """
    **Source Text** (Lines 10350-10381):
> Intimate encounters show you aspects of yourself and world. F...
    """
    
    original_text: str = """**Source Text** (Lines 10350-10381):
> Intimate encounters show you aspects of yourself and world. Favors formation and maintenance of all partnerships including marriage. Encounter people who can help you. Approach relationships with idea of mutual help. Not inclined to go it alone. Good time for professional consultants—lawyer, doctor, counselor. If go to court in civil suit, outcome favorable—but cover every angle, don't overestimate. May indicate partnership with foreigner or someone very different. Any intimate relationship has consciousness-expanding effect. Marriage partner likely older, established person.

**English Paraphrase**: Partnerships favored including marriage. Meet helpful people. Mutual help approach. Good for consultants, legal matters. Don't overestimate. May partner with foreigner or different person. Consciousness-expanding relationships.

**Complete Chinese Interpretation**: 伙伴关系受青睐包括婚姻。遇到有帮助的人。互助方式。适合顾问、法律事务。不要高估。可能与外国人或不同的人合作。扩展意识的关系。

**Narrative Snippets**:
- `[ns_pit_ju007]` `[trigger: jupiter_transit_house_7]` `[factor_trigger: astro_transit_jupiter AND astro_house_7]` `[role: 主干]` Partnerships favored. Meet helpful people. Legal matters favorable. Consciousness-expanding relationships. → PIT Ch9 Jupiter-7H"""
    normalized_text_zh: str = """"""
    subject: str = "Jupiter in the Seventh House (木星过境第七宫)"
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
        l1_anchor="pit_v1.0.0_jupiter_in_the_seventh_house___001_L1",
    )
    version: str = "1.0.0"
