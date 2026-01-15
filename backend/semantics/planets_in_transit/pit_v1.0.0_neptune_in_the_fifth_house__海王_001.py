"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.272595
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
    semantic_id="pit_v1.0.0_neptune_in_the_fifth_house__海王_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class NeptuneInTheFifthHouse海王(SemanticEntry):
    """
    **Source Text** (Lines 16772-16801):
> Inclined to seek relationships fitting very romantic image, h...
    """
    
    original_text: str = """**Source Text** (Lines 16772-16801):
> Inclined to seek relationships fitting very romantic image, highest expectations. Sexual satisfaction may not be highest priority—concerned with spiritual union rather than purely physical. Possible to find spiritual relationship if don't confuse what you see with your ideal. Difficult pattern: idealize lover as someone who can save you from yourself—Neptunian illusion, don't take seriously. Or pattern reversed: become involved with someone who regards you as savior—exercise in futility (e.g., alcoholic lover). Try to relate as equals. Avoid risky financial ventures—fifth is house of gambling—may enjoy illusion you cannot lose, but you can and probably will. Children may be source of difficulty—illnesses or hard to understand. Avoid idealizing children—they operate from same crazy motives as adults. Transit stimulates artistic creativity—imagination improved, new ideas.

**English Paraphrase**: Seek romantic, spiritual relationships—but don't idealize. May seek savior or be seen as one—both problematic. Relate as equals. Avoid gambling—may feel can't lose but will. Children may be difficult. Artistic creativity stimulated.

**Complete Chinese Interpretation**: 寻求浪漫、精神关系——但不要理想化。可能寻求救世主或被视为救世主——都有问题。作为平等者交往。避免赌博——可能觉得不会输但会输。孩子可能困难。艺术创造力被激发。

**Narrative Snippets**:
- `[ns_pit_ne005]` `[trigger: neptune_transit_house_5]` `[factor_trigger: astro_transit_neptune AND astro_house_5]` `[role: 主干]` Romantic idealism. Don't seek/be savior. Avoid gambling. Children difficult. Artistic creativity. → PIT Ch12 Neptune-5H"""
    normalized_text_zh: str = """"""
    subject: str = "Neptune in the Fifth House (海王星过境第五宫)"
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
        l1_anchor="pit_v1.0.0_neptune_in_the_fifth_house__海王_001_L1",
    )
    version: str = "1.0.0"
