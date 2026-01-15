"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.223809
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
    semantic_id="pit_v1.0.0_sun_in_the_sixth_house__太阳过境第六_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunInTheSixthHouse太阳过境第六(SemanticEntry):
    """
    **Source Text** (Lines 1794-1821):
> This transit is quite different from the immediately preceding ...
    """
    
    original_text: str = """**Source Text** (Lines 1794-1821):
> This transit is quite different from the immediately preceding one. Now is the time to examine the problem of how you should manage your life and what duties and responsibilities that entails. This is a house of work, of tasks that need to be done, which may necessitate postponing immediate gratification. Your focus should be on efficiency and effectiveness. Strive to make every action as much to the point as possible. In your work this is a good time to examine and refine your techniques and procedures, for your mind can work clearly and sharply to discover the best way of doing things.
> 
> The only problem you may have to contend with at this time is that you will probably not be on top of the heap. That is, you will probably have to work according to someone else's wishes or needs. But because of this, you can find out whether you can lower your ego drives when the situation requires it. If you cannot, you are likely to encounter quite a bit of discomfort and conflict at this time. This is the house of service, and you cannot spend all your efforts getting your own way now.
> 
> Nevertheless, this doesn't have to be a time of repression and self-denial, without satisfaction. You can derive quite a bit of satisfaction from doing things well, and that will mean more to you now than any other kind of satisfaction.
> 
> This transit also concerns physical efficiency. This is a house of health, but that does not mean that your physical health will necessarily be worse than usual. However, you will be more inclined to look at your body and to see how its functioning can be improved. You may be unusually concerned with health and hygiene.

**Key Term Analysis**:
- **Sixth house**: literal = Virgo's house / symbolic = work, service, health, routine / context = duty focus
- **Duties and responsibilities**: literal = obligations / symbolic = service requirements / context = what must be done
- **Efficiency and effectiveness**: literal = optimal function / symbolic = Virgoan perfection drive / context = refinement
- **Not on top of heap**: literal = subordinate position / symbolic = ego subordination / context = service role
- **House of service**: literal = serving others / symbolic = ego transcendence through work / context = 6H core meaning
- **Physical efficiency/health**: literal = body function / symbolic = vessel maintenance / context = 6H health rulership

**English Paraphrase (Primary Language)**:
The Sun's sixth house transit contrasts sharply with the preceding fifth house joy. Now you examine life management—duties and responsibilities requiring postponed gratification. Focus on efficiency and effectiveness, making every action purposeful. This is excellent timing to examine and refine work techniques and procedures—your mind works clearly for discovering optimal methods. The challenge: you probably won't be "on top of the heap"—you'll work according to others' wishes or needs. This tests whether you can lower ego drives when required. If you cannot, expect discomfort and conflict. This is the house of service—you cannot spend all efforts getting your own way. Yet this needn't be repressive self-denial; satisfaction comes from doing things well, which matters more now than other satisfactions. Physical efficiency is also highlighted—not necessarily health problems, but increased inclination to examine body functioning and improvement. Unusual concern with health and hygiene may arise.

**Complete Chinese Interpretation (Secondary Language)**:
太阳过境第六宫与前面第五宫的欢乐形成鲜明对比。现在你审视生活管理——需要推迟即时满足的责任和义务。专注于效率和有效性，使每个行动都有目的。这是审视和完善工作技巧和程序的绝佳时机——你的头脑清晰地发现最佳方法。挑战是：你可能不会处于"顶端"——你将按照他人的意愿或需求工作。这考验你是否能在需要时降低自我驱动。如果不能，预期会有不适和冲突。这是服务之宫——你不能把所有精力都用于随心所欲。然而这不必是压抑的自我否定；满足感来自把事情做好，这比其他满足现在更重要。身体效率也被突显——不一定是健康问题，而是增加检视身体功能和改善的倾向。可能出现对健康和卫生的异常关注。

**Core Points**:
- Sixth house transit contrasts sharply with fifth house joy
- Focus on life management, duties, responsibilities
- May require postponing immediate gratification
- Emphasize efficiency and effectiveness in all actions
- Good time to refine work techniques and procedures
- Mind works clearly for finding optimal methods
- Probably not "on top"—work according to others' needs
- Test of lowering ego drives when required
- Inability to do so creates discomfort and conflict
- House of service—cannot focus only on own way
- Satisfaction from doing things well, not other pleasures
- Physical efficiency and health focus increased
- Not necessarily health problems—body improvement focus
- Unusual concern with health and hygiene possible

**Narrative Snippets**:
- `[ns_pit_026]` `[trigger: sun_transit_house_6]` `[factor_trigger: astro_transit_sun AND astro_house_6]` `[role: 主干]` Now is the time to examine how you should manage your life—duties and responsibilities that may require postponing gratification. → PIT Ch4 Sun-6H
- `[ns_pit_027]` `[trigger: sun_transit_house_6]` `[factor_trigger: astro_transit_sun AND astro_house_6]` `[role: 主干依赖]` Focus on efficiency and effectiveness—strive to make every action as much to the point as possible. → PIT Ch4 Sun-6H
- `[ns_pit_028]` `[trigger: sun_transit_house_6]` `[factor_trigger: astro_transit_sun AND astro_house_6]` `[role: 条件分支]` You will probably have to work according to someone else's wishes—can you lower your ego drives when required? → PIT Ch4 Sun-6H
- `[ns_pit_029]` `[trigger: sun_transit_house_6]` `[factor_trigger: astro_transit_sun AND astro_house_6]` `[role: 主干依赖]` You can derive satisfaction from doing things well—that will mean more now than any other kind of satisfaction. → PIT Ch4 Sun-6H
- `[ns_pit_030]` `[trigger: sun_transit_house_6 AND astro_health]` `[factor_trigger: astro_transit_sun AND astro_house_6 AND astro_health]` `[role: 条件分支]` This house of health: not necessarily problems, but inclination to examine body functioning and improvement. → PIT Ch4 Sun-6H
- `[ns_pit_h6]` `[trigger: house_6]` `[factor_trigger: house_6]` `[role: 主干]` Sixth house represents work, service, health, daily routines, efficiency and subordination of ego to duty. → PIT Foundation

**Textual Criticism**: N/A - Single authoritative source."""
    normalized_text_zh: str = """"""
    subject: str = "Sun in the Sixth House (太阳过境第六宫)"
    factor_refs: list = ['house_6', 'state_efficiency', 'psych_ego_subordination', 'psych_service_satisfaction']
    
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
        l1_anchor="pit_v1.0.0_sun_in_the_sixth_house__太阳过境第六_001_L1",
    )
    version: str = "1.0.0"
