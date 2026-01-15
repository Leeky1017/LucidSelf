"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.412180
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
    semantic_id="dvd_v1.0.0_fleas_跳蚤_烦扰_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Fleas跳蚤烦扰(SemanticEntry):
    """
    ### Source Text

> **Fleas**: A picture of minor irritations and annoyances that distract you from w...
    """
    
    original_text: str = """### Source Text

> **Fleas**: A picture of minor irritations and annoyances that distract you from what is important.
> Fleas are small but cause great discomfort. In your spiritual life, fleas represent little things that irritate and distract you. If left unchecked, they multiply quickly.
> Negative: Fleas always have a negative connotation—they are pests that need to be dealt with.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Fleas | 跳蚤 | 小烦扰 |
| Irritation | 烦恼 | 分散注意力的事 |
| Distraction | 分心 | 离开重要的事 |
| Pest | 害虫 | 需要处理的问题 |

### English Paraphrase

Fleas represent minor irritations and annoyances that distract from what is important. Small but causing great discomfort, they represent little things that irritate. If unchecked, they multiply quickly. Fleas always have negative connotation—pests needing to be dealt with.

### Chinese Interpretation

跳蚤代表使你分心偏离重要事物的小烦扰和困扰。虽小但造成极大不适，它们代表令人烦恼的小事。若不处理，很快繁殖。跳蚤总是负面的——需要处理的害虫。

### Core Points

1. **始终负面**: 跳蚤没有正面含义
2. **小事烦扰**: 分散注意力的琐事
3. **快速繁殖**: 若不处理会恶化
4. **需要对付**: 必须及时处理

### Narrative Snippets

- `[ns_dav_f013]` `[trigger: fleas_irritation]` `[factor_trigger: dream_fleas AND dream_irritation]` `[role: 警告]` Fleas represent minor irritations that distract you—small but multiplying quickly if unchecked. → 跳蚤代表使你分心的小烦扰——虽小但若不处理很快繁殖。"""
    normalized_text_zh: str = """"""
    subject: str = "Fleas 跳蚤/烦扰"
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
        l1_anchor="dvd_v1.0.0_fleas_跳蚤_烦扰_001_L1",
    )
    version: str = "1.0.0"
