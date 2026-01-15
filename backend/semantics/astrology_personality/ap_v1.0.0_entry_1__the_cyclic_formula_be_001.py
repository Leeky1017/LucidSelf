"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237926
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
    semantic_id="ap_v1.0.0_entry_1__the_cyclic_formula_be_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry1TheCyclicFormulaBe(SemanticEntry):
    """
    **Source Text** (Lines 4327-4394):
> At the close of the last chapter we referred to the Yi King of ...
    """
    
    original_text: str = """**Source Text** (Lines 4327-4394):
> At the close of the last chapter we referred to the Yi King of ancient China and to its "Formula of Change" based on the interplay of the two cosmic polarities Yang and Yin... The "Formula of Change" of the Yi King is a cyclic formula, which purports to determine symbolically the universal and essential structure of all cycles; better still, of the Cycle or of cyclicity. As all life-processes are cyclic—in essence, if not in outer appearance—such a formula becomes the basic law of all life-processes.
>
> Every cycle can be interpreted structurally as being composed of beginning, middle and end. These three terms, however, are to be understood in a metaphysical sense rather than in the sense of values of time... BEGINNING. The beginning of every cycle is a One: a monad... a monad is the initial point of emanation of any life-cycle. It is the germinating seed, or that point within the seed whence arise root and stem.

**Key Term Analysis**:
- **Cyclic formula**: `universal structure of cycles` / `Yang-Yin interplay` / `Yi King basis`
- **Beginning-middle-end**: `metaphysical sense` / `three essential factors` / `wholeness of cycle`
- **Monad/beginning**: `initial emanation point` / `germinating seed` / `root and stem source`

**English Paraphrase (Primary Language)**:
Rudhyar introduces the "cyclic formula"—the universal structure of all cycles, based on Yi King's Yang-Yin interplay. "As all life-processes are cyclic—in essence—such a formula becomes the basic law of all life-processes."

Every cycle has beginning, middle, end—metaphysically, not temporally. Beginning = monad, "the initial point of emanation," the germinating seed. This establishes the philosophical framework for interpreting astrological cycles.

**Complete Chinese Interpretation (Secondary Language)**:
Rudhyar引入"周期公式"——所有周期的普遍结构，基于易经的阴阳相互作用。"既然所有生命过程本质上都是周期性的，这样一个公式就成为所有生命过程的基本法则。"

每个周期有始、中、终——形而上学意义，而非时间意义。开始=单子，"发散的初始点"，萌发的种子。这为解释占星周期建立了哲学框架。

**Narrative Snippets**:
- `[ns_aop_123]` `[trigger: cyclic_formula]` `[factor_trigger: astro_cyclic]` `[role: 主干]` Cyclic formula: universal cycle structure from Yi King, basic law of all life-processes. → L4327-4343
- `[ns_aop_124]` `[trigger: beginning_monad]` `[factor_trigger: astro_monad]` `[role: 总结]` Beginning = monad, initial emanation point, germinating seed—metaphysical not temporal. → L4385-4394"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 1: The Cyclic Formula—Beginning, Middle, End"
    factor_refs: list = ['astro_cyclic_formula', 'astro_monad']
    
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
        l1_anchor="ap_v1.0.0_entry_1__the_cyclic_formula_be_001_L1",
    )
    version: str = "1.0.0"
