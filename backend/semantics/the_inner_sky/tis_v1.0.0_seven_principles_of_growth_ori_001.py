"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.134291
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
    semantic_id="tis_v1.0.0_seven_principles_of_growth_ori_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class SevenPrinciplesOfGrowthOri(SemanticEntry):
    """
    **Source Text**:
The Seven Principles
Seven fundamental ideas form the backbone of any growth-orient...
    """
    
    original_text: str = """**Source Text**:
The Seven Principles
Seven fundamental ideas form the backbone of any growth-oriented vision of astrology. Any individual or text that diverges very far from them is probably more a part of astrology’s bad karma than part of its future.
• Astrological symbols are neutral. There are no good ones, no bad ones.
• Individuals are responsible for the way they embody their birthcharts.
• No astrologer can determine a person’s level of response to his birthchart from that birthchart alone.
• The birthchart is a blueprint for the happiest, most fulfilling, most spiritually creative path of growth available to the individual.
• All deviations from the ideal growth pattern symbolized by the birthchart are unstable states, usually accompanied by a sense of aimlessness, emptiness, and anxiety.
• Astrology recognizes only two absolutes: the irreducible mystery of life, and the uniqueness of each individual viewpoint on that mystery.
• Astrology suffers when wedded too closely to any philosophy or religion. Nothing in the system matters except the intensification of a person’s self-awareness.

**Key Term Analysis**:
- `neutral symbols`: placements and configurations that have no inherent moral value, only descriptive potential.
- `level of response`: how creatively or mechanically a person embodies their chart patterns in lived behavior.
- `growth blueprint`: the ideal, most fulfilling path implied by the chart, used as a reference for alignment.
- `unstable deviation states`: anxious, empty, or aimless conditions that signal misalignment with the growth blueprint.
- `self-awareness as absolute`: the principle that the only non‑negotiable outcome of astrology should be deeper awareness, not dogmatic belief.

**English Paraphrase (Primary Language)**:
Forrest collects his philosophy into seven concise principles that define what it means to practice growth‑oriented astrology. First, symbols are neutral: no placement is inherently good or bad. Second, people—not planets—are responsible for how they live out their charts. Third, no chart by itself can reveal the level at which someone is responding; behavior and consciousness cannot be read off the wheel like a printed report.

Fourth, the chart serves as a blueprint for the most fulfilling and spiritually alive path available to a person, not for all the ways things can go wrong. Fifth, when we deviate from that pattern, we typically end up in unstable, anxious states—signs that we have stepped away from alignment rather than proof that the chart is "bad." Sixth, only two absolutes are recognized: the irreducible mystery of life and the unique angle from which each person encounters that mystery. Finally, astrology must never be chained too tightly to any single religion or metaphysical system. Its only legitimate absolute is the intensification of self‑awareness.

**Complete Chinese Interpretation (Secondary Language)**:
Forrest 把自己的立场浓缩成七条原则，组成所谓「成长导向占星」的骨干。第一，星象符号本身是中性的，没有天生吉星、天生凶星之分；所有符号只是一组潜在过程的描述。第二，真正对命盘负责的，是人而不是行星——我们选择如何体现这些象征，才决定了现实结果。第三，单凭命盘本身，任何占星师都无法看出一个人究竟在「高水平」还是「低水平」回应，意识状态不能像读报表那样从盘面上直接抄出。

第四，命盘是一张「最快乐、最充实、最具灵性创造性人生道路」的蓝图，而不是一张所有灾难可能性的清单。第五，当我们偏离这条蓝图所指示的成长轨迹时，生活通常会陷入不稳定、空虚、焦虑等状态——这些是「失衡的信号」，而不是「命盘很糟糕」的证据。第六，在整个系统中，真正的绝对只有两个：生命本身不可化约的神秘，以及每个人在面对这一神秘时所站立的独特视角。最后，占星一旦被过紧地捆绑在任何单一宗教或哲学体系上，就会受损；对占星而言，唯一值得坚持的绝对，是不断加深一个人对自我与生命的觉察。

**Core Points**:
- Seven principles summarize the ethical and philosophical core of growth‑oriented astrology.
- Symbols are neutral; embodiment is the individual’s responsibility.
- The chart is a blueprint for optimal growth, not a catalogue of doom.
- Deviations from the growth pattern manifest as unstable, anxious states.
- Astrology’s only absolutes are mystery, uniqueness, and intensified self‑awareness.

**Detailed Explanation**:
These seven principles can be read as a contract between astrologer and client, as well as between astrology and psychology. Neutral symbols protect against superstition and moralistic labeling. Personal responsibility ensures that astrology does not become an excuse for avoiding change: "I’m just like this because of my chart" is no longer acceptable. The insistence that level of response cannot be seen in the wheel guards against spiritual elitism and projection.

Viewing the chart as a blueprint for the happiest available path reframes difficult configurations as challenging tools rather than curses. The description of unstable states as deviations from ideal growth replaces static notions of "good" and "bad" charts with a dynamic model of alignment versus misalignment. Finally, separating astrology from any single dogmatic framework keeps the practice flexible and human‑centered; its legitimacy rests on whether it deepens self‑awareness, not on whether it defends a particular theology.

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: The bullet list is preserved almost exactly, but lightly normalized into sentences in the paraphrase. The phrase "astrology's bad karma" is not repeated literally in paraphrase, but its meaning is captured in the idea of practices that belong to astrology's problematic past rather than its future.
- **中文**：七条原则在中文中保持「逐条呈现 + 合并解释」的结构，以免机械翻译。"bad karma" 直译为「坏业」会显得突兀，这里通过「占星的糟糕历史包袱」的含义间接表达，不在字面上出现。对「only two absolutes」则用「真正的绝对只有两个」明确强调其限缩作用。

**Narrative Snippets**:
- `[ns_innersky_025]` `[trigger: good_bad_chart_question]` `[factor_trigger: neutral_symbol]` `[role: 主干]` Astrological symbols are neutral—there are no good ones, no bad ones. → Source Text
- `[ns_innersky_026]` `[trigger: client_blames_chart]` `[factor_trigger: personal_responsibility]` `[role: 主干依赖]` Individuals are responsible for the way they embody their birthcharts. → Source Text
- `[ns_innersky_027]` `[trigger: predicting_behavior]` `[factor_trigger: level_of_response]` `[role: 条件分支]` No astrologer can determine a person's level of response from the birthchart alone. → Source Text
- `[ns_innersky_028]` `[trigger: growth_blueprint]` `[factor_trigger: chart_focalizers]` `[role: 总结]` The birthchart is a blueprint for the happiest, most fulfilling, most spiritually creative path of growth. → Source Text
- `[ns_innersky_029]` `[trigger: client_feels_anxious]` `[factor_trigger: discord]` `[role: 主干]` Deviations from the ideal growth pattern are usually accompanied by aimlessness, emptiness, and anxiety. → Source Text
- `[ns_innersky_030]` `[trigger: metaphysical_debate]` `[factor_trigger: balance]` `[role: 主干依赖]` Nothing in the system matters except the intensification of a person's self-awareness. → Source Text
- `[ns_innersky_031]` `[trigger: astrology_necessity_question]` `[factor_trigger: integration]` `[role: 条件分支]` Nothing can be learned from a birthchart that could not be learned someplace else. → Source Text
- `[ns_innersky_032]` `[trigger: alternative_growth_path]` `[factor_trigger: modality]` `[role: 总结]` Go into psychotherapy, meditate in a monastery, fall in love—any of those might do the same thing. → Source Text
- `[ns_innersky_033]` `[trigger: speed_advantage]` `[factor_trigger: concrete_bit]` `[role: 主干]` Astrology's principal advantage is speed—it compresses years of trial and error into concentrated insight. → Source Text
- `[ns_innersky_034]` `[trigger: insight_integration]` `[factor_trigger: element_system]` `[role: 主干依赖]` All that fine information can go in one ear and out the other. → Source Text
- `[ns_innersky_035]` `[trigger: responsibility_for_change]` `[factor_trigger: element]` `[role: 条件分支]` Astrology does not change people any more than psychotherapy changes people—people change themselves. → Source Text
- `[ns_innersky_036]` `[trigger: realistic_expectations]` `[factor_trigger: element_fire]` `[role: 总结]` Astrology is just one more path to self-knowledge, with certain advantages and disadvantages. → Source Text
- `[ns_innersky_037]` `[trigger: peace_seeking]` `[factor_trigger: astro_philosophy AND astro_alignment]` `[role: 主干]` Peace is the objective—but it arises only when we align outer personality with inner essence. → Source Text
- `[ns_innersky_038]` `[trigger: hedonistic_astrology]` `[factor_trigger: astro_philosophy AND astro_wellbeing]` `[role: 主干依赖]` Astrology is hedonistic: all that matters to it is happiness and the relief of suffering. → Source Text
- `[ns_innersky_039]` `[trigger: mirror_metaphor]` `[factor_trigger: astro_philosophy AND astro_reflection]` `[role: 条件分支]` A mirror reflecting life, astrology observes but does not interpret—it simply shows us who we are. → Source Text
- `[ns_innersky_040]` `[trigger: releasing_scripts]` `[factor_trigger: astro_psychology AND astro_growth]` `[role: 总结]` We must let go of those social scripts that upset us and grow toward our true nature. → Source Text
- `[ns_innersky_041]` `[trigger: witnessing_self]` `[factor_trigger: astro_philosophy AND astro_awareness]` `[role: 主干]` Through astrology we stand outside our personalities and witness the central core around which all minutiae orbit. → Source Text
- `[ns_innersky_042]` `[trigger: self_reminder]` `[factor_trigger: astro_psychology AND astro_identity]` `[role: 主干依赖]` Astrology helps us feel better by reminding us of who we are beneath the roles and programming. → English Paraphrase
- **Natural Attributes**:
  - Symbolism: Peace, happiness, mirror, witnessing, scripts, essence.
  - Characteristics: Experience-centered, outcome-focused, non-moralistic, reflective.
  - Elements: Psychological alignment, relief of suffering, self-recognition.
- **Functional Symbolism**:
  - Uses the chart to highlight misalignments between outer personality and inner essence.
  - Supports the release of harmful social scripts in favor of more authentic choices.
  - Provides a reflective space in which clients can witness themselves and move toward peace.
- **Conditional Structure**:
  - **Necessary Conditions**: Astrology is applied with the explicit aim of increasing clarity and well-being.
  - **Enhancing Conditions**: Client is willing to question inherited scripts and experiment with new behaviors.
  - **Nullifying Conditions**: Using astrology mainly to reinforce shame, guilt, or rigid moral judgments.
  - **Temporal Scope (check applicable items)**:
    - [x] Natal layer: Applies to natal chart analysis
    - [ ] Transit layer: Applies to planetary transit analysis
    - [ ] Progression layer: Applies to progressed chart analysis
- **Multi-layered Interpretation**:
  - Literal Layer: Concrete practices of naming pain, desires, and misaligned scripts.
  - Symbolic Layer: Astrology as a mirror and as a tool for aligning essence and personality.
  - Practical Layer: Guiding clients toward choices that reduce suffering and increase authenticity.
  - Psychological Layer: Cultivating self-compassion, self-recognition, and inner peace.

- **L2-Term Glossary**:

| English Term             | Chinese Term        | English Definition                                                                | Chinese Definition                                                               |
|--------------------------|---------------------|------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| hedonistic astrology     | 享乐取向占星        | An approach that prioritizes relief of suffering and increase of genuine happiness | 以减轻痛苦、提升真实幸福感为首要目标的占星取向                                    |
| inner essence            | 内在本质            | The core individuality or soul-level pattern beneath social roles and scripts     | 社会角色与脚本之下，更深一层的个体核心或灵魂结构                                 |

- **L2-Term Glossary**:

| English Term            | Chinese Term        | English Definition                                                                | Chinese Definition                                                               |
|-------------------------|---------------------|------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| sign system             | 星座符号系统        | The set of zodiac signs understood as inner growth patterns and identity styles   | 把黄道十二星座视为内在成长路径与身份风格的一整套符号系统                          |
| house system            | 宫位符号系统        | The set of houses representing concrete life arenas and tasks                     | 代表具体生活领域与必须面对任务的一整套宫位符号系统                               |
| planetary functions     | 行星心理功能        | Psychological functions symbolized by planets (thinking, feeling, relating, etc.) | 由行星所象征的一组心理机能，如思考、情感、关系需求等                             |
| identity process        | 身份化过程          | Ongoing inner process through which a sign’s pattern becomes part of "who I am"  | 某一星座的成长模式逐渐被个体认同为「我是谁」的动态过程                           |
| life arena              | 生命舞台 / 生活领域 | A concrete field of experience indicated by a house                               | 由某一宫位所指向的具体经验领域，如事业、关系、金钱、潜意识等                      |
<!-- L2_END -->

<!-- FACTOR_BEGIN -->
| Factor Type | Factor Label                                | Factor ID | Factor Source | Role/Position        | Value/Constraints                          | Notes | engine_id |
|------------|---------------------------------------------|-----------|--------------|----------------------|--------------------------------------------|-------|------------|
| Structure  | Sign system as identity/growth dimension    |           | new_candidate | Symbol Dimension     | Describes inner style and growth patterns  | Complements houses and planets        | astro_semantic |
| Structure  | House system as arena/life-domain dimension |           | new_candidate | Symbol Dimension     | Describes external fields and tasks        | Must be combined with signs/planets   | astro_semantic |
| Structure  | Planetary system as function dimension      |           | new_candidate | Symbol Dimension     | Describes psychological functions          | Operates across all signs and houses  | astro_semantic |
| Relational | Sign–House–Planet triadic combination       |           | new_candidate | Composite Structure  | Requires all three symbol sets             | Basis for full interpretations        | astro_semantic |
<!-- FACTOR_END -->

---

#### 2. Interpretive Grammar – Planet = What, Sign = How/Why, House = Where"""
    normalized_text_zh: str = """"""
    subject: str = "Seven Principles of Growth-Oriented Astrology"
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
        l1_anchor="tis_v1.0.0_seven_principles_of_growth_ori_001_L1",
    )
    version: str = "1.0.0"
