"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.301024
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
    semantic_id="pit_v1.0.0_moon_in_the_fifth_house__月亮过境第_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonInTheFifthHouse月亮过境第(SemanticEntry):
    """
    **Source Text** (Lines 3648-3666):
> Very difficult to conceal your feelings from others—and you sho...
    """
    
    original_text: str = """**Source Text** (Lines 3648-3666):
> Very difficult to conceal your feelings from others—and you shouldn't try. You need to be yourself now and feel what you really are. In love relationships, greater emotional depth and intensity. Watch excessive possessiveness or being wrapped up in your own feelings. Relations with women generally improved. May arouse protective and nurturing instincts toward children or loved ones. Don't let protection deprive someone of individual responsibility.

**English Paraphrase**: Can't conceal feelings—don't try. Need to be yourself. Love relationships gain emotional depth and intensity. Watch possessiveness. Relations with women improved. Protective/nurturing instincts aroused. Don't overprotect.

**Complete Chinese Interpretation**: 无法隐藏感受——不要尝试。需要做自己。爱情关系获得情感深度和强度。注意占有欲。与女性关系改善。保护/养育本能被唤醒。不要过度保护。

**Narrative Snippets**:
- `[ns_pit_m009]` `[trigger: moon_transit_house_5]` `[factor_trigger: astro_transit_moon AND astro_house_5]` `[role: 主干]` Can't conceal feelings—need to be yourself. Love relationships gain depth and intensity. → PIT Ch5 Moon-5H
- `[ns_pit_m010]` `[trigger: moon_transit_house_5]` `[factor_trigger: astro_transit_moon AND astro_house_5]` `[role: 条件分支]` Protective instincts aroused—don't overprotect or deprive others of responsibility. → PIT Ch5 Moon-5H"""
    normalized_text_zh: str = """"""
    subject: str = "Moon in the Fifth House (月亮过境第五宫)"
    factor_refs: list = ['state_emotional_transparency', 'state_protective_instinct', 'boundary_overprotection']
    
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
        l1_anchor="pit_v1.0.0_moon_in_the_fifth_house__月亮过境第_001_L1",
    )
    version: str = "1.0.0"
