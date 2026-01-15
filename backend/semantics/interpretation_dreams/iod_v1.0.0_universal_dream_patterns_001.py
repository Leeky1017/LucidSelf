"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.475536
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
    semantic_id="iod_v1.0.0_universal_dream_patterns_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class UniversalDreamPatterns(SemanticEntry):
    """
    **Source Text** (from section header and context):
"Typical Dreams" include: dreams of nakedness, dr...
    """
    
    original_text: str = """**Source Text** (from section header and context):
"Typical Dreams" include: dreams of nakedness, dreams of the death of loved ones, examination dreams, and falling/flying dreams. These appear across individuals with remarkably similar content, suggesting universal psychic structures.

"The dream of nakedness (Exhibitionsträume) in which we are naked and feel ashamed... The persons before whom we are ashamed are almost always strangers whose faces remain vague."

"Dreams of the death of beloved persons... The dreamer sees in his dream one or both parents, a brother or sister, a child, dying—and thereupon gives expression to painful feelings."

"The examination dream (Prüfungsträume)... Everyone who has passed the examination of the graduating class at a secondary school complains of the obstinacy with which the anxiety-dream of having failed in the examination pursues him."

**Key Term Analysis**:

| Term | Definition | Significance |
|------|-----------|---------------|
| Typical Dreams | Dreams appearing universally with similar content | Evidence for universal psychic structures |
| Nakedness Dream | Dream of being exposed without clothes | Exhibitionism/shame conflict |
| Death-of-Loved-One Dream | Dream featuring death of parent, sibling, child | Ambivalent wishes |
| Examination Dream | Dream of failing an already-passed exam | Anxiety about current challenges |
| Falling/Flying Dream | Dreams of falling or weightless flight | Childhood sensations; sexual arousal |

**English Paraphrase (Primary Language)**:

**Typical dreams** are universal patterns appearing across individuals and cultures with remarkably similar content. Freud identifies several major types:

**Nakedness Dreams** (Exhibitionsträume): The dreamer is naked or inadequately clothed in public, feels intense shame, but observers seem indifferent or have vague faces. This represents the conflict between **exhibitionistic wishes** (from childhood, when nakedness was not shameful) and adult **shame/repression**. The indifferent observers fulfill the wish that exposure doesn't matter.

**Death-of-Loved-Ones Dreams**: The dreamer sees a parent, sibling, or child die and experiences intense grief. Freud's controversial interpretation: these fulfill **repressed death wishes**—not murderous intent, but the ambivalent hostility present in all close relationships. The child who once wished a rival sibling "dead" (not understanding death) carries this wish into adulthood.

**Examination Dreams**: The dreamer fails an exam already passed in reality. This appears when facing new challenges—the dream says: "You feared the old exam but passed; you'll pass this too." Paradoxically, it's a **reassurance mechanism**.

**Falling/Flying Dreams**: These revive **childhood sensations** of being swung, bounced, or rocked. Flying often has erotic undertones; falling may represent fear of moral "falling."

**Complete Chinese Interpretation (Secondary Language)**:

**典型梦**是跨个体和文化出现的、内容惊人相似的普遍模式。弗洛伊德识别了几种主要类型：

**裸体梦**（Exhibitionsträume）：梦者在公共场合赤身裸体或衣着不当，感到强烈羞耻，但观察者似乎无动于衷或面目模糊。这代表**暴露愿望**（来自童年，那时裸体并不可耻）与成人**羞耻/压抑**之间的冲突。冷漠的观察者实现了暴露无关紧要的愿望。

**亲人死亡梦**：梦者看到父母、兄弟姐妹或孩子死亡，体验强烈悲痛。弗洛伊德的争议性解释：这些满足**被压抑的死亡愿望**——不是谋杀意图，而是所有亲密关系中存在的矛盾敌意。曾经希望竞争对手兄弟姐妹"死掉"的孩子（不理解死亡）将这一愿望带入成年。

**考试梦**：梦者在现实中已通过的考试中失败。这在面对新挑战时出现——梦说："你曾害怕旧考试但通过了；你也会通过这个。"悖论地，这是一种**安慰机制**。

**坠落/飞翔梦**：这些复活**童年感觉**——被荡、被弹、被摇。飞翔常有色情暗示；坠落可能代表对道德"堕落"的恐惧。

**Core Points**:

- Typical dreams = universal patterns with similar content
- Nakedness: exhibitionism vs. shame conflict
- Death of loved ones: ambivalent wishes, childhood rivalry
- Examination: reassurance mechanism ("you'll pass again")
- Falling/flying: childhood sensations; erotic undertones
- Universality suggests common psychic structures

**Detailed Explanation**:

Typical dreams are important because their **universality** points to shared psychic structures. If the same dream appears across cultures with similar content and affect, it cannot be explained by individual experience alone—it must tap into **universal developmental patterns**.

The **nakedness dream** illuminates the conflict between id and superego. The child's innocent exhibitionism is repressed in development; the dream returns to this pre-repression state while the dreamer's adult ego feels shame. The indifferent observers are wish-fulfillment: "Let me be seen without judgment."

The **death-wish interpretation** is Freud's most controversial claim about typical dreams. He argues that children's egocentrism produces wishes like "I wish he were dead" without understanding death's finality. These wishes persist unconsciously. When adults dream of a loved one's death with genuine grief, the grief is real—but so was the wish.

**Examination dreams** show dreams can serve **adaptive functions**. They appear during stress, reminding the ego: "You've overcome similar challenges before." The anxiety is real but points backward, not forward.

**Textual Criticism & Variant Analysis (Bilingual)**:

- **English**: "Typical dreams" (German: typische Träume) emphasizes the pattern recurrence. Some translators use "universal dreams" to emphasize cross-cultural appearance.
- **中文**: "典型梦"强调模式重复。有时译为"普遍梦"以强调跨文化出现。弗洛伊德对"亲人死亡梦"的解释在中国文化语境中尤具争议性。

**Narrative Snippets**:

- `[ns_freud_src_004]` `[trigger: typical_dreams]` `[factor_trigger: dream_typical_dream]` `[role: 主干]` Typical dreams appear across individuals with remarkably similar content—nakedness, death of loved ones, examination, falling/flying—suggesting universal psychic structures. → Freud Ch.V #TypicalDreams
- `[ns_freud_src_005]` `[trigger: nakedness_dream]` `[factor_trigger: dream_nakedness_dream AND dream_exhibitionism]` `[role: 主干依赖]` The nakedness dream represents conflict between childhood exhibitionism and adult shame—the indifferent observers fulfill the wish that exposure doesn't matter. → Freud Ch.V #TypicalDreams
- `[ns_freud_src_006]` `[trigger: examination_dream]` `[factor_trigger: dream_examination_dream]` `[role: 条件分支]` The examination dream appears when facing new challenges—it says "you feared the old exam but passed; you'll pass this too." A paradoxical reassurance mechanism. → Freud Ch.V #TypicalDreams
- `[ns_freud_src_012]` `[trigger: death_wish_dream]` `[factor_trigger: dream_death_wish AND dream_ambivalence]` `[role: 条件分支]` Dreams of death of loved ones fulfill repressed death wishes—not murderous intent, but the ambivalent hostility present in all close relationships from childhood. → Freud Ch.V #TypicalDreams
- `[ns_freud_src_013]` `[trigger: flying_falling]` `[factor_trigger: dream_flying AND dream_childhood]` `[role: 条件分支]` Flying and falling dreams revive childhood sensations of being swung, bounced, or rocked—flying often has erotic undertones; falling may represent fear of moral "falling." → Freud Ch.V #TypicalDreams"""
    normalized_text_zh: str = """"""
    subject: str = "Universal Dream Patterns"
    factor_refs: list = ['typical_dream', 'nakedness_dream', 'death_dream', 'examination_dream', 'falling_flying_dream']
    
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
        book_id="interpretation_dreams",
        chapter="",
        l1_anchor="iod_v1.0.0_universal_dream_patterns_001_L1",
    )
    version: str = "1.0.0"
