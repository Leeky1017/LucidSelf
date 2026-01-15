"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.094036
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
    semantic_id="tis_v1.0.0_sixth_house___service___compet_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class SixthHouseServiceCompet(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Need to be Useful | Func...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Need to be Useful | Functional utility | Core need |
| Competence | Skill development | Mastery |
| Apprenticeship | Humble learning | Process |
| Drudgery Trap | Meaningless work | Danger |

#### Source Text

"Now, we ourselves are the servant. But not in any degrading sense. In this house we recognize an elemental human need: the desire to exercise competence and to be recognized for it. If we fail to discover that special skill, or fail to develop it to its limits, there's an emptiness in our lives. Something basic is missing."

#### English Paraphrase

The **Sixth House** is the arena of **work, service, and self-improvement**. It governs the development of **competence**.

**The Need to be Useful**:
We have a deep need to be **good at something**. To have a skill that is valuable to others. This is not about ego-glory (Leo) but about **functional utility**.

**Service**:
- Helping others effectively.
- Fixing what is broken.
- Maintaining systems (health, daily routines).
- The joy of a job well done.

**Skill Cultivation**:
This house demands **apprenticeship**. We must humble ourselves to learn techniques, practice, and refine our craft.

**Health**:
The body is the primary tool for service. The Sixth House governs health maintenance, diet, and integration of mind and body.

**The Trap of Drudgery**:
If we don't find meaningful work, we fall into **drudgery**—working just for survival, feeling like a slave. We become resentful servants rather than proud craftspeople.

**Mastery**:
The goal is to perform tasks with such skill and care that the work itself becomes a form of meditation and dignity.

#### Complete Chinese Interpretation

**第六宫**是**工作、服务和自我完善**的领域。它掌管**能力**的发展。

**有用的需求**：
我们有深层的需求想要**擅长某事**。拥有一种对他有价值的技能。这不是关于小我荣耀（狮子座），而是关于**功能性效用**。

**服务**：
- 有效地帮助他人。
- 修复损坏的东西。
- 维护系统（健康、日常惯例）。
- 工作做好的喜悦。

**技能培养**：
这一宫要求**学徒精神**。我们必须谦卑自己去学习技术、练习并精炼我们的工艺。

**健康**：
身体是服务的主要工具。第六宫掌管健康维护、饮食以及身心的整合。

**苦工的陷阱**：
如果我们找不到有意义的工作，我们就会陷入**苦工**——仅为了生存而工作，感觉像奴隶。我们变成怨恨的仆人，而不是自豪的工匠。

**掌握**：
目标是以如此的技巧和关怀执行任务，以至于工作本身成为一种冥想和尊严的形式。

#### Core Points

- Arena of competence, skill, and service.
- Need to be useful and effective.
- Health and daily routines (maintenance).
- Meaningful work vs. drudgery.
- East parallel: 奴仆宫/官禄/技艺 (Servant Palace, Career, Skills).

#### Detailed Explanation

The Sixth House governs **competence, skill, and service**. Unlike the Tenth House's public career, the Sixth is about the **daily work** itself—the craft, the routines, the discipline of showing up and doing things well. Forrest emphasizes an elemental human need: to be useful, to exercise competence, and to be recognized for it.

The Sixth House is where we become **servants**—but not in a degrading sense. We serve by offering our skills to others, creating value through what we can do. When we help someone through our competence, we experience a **characteristic satisfaction** that nothing else provides.

**Successful navigation** means finding meaningful work that uses our gifts and allows for continuous skill development. The work itself becomes a form of meditation and dignity. **Unsuccessful navigation** produces either drudgery (work without meaning) or incompetence (undeveloped skills). Health issues often arise when Sixth House energy is blocked—the body protests when the need to serve is unfulfilled.

#### Narrative Snippets

- `[ns_innersky_h6_001]` `[trigger: house_6_general]` `[factor_trigger: astro_house_6]` `[role: 主干]` Now, we ourselves are the servant. But not in any degrading sense. In this house we recognize an elemental human need: the desire to exercise competence and to be recognized for it. → The Inner Sky Ch.7 #6H
- `[ns_innersky_h6_002]` `[trigger: house_6_competence]` `[factor_trigger: astro_house_6]` `[role: 主干依赖]` If we fail to discover that special skill within ourselves, or if we fail to develop it to its limits, there is an emptiness in our lives. Something basic is missing. → The Inner Sky Ch.7 #6H
- `[ns_innersky_h6_003]` `[trigger: house_6_service]` `[factor_trigger: astro_house_6 AND astro_state_success]` `[role: 条件分支]` We have demonstrated a personal skill in such a way that it helped another person. And whenever we do that, we feel a characteristic satisfaction. → The Inner Sky Ch.7 #6H
- `[ns_innersky_h6_004]` `[trigger: house_6_drudgery]` `[factor_trigger: astro_house_6 AND astro_state_dysfunction]` `[role: 条件分支]` If we fail to find meaningful work, we fall into drudgery—working just for survival, feeling like a slave. We become the wage slave or the drudge, praying for the weekend. → The Inner Sky Ch.7 #6H
- `[ns_innersky_h6_005]` `[trigger: house_6_bosses]` `[factor_trigger: astro_house_6 AND astro_state_dysfunction]` `[role: 总结]` Soon we find ourselves living in a world populated with bosses. We lack inner direction in our labors. Outer direction quickly takes up the slack. → The Inner Sky Ch.7 #6H"""
    normalized_text_zh: str = """"""
    subject: str = "Sixth House - Service & Competence"
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
        book_id="the_inner_sky",
        chapter="",
        l1_anchor="tis_v1.0.0_sixth_house___service___compet_001_L1",
    )
    version: str = "1.0.0"
