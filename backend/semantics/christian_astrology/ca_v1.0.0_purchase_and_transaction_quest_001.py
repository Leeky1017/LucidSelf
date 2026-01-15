"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.147476
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
    semantic_id="ca_v1.0.0_purchase_and_transaction_quest_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class PurchaseAndTransactionQuest(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------|------------|---------------|
| 4th house | Domus IV | Property, land, real estate | The thing purchased |
| 10th house | Domus X | Price, value | Fair valuation |
| 1st-7th axis | Buyer-Seller | Transaction parties | Agreement dynamics |
| Reception | Receptio | Mutual dignity welcome | Willingness to deal |

**English Paraphrase (Primary Language)**:

**Purchase/Transaction questions** (buying property, goods):

| House | Meaning |
|-------|---------|
| 1st | Buyer (querent) |
| 7th | Seller |
| 4th | Property/land being purchased |
| 10th | Price/value |

**Judgment patterns for purchase**:

| Configuration | Indication |
|--------------|------------|
| L1 applying to L7 with reception | Good deal, agreement |
| L4 well-dignified | Property is valuable/sound |
| L10 strong | Fair price |
| L4 afflicted | Hidden problems with property |
| L7 in 1st house | Seller eager, may get good price |
| Moon separating from L4 | Opportunity passing |

**Complete Chinese Interpretation (Secondary Language)**:

**购买/交易问题**（购置房产、商品）：

| 宫位 | 含义 |
|------|------|
| 第1宫 | 买方（问卜者） |
| 第7宫 | 卖方 |
| 第4宫 | 被购买的房产/土地 |
| 第10宫 | 价格/价值 |

**购买判断模式**：

| 配置 | 指示 |
|------|------|
| L1 有互容趋近 L7 | 好交易、达成协议 |
| L4 有尊贵 | 房产有价值/完好 |
| L10 强 | 公平价格 |
| L4 受克 | 房产有隐藏问题 |
| L7 在第1宫 | 卖方急切，可能得到好价格 |
| 月亮离开 L4 | 机会正在流失 |

**Core Points**:
- 1st-7th for buyer-seller relationship
- 4th = the property/thing itself
- 10th = price/fair value
- Reception indicates willingness

#### Narrative Snippets

- `[ns_lilly_042]` `[trigger: horary_purchase]` `[factor_trigger: horary_4th_property AND astro_item_purchased]` `[role: 主干]` For purchases: 1st house = buyer, 7th house = seller. The 4th house represents the property or thing being purchased. 10th house shows the price. → Christian Astrology Purchase
- `[ns_lilly_043]` `[trigger: purchase_quality]` `[factor_trigger: L4_condition]` `[role: 主干依赖]` L4 dignified = property is valuable and sound; L4 afflicted = hidden problems with the item. L7 in 1st = seller is eager, good bargaining position. → Christian Astrology Purchase
- `[ns_lilly_044]` `[trigger: deal_success]` `[factor_trigger: L1_L7_reception AND astro_deal_success]` `[role: 总结]` L1 applying to L7 with reception = good deal, agreement likely. Moon separating from L4 = opportunity slipping away. → Christian Astrology Purchase

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Property transactions were major life events in 17th-century England. The 4th house for real estate is universal (land, home, endings). The 10th as "price" derives from its opposition to 4th (value of the thing). Lilly's purchase method remains standard for real estate horary. Modern adaptations address mortgages (8th house involvement) and investment properties.
- **中文**: 房产交易在17世纪英国是重大生活事件。第4宫用于不动产是普遍的（土地、家庭、结局）。第10宫作为"价格"源于其与第4宫的对宫（事物的价值）。Lilly的购买方法仍是房产占星的标准。现代改编处理抵押贷款（第8宫参与）和投资房产。"""
    normalized_text_zh: str = """"""
    subject: str = "Purchase and Transaction Questions"
    factor_refs: list = ['house_4_property', 'house_10_price', 'property_quality', 'buyer_seller_reception', 'purchase_opportunity']
    
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
        book_id="christian_astrology",
        chapter="",
        l1_anchor="ca_v1.0.0_purchase_and_transaction_quest_001_L1",
    )
    version: str = "1.0.0"
