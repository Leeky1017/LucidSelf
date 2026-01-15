"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.309822
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
    semantic_id="pit_v1.0.0_jupiter_in_the_ninth_house__木星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class JupiterInTheNinthHouse木星(SemanticEntry):
    """
    **Source Text** (Lines 10402-10431):
> Very good position for Jupiter. Perspective of life expanded ...
    """
    
    original_text: str = """**Source Text** (Lines 10402-10431):
> Very good position for Jupiter. Perspective of life expanded tremendously. Opportunities for extensive travel, learning and teaching. Desire to learn great—more reading about abstract and profound subjects. Philosophy, metaphysics, religion typical studies. Good time for human-potential or consciousness-raising groups. Excellent for writing—ninth house is publishing. Views on life will change—powerful maturing influence. More involved with foreign persons or lands. Consciousness grows—can't live with old prejudices. Must know rather than just believe.

**English Paraphrase**: Excellent for Jupiter. Life perspective expands. Travel, learning, teaching opportunities. Study philosophy, metaphysics, religion. Good for writing and publishing. Views change—maturing. Foreign involvement. Replace belief with knowledge.

**Complete Chinese Interpretation**: 木星的绝佳位置。人生视角扩展。旅行、学习、教学机会。研究哲学、形而上学、宗教。适合写作和出版。观点改变——成熟。外国参与。用知识代替信仰。

**Narrative Snippets**:
- `[ns_pit_ju009]` `[trigger: jupiter_transit_house_9]` `[factor_trigger: astro_transit_jupiter AND astro_house_9]` `[role: 主干]` Excellent for expansion. Travel, learning, teaching. Philosophy and spirituality. Views mature. → PIT Ch9 Jupiter-9H"""
    normalized_text_zh: str = """"""
    subject: str = "Jupiter in the Ninth House (木星过境第九宫)"
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
        l1_anchor="pit_v1.0.0_jupiter_in_the_ninth_house__木星_001_L1",
    )
    version: str = "1.0.0"
