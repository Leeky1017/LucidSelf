"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.076530
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
    semantic_id="bot_v1.0.0_nine_of_swords__cruelty__宝剑九_残_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class NineOfSwordsCruelty宝剑九残(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Yesod in Air | Foundation in Air | Degenerated return |
| Mars in Gemini | Aggression + intellect | Inquisitor mentality |
| Rusty Jagged Swords | Degraded weapons | Poison dripping |
| Heartless Passion | Automatic cruelty | Unenlightened instinct |

**Title**: Lord of Despair and Cruelty (绝望与残酷之主)
**Qabalistic**: Yesod in Air (气中之基础)
**Astrological**: Mars in Gemini (火星入双子座)

**Source Text**:
> "The number Nine, Yesod, brings back the Energy to the central pillar of the Tree of Life. The previous disorder is now rectified. But the general idea of the suit has been constantly degenerating. The Swords no longer represent pure intellect so much as the automatic stirring of heartless passions. Consciousness has fallen into a realm unenlightened by reason... the world of the unconscious primitive instincts, of the psychopath, of the fanatic. The celestial ruler is Mars in Gemini, crude rage of hunger operating without restraint; although its form is intellectual, it is the temper of the inquisitor. ... Nine swords... jagged and rusty. Poison and blood drip from their blades."

**English Paraphrase**:
**Mind turned to Torture** – Corresponds to Yesod (Foundation/Moon) in Air. Energy returns to the central pillar, but the **suit has degenerated**: Swords no longer signify clear intellect, but **automatic, heartless passions**. With **Mars in Gemini**, crude rage, aggression and cruelty take on an intellectual form – the mentality of the inquisitor, fanatic, or psychopath. Nine jagged, rusty swords point downward, dripping poison and blood. This is **Cruelty**: anxiety, obsessive fear, self‑torment, and mental violence toward self or others.

**Core**: **Anxious Torment** – Nightmares, guilt, self‑attack, mental torture, obsessive worry, psychic pain.

**Chinese Explanation**:
**宝剑九（残酷）**对应空气元素中的**Yesod（基础/月亮）**，能量回到生命之树的中柱，却是在一个**已经不断堕落的宝剑体系**中回归。此时，剑不再代表纯粹理性，而是**未经理性照亮的本能冲动与残酷激情**。统治星为**火星入双子座**：攻击性以“智性形式”出现，成为**审判官、狂热者、施虐者的心态**。画面中九把锯齿状、带锈的剑全部向下，剑锋滴着毒液与鲜血，象征心理中那些不断刺痛自己的念头——羞耻、恐惧、内疚、妄想攻击——以及对他人的冷酷评判。这张牌常常指向**失眠、惊恐、强迫性反思、精神折磨**，比外界打击更像是内在对自己的审判。

**In Readings**: Cruelty, anxiety, insomnia, nightmares, self‑blame, obsessive fear, emotional abuse, “worst‑case” thinking.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Nine of Swords shows Yesod but suit has degenerated. Mars in Gemini gives inquisitor mentality. Nine rusty swords drip poison and blood. Heartless passions, not pure intellect.
- **中文**: Crowley的宝剑九展示Yesod但牌组已堕落。火星入双子给予审判官心态。九把锈剑滴着毒液和鲜血。无情激情，而非纯粹理性。

**Narrative Snippets**:
- `[ns_thoth_swords_025]` `[trigger: nine_swords_cruelty]` `[factor_trigger: thoth_swords_nine]` `[role: 主干]` Nine of Swords = Lord of Despair and Cruelty—Yesod; suit degenerated; heartless passions, not intellect. → Core
- `[ns_thoth_swords_026]` `[trigger: mars_gemini_inquisitor]` `[factor_trigger: thoth_swords_nine AND planet_mars_gemini]` `[role: 条件分支]` Mars in Gemini—crude rage in intellectual form; inquisitor, fanatic, psychopath mentality. → Astrological
- `[ns_thoth_swords_027]` `[trigger: rusty_poison_swords]` `[factor_trigger: thoth_swords_nine AND symbol_rusty_swords]` `[role: 条件分支]` Nine jagged rusty swords point down—poison and blood drip; mental violence and self-torment. → Visual"""
    normalized_text_zh: str = """"""
    subject: str = "Nine of Swords: Cruelty (宝剑九：残酷)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_swords_nine_001', 'tarot_mental_torture', 'rel_swords_nine_002', 'tarot_obsessive_anxiety', 'l1_anchor', 'confidence', 'evi_swords_nine_001', 'evi_swords_nine_002', 'tarot_rusty_swords', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_swords_nine_001', 'tarot_swords_nine', 'astro_mars_gemini']
    
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
        book_id="book_of_thoth",
        chapter="",
        l1_anchor="bot_v1.0.0_nine_of_swords__cruelty__宝剑九_残_001_L1",
    )
    version: str = "1.0.0"
