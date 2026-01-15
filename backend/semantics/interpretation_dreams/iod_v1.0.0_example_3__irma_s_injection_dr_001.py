"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.460931
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
    semantic_id="iod_v1.0.0_example_3__irma_s_injection_dr_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class Example3IrmaSInjectionDr(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Overdetermination | Multiple causes per element | No simple 1:1 code |
| Composite Figure | Multiple people merged | Irma=4+ women |
| Economic Principle | Max meaning, min material | Dream efficiency |
| Analytic Resistance | Layers resist interpretation | Multiple meanings |

**Revisited - Overdetermination Principle**:

**Source Text** (key passage):
"The dream fulfills several wishes, which were actuated by the occasion of the preceding evening (Otto's news, and the writing of the clinical history). The result of the dream is that I am not responsible for the persistence of Irma's pains, but that Otto is responsible for them."

**Overdetermination** (多重决定) means:
- Every dream element has **multiple causes**
- Every wish has **multiple representations**
- **Irma = composite figure**:
  - Real patient Irma
  - Freud's wife
  - Friend who resisted treatment
  - Female friend who died from injection

**Why overdetermination matters**:
1. Makes dreams **resistant to analysis** (multiple layers)
2. Every element **multiply meaningful** (no simple 1:1 symbol code)
3. **Economic principle**: Dream work achieves maximum expression with minimum material
4. Explains why dreams seem **absurd** yet feel **significant**

**Complete Chinese Interpretation (Secondary Language)**:

“伊尔玛注射之梦”的再次讨论，重点不再是责任推卸本身，而是用来说明梦的一个结构性原则：**多重决定（overdetermination）**。在这个梦里，表面上似乎只有一位名叫伊尔玛的病人，但细究其特征与联想，就会发现这个人物其实是由多位真实人物“叠加”而成的复合体：真实患者伊尔玛、妻子、拒绝治疗的朋友、曾因注射事故而死亡的熟人等。她的每一个细节，都同时连接着数条不同的记忆与情感线索。

这意味着，梦中的任何一个元素，往往都不是单一原因的结果，而是多种动机与经历的交汇点——**每个梦元素有多重原因，每个愿望也有多重表征**。正因如此，梦才会表现出对分析的“顽固性”：当我们以为已经为某个符号找到满意解释时，新的联想又会打开另一层含义，提醒我们它还承载着别的东西。这种多重决定打破了“一个符号=一个意义”的机械解梦模式，迫使分析工作尊重心灵材料的复杂性。

从经济角度看，多重决定也说明梦的工作如何“以最少的显梦材料，达成最多的潜在表达”：有限的画面与情节被用来承载成串的记忆与愿望，这既解释了梦在形式上的**荒诞与碎片化**，也解释了为什么即便内容看似胡乱拼贴，梦者却常常体验到一种“这里面有东西”的深刻感受——那是因为多条意义在同一个象征点上叠加，使得那个点自然显得格外“重”。

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Irma's Injection (Overdetermination): Every dream element has multiple causes, every wish has multiple representations. Irma=composite figure (4+ women). Breaks 1:1 symbol=meaning paradigm. Economic principle: max meaning, min material.
- **中文**: 伊尔玛注射(多重决定):每个梦元素有多重原因,每个愿望有多重表征。伊尔玛=复合人物(4+女性)。打破1:1符号=意义范式。经济原则:最大意义,最少材料。

**Narrative Snippets**:
- `[ns_freud_ex_007]` `[trigger: overdetermination_example]` `[factor_trigger: dream_work_overdetermination]` `[role: 主干]` Irma's Injection: every element has multiple causes; Irma = composite of 4+ women. → Example
- `[ns_freud_ex_008]` `[trigger: composite_figure]` `[factor_trigger: dream_work_overdetermination AND condensation]` `[role: 条件分支]` Composite figure merges multiple people; breaks 1:1 symbol-meaning paradigm. → Mechanism
- `[ns_freud_ex_009]` `[trigger: analytic_resistance]` `[factor_trigger: dream_work_overdetermination AND interpretation]` `[role: 条件分支]` Multiple layers resist interpretation; new associations reveal further meanings. → Process"""
    normalized_text_zh: str = """"""
    subject: str = "Example 3: Irma's Injection Dream (Overdetermination)"
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
        book_id="interpretation_dreams",
        chapter="",
        l1_anchor="iod_v1.0.0_example_3__irma_s_injection_dr_001_L1",
    )
    version: str = "1.0.0"
