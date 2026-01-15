"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.182382
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
    semantic_id="tb_v1.0.0_proem__two_preliminary_studies_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class ProemTwoPreliminaryStudies(SemanticEntry):
    """
    **Source Text** (Lines 971-1006):
> The studies preliminary to astronomical prognostication, O Syrus...
    """
    
    original_text: str = """**Source Text** (Lines 971-1006):
> The studies preliminary to astronomical prognostication, O Syrus! are two: the one, first alike in order and in power, leads to the knowledge of the figurations of the Sun, the Moon, and the stars; and of their relative aspects to each other, and to the earth: the other takes into consideration the changes which their aspects create, by means of their natural properties, in objects under their influence. The first mentioned study has been already explained in the Syntaxis to the utmost practicable extent; for it is complete in itself, and of essential utility even without being blended with the second; to which this treatise will be devoted, and which is not equally self-complete. The present work shall, however, be regulated by that due regard for truth which philosophy demands: and since the material quality of the objects acted upon renders them weak and variable, and difficult to be accurately apprehended, no positive or infallible rules can be here set forth.

**Key Term Analysis**:
- **Astronomical prognostication**: προγνωστική - predictive science based on celestial observations, distinct from mere fortune-telling
- **Figurations**: σχηματισμοί - geometric configurations/aspects between celestial bodies
- **Natural properties**: φυσικαί δυνάμεις - inherent physical qualities (hot/cold, moist/dry) causing effects
- **Syntaxis**: The Almagest, Ptolemy's mathematical astronomy treatise
- **The Ambient**: περιέχον - the surrounding celestial environment affecting all earthly things

**English Paraphrase (Primary Language)**:
Ptolemy establishes a rigorous two-tier epistemological framework distinguishing **astronomy** (mathematical celestial science) from **astrology** (interpretive application). The first study—astronomy—is "first alike in order and in power," meaning it is both logically prior and more certain. Astronomy calculates precise planetary positions, aspects, and configurations through mathematical demonstration; it was already fully treated in the *Almagest*. The second study—astrology or "astronomical prognostication"—examines how these configurations produce changes in terrestrial life through the planets' **natural properties**.

Crucially, Ptolemy acknowledges astrology's inherent limitations: because material things are "weak and variable," no **infallible rules** can be established. This epistemic humility distinguishes Ptolemy's scientific astrology from dogmatic fortune-telling. He grounds astrology in Aristotelian natural philosophy—planets influence Earth through physical causation (heat, cold, moisture, dryness), not divine will or magical sympathy. The framework is naturalistic and mechanistic, positioning astrology as a branch of physics rather than religion.

**Complete Chinese Interpretation (Secondary Language)**:
托勒密在开篇即建立了严格的双层认识论框架，明确区分**天文学**（数学天体科学）与**占星学**（解释性应用）。第一门学问——天文学——"在次序和力量上都是第一位的"，意即它在逻辑上优先且更为确定。天文学通过数学证明计算精确的行星位置、相位和配置；这在《天文学大成》（Almagest）中已有完整论述。第二门学问——占星学或"天文预测"——研究这些配置如何通过行星的**自然属性**在地上生命中产生变化。

关键地，托勒密承认占星学的内在局限：由于物质事物"脆弱易变"，不可能建立**绝对可靠的规则**。这种认识论上的谦逊将托勒密的科学占星学与教条式算命区分开来。他将占星学奠基于亚里士多德自然哲学——行星通过物理因果（热、冷、湿、干）影响地球，而非神意或魔法感应。这一框架是自然主义和机械论的，将占星学定位为物理学的分支而非宗教。

**Core Points**:
- Two distinct disciplines: Astronomy (mathematical) and Astrology (interpretive)
- Astronomy is prior in order (logical sequence) and power (certainty)
- Astronomy = demonstrative science; Astrology = conjectural art
- Planets influence through natural properties, not divine intervention
- No infallible rules possible due to material variability
- Astrology depends on astronomy but is not self-complete
- Naturalistic framework: physical causation, not magical sympathy
- Epistemic humility distinguishes scientific from dogmatic astrology

**Detailed Explanation**:
This proem is foundational for understanding Ptolemy's entire astrological system. By explicitly subordinating astrology to astronomy, he accomplishes several rhetorical and philosophical goals: (1) legitimates astrology by connecting it to respected mathematical science; (2) maintains epistemic humility about astrology's conjectural nature; (3) establishes proper methodology—precise calculation first, cautious interpretation second; (4) grounds the system in Aristotelian physics rather than Platonic mysticism or religious revelation.

The phrase "natural properties" (φυσικαί δυνάμεις) is philosophically crucial. Ptolemy explicitly adopts a naturalistic causation model: planets possess inherent elemental qualities (hot/cold, moist/dry) that mechanistically affect sublunary matter through the medium of the atmosphere (the Ambient). This distinguishes his approach from magical or theurgical astrology that relied on divine intervention or occult sympathies.

**Narrative Snippets**:
- `[ns_tetra_i001]` `[trigger: two_studies_foundation]` `[factor_trigger: astro_astro_astronomy AND astro_astrology AND astro_prognostication]` `[role: 主干]` Two studies are preliminary to astronomical prognostication: astronomy (celestial positions) and astrology (their effects). → Source Text I.1
- `[ns_tetra_i002]` `[trigger: astronomy_priority]` `[factor_trigger: astro_absolute_certainty AND astro_conjecture AND astro_astro_conjecture]` `[role: 主干依赖]` The first study is first alike in order and in power—astronomy provides the mathematical foundation. → Source Text I.1
- `[ns_tetra_i003]` `[trigger: natural_properties]` `[factor_trigger: astro_material_variability AND astro_native_constitution]` `[role: 主干]` Planets create changes through their natural properties, not divine will or magical sympathy. → Source Text I.1
- `[ns_tetra_i004]` `[trigger: no_infallible_rules]` `[factor_trigger: astro_astro_ambient AND astro_terrestrial_effect AND ambient_configuration]` `[role: 条件分支]` No positive or infallible rules can be set forth due to the material quality of objects acted upon. → Source Text I.1
- `[ns_tetra_i005]` `[trigger: conjectural_nature]` `[factor_trigger: astro_astro_moisture AND astro_seasonal_variation]` `[role: 总结]` Astrology is conjectural because the causal chain has many stages, each introducing variability. → English Paraphrase

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: The Greek original uses προγνωστική (prognostikē) rather than ἀστρολογία, emphasizing prediction over symbolism. Ashmand's translation "astronomical prognostication" preserves this technical distinction. The Syntaxis reference confirms Ptolemy authored both works.
- **中文**: 希腊原文使用προγνωστική（预测科学）而非ἀστρολογία（占星学），强调预测而非象征。Ashmand的翻译"astronomical prognostication"保留了这一技术区分。对《大成》的引用确认托勒密是两部著作的作者。"""
    normalized_text_zh: str = """"""
    subject: str = "Proem: Two Preliminary Studies (Chapter I)"
    factor_refs: list = ['astro_prognostication', 'planet_quality', 'ambient_configuration']
    
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
        book_id="tetrabiblos",
        chapter="",
        l1_anchor="tb_v1.0.0_proem__two_preliminary_studies_001_L1",
    )
    version: str = "1.0.0"
