"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.301000
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
    semantic_id="pit_v1.0.0_moon_in_the_third_house__月亮过境第_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonInTheThirdHouse月亮过境第(SemanticEntry):
    """
    **Source Text** (Lines 3606-3624):
> Communications with others are very subjective, colored by pers...
    """
    
    original_text: str = """**Source Text** (Lines 3606-3624):
> Communications with others are very subjective, colored by personal considerations, not always factually accurate. But you're concerned with "gut" level communication—matters of great importance communicated through feelings. Your casual conversations have emotional depth that can make them very important. Danger: thinking influenced by past experiences and automatic reactions. Be careful not to make bad impressions through automatic reactions.

**English Paraphrase**: Subjective communications, not always accurate. Concerned with gut-level, emotional communication. Casual conversations gain depth. Danger: thinking influenced by past, automatic reactions. May make bad impressions through autopilot behavior.

**Complete Chinese Interpretation**: 主观的沟通，不总是准确。关注内心层面的情感交流。随意对话获得深度。危险：思维受过去影响，自动反应。可能因自动驾驶行为留下坏印象。

**Narrative Snippets**:
- `[ns_pit_m005]` `[trigger: moon_transit_house_3]` `[factor_trigger: astro_transit_moon AND astro_house_3]` `[role: 主干]` Communications very subjective—but concerned with gut-level emotional communication. Casual conversations gain depth. → PIT Ch5 Moon-3H
- `[ns_pit_m006]` `[trigger: moon_transit_house_3]` `[factor_trigger: astro_transit_moon AND astro_house_3]` `[role: 条件分支]` Danger: automatic reactions from past conditioning. May make bad impressions. → PIT Ch5 Moon-3H"""
    normalized_text_zh: str = """"""
    subject: str = "Moon in the Third House (月亮过境第三宫)"
    factor_refs: list = ['pattern_gut_communication', 'state_automatic_reactions', 'state_subjective_thinking']
    
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
        l1_anchor="pit_v1.0.0_moon_in_the_third_house__月亮过境第_001_L1",
    )
    version: str = "1.0.0"
