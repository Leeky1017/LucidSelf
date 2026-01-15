"""
Auto-generated semantic module for collected_works
Generated at: 2025-12-05T13:30:20.574984
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
    semantic_id="cw_v1.0.0_source_text_012",
    book_id="collected_works",
    engine_id="psych"
)
class SourceText(SemanticEntry):
    """
    "The transcendent function arises from the union of conscious and unconscious contents. It is not a ...
    """
    
    original_text: str = """"The transcendent function arises from the union of conscious and unconscious contents. It is not a function in the sense of thinking or feeling, but a psychic process that creates a third thing—a symbol—which transcends both poles."

#### English Paraphrase (Primary Language)

**Transcendent Function** = Psychic process that **unites opposites** and produces **third thing** (symbol).

**Not a function like T/F/S/N**, but a **process** that:
- Emerges when ego holds tension between opposites
- Does not choose either pole
- Allows unconscious to contribute
- Creates **symbol** that transcends both

**How it works**:
1. **Confrontation**: Conscious attitude meets unconscious content
2. **Tension**: Ego holds both without resolving
3. **Third emerges**: Symbol/solution transcending both
4. **Synthesis**: New conscious position integrating both

**Practical methods** to activate:
- Active imagination
- Dream work
- Artistic expression
- Holding paradox without resolution

#### Complete Chinese Interpretation (Secondary Language)

**超越功能** = 统一对立面并产生**第三物**（象征）的心理过程。

**不是像思维/情感/感觉/直觉那样的功能**，而是一种**过程**：
- 当自我持住对立面之间的张力时涌现
- 不选择任何一极
- 允许无意识参与
- 创造**象征**超越二者

**如何运作**：
1. **对峙**：意识态度遇见无意识内容
2. **张力**：自我持住两者不解决
3. **第三者涌现**：超越两者的象征/解决方案
4. **综合**：整合两者的新意识立场

**激活的实践方法**：
- 积极想象
- 梦的工作
- 艺术表达
- 持住悖论不求解决

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Transcendent Function | Process uniting opposites | Core transformation |
| Third Thing | Symbol from tension | Transcends both poles |
| Holding Tension | Not choosing either | Prerequisite |
| Active Imagination | Technique | Activation method |

#### Core Points

- Transcendent function = process (not function) uniting opposites
- Creates symbol/third thing transcending both poles
- Requires holding tension without premature choice
- Foundation of psychological transformation

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Transcendent Function: Process (not function) uniting opposites. Creates symbol/third thing. Requires holding tension. Activated via active imagination, dreams, art. Core of individuation.
- **中文**: 超越功能:统一对立面的过程(非功能)。创造象征/第三物。需要持住张力。通过积极想象、梦、艺术激活。个体化核心。

**Narrative Snippets**:
- `[ns_jung_044]` `[trigger: transcendent_function]` `[factor_trigger: jung_transcendent AND jung_union AND jung_transcendent_function]` `[role: 主干]` The transcendent function arises from union of conscious and unconscious contents—a psychic process that creates a third thing, a symbol. → Core
- `[ns_jung_045]` `[trigger: holding_tension]` `[factor_trigger: jung_tension AND jung_opposites AND jung_opposites_union AND jung_active_imagination]` `[role: 条件分支]` It emerges when ego holds tension between opposites without choosing either pole—allowing unconscious to contribute. → Process
- `[ns_jung_046]` `[trigger: symbol_creation]` `[factor_trigger: jung_symbol AND jung_transcendence AND jung_third_thing]` `[role: 条件分支]` The symbol transcends both poles, creating new conscious position integrating what seemed irreconcilable. → Product

#### L2 Semantic Extraction

- **Theme**: Psychic process creating synthetic third from opposing forces.
- **Natural Attributes**:
  - Symbolism: Bridge, third thing, symbol, transcendence.
  - Characteristics: Processual, emergent, synthetic.
  - Elements: Conscious, unconscious, tension, symbol.
