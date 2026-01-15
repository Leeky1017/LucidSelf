"""
Auto-generated semantic module for collected_works
Generated at: 2025-12-05T13:30:20.574949
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
    semantic_id="cw_v1.0.0_source_text_008",
    book_id="collected_works",
    engine_id="psych"
)
class SourceText(SemanticEntry):
    """
    "Besides the two attitudes, there are four functions of consciousness: Thinking and Feeling are the ...
    """
    
    original_text: str = """"Besides the two attitudes, there are four functions of consciousness: Thinking and Feeling are the rational or judging functions; Sensation and Intuition are the irrational or perceiving functions. These form two pairs of opposites."

#### English Paraphrase (Primary Language)

**Four functions** = Four ways consciousness relates to reality:

| Function | Type | Definition | Opposite |
|----------|------|------------|----------|
| **Thinking** | Rational/Judging | Logical analysis, true/false judgment | Feeling |
| **Feeling** | Rational/Judging | Value judgment, pleasant/unpleasant | Thinking |
| **Sensation** | Irrational/Perceiving | Direct sensory perception, "what is" | Intuition |
| **Intuition** | Irrational/Perceiving | Unconscious perception, "what could be" | Sensation |

**Rational (judging)**: T and F make judgments about reality.
**Irrational (perceiving)**: S and N perceive without evaluation.

**Function hierarchy** in each person:
1. **Superior**: Most developed, conscious, reliable
2. **Auxiliary**: Second strongest, supports superior
3. **Tertiary**: Weaker, less differentiated
4. **Inferior**: Least developed, unconscious, primitive

#### Complete Chinese Interpretation (Secondary Language)

**四功能** = 意识与现实关联的四种方式：

| 功能 | 类型 | 定义 | 对立面 |
|------|------|------|--------|
| **思维** | 理性/判断 | 逻辑分析，真/假判断 | 情感 |
| **情感** | 理性/判断 | 价值判断，愉快/不愉快 | 思维 |
| **感觉** | 非理性/感知 | 直接感官知觉，"是什么" | 直觉 |
| **直觉** | 非理性/感知 | 无意识知觉，"可能是什么" | 感觉 |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_jung_8 | concept | jung_8 | system | Theoretical | When theoretical framework connects concept to system | connecting | Source #jung |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_jung_8 | "Source text" | jung_8 | Concept -> application | Theory | High | Yes | rule_jung_8 |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_jung_8 | Core concept | | relevant | | relevant | System |
<!-- L2.5_END -->

**理性（判断型）**：思维和情感对现实做判断。
**非理性（感知型）**：感觉和直觉只感知不评判。

**每人的功能层级**：
1. **优势**：最发达、意识、可靠
2. **辅助**：第二强、支持优势
3. **第三**：较弱、分化不足
4. **劣势**：最弱、无意识、原始

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Thinking | Logical judgment | Rational function |
| Feeling | Value judgment | Rational function |
| Sensation | Direct perception | Irrational function |
| Intuition | Unconscious perception | Irrational function |

#### Core Points

- Four functions: Thinking, Feeling, Sensation, Intuition
- Two rational (T/F) + Two irrational (S/N)
- Two pairs of opposites: T↔F, S↔N
- Hierarchy: Superior → Auxiliary → Tertiary → Inferior

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Four Functions: Thinking (logic), Feeling (values), Sensation (concrete), Intuition (possibilities). Two rational (T/F) + two irrational (S/N). Function hierarchy from superior to inferior. Foundation for MBTI.
- **中文**: 四功能:思维(逻辑)、情感(价值)、感觉(具体)、直觉(可能性)。两种理性(T/F)+两种非理性(S/N)。功能层级从优势到劣势。MBTI基础。

**Narrative Snippets**:
- `[ns_jung_032]` `[trigger: four_functions]` `[factor_trigger: jung_thinking AND jung_feeling AND jung_sensation AND jung_intuition AND jung_four_functions]` `[role: 主干]` Four functions of consciousness: Thinking and Feeling are rational/judging; Sensation and Intuition are irrational/perceiving. → Core
- `[ns_jung_033]` `[trigger: opposite_pairs]` `[factor_trigger: jung_tf_axis AND jung_sn_axis]` `[role: 条件分支]` These form two pairs of opposites: Thinking↔Feeling (rational axis), Sensation↔Intuition (irrational axis). → Structure
- `[ns_jung_034]` `[trigger: function_hierarchy]` `[factor_trigger: jung_superior AND jung_inferior_function AND jung_function_hierarchy]` `[role: 条件分支]` Function hierarchy: Superior (most developed) → Auxiliary → Tertiary → Inferior (least developed, unconscious). → Development"""
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
        l1_anchor="cw_v1.0.0_source_text_008_L1",
    )
    version: str = "1.0.0"
