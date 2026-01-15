"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.301048
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
    semantic_id="pit_v1.0.0_moon_in_the_seventh_house__月亮过_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonInTheSeventhHouse月亮过(SemanticEntry):
    """
    **Source Text** (Lines 3688-3707):
> Turn attention to most personal relationships with more emotion...
    """
    
    original_text: str = """**Source Text** (Lines 3688-3707):
> Turn attention to most personal relationships with more emotional expression than usual. Affects marriage, opponents, any emotional confrontation. Loved ones provide security and support—and you want to provide these for them too. If in negative emotional state, may become excessively jealous and possessive or act unconsciously with loved ones. Conflicts more emotional, difficult to maintain detachment. Opponents can manipulate by controlling your feelings. Look upon confrontations as opportunity to see unconscious parts of yourself.

**English Paraphrase**: Attention to personal relationships, more emotional. Marriage, opponents, emotional confrontations affected. Loved ones provide security—you want to provide too. Negative state → jealous, possessive, unconscious. Conflicts emotional, hard to detach. Opponents can manipulate your feelings. Confrontations reveal unconscious self.

**Complete Chinese Interpretation**: 关注个人关系，更情绪化。婚姻、对手、情感对抗受影响。爱人提供安全——你也想提供。负面状态→嫉妒、占有、无意识。冲突情绪化，难以超脱。对手可以操控你的感受。对抗揭示无意识自我。

**Narrative Snippets**:
- `[ns_pit_m013]` `[trigger: moon_transit_house_7]` `[factor_trigger: astro_transit_moon AND astro_house_7]` `[role: 主干]` Attention to personal relationships—more emotional than usual. Loved ones provide security. → PIT Ch5 Moon-7H
- `[ns_pit_m014]` `[trigger: moon_transit_house_7]` `[factor_trigger: astro_transit_moon AND astro_house_7]` `[role: 条件分支]` Negative state → jealous, possessive. Opponents can manipulate your feelings. Confrontations reveal unconscious self. → PIT Ch5 Moon-7H"""
    normalized_text_zh: str = """"""
    subject: str = "Moon in the Seventh House (月亮过境第七宫)"
    factor_refs: list = ['state_relationship_emotional', 'pattern_emotional_manipulation', 'pattern_confrontation_mirror']
    
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
        l1_anchor="pit_v1.0.0_moon_in_the_seventh_house__月亮过_001_L1",
    )
    version: str = "1.0.0"
