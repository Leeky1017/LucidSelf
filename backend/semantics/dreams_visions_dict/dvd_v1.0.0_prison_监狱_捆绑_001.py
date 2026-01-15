"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.405334
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
    semantic_id="dvd_v1.0.0_prison_监狱_捆绑_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Prison监狱捆绑(SemanticEntry):
    """
    ### Source Text

> **Prison**: Being restricted and bound. The only positive interpretation is if th...
    """
    
    original_text: str = """### Source Text

> **Prison**: Being restricted and bound. The only positive interpretation is if the enemy is in it. If Joseph had never gone to prison, he would never have risen to second in command! A tight situation from the Lord prepares you for blessing.
> Negative: A dark prison means the enemy has bound you—he needs license through sin or closed heart. Spiritual imprisonment occurs when someone hides away after hurts.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Prison | 监狱 | 限制和捆绑 |
| Restricted | 被限制 | 无法行动 |
| Joseph | 约瑟 | 监狱预备祝福 |
| Imprisonment | 禁闭 | 属灵的封闭 |

### English Paraphrase

Prison represents restriction and bondage. Positive only if the enemy is imprisoned. Joseph's prison prepared him for promotion! A tight situation from the Lord prepares for blessing. A dark prison means enemy bondage—needing license through sin. Spiritual imprisonment comes from hiding after hurts.

### Chinese Interpretation

监狱代表限制和捆绑。只有当仇敌被关时才是正面的。约瑟的监狱为他预备了晋升！来自主的紧迫处境为祝福做预备。黑暗的监狱意味着仇敌的捆绑——需要通过罪的许可。属灵的禁闭来自伤害后的躲藏。

### Core Points

1. **正负皆可**: 谁被关决定含义
2. **预备象征**: 可能是为祝福预备
3. **约瑟例子**: 监狱带来晋升
4. **捆绑警告**: 可能是仇敌的工作

### Narrative Snippets

- `[ns_dav_p017]` `[trigger: prison_joseph]` `[factor_trigger: dream_prison AND dream_preparation]` `[role: 主干]` If Joseph had never gone to prison, he would never have risen to second in command—preparation! → 如果约瑟从未进过监狱，他就永远不会成为第二把手——这是预备！
- `[ns_dav_p018]` `[trigger: prison_bondage]` `[factor_trigger: dream_prison AND dream_bondage]` `[role: 警告]` A dark prison means the enemy has bound you—he needs license through sin to do this. → 黑暗的监狱意味着仇敌已捆绑你——他需要通过罪的许可才能这样做。"""
    normalized_text_zh: str = """"""
    subject: str = "Prison 监狱/捆绑"
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
        l1_anchor="dvd_v1.0.0_prison_监狱_捆绑_001_L1",
    )
    version: str = "1.0.0"
