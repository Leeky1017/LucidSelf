"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.007856
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
    semantic_id="lt_v1.0.0_entry_1_1__the_origin_and_natu_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class Entry11TheOriginAndNatu(SemanticEntry):
    """
    **Source Text** (Lines 303-343):
> Years ago, when I told my brother I was studying the tarot, his f...
    """
    
    original_text: str = """**Source Text** (Lines 303-343):
> Years ago, when I told my brother I was studying the tarot, his first comment was, "How can a deck of cards possibly tell you anything about anything?" I laughed because I thought his reply summed up pretty well the commonsense view of the cards. I, too, had my doubts about the tarot, but I found out that the cards can make a real difference in the way you perceive and deal with the challenges in your life...
>
> The origin of the tarot is a mystery. We do know for sure that the cards were used in Italy in the fifteenth century as a popular card game... Later in the eighteenth and nineteenth centuries, the cards were discovered by a number of influential scholars of the occult. These gentlemen were fascinated by the tarot and recognized that the images on the cards were more powerful than a simple game would suggest.

**Key Term Analysis**:
- **Tarot**: `deck of 78 picture cards` / `reveal hidden truths` / `tool for personal growth`
- **Origin mystery**: `15th century Italy` / `popular card game` / `Visconti-Sforza 1450`
- **Occult rediscovery**: `18th-19th century scholars` / `Egyptian mysteries, Hermetic philosophy, Kabbalah`
- **Modern skepticism**: `common sense view` / `scientific establishment condemns`

**English Paraphrase (Primary Language)**:
Tarot's origins are mysterious—documented from 15th century Italy as card game, but occultists later recognized deeper symbolic power. The "commonsense view" dismisses cards as meaningless, yet Bunning argues they "make a real difference" in perceiving life challenges.

Historical development: card game (1450s) → occult tool (18th-19th century) → psychological self-discovery (20th century). Modern interest expanded beyond occultism to include psychology, personal growth, and creative self-exploration.

**Complete Chinese Interpretation (Secondary Language)**:
塔罗的起源是一个谜——有文献记录可追溯至15世纪意大利的纸牌游戏，但神秘学家后来认识到其更深层的象征力量。"常识观点"认为纸牌毫无意义，但Bunning认为它们"确实能改变"人们感知生活挑战的方式。

历史发展：纸牌游戏（1450年代）→ 神秘学工具（18-19世纪）→ 心理自我探索（20世纪）。现代兴趣已超越神秘主义，包括心理学、个人成长和创造性自我探索。

**Core Points**:
- Tarot origins mysterious, documented from 15th century Italy
- Originally card game, later recognized as symbolic system
- Modern tarot = tool for personal growth and insight
- Scientific skepticism exists but doesn't invalidate psychological use

**Narrative Snippets**:
- `[ns_ltt_001]` `[trigger: tarot_origin]` `[factor_trigger: tarot_origin_italy AND tarot_78_system AND mystery AND tarot_system]` `[role: 主干]` The origin of the tarot is a mystery—cards were used in Italy in the fifteenth century as a popular card game. → L308-310
- `[ns_ltt_002]` `[trigger: occult_rediscovery]` `[factor_trigger: tarot_occult AND occult]` `[role: 主干依赖]` Later scholars recognized that the images on the cards were more powerful than a simple game would suggest—connecting them to Egyptian mysteries, Hermetic philosophy, the Kabbalah. → L312-316
- `[ns_ltt_003]` `[trigger: personal_growth]` `[factor_trigger: tarot_growth_tool]` `[role: 总结]` The cards can make a real difference in the way you perceive and deal with the challenges in your life. → L306-307

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: Bunning acknowledges tarot's contested history. The "Egyptian origin" theory (Court de Gébelin, 1781) is now discredited; the Visconti-Sforza deck (c.1450) is the earliest documented complete deck. Modern scholars (Dummett, Kaplan) favor Italian game origin over mystical theories.
- **中文**: Bunning承认塔罗历史有争议。"埃及起源"理论（Court de Gébelin，1781年）现已被否定；Visconti-Sforza牌组（约1450年）是最早有记录的完整牌组。现代学者（Dummett、Kaplan）倾向于意大利游戏起源而非神秘理论。"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 1.1: The Origin and Nature of Tarot"
    factor_refs: list = ['tarot_system', 'arcana', 'occult']
    
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
        l1_anchor="lt_v1.0.0_entry_1_1__the_origin_and_natu_001_L1",
    )
    version: str = "1.0.0"
