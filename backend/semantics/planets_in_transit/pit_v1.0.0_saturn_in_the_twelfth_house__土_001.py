"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.318520
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
    semantic_id="pit_v1.0.0_saturn_in_the_twelfth_house__土_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SaturnInTheTwelfthHouse土(SemanticEntry):
    """
    **Source Text** (Lines 12573-12601):
> Decks cleared for new action. Finishing anything not done com...
    """
    
    original_text: str = """**Source Text** (Lines 12573-12601):
> Decks cleared for new action. Finishing anything not done completely. Not good for starting new projects—energy not there. Circumstances compel finishing phase. Important life elements may pass away. Activities that worked no longer do. Old ways of handling people no longer achieve response. Impression that must change everything but don't know how. Tendency to "withdraw" to get in tune. Important to understand accomplishments and failures—don't judge, simply observe. If life hasn't succeeded per expectations in 10H/11H, now opportunity to clear barriers. But won't bear fruit immediately—end of cycle not beginning. Tempting to fall into despair over "failures." Neither productive nor therapeutic. Clear away leftovers, make ready for new start. Feel pressures for tremendous changes—heed them as signs of new order beginning.

**English Paraphrase**: Clearing phase—finish incomplete matters. Not good for new projects. Old ways stop working. Withdraw to tune in. Observe accomplishments/failures without judgment. Clear barriers. End of cycle—don't despair. Prepare for new beginning. Pressures for change signal new order.

**Complete Chinese Interpretation**: 清理阶段——完成未完成的事务。不适合新项目。旧方式停止工作。退缩以调整。不带判断地观察成就/失败。清除障碍。周期结束——不要绝望。为新的开始做准备。变化的压力预示新秩序。

**Narrative Snippets**:
- `[ns_pit_sa012]` `[trigger: saturn_transit_house_12]` `[factor_trigger: astro_transit_saturn AND astro_house_12]` `[role: 主干]` Clearing phase. Finish incomplete matters. Observe without judgment. Prepare for new cycle. → PIT Ch10 Saturn-12H"""
    normalized_text_zh: str = """"""
    subject: str = "Saturn in the Twelfth House (土星过境第十二宫)"
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
        l1_anchor="pit_v1.0.0_saturn_in_the_twelfth_house__土_001_L1",
    )
    version: str = "1.0.0"
