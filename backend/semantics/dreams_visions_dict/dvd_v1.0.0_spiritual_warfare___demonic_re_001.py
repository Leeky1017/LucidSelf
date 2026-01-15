"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.414649
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
    semantic_id="dvd_v1.0.0_spiritual_warfare___demonic_re_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class SpiritualWarfareDemonicRe(SemanticEntry):
    """
    **English**: Dark figures = demons, attacks = enemy assault, weapons = armor needed. Two types: atta...
    """
    
    original_text: str = """**English**: Dark figures = demons, attacks = enemy assault, weapons = armor needed. Two types: attack dreams (defend) vs intercession dreams (pray for others).
**Chinese**: 黑暗人物=魔鬼、攻击=仇敌突袭、武器=需军装。两类：攻击梦(防御) vs 代祷梦(为他人祷告)。
**Core**: Ephesians 6:12. Christian-specific (not in Jung/Freud). East: 灵性争战(Christian) vs 心魔(Buddhist)"""
    normalized_text_zh: str = """"""
    subject: str = "Spiritual Warfare - Demonic Reality"
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
        book_id="dreams_visions_dict",
        chapter="",
        l1_anchor="dvd_v1.0.0_spiritual_warfare___demonic_re_001_L1",
    )
    version: str = "1.0.0"
