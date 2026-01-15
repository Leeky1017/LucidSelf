"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.419734
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
    semantic_id="dvd_v1.0.0_cattle_牛群_财务_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Cattle牛群财务(SemanticEntry):
    """
    ### Source Text

> **Cattle**: A picture of business and financial blessing.
> Cattle in the Old Tes...
    """
    
    original_text: str = """### Source Text

> **Cattle**: A picture of business and financial blessing.
> Cattle in the Old Testament was a picture of business and trade. Depending on how much cattle you had determined your level of wealth.
> Genesis 13:2 "And Abram was very rich in cattle, in silver, and in gold."
> Negative: To lose your cattle or to see them struck down means there is a curse and the enemy is stealing from you. Fat cattle becoming thin speaks of financial lack and economic downturn.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Cattle | 牛群 | 事业和财务祝福的象征 |
| Business | 事业 | 贸易和生产活动 |
| Wealth | 财富 | 牛群数量决定富裕程度 |
| Curse | 咒诅 | 财务损失的属灵原因 |

### English Paraphrase

Cattle represent business and financial blessing. In the Old Testament, cattle determined wealth level. To receive cattle or see them multiply means business increase and blessing. Losing cattle or seeing them struck down means a curse—the enemy is stealing. Fat cattle becoming thin speaks of financial lack.

### Chinese Interpretation

牛群代表事业和财务祝福。在旧约中，牛群决定财富水平。接受牛群或看见它们增多意味着事业增长和祝福。失去牛群或看见它们被击倒意味着咒诅——仇敌在偷窃。肥牛变瘦象征财务缺乏。

### Core Points

1. **正负皆可**: 牛群状态决定含义
2. **财富指标**: 牛群数量代表富裕程度
3. **祝福应许**: 神要祝福你手中的工作
4. **咒诅警告**: 失去牛群表明仇敌偷窃

### Narrative Snippets

- `[ns_dav_c016]` `[trigger: cattle_blessing]` `[factor_trigger: dream_cattle AND dream_blessing]` `[role: 主干]` Cattle is a picture of business and financial blessing—the Lord wants you to prosper in your workplace. → 牛群象征事业和财务祝福，主要祝福你的工作。
- `[ns_dav_c017]` `[trigger: cattle_curse]` `[factor_trigger: dream_cattle AND dream_curse]` `[role: 警告]` Fat cattle becoming thin speaks of financial lack and economic downturn—a curse is present. → 肥牛变瘦象征财务缺乏和经济衰退，有咒诅临到。"""
    normalized_text_zh: str = """"""
    subject: str = "Cattle 牛群/财务"
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
        book_id="dreams_visions_dict",
        chapter="",
        l1_anchor="dvd_v1.0.0_cattle_牛群_财务_001_L1",
    )
    version: str = "1.0.0"
