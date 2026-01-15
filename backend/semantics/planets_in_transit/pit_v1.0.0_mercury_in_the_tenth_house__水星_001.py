"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.280811
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
    semantic_id="pit_v1.0.0_mercury_in_the_tenth_house__水星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MercuryInTheTenthHouse水星(SemanticEntry):
    """
    **Source Text** (Lines 5187-5212):
> Make plans concerning professional life. Think about whether wh...
    """
    
    original_text: str = """**Source Text** (Lines 5187-5212):
> Make plans concerning professional life. Think about whether what you're doing is working out. Plan changes if necessary. Good time for new career studies. Good to talk to superiors about work and advancement. Communications on job assume greater importance—but avoid red tape. May become involved with advertising or contract negotiations.

**English Paraphrase**: Plan professional life. Evaluate if career working. Study for career advancement. Talk to superiors. Communications important—avoid red tape. Advertising or negotiations possible.

**Complete Chinese Interpretation**: 计划职业生活。评估职业是否有效。为职业发展学习。与上级交谈。沟通重要——避免繁文缛节。可能涉及广告或谈判。

**Narrative Snippets**:
- `[ns_pit_me011]` `[trigger: mercury_transit_house_10]` `[factor_trigger: astro_transit_mercury AND astro_house_10]` `[role: 主干]` Plan professional life. Talk to superiors. Communications important on job. → PIT Ch6 Mercury-10H"""
    normalized_text_zh: str = """"""
    subject: str = "Mercury in the Tenth House (水星过境第十宫)"
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
        l1_anchor="pit_v1.0.0_mercury_in_the_tenth_house__水星_001_L1",
    )
    version: str = "1.0.0"
