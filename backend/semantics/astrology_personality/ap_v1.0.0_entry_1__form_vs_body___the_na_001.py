"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238274
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
    semantic_id="ap_v1.0.0_entry_1__form_vs_body___the_na_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry1FormVsBodyTheNa(SemanticEntry):
    """
    **Source Text** (Lines 12413-12471):
> Form is, generally speaking, the element of being which defin...
    """
    
    original_text: str = """**Source Text** (Lines 12413-12471):
> Form is, generally speaking, the element of being which defines the particular out of the universal... Form is an abstraction. To speak of form as a tangible reality is to misuse the term and to confuse it with "body."...
>
> Body is unsubstantiated form and incorporated substance. Form, in itself, has no substantial implications... Body is an agglomeration of substantial elements (atoms, molecules, etc.) which is made relatively permanent and significant by the fact that it has form.
>
> Thus we have the basic trinity: energy, form, substance, synthetized by the fourth term: personality.

**Key Term Analysis**:
- **Form**: `abstraction` / `blueprint` / `pattern of relationships` / `defines particular from universal`
- **Body**: `substantiated form` / `incorporated substance` / `tangible`
- **Idea vs Concept**: `idea = vital + energy` / `concept = purely intellectual`
- **Basic trinity**: `energy, form, substance` + `personality (fourth term)`

**English Paraphrase (Primary Language)**:
Form = "abstraction," the "blueprint" defining particular from universal. NOT tangible (that's body).

Body = "substantiated form and incorporated substance"—atoms given structure by form.

Idea = form + energy (vital seed). Concept = form without energy (algebraic formula).

"Basic trinity: energy, form, substance, synthetized by the fourth term: personality."

**Complete Chinese Interpretation (Secondary Language)**:
形式 = "抽象"，定义特殊与普遍的"蓝图"。不是有形的（那是身体）。

身体 = "实体化的形式和结合的物质"——通过形式获得结构的原子。

理念 = 形式 + 能量（生命种子）。概念 = 没有能量的形式（代数公式）。

"基本三位一体：能量、形式、物质，由第四个术语综合：人格。"

**Narrative Snippets**:
- `[ns_aop_199]` `[trigger: form_definition]` `[factor_trigger: astro_form_nature]` `[role: 主干]` Form = abstraction, blueprint; Body = substantiated form. Idea = form + energy. → L12413-12462
- `[ns_aop_200]` `[trigger: basic_trinity]` `[factor_trigger: astro_trinity_terms]` `[role: 总结]` Basic trinity: energy, form, substance; synthesized by personality (fourth term). → L12464-12471"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 1: Form vs Body - The Nature of Form"
    factor_refs: list = ['form_abstract', 'body_substance', 'trinity_basic']
    
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
        l1_anchor="ap_v1.0.0_entry_1__form_vs_body___the_na_001_L1",
    )
    version: str = "1.0.0"
