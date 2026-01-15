"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.412147
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
    semantic_id="dvd_v1.0.0_field_田地_事工_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Field田地事工(SemanticEntry):
    """
    ### Source Text

> **Field**: A picture of your ministry or area of influence. Can also represent ha...
    """
    
    original_text: str = """### Source Text

> **Field**: A picture of your ministry or area of influence. Can also represent harvest and provision.
> Matthew 13:38 "The field is the world; the good seed are the children of the kingdom."
> Positive: A fruitful field speaks of blessing. Negative: A barren field speaks of curse or neglect.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Field | 田地 | 事工和影响领域 |
| Harvest | 收割 | 成果和丰收 |
| World | 世界 | 福音的禾场 |
| Barren | 荒芜 | 没有果实 |

### English Paraphrase

A field represents your ministry or area of influence—also harvest and provision. The field is the world where good seed is sown. A fruitful field speaks of blessing; a barren field speaks of curse or neglect.

### Chinese Interpretation

田地代表你的事工或影响领域——也象征收割和供应。田地就是世界，好种子撒在其中。多结果的田地象征祝福；荒芜的田地象征咒诅或忽视。

### Core Points

1. **正负皆可**: 田地状态决定含义
2. **事工象征**: 你的服事领域
3. **收割禾场**: 福音和灵魂的收割
4. **荒芜警告**: 可能表示忽视

### Narrative Snippets

- `[ns_dav_f007]` `[trigger: field_harvest]` `[factor_trigger: dream_field AND dream_harvest]` `[role: 主干]` The field is the world—a fruitful field speaks of harvest and blessing in your ministry. → 田地就是世界——多结果的田地象征你事工中的收割和祝福。"""
    normalized_text_zh: str = """"""
    subject: str = "Field 田地/事工"
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
        l1_anchor="dvd_v1.0.0_field_田地_事工_001_L1",
    )
    version: str = "1.0.0"
