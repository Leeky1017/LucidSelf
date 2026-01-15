"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.419899
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
    semantic_id="dvd_v1.0.0_cords_绳索_联结_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Cords绳索联结(SemanticEntry):
    """
    ### Source Text

> **Cords**: Cords are a lot like chains, they speak of bondage and restriction. Ho...
    """
    
    original_text: str = """### Source Text

> **Cords**: Cords are a lot like chains, they speak of bondage and restriction. However they can also refer to the cord or bond of marriage.
> Positive: When a couple commits themselves, they are bound together as one—the covenant bond.
> Negative: In families the cord is temporary. We have seen a cord in the spirit attached to a person's first love preventing them from uniting with their spouse.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Cords | 绳索 | 联结或捆绑 |
| Bond | 联结 | 关系的纽带 |
| Marriage | 婚姻 | 合法的联结 |
| Bondage | 捆绑 | 不健康的依附 |

### English Paraphrase

Cords are like chains speaking of bondage, but also the bond of marriage. When a couple commits, they are bound as one—a covenant bond. Negatively, cords to first loves or past mentors can prevent healthy relationships. These bondages need to be broken.

### Chinese Interpretation

绳索像锁链一样代表捆绑，但也可指婚姻的联结。当夫妻委身时，他们被联结为一——盟约的联结。负面而言，与初恋或过去导师的绳索可能阻碍健康的关系。这些捆绑需要被打破。

### Core Points

1. **正负皆可**: 联结性质决定含义
2. **婚姻联结**: 合法的盟约纽带
3. **不健康依附**: 与过去的人或事不当联结
4. **需要断开**: 错误的绳索需要被剪断

### Narrative Snippets

- `[ns_dav_c043]` `[trigger: cords_marriage]` `[factor_trigger: dream_cords AND dream_marriage]` `[role: 正面]` The cord of marriage speaks of the covenant bond—two becoming one. → 婚姻的绳索象征盟约的联结——二人成为一体。
- `[ns_dav_c044]` `[trigger: cords_bondage]` `[factor_trigger: dream_cords AND dream_bondage]` `[role: 警告]` Cords to first loves or past mentors can prevent healthy relationships—these need to be broken. → 与初恋或过去导师的绳索可能阻碍健康的关系——这些需要被断开。"""
    normalized_text_zh: str = """"""
    subject: str = "Cords 绳索/联结"
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
        l1_anchor="dvd_v1.0.0_cords_绳索_联结_001_L1",
    )
    version: str = "1.0.0"
