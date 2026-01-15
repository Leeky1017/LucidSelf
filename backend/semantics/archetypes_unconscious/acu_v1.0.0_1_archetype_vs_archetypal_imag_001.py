"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.515278
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
    semantic_id="acu_v1.0.0_1_archetype_vs_archetypal_imag_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 1ArchetypeVsArchetypalImag(SemanticEntry):
    """
    **Source Text** (¶6-7, Lines 418-430):

> [6] Another well-known expression of the archetypes is myt...
    """
    
    original_text: str = """**Source Text** (¶6-7, Lines 418-430):

> [6] Another well-known expression of the archetypes is myth and fairytale. But here too we are dealing with forms that have received a specific stamp and have been handed down through long periods of time. The term "archetype" thus applies only indirectly to the "représentations collectives," since it designates only those psychic contents which have not yet been submitted to conscious elaboration and are therefore an immediate datum of psychic experience. In this sense there is a considerable difference between the archetype and the historical formula that has evolved. Especially on the higher levels of esoteric teaching the archetypes appear in a form that reveals quite unmistakably the critical and evaluating influence of conscious elaboration. Their immediate manifestation, as we encounter it in dreams and visions, is much more individual, less understandable, and more naïve than in myths, for example. The archetype is essentially an unconscious content that is altered by becoming conscious and by being perceived, and it takes its colour from the individual consciousness in which it happens to appear.
>
> [7] What the word "archetype" means in the nominal sense is clear enough, then, from its relations with myth, esoteric teaching, and fairytale. But if we try to establish what an archetype is psychologically, the matter becomes more complicated. So far mythologists have always helped themselves out with solar, lunar, meteorological, vegetal, and other ideas of the kind. The fact that myths are first and foremost psychic phenomena that reveal the nature of the soul is something they have absolutely refused to see until now.

**Key Term Analysis**:

| Term | Literal Meaning | Symbolic Significance | Contextual Usage |
|------|----------------|----------------------|------------------|
| Représentations collectives | Collective representations | Lévy-Bruhl's term for shared symbols | Myth/fairytale as elaborated archetype |
| Conscious elaboration | Mental processing | Cultural shaping of raw archetype | Transforms archetype into image |
| Immediate datum | Direct experience | Unprocessed archetypal encounter | Dreams/visions vs myths |
| Historical formula | Evolved cultural form | Myth as processed archetype | Distinguishes from raw archetype |

**English Paraphrase (Primary Language)**:

Jung makes the **crucial distinction** between archetype-as-such and archetypal manifestation:

**Archetype vs Cultural Expression**:
- Myths and fairytales express archetypes but are **not** archetypes themselves
- They are "forms that have received a specific stamp"—culturally elaborated
- The term "archetype" applies only to contents **not yet** submitted to conscious elaboration

**Key insight**: The archetype is altered by becoming conscious:
- **Raw archetype** (in dreams/visions): More individual, less understandable, more naïve
- **Elaborated archetype** (in myths/esoteric teaching): Polished by conscious processing

**Archetype's nature**: "Essentially an unconscious content that is altered by becoming conscious and by being perceived, and it takes its colour from the individual consciousness in which it happens to appear."

**Critique of mythologists**: They explain myths through solar, lunar, meteorological ideas—missing that myths are **psychic phenomena revealing the soul's nature**.

**Complete Chinese Interpretation (Secondary Language)**:

荣格做出**关键区分**——原型本身与原型显现：

**原型 vs 文化表达**：
- 神话和童话表达原型但**不是**原型本身
- 它们是"接受了特定印记的形式"——经过文化加工
- "原型"一词仅适用于**尚未**经过有意识加工的内容

**关键洞见**：原型因变得有意识而被改变：
- **原始原型**（在梦境/幻象中）：更个人、更难理解、更天真
- **加工原型**（在神话/密传中）：经有意识处理打磨

**原型的本质**："本质上是无意识内容，因变得有意识和被感知而改变，并从它碰巧出现的个体意识中获取色彩。"

**对神话学家的批评**：他们用太阳、月亮、气象理念解释神话——忽略了神话是**揭示灵魂本质的心理现象**。

**Core Points**:
- Archetype ≠ myth/fairytale (the latter are culturally elaborated forms)
- Archetype is altered by becoming conscious
- Raw archetypal experience (dreams) differs from elaborated form (myths)
- Archetype takes color from individual consciousness
- Myths are primarily psychic phenomena, not nature allegories
- Mythologists miss the psychological dimension of myths

**Narrative Snippets**:
- `[ns_cw9i_007]` `[trigger: archetype_vs_myth]` `[factor_trigger: anima AND anima_dark]` `[role: 主干]` Myth and fairytale express archetypes but are forms that have received a specific stamp—the archetype itself is prior to conscious elaboration. → ¶6
- `[ns_cw9i_008]` `[trigger: archetype_alteration]` `[factor_trigger: anima_light AND anima_relationship]` `[role: 主干依赖]` The archetype is essentially an unconscious content that is altered by becoming conscious and takes its colour from the individual consciousness. → ¶6
- `[ns_cw9i_009]` `[trigger: myth_as_psyche]` `[factor_trigger: anima_loss_postmidlife AND atheism]` `[role: 条件分支]` Myths are first and foremost psychic phenomena that reveal the nature of the soul—not solar, lunar, or meteorological allegories. → ¶7

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: This distinction between archetype-as-such and archetypal image became increasingly important in Jung's later work. Critics note tension between archetype as "irrepresentable" and Jung's detailed descriptions. The Lévy-Bruhl reference ("représentations collectives") shows Jung's engagement with anthropology.
- **中文**: 原型本身与原型意象的区分在荣格后期作品中变得越来越重要。批评者注意到原型作为"不可表征的"与荣格详细描述之间的张力。Lévy-Bruhl引用表明荣格与人类学的对话。"""
    normalized_text_zh: str = """"""
    subject: str = "1 Archetype vs Archetypal Image (¶6-7)"
    factor_refs: list = ['engine_id', 'conscious_elaboration', 'psych_semantic', 'archetypal_image', 'psych_semantic', 'archetype_image_distinction', 'psych_semantic', 'source_ref', 'rel_cw9i_006', 'archetype', 'manifesting', 'rel_cw9i_007', 'archetype', 'expressing', 'evi_cw9i_005', 'rule_archetype_alteration', 'evi_cw9i_006', 'myth', 'rule_myth_psyche', 'concept_raw_vs_elaborated', 'natal_vs_progressed', 'archetype_vs_image']
    
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
        book_id="archetypes_unconscious",
        chapter="",
        l1_anchor="acu_v1.0.0_1_archetype_vs_archetypal_imag_001_L1",
    )
    version: str = "1.0.0"
