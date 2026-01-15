"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.063819
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
    semantic_id="bot_v1.0.0_princess_of_disks__钱币公主_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class PrincessOfDisks钱币公主(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Earth of Earth | Densest matter | Transfiguration brink |
| Diamond Scepter | Kether in darkness | Highest in lowest |
| Demeter Priestess | Grain goddess | Fertility mystery |
| Twin Spiral | Chinese creation | Perfect equilibrium |

**Title**: Princess of the Echoing Hills, Rose of the Palace of Earth (回响山丘公主，土之宫殿之玫瑰)
**Elemental**: The Earthy part of Earth (土中之土)
**Rule**: Quadrant around North Pole (北极周围象限)

**Source Text**:
> "The Princess of Disks, the last of the Court cards, represents the earthy part of Earth. She is consequently on the brink of transfiguration. She is strong and beautiful, with an expression of intense brooding, as if about to become aware of secret wonder. Her crest is the head of the ram, and her sceptre descends into the earth. There its head becomes a diamond, the precious stone of Kether, thus symbolizing the birth of the highest and purest light in the deepest and darkest of the Elements. She stands within a grove of sacred trees before an altar suggesting a wheatsheaf, for she is a priestess of Demeter. She bears within her body the secret of the future. Her sublimity is further emphasized by the disk which she bears; for in the centre thereof is the Chinese ideogram denoting the twin spiral force of Creation in perfect equilibrium; from this is born the rose of Isis, the great fertile Mother... She is Womanhood in its ultimate projection... every turn of the wheel is equally probable, and equally a prize; for every Event is 'a play of Nuit'."

**English Paraphrase**:
**Earth's Transfiguration** – **Earth of Earth**: the last court card, on the **brink of transfiguration**. Strong, beautiful, intensely brooding, about to awaken to secret wonder. Ram-head crest; scepter descends into earth, tip becoming **diamond** (Kether's stone) – the **highest light born in deepest darkness**. Stands in sacred grove before wheatsheaf altar: **priestess of Demeter**. Bears the secret of the future. Disk shows Chinese ideogram of **twin spiral Creation** in equilibrium, birthing the **rose of Isis**, the great Mother. She is **Womanhood in ultimate projection**: all characteristics potential, manifesting according to circumstance – bewilderingly inconsistent, yet each quality pure. Every Event is "a play of Nuit."

**Core**: **Potentiality & Pregnancy** – The seed, the future, womanhood, fertile mystery, all possibilities, transfiguration.

**Chinese Explanation**:
**钱币公主**代表**土中之土**：最后一张宫廷牌，处于**蜕变的边缘**。强壮美丽，深沉凝思，仿佛即将觉察到秘密奇迹。**公羊头**顶饰；权杖向下插入大地，尖端化为**钻石**（Kether 之石）——**最高之光诞生于最深最暗的元素中**。站在圣树林中的麦穗祭坛前：**得墨忒耳的女祭司**。体内怀着未来的秘密。圆盘中心是中国**双螺旋创造**理念图（完美平衡），由此诞生**伊西斯玫瑰**，伟大的生育之母。她是**终极投射的女性**：一切特质皆为潜能，依情境显化——令人困惑地矛盾，却每种品质都纯粹。每个事件都是"努特的游戏"。

**In Readings**: Young woman full of potential, pregnancy (literal or symbolic), new beginnings in material world, secret wonder, bewildering inconsistency, pure potentiality.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Princess of Disks is Earth of Earth - on brink of transfiguration. Ram-head crest, diamond scepter (Kether in deepest darkness). Priestess of Demeter. Twin spiral disk births rose of Isis. Womanhood in ultimate projection.
- **中文**: Crowley的钱币公主是土中之土—处于蜕变边缘。公羊头顶饰，钻石权杖（Kether在最深黑暗中）。得墨徽尔的女祭司。双螺旋圆盘诞生伊西斯玫瑰。女性的终极投射。

**Narrative Snippets**:
- `[ns_thoth_disks_040]` `[trigger: princess_disks_thoth]` `[factor_trigger: thoth_disks_princess]` `[role: 主干]` Princess of Disks = Earth of Earth—last court card; on brink of transfiguration; secret wonder. → Core
- `[ns_thoth_disks_041]` `[trigger: diamond_demeter]` `[factor_trigger: thoth_disks_princess AND symbol_diamond]` `[role: 条件分支]` Diamond scepter (Kether in deepest darkness); priestess of Demeter; wheatsheaf altar. → Visual
- `[ns_thoth_disks_042]` `[trigger: twin_spiral_isis]` `[factor_trigger: thoth_disks_princess AND symbol_spiral]` `[role: 条件分支]` Twin spiral Creation in equilibrium births rose of Isis; Womanhood in ultimate projection. → Symbolism"""
    normalized_text_zh: str = """"""
    subject: str = "Princess of Disks (钱币公主)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_princess_disks_earth', 'earth_of_earth', 'rel_princess_disks_kether', 'diamond', 'princess_disks_potential']
    
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
        l1_anchor="bot_v1.0.0_princess_of_disks__钱币公主_001_L1",
    )
    version: str = "1.0.0"
