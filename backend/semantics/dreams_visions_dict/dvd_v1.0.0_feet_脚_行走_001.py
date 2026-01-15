"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.412138
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
    semantic_id="dvd_v1.0.0_feet_脚_行走_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Feet脚行走(SemanticEntry):
    """
    ### Source Text

> **Feet**: A picture of your walk with God and your direction in life.
> Positive:...
    """
    
    original_text: str = """### Source Text

> **Feet**: A picture of your walk with God and your direction in life.
> Positive: Beautiful feet speak of bringing the gospel. Washed feet speak of being cleansed. Bare feet can mean holy ground.
> Negative: Dirty feet speak of contamination. Wounded feet indicate obstacles in your walk.
> Romans 10:15 "How beautiful are the feet of them that preach the gospel of peace."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Feet | 脚 | 行走和方向 |
| Walk | 行走 | 与神同行 |
| Gospel | 福音 | 传扬好消息 |
| Cleansing | 洁净 | 洗脚代表洁净 |

### English Paraphrase

Feet represent your walk with God and life direction. Beautiful feet speak of bringing the gospel. Washed feet mean cleansing. Bare feet may indicate holy ground. Dirty feet speak of contamination, wounded feet of obstacles.

### Chinese Interpretation

脚代表你与神同行和生命方向。美丽的脚象征传福音。洗过的脚意味着洁净。赤脚可能表示圣地。肮脏的脚象征污染，受伤的脚代表障碍。

### Core Points

1. **正负皆可**: 脚的状态决定含义
2. **传道象征**: 美丽的脚传福音
3. **洁净需要**: 洗脚代表洁净
4. **障碍识别**: 受伤的脚代表拦阻

### Narrative Snippets

- `[ns_dav_f005]` `[trigger: feet_gospel]` `[factor_trigger: dream_feet AND dream_gospel]` `[role: 主干]` How beautiful are the feet of them that preach the gospel of peace—bringing good news. → 传和平福音的脚何等佳美——带来好消息。
- `[ns_dav_f006]` `[trigger: feet_dirty]` `[factor_trigger: dream_feet AND dream_dirty]` `[role: 警告]` Dirty feet speak of contamination in your walk—something that has stained your journey. → 肮脏的脚象征行走中的污染——某些东西玷污了你的旅程。"""
    normalized_text_zh: str = """"""
    subject: str = "Feet 脚/行走"
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
        l1_anchor="dvd_v1.0.0_feet_脚_行走_001_L1",
    )
    version: str = "1.0.0"
