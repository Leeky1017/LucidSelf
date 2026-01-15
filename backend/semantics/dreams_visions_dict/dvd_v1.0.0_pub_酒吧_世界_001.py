"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.405343
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
    semantic_id="dvd_v1.0.0_pub_酒吧_世界_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Pub酒吧世界(SemanticEntry):
    """
    ### Source Text

> **Pub**: A picture of the world's solution to a spiritual need. If dreaming of be...
    """
    
    original_text: str = """### Source Text

> **Pub**: A picture of the world's solution to a spiritual need. If dreaming of being in a pub and finding people, the Lord is calling you to evangelism—go into the world and reach the lost.
> Negative: Getting drunk in a pub means using the world to satisfy a deep spiritual need—escaping into the world instead of the Lord's presence.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Pub | 酒吧 | 世界的解决 |
| World | 世界 | 属世的满足 |
| Evangelism | 传福音 | 接触失丧的人 |
| Escape | 逃避 | 不进入主的同在 |

### English Paraphrase

A pub pictures the world's solution to spiritual need. Finding people in a pub means the Lord is calling you to evangelism—reach the lost in the world. Getting drunk means using the world to satisfy spiritual need—escaping into the world instead of the Lord's presence.

### Chinese Interpretation

酒吧象征世界对属灵需要的解决方案。在酒吧找到人意味着主呼召你传福音——在世界中接触失丧的人。喝醉意味着用世界满足属灵需要——逃进世界而不是主的同在。

### Core Points

1. **正负皆可**: 行动决定含义
2. **世界象征**: 属世的满足
3. **传福音呼召**: 接触失丧的人
4. **逃避警告**: 用世界代替神

### Narrative Snippets

- `[ns_dav_p019]` `[trigger: pub_evangelism]` `[factor_trigger: dream_pub AND dream_evangelism]` `[role: 主干]` Being in a pub finding people means the Lord is calling you to evangelism—reach the lost. → 在酒吧找到人意味着主呼召你传福音——接触失丧的人。
- `[ns_dav_p020]` `[trigger: pub_escape]` `[factor_trigger: dream_pub AND dream_escape]` `[role: 警告]` Getting drunk in a pub means using the world to satisfy spiritual need—escaping instead of seeking the Lord. → 在酒吧喝醉意味着用世界满足属灵需要——逃避而不是寻求主。"""
    normalized_text_zh: str = """"""
    subject: str = "Pub 酒吧/世界"
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
        l1_anchor="dvd_v1.0.0_pub_酒吧_世界_001_L1",
    )
    version: str = "1.0.0"
