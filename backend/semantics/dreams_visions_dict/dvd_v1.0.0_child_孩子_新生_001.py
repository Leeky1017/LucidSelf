"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.419768
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
    semantic_id="dvd_v1.0.0_child_孩子_新生_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Child孩子新生(SemanticEntry):
    """
    ### Source Text

> **Child**: A new birth in the spirit or a new ministry function. Can also represe...
    """
    
    original_text: str = """### Source Text

> **Child**: A new birth in the spirit or a new ministry function. Can also represent spiritual immaturity.
> In dreams, your own children represent the spiritual fruit you have borne. An unknown child speaks of something new the Lord is birthing in you.
> 1 Corinthians 13:11 "When I was a child, I spoke as a child, I understood as a child, I thought as a child."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Child | 孩子 | 新生或属灵果实 |
| New birth | 新生 | 属灵的新开始 |
| Immaturity | 不成熟 | 需要成长的阶段 |
| Ministry | 事工 | 属灵的服事功能 |

### English Paraphrase

A child represents a new birth in the spirit or a new ministry function. Your own children in dreams represent spiritual fruit you have borne. An unknown child speaks of something new the Lord is birthing. Children can also represent immaturity.

### Chinese Interpretation

孩子代表灵里的新生或新的事工功能。梦中自己的孩子代表你所结的属灵果实。不认识的孩子象征主正在你里面孕育的新事物。孩子也可能代表不成熟。

### Core Points

1. **正负皆可**: 上下文决定含义
2. **果实象征**: 自己的孩子代表属灵果实
3. **新事孕育**: 不认识的孩子代表新开始
4. **成熟呼召**: 可能警示需要成长

### Narrative Snippets

- `[ns_dav_c023]` `[trigger: child_newbirth]` `[factor_trigger: dream_child AND dream_newbirth]` `[role: 主干]` An unknown child speaks of something new the Lord is birthing in you spiritually. → 不认识的孩子象征主正在你里面孕育属灵的新事物。
- `[ns_dav_c024]` `[trigger: child_immaturity]` `[factor_trigger: dream_child AND dream_immaturity]` `[role: 警告]` A child can represent spiritual immaturity—the Lord is calling you to grow up. → 孩子可能代表属灵不成熟，主呼召你成长。"""
    normalized_text_zh: str = """"""
    subject: str = "Child 孩子/新生"
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
        l1_anchor="dvd_v1.0.0_child_孩子_新生_001_L1",
    )
    version: str = "1.0.0"
