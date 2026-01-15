"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.063680
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
    semantic_id="bot_v1.0.0_nine_of_disks__gain__钱币九_获得_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class NineOfDisksGain钱币九获得(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Yesod in Earth | Foundation in Earth | Balance restored |
| Venus in Virgo | Refined enjoyment | Good luck |
| Triangle + Hexagon | 3+6 pattern | Multiplication |
| Degraded Essence | Concrete but less magical | Quantity vs quality |

**Title**: Lord of Material Gain (物质获得之主)
**Qabalistic**: Yesod in Earth (土中之基础)
**Astrological**: Venus in Virgo (金星入处女座)

**Source Text**:
> "The number Nine, Yesod, inevitably brings back the balance of Force in fulfilment. The card is ruled by Venus in Virgo. It shows good luck attending material affairs, favour and popularity. The disks are arranged as an equilateral triangle of three... and... six larger disks in the form of a hexagon. This signifies the multiplication of the original established Word—by the mingling of 'good luck and good management'... the multiplication of a symbol of Energy always tends to degrade its essential meaning..."

**English Paraphrase**:
**Multiplication of Wealth** – Yesod in Earth: balance restored in fulfillment. **Venus in Virgo** brings good luck, favor. Three magical disks (triangle) + six coins (hexagon). **Multiplication** through "luck and management," but with degradation of essence: wealth becomes concrete but less magical. This is **Gain**: increase, prosperity, but risk of losing original purity.

**Core**: **Prosperity & Increase** – Gain, good fortune, material growth, but complexity and potential hollowness.

**Chinese Explanation**:
**钱币九（获得）**对应**Yesod（基础）**：平衡恢复。**金星入处女**带来好运。三魔法盘+六钱币。**倍增**通过"运气与管理"，但削弱本质：财富更具体却失去魔法性。这是**获得**：增长、繁荣，但"更多"未必"更好"。

**In Readings**: Gain, increase, good luck, material success, popularity, but also complexity of accumulation.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Nine of Disks shows Yesod restoring balance. Venus in Virgo brings good luck. Triangle (3) + hexagon (6) pattern. Multiplication through luck and management. Degradation of essence as quantity increases.
- **中文**: Crowley的钱币九展示Yesod恢复平衡。金星入处女带来好运。三角（3）+六边形（6）图案。通过运气与管理倍增。数量增加时本质稀释。

**Narrative Snippets**:
- `[ns_thoth_disks_025]` `[trigger: nine_disks_gain]` `[factor_trigger: thoth_disks_nine]` `[role: 主干]` Nine of Disks = Lord of Material Gain—Yesod restores balance; good luck in material affairs. → Core
- `[ns_thoth_disks_026]` `[trigger: venus_virgo_luck]` `[factor_trigger: thoth_disks_nine AND planet_venus_virgo]` `[role: 条件分支]` Venus in Virgo—refined enjoyment; favor and popularity; good luck + good management. → Astrological
- `[ns_thoth_disks_027]` `[trigger: triangle_hexagon_multiply]` `[factor_trigger: thoth_disks_nine AND symbol_triangle_hexagon]` `[role: 条件分支]` Three magical disks (triangle) + six coins (hexagon)—multiplication but degraded essence. → Visual"""
    normalized_text_zh: str = """"""
    subject: str = "Nine of Disks: Gain (钱币九：获得)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_disks_nine_001', 'tarot_material_multiplication', 'rel_disks_nine_002', 'tarot_quantity_vs_quality', 'l1_anchor', 'confidence', 'evi_disks_nine_001', 'evi_disks_nine_002', 'tarot_degraded_essence', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_disks_nine_001', 'tarot_disks_nine', 'astro_venus_virgo']
    
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
        l1_anchor="bot_v1.0.0_nine_of_disks__gain__钱币九_获得_001_L1",
    )
    version: str = "1.0.0"
