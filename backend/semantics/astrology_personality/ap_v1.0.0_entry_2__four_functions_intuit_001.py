"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238080
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
    semantic_id="ap_v1.0.0_entry_2__four_functions_intuit_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry2FourFunctionsIntuit(SemanticEntry):
    """
    **Source Text** (Lines 7143-7257):
> The Significance of the Twelve Houses... The two axes mentioned...
    """
    
    original_text: str = """**Source Text** (Lines 7143-7257):
> The Significance of the Twelve Houses... The two axes mentioned above represent the structure of space... They form his cross of incarnation...
>
> The cross of particular selfhood for man generates four basic modes of being, four fundamental operations in the process of living as an individual. These can be described (using C. G. Jung's nomenclature) as: Intuition, Feeling, Sensation, Thinking.
>
> The horizon is the line of awareness... Ascendant = pure self-awareness; Descendant = awareness of others. Thus intuition and sensation are seen as two complementary factors...
>
> The vertical axis relates to the rational operations of the self... Feeling is the result of intuition, just as thinking is the result of sensation.

**Key Term Analysis**:
- **Four functions (Jung)**: `Intuition, Feeling, Sensation, Thinking` / `four basic modes of being`
- **Horizontal axis (Awareness)**: `Ascendant = self-awareness (intuition)` / `Descendant = awareness of others (sensation)`
- **Vertical axis (Experience)**: `Nadir = feeling (subjective experience)` / `Zenith = thinking (objective experience)`
- **Irrational vs Rational**: `horizontal = irrational (awareness)` / `vertical = rational (experience/judgment)`

**English Paraphrase (Primary Language)**:
The two axes generate four basic modes of being (Jung's four functions):
- **Horizontal (Awareness)**: Ascendant = Intuition (self-awareness); Descendant = Sensation (awareness of others)
- **Vertical (Experience)**: Nadir = Feeling (subjective experience); Zenith = Thinking (objective experience)

"Feeling is the result of intuition, just as thinking is the result of sensation." Horizontal = irrational; Vertical = rational.

**Complete Chinese Interpretation (Secondary Language)**:
两条轴生成四种基本存在模式（荣格的四功能）：
- **水平轴（觉知）**：上升点=直觉（自我觉知）；下降点=感官（对他者的觉知）
- **垂直轴（经验）**：天底=感受（主观经验）；中天=思维（客观经验）

"感受是直觉的结果，正如思维是感官的结果。"水平=非理性；垂直=理性。

**Narrative Snippets**:
- `[ns_aop_157]` `[trigger: four_functions]` `[factor_trigger: astro_jung_four_functions AND astro_analytical_psych AND astro_coll_uncons_struct AND jung_four_functions]` `[role: 主干]` Four Jungian functions: Intuition, Feeling, Sensation, Thinking as four modes of being. → L7172-7175
- `[ns_aop_158]` `[trigger: horizontal_vertical]` `[factor_trigger: experience AND axes_functions]` `[role: 主干依赖]` Horizontal = awareness (irrational); Vertical = experience (rational). → L7203-7257"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 2: Four Functions—Intuition, Feeling, Sensation, Thinking"
    factor_refs: list = ['func_intuition', 'func_sensation', 'func_feeling', 'func_thinking']
    
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
        book_id="astrology_personality",
        chapter="",
        l1_anchor="ap_v1.0.0_entry_2__four_functions_intuit_001_L1",
    )
    version: str = "1.0.0"
