"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224133
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
    semantic_id="pit_v1.0.0_sun_opposition_sun__流年太阳冲本命太阳_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunOppositionSun流年太阳冲本命太阳(SemanticEntry):
    """
    **Source Text** (Lines 2100-2131):
> This transit occurs six months after your birthday and signifie...
    """
    
    original_text: str = """**Source Text** (Lines 2100-2131):
> This transit occurs six months after your birthday and signifies a time when energies in your life are reaching a culmination. Now is the time to try to bring your affairs to a climax, but do not expect to escape opposition from other people.
> 
> Sometimes this can be a time of failure, when you realize certain efforts have not worked out. But failures now should not be the occasion for feeling defeated—a "life experiment" has not worked out. On the other hand, this can also be a day of high energy and achievement if you have been unified in purpose.

**English Paraphrase**: Occurs 6 months after birthday. Energies reaching culmination; bring affairs to climax but expect opposition. May be time of failure—"life experiment" not working—don't feel defeated. Or high energy and achievement if unified in purpose.

**Complete Chinese Interpretation**: 发生在生日后六个月。能量达到顶点；将事务推向高潮但预期有反对。可能是失败的时期——"生活实验"未成功——不要感到被打败。或者如果目标统一则是高能量和成就。

**Narrative Snippets**:
- `[ns_pit_053]` `[trigger: transit_sun_opposition_natal_sun]` `[factor_trigger: astro_transit_sun OPPOSITION natal_sun]` `[role: 主干]` Energies reaching culmination—bring affairs to climax but expect opposition from others. → PIT Ch4 Sun☍Sun
- `[ns_pit_054]` `[trigger: transit_sun_opposition_natal_sun]` `[factor_trigger: astro_transit_sun OPPOSITION natal_sun]` `[role: 条件分支]` May be time of failure—don't feel defeated, a "life experiment" hasn't worked out. Or high achievement if unified in purpose. → PIT Ch4 Sun☍Sun"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Opposition Sun (流年太阳冲本命太阳)"
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
        l1_anchor="pit_v1.0.0_sun_opposition_sun__流年太阳冲本命太阳_001_L1",
    )
    version: str = "1.0.0"
