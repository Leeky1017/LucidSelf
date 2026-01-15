"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.223981
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
    semantic_id="pit_v1.0.0_sun_sextile_sun__流年太阳六合本命太阳_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunSextileSun流年太阳六合本命太阳(SemanticEntry):
    """
    **Source Text** (Lines 2016-2040):
> This transit occurs twice a year, roughly two months before and...
    """
    
    original_text: str = """**Source Text** (Lines 2016-2040):
> This transit occurs twice a year, roughly two months before and two months after your birthday. It is a time when you should strive to integrate your energies with those of the people around you. You will be able to work very effectively with others now, and your goals will harmonize with those of the people you associate with.
> 
> This is a good time for socializing with others. On the transit two months after your birthday, examine how far you have gotten in realizing the goals you set for this year. On the transit two months prior, check how well this current cycle has served you.

**English Paraphrase**: Occurs twice yearly, ~2 months before/after birthday. Time to integrate your energies with others; work effectively with people, goals harmonize. Good for socializing. Post-birthday: check goal progress. Pre-birthday: evaluate current cycle's service to you.

**Complete Chinese Interpretation**: 每年发生两次，生日前后约两个月。与他人整合能量的时期；与人有效合作，目标和谐。适合社交。生日后：检查目标进展。生日前：评估当前周期对你的服务。

**Narrative Snippets**:
- `[ns_pit_047]` `[trigger: transit_sun_sextile_natal_sun]` `[factor_trigger: astro_transit_sun SEXTILE natal_sun]` `[role: 主干]` Strive to integrate your energies with those around you—work effectively with others, goals harmonize. → PIT Ch4 Sun⚹Sun
- `[ns_pit_048]` `[trigger: transit_sun_sextile_natal_sun]` `[factor_trigger: astro_transit_sun SEXTILE natal_sun]` `[role: 条件分支]` Two months after birthday: examine goal progress. Two months before: check how well this cycle has served you. → PIT Ch4 Sun⚹Sun"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Sextile Sun (流年太阳六合本命太阳)"
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
        l1_anchor="pit_v1.0.0_sun_sextile_sun__流年太阳六合本命太阳_001_L1",
    )
    version: str = "1.0.0"
