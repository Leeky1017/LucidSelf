"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.206518
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
    semantic_id="pit_v1.0.0_uranus_in_the_first_house__天王星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class UranusInTheFirstHouse天王星(SemanticEntry):
    """
    **Source Text** (Lines 14409-14442):
> ~7-year period. Radically redefine your relationship to outsi...
    """
    
    original_text: str = """**Source Text** (Lines 14409-14442):
> ~7-year period. Radically redefine your relationship to outside world. Old patterns broken down, people may be upset by changes. Old limitations no longer acceptable, need to change even if break away from past. Stultifying marriage/relationship may end; relationship allowing you to be yourself will be changed not destroyed. Drive for freedom—may seem pointless rebellion. Open to experiences never allowed before. Good time for astrology, yoga, human potential, consciousness-expanding techniques. If find it upsetting, ask what you're holding onto. Accidents sign of unconscious setting the stage. See what aspects are truly limiting.

**English Paraphrase**: ~7-year radical redefinition. Old patterns break down. Drive for freedom. Open to new experiences. Good for astrology, yoga, consciousness-expansion. If upsetting, ask what you're holding onto.

**Complete Chinese Interpretation**: 约7年彻底重新定义。旧模式崩溃。追求自由的驱动。对新体验开放。适合占星、瑜伽、意识扩展。如果令人不安，问问你在坚持什么。

**Narrative Snippets**:
- `[ns_pit_ur001]` `[trigger: uranus_transit_house_1]` `[factor_trigger: astro_transit_uranus AND astro_house_1]` `[role: 主干]` Radical redefinition ~7 years. Drive for freedom. Open to new experiences. Good for astrology/yoga. → PIT Ch11 Uranus-1H"""
    normalized_text_zh: str = """"""
    subject: str = "Uranus in the First House (天王星过境第一宫)"
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
        l1_anchor="pit_v1.0.0_uranus_in_the_first_house__天王星_001_L1",
    )
    version: str = "1.0.0"
