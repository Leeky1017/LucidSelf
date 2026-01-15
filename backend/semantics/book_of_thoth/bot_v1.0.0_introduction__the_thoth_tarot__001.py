"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.044361
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
    semantic_id="bot_v1.0.0_introduction__the_thoth_tarot__001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class IntroductionTheThothTarot(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Thoth Tarot | Crowley-Harris Qabalistic tarot (1938-1943) | Esoteric alternative to RWS |
| Atu | Egyptian-derived term for Major Arcana | 22 paths on Tree of Life |
| True Will | Authentic purpose/destiny in Thelema | Core interpretive lens |
| Tree of Life | Qabalistic diagram of 10 Sephiroth | Structural framework |

**English Paraphrase**:

The **Thoth Tarot**, created by Aleister Crowley and artist Lady Frieda Harris (1938-1943), represents a **Qabalistic-magical interpretation system** deeply rooted in Western esoteric tradition. Unlike the humanistic-psychological approach of the Rider-Waite deck (as refined by Rachel Pollack), the Thoth system emphasizes **initiatory transformation through magical symbolism and Thelemic philosophy**.

**Core Framework - The Tree of Life**:
The 22 Major Arcana (called "Atu" - singular/plural, from Egyptian) correspond to the **22 paths connecting the 10 Sephiroth** on the Qabalistic Tree of Life. Each card represents:
- **Hebrew Letter**: One of 22 letters of sacred alphabet
- **Path Number**: Connection between specific Sephiroth (divine emanations)
- **Astrological Attribution**: Planet, sign, or element
- **Initiatory Experience**: Stage in magical/spiritual development

**Thelemic Philosophy**:
Crowley's system integrates **Thelema** - the philosophy centered on discovering and fulfilling one's **True Will** (authentic purpose/destiny). Key maxim: **"Do what thou wilt shall be the whole of the Law. Love is the law, love under will."** This colors all card interpretations toward self-actualization and magical empowerment.

**Key Differences from Rider-Waite**:
- **Strength (VIII) → Lust (XI)**: Swapped positions, emphasizing primal creative force over moral restraint
- **Justice (XI) → Adjustment (VIII)**: Renamed to reflect dynamic balance vs static judgment
- **Temperance (XIV) → Art (XIV)**: Alchemical transformation emphasized
- **Judgment (XX) → Aeon (XX)**: Cosmic cycle vs personal resurrection
- **More explicit symbolism**: Sexual, magical, and initiatory themes overt rather than veiled

**完整中文诠释**: **透特塔罗**由Aleister Crowley与艺术家Lady Frieda Harris创作（1938-1943），代表深植于西方秘学传统的**卡巴拉-魔法解释系统**。不同于Rider-Waite的人本-心理学方法，透特系统强调**通过魔法象征与泰勒玛哲学的启蒙转化**。核心框架-生命之树：22张大阿尔卡纳（称"Atu"来自埃及语）对应连接10个Sephiroth的**22条路径**。每牌代表：希伯来字母、路径编号、占星对应、启蒙经验。泰勒玛哲学：整合Thelema-围绕发现并实现**真实意志**（真实目的/命运）的哲学。关键格言："依你意愿而行乃全部法则。爱是法则，意志之下的爱。"这为所有牌义染上自我实现与魔法赋权色彩。与Rider-Waite关键差异：力量(VIII)→欲望(XI)交换位置强调原始创造力而非道德约束，正义(XI)→调整(VIII)重命名反映动态平衡vs静态判断，节制(XIV)→艺术(XIV)强调炼金转化，审判(XX)→永劫(XX)宇宙周期vs个人复活，更明确象征：性、魔法、启蒙主题显露而非隐藏。

#### Core Points

- Thoth Tarot is a **Qabalistic-magical interpretation system** rooted in Western esoteric tradition, distinct from the more psychological Rider–Waite approach.
- The 22 Major Arcana ("Atu") correspond to the **22 paths** connecting the 10 Sephiroth on the Tree of Life, each with Hebrew letter, path number, astrological attribution, and initiatory experience.
- **Thelema** and the discovery of **True Will** form the philosophical core that colors all card meanings and directs interpretation toward self-actualization.
- Structural differences from Rider–Waite (Strength→Lust, Justice→Adjustment, Temperance→Art, Judgment→Aeon) highlight a shift from moral judgment to **dynamic balance, creative force, and cosmic cycles**.
- The deck emphasizes **initiatory transformation** through explicit magical, sexual, and mystical symbolism rather than veiled or purely psychological imagery.

#### Detailed Explanation

The Thoth Tarot system integrates Golden Dawn Qabalah, ceremonial magic, and Thelemic philosophy into a single coherent symbolic framework. Rather than presenting isolated images, Crowley and Harris tie each Major Arcana card to a **specific path on the Tree of Life**, assigning it a Hebrew letter, astrological correspondence, and initiatory stage. This means every card operates simultaneously as a pictorial symbol, a Qabalistic path, and a step in spiritual development.

Within this architecture, readings become descriptions of where consciousness is working on the Tree rather than simple fortune-telling. The emphasis on **True Will** shifts interpretation away from external morality toward the question "What is my authentic purpose, and how is this experience serving it?" The deliberate renaming and repositioning of cards (Lust vs Strength, Adjustment vs Justice, Aeon vs Judgment) underline this philosophical move: from static judgment and repression toward **dynamic balance, creative transformation, and participation in larger cosmic cycles**. The result is a deck that demands more esoteric background but offers a deeper initiatory map than conventional Rider–Waite-style systems.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Book of Thoth (1944) remains the authoritative text, though posthumous editions vary in image quality. The VIII/XI swap follows Golden Dawn tradition. Harris's artwork took 5 years (1938-1943) under Crowley's direction. Modern interpretations (DuQuette, Snuffin) provide accessible commentary.
- **中文**: Crowley的《透特之书》（1944）仍是权威文本，尽管遗作版本图像质量不一。VIII/XI互换遵循金色黎明传统。Harris的艺术作品在Crowley指导下历时5年（1938-1943）。现代诠释（DuQuette、Snuffin）提供了易懂的注释。

**Narrative Snippets**:
- `[ns_thoth_001]` `[trigger: thoth_system]` `[factor_trigger: 777_tables AND card_behaviour]` `[role: 主干]` The Thoth Tarot represents a Qabalistic-magical interpretation deeply rooted in Western esoteric tradition, emphasizing initiatory transformation. → English Paraphrase
- `[ns_thoth_002]` `[trigger: 22_atu]` `[factor_trigger: card_interplay AND card_meaning]` `[role: 主干依赖]` The 22 Major Arcana (called "Atu") correspond to the 22 paths connecting the 10 Sephiroth on the Qabalistic Tree of Life. → English Paraphrase
- `[ns_thoth_003]` `[trigger: true_will]` `[factor_trigger: court_cards AND creation]` `[role: 主干依赖]` Crowley's system integrates Thelema—the philosophy centered on discovering and fulfilling one's True Will. → English Paraphrase
- `[ns_thoth_004]` `[trigger: thelemic_maxim]` `[factor_trigger: crystallization AND darkness]` `[role: 总结]` "Do what thou wilt shall be the whole of the Law. Love is the law, love under will."—the key Thelemic maxim coloring all interpretations. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "Introduction: The Thoth Tarot System"
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
        book_id="book_of_thoth",
        chapter="",
        l1_anchor="bot_v1.0.0_introduction__the_thoth_tarot__001_L1",
    )
    version: str = "1.0.0"
