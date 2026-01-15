"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.429311
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
    semantic_id="dvd_v1.0.0_jewelry_珠宝_祝福_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Jewelry珠宝祝福(SemanticEntry):
    """
    ### Source Text

> **Jewelry**: All over the world, jewelry speaks of beauty, wealth, blessing and f...
    """
    
    original_text: str = """### Source Text

> **Jewelry**: All over the world, jewelry speaks of beauty, wealth, blessing and favor. It also represents the image you portray to the world. Knowledge is also considered a jewel in Scripture.
> Negative: A jewel in a pig's nose is a fair woman without discretion.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Jewelry | 珠宝 | 美丽和财富 |
| Blessing | 祝福 | 神的恩惠 |
| Knowledge | 知识 | 宝贵的财富 |
| Discretion | 谨慎 | 智慧的选择 |

### English Paraphrase

Jewelry speaks of beauty, wealth, blessing and favor worldwide. It represents your image to the world. Knowledge is also a jewel. Discovering jewels while working speaks of finding valuable things along God's path. A jewel in a pig's nose represents a woman without discretion.

### Chinese Interpretation

珠宝在全世界代表美丽、财富、祝福和恩惠。它代表你向世界呈现的形象。知识也是珠宝。工作时发现珠宝象征在神的道路上发现宝贵的事物。猪鼻子上的珠宝代表没有谨慎的女人。

### Core Points

1. **正负皆可**: 使用方式决定含义
2. **财富象征**: 美丽和祝福
3. **知识珠宝**: 知识如宝石
4. **谨慎警告**: 需要智慧使用

### Narrative Snippets

- `[ns_dav_j004]` `[trigger: jewelry_blessing]` `[factor_trigger: dream_jewelry AND dream_blessing]` `[role: 主干]` Jewelry speaks of beauty, wealth, blessing and favor—representing your image to the world. → 珠宝象征美丽、财富、祝福和恩惠——代表你向世界呈现的形象。"""
    normalized_text_zh: str = """"""
    subject: str = "Jewelry 珠宝/祝福"
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
        l1_anchor="dvd_v1.0.0_jewelry_珠宝_祝福_001_L1",
    )
    version: str = "1.0.0"
