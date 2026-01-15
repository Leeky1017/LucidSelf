"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.288084
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
    semantic_id="pit_v1.0.0_mars_in_the_twelfth_house__火星过_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MarsInTheTwelfthHouse火星过(SemanticEntry):
    """
    **Source Text** (Lines 8568-8598):
> Can be difficult if not handled properly. Frustration and self-...
    """
    
    original_text: str = """**Source Text** (Lines 8568-8598):
> Can be difficult if not handled properly. Frustration and self-denial, don't get credit. May feel vaguely irritable—repressed energies. When asserting yourself, create wrong impression, undermine position. Past unconscious behavior patterns come into play. "Secret enemies" created. Become conscious of self-defeating acts. Work alone as much as possible. Or social-service field where helping others primary. Get ego out of the way. Do research in secluded place.

**English Paraphrase**: Frustration and self-denial. Feel irritable from repressed energy. Self-assertion undermined by unconscious patterns. Work alone or in service field. Get ego out of the way.

**Complete Chinese Interpretation**: 挫败感和自我否定。因压抑能量感到烦躁。自我主张被无意识模式破坏。独自工作或在服务领域。把自我放到一边。

**Narrative Snippets**:
- `[ns_pit_ma012]` `[trigger: mars_transit_house_12]` `[factor_trigger: astro_transit_mars AND astro_house_12]` `[role: 主干]` Frustration and repressed energy. Self-assertion undermined. Work alone or in service. → PIT Ch8 Mars-12H"""
    normalized_text_zh: str = """"""
    subject: str = "Mars in the Twelfth House (火星过境第十二宫)"
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
        l1_anchor="pit_v1.0.0_mars_in_the_twelfth_house__火星过_001_L1",
    )
    version: str = "1.0.0"
