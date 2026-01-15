"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.515245
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
    semantic_id="acu_v1.0.0_2_archetype_as_content_of_coll_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 2ArchetypeAsContentOfColl(SemanticEntry):
    """
    **Source Text** (¶4-5, Lines 389-416):

> [4] Psychic existence can be recognized only by the presen...
    """
    
    original_text: str = """**Source Text** (¶4-5, Lines 389-416):

> [4] Psychic existence can be recognized only by the presence of contents that are capable of consciousness. We can therefore speak of an unconscious only in so far as we are able to demonstrate its contents. The contents of the personal unconscious are chiefly the feeling-toned complexes, as they are called; they constitute the personal and private side of psychic life. The contents of the collective unconscious, on the other hand, are known as archetypes.
>
> [5] The term "archetype" occurs as early as Philo Judaeus, with reference to the Imago Dei (God-image) in man. It can also be found in Irenaeus, who says: "The creator of the world did not fashion these things directly from himself but copied them from archetypes outside himself." In the Corpus Hermeticum, God is called τò άρχέτυπov φώς (archetypal light). The term occurs several times in Dionysius the Areopagite... "Archetype" is an explanatory paraphrase of the Platonic εἶδος. For our purposes this term is apposite and helpful, because it tells us that so far as the collective unconscious contents are concerned we are dealing with archaic or—I would say—primordial types, that is, with universal images that have existed since the remotest times.

**Key Term Analysis**:

| Term | Literal Meaning | Symbolic Significance | Contextual Usage |
|------|----------------|----------------------|------------------|
| Archetype | Original pattern/type | Universal inherited form | Contents of collective unconscious |
| Feeling-toned complex | Emotionally charged cluster | Personal psychological knot | Contents of personal unconscious |
| Imago Dei | Image of God | Divine template in human | Philo's usage of archetype |
| Primordial types | Original/ancient forms | Universal images from remotest times | Jung's definition |

**English Paraphrase (Primary Language)**:

Jung establishes the **archetype** as the content of the collective unconscious:

**Epistemological foundation**: We can only speak of unconscious contents we can demonstrate. The unconscious manifests through its contents becoming conscious.

**Two types of unconscious contents**:
1. **Personal unconscious contents** = feeling-toned complexes (personal, private, biographical)
2. **Collective unconscious contents** = archetypes (universal, inherited, primordial)

**Etymology of "archetype"**:
- **Philo Judaeus**: Imago Dei (God-image in man)
- **Irenaeus**: Creator copied from "archetypes outside himself"
- **Corpus Hermeticum**: God = "archetypal light" (τò άρχέτυπov φώς)
- **Dionysius the Areopagite**: "immaterial Archetypes"
- **Platonic connection**: Archetype = paraphrase of Platonic εἶδος (Form/Idea)

**Definition**: Archetypes = **primordial types**, universal images existing since remotest times. They are archaic patterns, not specific images.

**Complete Chinese Interpretation (Secondary Language)**:

荣格确立**原型**为集体无意识的内容：

**认识论基础**：我们只能谈论可以证明的无意识内容。无意识通过其内容变得有意识而显现。

**两种无意识内容**：
1. **个人无意识内容** = 情结（个人的、私人的、传记性的）
2. **集体无意识内容** = 原型（普遍的、遗传的、原始的）

**"原型"词源**：
- **斐洛·犹大斯**：上帝意象（人内的神之像）
- **爱任纽**：造物主从"自身之外的原型"复制
- **赫尔墨斯文集**：上帝 = "原型之光"
- **狄奥尼修斯·亚略巴古**："非物质原型"
- **柏拉图联系**：原型 = 柏拉图εἶδος（形式/理念）的解释性释义

**定义**：原型 = **原始类型**，自远古以来存在的普遍意象。它们是古老模式，非具体意象。

**Core Points**:
- Archetypes are the specific contents of the collective unconscious
- Personal unconscious contains complexes; collective unconscious contains archetypes
- "Archetype" has ancient philosophical lineage (Philo, Irenaeus, Hermetica, Dionysius)
- Archetype is related to Platonic Forms (εἶδος)
- Archetypes are primordial types—universal images from remotest times
- They are archaic patterns, not specific cultural images

**Narrative Snippets**:
- `[ns_cw9i_004]` `[trigger: archetype_definition]` `[factor_trigger: archetype_energy AND archetype_strength]` `[role: 主干]` The contents of the collective unconscious are known as archetypes—primordial types, universal images that have existed since the remotest times. → ¶4-5
- `[ns_cw9i_005]` `[trigger: complex_vs_archetype]` `[factor_trigger: archetype_consciousness AND archetype_loss]` `[role: 条件分支]` Personal unconscious contains feeling-toned complexes; collective unconscious contains archetypes. → ¶4
- `[ns_cw9i_006]` `[trigger: archetype_etymology]` `[factor_trigger: archetype_reconnection AND apriori_factor]` `[role: 主干依赖]` "Archetype" occurs in Philo (Imago Dei), Irenaeus, Corpus Hermeticum—it is a paraphrase of the Platonic εἶδος. → ¶5

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: Jung deliberately chose "archetype" over alternatives like "primordial image" to emphasize the Platonic connection. The Greek citations demonstrate Jung's classical education and establish psychological concepts within Western philosophical tradition.
- **中文**: 荣格刻意选择"原型"而非"原始意象"等替代词以强调柏拉图联系。希腊语引用展示了荣格的古典教育，并将心理学概念置于西方哲学传统中。"""
    normalized_text_zh: str = """"""
    subject: str = "2 Archetype as Content of Collective Unconscious (¶4-5)"
    factor_refs: list = ['archetype', 'complex', 'imago_dei', 'primordial_type', 'engine_id', 'archetype', 'psych_semantic', 'complex', 'psych_semantic', 'content_distinction', 'psych_semantic', 'source_ref', 'rel_cw9i_003', 'archetype', 'defining', 'rel_cw9i_004', 'complex', 'defining', 'rel_cw9i_005', 'archetype', 'connecting', 'evi_cw9i_003', 'rule_archetype_cu', 'evi_cw9i_004', 'archetype', 'rule_archetype_nature', 'concept_archetype', 'planetary_archetype', 'archetype', 'concept_complex', 'afflicted_planet', 'complex']
    
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
        l1_anchor="acu_v1.0.0_2_archetype_as_content_of_coll_001_L1",
    )
    version: str = "1.0.0"
