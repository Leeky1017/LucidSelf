"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.223694
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
    semantic_id="pit_v1.0.0_sun_in_the_second_house__太阳过境第_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunInTheSecondHouse太阳过境第(SemanticEntry):
    """
    **Source Text** (Lines 1695-1718):
> At this time you should reflect upon your values and the things...
    """
    
    original_text: str = """**Source Text** (Lines 1695-1718):
> At this time you should reflect upon your values and the things that you value. Traditionally the second house is the house of money and of moveable property, as opposed to real estate. In modern times we refer to it as the house of resources in general and of what we value, both abstract values and material objects. During this month-long transit you should examine your relationship to the resources of your life.
> 
> Do they serve your needs, or do you serve theirs? Many people, out of a misguided need for security, become so involved with their possessions that they cannot act freely for fear of damaging their own interests, that is, property interests. At this time you need to express yourself through your material and nonmaterial resources, using them to define you to yourself and others.
> 
> More than any other time, you now want to have greater control of your life through the things that you value. On the material level this may mean that you will acquire possessions in order to gain more control over your own life or over other people. On the psychological level it indicates a need to assert your value system. But remember that others have a right to their own values. You should stand up for your own, but not by obliterating someone else's.

**Key Term Analysis**:
- **Values**: literal = what you consider important / symbolic = core worth system / context = both material and abstract
- **Resources**: literal = money, possessions / symbolic = all life assets / context = what you draw upon
- **Second house**: literal = house after Ascendant / symbolic = possessions, self-worth, values / context = what you own vs what owns you
- **Express yourself through resources**: literal = use possessions for self-definition / symbolic = values as identity expression / context = resources as self-extension
- **Value system**: literal = hierarchy of what matters / symbolic = psychological foundation / context = basis of choices

**English Paraphrase (Primary Language)**:
The Sun's transit through your second house (approximately one month annually) brings focus to your values—both material possessions and abstract principles. Hand expands the traditional second house meaning from money and moveable property to encompass all resources and everything you value. This is a period for examining your relationship with these resources: do they serve you, or have you become their servant? Many people, driven by misguided security needs, become so attached to possessions that they lose freedom of action. During this transit, you should express yourself through your resources, using them to define your identity to yourself and others. You desire greater life control through what you value—materially this may manifest as acquisitiveness for control, psychologically as asserting your value system. Hand's warning: while you should stand up for your values, you must not obliterate others' right to their own values.

**Complete Chinese Interpretation (Secondary Language)**:
太阳过境第二宫（每年约一个月）将焦点带到你的价值观——包括物质财产和抽象原则。汉德将传统第二宫含义从金钱和动产扩展到包含所有资源和你珍视的一切。这是审视你与这些资源关系的时期：它们在服务你，还是你成了它们的奴仆？许多人出于错误的安全需求，对财产过度依附以至于失去行动自由。在此行运期间，你应通过资源表达自己，用它们向自己和他人定义你的身份。你渴望通过你所珍视的事物获得更大的人生控制——物质层面可能表现为为了控制而获取财产，心理层面则表现为主张你的价值体系。汉德的警告：虽然你应该坚持自己的价值观，但不能抹杀他人拥有自己价值观的权利。

**Core Points**:
- Second house = values (material and abstract) + resources + possessions
- Traditional meaning: money and moveable property (not real estate)
- Modern meaning: all resources and what we value
- Examine: do resources serve you, or do you serve them?
- Misguided security need can create possession-bondage
- Express yourself through material and nonmaterial resources
- Resources define identity to self and others
- Desire for greater control through valued things
- Material level: acquisition for control
- Psychological level: value system assertion
- Warning: respect others' right to their own values

**Detailed Explanation**:
Hand's interpretation of the second house transit reflects modern psychological astrology's evolution beyond simple material meanings. The question "do they serve your needs, or do you serve theirs?" captures the second house's shadow potential—becoming possessed by possessions. The psychological layer (value system assertion) is as important as the material layer (acquisition). The warning about respecting others' values reflects the second house's opposition to the eighth house (others' resources/values), suggesting that over-assertion of personal values can create conflict in shared resource situations.

**Narrative Snippets**:
- `[ns_pit_007]` `[trigger: sun_transit_house_2]` `[factor_trigger: astro_transit_sun AND astro_house_2]` `[role: 主干]` At this time you should reflect upon your values and the things that you value—both abstract values and material objects. → PIT Ch4 Sun-2H
- `[ns_pit_008]` `[trigger: sun_transit_house_2]` `[factor_trigger: astro_transit_sun AND astro_house_2]` `[role: 主干依赖]` Do your resources serve your needs, or do you serve theirs? Many become so involved with possessions that they cannot act freely. → PIT Ch4 Sun-2H
- `[ns_pit_009]` `[trigger: sun_transit_house_2]` `[factor_trigger: astro_transit_sun AND astro_house_2]` `[role: 主干依赖]` You need to express yourself through your material and nonmaterial resources, using them to define you to yourself and others. → PIT Ch4 Sun-2H
- `[ns_pit_010]` `[trigger: sun_transit_house_2]` `[factor_trigger: astro_transit_sun AND astro_house_2]` `[role: 条件分支]` On the material level you may acquire possessions for control; on the psychological level you need to assert your value system. → PIT Ch4 Sun-2H
- `[ns_pit_011]` `[trigger: sun_transit_house_2]` `[factor_trigger: astro_transit_sun AND astro_house_2]` `[role: 总结]` Stand up for your own values, but not by obliterating someone else's—others have a right to their own values. → PIT Ch4 Sun-2H
- `[ns_pit_h2]` `[trigger: house_2]` `[factor_trigger: house_2]` `[role: 主干]` Second house represents values, resources, money, possessions, self-worth and what we consider valuable. → PIT Foundation
- `[ns_pit_h8]` `[trigger: house_8]` `[factor_trigger: house_8]` `[role: 条件分支]` Eighth house represents shared resources, transformation, death/rebirth, others' values—opposite the second house. → PIT Foundation
- `[ns_pit_s2h]` `[trigger: sun_2h]` `[factor_trigger: sun_2h]` `[role: 效果]` Sun in 2nd house transit illuminates values, resources and self-worth for conscious examination. → PIT Ch4
- `[ns_pit_s4h]` `[trigger: sun_4h]` `[factor_trigger: sun_4h]` `[role: 效果]` Sun in 4th house transit illuminates home, family roots and inner psychological foundations. → PIT Ch4
- `[ns_pit_sdec]` `[trigger: spending_decision]` `[factor_trigger: spending_decision]` `[role: 效果]` Spending decisions are highlighted during 2nd house and Venus transits affecting resource management. → PIT Foundation
- `[ns_pit_pvl]` `[trigger: private_life]` `[factor_trigger: private_life]` `[role: 条件分支]` Private life and inner world are emphasized during 4th and 12th house transits. → PIT Foundation
- `[ns_pit_pbd]` `[trigger: public_display]` `[factor_trigger: public_display]` `[role: 效果]` Public display and visibility increase during 10th house and Sun transits to angles. → PIT Foundation
- `[ns_pit_imp]` `[trigger: impression]` `[factor_trigger: impression]` `[role: 效果]` Making impressions on others is enhanced during 1st house and Sun transits. → PIT Foundation

**Textual Criticism & Variant Analysis**:
- **English**: N/A - Single authoritative source (1976 Para Research edition).
- **中文**: 无变体 - 单一权威来源。"""
    normalized_text_zh: str = """"""
    subject: str = "Sun in the Second House (太阳过境第二宫)"
    factor_refs: list = ['house_2', 'concept_resources', 'psych_value_system', 'state_possession_bondage']
    
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
        l1_anchor="pit_v1.0.0_sun_in_the_second_house__太阳过境第_001_L1",
    )
    version: str = "1.0.0"
