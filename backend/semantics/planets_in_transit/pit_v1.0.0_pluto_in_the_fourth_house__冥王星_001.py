"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.237945
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
    semantic_id="pit_v1.0.0_pluto_in_the_fourth_house__冥王星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class PlutoInTheFourthHouse冥王星(SemanticEntry):
    """
    **Source Text** (Lines 18855-18881):
> Tremendous psychological changes continue from 3H—now deeper,...
    """
    
    original_text: str = """**Source Text** (Lines 18855-18881):
> Tremendous psychological changes continue from 3H—now deeper, more internal and personal. Inner psyche, home, family, most personal areas affected. Psychological level: may deal at last with problems lived with since childhood. Issues from childhood reemerge—understand consequences as adult. No longer satisfied just to live with them—want change, and can change at most fundamental levels. Irrational compulsions and inappropriate childish behavior called into light. Excellent period for psychotherapy. Even without, will undergo tremendous inward changes. On exterior: home life may change tremendously—change of residence, extensive repair/remodeling, divorce/death/separations, tremendous change in family relationships. Relationships with parents likely to change—if overly dependent, may need to break away. May have power struggle with parents if they try to hold on. Changes need not be negative—certainly will be significant, new order will begin.

**English Paraphrase**: Deeper psychological changes. Home, family, inner psyche affected. Childhood issues reemerge—can change at fundamental levels. Excellent for therapy. Home life may change—residence, family structure, parent relationships. Power struggles possible. New order begins.

**Complete Chinese Interpretation**: 更深层的心理变化。家庭、家人、内在心灵受影响。童年问题重新出现——可以在根本层面改变。适合治疗。家庭生活可能改变——住所、家庭结构、与父母的关系。可能有权力斗争。新秩序开始。

**Narrative Snippets**:
- `[ns_pit_pl004]` `[trigger: pluto_transit_house_4]` `[factor_trigger: astro_transit_pluto AND astro_house_4]` `[role: 主干]` Deep psychological changes. Home/family transformed. Childhood issues surface. New order begins. → PIT Ch13 Pluto-4H"""
    normalized_text_zh: str = """"""
    subject: str = "Pluto in the Fourth House (冥王星过境第四宫)"
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
        l1_anchor="pit_v1.0.0_pluto_in_the_fourth_house__冥王星_001_L1",
    )
    version: str = "1.0.0"
