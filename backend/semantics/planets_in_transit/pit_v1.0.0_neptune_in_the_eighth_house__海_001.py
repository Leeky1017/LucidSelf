"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.272633
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
    semantic_id="pit_v1.0.0_neptune_in_the_eighth_house__海_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class NeptuneInTheEighthHouse海(SemanticEntry):
    """
    **Source Text** (Lines 16868-16890):
> Attention turns to hidden areas and deepest subconscious. Int...
    """
    
    original_text: str = """**Source Text** (Lines 16868-16890):
> Attention turns to hidden areas and deepest subconscious. Interest in psychic and occult sciences increases. Want to learn more about yourself and make changes to work with unconscious drives more successfully. Good time to begin psychotherapy. Old order passing away, new one coming—process very subtle, may not notice until years passed. Someone close may die, changing your life considerably. May affect joint finances adversely—resources held with others. May cause misunderstanding with others concerning money/property. Danger of misrepresentation and fraud. Hidden forces at work preventing you from knowing what's happening. Not good time to borrow money—may have trouble getting bank loan anyway. Certainly don't borrow more than a little from friends—strict business relationship of bank mitigates fogginess, but casual borrowing from friends open to worst Neptunian misunderstandings.

**English Paraphrase**: Interest in subconscious, occult increases. Good for therapy. Old order passing—subtle process. Someone close may die. Joint finances may be confused. Danger of fraud, hidden forces. Not good for borrowing—especially from friends.

**Complete Chinese Interpretation**: 对潜意识、神秘学的兴趣增加。适合治疗。旧秩序消逝——微妙的过程。亲近的人可能去世。共同财务可能混乱。欺诈、隐藏力量的危险。不利于借款——尤其是向朋友借。

**Narrative Snippets**:
- `[ns_pit_ne008]` `[trigger: neptune_transit_house_8]` `[factor_trigger: astro_transit_neptune AND astro_house_8]` `[role: 主干]` Subconscious/occult interest. Good for therapy. Joint finances confused. Fraud danger. Don't borrow. → PIT Ch12 Neptune-8H"""
    normalized_text_zh: str = """"""
    subject: str = "Neptune in the Eighth House (海王星过境第八宫)"
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
        l1_anchor="pit_v1.0.0_neptune_in_the_eighth_house__海_001_L1",
    )
    version: str = "1.0.0"
