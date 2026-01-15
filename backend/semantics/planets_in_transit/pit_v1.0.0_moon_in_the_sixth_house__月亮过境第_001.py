"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.301036
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
    semantic_id="pit_v1.0.0_moon_in_the_sixth_house__月亮过境第_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonInTheSixthHouse月亮过境第(SemanticEntry):
    """
    **Source Text** (Lines 3667-3687):
> Inclined to put emotional considerations second to immediate ne...
    """
    
    original_text: str = """**Source Text** (Lines 3667-3687):
> Inclined to put emotional considerations second to immediate necessities. Contradictory energy—Moon's need for personal contact conflicts with sixth house self-denial. Emotional repression is probable. Can signify attention to home crafts, personal hygiene, home care, reorganization. If emotional repression, may become hypercritical or play the "martyr game." Better to put feelings on the line. May occupy attention with personal health—don't become hypochondriac.

**English Paraphrase**: Put emotions second to necessities. Contradictory—Moon's needs vs 6H self-denial. Emotional repression probable. Good for home crafts, hygiene, reorganization. Repression → hypercritical or martyr games. Better to express feelings. Health focus—don't become hypochondriac.

**Complete Chinese Interpretation**: 把情感放在必需之后。矛盾——月亮的需求vs第六宫自我否定。情感压抑可能。适合家务、卫生、重组。压抑→过度批评或殉道游戏。最好表达感受。健康关注——不要变成疑病症。

**Narrative Snippets**:
- `[ns_pit_m011]` `[trigger: moon_transit_house_6]` `[factor_trigger: astro_transit_moon AND astro_house_6]` `[role: 主干]` Put emotions second to necessities—contradictory energy, emotional repression probable. → PIT Ch5 Moon-6H
- `[ns_pit_m012]` `[trigger: moon_transit_house_6]` `[factor_trigger: astro_transit_moon AND astro_house_6]` `[role: 条件分支]` May become hypercritical or play martyr game. Better to express feelings directly. → PIT Ch5 Moon-6H"""
    normalized_text_zh: str = """"""
    subject: str = "Moon in the Sixth House (月亮过境第六宫)"
    factor_refs: list = ['state_emotional_repression', 'pattern_martyr_game', 'state_hypercritical']
    
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
        l1_anchor="pit_v1.0.0_moon_in_the_sixth_house__月亮过境第_001_L1",
    )
    version: str = "1.0.0"
