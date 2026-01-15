"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.288048
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
    semantic_id="pit_v1.0.0_mars_in_the_ninth_house__火星过境第_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MarsInTheNinthHouse火星过境第(SemanticEntry):
    """
    **Source Text** (Lines 8490-8513):
> More creative intellectual work. Assert and defend beliefs and ...
    """
    
    original_text: str = """**Source Text** (Lines 8490-8513):
> More creative intellectual work. Assert and defend beliefs and ideas. Valuable for influencing others but danger if beating people over the head. Avoid identifying ego with what you believe. Don't force religious/philosophical views on others. Put energy into expanding mind instead of defending ideas. Travel can be gratifying if no afflictions. House of law—possible legal difficulties.

**English Paraphrase**: Creative intellectual work. Assert beliefs but don't force on others. Expand mind instead of defending. Travel gratifying if no afflictions. Possible legal issues.

**Complete Chinese Interpretation**: 创造性智力工作。主张信念但不要强加于人。扩展思维而不是防守。如果没有刑克，旅行令人满足。可能的法律问题。

**Narrative Snippets**:
- `[ns_pit_ma009]` `[trigger: mars_transit_house_9]` `[factor_trigger: astro_transit_mars AND astro_house_9]` `[role: 主干]` Assert beliefs but don't force. Expand mind. Travel gratifying. Possible legal issues. → PIT Ch8 Mars-9H"""
    normalized_text_zh: str = """"""
    subject: str = "Mars in the Ninth House (火星过境第九宫)"
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
        l1_anchor="pit_v1.0.0_mars_in_the_ninth_house__火星过境第_001_L1",
    )
    version: str = "1.0.0"