- **Functional Symbolism**:
  - Bridges conscious-unconscious divide.
  - Produces symbols that carry transformative energy.
  - Enables psychological development beyond either/or.
- **Conditional Structure**:
  - **Necessary Conditions**: Opposites in tension, ego capacity to hold.
  - **Enhancing Conditions**: Active imagination, dream work, artistic expression.
  - **Nullifying Conditions**: Premature resolution, identification with one pole.
- **Multi-layered Interpretation**:
  - Literal Layer: Therapeutic technique.
  - Psychological Layer: Core mechanism of individuation.
  - Philosophical Layer: Hegelian thesis-antithesis-synthesis in psyche.
  - Eastern Layer: 超越功能↔中道/不二/持中.

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition |
|--------------|--------------|-------------------|-------------------|
| Transcendent function | 超越功能 | Psychic process uniting opposites through symbol | 通过象征统一对立面的心理过程 |
| Third thing | 第三物 | Symbol emerging from tension of opposites | 从对立面张力中涌现的象征 |
| Holding tension | 持住张力 | Maintaining opposites without premature resolution | 维持对立面不过早解决 |
| Active imagination | 积极想象 | Technique for engaging unconscious contents directly | 直接参与无意识内容的技术 |

#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-------|
| Process | Transcendent function | jung_transcendent_function | new_candidate | Integration Mechanism | Tension→Symbol | Core of transformation |
| Product | Third thing/Symbol | jung_third_thing | new_candidate | Process Output | Transcends both poles | Carries transformative energy |
| Method | Active imagination | jung_active_imagination | new_candidate | Technique | Conscious-unconscious dialogue | Primary activation method |

---

## L2-Term Glossary (P2 Additions)

| English Term | Chinese Term | English Definition | Chinese Definition |
|--------------|--------------|-------------------|-------------------|
| Psychological types | 心理类型 | Jung's typology system based on attitudes and functions | Jung基于态度和功能的类型学系统 |
| Attitude | 态度 | Fundamental orientation of psychic energy (E or I) | 心理能量的基本取向（外向或内向） |
| Function | 功能 | Mode of conscious orientation (T/F/S/N) | 意识取向的模式（思维/情感/感觉/直觉） |
| Type | 类型 | Combination of dominant attitude and function | 主导态度和功能的组合 |
| Function stack | 功能栈 | Hierarchy of four functions in a type | 某类型中四功能的层级 |

---

## Completion Summary

**Status**: ✅ v2.1 COMPLETE - Jung Core Psychology (P0 + P2)

**Achievements**:
- 12 core concepts fully upgraded to v2.1 format (6 P0 + 6 P2)
- Complete L1+L2+Factor Layer for all concepts
- Bilingual English-Chinese term glossary (45 technical terms)
- 100% template compliance
- East-West psychological correlations documented
- P2 Psychological Types + Alchemical Psychology complete

**Coverage**:
- **Foundational Theory** (3): Collective Unconscious, Archetype, Individuation
- **Core Components** (3): Shadow, Anima/Animus, Self
- **Psychological Types P2** (2): Introversion/Extraversion, Four Functions
- **Alchemical Psychology P2** (4): Coniunctio, Synchronicity, Opus Stages, Transcendent Function

**East-West Bridges Established**:
- Collective Unconscious ↔ 共通心性 (universal mind-nature)
- Anima/Animus ↔ 阴阳 (yin-yang)
- Self ↔ 道/梵我/本性 (Tao/Atman/Original Nature)
- Individuation ↔ 修行/自我实现 (cultivation/self-realization)
- Four Functions ↔ 四象 (four images)

**Quality Standards Met**:
- ✅ Complete bilingual structure (Primary English, Secondary Chinese)"""
    normalized_text_zh: str = """"""
    subject: str = "Source Text"
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
        book_id="collected_works",
        chapter="",
        l1_anchor="cw_v1.0.0_source_text_012_L1",
    )
    version: str = "1.0.0"
