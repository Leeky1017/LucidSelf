"""
Auto-generated semantic module for collected_works
Generated at: 2025-12-05T13:30:20.574857
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
    semantic_id="cw_v1.0.0_source_text_001",
    book_id="collected_works",
    engine_id="psych"
)
class SourceText(SemanticEntry):
    """
    "My thesis then, is as follows: in addition to our immediate consciousness, which is of a thoroughly...
    """
    
    original_text: str = """"My thesis then, is as follows: in addition to our immediate consciousness, which is of a thoroughly personal nature and which we believe to be the only empirical psyche (even if we tack on the personal unconscious as an appendix), there exists a second psychic system of a collective, universal, and impersonal nature which is identical in all individuals. This collective unconscious does not develop individually but is inherited. It consists of pre-existent forms, the archetypes, which can only become conscious secondarily and which give definite form to certain psychic contents."

#### English Paraphrase (Primary Language)

The **Collective Unconscious** is Jung's revolutionary concept proposing a layer of psyche **deeper than personal unconscious**—a universal, inherited stratum **identical in all humans** regardless of culture or era. This isn't learned or acquired but **pre-exists** at birth, containing the accumulated psychic experience of humanity's entire evolutionary history.

**Structure**:
- **Personal Consciousness**: Everyday awareness, ego, what we think of as "me"
- **Personal Unconscious**: Repressed memories, forgotten experiences, shadow material (individual's unique history)
- **Collective Unconscious**: Universal patterns, instinctual responses, archetypal images (species-wide inheritance)

**Key characteristics**:
- **Pre-existent**: Present before individual experience, inherited like biological instincts
- **Universal**: Identical structure in all humans (though content varies culturally)
- **Impersonal**: Not derived from personal experience but from human evolutionary heritage
- **Archetypal**: Contains **archetypes**—universal patterns that structure experience

**Why it matters**: Explains why humans across all cultures produce similar myths, symbols, dreams despite no contact. The snake as wisdom/danger, the Great Mother, the Hero's Journey—these aren't learned but emerge spontaneously from collective unconscious.

**Evidence**: Cross-cultural mythological parallels, recurring dream symbols, spontaneous religious imagery in psychotics who've had no religious education, children's fantasies matching ancient myths.

**Function**: Provides **inherited templates** for responding to universal human situations—birth, death, danger, mating, conflict. When situation arises (e.g., encountering authority figure), corresponding archetype (Father) activates, structuring perception and response.

**Distinction from Freud**: Freud's unconscious is entirely personal (repressed individual content). Jung adds **transpersonal layer**—not my repressed father but THE Father archetype shaping all father experiences.

#### Complete Chinese Interpretation (Secondary Language)

完整中文诠释：集体无意识在荣格体系中，是位于个人无意识之下、更为深层的一层“普遍心灵基底”。它**不是**由个人经验累积而成，而是像本能一样**与生俱来、通过种族演化遗传下来**的心理结构——好比身体有大脑、四肢这一套普遍解剖架构，心灵也有一套对所有人都相同的深层结构。表层我们有清醒意识（自我、小我）与承载被压抑记忆的个人无意识，而在更深处，则存在一个对所有文化、年代的人类都共同的“心灵海洋”：其中包含各种原型的**先验形式**，一旦被情境触发，就会在梦、神话、宗教意象、幻想故事中，以各民族的符号语言浮出水面。

这一概念首先用来解释一个经验事实：**世界各地互不相通的文化，却反复讲述极其相似的故事、制造相似的象征**——英雄下冥界、伟大母亲、智慧老人、蛇既代表危险又代表智慧等。荣格认为，这种跨文化平行并不能完全用“文化传播”或“巧合”解释，更合理的说法是：人类在漫长演化历程中，对某些反复出现的生命情境（生死、父权、母爱、群体冲突、启蒙经验）形成了稳定的心理应对模式，这些模式沉积为**原型（archetype）**，以集体无意识的形式遗传给后代。当我们再次面对类似处境时，对应原型便被“激活”，用已有的结构为经验赋形。

与弗洛伊德只承认“个人无意识”不同，荣格在此基础上提出**“超个人/跨个体”的深层维度**：弗洛伊德的无意识主要是“我的历史里被压抑的东西”，而荣格认为在这一层之下，还有一个“并非我个人专属、而是整个人类共享的心灵层级”。因此，当我们在梦中见到陌生却庄严的宗教形象，或在极端状态下涌现出古老神话的场景，即便当事人从未受过相关教育，也可以理解为：集体无意识正在透过原型意象发声。临床上，荣格在精神病人的妄想与幻觉中，屡次观察到与诺斯替主义、炼金术文献高度相似的象征结构，这正是他提出集体无意识假说的经验依据之一。

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Collective Unconscious | Universal inherited psychic layer | Jung's foundation |
| Archetypes | Pre-existent forms | Structure experience |
| Transpersonal | Beyond individual | Species-wide |
| Evolutionary Heritage | Inherited patterns | Not learned |

#### Core Points

- **Deeper than personal**: Beyond individual repressed content lies universal layer
- **Inherited not learned**: Pre-exists at birth, evolutionary psychic heritage
- **Universal in all humans**: Identical structure regardless of culture/era
- **Contains archetypes**: Pre-existent forms structuring experience
- **Explains parallels**: Why myths/symbols/dreams similar across cultures
- **Impersonal**: Species-wide, not derived from personal history
- **Distinction from Freud**: Adds transpersonal layer to personal unconscious

#### Detailed Explanation

Jung's collective unconscious concept emerged from clinical observation and comparative mythology study. As Swiss psychiatrist treating psychotics, he noticed **patients with no religious education producing elaborate religious symbolism** matching ancient Gnostic texts they couldn't have known. Children's dreams contained mythological motifs they'd never encountered. Patients worldwide reported similar archetypal dreams—pursued by shadow figure, meeting wise old man, descending into underworld.

**Evolutionary basis**: Just as body evolved universal structures (two arms, one heart), psyche evolved universal structures—archetypes. These represent humanity's **accumulated experience of recurrent situations**. Every human faces authority (Father archetype), nurturing (Mother archetype), choosing identity (Hero archetype). Over millions of years, responses to these situations crystallized into inherited psychic patterns.

**Biological parallel**: Analogous to instincts. A bird doesn't learn nest-building through education—the pattern is inherited. Similarly, humans don't learn to see authority figures as fathers or nurturers as mothers—these patterns activate automatically when appropriate situation triggers them.

**How it manifests**: Collective unconscious never becomes conscious directly—too vast, too impersonal. It manifests through **archetypal images and motifs** that emerge in:
- **Dreams**: Universal symbols appearing spontaneously
- **Myths**: Similar stories across unconnected cultures
- **Fantasies**: Active imagination producing archetypal narratives
- **Psychosis**: When ego weakens, archetypal material floods consciousness
- **Religious experience**: Numinous encounters with divine archetypes

**Cultural clothing**: While collective unconscious is universal, archetypes manifest through cultural symbols. The Great Mother appears as Virgin Mary (Christian), Kali (Hindu), Isis (Egyptian)—different cultural expressions of same underlying archetype.

**Therapeutic significance**: Neurosis often involves **disconnection from collective unconscious**. Over-identification with persona/ego cuts person off from deeper psychic life. Reconnecting through dream work, active imagination, ritual allows access to transpersonal wisdom and healing.

**Philosophical implications**: Challenges Enlightenment view of humans as "blank slates." We're born with inherited psychic structures shaping perception and experience. Also implies **psychic unity of humankind**—beneath cultural differences lies shared symbolic substrate.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Collective Unconscious: Jung's foundational concept. Universal inherited psychic layer deeper than personal unconscious. Contains archetypes as pre-existent forms. Explains cross-cultural symbol parallels. Distinct from Freud's purely personal unconscious.
- **中文**: 集体无意识:荣格基础概念。比个人无意识更深的普遍遗传心理层。包含原型作为先在形式。解释跨文化符号平行。不同于弗洛伊德纯籹个人无意识。

**Narrative Snippets**:
- `[ns_jung_001]` `[trigger: collective_unconscious]` `[factor_trigger: jung_collective_unconscious AND jung_universal]` `[role: 主干]` Beyond personal consciousness exists a second psychic system of collective, universal, impersonal nature—identical in all individuals. → Source Text
- `[ns_jung_002]` `[trigger: inherited_not_learned]` `[factor_trigger: jung_inherited AND jung_archetype]` `[role: 主干依赖]` This collective unconscious does not develop individually but is inherited; it consists of pre-existent forms, the archetypes. → Source Text
- `[ns_jung_003]` `[trigger: deeper_than_personal]` `[factor_trigger: jung_collective AND jung_personal]` `[role: 条件分支]` The collective unconscious is deeper than personal unconscious—a universal inherited stratum present at birth. → English Paraphrase
- `[ns_jung_004]` `[trigger: cross_cultural_parallels]` `[factor_trigger: jung_cross_cultural AND jung_symbol]` `[role: 总结]` Explains why humans across all cultures produce similar myths, symbols, dreams despite no contact. → English Paraphrase
- `[ns_jung_005]` `[trigger: transpersonal_layer]` `[factor_trigger: jung_transpersonal AND jung_species]` `[role: 主干]` Unlike Freud's purely personal unconscious, Jung adds a transpersonal layer—species-wide, not individual. → English Paraphrase
- `[ns_jung_006]` `[trigger: psychic_unity]` `[factor_trigger: jung_psychic AND jung_unity]` `[role: 主干依赖]` Beneath cultural differences lies a shared symbolic substrate—the psychic unity of humankind. → English Paraphrase

---"""
    normalized_text_zh: str = """"""
    subject: str = "Source Text"
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
        book_id="collected_works",
        chapter="",
        l1_anchor="cw_v1.0.0_source_text_001_L1",
    )
    version: str = "1.0.0"
