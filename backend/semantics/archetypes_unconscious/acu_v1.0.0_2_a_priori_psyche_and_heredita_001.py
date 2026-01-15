"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.491475
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
    semantic_id="acu_v1.0.0_2_a_priori_psyche_and_heredita_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 2APrioriPsycheAndHeredita(SemanticEntry):
    """
    **Source Text** (¶151-154, Lines 2400-2457):

> [151] There is an a priori factor in all human activ...
    """
    
    original_text: str = """**Source Text** (¶151-154, Lines 2400-2457):

> [151] There is an a priori factor in all human activities, namely the inborn, preconscious and unconscious individual structure of the psyche. The preconscious psyche—for example, that of a new-born infant—is not an empty vessel into which anything can be poured. On the contrary, it is a tremendously complicated, sharply defined individual entity.
>
> [152] Man possesses a preformed psyche which breeds true to his species. We cannot know the nature of the preconscious psychic disposition that enables a child to react in a human manner. We can only suppose that his behaviour results from patterns of functioning—"images." These are "primordial" images, the "human quality" of the human being.
>
> [153] Since everything psychic is preformed, this must also be true of the individual functions, especially creative fantasy. In the products of fantasy the primordial images are made visible—here the concept of the archetype finds its specific application. I have shown that archetypes can rearise spontaneously, at any time, at any place, without any outside influence.
>
> [154] There are present in every psyche forms which are unconscious but nonetheless active—living dispositions, ideas in the Platonic sense, that preform and continually influence our thoughts, feelings, and actions.

**English Paraphrase**:
- A priori factor in all human activities = inborn psychic structure
- Newborn psyche = NOT empty vessel but complicated individual entity
- Man has preformed psyche breeding true to species
- Behaviour results from "images" = primordial patterns = "human quality"
- Creative fantasy = where primordial images become visible
- Archetypes can rearise spontaneously without outside influence
- Unconscious forms = living dispositions preforming thoughts/feelings/actions

**中文诠释**:
- 所有人类活动的先验因素 = 先天心理结构
- 新生儿心灵 = 非空容器而是复杂的个体实体
- 人有繁殖真实物种的预成心灵
- 行为来自"意象" = 原始模式 = "人的品质"
- 创造性幻想 = 原始意象变得可见之处
- 原型可自发重现，无需外部影响
- 无意识形式 = 预成思想/感受/行动的活性倾向

**Narrative Snippets**:
- `[ns_cw9i_III_151]` `[trigger: preconscious]` `[factor_trigger: jung_psyche AND jung_archetype]` `[role: 主干]` Preconscious psyche is NOT empty vessel—tremendously complicated individual entity. → ¶151
- `[ns_cw9i_III_152]` `[trigger: primordial_images]` `[factor_trigger: jung_archetype AND jung_behavior]` `[role: 主干依赖]` Man's behaviour results from "images"—primordial patterns, the "human quality." → ¶152
- `[ns_cw9i_III_153]` `[trigger: archetype_spontaneous]` `[factor_trigger: jung_archetype AND jung_autonomous]` `[role: 条件分支]` Archetypes can rearise spontaneously, at any time, without outside influence. → ¶153
- `[ns_cw9i_III_154]` `[trigger: unconscious_forms]` `[factor_trigger: jung_unconscious AND jung_archetype]` `[role: 总结]` Present in every psyche: unconscious but active forms—living dispositions preforming thoughts. → ¶154"""
    normalized_text_zh: str = """"""
    subject: str = "2 A Priori Psyche and Hereditary Predisposition (¶151-154)"
    factor_refs: list = []
    
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
        l1_anchor="acu_v1.0.0_2_a_priori_psyche_and_heredita_001_L1",
    )
    version: str = "1.0.0"
