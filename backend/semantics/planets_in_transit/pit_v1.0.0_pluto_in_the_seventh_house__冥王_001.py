"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.237998
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
    semantic_id="pit_v1.0.0_pluto_in_the_seventh_house__冥王_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class PlutoInTheSeventhHouse冥王(SemanticEntry):
    """
    **Source Text** (Lines 18948-18985):
> Either all relationships and partnerships go through profound...
    """
    
    original_text: str = """**Source Text** (Lines 18948-18985):
> Either all relationships and partnerships go through profound transformations, or life transformed through close encounter with another person. Includes marriage, partnerships, enemies, consultants, any one-to-one relationship. In marriage: profound change through or within relationship—may reach crisis requiring redefinition. Long-hidden tensions must be released. Not basically sound marriage/partnership probably won't survive. Not particularly good time to start partnership or marriage—energies make it difficult to settle into comfortable routine. In marriage, may operate under unconscious compulsions making it difficult to create structure in your interests. Some people need emotional intensity—for them, marriage okay. Encounters with professional consultants may bring significant life changes. Pluto transiting often coincides with psychotherapy—don't expect therapist to do all the work. Important to avoid power struggles with enemies—likely extremely nasty and destructive. If involved, expect opponent to use every sneaky device. Don't reciprocate—you wouldn't be successful. More likely to receive underhanded treatment than give it. People you encounter are mirrors of inner psychic impulses. Stop attributing everything to others—recognize you trigger encounters by subtle unconscious cues.

**English Paraphrase**: Relationships undergo profound transformation. Marriage may reach crisis. Not good to start new partnerships. Consultants may transform life. Avoid power struggles with enemies. People encountered are mirrors of inner impulses—you trigger encounters unconsciously.

**Complete Chinese Interpretation**: 关系经历深刻转变。婚姻可能达到危机。不适合开始新的伙伴关系。顾问可能改变生活。避免与敌人的权力斗争。遇到的人是内在冲动的镜子——你无意识地触发相遇。

**Narrative Snippets**:
- `[ns_pit_pl007]` `[trigger: pluto_transit_house_7]` `[factor_trigger: astro_house_7 AND astro_relationship_power]` `[role: 主干]` Relationships transform profoundly. May reach crisis. Others mirror your unconscious. → PIT Ch13 Pluto-7H"""
    normalized_text_zh: str = """"""
    subject: str = "Pluto in the Seventh House (冥王星过境第七宫)"
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
        l1_anchor="pit_v1.0.0_pluto_in_the_seventh_house__冥王_001_L1",
    )
    version: str = "1.0.0"
