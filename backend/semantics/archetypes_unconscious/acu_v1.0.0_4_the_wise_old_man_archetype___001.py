"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.515512
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
    semantic_id="acu_v1.0.0_4_the_wise_old_man_archetype___001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 4TheWiseOldManArchetype(SemanticEntry):
    """
    **Source Text** (¶74, Lines 1316-1328):

> [74] The two magicians are, indeed, two aspects of the wi...
    """
    
    original_text: str = """**Source Text** (¶74, Lines 1316-1328):

> [74] The two magicians are, indeed, two aspects of the wise old man, the superior master and teacher, the archetype of the spirit, who symbolizes the pre-existent meaning hidden in the chaos of life. He is the father of the soul, and yet the soul, in some miraculous manner, is also his virgin mother, for which reason he was called by the alchemists the "first son of the mother." The black magician and the black horse correspond to the descent into darkness in the dreams mentioned earlier.

**Key Term Analysis**:

| Term | Literal Meaning | Symbolic Significance | Contextual Usage |
|------|----------------|----------------------|------------------|
| Wise Old Man | Elder sage | Archetype of spirit | Meaning-giver |
| Two magicians | White and black | Dual aspects of spirit | Good/evil unity |
| Father of soul | Origin | Source of meaning | Spirit as father |
| First son of mother | Alchemical term | Paradox of spirit-soul | Self-generating |

**English Paraphrase (Primary Language)**:

Jung introduces the **Wise Old Man archetype**:

**Nature**:
- "Superior master and teacher"
- "Archetype of the spirit"
- Symbolizes "pre-existent meaning hidden in the chaos of life"

**Dual aspects** (from dream of white/black magicians):
- White magician and black magician = two aspects of same archetype
- Spirit has both light and dark sides
- Black magician found the keys to paradise

**Paradox**:
- Wise Old Man is "father of the soul"
- Yet soul is "also his virgin mother"
- Alchemists called him "first son of the mother"
- Self-generating, self-referential principle

**Complete Chinese Interpretation (Secondary Language)**:

荣格引入**智慧老人原型**：

**本质**：
- "卓越的主人和老师"
- "精神的原型"
- 象征"隐藏在生命混沌中的先存意义"

**双重面向**（来自白/黑魔法师之梦）：
- 白魔法师与黑魔法师 = 同一原型的两面
- 精神有光明与黑暗两面
- 黑魔法师找到了天堂的钥匙

**悖论**：
- 智慧老人是"灵魂之父"
- 然而灵魂"也是他的处女母亲"
- 炼金术士称他为"母亲的第一个儿子"
- 自生、自指原则

**Core Points**:
- Wise Old Man = archetype of spirit, meaning, guidance
- Has dual aspects (light and dark)
- "Pre-existent meaning hidden in chaos"
- Paradoxical: father of soul yet soul's son
- Alchemical term: "first son of the mother"
- Represents hidden wisdom that can be accessed

**Narrative Snippets**:
- `[ns_cw9i_023]` `[trigger: wise_old_man]` `[factor_trigger: jung_wise_old_man]` `[role: 主干]` The wise old man is the superior master and teacher, the archetype of the spirit, symbolizing the pre-existent meaning hidden in the chaos of life. → ¶74
- `[ns_cw9i_024]` `[trigger: spirit_dual]` `[factor_trigger: jung_wise_old_man]` `[role: 条件分支]` The two magicians (white and black) are two aspects of the wise old man—spirit has light and dark sides. → ¶74"""
    normalized_text_zh: str = """"""
    subject: str = "4 The Wise Old Man Archetype (¶74)"
    factor_refs: list = ['engine_id', 'wise_old_man', 'psych_semantic', 'preexistent_meaning', 'psych_semantic', 'source_ref', 'rel_cw9i_018', 'jung_wise_old_man', 'manifesting', 'rel_cw9i_019', 'wise_old_man_light', 'complementary', 'concept_wise_old_man', 'wise_elder_dream']
    
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
        l1_anchor="acu_v1.0.0_4_the_wise_old_man_archetype___001_L1",
    )
    version: str = "1.0.0"
