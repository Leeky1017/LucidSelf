"""
Auto-generated semantic module for astrological_houses
Generated at: 2025-12-05T13:30:20.333822
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
    semantic_id="ah_v1.0.0_angular_succedent_cadent_class_001",
    book_id="astrological_houses",
    engine_id="astro"
)
class AngularSuccedentCadentClass(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Angular | 1,4,7,10 | Act...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Angular | 1,4,7,10 | Action/initiative |
| Succedent | 2,5,8,11 | Consolidation |
| Cadent | 3,6,9,12 | Distribution |
| Threefold Cycle | Repeats 4x | Rhythm |

#### Source Text

"The twelve houses are classified into three groups of four: Angular houses (1, 4, 7, 10) represent action and initiative, forming the cardinal cross. Succedent houses (2, 5, 8, 11) represent consolidation and substance, embodying fixed quality. Cadent houses (3, 6, 9, 12) represent distribution and transition, manifesting mutable quality. This three-phase cycle (action→consolidation→distribution) repeats four times around the chart."

#### English Paraphrase (Primary Language)

Rudhyar's house classification system divides the twelve houses into three functional groups. The four Angular houses (1st, 4th, 7th, 10th) mark the cardinal cross, representing initiatory action and primary life orientations. The four Succedent houses (2nd, 5th, 8th, 11th) follow the angular, consolidating and stabilizing what was initiated, building substance and security. The four Cadent houses (3rd, 6th, 9th, 12th) precede the next angular house, distributing energy outward and transitioning between cycles. This threefold pattern—action, consolidation, distribution—repeats four times, creating a rhythm that structures consciousness unfoldment through the houses.

#### Complete Chinese Interpretation (Secondary Language)

完整中文诠释：鲁迪亚将十二宫依功能分为三类循环的宫群：**始宫/角宫（Angular，1/4/7/10）**、**续宫（Succedent，2/5/8/11）** 与 **果宫/衰宫（Cadent，3/6/9/12）**。角宫对应基本星座气质，是整轮循环的“启动点”：每逢落入角宫的行星，都会倾向于主动发起、表态或推动事件发展，因此这些位置往往代表生命中最核心的行动与抉择场域。续宫承接角宫之后的能量，好比“建设与积累阶段”：把之前启动的意图具体化、物质化，形成可持续的结构与资源——因此与稳定、安全感、拥有感密切相关。果宫则处在下一轮角宫之前，承担“分配与过渡”的角色：把已经累积起来的能量向外释放、传播或消化，同时为下一轮新的起点腾出空间，因而带有流动、调整与过门的性质。

这三类宫位构成一个**行动→巩固→分配/过渡**的三相节律，并沿着十二宫重复四次：1-2-3 宫是一轮个人层面的起承转，4-5-6 宫是一轮内在/日常生活层面的起承转，7-8-9 宫扩展到他人与意义世界，10-11-12 宫则提升到社会与集体/潜意识层面。这样一来，命盘不是十二个互不相关的格子，而是四圈连续的三段式过程；阅读宫位时，既要看单一宫位的含义，也要看它在“三步走”节律中所处的位置——是点燃新的行动、把既有成果坐实，还是把能量散布出去并为下一阶段做心理与环境上的准备。

#### Core Points

- **Angular (1,4,7,10)**: Action, initiative, cardinal quality, life orientation
- **Succedent (2,5,8,11)**: Consolidation, substance, fixed quality, stability
- **Cadent (3,6,9,12)**: Distribution, transition, mutable quality, preparation
- **Threefold cycle**: Repeats four times around chart

#### Narrative Snippets

- `[ns_rudhyar_asc_001]` `[trigger: house_classification]` `[factor_trigger: astro_angular OR astro_succedent OR astro_cadent AND house_system_12]` `[role: 主干]` The twelve houses are classified into three groups: Angular houses (1,4,7,10) represent action and initiative; Succedent houses (2,5,8,11) represent consolidation and substance; Cadent houses (3,6,9,12) represent distribution and transition. → The Astrological Houses Classification
- `[ns_rudhyar_asc_002]` `[trigger: angular_houses]` `[factor_trigger: astro_houses_angular AND angles_cardinal_cross]` `[role: 条件分支]` Angular houses mark the cardinal cross—the four most powerful positions in any natal chart. Planets here act with directness, initiating new phases of life. → The Astrological Houses Classification
- `[ns_rudhyar_asc_003]` `[trigger: succedent_houses]` `[factor_trigger: astro_houses_succedent AND houses_succedent]` `[role: 条件分支]` Succedent houses follow the angular, consolidating what was initiated, building substance, security, and resources. → The Astrological Houses Classification
- `[ns_rudhyar_asc_004]` `[trigger: cadent_houses]` `[factor_trigger: astro_houses_cadent AND houses_cadent]` `[role: 条件分支]` Cadent houses precede the next angular, distributing energy outward, preparing for transition, and processing experience. → The Astrological Houses Classification
- `[ns_rudhyar_asc_005]` `[trigger: threefold_cycle]` `[factor_trigger: astro_house_cycle]` `[role: 总结]` The threefold pattern—action, consolidation, distribution—repeats four times around the chart, creating the rhythm that structures consciousness unfoldment. → The Astrological Houses Classification

#### L2 Semantic Extraction

- **Theme**: Threefold functional classification structuring house cycle through action-consolidation-distribution rhythm

- **Natural Attributes**:
  - Symbolism: Threefold rhythm, cyclical unfoldment, functional phases
  - Characteristics: Angular (cardinal), Succedent (fixed), Cadent (mutable)
  - Elements: Four cardinal points, four fixed positions, four mutable transitions

- **Functional Symbolism**:
  - Angular function: Initiates new phase, establishes orientation
  - Succedent function: Consolidates initiated energy, builds substance
  - Cadent function: Distributes consolidated energy, prepares transition

- **Conditional Structure**:
  - Necessary Conditions: Understanding of cardinal/fixed/mutable qualities, recognition of cyclic patterns
  - Enhancing Conditions: Awareness of four elemental cycles (fire/earth/air/water houses)
  - Nullifying Conditions: Treating houses as isolated units without recognizing functional patterns

- **Multi-layered Interpretation**:
  - Literal Layer: Three groups of four houses each
  - Symbolic Layer: Threefold cosmic rhythm (beginning-middle-end)
  - Practical Layer: Life phases (initiation-consolidation-transition)
  - Philosophical Layer: Consciousness unfoldment through rhythmic cycles

#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | Notes | engine_id |
|-------------|--------------|-----------|---------------|---------------|-------------------|-------|------------|
| **Structure** | Angular houses | houses_angular | existing | Action Houses | 1,4,7,10 | Cardinal cross | astro_semantic |
| **Structure** | Succedent houses | houses_succedent | existing | Consolidation Houses | 2,5,8,11 | Fixed quality | astro_semantic |
| **Structure** | Cadent houses | houses_cadent | existing | Distribution Houses | 3,6,9,12 | Mutable quality | astro_semantic |
| **Temporal** | Threefold cycle | | new_candidate | Rhythmic Pattern | Action→Consolidation→Distribution | Repeats 4 times | astro_semantic |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_House_Philosophy_12H_20 | concept | House_Philosophy_12H_20 | system | Framework | When framework connects concept to system interpretation | connecting | Source |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_House_Philosophy_12H_20 | "Source" | House_Philosophy_12H_20 | Concept -> application | Theory | High | Yes | rule_House_Philosophy_12H_20 |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_House_Philosophy_12H_20 | Core concept | | relevant | relevant | relevant | System |
<!-- L2.5_END -->

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Rudhyar's tripartite classification: Angular (cardinal/action), Succedent (fixed/consolidation), Cadent (mutable/distribution). 4 cycles of 3 phases. Parallels Chinese 三合局/四正四马.
- **中文**: Rudhyar的三分类:角宫(基本/行动)，续宫(固定/巩固)，果宫(变动/分配)。4轮3相循环。平行中国三合局/四正四马。

---

## PART 3: The Four Angles and Zodiacal Polarities

### 21. Polarity Principle and Axis Interpretation"""
    normalized_text_zh: str = """"""
    subject: str = "Angular-Succedent-Cadent Classification"
    factor_refs: list = ['engine_id']
    
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
        book_id="astrological_houses",
        chapter="",
        l1_anchor="ah_v1.0.0_angular_succedent_cadent_class_001_L1",
    )
    version: str = "1.0.0"
