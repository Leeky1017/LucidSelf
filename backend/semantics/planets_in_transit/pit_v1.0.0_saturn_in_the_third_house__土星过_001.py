"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.318415
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
    semantic_id="pit_v1.0.0_saturn_in_the_third_house__土星过_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SaturnInTheThirdHouse土星过(SemanticEntry):
    """
    **Source Text** (Lines 12284-12321):
> Completes phase of inward preparation. Main issue: structurin...
    """
    
    original_text: str = """**Source Text** (Lines 12284-12321):
> Completes phase of inward preparation. Main issue: structuring of your mind—everyday mental patterns, attitudes, habits, speaking and listening styles. Normally take these for granted. Need to understand to gain greater control over daily life. May need extensive changes. May have trouble with people in immediate environment, relatives, neighbors. May become discouraged, unable to communicate as readily. Learn to see what is happening dispassionately without value judgments. As completes, attention moves away from inner truths to how inner relates to outer.

**English Paraphrase**: Completes inward phase. Structure your mind—patterns, attitudes, habits, communication. May need changes, trouble with relatives/neighbors. May feel discouraged. See without judgment. Then attention shifts to inner-outer relationship.

**Complete Chinese Interpretation**: 完成内向阶段。构建你的思维——模式、态度、习惯、沟通。可能需要改变，与亲戚/邻居有麻烦。可能感到沮丧。不带判断地看。然后注意力转向内外关系。

**Narrative Snippets**:
- `[ns_pit_sa003]` `[trigger: saturn_transit_house_3]` `[factor_trigger: astro_transit_saturn AND astro_house_3]` `[role: 主干]` Structure your mind—patterns, habits, communication. May need changes. See without judgment. → PIT Ch10 Saturn-3H"""
    normalized_text_zh: str = """"""
    subject: str = "Saturn in the Third House (土星过境第三宫)"
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
        l1_anchor="pit_v1.0.0_saturn_in_the_third_house__土星过_001_L1",
    )
    version: str = "1.0.0"
