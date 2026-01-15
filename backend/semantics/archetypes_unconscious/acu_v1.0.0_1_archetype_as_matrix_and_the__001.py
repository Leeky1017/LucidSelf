"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.491642
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
    semantic_id="acu_v1.0.0_1_archetype_as_matrix_and_the__001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 1ArchetypeAsMatrixAndThe(SemanticEntry):
    """
    **Source Text** (¶187-190, Lines 3022-3139):

> [187] All statements of mythology and observed effec...
    """
    
    original_text: str = """**Source Text** (¶187-190, Lines 3022-3139):

> [187] All statements of mythology and observed effects of the mother-complex point to the unconscious as their place of origin. How else could man divide the cosmos into bright day-world and dark night-world unless he had the prototype in himself, in the polarity between conscious and unconscious?
>
> [188] The carrier of the archetype is first the personal mother, because the child lives in complete participation with her, in unconscious identity. As the distance increases, grandmother becomes "Great Mother"—wisdom and witch.
>
> [189] As distance between conscious and unconscious increases, opposites contained in the image split apart: good fairy and wicked fairy, benevolent goddess and malevolent. In the West, the morally ambiguous Yahweh became exclusively good God; everything evil united in the devil.
>
> [190] Western man has sunk so low that he must deny the divinity itself, so that after swallowing evil, he may possess the good as well. Nietzsche described with passion the "Superman" for whom God is dead—burst asunder trying to imprison the divine paradox within mortal man.

**English Paraphrase**:
- Mythology and mother-complex point to unconscious as origin
- Day-world/night-world = conscious/unconscious polarity in man
- Personal mother → grandmother → Great Mother (as archetype recedes)
- West split God into good (God) and evil (devil)
- Man swallowed evil → tries to possess good → becomes devil himself
- Nietzsche's Superman = tried to imprison divine paradox → burst asunder

**中文诠释**:
- 神话和母亲情结指向无意识为起源
- 白昼世界/黑夜世界 = 人内意识/无意识极性
- 个人母亲 → 祖母 → 大母神（原型退却时）
- 西方分裂上帝为善（上帝）和恶（魔鬼）
- 人吞噬恶 → 试图拥有善 → 自己成为魔鬼
- 尼采的超人 = 试图囚禁神圣悖论 → 自身崩裂

**Narrative Snippets**:
- `[ns_cw9i_III_187]` `[trigger: cosmos_division]` `[factor_trigger: jung_unconscious AND jung_polarity]` `[role: 主干]` Mythology and mother-complex point to unconscious—man's cosmos division reflects conscious/unconscious polarity. → ¶187
- `[ns_cw9i_III_189]` `[trigger: god_split]` `[factor_trigger: jung_god AND jung_shadow]` `[role: 主干依赖]` West split God: Yahweh → exclusively good God; evil → devil. Man swallowed evil, became carrier of mysterium iniquitatis. → ¶189
- `[ns_cw9i_III_190]` `[trigger: superman_paradox]` `[factor_trigger: jung_inflation AND jung_god]` `[role: 条件分支]` Nietzsche's Superman tried to imprison divine paradox in mortal man—burst asunder. → ¶190"""
    normalized_text_zh: str = """"""
    subject: str = "1 Archetype as Matrix and the Devil Problem (¶187-190)"
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
        l1_anchor="acu_v1.0.0_1_archetype_as_matrix_and_the__001_L1",
    )
    version: str = "1.0.0"
