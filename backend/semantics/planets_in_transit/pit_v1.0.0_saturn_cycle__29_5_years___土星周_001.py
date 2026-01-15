"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.251550
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
    semantic_id="pit_v1.0.0_saturn_cycle__29_5_years___土星周_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SaturnCycle295Years土星周(SemanticEntry):
    """
    **Source Text** (Paraphrased from Hand):
> "Saturn's approximately 29.5-year orbital period creates ...
    """
    
    original_text: str = """**Source Text** (Paraphrased from Hand):
> "Saturn's approximately 29.5-year orbital period creates the fundamental maturation cycle in human life. Saturn rules structure, responsibility, limitation, discipline, and reality. Its cycle divides naturally into four 7-year quarters, each representing a developmental phase. The Saturn return at ages 29-30 and 58-60 marks major life restructuring periods."

**English Paraphrase (Primary Language)**:
The **Saturn cycle** (29.5 years) is astrology's primary **maturation cycle**, governing the progressive development from childhood through adulthood to elder wisdom. Saturn symbolizes **reality principle**: structure, limitation, discipline, responsibility, time, authority, ambition. Its transit cycle provides the fundamental timeline for psychological and social maturation. The cycle divides into **four 7-year quarters** (~7.4 years each): (1) **Crisis Quarter** (0-7.4): initial contact with limitation, structure begins; (2) **Action Quarter** (7.4-14.8): working with structures, building competence; (3) **Establishment Quarter** (14.8-22.2): consolidating achievements, mature structures; (4) **Transition Quarter** (22.2-29.5): preparing for next cycle, old structures dissolve. **Saturn returns** (ages 29-30, 58-60) are especially potent: Saturn returns to its natal position, completing one full cycle. These periods bring **reality confrontations**—what we built that lacks solid foundation crumbles; what's real and authentic strengthens. First return (late 20s) ends youth and demands adult responsibility. Second return (late 50s) brings legacy questions and elder wisdom. Hand emphasizes Saturn's 29.5-year cycle **exactly parallels** the Chinese **大运** (Great Fortune) 30-year cycle—one of the most precise East-West correlations in timing systems.

**Complete Chinese Interpretation (Secondary Language)**:
在行运体系中，土星约 29.5 年一周的轨道，被视为**人类一生最重要的"成熟结构周期"**。它象征现实原则：结构、责任、限制、纪律与时间本身。汉德把这 29.5 年自然划分为四个约 7 年的阶段：从儿童第一次真实感受到"规则与边界"，到青少年学习在规则内行动，再到二十出头巩固自我与社会身份，最后在 30 岁前后对既有结构进行清算与重组。每一阶段都像一次"结构课"：不是马上给你成果，而是一点点训练你面对现实、承受压力、为自己的人生负责。其中最关键的是两次**土星回归**：第一次大约在 29–30 岁，当行运行土星回到本命土星的位置，意味着第一轮成熟循环的结算——那些虚浮、没有结构支撑的东西会在这一段时间内崩塌，真正有根基的部分会被保留下来并进一步强化，这也是"告别少年、正式成为大人"的经典节点；第二次大约在 58–60 岁，则把焦点从"建立人生"转向"如何收束与传承"，促使人重新评估自己这一生的结构是否值得留下、要以怎样的面貌进入老年阶段。汉德特别指出，这一 29.5 年循环与中国命理中的**大运 30 年**高度同构：两者都刻画"人生大的结构性更迭周期"，内部又往往细分为若干 7–10 年的小阶段。

**Key Term Analysis**:
- **Saturn Cycle**: `29.5-year orbit` / `maturation timeline` / `reality principle`
- **Four Quarters**: `7-year phases` / `developmental stages` / `crisis/action/establishment/transition`
- **Saturn Return**: `ages 29-30, 58-60` / `major restructuring` / `reality confrontation`

**Core Points** (decomposed, no upper limit):
- 29.5-year cycle = one complete Saturn orbit = maturation cycle
- Four 7-year quarters: Crisis/Action/Establishment/Transition developmental phases
- Saturn return (ages 29-30, 58-60): Major life restructuring points
- Reality principle: Structure, responsibility, limitation, discipline themes
- First return (29): End youth, begin adult responsibility
- Second return (58): Legacy questions, elder wisdom
- East-West parallel: Precisely matches 大运 30-year cycle
- Ages 7/14/21/29/58 = major life structuring points
- What's real and authentic strengthens; what lacks foundation crumbles

**Detailed Explanation**:
The Saturn cycle is nature's curriculum for maturation. Each 7-year quarter teaches specific lessons: Crisis teaches you that limitations exist; Action teaches you to work within them; Establishment teaches you to build lasting structures; Transition teaches you to prepare for renewal. The Saturn returns are the exams—moments when everything you've built is tested for authenticity and durability.

**Narrative Snippets** (English only, decomposed):
- `[ns_hand_pit_031]` `[trigger: saturn_cycle]` `[factor_trigger: astro_saturn_cycle]` `[role: 主干]` Saturn's 29.5-year cycle is the fundamental maturation cycle in human life. → Source Text
- `[ns_hand_pit_032]` `[trigger: four_quarters]` `[factor_trigger: astro_four_quarters]` `[role: 主干依赖]` Four 7-year quarters: Crisis, Action, Establishment, Transition. → Source Text
- `[ns_hand_pit_033]` `[trigger: saturn_return]` `[factor_trigger: astro_saturn_return]` `[role: 条件分支]` Saturn return (29-30, 58-60) marks major life restructuring and reality testing. → Source Text
- `[ns_hand_pit_034]` `[trigger: east_west_parallel]` `[factor_trigger: astro_east_west_parallel]` `[role: 总结]` Saturn cycle precisely parallels Chinese 大运 30-year cycle. → Source Text

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: N/A: Single authoritative source (Hand's "Planets in Transit" 1976). The Saturn cycle is foundational to modern predictive astrology.
- **中文**: 无版本差异：单一权威来源（Hand《行运中的行星》1976）。土星周期是现代预测占星的基础。"""
    normalized_text_zh: str = """"""
    subject: str = "Saturn Cycle (29.5 Years) (土星周期)"
    factor_refs: list = ['astro_saturn_cycle', 'astro_four_quarters', 'astro_saturn_return', 'astro_reality_testing', 'astro_maturation_cycle']
    
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
        l1_anchor="pit_v1.0.0_saturn_cycle__29_5_years___土星周_001_L1",
    )
    version: str = "1.0.0"
