"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.288073
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
    semantic_id="pit_v1.0.0_mars_in_the_eleventh_house__火星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MarsInTheEleventhHouse火星(SemanticEntry):
    """
    **Source Text** (Lines 8541-8567):
> Formulate goals and actively pursue them. Identify ego with the...
    """
    
    original_text: str = """**Source Text** (Lines 8541-8567):
> Formulate goals and actively pursue them. Identify ego with the future. Achieve goals most effectively by working cooperatively with others. Team action is watchword. But Mars energies are individual—need balance between self-interest and others'. Find people with whom you can work. If fail, difficulties between you and friends. Resentful of group pressures. Physical activity with friends especially good.

**English Paraphrase**: Pursue goals actively. Team action but balance self vs group interests. Find compatible people. If fail, friend conflicts. Physical activity with friends good.

**Complete Chinese Interpretation**: 积极追求目标。团队行动但平衡自我vs群体利益。找到兼容的人。如果失败，与朋友冲突。与朋友的体育活动好。

**Narrative Snippets**:
- `[ns_pit_ma011]` `[trigger: mars_transit_house_11]` `[factor_trigger: astro_transit_mars AND astro_house_11]` `[role: 主干]` Pursue goals through teamwork. Balance self and group interests. → PIT Ch8 Mars-11H"""
    normalized_text_zh: str = """"""
    subject: str = "Mars in the Eleventh House (火星过境第十一宫)"
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
        l1_anchor="pit_v1.0.0_mars_in_the_eleventh_house__火星_001_L1",
    )
    version: str = "1.0.0"
