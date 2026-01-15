"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.309906
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
    semantic_id="pit_v1.0.0_jupiter_in_the_twelfth_house___001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class JupiterInTheTwelfthHouse(SemanticEntry):
    """
    **Source Text** (Lines 10479-10504):
> One 12H transit that is quite beneficial, though benefits not...
    """
    
    original_text: str = """**Source Text** (Lines 10479-10504):
> One 12H transit that is quite beneficial, though benefits not as obvious. Capacity to learn about spiritual and religious dimensions. Learn about yourself without encountering usual fear or resistance. Demands of ego less exacting. Look dispassionately and compassionately at self, world, others. Direct empathy for suffering—genuinely want to help. Understand we're all in the same boat. May find spiritual teacher—can come in any guise. May play this role for someone else. Concerned about spiritual truth and wisdom. May incline to study metaphysics or occult. Greater involvement with orthodox religion possible.

**English Paraphrase**: Beneficial 12H transit. Learn spiritual dimensions. Self-understanding without fear. Ego demands less. Compassionate view. Empathy for suffering. May find or be spiritual teacher. Study metaphysics/occult or religion.

**Complete Chinese Interpretation**: 有益的第十二宫行运。学习精神维度。不带恐惧的自我理解。自我要求减少。慈悲的视角。对苦难的共情。可能找到或成为精神导师。研究形而上学/神秘学或宗教。

**Narrative Snippets**:
- `[ns_pit_ju012]` `[trigger: jupiter_transit_house_12]` `[factor_trigger: astro_transit_jupiter AND astro_house_12 AND astro_spiritual_growth]` `[role: 主干]` Beneficial for spiritual growth. Self-understanding. Compassion. May find/be teacher. → PIT Ch9 Jupiter-12H"""
    normalized_text_zh: str = """"""
    subject: str = "Jupiter in the Twelfth House (木星过境第十二宫)"
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
        l1_anchor="pit_v1.0.0_jupiter_in_the_twelfth_house___001_L1",
    )
    version: str = "1.0.0"
