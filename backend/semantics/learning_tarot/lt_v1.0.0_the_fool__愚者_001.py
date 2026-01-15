"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.007948
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
    semantic_id="lt_v1.0.0_the_fool__愚者_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class TheFool愚者(SemanticEntry):
    """
    **Source Text** (Lines 3454-3522):
> **Keywords**: Beginning • Spontaneity • Faith • Apparent Folly
...
    """
    
    original_text: str = """**Source Text** (Lines 3454-3522):
> **Keywords**: Beginning • Spontaneity • Faith • Apparent Folly
>
> **Actions**:
> - **Beginning**: entering a new phase, striking out on a new path, expanding horizons, starting something new, beginning an adventure, going on a journey, heading into the unknown
> - **Being Spontaneous**: living in the moment, letting go of expectations, doing the unexpected, acting on impulse, feeling uninhibited, surprising someone, feeling carefree
> - **Having Faith**: trusting the flow, staying open, letting go of worry and fear, feeling protected and loved, living in joy, recapturing innocence, believing
> - **Embracing Folly**: accepting your choices, taking the "foolish" path, pursuing a pipe dream, being true to yourself, taking a "crazy" chance, trusting your heart's desire
>
> **Description**: As Card 0, the Fool lies at the beginning of the major arcana, but also somewhat apart from the other cards. In medieval courts, the court jester was someone who was not expected to follow the same rules as others... The Fool also represents the complete faith that life is good and worthy of trust. Some might call the Fool too innocent, but his innocence sustains him and brings him joy.

**Key Term Analysis**:
- **The Fool (0)**: `beginning of major arcana` / `apart from other cards` / `court jester`
- **Beginning**: `new phase` / `new path` / `expanding horizons` / `heading into unknown`
- **Spontaneity**: `living in the moment` / `letting go of expectations` / `acting on impulse`
- **Faith**: `trusting the flow` / `staying open` / `feeling protected and loved`
- **Apparent Folly**: `"foolish" path` / `pipe dream` / `being true to yourself`

**English Paraphrase (Primary Language)**:
**The Fool (Card 0)** is unique—"at the beginning of the major arcana, but also somewhat apart." Like the court jester who "was not expected to follow the same rules," The Fool represents:

1. **Beginning**: New phases, new paths, adventures, journeys into the unknown. The Fool signals fresh starts and expanded horizons.

2. **Spontaneity**: Living in the moment, acting on impulse, doing the unexpected. "There is a sense with this card that anything goes—nothing is certain or regular."

3. **Faith**: "The complete faith that life is good and worthy of trust." Some call this innocence, but "his innocence sustains him and brings him joy."

4. **Apparent Folly**: Taking chances others consider crazy. "If you are facing a decision or moment of doubt, the Fool tells you to believe in yourself and follow your heart no matter how crazy or foolish your impulses may seem."

**Opposing cards**: Hierophant (convention), Death (ending), Devil (cynicism), Two of Swords (blocking experience), Four of Pentacles (order/regularity).

**Reinforcing cards**: Hanged Man (faith, going with flow), Star (innocence, trust), Judgement (rebirth, new starts), Three of Wands (expanding horizons).

**Complete Chinese Interpretation (Secondary Language)**:
**愚者（第0号牌）**是独特的——"在大阿卡纳的开始，但也有些与众不同"。就像宫廷小丑"不需要遵循与他人相同的规则"，愚者代表：

1. **开始**：新阶段、新道路、冒险、进入未知的旅程。愚者预示着新的开始和扩展的视野。

2. **自发性**：活在当下、凭冲动行事、做出意外之举。"这张牌给人的感觉是一切皆有可能——没有什么是确定或规律的。"

3. **信念**："对生命美好且值得信任的完全信念。"有人称之为天真，但"他的天真维持着他并带给他快乐。"

4. **表面的愚蠢**：冒他人认为疯狂的风险。"如果你面临决定或怀疑的时刻，愚者告诉你要相信自己，追随内心，无论你的冲动看起来多么疯狂或愚蠢。"

**对立牌**：教皇（传统）、死神（结束）、恶魔（愤世嫉俗）、宝剑二（阻断体验）、星币四（秩序/规律）。

**增强牌**：倒吊人（信念、顺其自然）、星星（纯真、信任）、审判（重生、新开始）、权杖三（扩展视野）。

**Core Points**:
- Card 0 = beginning AND tarot_apart, like court jester outside normal rules
- Beginning: new phases, paths, adventures, unknown territory
- Spontaneity: living in moment, acting on impulse, anything goes
- Faith: complete trust that life is good, innocence sustains joy
- Apparent Folly: "crazy" chances, following heart despite doubt

**Narrative Snippets**:
- `[ns_ltt_019]` `[trigger: fool_card]` `[factor_trigger: tarot_fool]` `[role: 主干]` The Fool lies at the beginning of the major arcana but also somewhat apart—like the court jester not expected to follow the same rules as others. → L3507-3510
- `[ns_ltt_020]` `[trigger: fool_beginning]` `[factor_trigger: tarot_fool AND tarot_new_beginning]` `[role: 主干依赖]` The Fool can signal a new beginning or change of direction—one that will guide you onto a path of adventure, wonder, and personal growth. → L3518-3519
- `[ns_ltt_021]` `[trigger: fool_faith]` `[factor_trigger: tarot_fool AND tarot_faith AND faith AND spontaneity]` `[role: 主干依赖]` The Fool represents complete faith that life is good and worthy of trust—his innocence sustains him and brings him joy. → L3515-3517
- `[ns_ltt_022]` `[trigger: fool_folly]` `[factor_trigger: tarot_fool AND tarot_decision AND apparent_folly]` `[role: 总结]` If you are facing a decision or moment of doubt, the Fool tells you to believe in yourself and follow your heart no matter how crazy your impulses may seem. → L3520-3522

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: The Fool's number (0 vs 22) is debated. RWS and most modern decks place him at 0 (beginning). Some esoteric systems place him at 22 (completion/transcendence). Bunning follows RWS positioning. The jester/innocent symbolism is consistent across traditions.
- **中文**: 愚者的编号（0还是22）有争议。RWS和大多数现代牌组将其放在0号（开始）。一些神秘系统将其放在22号（完成/超越）。Bunning遵循RWS定位。小丑/纯真象征在各传统中是一致的。"""
    normalized_text_zh: str = """"""
    subject: str = "The Fool (愚者)"
    factor_refs: list = ['tarot_fool', 'new_beginning', 'spontaneity', 'faith', 'apparent_folly']
    
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
        book_id="learning_tarot",
        chapter="",
        l1_anchor="lt_v1.0.0_the_fool__愚者_001_L1",
    )
    version: str = "1.0.0"
