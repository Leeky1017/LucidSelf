"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.122539
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
    semantic_id="tis_v1.0.0_seventh_house___the_descendant_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class SeventhHouseTheDescendant(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| The Other | Not-Self int...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| The Other | Not-Self integration | Core concept |
| Identification | Suspend ego | Challenge |
| Three Keys | Equality/Open/Magic | Success factors |
| Anima/Animus | Shadow projection | Depth psychology |

#### Source Text

"The cornerstone of all dramatic art—and the basis of any intimate relationship—is the elemental I-equal-you equation. To identify with others—to love them—we must temporarily set aside our own point of view. Three requirements for success: Equality, Open-endedness, and Magic."

#### English Paraphrase

The **Seventh House** (Descendant) is the arena of **intimate partnership and identification**. It represents the "Not-Self"—the Other we must integrate to become whole.

**The Core Challenge**:
- **Identification**: Putting yourself in another's shoes. Recognizing that the Other is as real as you are.
- **Setting Aside Self**: Temporarily suspending your own ego to experience life through another's eyes.

**Two Perils**:
1.  **Isolation**: Failing to connect, living in a universe of strangers.
2.  **Loss of Self**: Becoming lost in the relationship, a shadow of the partner.

**Three Keys to Success**:
1.  **Equality**: Interdependency, no boss/subordinate dynamic.
2.  **Open-endedness**: Commitment to the *person*, not just the convenience or circumstance. ("Till death do us part").
3.  **Magic**: Special rapport, chemistry, karma—the spark that blasts through ego walls.

**Planets Here**:
Describe the type of partner we attract and the qualities we project onto them (our "Shadow" or "Anima/Animus").

#### Complete Chinese Interpretation

**第七宫**（下降点）是**亲密伙伴关系和认同**的领域。它代表"非我"——我们必须整合以变得完整的他者。

**核心挑战**：
- **认同**：设身处地为他人着想。认识到他者与你一样真实。
- **搁置自我**：暂时悬置自己的小我，通过他人的眼睛体验生活。

**两个危险**：
1.  **孤立**：未能连接，生活在陌生人的宇宙中。
2.  **丧失自我**：迷失在关系中，成为伴侣的影子。

**成功的三个关键**：
1.  **平等**：相互依赖，没有老板/下属的动态。
2.  **开放性**：对*人*的承诺，而不仅仅是便利或环境。（"至死不渝"）。
3.  **魔力**：特殊的融洽关系、化学反应、业力——炸开小我墙壁的火花。

**此处的行星**：
描述了我们吸引的伴侣类型以及我们投射到他们身上的特质（我们的"阴影"或"阿尼玛/阿尼姆斯"）。

#### Core Points

- Arena of "The Other" and intimate one-on-one relationships.
- Challenge: Identification without losing self.
- Requires Equality, Commitment, and "Magic".
- East parallel: 夫妻宫/正官/合 (Spouse Palace, Partnership, Harmony).

#### Detailed Explanation

The Seventh House governs **intimate one-on-one relationships**—the realm of "The Other." Forrest emphasizes that true intimacy requires **identification**: temporarily setting aside our own viewpoint to see through another's eyes. This is the foundation of love, friendship, and partnership.

The challenge is profound: to identify **without losing ourselves**. We must merge enough to truly know another person, yet maintain enough separateness to remain ourselves. Many fail at one extreme or the other—either never truly connecting (living among strangers) or merging so completely that they lose their own identity.

**Successful navigation** requires three elements: **Equality** (interdependence without dominance), **Open-ended Commitment** (loyalty to the person, not just convenience), and **Magic** (special rapport that transcends ego boundaries). The Seventh House describes not just who we attract, but what qualities we project onto partners—our "shadow" or unlived self.

#### Narrative Snippets

- `[ns_innersky_h7_001]` `[trigger: house_7_general]` `[factor_trigger: astro_house_7]` `[role: 主干]` Identification—putting yourself in the other person's shoes—is the cornerstone of all dramatic art and the basis of any intimate relationship. If the mind fails to set up that elemental I-equal-you equation, no human being will ever touch us. → The Inner Sky Ch.7 #7H
- `[ns_innersky_h7_002]` `[trigger: house_7_challenge]` `[factor_trigger: astro_house_7]` `[role: 主干依赖]` To identify with them—to love them—we must temporarily set aside our own point of view. We must look at life through their eyes. A perilous process. → The Inner Sky Ch.7 #7H
- `[ns_innersky_h7_003]` `[trigger: house_7_isolation]` `[factor_trigger: astro_house_7 AND astro_state_dysfunction]` `[role: 条件分支]` If we cannot manage it, we make no lasting intimate contacts. We may be married. We may have friends. But our isolation is perfect—our universe is populated only with strangers. → The Inner Sky Ch.7 #7H
- `[ns_innersky_h7_004]` `[trigger: house_7_success]` `[factor_trigger: astro_house_7 AND astro_state_success]` `[role: 条件分支]` A successful passage requires: Equality (interdependency, no boss), Open-endedness (commitment to the person, not convenience), and Magic (special rapport that blasts through ego walls). → The Inner Sky Ch.7 #7H
- `[ns_innersky_h7_005]` `[trigger: house_7_loss_of_self]` `[factor_trigger: astro_house_7 AND astro_state_dysfunction]` `[role: 总结]` Perhaps we cannot get our personality back again. We may become lost in the relationship, so swayed by the other person's world view that we lose track of our own identity. We become a shadow cast by another person. → The Inner Sky Ch.7 #7H"""
    normalized_text_zh: str = """"""
    subject: str = "Seventh House - The Descendant (Partnership)"
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
        book_id="the_inner_sky",
        chapter="",
        l1_anchor="tis_v1.0.0_seventh_house___the_descendant_001_L1",
    )
    version: str = "1.0.0"
