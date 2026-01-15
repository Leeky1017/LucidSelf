"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.052202
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
    semantic_id="bot_v1.0.0_appendix_b__correspondences_ov_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class AppendixBCorrespondencesOv(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Correspondences | Systematic symbol mapping | Integration framework |
| Key Scale | Master attribution table | Reference system |
| 777 | Crowley's correspondence tables | Standard reference |
| Liber DCCLXXVII | "Book 777" | Latin title |

**Source Text**:
> "Note that the Nature of each Decan is shown by the small card attributed to it, and by the symbols given in Liber DCCLXXVII, cols. 149-151."

**English Paraphrase**:

Crowley's **777 Tables** provide the **master key** to Tarot correspondences:

**The Key Scale**:
- **32 Rows**: 10 Sephiroth + 22 Paths
- **Columns**: Multiple symbol systems mapped to each row

**Major Correspondence Categories**:

| Category | Examples |
|----------|----------|
| **Qabalistic** | Hebrew letters, Sephiroth, Paths, Divine Names |
| **Astrological** | Planets, Signs, Houses, Decans |
| **Elemental** | Fire, Water, Air, Earth; Tattvas |
| **Mythological** | Egyptian, Greek, Roman, Hindu gods |
| **Color** | King Scale, Queen Scale, Prince Scale, Princess Scale |
| **Gemstone** | Precious stones per path |
| **Perfume** | Incenses and oils |
| **Magical** | Weapons, practices, formulas |
| **Anatomical** | Body parts |
| **Animal** | Sacred animals |
| **Plant** | Herbs and trees |

**Tarot Specific**:
- **22 Trumps** → 22 Hebrew Letters → 22 Paths
- **4 Suits** → 4 Elements → YHVH
- **10 Pips** → 10 Sephiroth
- **16 Court Cards** → YHVH × 4 Elements
- **36 Small Cards (2-10)** → 36 Decans

**完整中文诠释**：

Crowley的**777表格**提供塔罗对应的**总钥匙**：

**钥匙表**：
- **32行**：10个Sephiroth + 22条路径
- **列**：映射到每行的多个符号系统

**主要对应类别**：

| 类别 | 示例 |
|------|------|
| **卡巴拉** | 希伯来字母、Sephiroth、路径、神圣名字 |
| **占星** | 行星、星座、宫位、旬 |
| **元素** | 火、水、气、土；Tattvas |
| **神话** | 埃及、希腊、罗马、印度神祇 |
| **颜色** | 国王尺度、皇后尺度、王子尺度、公主尺度 |
| **宝石** | 每条路径的宝石 |
| **香料** | 熏香和油 |
| **魔法** | 武器、实践、公式 |
| **解剖** | 身体部位 |
| **动物** | 神圣动物 |
| **植物** | 草药和树木 |

**塔罗专属**：
- **22张大牌** → 22希伯来字母 → 22路径
- **4花色** → 4元素 → YHVH
- **10数字牌** → 10 Sephiroth
- **16宫廷牌** → YHVH × 4元素
- **36小牌（2-10）** → 36旬

#### Core Points

- **777 Tables**: Crowley's "Liber DCCLXXVII" is the **master reference** for all Tarot correspondences.
- **32-row Key Scale**: 10 Sephiroth + 22 Paths = complete framework.
- **Multi-system integration**: Qabalah, astrology, mythology, color, gemstone, perfume, etc.
- **36 Decans**: The 36 small cards (2-10 of each suit) correspond to the 36 zodiacal decans.
- **Four Color Scales**: King (Atziluth), Queen (Briah), Prince (Yetzirah), Princess (Assiah) = four worlds.

**Narrative Snippets**:
- `[ns_thoth_app_007]` `[trigger: 777_tables]` `[factor_trigger: tarot_777 AND tarot_correspondence]` `[role: 主干]` Liber DCCLXXVII (777) provides the master key to all Tarot correspondences through its 32-row Key Scale. → English Paraphrase
- `[ns_thoth_app_008]` `[trigger: decan_cards]` `[factor_trigger: tarot_decan AND tarot_small_cards]` `[role: 主干依赖]` The 36 small cards (2-10 of each suit) correspond to the 36 zodiacal decans as shown in 777. → Source Text
- `[ns_thoth_app_015]` `[trigger: trump_path]` `[factor_trigger: tarot_trump AND tarot_hebrew]` `[role: 条件分支]` 22 Trumps correspond to 22 Hebrew letters and 22 paths on the Tree of Life—the structural backbone of Thoth correspondences. → Trumps
- `[ns_thoth_app_016]` `[trigger: color_scales]` `[factor_trigger: tarot_color AND tarot_four_worlds]` `[role: 条件分支]` Four Color Scales (King/Queen/Prince/Princess) correspond to four Qabalistic worlds: Atziluth, Briah, Yetzirah, Assiah. → Colors"""
    normalized_text_zh: str = """"""
    subject: str = "Appendix B: Correspondences Overview (对应表概览)"
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
        l1_anchor="bot_v1.0.0_appendix_b__correspondences_ov_001_L1",
    )
    version: str = "1.0.0"
