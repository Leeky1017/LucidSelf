"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224474
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
    semantic_id="pit_v1.0.0_sun_opposition_jupiter__流年太阳冲本_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunOppositionJupiter流年太阳冲本(SemanticEntry):
    """
    **Source Text** (Lines 2766-2800 estimated):
> Time of culmination of Jupiter energies. Projects and...
    """
    
    original_text: str = """**Source Text** (Lines 2766-2800 estimated):
> Time of culmination of Jupiter energies. Projects and activities reach climax. Examine how well you've handled them. Your ability to work with others and get along with authorities is tested. May feel that you are right and others are wrong—avoid this attitude. Jupiter opposition can bring overconfidence that leads to mistakes. Be willing to acknowledge your limitations. Financial matters may reach a climax—be careful with speculation.

**English Paraphrase**: Jupiter energies culminate. Projects reach climax—examine handling. Working with others/authorities tested. May feel you're right, others wrong—avoid this. Overconfidence leads to mistakes. Acknowledge limitations. Financial climax—careful with speculation.

**Complete Chinese Interpretation**: 木星能量达到顶点。项目达到高潮——检验处理方式。与他人/权威合作受到测试。可能觉得你对他人错——避免这种态度。过度自信导致错误。承认局限。财务高潮——小心投机。

**Narrative Snippets**:
- `[ns_pit_097]` `[trigger: transit_sun_opposition_natal_jupiter]` `[factor_trigger: astro_transit_sun OPPOSITION natal_jupiter]` `[role: 主干]` Jupiter energies culminate—projects reach climax. Test of working with others and authorities. → PIT Ch4 Sun☍Jupiter
- `[ns_pit_098]` `[trigger: transit_sun_opposition_natal_jupiter]` `[factor_trigger: astro_transit_sun OPPOSITION natal_jupiter]` `[role: 条件分支]` Avoid feeling you're right, others wrong. Overconfidence leads to mistakes. Acknowledge limitations. → PIT Ch4 Sun☍Jupiter"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Opposition Jupiter (流年太阳冲本命木星)"
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
        l1_anchor="pit_v1.0.0_sun_opposition_jupiter__流年太阳冲本_001_L1",
    )
    version: str = "1.0.0"
