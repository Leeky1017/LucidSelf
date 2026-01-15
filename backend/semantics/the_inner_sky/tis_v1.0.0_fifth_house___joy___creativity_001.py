"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.094022
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
    semantic_id="tis_v1.0.0_fifth_house___joy___creativity_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class FifthHouseJoyCreativity(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Necessity of Joy | Life ...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Necessity of Joy | Life requires pleasure | Core concept |
| Portfolio of Pleasures | Variety not addiction | Mastery |
| Creative Imprint | Self on world | Expression |
| Romance Vitality | Ego revitalized | Experience |

#### Source Text

"In the face of all that hellishness, there is only one force between us and despair: pleasure. Pleasure is what keeps us in the world. Unsuccessful passage invariably involves getting hung up on a single pleasure, forgetting there are so many others. Do all that, and even when you die they won't be able to wipe away your smile."

#### English Paraphrase

The **Fifth House** is the arena of **joy, creativity, and self-expression**. It is the antidote to the seriousness of life.

**The Necessity of Joy**:
Life is hard. Without **pleasure** and **play**, we wither. The Fifth House represents the vital spark that makes life worth living.

**Forms of Pleasure**:
- **Physical**: Romance, sex, games, sports.
- **Creative**: Art, making things, self-expression.
- **Spiritual**: Meditation, awe, deep connection.
- **Risk**: Gambling, adventure, taking chances.

**The Trap**:
Becoming addicted to **one** type of pleasure (e.g., alcohol, one lover, gambling) destroys joy. True Fifth House mastery means cultivating a **broad portfolio of pleasures** so that joy is sustainable and balanced.

**Creative Self-Expression**:
This house is about externalizing what is inside—imprinting our unique identity onto the world through creation (children, art, projects).

**Falling in Love**:
The thrill of romance is a Fifth House experience—it revitalizes the ego and makes the world seem magical.

#### Complete Chinese Interpretation

**第五宫**是**喜悦、创造力和自我表达**的领域。它是生活严肃性的解药。

**喜悦的必要性**：
生活是艰难的。没有**快乐**和**玩耍**，我们会枯萎。第五宫代表让生活值得过的生命火花。

**快乐的形式**：
- **身体**：浪漫、性、游戏、运动。
- **创造**：艺术、制作东西、自我表达。
- **精神**：冥想、敬畏、深度连接。
- **风险**：赌博、冒险、抓住机会。

**陷阱**：
对**单一**类型的快乐（如酒精、一个情人、赌博）上瘾会摧毁喜悦。真正的第五宫掌握意味着培养**广泛的快乐组合**，使喜悦可持续且平衡。

**创造性自我表达**：
这一宫是关于将内在的东西外在化——通过创造（孩子、艺术、项目）将我们独特的身份印刻在世界上。

**坠入爱河**：
浪漫的兴奋是第五宫的体验——它使自我恢复活力，让世界看起来充满魔力。

#### Core Points

- Arena of joy, pleasure, and play.
- Creative self-expression (imprinting self on world).
- Romance and risk-taking.
- Warning against addiction to single pleasures.
- East parallel: 子女宫/食神/桃花 (Children Palace, Creativity, Romance).

#### Detailed Explanation

The Fifth House is the arena of **joy, play, and creative self-expression**. Forrest emphasizes that pleasure is not frivolous—it's **essential to survival**. Without that sparkle, we wither. Joy is what keeps us engaged with life despite its inevitable suffering.

Creativity in the Fifth House means **imprinting ourselves on the world**: painting, writing, performing, building—any activity where we leave our unique mark. Romance belongs here too, not for its relational aspect (that's the Seventh) but for its **ecstatic quality**—the joy of falling in love, the thrill of attraction.

**Successful navigation** means finding reliable sources of joy and creative expression that renew the spirit. The challenge is **diversity**: if we become addicted to a single pleasure (one romance, one hobby, one substance), we become vulnerable. **Unsuccessful navigation** produces either joylessness (the person who has forgotten how to play) or addictive pursuit of narrow pleasures.

#### Narrative Snippets

- `[ns_innersky_h5_001]` `[trigger: house_5_general]` `[factor_trigger: astro_house_5]` `[role: 主干]` Joy—how deeply we need it! Its absence is as fatal as a ten-year fast or a month without oxygen. Without that sparkle, we wither. → The Inner Sky Ch.7 #5H
- `[ns_innersky_h5_002]` `[trigger: house_5_pleasure]` `[factor_trigger: astro_house_5]` `[role: 主干依赖]` In the face of all that hellishness, there is only one force between us and despair. That force is pleasure. At some undeniable, immediate level, pleasure is what keeps us in the world. → The Inner Sky Ch.7 #5H
- `[ns_innersky_h5_003]` `[trigger: house_5_creativity]` `[factor_trigger: astro_house_5 AND astro_creative_expression]` `[role: 条件分支]` Imagine how good Michelangelo felt when he first stood back and admired his Sistine Chapel. Creativity is a joy. Meditation is a joy. "Falling in love" with a grizzled sea captain ninety years old is a joy. → The Inner Sky Ch.7 #5H
- `[ns_innersky_h5_004]` `[trigger: house_5_addiction]` `[factor_trigger: astro_house_5 AND astro_state_dysfunction]` `[role: 条件分支]` An unsuccessful passage through the fifth house invariably involves getting hung up on a single pleasure, forgetting that there are so many others. → The Inner Sky Ch.7 #5H
- `[ns_innersky_h5_005]` `[trigger: house_5_mastery]` `[factor_trigger: astro_house_5 AND astro_state_success]` `[role: 总结]` Learn to enjoy all of them. Develop the skills and habits they require. Guard against asking too much of any single one. Do all that, and even when you die they won't be able to wipe away your smile. → The Inner Sky Ch.7 #5H"""
    normalized_text_zh: str = """"""
    subject: str = "Fifth House - Joy & Creativity"
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
        l1_anchor="tis_v1.0.0_fifth_house___joy___creativity_001_L1",
    )
    version: str = "1.0.0"
