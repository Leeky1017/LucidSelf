"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.535870
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
    semantic_id="acu_v1.0.0_283__比小更小_比大更大_的悖论_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 283比小更小比大更大的悖论(SemanticEntry):
    """
    **原文** (¶283, 行4751-4757):

> [283] The motif of "smaller than small yet bigger than big" complement...
    """
    
    original_text: str = """**原文** (¶283, 行4751-4757):

> [283] The motif of "smaller than small yet bigger than big" complements the impotence of the child by means of its equally miraculous deeds. This paradox is the essence of the hero and runs through his whole destiny like a red thread. He can cope with the greatest perils, yet, in the end, something quite insignificant is his undoing: Baldur perishes because of the mistletoe, Maui because of the laughter of a little bird, Siegfried because of his one vulnerable spot, Heracles because of his wife's gift, others because of common treachery, and so on.

**英文释义（主语言）**:

**"比小更小，比大更大"母题**：
通过同样奇迹的行为补充了童子的无能。

**悖论是英雄的本质**：
这个悖论贯穿英雄的整个命运如一条红线。

**英雄的命运模式**：
他能应对最大的危险，但最终，某个完全微不足道的东西成为他的毁灭：
- 巴尔德尔因槲寄生而死
- 毛伊因小鸟的笑声而死
- 齐格弗里德因唯一的弱点而死
- 赫拉克勒斯因妻子的礼物而死
- 其他人因普通背叛而死

**完整中文诠释（次语言）**:

**"比小更小，比大更大"母题的功能**：
"比小更小，比大更大"的母题通过同样奇迹的行为补充了童子的无能。

**悖论贯穿英雄命运**：
这个悖论是英雄的本质，贯穿他的整个命运如一条红线。

**英雄命运的典型模式**：
英雄能应对最大的危险，但最终，某个完全微不足道的东西成为他的毁灭：
- **巴尔德尔**因槲寄生而死
- **毛伊**因小鸟的笑声而死
- **齐格弗里德**因唯一的弱点而死
- **赫拉克勒斯**因妻子的礼物而死
- 其他人因普通背叛而死

这种模式说明了悖论的普遍性：最强大者被最微小者击败。

**核心要点**:
- "比小更小，比大更大" = 补充童子无能的奇迹行为
- 悖论 = 英雄的本质
- 模式：能应对最大危险，却被微不足道之物毁灭
- 例证：巴尔德尔、毛伊、齐格弗里德、赫拉克勒斯

**叙事片段**:
- `[ns_cw9i_IV_283_001]` `[trigger: smaller_bigger_paradox]` `[factor_trigger: jung_hero AND jung_paradox]` `[role: 主干]` "比小更小，比大更大"悖论是英雄本质——能应对最大危险，却被微不足道之物毁灭。→ ¶283"""
    normalized_text_zh: str = """"""
    subject: str = "¶283 "比小更小，比大更大"的悖论"
    factor_refs: list = ['engine_id', 'smaller_bigger', 'psych_semantic', 'hero_undoing', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_283__比小更小_比大更大_的悖论_001_L1",
    )
    version: str = "1.0.0"
