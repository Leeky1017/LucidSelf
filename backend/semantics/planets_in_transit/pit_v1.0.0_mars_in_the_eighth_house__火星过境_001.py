"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.288037
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
    semantic_id="pit_v1.0.0_mars_in_the_eighth_house__火星过境_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MarsInTheEighthHouse火星过境(SemanticEntry):
    """
    **Source Text** (Lines 8462-8489):
> Effects subtle or blatant. Ego drives create confrontation forc...
    """
    
    original_text: str = """**Source Text** (Lines 8462-8489):
> Effects subtle or blatant. Ego drives create confrontation forcing transformation. May encounter someone who has powerful effect on you. Conflict concerning values or shared property. Disagreement on managing joint resources. Not good time for loans—ego conflicts foul negotiations. Stimulates sex as ego expression. Seek intense, transforming quality in sexual relationships. Death of old order, birth of new.

**English Paraphrase**: Confrontation forcing transformation. Powerful encounters. Conflict over shared resources. Not good for loans. Sex as ego expression—seek intensity. Death/rebirth process.

**Complete Chinese Interpretation**: 对抗迫使转变。强大的遭遇。共享资源上的冲突。不适合贷款。性作为自我表达——寻求强度。死亡/重生过程。

**Narrative Snippets**:
- `[ns_pit_ma008]` `[trigger: mars_transit_house_8]` `[factor_trigger: astro_transit_mars AND astro_house_8]` `[role: 主干]` Confrontation forcing transformation. Conflict over shared resources. Intense sexuality. → PIT Ch8 Mars-8H"""
    normalized_text_zh: str = """"""
    subject: str = "Mars in the Eighth House (火星过境第八宫)"
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
        l1_anchor="pit_v1.0.0_mars_in_the_eighth_house__火星过境_001_L1",
    )
    version: str = "1.0.0"
