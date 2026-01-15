"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.491524
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
    semantic_id="acu_v1.0.0_2_qualities_of_the_mother_arch_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 2QualitiesOfTheMotherArch(SemanticEntry):
    """
    **Source Text** (¶158, Lines 2514-2535):

> [158] The qualities associated with it are maternal soli...
    """
    
    original_text: str = """**Source Text** (¶158, Lines 2514-2535):

> [158] The qualities associated with it are maternal solicitude and sympathy; the magic authority of the female; the wisdom and spiritual exaltation that transcend reason; any helpful instinct or impulse; all that is benign, all that cherishes and sustains, that fosters growth and fertility. The place of magic transformation and rebirth, together with the underworld and its inhabitants, are presided over by the mother. On the negative side the mother archetype may connote anything secret, hidden, dark; the abyss, the world of the dead, anything that devours, seduces, and poisons, that is terrifying and inescapable like fate. All these attributes of the mother archetype have been fully described and documented in my book Symbols of Transformation. There I formulated the ambivalence of these attributes as "the loving and the terrible mother." Perhaps the historical example of the dual nature of the mother most familiar to us is the Virgin Mary, who is not only the Lord's mother, but also, according to the medieval allegories, his cross. In India, "the loving and terrible mother" is the paradoxical Kali.

**Key Term Analysis**:

| Term | Literal Meaning | Symbolic Significance | Contextual Usage |
|------|----------------|----------------------|------------------|
| Maternal solicitude | Caring | Positive mother | Nurturing |
| Magic authority | Numinous power | Female wisdom | Transcending reason |
| Loving and terrible | Dual nature | Ambivalence | Virgin Mary, Kali |
| Transformation/rebirth | Death and renewal | Underworld connection | Initiation |

**English Paraphrase (Primary Language)**:

Jung summarizes **mother archetype qualities**:

**Positive qualities**:
- Maternal solicitude and sympathy
- "Magic authority of the female"
- Wisdom and spiritual exaltation transcending reason
- Helpful instinct/impulse
- All that cherishes, sustains, fosters growth

**Transformative function**:
- Presides over "place of magic transformation and rebirth"
- Together with underworld and its inhabitants

**Negative qualities**:
- Anything secret, hidden, dark
- Abyss, world of the dead
- Devouring, seducing, poisoning
- "Terrifying and inescapable like fate"

**The dual nature**:
- Formulated as **"the loving and the terrible mother"**
- **Virgin Mary**: Lord's mother AND jung_his cross
- **Kali**: Indian paradoxical loving-terrible mother

**Complete Chinese Interpretation (Secondary Language)**:

荣格总结**母亲原型品质**：

**正面品质**：
- 母性关怀与同情
- "女性的魔法权威"
- 超越理性的智慧与精神升华
- 有益本能/冲动
- 一切珍爱、维持、促进成长的

**转化功能**：
- 主宰"魔法转化与重生之地"
- 与冥界及其居民同在

**负面品质**：
- 一切秘密、隐藏、黑暗的
- 深渊、亡者世界
- 吞噬、诱惑、毒害
- "如命运般恐怖且不可逃避"

**双重本质**：
- 表述为**"慈爱与可怕的母亲"**
- **圣母玛利亚**：主的母亲也是他的十字架
- **卡莉**：印度矛盾的慈爱-可怕母亲

**Core Points**:
- Positive: solicitude, magic authority, wisdom, nourishment
- Mother presides over transformation, rebirth, underworld
- Negative: secret, dark, devouring, poisoning, fatal
- "Loving and terrible mother" = fundamental ambivalence
- Virgin Mary = mother AND jung_cross (medieval allegory)
- Kali = paradigmatic paradoxical mother

**Narrative Snippets**:
- `[ns_cw9i_III_009]` `[trigger: mother_qualities]` `[factor_trigger: jung_mother_archetype]` `[role: 主干]` The mother archetype's qualities: maternal solicitude, magic authority, wisdom transcending reason, and all that cherishes and sustains—but also the abyss, the world of the dead, all that devours and poisons. → ¶158
- `[ns_cw9i_III_010]` `[trigger: loving_terrible]` `[factor_trigger: jung_mother_archetype]` `[role: 主干依赖]` The loving and the terrible mother—Virgin Mary is not only the Lord's mother but also his cross; in India, Kali embodies this paradox. → ¶158"""
    normalized_text_zh: str = """"""
    subject: str = "2 Qualities of the Mother Archetype (¶158)"
    factor_refs: list = ['engine_id', 'loving_mother', 'psych_semantic', 'terrible_mother', 'psych_semantic', 'kali', 'psych_semantic', 'source_ref', 'embodies', 'mother_archetype', 'exemplifying', 'concept_loving_terrible', 'moon_benefic_vs_afflicted', 'ambivalent_mother']
    
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
        l1_anchor="acu_v1.0.0_2_qualities_of_the_mother_arch_001_L1",
    )
    version: str = "1.0.0"
