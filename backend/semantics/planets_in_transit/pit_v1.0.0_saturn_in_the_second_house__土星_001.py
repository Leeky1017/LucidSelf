"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.318402
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
    semantic_id="pit_v1.0.0_saturn_in_the_second_house__土星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SaturnInTheSecondHouse土星(SemanticEntry):
    """
    **Source Text** (Lines 12254-12283):
> Learn what is really important to you—psychological, spiritua...
    """
    
    original_text: str = """**Source Text** (Lines 12254-12283):
> Learn what is really important to you—psychological, spiritual, moral values may take precedence over material. Not necessarily financial loss, but may feel financially insecure. Control seems to be slipping. Work hard to keep things going. Avoid letting fear run your life—takes attention from restructuring value-system. Organize finances so don't have to pay much attention. Possessions reflect inner values—if unconscious, won't accurately reflect who you are. Discover your real needs. Be economical.

**English Paraphrase**: Learn what you truly value. May feel financially insecure but not necessarily loss. Avoid fear running your life. Restructure value-system. Possessions reflect inner values. Discover real needs. Be economical.

**Complete Chinese Interpretation**: 学习你真正看重什么。可能感觉财务不安全但不一定是损失。避免恐惧主导你的生活。重构价值体系。财产反映内在价值。发现真正的需求。要节俭。

**Narrative Snippets**:
- `[ns_pit_sa002]` `[trigger: saturn_transit_house_2]` `[factor_trigger: astro_transit_saturn AND astro_house_2]` `[role: 主干]` Learn true values. May feel financially insecure. Restructure value-system. Be economical. → PIT Ch10 Saturn-2H"""
    normalized_text_zh: str = """"""
    subject: str = "Saturn in the Second House (土星过境第二宫)"
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
        l1_anchor="pit_v1.0.0_saturn_in_the_second_house__土星_001_L1",
    )
    version: str = "1.0.0"
