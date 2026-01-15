"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.482431
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
    semantic_id="iod_v1.0.0_source_text_008",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class SourceText(SemanticEntry):
    """
    "Between the unconscious and the consciousness there is stationed a sort of guard or censor, which e...
    """
    
    original_text: str = """"Between the unconscious and the consciousness there is stationed a sort of guard or censor, which examines the various mental excitations, subjects them to a censorship, and will not admit them into consciousness if they do not meet with his approval. This censor is stricter during the waking state; during sleep he relaxes somewhat, but even then he does not entirely lay down his office. Thus, the unacceptable wish is forced to shape itself in such a way that it will not offend the censor; it must adopt a disguise."

#### English Paraphrase (Primary Language)

Censorship is the psychic force or agency that prevents unacceptable unconscious wishes from entering consciousness directly. Positioned between the unconscious and consciousness, the censor examines all material attempting to cross this boundary, blocking or requiring disguise of anything deemed unacceptable—forbidden wishes, shameful thoughts, anxiety-provoking ideas. During waking, censorship operates at full strength, maintaining strict repression. During sleep, censorship relaxes but doesn't disappear, allowing unconscious wishes expression only if sufficiently disguised. This necessitates the dream-work's elaborate transformations—condensation, displacement, symbolization—which disguise latent wishes enough to pass the censored barrier while still achieving some satisfaction. The censor is not consciously controlled; it operates automatically as part of ego's defensive structure.

#### Complete Chinese Interpretation

所谓**审查机制**，就是弗洛伊德在拓扑模型中假定的一道“心理边防线”：一切来自无意识的冲动、图像与思想，要想进入意识，必须先通过这道关卡的检查。凡是与道德禁忌、理想自我形象或现实适应严重冲突的内容——尤其是性与攻击的原始愿望、对亲近对象的矛盾情感、与创伤相关的记忆——都会在这一层被拦下或要求彻底伪装。

在清醒状态下，审查几乎全力运作：不可接受的欲望被压抑到底层，只能以口误、笑话、症状等间接方式冒头。一旦入睡，外界感官输入减少、身体运动被抑制，冲动在现实中实施的危险降低，于是审查会**相对放松**，允许部分被压抑内容以“变装”形式浮上来——这就是梦得以发生的条件。但即便在睡眠中，审查也从不完全撤岗，因此梦的工作必须通过凝缩、移置、象征化等方式，把原始愿望改装成审查可以容忍的样子。

从这个角度看，梦的荒诞、断裂与间接，正是审查机制的工作痕迹：显梦之所以看不出真实意图，是因为那股“看门人”的力量要求一切敏感内容都绕圈子说话。一旦伪装失败，审查无法接受的内容过于直接突破，就会出现强烈焦虑和噩梦，甚至把人惊醒——这既是梦的失败，也是防御的成功：通过醒来终止危险的心理过程。

同一套审查逻辑也在神经症症状中运作：症状与梦一样，是在审查压力下形成的“折衷产物”，既让被压抑欲望在扭曲形式中获得某种实现，又维持自我表层的道德与秩序感。因此，理解梦中的审查，也就抓到理解症状形成的总钥匙。

#### Core Points

- **Guardian agency**: Psychic force stationed between unconscious and consciousness
- **Approval requirement**: Examines mental content, blocks unacceptable material
- **Waking vs sleeping**: Stricter when awake, relaxes but persists during sleep
- **Necessitates disguise**: Unacceptable wishes must adopt disguise to pass censorship
- **Automatic operation**: Not consciously controlled, part of ego's defensive structure

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Censorship (Zensur) | Psychic gatekeeper | Blocks unacceptable |
| Guardian Agency | Between Ucs-Cs | Examines/blocks |
| Waking vs Sleep | Strictness variation | Relaxes in sleep |
| Disguise Requirement | Pass the censor | Drives dream-work |

#### Textual Criticism & Variant Analysis (Bilingual)
- **English**: Censorship: guardian between unconscious/consciousness. Blocks unacceptable wishes. Stricter awake, relaxes in sleep. Necessitates dream-work disguise.
- **中文**: 审查:无意识/意识之间的守护者。阻挡不可接受的愿望。清醒时更严格,睡眠中放松。使梦的工作伪装成为必要。

**Narrative Snippets**:
- `[ns_freud_029]` `[trigger: censor_guardian]` `[factor_trigger: dream_censor AND dream_guardian]` `[role: 主干]` Between the unconscious and consciousness stands a psychic guard or censor that examines mental excitations and blocks unacceptable material. → Source Text
- `[ns_freud_030]` `[trigger: waking_sleep_strength]` `[factor_trigger: dream_censor AND dream_sleep]` `[role: 主干依赖]` The censor is stricter during the waking state and only relaxes somewhat in sleep—it never entirely lays down its office. → Source Text
- `[ns_freud_031]` `[trigger: disguise_requirement]` `[factor_trigger: dream_censor AND dream_disguise]` `[role: 条件分支]` Because the censor remains on duty even in sleep, unacceptable wishes can reach consciousness only by adopting disguise through dream-work mechanisms. → English Paraphrase
- `[ns_freud_032]` `[trigger: ego_defense_censor]` `[factor_trigger: dream_ego AND dream_defense]` `[role: 总结]` Censorship operates automatically as part of the ego's defensive structure, enforcing internalized moral prohibitions on what may become conscious. → English Paraphrase

#### Detailed Explanation

Censorship is a crucial concept in Freud's topographical model of mind, explaining why unconscious content requires disguise to become conscious. The censor represents the ego's defensive function protecting consciousness from material that would provoke anxiety, guilt, or disruption if acknowledged directly.

**The censor as guardian**: Freud's metaphor of a "guard" or "censor" stationed at the boundary between unconscious and consciousness captures the active, selective nature of this process. Not a passive barrier but an examining agent that scrutinizes content, permitting some, blocking most, and demanding disguise of forbidden material.

**What the censor rejects**: Primarily unconscious wishes that violate moral prohibitions (superego demands), threaten self-esteem (narcissistic wounds), or would generate overwhelming anxiety (traumatic material). Especially sexual and aggressive wishes from infantile sources—the Oedipus complex and its derivatives. The censor operates according to internalized parental and cultural prohibitions.

**Differential operation during sleep**: During waking, censorship maintains maximum vigilance. Unacceptable wishes remain fully repressed, accessible only through derivatives (symptoms, slips, jokes). During sleep, motor inhibition and sensory withdrawal reduce the danger posed by wish-fulfillment (can't act on wishes during sleep), so the censor relaxes slightly. This partial relaxation enables dreams—disguised fulfillments that would be completely blocked when awake.

**Necessitates dream-work**: Because censorship persists even during sleep, unconscious wishes cannot appear directly. The dream-work is essentially the process of achieving sufficient disguise to satisfy the censor. Condensation makes wishes unrecognizable through compression; displacement shifts attention from significant to trivial; symbolization uses universal symbols the dreamer doesn't consciously understand. These mechanisms transform unacceptable latent wishes into acceptable manifest content.

**Anxiety dreams and nightmares**: Represent partial failures of censorship. The disguise proves insufficient; the wish breaks through in recognizable form generating anxiety that disrupts sleep. Or, the censorship itself generates punishment (masochistic punishment wishes fulfill the need to suffer).

**Censorship in symptom formation**: The same censorship operating in dreams functions in neurotic symptom formation. Symptoms are compromise formations—disguised expressions of forbidden wishes that pass censorship through their symbolic, displaced character. Dream interpretation thus models understanding all unconscious compromise formations.

**Ego psychology development**: Later psychoanalysis elaborated censorship into a more sophisticated theory of ego defenses (repression, denial, reaction-formation, etc.). But Freud's dream censor captures the essential insight: unconscious wishes face an internal barrier requiring disguise for any expression.

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
        book_id="interpretation_dreams",
        chapter="",
        l1_anchor="iod_v1.0.0_source_text_008_L1",
    )
    version: str = "1.0.0"
