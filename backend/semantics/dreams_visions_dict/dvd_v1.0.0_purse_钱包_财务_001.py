"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.405360
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
    semantic_id="dvd_v1.0.0_purse_钱包_财务_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Purse钱包财务(SemanticEntry):
    """
    ### Source Text

> **Purse/Wallet**: A picture of financial provision or lack. A purse being filled ...
    """
    
    original_text: str = """### Source Text

> **Purse/Wallet**: A picture of financial provision or lack. A purse being filled speaks of blessing and provision. A filled purse in the spirit speaks of financial provision—release it and speak it into the earth.
> Negative: An empty wallet speaks of lack and curse. A purse with holes speaks of a curse—have you stopped sowing into the Lord's work?

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Purse | 钱包 | 财务状况 |
| Provision | 供应 | 被满足的需要 |
| Empty | 空的 | 缺乏和咒诅 |
| Holes | 漏洞 | 财务流失 |

### English Paraphrase

A purse pictures financial provision or lack. A filled purse speaks of blessing and provision—release it into the earth. An empty wallet speaks of lack and curse. A purse with holes speaks of a curse—have you stopped sowing into the Lord's work?

### Chinese Interpretation

钱包象征财务供应或缺乏。满的钱包象征祝福和供应——释放它进入地上。空的钱包象征缺乏和咒诅。有漏洞的钱包象征咒诅——你是否停止了向主的工作撒种？

### Core Points

1. **正负皆可**: 钱包状态决定含义
2. **供应象征**: 财务的满足
3. **缺乏警告**: 空的是咒诅
4. **漏洞警告**: 财务流失

### Narrative Snippets

- `[ns_dav_p022]` `[trigger: purse_filled]` `[factor_trigger: dream_purse AND dream_blessing]` `[role: 主干]` A purse being filled speaks of blessing and financial provision from the Lord. → 被填满的钱包象征祝福和来自主的财务供应。
- `[ns_dav_p023]` `[trigger: purse_holes]` `[factor_trigger: dream_purse AND dream_curse]` `[role: 警告]` A purse with holes speaks of a curse—have you stopped sowing into the Lord's work? → 有漏洞的钱包象征咒诅——你是否停止了向主的工作撒种？"""
    normalized_text_zh: str = """"""
    subject: str = "Purse 钱包/财务"
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
        l1_anchor="dvd_v1.0.0_purse_钱包_财务_001_L1",
    )
    version: str = "1.0.0"
