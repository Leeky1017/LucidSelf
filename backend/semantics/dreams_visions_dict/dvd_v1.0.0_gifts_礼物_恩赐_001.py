"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.390669
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
    semantic_id="dvd_v1.0.0_gifts_礼物_恩赐_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Gifts礼物恩赐(SemanticEntry):
    """
    ### Source Text

> **Gifts**: A picture of spiritual gifts and abilities being imparted.
> Positive:...
    """
    
    original_text: str = """### Source Text

> **Gifts**: A picture of spiritual gifts and abilities being imparted.
> Positive: Receiving a gift speaks of receiving something from the Lord—a spiritual ability or blessing. Wrapped gifts indicate blessings yet to be revealed. Giving gifts speaks of ministry and generosity.
> Negative: A gift with strings attached indicates manipulation. Rejecting a gift means refusing blessing.
> Romans 12:6 "Having then gifts differing according to the grace that is given to us..."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Gifts | 礼物 | 恩赐和祝福 |
| Spiritual gifts | 属灵恩赐 | 从神来的能力 |
| Impart | 传递 | 赐予能力 |
| Blessing | 祝福 | 神的恩惠 |

### English Paraphrase

Gifts represent spiritual gifts and abilities being imparted. Receiving a gift speaks of receiving from the Lord—a spiritual ability or blessing. Wrapped gifts indicate blessings yet to be revealed. Giving gifts speaks of ministry. A gift with strings attached indicates manipulation.

### Chinese Interpretation

礼物代表属灵恩赐和能力的传递。接受礼物象征从主那里得到——属灵能力或祝福。包装的礼物表示尚未揭示的祝福。给予礼物象征服事。有条件的礼物表示操控。

### Core Points

1. **正负皆可**: 礼物性质决定含义
2. **恩赐传递**: 从主接受能力
3. **尚未揭示**: 包装的礼物待展开
4. **操控警告**: 有条件的礼物是操控

### Narrative Snippets

- `[ns_dav_g003]` `[trigger: gifts_receive]` `[factor_trigger: dream_gifts AND dream_receive]` `[role: 主干]` Receiving a gift speaks of receiving something from the Lord—a spiritual ability or blessing. → 接受礼物象征从主那里得到——属灵能力或祝福。
- `[ns_dav_g004]` `[trigger: gifts_strings]` `[factor_trigger: dream_gifts AND dream_manipulation]` `[role: 警告]` A gift with strings attached indicates manipulation—not a true blessing from the Lord. → 有条件的礼物表示操控——不是从主来的真祝福。"""
    normalized_text_zh: str = """"""
    subject: str = "Gifts 礼物/恩赐"
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
        l1_anchor="dvd_v1.0.0_gifts_礼物_恩赐_001_L1",
    )
    version: str = "1.0.0"
