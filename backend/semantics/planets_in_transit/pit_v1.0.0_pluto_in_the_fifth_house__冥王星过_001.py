"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.237963
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
    semantic_id="pit_v1.0.0_pluto_in_the_fifth_house__冥王星过_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class PlutoInTheFifthHouse冥王星过(SemanticEntry):
    """
    **Source Text** (Lines 18882-18915):
> Many consequences—fifth house rules recreation/amusement and ...
    """
    
    original_text: str = """**Source Text** (Lines 18882-18915):
> Many consequences—fifth house rules recreation/amusement and children (re-creation of self). If have children, likely fateful period with them—not necessarily bad. Everything you do with them will have powerful effect later. Be careful, use common sense. Specifically: periods of tension—power struggles with children as you apply too much pressure or vice versa. If severe afflictions, can be dangerous period for children—don't take unnecessary risks with their health. Fifth also house of love affairs—early phase of relationship as opposed to serious commitment. With Pluto, love affair likely very heavy, emotionally intense. May regard relationships as fated—could distort sense of proportion. Beware of fascination with someone you know isn't good for you—subconscious playing tricks. Existing relationship will be very intense and go through complete change. Relationship in severe trouble unlikely to survive—if it does, will last forever. Fifth also creative self-expression—attracted to powerful, involving activities, even carrying risk, because want to experience everything intensely. Superficial doesn't attract.

**English Paraphrase**: Fateful period with children—be careful. Power struggles possible. Love affairs intense, heavy, fated—may distort proportion. Beware fascination with wrong person. Existing relationships transform or end permanently. Attracted to intense experiences and creative expression.

**Complete Chinese Interpretation**: 与孩子的命运时期——要小心。可能有权力斗争。爱情关系强烈、沉重、命中注定——可能扭曲比例。警惕对错误的人的迷恋。现有关系转变或永久结束。被强烈体验和创意表达吸引。

**Narrative Snippets**:
- `[ns_pit_pl005]` `[trigger: pluto_transit_house_5]` `[factor_trigger: astro_transit_pluto AND astro_house_5]` `[role: 主干]` Fateful with children. Love affairs intense and transformative. Attracted to intense experiences. → PIT Ch13 Pluto-5H"""
    normalized_text_zh: str = """"""
    subject: str = "Pluto in the Fifth House (冥王星过境第五宫)"
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
        l1_anchor="pit_v1.0.0_pluto_in_the_fifth_house__冥王星过_001_L1",
    )
    version: str = "1.0.0"
