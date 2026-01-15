"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.288004
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
    semantic_id="pit_v1.0.0_mars_in_the_sixth_house__火星过境第_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MarsInTheSixthHouse火星过境第(SemanticEntry):
    """
    **Source Text** (Lines 8405-8430):
> Throw ego energies into working hard. More able to defer pleasu...
    """
    
    original_text: str = """**Source Text** (Lines 8405-8430):
> Throw ego energies into working hard. More able to defer pleasure for today's work. Take pride in how much work you can do. Problems: sixth house is service—subordinating ego. May not want to work for someone else. Conflicts with superiors or employees. Best to work alone with individual initiative. Health: infections, fevers, accidents from frustrated energies. Keep physical activity, don't bottle frustrations.

**English Paraphrase**: Work hard, defer pleasure. Take pride in productivity. Problems: service vs ego. Conflicts at work. Better to work alone. Health issues from frustration—stay active.

**Complete Chinese Interpretation**: 努力工作，推迟享乐。为生产力自豪。问题：服务vs自我。工作中的冲突。最好独自工作。挫败感导致的健康问题——保持活跃。

**Narrative Snippets**:
- `[ns_pit_ma006]` `[trigger: mars_transit_house_6]` `[factor_trigger: astro_transit_mars AND astro_house_6]` `[role: 主干]` Work hard, pride in productivity. Service vs ego tension. Health issues from frustration. → PIT Ch8 Mars-6H"""
    normalized_text_zh: str = """"""
    subject: str = "Mars in the Sixth House (火星过境第六宫)"
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
        l1_anchor="pit_v1.0.0_mars_in_the_sixth_house__火星过境第_001_L1",
    )
    version: str = "1.0.0"
