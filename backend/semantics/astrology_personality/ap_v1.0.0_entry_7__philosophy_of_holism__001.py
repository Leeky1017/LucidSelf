"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237792
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
    semantic_id="ap_v1.0.0_entry_7__philosophy_of_holism__001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry7PhilosophyOfHolism(SemanticEntry):
    """
    **Source Text** (Lines 2182-2255):
> The Philosophy of Holism... This philosophy is expounded fully ...
    """
    
    original_text: str = """**Source Text** (Lines 2182-2255):
> The Philosophy of Holism... This philosophy is expounded fully in a remarkable book, "Holism and Evolution," written in 1926 by... General Jan C. Smuts...
>
> "Holism is the theory which makes the existence of 'wholes' a fundamental feature of the world. It regards natural objects, both animate and inanimate, as wholes and not merely as assemblages of elements or parts... these bodies or things are not entirely resolvable into parts; in one degree or another they are wholes which are more than the sum of their parts, and the mechanical putting together of their parts will not produce them or account for their character and behavior.
>
> "Holism is therefore a viewpoint additional and complementary to that of science, whose keywords are continuity and mechanism...
>
> "The whole is creative; wherever parts conspire to form a whole, there something arises which is more than the parts."
>
> General Smuts explains further how... if cause is and must always necessarily be an exact measure of effect, this cannot be a creative progressive universe. Holistic causation (where several factors contribute to the making of new wholes) is the real process... In the holistic universe freedom is recognized as inherent in nature.

**Key Term Analysis**:
- **Holism**: `wholes as fundamental` / `more than sum of parts` / `not resolvable into parts`
- **Whole > parts**: `creative emergence` / `mechanical assembly doesn't produce` / `parts are abstractions`
- **Holistic vs mechanical causation**: `effect ≠ cause` / `creative progress` / `freedom inherent`
- **Evolution as rising wholes**: `complexifying parts` / `increasing unity of pattern` / `older patterns incorporated`

**English Paraphrase (Primary Language)**:
Rudhyar introduces Smuts's holism as the philosophical foundation for his astrology. Holism holds that "wholes" are fundamental features of reality—not reducible to parts. "The whole is more than the sum of its parts"—mechanical assembly cannot produce or explain wholes.

Key implications: (1) Parts are "largely abstract analytical distinctions," not fully real; (2) Mechanical causation (effect = cause) cannot account for creative evolution; (3) Holistic causation (multiple factors → emergent whole) is the real process; (4) Freedom is inherent in nature.

Evolution becomes "a rising series of wholes"—each level incorporates previous levels (chemical → biological → psychological). This provides the metaphysical ground for astrology: the birth-chart describes a whole person, not an assemblage of separate factors.

**Complete Chinese Interpretation (Secondary Language)**:
Rudhyar将Smuts的整体论作为其占星学的哲学基础。整体论认为"整体"是现实的根本特征——不可还原为部分。"整体大于部分之和"——机械组装无法产生或解释整体。

关键含义：(1)部分"主要是抽象的分析区分"，非完全真实；(2)机械因果（效果=原因）无法解释创造性演化；(3)整体因果（多因素→涌现整体）是真实过程；(4)自由内在于自然。

演化成为"整体的上升序列"——每一层级纳入先前层级（化学→生物→心理）。这为占星学提供了形而上学基础：出生图描述一个完整的人，而非独立因素的集合。

**Core Points**:
- Holism: wholes as fundamental reality feature
- Whole > sum of parts—mechanical assembly fails
- Parts are abstract analytical distinctions
- Mechanical causation cannot explain creative evolution
- Holistic causation: multiple factors → emergent whole
- Freedom inherent in nature
- Evolution = rising series of wholes
- Provides metaphysical ground for chart interpretation

**Narrative Snippets**:
- `[ns_aop_081]` `[trigger: holism_defined]` `[factor_trigger: phil_holism AND holism]` `[role: 主干]` Holism: wholes fundamental, more than sum of parts, not resolvable into parts. → L2191-2201
- `[ns_aop_082]` `[trigger: whole_creative]` `[factor_trigger: astro_whole_creative AND astro_emergence AND astro_holism_struct]` `[role: 主干依赖]` Whole is creative—wherever parts conspire, something more than parts arises. → L2239-2244
- `[ns_aop_083]` `[trigger: holistic_causation]` `[factor_trigger: holistic_causation AND mechanical_causation]` `[role: 条件分支]` Holistic causation (multiple factors → emergent whole) is real process; freedom inherent. → L2251-2255
- `[ns_aop_084]` `[trigger: evolution_wholes]` `[factor_trigger: human_consciousness]` `[role: 总结]` Evolution = rising series of wholes; older patterns incorporated into newer. → L2226-2237"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 7: Philosophy of Holism—Smuts's Foundation"
    factor_refs: list = ['astro_holism', 'astro_whole_greater', 'astro_holistic_cause', 'astro_evol_wholes']
    
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
        l1_anchor="ap_v1.0.0_entry_7__philosophy_of_holism__001_L1",
    )
    version: str = "1.0.0"
