"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.460942
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
    semantic_id="iod_v1.0.0_example_4__children_s_transpar_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class Example4ChildrenSTranspar(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Transparent Dreams | Direct wish satisfaction | Weak censorship |
| Children's Dreams | Simple, undisguised | Prove thesis |
| Weak Censorship | Ego permissive | No distortion needed |
| Evidence Value | Dream's essential nature | Before complication |

**Source Text** (Freud's daughter, age 8.5):
"Just think, I dreamt that Emil was one of us, that he said papa and mamma to you, and slept at our house in the big room like our boys. Then mamma came into the room and threw a large handful of chocolate bars under our beds."

**Analysis**:
- **Day residue**: Excursion with neighbor's 12-year-old boy Emil, chocolate machine seen but denied
- **Manifest wish**: Emil becoming permanent family member + chocolate wish fulfilled
- **No distortion**: Child's dreams show wishes **transparently** (weak censorship)
- **Overdetermination**: Two wishes condensed (romantic/family wish + oral gratification)

**Key Insight**: **Children's dreams prove wish-fulfillment thesis**
- Simplest form: Direct, undisguised wish satisfaction
- **Why transparent?**: Sexual repression not yet developed, ego permissive
- Comparison: Adult dreams require elaborate distortion for same wishes
- **Evidence value**: Shows dream's essential nature before censorship complicates it

**Complete Chinese Interpretation (Secondary Language)**:

在这个儿童梦中，弗洛伊德 8 岁半的女儿梦见邻家男孩 Emil 成为自家的一员，像哥哥们一样住在家中，并且母亲走进屋里，从床底下撒出一大把巧克力棒。白天的情境是：她与 Emil 一同远足，在街上看到卖巧克力的机器却被拒绝购买。显梦与日间残余之间的联系极为直接：未被满足的**口欲愿望**（想吃巧克力）和对 Emil 的好感、想要建立更亲密、稳定关系的**家庭/浪漫愿望**，在梦里都被完整实现。

与成人梦不同，这个梦几乎**没有任何伪装或扭曲**：Emil 真的成了“我们家”的一员，巧克力也被大把撒在床底下任其拾取。正因为儿童的性压抑与复杂道德结构尚未发展，自我对愿望的宽容度更高，审查机制也更弱，梦才得以以如此透明、直接的方式呈现愿望满足的本质结构。

这个梦由此成为弗洛伊德理论中的关键证据：它以最“原始”、“简化”的形式，展示了梦如何把“未被满足的愿望”变成“已经实现的情境”。当我们把同样的逻辑应用到成人梦中时，虽然需要穿过更多层审查与扭曲，但可以看到结构并未改变，只是包装更复杂。儿童梦因此像是一扇窗口，让我们在审查机制尚未全面运作之前，观察到梦的本来面目。

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Children's Transparent Dreams: Prove wish-fulfillment thesis. Direct, undisguised satisfaction. Weak censorship (ego permissive). Shows dream's essential nature before adult complications.
- **中文**: 儿童透明梦:证明愿望满足命题。直接、未伪装的满足。弱审查(自我宽容)。展示成人复杂化之前梦的本质。

**Narrative Snippets**:
- `[ns_freud_ex_010]` `[trigger: transparent_dreams]` `[factor_trigger: children_dreams]` `[role: 主干]` Children's dreams: direct, undisguised wish satisfaction; prove wish-fulfillment thesis. → Evidence
- `[ns_freud_ex_011]` `[trigger: weak_censorship]` `[factor_trigger: children_dreams AND ego_development]` `[role: 条件分支]` Weak censorship: sexual repression undeveloped, ego permissive; no distortion needed. → Mechanism
- `[ns_freud_ex_012]` `[trigger: essential_nature]` `[factor_trigger: children_dreams AND theoretical_value]` `[role: 条件分支]` Shows dream's essential nature before adult complications; window into primitive form. → Theory"""
    normalized_text_zh: str = """"""
    subject: str = "Example 4: Children's Transparent Wish Dreams"
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
        l1_anchor="iod_v1.0.0_example_4__children_s_transpar_001_L1",
    )
    version: str = "1.0.0"
