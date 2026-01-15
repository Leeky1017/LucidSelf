"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.405351
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
    semantic_id="dvd_v1.0.0_purple_紫色_王权_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Purple紫色王权(SemanticEntry):
    """
    ### Source Text

> **Purple**: In Scripture purple always has a positive connotation—royalty, wealth...
    """
    
    original_text: str = """### Source Text

> **Purple**: In Scripture purple always has a positive connotation—royalty, wealth and prosperity. In the Old Testament only the wealthy could afford purple clothing, worn by kings. Purple was used in the tabernacle, representing the deity of the Lord.
> Negative: Purple like blue can speak of bruising and hurts.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Purple | 紫色 | 王权和财富 |
| Royalty | 王权 | 君王的颜色 |
| Wealth | 财富 | 富贵的象征 |
| Bruising | 瘀伤 | 伤害的颜色 |

### English Paraphrase

Purple in Scripture has positive connotation—royalty, wealth and prosperity. Only the wealthy could afford purple, worn by kings. Purple in the tabernacle represented the Lord's deity. Negatively, purple like blue can speak of bruising and hurts.

### Chinese Interpretation

紫色在圣经中有正面含义——王权、财富和昌盛。只有富人买得起紫色，由君王穿戴。会幕中的紫色代表主的神性。负面而言，紫色像蓝色可以象征瘀伤和伤害。

### Core Points

1. **通常正面**: 紫色通常代表王权
2. **财富象征**: 只有富人能穿
3. **神性记号**: 会幕中的颜色
4. **伤害警告**: 可能代表瘀伤

### Narrative Snippets

- `[ns_dav_p021]` `[trigger: purple_royal]` `[factor_trigger: dream_purple AND dream_royalty]` `[role: 主干]` Purple always has positive connotation in Scripture—royalty, wealth and prosperity. → 紫色在圣经中总是有正面含义——王权、财富和昌盛。"""
    normalized_text_zh: str = """"""
    subject: str = "Purple 紫色/王权"
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
        l1_anchor="dvd_v1.0.0_purple_紫色_王权_001_L1",
    )
    version: str = "1.0.0"
