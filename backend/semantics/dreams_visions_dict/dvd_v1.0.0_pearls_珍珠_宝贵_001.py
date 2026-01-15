"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.405215
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
    semantic_id="dvd_v1.0.0_pearls_珍珠_宝贵_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Pearls珍珠宝贵(SemanticEntry):
    """
    ### Source Text

> **Pearls**: Since the beginning of time, pearls have been a picture of beauty and...
    """
    
    original_text: str = """### Source Text

> **Pearls**: Since the beginning of time, pearls have been a picture of beauty and wealth—a hidden treasure waiting to be found, bought at great expense. The parable of the businessman who sells all for one pearl speaks of Jesus paying all for the church.
> Negative: Casting pearls before swine means giving precious things to people who do not appreciate them.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Pearls | 珍珠 | 美丽和财富 |
| Treasure | 宝藏 | 隐藏的价值 |
| Expense | 代价 | 付出的价格 |
| Swine | 猪 | 不懂珍惜的人 |

### English Paraphrase

Pearls represent beauty and wealth—hidden treasure bought at great expense. Jesus paid all for the church, His pearl. Casting pearls before swine means giving precious things to those who don't appreciate them.

### Chinese Interpretation

珍珠代表美丽和财富——付出巨大代价买来的隐藏宝藏。耶稣为教会——祂的珍珠——付出了一切。把珍珠丢在猪前意味着把宝贵的东西给不懂珍惜的人。

### Core Points

1. **正负皆可**: 使用方式决定含义
2. **价值象征**: 宝贵的东西
3. **代价记号**: 付出的代价
4. **浪费警告**: 不要给不珍惜的人

### Narrative Snippets

- `[ns_dav_p001]` `[trigger: pearls_treasure]` `[factor_trigger: dream_pearls AND dream_treasure]` `[role: 主干]` Pearls represent hidden treasure bought at great expense—Jesus paid all for the church, His pearl. → 珍珠代表付出巨大代价买来的隐藏宝藏——耶稣为教会——祂的珍珠——付出了一切。
- `[ns_dav_p002]` `[trigger: pearls_swine]` `[factor_trigger: dream_pearls AND dream_swine]` `[role: 警告]` Casting pearls before swine means giving precious things to people who do not appreciate them. → 把珍珠丢在猪前意味着把宝贵的东西给不懂珍惜的人。"""
    normalized_text_zh: str = """"""
    subject: str = "Pearls 珍珠/宝贵"
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
        l1_anchor="dvd_v1.0.0_pearls_珍珠_宝贵_001_L1",
    )
    version: str = "1.0.0"
