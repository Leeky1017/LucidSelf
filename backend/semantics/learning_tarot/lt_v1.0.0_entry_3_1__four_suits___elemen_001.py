"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.007928
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
    semantic_id="lt_v1.0.0_entry_3_1__four_suits___elemen_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class Entry31FourSuitsElemen(SemanticEntry):
    """
    **Source Text** (Lines 532-606):
> While the major arcana expresses universal themes, the minor arca...
    """
    
    original_text: str = """**Source Text** (Lines 532-606):
> While the major arcana expresses universal themes, the minor arcana brings those themes down into the practical arena to show how they operate in daily events...
>
> **Wands**: The Wands are the suit of creativity, action, and movement. They are associated with such qualities as enthusiasm, adventure, risk-taking, and confidence. This suit corresponds to the yang, or masculine principle, in Chinese philosophy and is associated with the element Fire.
>
> **Cups**: The Cups are the suit of emotions and spiritual experience. They describe inner states, feelings, and relationship patterns. The energy of this suit flows inward. Cups correspond to the yin, or feminine principle, in Chinese philosophy and are associated with the element Water.
>
> **Swords**: The Swords are the suit of intellect, thought, and reason. They are concerned with justice, truth, and ethical principles. Swords are associated with the element Air... This suit is also associated with states that lead to disharmony and unhappiness.
>
> **Pentacles**: The Pentacles are the suit of practicality, security, and material concerns. They are associated with the element Earth and the concrete requirements of working with matter.

**Key Term Analysis**:
- **Minor Arcana (56)**: `practical arena` / `daily events` / `dramas of everyday lives`
- **Wands (Fire)**: `creativity, action, movement` / `enthusiasm, adventure, risk-taking` / `yang/masculine`
- **Cups (Water)**: `emotions, spiritual experience` / `inner states, feelings, relationships` / `yin/feminine`
- **Swords (Air)**: `intellect, thought, reason` / `justice, truth, ethics` / `disharmony warning`
- **Pentacles (Earth)**: `practicality, security, material` / `concrete requirements` / `prosperity, wealth`

**English Paraphrase (Primary Language)**:
Minor Arcana (56 cards) = how Major Arcana themes "operate in daily events." Four suits correspond to four elements, each governing a life domain:

**Wands (Fire)**: Creativity, action, movement—enthusiasm, adventure, confidence. Yang/masculine energy flowing outward. "A flickering flame is the perfect symbol."

**Cups (Water)**: Emotions, spiritual experience—inner states, feelings, relationships. Yin/feminine energy flowing inward. "The ability of water to flow and fill up spaces."

**Swords (Air)**: Intellect, thought, reason—justice, truth, ethics. Double-edged: "Our intellect is a valuable asset, but as an agent of ego, it can lead us astray." Often associated with conflict and unhappiness.

**Pentacles (Earth)**: Practicality, security, material—physical body, nature, prosperity. Grounded in concrete reality, "the exchange of goods and services."

**Structure**: Each suit has 10 numbered cards (Ace-10) + 4 court cards (Page/Knight/Queen/King) = 14 cards per suit × 4 suits = 56 total.

**Complete Chinese Interpretation (Secondary Language)**:
小阿卡纳（56张牌）= 大阿卡纳主题如何"在日常事件中运作"。四个花色对应四元素，每个管辖一个生活领域：

**权杖（火）**：创造力、行动、运动——热情、冒险、自信。阳性/男性能量向外流动。"闪烁的火焰是完美的象征。"

**圣杯（水）**：情感、灵性体验——内在状态、感受、关系。阴性/女性能量向内流动。"水流动和填充空间的能力。"

**宝剑（风）**：智力、思想、理性——正义、真理、伦理。双刃剑："我们的智力是宝贵资产，但作为自我的代理人，它可能使我们误入歧途。"常与冲突和不幸相关。

**星币（土）**：实用性、安全、物质——身体、自然、繁荣。植根于具体现实，"商品和服务的交换。"

**结构**：每个花色有10张数字牌（A-10）+ 4张宫廷牌（侍从/骑士/王后/国王）= 每花色14张 × 4花色 = 共56张。

**Core Points**:
- Minor Arcana (56) = practical daily manifestation of Major themes
- Four suits = four elements governing life domains
- Wands/Fire: creativity, action, yang, outward
- Cups/Water: emotion, spiritual, yin, inward
- Swords/Air: intellect, truth, conflict potential
- Pentacles/Earth: material, practical, grounded
- Each suit: 10 numbered + 4 court = 14 cards

**Narrative Snippets**:
- `[ns_ltt_014]` `[trigger: minor_practical]` `[factor_trigger: tarot_minor_arcana AND minor_arcana]` `[role: 主干]` The minor arcana brings universal themes into the practical arena—showing how they operate in daily events. → L532-534
- `[ns_ltt_015]` `[trigger: wands_fire]` `[factor_trigger: suit_wands]` `[role: 主干依赖]` Wands are the suit of creativity, action, and movement—associated with Fire, yang energy flowing outward. → L538-543
- `[ns_ltt_016]` `[trigger: cups_water]` `[factor_trigger: suit_cups]` `[role: 主干依赖]` Cups are the suit of emotions and spiritual experience—associated with Water, yin energy flowing inward. → L544-549
- `[ns_ltt_017]` `[trigger: swords_air]` `[factor_trigger: suit_swords]` `[role: 条件分支]` Swords are the suit of intellect and reason—but also associated with disharmony and unhappiness when intellect serves ego. → L550-556
- `[ns_ltt_018]` `[trigger: pentacles_earth]` `[factor_trigger: suit_pentacles]` `[role: 主干依赖]` Pentacles are the suit of practicality and material concerns—associated with Earth, concrete reality. → L557-561
- `[ns_ltt_019]` `[trigger: element_fire]` `[factor_trigger: element_fire]` `[role: 条件分支]` Fire element (Wands): creativity, action, enthusiasm, adventure, risk-taking, confidence—a flickering flame symbolizing will and passion. → L538-543
- `[ns_ltt_020]` `[trigger: element_water]` `[factor_trigger: element_water]` `[role: 条件分支]` Water element (Cups): emotions, spiritual experience, inner states, feelings, relationships—energy flowing inward. → L544-549
- `[ns_ltt_021]` `[trigger: element_air]` `[factor_trigger: element_air]` `[role: 条件分支]` Air element (Swords): intellect, thought, reason, justice, truth, ethics—but also conflict and disharmony potential. → L550-556
- `[ns_ltt_022]` `[trigger: element_earth]` `[factor_trigger: element_earth]` `[role: 条件分支]` Earth element (Pentacles): practicality, security, material concerns—concrete requirements of working with matter. → L557-561

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: The four-element correspondence was formalized by Golden Dawn (late 19th century). Bunning's Wands=Fire follows RWS tradition; some systems (e.g., Crowley's Thoth) assign Wands to Air. The yin-yang correspondence is Bunning's cross-cultural addition. "Swords = disharmony" reflects the suit's reputation for difficult cards.
- **中文**: 四元素对应由金色黎明（19世纪末）正式化。Bunning的权杖=火遵循RWS传统；某些系统（如克劳利的托特）将权杖分配给风。阴阳对应是Bunning的跨文化添加。"宝剑=不和谐"反映该花色因困难牌而闻名。"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 3.1: Four Suits - Elemental Domains"
    factor_refs: list = ['minor_arcana', 'suit_wands', 'suit_cups', 'suit_swords', 'suit_pentacles']
    
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
        l1_anchor="lt_v1.0.0_entry_3_1__four_suits___elemen_001_L1",
    )
    version: str = "1.0.0"
