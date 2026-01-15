"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.419715
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
    semantic_id="dvd_v1.0.0_car_汽车_事工_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Car汽车事工(SemanticEntry):
    """
    ### Source Text

> **Car**: A representation of your ministry.
> Cars are by far the most common veh...
    """
    
    original_text: str = """### Source Text

> **Car**: A representation of your ministry.
> Cars are by far the most common vehicle seen in dreams. A car from the past could represent circumstances from that time or 'old ministry functions.'
> Positive: Dreaming of a fast sports car means the Lord is leading you into a ministry with bigger realm of influence.
> Negative: Someone else driving your car that represents the flesh, pride or the world system would mean something other than the Lord is in control.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Car | 汽车 | 事工的代表 |
| Ministry | 事工 | 你的属灵服事 |
| Driver | 驾驶者 | 控制事工的人 |
| Vehicle | 载具 | 事工的工具 |

### English Paraphrase

A car represents your ministry—the most common vehicle seen in dreams. A car from the past could represent old ministry functions or past circumstances. Who is driving indicates who is in control. A sports car means a bigger realm of influence; someone else driving (representing flesh/world) means the Lord is not in control.

### Chinese Interpretation

汽车代表你的事工——梦中最常见的载具。过去的车可能代表旧事工功能或过去的境况。谁在驾驶表明谁在掌控。跑车意味着更大的影响力范围；他人驾驶（代表肉体/世界）意味着主不在掌控中。

### Core Points

1. **正负皆可**: 状态和驾驶者决定含义
2. **事工象征**: 最常见的梦中载具
3. **控制者重要**: 谁在驾驶决定事工方向
4. **变化指标**: 车型变化反映事工季节

### Narrative Snippets

- `[ns_dav_c012]` `[trigger: car_ministry]` `[factor_trigger: dream_car AND dream_ministry]` `[role: 主干]` A car represents your ministry—who is driving indicates who is in control of your spiritual life. → 汽车代表事工，驾驶者表明谁在掌控你的属灵生命。
- `[ns_dav_c013]` `[trigger: car_stolen]` `[factor_trigger: dream_car AND dream_stolen]` `[role: 警告]` Having your car stolen, taken over or stopped speaks of your ministry being taken from you. → 车被偷、被接管或停止象征事工被夺走。"""
    normalized_text_zh: str = """"""
    subject: str = "Car 汽车/事工"
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
        l1_anchor="dvd_v1.0.0_car_汽车_事工_001_L1",
    )
    version: str = "1.0.0"
