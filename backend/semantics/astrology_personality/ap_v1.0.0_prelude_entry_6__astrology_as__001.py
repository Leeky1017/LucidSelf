"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237645
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
    semantic_id="ap_v1.0.0_prelude_entry_6__astrology_as__001",
    book_id="astrology_personality",
    engine_id="astro"
)
class PreludeEntry6AstrologyAs(SemanticEntry):
    """
    **Source Text** (Lines 1071-1101):
> The use made of astrology in alchemy is largely symbolical. But...
    """
    
    original_text: str = """**Source Text** (Lines 1071-1101):
> The use made of astrology in alchemy is largely symbolical. But in a sense astrology is always symbolical when properly understood. All depends upon what is meant by "symbol." Algebra is also purely symbolical, and yet algebra and higher mathematics have made possible modern science and the age of machines. Astrology is fundamentally the algebra of life. But its applications are as numerous as the types of life it co-ordinates, integrates, and to which it gives the significance of Order.
>
> The old Chaldean astrology was based on the principles of correspondences—purely symbolical principles. True, the Chaldeans did believe that planets were the bodies of gods according to whose dictates the universe was run. But this was merely an interpretation of astrological symbolism. The symbols were interpreted as gods because man's consciousness was essentially physiological and biological...
>
> As mind developed independently, especially after the sixth century B.C, as abstract thinking began to separate thought from its concrete life-foundation, the biological valuation of "practical utility" receded into the background, and the interpretation of "pure knowledge," "pure science," was given to astrology. Then it became astronomy.

**Key Term Analysis**:
- **Algebra of life**: `symbolic system` / `integrating life-types` / `giving Order significance`
- **Symbol**: `not arbitrary sign` / `effective as algebra` / `enables science`
- **Correspondence principles**: `Chaldean foundation` / `symbolic not literal` / `interpreted as gods`
- **Astronomy separation**: `after 6th century B.C.` / `pure knowledge` / `abstract from life`
- **Practical utility**: `biological valuation` / `recedes with abstraction` / `vitalistic criterion`

**English Paraphrase (Primary Language)**:
Rudhyar defines astrology's essential nature: "the algebra of life." This is not metaphor but precise description. Algebra is purely symbolic, yet enabled modern science and technology. Similarly, astrology operates through symbols that integrate and coordinate life-processes, giving them the significance of Order.

Chaldean astrology was based on correspondence principles—symbolic, not literal. The interpretation of planets as gods reflected the stage of consciousness (physiological-biological), not astrology's inherent nature. As mind developed independently after the sixth century B.C., astrology's biological-practical function receded and "pure knowledge" interpretation emerged—leading to astronomy's separation.

This is crucial: astrology's symbolic nature is its strength, not weakness. It operates at the level of formal causes (meaning, pattern, Order), not material causes (physical mechanism). The critique that astrology "isn't scientific" misunderstands its domain—just as criticizing algebra for not being chemistry would be a category error.

**Complete Chinese Interpretation (Secondary Language)**:
Rudhyar定义了占星学的本质："生命的代数"。这不是隐喻而是精确描述。代数是纯符号的，却促成了现代科学和技术。同样，占星学通过整合和协调生命过程的符号运作，赋予它们秩序的意义。

迦勒底占星学基于对应原则——象征性的，而非字面的。将行星解释为神灵反映了意识的阶段（生理-生物的），而非占星学的内在本质。随着公元前6世纪后心智的独立发展，占星学的生物-实用功能退居次要，"纯知识"解释出现——导致天文学的分离。

这是关键：占星学的符号本质是其优势，而非弱点。它在形式因（意义、模式、秩序）层面运作，而非质料因（物理机制）。批评占星学"不科学"误解了其领域——正如批评代数不是化学是范畴错误。

**Core Points**:
- Astrology = algebra of life (fundamental definition)
- Symbols are effective (algebra enabled science)
- Applications as numerous as life-types coordinated
- Chaldean astrology based on correspondence (symbolic)
- Gods-interpretation reflected consciousness stage
- 6th century: abstract thinking separated from life-foundation
- "Pure knowledge" interpretation led to astronomy
- Astrology's symbolic nature is strength not weakness
- Operates at formal cause level (meaning, Order)

**Narrative Snippets**:
- `[ns_aop_041]` `[trigger: algebra_life_definition]` `[factor_trigger: algebra AND astro_algebra_life]` `[role: 主干]` Astrology is fundamentally the algebra of life—symbolic system integrating life-types and giving significance of Order. → Source Text L1075-1077
- `[ns_aop_042]` `[trigger: symbol_effectiveness]` `[factor_trigger: astro_symbol_power AND astro_symbolic_mode]` `[role: 主干依赖]` Algebra is purely symbolical yet made possible modern science—astrology's symbolism equally effective in its domain. → Source Text L1072-1075
- `[ns_aop_043]` `[trigger: astronomy_separation]` `[factor_trigger: astro_astronomy_split AND astro_split]` `[role: 条件分支]` As abstract thinking developed, "pure knowledge" interpretation was given to astrology—then it became astronomy. → Source Text L1089-1094
- `[ns_aop_044]` `[trigger: correspondence_basis]` `[factor_trigger: astro_correspondence AND astro_correspond_op]` `[role: 总结]` Chaldean astrology based on symbolic correspondence principles—gods-interpretation reflected consciousness stage. → Source Text L1079-1087

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: "Algebra of life" becomes one of Rudhyar's signature phrases, later elaborated in the book's title concepts. The astronomy-astrology split historically occurred gradually over centuries.
- **中文**: "生命的代数"成为Rudhyar的标志性短语之一，后来在书名概念中得到详述。天文学与占星学的分离历史上是逐渐发生的。"""
    normalized_text_zh: str = """"""
    subject: str = "Prelude Entry 6: Astrology as Algebra of Life"
    factor_refs: list = ['astro_algebra_life', 'astro_correspondence_princ', 'astro_astronomy_split', 'astro_symbol_effective']
    
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
        l1_anchor="ap_v1.0.0_prelude_entry_6__astrology_as__001_L1",
    )
    version: str = "1.0.0"
