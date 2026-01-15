"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.272670
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
    semantic_id="pit_v1.0.0_neptune_in_the_eleventh_house__001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class NeptuneInTheEleventhHouse(SemanticEntry):
    """
    **Source Text** (Lines 16959-16978):
> Ideals become more important, work hard to actualize them. At...
    """
    
    original_text: str = """**Source Text** (Lines 16959-16978):
> Ideals become more important, work hard to actualize them. Attracted in friendship to those who share your feelings. Be sure dealing with reality even as you attempt to actualize dreams. Be careful particularly with people you choose as friends—may be relating to what you'd like them to be rather than them as real people. Lays you open to disillusionment and deception. Don't become martyr to friends by letting them take undue advantage. Make sure people you help are worth helping—both you and they should get something. New friends may enter who share your ideals—can give each other moral support. Make sure you aren't fostering illusions that keep each from achieving real growth. If interested in psychic and spiritual matters, will be attracted to movements working for these causes—useful but make sure not joining mutual self-delusion society.

**English Paraphrase**: Ideals important. Attracted to friends sharing feelings. Be careful—may relate to idealized version of friends. Open to disillusionment. Don't be martyr to friends. New friends may share ideals. Avoid mutual self-delusion in spiritual groups.

**Complete Chinese Interpretation**: 理想重要。被分享感受的朋友吸引。小心——可能与朋友的理想化版本交往。容易幻灭。不要为朋友做烈士。新朋友可能分享理想。避免精神团体中的相互自欺。

**Narrative Snippets**:
- `[ns_pit_ne011]` `[trigger: neptune_transit_house_11]` `[factor_trigger: astro_transit_neptune AND astro_house_11]` `[role: 主干]` Ideals important. May idealize friends. Don't be martyr. Avoid mutual self-delusion in groups. → PIT Ch12 Neptune-11H"""
    normalized_text_zh: str = """"""
    subject: str = "Neptune in the Eleventh House (海王星过境第十一宫)"
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
        l1_anchor="pit_v1.0.0_neptune_in_the_eleventh_house__001_L1",
    )
    version: str = "1.0.0"
