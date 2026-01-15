"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224206
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
    semantic_id="pit_v1.0.0_sun_conjunct_mercury__流年太阳合本命水_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunConjunctMercury流年太阳合本命水(SemanticEntry):
    """
    **Source Text** (Lines 2292-2322):
> This transit emphasizes Mercury-ruled areas. You are likely to ...
    """
    
    original_text: str = """**Source Text** (Lines 2292-2322):
> This transit emphasizes Mercury-ruled areas. You are likely to have many more conversations. This is an opportunity to get your point of view across. You may be more involved in sending or receiving letters. Good time for routine paperwork—mind clearer than usual.
> 
> Excellent day for starting a new business venture. Mercury rules commerce and favors rapid interchange. This is a good time to make plans for the future. You may also travel today—an activated Mercury creates restless tension.

**English Paraphrase**: Emphasizes Mercury-ruled areas: conversations, letters, paperwork. Mind clearer than usual. Excellent for new business ventures—Mercury rules commerce. Good for future planning. May travel—activated Mercury creates restless tension.

**Complete Chinese Interpretation**: 强调水星主宰的领域：对话、信件、文书工作。头脑比平时更清晰。对新商业项目极好——水星主宰商业。适合规划未来。可能旅行——激活的水星创造不安的紧张。

**Narrative Snippets**:
- `[ns_pit_065]` `[trigger: transit_sun_conjunct_natal_mercury]` `[factor_trigger: astro_transit_sun CONJUNCT natal_mercury]` `[role: 主干]` Emphasizes Mercury areas—many conversations, mind clearer than usual, good for paperwork. → PIT Ch4 Sun☌Mercury
- `[ns_pit_066]` `[trigger: transit_sun_conjunct_natal_mercury]` `[factor_trigger: astro_transit_sun CONJUNCT natal_mercury]` `[role: 主干依赖]` Excellent for new business ventures and future planning. May travel—Mercury creates restless tension. → PIT Ch4 Sun☌Mercury"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Conjunct Mercury (流年太阳合本命水星)"
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
        l1_anchor="pit_v1.0.0_sun_conjunct_mercury__流年太阳合本命水_001_L1",
    )
    version: str = "1.0.0"
