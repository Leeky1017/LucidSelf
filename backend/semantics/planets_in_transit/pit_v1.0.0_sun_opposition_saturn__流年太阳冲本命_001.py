"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224525
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
    semantic_id="pit_v1.0.0_sun_opposition_saturn__流年太阳冲本命_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunOppositionSaturn流年太阳冲本命(SemanticEntry):
    """
    **Source Text** (estimated):
> Critical test of your structures and commitments. Projects you've bui...
    """
    
    original_text: str = """**Source Text** (estimated):
> Critical test of your structures and commitments. Projects you've built are now tested. Relations with authorities reach a critical point. May feel depressed or overburdened. If you've been avoiding responsibilities, they catch up with you now. Whatever isn't working well becomes obvious. Time for reality check—what needs restructuring? Frustrations reveal where you need to work harder or differently.

**English Paraphrase**: Critical test of structures and commitments. Projects tested. Authority relations at critical point. May feel depressed or overburdened. Avoided responsibilities catch up. What isn't working becomes obvious. Reality check—what needs restructuring?

**Complete Chinese Interpretation**: 结构和承诺的关键测试。项目受到测试。与权威的关系到达关键点。可能感到沮丧或负担过重。逃避的责任追上来。不奏效的变得明显。现实检查——什么需要重组？

**Narrative Snippets**:
- `[ns_pit_105]` `[trigger: transit_sun_opposition_natal_saturn]` `[factor_trigger: astro_transit_sun OPPOSITION natal_saturn]` `[role: 主干]` Critical test of structures—projects and authority relations at critical point. Reality check. → PIT Ch4 Sun☍Saturn
- `[ns_pit_106]` `[trigger: transit_sun_opposition_natal_saturn]` `[factor_trigger: astro_transit_sun OPPOSITION natal_saturn]` `[role: 条件分支]` May feel depressed. Avoided responsibilities catch up. What needs restructuring? → PIT Ch4 Sun☍Saturn"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Opposition Saturn (流年太阳冲本命土星)"
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
        l1_anchor="pit_v1.0.0_sun_opposition_saturn__流年太阳冲本命_001_L1",
    )
    version: str = "1.0.0"
