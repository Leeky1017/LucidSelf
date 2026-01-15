"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.491491
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
    semantic_id="acu_v1.0.0_3_the_crystal_analogy___155_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 3TheCrystalAnalogy155(SemanticEntry):
    """
    **Source Text** (¶155, Lines 2459-2482):

> [155] Again and again I encounter the mistaken notion th...
    """
    
    original_text: str = """**Source Text** (¶155, Lines 2459-2482):

> [155] Again and again I encounter the mistaken notion that an archetype is determined in regard to its content, in other words that it is a kind of unconscious idea (if such an expression be admissible). It is necessary to point out once more that archetypes are not determined as regards their content, but only as regards their form and then only to a very limited degree... Its form, however... might perhaps be compared to the axial system of a crystal, which, as it were, preforms the crystalline structure in the mother liquid, although it has no material existence of its own. This first appears according to the specific way in which the ions and molecules aggregate. The archetype in itself is empty and purely formal, nothing but a facultas praeformandi, a possibility of representation which is given a priori. The representations themselves are not inherited, only the forms, and in that respect they correspond in every way to the instincts, which are also determined in form only.

**Key Term Analysis**:

| Term | Literal Meaning | Symbolic Significance | Contextual Usage |
|------|----------------|----------------------|------------------|
| Axial system | Crystal structure | Archetype form | Preforming pattern |
| Mother liquid | Solution | Conscious experience | Content source |
| Facultas praeformandi | Preforming capacity | Empty pattern | Archetype nature |
| Form vs content | Structure vs substance | Inherited vs acquired | Key distinction |

**English Paraphrase (Primary Language)**:

Jung's famous **crystal analogy** for archetypes:

**Common misconception**:
- Mistake: archetype = "unconscious idea" with determined content
- Correction: archetypes determined ONLY in form, not content

**Crystal analogy**:
- Archetype = like crystal's axial system
- **Axial system preforms structure** in mother liquid
- But has **no material existence of its own**
- Visible structure appears when ions/molecules aggregate

**Key definition**:
- "Archetype in itself is empty and purely formal"
- It is **facultas praeformandi** = "preforming capacity"
- A "possibility of representation which is given a priori"
- **Representations not inherited; only forms**
- Archetypes = formal patterns like instincts

**Complete Chinese Interpretation (Secondary Language)**:

荣格著名的**晶体类比**解释原型：

**常见误解**：
- 错误：原型 = 有确定内容的"无意识观念"
- 纠正：原型仅在形式上确定，非内容

**晶体类比**：
- 原型 = 如晶体的轴系
- **轴系在母液中预成结构**
- 但**自身没有物质存在**
- 可见结构在离子/分子聚合时出现

**关键定义**：
- "原型本身是空的、纯形式的"
- 它是 **facultas praeformandi** = "预成能力"
- "先验给定的表征可能性"
- **表征不遗传；只有形式遗传**
- 原型 = 形式模式如本能

**Core Points**:
- Archetype = form only, not content
- Crystal analogy: axial system preforms but has no material existence
- Archetype is "empty and purely formal"
- Facultas praeformandi = preforming capacity
- Representations (content) not inherited; only forms
- Archetypes parallel instincts (both formal patterns)

**Narrative Snippets**:
- `[ns_cw9i_III_004]` `[trigger: archetype_form_not_content]` `[factor_trigger: jung_archetype]` `[role: 主干]` Archetypes are not determined as regards their content, but only as regards their form—they correspond in every way to instincts. → ¶155
- `[ns_cw9i_III_005]` `[trigger: crystal_analogy]` `[factor_trigger: jung_archetype]` `[role: 主干依赖]` The archetype's form might be compared to the axial system of a crystal, which preforms the structure in the mother liquid although it has no material existence of its own. → ¶155
- `[ns_cw9i_III_006]` `[trigger: facultas_praeformandi]` `[factor_trigger: jung_archetype]` `[role: 主干]` The archetype in itself is empty and purely formal, nothing but a facultas praeformandi, a possibility of representation given a priori. → ¶155"""
    normalized_text_zh: str = """"""
    subject: str = "3 The Crystal Analogy (¶155)"
    factor_refs: list = ['engine_id', 'crystal_analogy', 'psych_semantic', 'facultas_praeformandi', 'psych_semantic', 'form_content_distinction', 'psych_semantic', 'source_ref', 'illustrates', 'archetype', 'explaining', 'parallel', 'instinct', 'corresponding', 'concept_formal_pattern', 'chart_pattern', 'archetype_form']
    
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
        l1_anchor="acu_v1.0.0_3_the_crystal_analogy___155_001_L1",
    )
    version: str = "1.0.0"
