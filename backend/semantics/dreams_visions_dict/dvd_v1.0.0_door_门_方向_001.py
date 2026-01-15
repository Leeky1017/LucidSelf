"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.402061
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
    semantic_id="dvd_v1.0.0_door_门_方向_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Door门方向(SemanticEntry):
    """
    ### Source Text

> **Door**: A new direction in your life or one that has passed. A gate, path, door...
    """
    
    original_text: str = """### Source Text

> **Door**: A new direction in your life or one that has passed. A gate, path, door or fence opening all speak of a new direction or one that has passed.
> I often see a door or gate in the spirit when releasing someone into something new. If I see an open door, the way is clear. If closed, we need to pray and open it, or something is blocking them.
> 1 Corinthians 16:9 "...a great door for effective work has opened to me, and there are many who oppose me."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Door | 门 | 新的方向 |
| Open | 敞开 | 道路通畅 |
| Closed | 关闭 | 需要祷告或有阻挡 |
| Direction | 方向 | 人生的新计划 |

### English Paraphrase

A door represents a new direction or one that has passed. An open door means the way is clear—a new plan from the Lord. A closed door either needs prayer to open or indicates something blocking. Negative doors refer to open doors to the demonic realm.

### Chinese Interpretation

门代表新的方向或已过去的方向。敞开的门意味着道路通畅——来自主的新计划。关闭的门要么需要祷告来开启，要么表示有阻挡。负面的门指向邪灵领域敞开的门。

### Core Points

1. **正负皆可**: 门的状态决定含义
2. **新方向**: 主带领进入新事物
3. **阻挡识别**: 关闭的门需要辨别原因
4. **邪灵敞开门**: 可能表示生命中的破口

### Narrative Snippets

- `[ns_dav_d022]` `[trigger: door_open]` `[factor_trigger: dream_door AND dream_open]` `[role: 主干]` An open door means the way is clear—the Lord is leading you into something new. → 敞开的门意味着道路通畅——主正带领你进入新事物。
- `[ns_dav_d023]` `[trigger: door_demonic]` `[factor_trigger: dream_door AND dream_demonic]` `[role: 警告]` Most negative doors refer to an open door to the demonic realm—given license through sin. → 大多数负面的门指向邪灵领域敞开的门——因罪而给予许可。"""
    normalized_text_zh: str = """"""
    subject: str = "Door 门/方向"
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
        l1_anchor="dvd_v1.0.0_door_门_方向_001_L1",
    )
    version: str = "1.0.0"
