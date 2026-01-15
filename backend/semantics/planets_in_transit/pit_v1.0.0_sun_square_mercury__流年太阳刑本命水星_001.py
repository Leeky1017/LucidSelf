"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224227
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
    semantic_id="pit_v1.0.0_sun_square_mercury__流年太阳刑本命水星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunSquareMercury流年太阳刑本命水星(SemanticEntry):
    """
    **Source Text** (Lines 2340-2366):
> Mentally active day. Ideas and communications come quickly—unde...
    """
    
    original_text: str = """**Source Text** (Lines 2340-2366):
> Mentally active day. Ideas and communications come quickly—understand not only surface but underlying meaning. Be aware of hints about motivations. This transit produces interactions that test your thinking clarity and force you to prove validity.
> 
> Potential for conflict with people not actually opposed but whose position unknowingly conflicts with yours. Listen to others, find weak points in your own thinking. Avoid being overwhelmed by your own thought's power. Be self-critical before others get the chance.

**English Paraphrase**: Mentally active; rapid ideas and communications. Understand surface and underlying meaning. Interactions test thinking clarity. Potential conflict with people whose positions unknowingly conflict. Listen, find your thinking's weak points. Be self-critical before others critique.

**Complete Chinese Interpretation**: 心智活跃；快速的想法和沟通。理解表面和潜在含义。互动测试思维清晰度。可能与立场不知不觉冲突的人发生冲突。倾听，找到你思维的弱点。在他人批评前自我批评。

**Narrative Snippets**:
- `[ns_pit_068]` `[trigger: transit_sun_square_natal_mercury]` `[factor_trigger: astro_transit_sun SQUARE natal_mercury]` `[role: 主干]` Mentally active—interactions test your thinking clarity and force you to prove validity. → PIT Ch4 Sun□Mercury
- `[ns_pit_069]` `[trigger: transit_sun_square_natal_mercury]` `[factor_trigger: astro_transit_sun SQUARE natal_mercury]` `[role: 条件分支]` Listen to others, find weak points in your thinking. Be self-critical before others get the chance. → PIT Ch4 Sun□Mercury"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Square Mercury (流年太阳刑本命水星)"
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
        l1_anchor="pit_v1.0.0_sun_square_mercury__流年太阳刑本命水星_001_L1",
    )
    version: str = "1.0.0"
