"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.443901
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
    semantic_id="dvd_v1.0.0_lamp_灯_启示_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Lamp灯启示(SemanticEntry):
    """
    ### Source Text

> **Lamp**: A source of revelation. A lamp reveals the road just ahead of you—the r...
    """
    
    original_text: str = """### Source Text

> **Lamp**: A source of revelation. A lamp reveals the road just ahead of you—the revelation and direction of the Lord. The Lord will show you just the next step and you must trust Him for the rest.
> Positive: Your word is a lamp to my feet—lighting the path one step at a time.
> Negative: A lamp gone out speaks of passion and love for the Lord going out. A dim lamp means not feeding your spirit correctly.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Lamp | 灯 | 启示的来源 |
| Revelation | 启示 | 神的指引 |
| Direction | 方向 | 前方的道路 |
| Dim | 暗淡 | 没有喂养灵 |

### English Paraphrase

A lamp is a source of revelation—lighting the road just ahead, showing the next step. You must trust the Lord for the rest. A lamp gone out speaks of passion for the Lord fading. A dim lamp means not feeding your spirit with the right things.

### Chinese Interpretation

灯是启示的来源——照亮前方的路，显示下一步。你必须信靠主走其余的路。熄灭的灯象征对主的热情消退。暗淡的灯意味着没有用正确的事物喂养你的灵。

### Core Points

1. **正负皆可**: 灯的状态决定含义
2. **启示象征**: 神话语的光
3. **一步一步**: 主只显示下一步
4. **熄灭警告**: 热情消退需警惕

### Narrative Snippets

- `[ns_dav_l005]` `[trigger: lamp_word]` `[factor_trigger: dream_lamp AND dream_word]` `[role: 主干]` Your word is a lamp to my feet—the Lord shows you just the next step to take. → 你的话是我脚前的灯——主只向你显示要走的下一步。
- `[ns_dav_l006]` `[trigger: lamp_dim]` `[factor_trigger: dream_lamp AND dream_dim]` `[role: 警告]` A dim lamp means you are not feeding your spirit with the correct things. → 暗淡的灯意味着你没有用正确的事物喂养你的灵。"""
    normalized_text_zh: str = """"""
    subject: str = "Lamp 灯/启示"
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
        l1_anchor="dvd_v1.0.0_lamp_灯_启示_001_L1",
    )
    version: str = "1.0.0"
