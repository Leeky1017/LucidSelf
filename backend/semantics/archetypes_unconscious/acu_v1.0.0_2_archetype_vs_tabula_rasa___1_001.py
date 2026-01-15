"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.568709
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
    semantic_id="acu_v1.0.0_2_archetype_vs_tabula_rasa___1_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 2ArchetypeVsTabulaRasa1(SemanticEntry):
    """
    **Source Text** (¶136-137, Lines 2171-2196):

> [136] It is in my view a great mistake to suppose th...
    """
    
    original_text: str = """**Source Text** (¶136-137, Lines 2171-2196):

> [136] It is in my view a great mistake to suppose that the psyche of a new-born child is a tabula rasa in the sense that there is absolutely nothing in it. In so far as the child is born with a differentiated brain that is predetermined by heredity and therefore individualized, it meets sensory stimuli coming from outside not with any aptitudes, but with specific ones, and this necessarily results in a particular, individual choice and pattern of apperception. These aptitudes can be shown to be inherited instincts and preformed patterns, the latter being the a priori and formal conditions of apperception that are based on instinct. Their presence gives the world of the child and the dreamer its anthropomorphic stamp. They are the archetypes...
>
> [137] Just as the archetypes occur on the ethnological level as myths, so also they are found in every individual, and their effect is always strongest, that is, they anthropomorphize reality most, where consciousness is weakest and most restricted, and where fantasy can overrun the facts of the outer world.

**Key Term Analysis**:

| Term | Literal Meaning | Symbolic Significance | Contextual Usage |
|------|----------------|----------------------|------------------|
| Tabula rasa | Blank slate | Empty at birth | Rejected hypothesis |
| Inherited instincts | Inborn patterns | Archetypal aptitudes | Psychic heredity |
| A priori conditions | Pre-experiential | Formal patterns | Apperception structure |
| Anthropomorphize | Human-shape | Mythologize reality | Archetype effect |

**English Paraphrase (Primary Language)**:

Jung refutes **tabula rasa**:

**Against blank slate**:
- "Great mistake" to think newborn psyche has "absolutely nothing"
- Child born with differentiated brain, predetermined by heredity
- Meets stimuli with **specific aptitudes**, not blank receptivity

**Archetypes as inherited patterns**:
- Aptitudes = inherited instincts + preformed patterns
- Patterns = "a priori and formal conditions of apperception"
- They give child's/dreamer's world its "anthropomorphic stamp"
- They ARE the archetypes

**Archetype strength**:
- Strongest where consciousness is weakest
- Fantasy overruns facts when consciousness is restricted
- Child + dreamer + psychotic = high archetypal influence
- Archetypes "anthropomorphize reality"

**Complete Chinese Interpretation (Secondary Language)**:

荣格反驳**白板论**：

**反对空白板**：
- 认为新生儿心灵"完全空白"是"大错误"
- 儿童生来有分化的大脑，由遗传预定
- 以**特定天赋**迎接刺激，非空白接受

**原型作为遗传模式**：
- 天赋 = 遗传本能 + 预成模式
- 模式 = "领悟的先验和形式条件"
- 它们给儿童/梦者世界以"拟人印记"
- 它们就是原型

**原型强度**：
- 意识最弱处最强
- 意识受限时幻想压倒事实
- 儿童 + 梦者 + 精神病 = 高原型影响
- 原型"拟人化现实"

**Core Points**:
- Newborn is NOT tabula rasa—has inherited aptitudes
- Archetypes = inherited instincts + preformed patterns
- They are a priori conditions of apperception
- Archetypes anthropomorphize reality (give human shape)
- Strongest where consciousness is weakest (child, dreamer)
- Fantasy overruns facts when consciousness restricted

**Narrative Snippets**:
- `[ns_cw9i_II_011]` `[trigger: tabula_rasa_refuted]` `[factor_trigger: jung_archetype]` `[role: 主干]` It is a great mistake to suppose the newborn psyche is a tabula rasa—the child meets stimuli with specific inherited aptitudes, the archetypes. → ¶136
- `[ns_cw9i_II_012]` `[trigger: archetype_strength]` `[factor_trigger: jung_archetype]` `[role: 条件分支]` Archetypes are strongest where consciousness is weakest—they anthropomorphize reality most where fantasy can overrun facts. → ¶137"""
    normalized_text_zh: str = """"""
    subject: str = "2 Archetype vs Tabula Rasa (¶136-137)"
    factor_refs: list = ['engine_id', 'anti_tabula_rasa', 'psych_semantic', 'anthropomorphize', 'psych_semantic', 'source_ref', 'refutes', 'tabula_rasa', 'opposing', 'inverse', 'consciousness', 'inverse', 'concept_inherited_pattern', 'natal_chart', 'archetype']
    
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
        l1_anchor="acu_v1.0.0_2_archetype_vs_tabula_rasa___1_001_L1",
    )
    version: str = "1.0.0"
