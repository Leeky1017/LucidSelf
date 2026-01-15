"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.477418
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
    semantic_id="iod_v1.0.0_1_the_dream_narrative_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class 1TheDreamNarrative(SemanticEntry):
    """
    **Source Text**:
"Dream of July 23–24, 1895: A great hall—many guests whom we are receiving—among th...
    """
    
    original_text: str = """**Source Text**:
"Dream of July 23–24, 1895: A great hall—many guests whom we are receiving—among them Irma, whom I immediately take aside, as though to answer her letter, to reproach her for not yet accepting the 'solution.' I say to her: 'If you still have pains, it is really only your own fault.'"

"I take her to the window and look into her throat... I find a large white spot to the right, and at another place I see extended grayish-white scabs... I quickly call Dr. M., who repeats the examination."

"Dr. M. says: 'No doubt it is an infection, but it does not matter; dysentery will develop too, and the poison will be excreted.'... My friend Otto has recently given her an injection with a propyl preparation... propyls... propionic acid... Trimethylamine (the formula of which I see printed before me in heavy type)... Such injections are not made so rashly... Probably also the syringe was not clean."

**Key Term Analysis**:

| Term | Definition | Significance |
|------|-----------|---------------|
| Irma's Injection | 伊尔玛注射 | Freud's specimen dream | Prototype of dream analysis |
| Wish Fulfillment | 愿望满足 | Dream's core function | "Not my fault" |
| Day Residue | 日间残余 | Otto's visit, writing case history | Trigger for dream |
| Condensation | 凝缩 | Multiple figures in one | Irma = 3 women |
| Displacement | 移置 | Blame shifted to Otto | Self-exculpation |

**English Paraphrase (Primary Language)**:

The **Irma dream** is the first dream Freud analyzed in full, becoming the **prototype** for all subsequent dream interpretation. Its core meaning: **wish fulfillment** (Wunscherfüllung).

The dream's logic: Freud had been treating Irma with partial success. His friend Otto implied criticism. The dream constructs an elaborate scenario where:
1. If Irma still has pains, it's **her fault** (she didn't accept the solution)
2. Or it's **Otto's fault** (he gave her a dirty injection)
3. Or it's an **organic illness** (not psychological, therefore not Freud's domain)

In every case: **not Freud's fault**. The dream fulfills the wish to be exculpated from professional failure.

This dream demonstrates key mechanisms:
- **Condensation**: Irma = Irma + her friend + another patient
- **Displacement**: Blame moved from Freud to Otto
- **Day residue**: Otto's visit and writing the case history
- **Somatic sources**: Freud's own nasal issues (cocaine use)

**Complete Chinese Interpretation (Secondary Language)**:

**伊尔玛之梦**是弗洛伊德完整分析的第一个梦，成为所有后续梦境解释的**原型**。其核心意义：**愿望满足**（Wunscherfüllung）。

梦的逻辑：弗洛伊德治疗伊尔玛取得部分成功。他的朋友奥托暗示批评。梦构建了一个精心设计的场景：
1. 如果伊尔玛仍有疼痛，那是**她的错**（她不接受解决方案）
2. 或者是**奥托的错**（他给她打了不干净的针）
3. 或者是**器质性疾病**（不是心理的，因此不在弗洛伊德领域）

在每种情况下：**不是弗洛伊德的错**。梦满足了从职业失败中开脱的愿望。

这个梦展示了关键机制：
- **凝缩**：伊尔玛 = 伊尔玛 + 她的朋友 + 另一个患者
- **移置**：责备从弗洛伊德转移到奥托
- **日间残余**：奥托的来访和撰写病历
- **躯体来源**：弗洛伊德自己的鼻腔问题（可卡因使用）

**Narrative Snippets**:

- `[ns_freud_method_009]` `[trigger: irma_dream]` `[factor_trigger: irma_dream AND wish_fulfillment AND day_residue]` `[role: 主干]` The Dream of Irma's Injection (July 1895): Freud's specimen dream demonstrating that dreams fulfill wishes—the elaborate scenario exculpates him from professional failure. → Freud Ch.II #Irma
- `[ns_freud_method_010]` `[trigger: irma_condensation]` `[factor_trigger: irma_figure AND condensation AND manifest_content AND dream_content]` `[role: 主干依赖]` Irma in the dream = condensation of multiple women (Irma + her friend + another patient)—one manifest figure carrying multiple latent meanings. → Freud Ch.II #Irma
- `[ns_freud_method_011]` `[trigger: irma_displacement]` `[factor_trigger: dream_displacement AND dream_mechanism AND displacement]` `[role: 主干依赖]` Blame displaced from Freud to Otto—if Irma still has pains, it's Otto's dirty syringe, not Freud's incomplete treatment. → Freud Ch.II #Irma
- `[ns_freud_method_012]` `[trigger: irma_wish]` `[factor_trigger: dream_wishfulfillment AND dream_exculpation]` `[role: 总结]` The Irma dream's wish: exculpation from professional failure—"If you still have pains, it is really only your own fault." → Freud Ch.II #Irma"""
    normalized_text_zh: str = """"""
    subject: str = "1 The Dream Narrative"
    factor_refs: list = ['specimen_dream', 'wish_fulfillment', 'condensation', 'displacement', 'exculpation']
    
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
        l1_anchor="iod_v1.0.0_1_the_dream_narrative_001_L1",
    )
    version: str = "1.0.0"
