"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.402070
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
    semantic_id="dvd_v1.0.0_dove_鸽子_圣灵_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Dove鸽子圣灵(SemanticEntry):
    """
    ### Source Text

> **Dove**: A depiction of the Holy Spirit. A symbol of peace and promise.
> The Ho...
    """
    
    original_text: str = """### Source Text

> **Dove**: A depiction of the Holy Spirit. A symbol of peace and promise.
> The Holy Spirit is often represented as a Dove in Scripture. Noah also used the dove when seeing if there was dry land. Because of its timid nature, a dove speaks of peace—easily unsettled. If you see a dove flying away in a meeting, it means the Holy Spirit has left.
> John 1:32 "And John bore record, saying, I saw the Spirit descending from heaven like a dove."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Dove | 鸽子 | 圣灵的象征 |
| Holy Spirit | 圣灵 | 神的灵 |
| Peace | 和平 | 温柔的性情 |
| Promise | 应许 | 神即将成就的事 |

### English Paraphrase

A dove represents the Holy Spirit—a symbol of peace and promise. Noah used a dove to find dry land—a promise the Lord is about to fulfill. The dove is timid and easily unsettled. If a dove flies away, the Holy Spirit has left, often when leadership doesn't obey His prompting.

### Chinese Interpretation

鸽子代表圣灵——和平和应许的象征。挪亚用鸽子寻找干地——主即将成就的应许。鸽子胆小，容易受惊。如果鸽子飞走，表示圣灵已离开，通常是领导层没有顺从祂的提醒。

### Core Points

1. **通常正面**: 圣灵的美好象征
2. **和平象征**: 温柔容易受惊的性情
3. **应许记号**: 神即将成就的事
4. **离开警告**: 可能表示圣灵被驱赶

### Narrative Snippets

- `[ns_dav_d024]` `[trigger: dove_spirit]` `[factor_trigger: dream_dove AND dream_spirit]` `[role: 主干]` A dove represents the Holy Spirit—a symbol of peace and a promise the Lord is about to fulfill. → 鸽子代表圣灵——和平的象征和主即将成就的应许。
- `[ns_dav_d025]` `[trigger: dove_leave]` `[factor_trigger: dream_dove AND dream_departure]` `[role: 警告]` If you see a dove flying away, it means the Holy Spirit has left—often when leadership disobeys. → 如果你看见鸽子飞走，表示圣灵已离开——通常是领导层不顺服时。"""
    normalized_text_zh: str = """"""
    subject: str = "Dove 鸽子/圣灵"
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
        l1_anchor="dvd_v1.0.0_dove_鸽子_圣灵_001_L1",
    )
    version: str = "1.0.0"
