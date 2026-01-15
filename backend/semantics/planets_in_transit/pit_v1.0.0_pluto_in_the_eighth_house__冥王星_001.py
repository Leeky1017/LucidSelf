"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.238019
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
    semantic_id="pit_v1.0.0_pluto_in_the_eighth_house__冥王星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class PlutoInTheEighthHouse冥王星(SemanticEntry):
    """
    **Source Text** (Lines 18986-19009):
> Pluto is "at home"—symbolism closely related to eighth house....
    """
    
    original_text: str = """**Source Text** (Lines 18986-19009):
> Pluto is "at home"—symbolism closely related to eighth house. Both relate to death and resurrection symbolically and literally. Issues of major transformation—even death, rebirth, regeneration—more significant than ever. Your own life not in great danger, but deaths of people around you may have important effect. Such a death may radically change circumstances or force confrontation about nature and meaning of your life. Concerns become quite deep. May become involved in occult or teachings about life and death. Difficult to accept explanations that don't get to very bottom of matter. Seeking answers to mysteries. On different level: can affect possessions and resources held jointly—spouse's finances, corporate finances. Major change may occur through these sources. Not good time to go into debt—indebtedness puts you under someone else's control. One possibility combining both themes: inheritance (if other transits and natal indications support).

**English Paraphrase**: Pluto at home. Death/rebirth themes significant. Deaths around you may change your life. Concerns become deep—seek mysteries. Joint finances may change. Avoid debt. Inheritance possible.

**Complete Chinese Interpretation**: 冥王星在本宫。死亡/重生主题重要。周围的死亡可能改变你的生活。关注变得深刻——寻求神秘。共同财务可能改变。避免债务。可能有遗产。

**Narrative Snippets**:
- `[ns_pit_pl008]` `[trigger: pluto_transit_house_8]` `[factor_trigger: astro_house_8 AND astro_deep_transformation]` `[role: 主干]` Death/rebirth themes significant. Seek mysteries. Joint finances change. Avoid debt. → PIT Ch13 Pluto-8H"""
    normalized_text_zh: str = """"""
    subject: str = "Pluto in the Eighth House (冥王星过境第八宫)"
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
        l1_anchor="pit_v1.0.0_pluto_in_the_eighth_house__冥王星_001_L1",
    )
    version: str = "1.0.0"
