"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.258670
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
    semantic_id="pit_v1.0.0_venus_in_the_third_house__金星过境_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class VenusInTheThirdHouse金星过境(SemanticEntry):
    """
    **Source Text** (Lines 6850-6867):
> Makes everyday surroundings more pleasant. Social life picks up...
    """
    
    original_text: str = """**Source Text** (Lines 6850-6867):
> Makes everyday surroundings more pleasant. Social life picks up—get together with friends/neighbors. All dealings light and pleasant. Not discussing serious matters. Discover considerable love in everyday life. Good time to let people know how much you love them. Third house is communication. Encounter beauty in surroundings, beautify neighborhood.

**English Paraphrase**: Everyday life more pleasant. Social life picks up. Pleasant, light dealings. Discover love in daily life. Express affection through communication. Encounter and create beauty.

**Complete Chinese Interpretation**: 日常生活更愉快。社交生活活跃。愉快、轻松的交往。发现日常生活中的爱。通过沟通表达感情。遇见和创造美。

**Narrative Snippets**:
- `[ns_pit_ve003]` `[trigger: venus_transit_house_3]` `[factor_trigger: astro_transit_venus AND astro_house_3]` `[role: 主干]` Everyday life more pleasant. Social life picks up. Express love through communication. → PIT Ch7 Venus-3H"""
    normalized_text_zh: str = """"""
    subject: str = "Venus in the Third House (金星过境第三宫)"
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
        l1_anchor="pit_v1.0.0_venus_in_the_third_house__金星过境_001_L1",
    )
    version: str = "1.0.0"
