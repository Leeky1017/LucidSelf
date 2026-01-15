"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.301121
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
    semantic_id="pit_v1.0.0_moon_conjunct_sun__流年月亮合本命太阳_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MoonConjunctSun流年月亮合本命太阳(SemanticEntry):
    """
    **Source Text** (Lines 3804-3823):
> This is like your personal "new Moon," a time when mind and bod...
    """
    
    original_text: str = """**Source Text** (Lines 3804-3823):
> This is like your personal "new Moon," a time when mind and body are recharged for the month ahead. Your feelings may be strongly influenced by larger emotional patterns that dominate your life. Usually felt as burst of energy where will, physical vitality and emotions work together harmoniously. The split between mind and feelings is not noticeable now. Group efforts favorably affected—greater sensitivity to people around you. However, if not feeling good due to longer-range transit, you may have very little energy—take time off to let energy build.

**English Paraphrase**: Personal "new Moon"—mind and body recharged. Feelings influenced by larger life patterns. Usually burst of energy—will, vitality, emotions harmonious. Mind/feelings split not noticeable. Group efforts favored—sensitivity to others. If longer transit causing problems, energy may be low—rest.

**Complete Chinese Interpretation**: 个人"新月"——身心充电。感受受更大生活模式影响。通常是能量爆发——意志、活力、情感和谐。心智/感受分裂不明显。群体活动有利——对他人敏感。如果长期行运导致问题，能量可能低——休息。

**Narrative Snippets**:
- `[ns_pit_m025]` `[trigger: transit_moon_conjunct_natal_sun]` `[factor_trigger: astro_transit_moon CONJUNCT natal_sun]` `[role: 主干]` Personal "new Moon"—mind and body recharged. Will, vitality, emotions work harmoniously. → PIT Ch5 Moon☌Sun"""
    normalized_text_zh: str = """"""
    subject: str = "Moon Conjunct Sun (流年月亮合本命太阳)"
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
        l1_anchor="pit_v1.0.0_moon_conjunct_sun__流年月亮合本命太阳_001_L1",
    )
    version: str = "1.0.0"
