"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.206596
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
    semantic_id="pit_v1.0.0_uranus_in_the_third_house__天王星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class UranusInTheThirdHouse天王星(SemanticEntry):
    """
    **Source Text** (Lines 14484-14523):
> Focus of change on everyday encounters—neighbors, relatives, ...
    """
    
    original_text: str = """**Source Text** (Lines 14484-14523):
> Focus of change on everyday encounters—neighbors, relatives, friends, daily routines. Everyday mental attitudes will change. See things never seen before, communicate in new ways. If involved in intellectual pursuits, exciting time. Old habits of thinking fall away. New interests, particularly Uranian—sciences, technology, yoga, astrology, occult. Tempo of events increases. Can't take much for granted. Little details contain germ of revolutionizing consciousness. If afraid of change, everything upsetting; if flexible, nothing terrible, only new. Signs come through daily communication. Short trips may produce unexpected events. Beginning of fundamental reorientation of inner self.

**English Paraphrase**: Everyday encounters change. Mental attitudes shift. Old thinking habits fall away. Uranian interests attract. Tempo increases. Details contain seeds of revolution. Be flexible. Signs through daily communication.

**Complete Chinese Interpretation**: 日常遭遇改变。心理态度转变。旧思维习惯消失。天王星兴趣吸引。节奏加快。细节包含革命的种子。要灵活。通过日常沟通获得信号。

**Narrative Snippets**:
- `[ns_pit_ur003]` `[trigger: uranus_transit_house_3]` `[factor_trigger: astro_transit_uranus AND astro_house_3]` `[role: 主干]` Everyday mental attitudes change. Uranian interests. Tempo increases. Be flexible. → PIT Ch11 Uranus-3H"""
    normalized_text_zh: str = """"""
    subject: str = "Uranus in the Third House (天王星过境第三宫)"
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
        l1_anchor="pit_v1.0.0_uranus_in_the_third_house__天王星_001_L1",
    )
    version: str = "1.0.0"
