"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.223898
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
    semantic_id="pit_v1.0.0_sun_in_the_tenth_house__太阳过境第十_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunInTheTenthHouse太阳过境第十(SemanticEntry):
    """
    **Source Text** (Lines 1906-1936):
> This is a time when you should turn your attention to the most ...
    """
    
    original_text: str = """**Source Text** (Lines 1906-1936):
> This is a time when you should turn your attention to the most outward aspects of your life — your career, your role in the larger society and your standing and reputation within the community.
> 
> One possible effect of the Sun in this house is to put you in the limelight. You may be called upon to take over the direction of a task or project in which you would have considerable power, but the responsibility will be equally great.
> 
> The only real danger: if you have done something wrong or in a slipshod fashion it may be exposed now and trip you up in unpleasant ways.

**English Paraphrase**: Turn attention to outward aspects—career, societal role, standing, reputation. May be put in limelight with leadership opportunity; power comes with equal responsibility. Danger: past wrongs or slipshod work may be exposed.

**Complete Chinese Interpretation**: 将注意力转向外向方面——事业、社会角色、地位、声誉。可能被置于聚光灯下，有领导机会；权力伴随同等责任。危险：过去的错误或马虎工作可能被揭露。

**Narrative Snippets**:
- `[ns_pit_038]` `[trigger: sun_transit_house_10]` `[factor_trigger: astro_transit_sun AND astro_house_10]` `[role: 主干]` Turn attention to outward aspects—career, role in society, standing and reputation in community. → PIT Ch4 Sun-10H
- `[ns_pit_039]` `[trigger: sun_transit_house_10]` `[factor_trigger: astro_transit_sun AND astro_house_10]` `[role: 条件分支]` May be put in limelight with considerable power—but responsibility will be equally great. → PIT Ch4 Sun-10H"""
    normalized_text_zh: str = """"""
    subject: str = "Sun in the Tenth House (太阳过境第十宫)"
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
        l1_anchor="pit_v1.0.0_sun_in_the_tenth_house__太阳过境第十_001_L1",
    )
    version: str = "1.0.0"
