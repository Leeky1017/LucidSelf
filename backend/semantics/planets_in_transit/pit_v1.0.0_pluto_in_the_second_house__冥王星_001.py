"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.237904
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
    semantic_id="pit_v1.0.0_pluto_in_the_second_house__冥王星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class PlutoInTheSecondHouse冥王星(SemanticEntry):
    """
    **Source Text** (Lines 18795-18820):
> Values undergo complete metamorphosis—possessions on material...
    """
    
    original_text: str = """**Source Text** (Lines 18795-18820):
> Values undergo complete metamorphosis—possessions on material plane and sense of values on psychological level. May include major changes in financial picture. Most upsetting: quite frequently begins with breakdown phase—get along with much less. Business might lessen, difficulty borrowing, change income source, invest money in property repairs. Material base will change—hard to count on accustomed income. Not doomed to poverty—temporary phase. If try to hold on, only slow down process. Attitude toward property may change completely—may see physical property not so important. Metaphysical and moral values may become more important—no longer seek to acquire material possessions. Only inner values within total control.

**English Paraphrase**: Values undergo metamorphosis. Major financial changes possible—often begins with breakdown phase. Not permanent poverty. If hold on, slow the process. May see property as less important. Inner values become central.

**Complete Chinese Interpretation**: 价值观经历蜕变。可能有重大财务变化——通常以崩溃阶段开始。不是永久贫困。如果坚持，会减慢过程。可能认为财产不那么重要。内在价值成为核心。

**Narrative Snippets**:
- `[ns_pit_pl002]` `[trigger: pluto_transit_house_2]` `[factor_trigger: astro_transit_pluto AND astro_house_2]` `[role: 主干]` Values metamorphosis. Financial changes with breakdown phase. Inner values become central. → PIT Ch13 Pluto-2H"""
    normalized_text_zh: str = """"""
    subject: str = "Pluto in the Second House (冥王星过境第二宫)"
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
        l1_anchor="pit_v1.0.0_pluto_in_the_second_house__冥王星_001_L1",
    )
    version: str = "1.0.0"
