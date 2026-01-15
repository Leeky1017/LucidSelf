"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.287950
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
    semantic_id="pit_v1.0.0_mars_in_the_third_house__火星过境第_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MarsInTheThirdHouse火星过境第(SemanticEntry):
    """
    **Source Text** (Lines 8323-8348):
> Tempo of everyday life picks up considerably. Danger of conflic...
    """
    
    original_text: str = """**Source Text** (Lines 8323-8348):
> Tempo of everyday life picks up considerably. Danger of conflicts with neighbors, relatives, daily contacts. But may accomplish things together. Identify strongly with ideas and opinions—argumentative. Defending positions that don't need defending. Beware coercing others into believing as you do. Good for "selling" ideas with power. Good for vigorous mental work.

**English Paraphrase**: Everyday tempo picks up. Conflicts with neighbors/relatives possible. Argumentative about ideas. Don't coerce. Good for selling ideas and vigorous mental work.

**Complete Chinese Interpretation**: 日常节奏加快。可能与邻居/亲戚冲突。对想法好争论。不要强迫。适合推销想法和积极的脑力工作。

**Narrative Snippets**:
- `[ns_pit_ma003]` `[trigger: mars_transit_house_3]` `[factor_trigger: astro_transit_mars AND astro_house_3]` `[role: 主干]` Everyday tempo picks up. Argumentative. Good for selling ideas and mental work. → PIT Ch8 Mars-3H"""
    normalized_text_zh: str = """"""
    subject: str = "Mars in the Third House (火星过境第三宫)"
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
        l1_anchor="pit_v1.0.0_mars_in_the_third_house__火星过境第_001_L1",
    )
    version: str = "1.0.0"
