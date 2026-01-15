"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.469091
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
    semantic_id="iod_v1.0.0_affect_presentation_dissociati_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class AffectPresentationDissociati(SemanticEntry):
    """
    **Source Text**:
"A profound remark of Stricker's has called our attention to the fact that the expr...
    """
    
    original_text: str = """**Source Text**:
"A profound remark of Stricker's has called our attention to the fact that the expressions of emotion in the dream do not permit of being disposed of in the slighting manner in which we are accustomed to shake off the dream itself, after we have awakened. 'If I am afraid of robbers in the dream, the robbers, to be sure, are imaginary, but the fear of them is real,' and the same is true if I am glad in the dream."

"Analysis teaches us that presentation contents have undergone displacements and substitutions, while affects have remained unchanged. No wonder, then, that the presentation content which has been altered by dream disfigurement no longer fits the affect that has remained intact."

"In a psychic complex which has been subjected to the influence of the resisting censor the affects are the unyielding constituent, which alone is capable of guiding us to a correct supplementation."

**Key Term Analysis**:

| Term | Definition | Significance |
|------|-----------|---------------|
| Affect | Emotional experience in dreams | Remains unchanged through dream-work |
| Presentation Content | Ideas/images in dreams | Subject to displacement/substitution |
| Affect-Content Dissociation | Separation of emotion from its source | Key to understanding dream emotions |
| Unyielding Constituent | Affect as stable element | Guide to interpretation |
| Incongruence | Mismatch between affect and content | Diagnostic sign |

**English Paraphrase (Primary Language)**:

Section (g) addresses a paradox: **dream emotions are real even when dream content is imaginary**. Stricker's insight: "If I am afraid of robbers in the dream, the robbers are imaginary, but the fear is real." Upon waking, we dismiss dream images but cannot easily dismiss dream feelings.

The explanation lies in **affect-presentation dissociation**. Dream-work (condensation, displacement, symbolization) transforms **presentation content** (images, ideas) but leaves **affects unchanged**. The result: emotions become "attached" to the wrong content. Intense fear about a trivial object; calm indifference to a threatening situation—these **incongruencies** reveal that the affect has been displaced from its true source.

This makes affect the **interpretive compass**: "In a psychic complex which has been subjected to the censoring influence, affects are the unyielding constituent, which alone is capable of guiding us to correct supplementation." The analyst trusts the emotion and seeks the presentation that truly belongs to it.

**Complete Chinese Interpretation (Secondary Language)**:

(g)部分探讨一个悖论：**梦中情感是真实的，即使梦境内容是虚构的**。斯特里克的洞见："如果我在梦中害怕强盗，强盗是想象的，但恐惧是真实的。"醒来后，我们可以否定梦境图像，但无法轻易否定梦境感受。

解释在于**情感-表象分离**。梦的工作（凝缩、移置、象征化）转变**表象内容**（图像、观念）但使**情感保持不变**。结果：情感变得"附着"在错误的内容上。对琐事的强烈恐惧；对威胁情境的平静漠然——这些**不协调**揭示了情感已从其真正来源被移置。

这使情感成为**释梦的指南针**："在经受审查影响的心理复合体中，情感是不可动摇的成分，唯有它能够引导我们正确地补充内容。"分析师信任情感，寻找真正属于它的表象。

**Core Points**:

- Dream emotions are real; dream images are imaginary
- Affect remains unchanged; presentation content is transformed
- Result: affect-content incongruence (wrong emotion on wrong object)
- Affect is the "unyielding constituent"—interpretation compass
- Follow the emotion to find the true latent content
- Neurotic symptoms show same pattern (misplaced affect)

**Detailed Explanation**:

This section has major **clinical implications**. Patients often report emotions that seem "irrational"—intense anxiety about trivial matters, excessive guilt about minor actions. Freud's insight: **the affect is always right; only the presentation is wrong**. The therapeutic task is not to dismiss the emotion as "irrational" but to find the hidden presentation that truly belongs to it.

The **dissociation model** (affect can be "soldered" to content and "detached" by analysis) is fundamental to psychoanalytic technique. Free association traces the emotional thread backward from its manifest attachment to its latent source.

For **dream interpretation**, this means: trust the emotional tone even when content seems random. A dream of calm terror (threatening content, no fear) signals massive displacement—the real terror source has been completely removed. A dream of inexplicable joy over mundane events points to hidden satisfactions. The **emotional residue** is the most reliable guide.

**Textual Criticism & Variant Analysis (Bilingual)**:

- **English**: "Affect" (German: Affekt) refers specifically to the experiential/felt dimension of emotion, distinct from its ideational content.
- **中文**: "情感"（德语：Affekt）专指情绪的体验/感受维度，区别于其观念内容。中文"情动"可能更精确，强调被触动的动态过程。

**Narrative Snippets**:

- `[ns_freud_dw_016]` `[trigger: affect_reality]` `[factor_trigger: dream_affect]` `[role: 主干]` If I am afraid of robbers in the dream, the robbers are imaginary, but the fear of them is real. The emotion experienced in the dream is in no way less valid than one of like intensity in waking life. → Freud Ch.VI #Affects
- `[ns_freud_dw_017]` `[trigger: affect_unchanged]` `[factor_trigger: presentation_content AND affect_dissociation]` `[role: 主干依赖]` Presentation contents have undergone displacements and substitutions, while affects have remained unchanged—no wonder the altered content no longer fits the intact affect. → Freud Ch.VI #Affects
- `[ns_freud_dw_018]` `[trigger: affect_guide]` `[factor_trigger: incongruence AND dream_affect]` `[role: 条件分支]` In a psychic complex subjected to censorship, affects are the unyielding constituent, which alone is capable of guiding us to correct supplementation of the latent content. → Freud Ch.VI #Affects"""
    normalized_text_zh: str = """"""
    subject: str = "Affect-Presentation Dissociation"
    factor_refs: list = ['dream_affect', 'presentation_content', 'affect_dissociation', 'incongruence']
    
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
        l1_anchor="iod_v1.0.0_affect_presentation_dissociati_001_L1",
    )
    version: str = "1.0.0"
