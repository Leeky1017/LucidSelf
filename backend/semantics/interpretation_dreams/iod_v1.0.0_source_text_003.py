"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.482378
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
    semantic_id="iod_v1.0.0_source_text_003",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class SourceText(SemanticEntry):
    """
    "When, after passing through a narrow defile, one suddenly reaches a height beyond which the ways pa...
    """
    
    original_text: str = """"When, after passing through a narrow defile, one suddenly reaches a height beyond which the ways part and a rich prospect lies outspread in different directions, it may be well to stop for a moment and consider whither one shall turn next. We are in much the same position after we have mastered this first interpretation of a dream. We find ourselves standing in the light of a sudden discovery. The dream is not comparable to the irregular sounds of a musical instrument, which, instead of being played by the hand of a musician, is struck by some external force; the dream is not meaningless, not absurd, does not presuppose that one part of our store of ideas is dormant while another part begins to awake. It is a perfectly valid psychic phenomenon, actually a wish-fulfillment."

#### English Paraphrase (Primary Language)

Freud presents his central theoretical claim with remarkable confidence: dreams are not random neural discharge or meaningless mental noise but meaningful psychological phenomena—specifically, wish-fulfillments. Every dream, without exception, represents the imaginary fulfillment of a wish, usually unconscious. The wish may be disguised through dream-work mechanisms, but fundamentally all dreams serve this function. This theory revolutionized dream psychology by asserting that even nightmares and anxious dreams ultimately fulfill wishes (though these may be punishment wishes or the wish to prove the theory wrong). The dream creates a hallucinatory experience of wish-satisfaction, allowing the dreamer to continue sleeping rather than waking to address the wish in reality.

#### Complete Chinese Interpretation

在区分了显梦与潜梦之后，弗洛伊德给出了极具挑衅性的总论：**每一个梦，本质上都是愿望的满足**。这里的“愿望”并不限于清醒状态下自觉的欲求，而包括大量被压抑的、童年的、社会上不可接受的冲动；这里的“满足”也不是在现实中真正得到，而是在梦的内部以想象、幻觉的方式被“好像已经实现了”。

梦的核心功能，是在不惊动清醒自我的前提下，为这些未被满足的愿望提供一个虚拟情境。睡眠中的心灵在梦里布置一个场景，好让主体仿佛已经得到了想要的东西，于是紧张暂时缓解，睡眠得以继续——这就是梦的**护眠功能**：如果欲望只能在现实中去行动，个体就会被迫醒来；通过梦的幻觉性满足，身体可以继续休息。

问题在于，许多愿望在道德、情感或现实层面都无法被自我接受，尤其是性与攻击冲动、童年依恋与敌意等。如果它们以直接形式出现在显梦中，会立即唤起焦虑，把人惊醒。于是梦的工作必须对愿望进行伪装：通过凝缩、移置和象征等机制，把真正的欲求隐藏在看似无关紧要的情节和人物之下。

这也解释了为什么连恶梦和焦虑梦在弗洛伊德眼中依然是“愿望满足”：要么愿望本身带有自我惩罚色彩（受罚、受苦、赎罪的无意识企图），要么焦虑本身在为更深的心理目的服务，例如证明自己的痛苦、维护某种道德立场，甚至在潜层“希望”精神分析的理论是错的。无论如何，梦总是在为某种欲求工作，只是方式往往高度间接而矛盾。

#### Core Points

- **Universal principle**: Every dream without exception fulfills a wish
- **Unconscious wishes**: Usually hidden, infantile, or forbidden desires
- **Hallucinatory satisfaction**: Dream creates imaginary fulfillment experience
- **Sleep protection**: Wish-fulfillment prevents waking by satisfying desire mentally
- **Disguise necessity**: Unacceptable wishes require distortion to avoid anxiety

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Wish-Fulfillment | Dreams as desire satisfaction | Core Freudian theory |
| Unconscious Wish | Hidden infantile desires | Motivating force |
| Hallucinatory Satisfaction | Imaginary fulfillment | Allows sleep continuation |
| Sleep Protection | Dream function | Prevents waking |

#### Textual Criticism & Variant Analysis (Bilingual)
- **English**: Every dream fulfills a wish. Unconscious, often forbidden desires. Hallucinatory satisfaction prevents waking. Disguise necessary for unacceptable wishes.
- **中文**: 每个梦都满足一个愿望。无意识、常是禁忌的欲望。幻觉满足防止醒来。不可接受的愿望需要伪装。

**Narrative Snippets**:
- `[ns_freud_009]` `[trigger: wish_principle]` `[factor_trigger: wish_fulfillment AND unconscious_wish]` `[role: 主干]` The dream is a perfectly valid psychic phenomenon, actually a wish-fulfillment. → Source Text
- `[ns_freud_010]` `[trigger: dream_not_random]` `[factor_trigger: childhood_wish AND adult_dream]` `[role: 主干依赖]` The dream is not meaningless, not absurd—it does not presuppose that one part of our store of ideas is dormant while another begins to awake. → Source Text
- `[ns_freud_011]` `[trigger: sleep_protection]` `[factor_trigger: sleep_guardian AND hallucinatory_satisfaction]` `[role: 条件分支]` The dream creates hallucinatory experience of wish-satisfaction, allowing the dreamer to continue sleeping. → English Paraphrase
- `[ns_freud_012]` `[trigger: disguise_necessity]` `[factor_trigger: disguise AND censorship]` `[role: 总结]` Because many wishes are unacceptable to consciousness, they require disguise through dream-work mechanisms. → English Paraphrase

#### Detailed Explanation

Freud's wish-fulfillment theory is his most controversial and influential contribution to dream psychology. The claim that every dream fulfills a wish shocked contemporaries and remains debated today. Several aspects require careful understanding:

First, "wish" in Freud's sense is broader than conscious desires. It includes unconscious infantile wishes, forbidden impulses, and even negative wishes (masochistic wishes for punishment, wishes to prove psychoanalysis wrong). The wish may be recent (from the previous day's events) or ancient (rooted in childhood), but it must connect to something currently active in the unconscious.

Second, "fulfillment" means imaginary, hallucinatory satisfaction—not real satisfaction. The dream represents the wish as if it were fulfilled, creating a mental experience of satisfaction. This hallucinatory fulfillment serves a crucial function: it allows sleep to continue by temporarily satisfying the wish mentally so it doesn't demand real-world action that would require waking.

Third, the wish-fulfillment is often heavily disguised. Because many wishes are unacceptable to consciousness (incestuous, aggressive, shameful), they cannot be directly represented without causing anxiety that would disrupt sleep. The dream-work disguises these wishes through condensation, displacement, and symbolization, creating manifest content that doesn't obviously reveal the underlying wish. This explains why dreams often seem meaningless or bizarre—the disguise is working.

Fourth, even nightmares and anxiety dreams fit this theory, though this requires explanation. Freud argues that nightmares may fulfill masochistic punishment wishes, or may represent cases where the censorship fails and the anxiety breakthrough occurs. Alternatively, the anxiety itself may serve a wish—to prove one's suffering, to punish oneself, or to demonstrate that psychoanalytic theory is wrong.

The wish-fulfillment theory provided Freud with a unified principle explaining all dreams, making dream interpretation a scientific rather than mystical enterprise. If every dream is a disguised wish-fulfillment, interpretation becomes the systematic uncovering of which wish is being fulfilled and how it's disguised.

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
        l1_anchor="iod_v1.0.0_source_text_003_L1",
    )
    version: str = "1.0.0"
