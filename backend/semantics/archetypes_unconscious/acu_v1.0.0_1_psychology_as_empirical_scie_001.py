"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.568588
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
    semantic_id="acu_v1.0.0_1_psychology_as_empirical_scie_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 1PsychologyAsEmpiricalScie(SemanticEntry):
    """
    **Source Text** (¶111-113, Lines 1836-1885):

> [111] Although modern man appears to believe that th...
    """
    
    original_text: str = """**Source Text** (¶111-113, Lines 1836-1885):

> [111] Although modern man appears to believe that the non-empirical approach to psychology is a thing of the past, his general attitude remains very much the same as it was before... In academic circles, a drastic revolution in methodology, initiated by Fechner and Wundt, was needed in order to make clear to the scientific world that psychology was a field of experience and not a philosophical theory.
>
> [112] Even Freud, whose empirical attitude is beyond doubt, coupled his theory as a sine qua non with his method, as if psychic phenomena had to be viewed in a certain light in order to mean something... But the ground he cleared extended only so far as certain basic physiological concepts permitted.
>
> [113] Medical psychology has recognized that the salient facts are extraordinarily complex and can be grasped only through descriptions based on case material. But this method presupposes freedom from theoretical prejudice... The psyche does not come to an end where some physiological assumption or other stops. In each individual case we observe scientifically, we have to consider the manifestations of the psyche in their totality.

**Key Term Analysis**:

| Term | Literal Meaning | Symbolic Significance | Contextual Usage |
|------|----------------|----------------------|------------------|
| Empirical approach | Experience-based | Scientific method | Against philosophy |
| Fechner-Wundt revolution | Experimental turn | Psychology as science | Historical context |
| Theoretical prejudice | Pre-conception | Limits observation | Must avoid |
| Psyche's totality | Whole psyche | Complete picture | Not just physiology |

**English Paraphrase (Primary Language)**:

**Psychology as empirical science**:
Modern psychology required a "drastic revolution" by Fechner and Wundt to establish it as a **field of experience** rather than philosophical theory. Yet theory still plays too great a role—even Freud coupled his theory as **sine qua non** with his method.

**Limits of physiological reduction**:
Freud cleared ground only so far as physiological concepts permitted—psychology looked like an "offshoot of the physiology of the instincts." This gave an excuse to not bother with the **wider world** of psychic phenomena.

**Need for totality**:
Complex psychic facts can only be grasped through **descriptions based on case material**—presupposing freedom from theoretical prejudice. The psyche does not end where physiological assumptions stop. In each case, we must consider psychic manifestations **in their totality**.

**Complete Chinese Interpretation (Secondary Language)**:

**心理学作为经验科学**：
现代心理学需要费希纳和冯特的"彻底革命"才能确立为**经验领域**而非哲学理论。然而理论仍然作用太大——即使弗洛伊德也将其理论作为**必要条件**与方法结合。

**生理还原的局限**：
弗洛伊德只在生理概念允许的范围内开辟领域——心理学看起来像"本能生理学的分支"。这给了人们不关注心理现象**更广阔世界**的借口。

**对整体性的需要**：
复杂的心理事实只能通过**基于案例材料的描述**来把握——预设免于理论偏见。心灵不会在生理假设停止的地方结束。在每个案例中，我们必须考虑心理表现的**整体性**。

**Core Points**:
- Fechner-Wundt revolution: psychology as empirical, not philosophical
- Even Freud limited by physiological concepts
- Medical psychology needs case-based description
- Must avoid theoretical prejudice
- Psyche doesn't end where physiology stops
- Consider psychic manifestations in totality

**Narrative Snippets**:
- `[ns_cw9i_II_013]` `[trigger: psychology_empirical]` `[factor_trigger: jung_methodology AND empirical_method AND jung_depth_psychology AND jung_jung_empirical_method AND jung_valid_knowledge]` `[role: 主干]` A drastic revolution by Fechner and Wundt was needed to show that psychology was a field of experience, not philosophical theory. → ¶111
- `[ns_cw9i_II_014]` `[trigger: freud_limits]` `[factor_trigger: jung_methodology AND anti_reductionism]` `[role: 条件分支]` Freud cleared ground only so far as physiological concepts permitted—psychology looked like an offshoot of physiology. → ¶112
- `[ns_cw9i_II_015]` `[trigger: psyche_totality]` `[factor_trigger: jung_psyche AND psyche_totality AND jung_psyche_totality AND jung_jung_reductionism AND jung_incomplete_view]` `[role: 总结]` The psyche does not end where physiological assumption stops—we must consider manifestations in their totality. → ¶113"""
    normalized_text_zh: str = """"""
    subject: str = "1 Psychology as Empirical Science (¶111-113)"
    factor_refs: list = ['engine_id', 'empirical_method', 'psych_semantic', 'anti_reductionism', 'psych_semantic', 'psyche_totality', 'psych_semantic', 'source_ref', 'causal', 'jung_valid_knowledge', 'inhibitory', 'jung_incomplete_view', 'l1_anchor', 'confidence', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'jung', 'astro', 'analogous', 'jung', 'tarot', 'analogous']
    
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
        l1_anchor="acu_v1.0.0_1_psychology_as_empirical_scie_001_L1",
    )
    version: str = "1.0.0"
