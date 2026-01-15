"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.419809
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
    semantic_id="dvd_v1.0.0_cloak_斗篷_遮盖_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Cloak斗篷遮盖(SemanticEntry):
    """
    ### Source Text

> **Cloak**: A covering or mantle. Speaks of spiritual authority and anointing.
> A...
    """
    
    original_text: str = """### Source Text

> **Cloak**: A covering or mantle. Speaks of spiritual authority and anointing.
> A cloak or mantle speaks of a covering and authority. Elijah's mantle represented his prophetic authority which passed to Elisha.
> 2 Kings 2:13 "He took up also the mantle of Elijah that fell from him, and went back, and stood by the bank of Jordan."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Cloak | 斗篷 | 遮盖和权柄 |
| Mantle | 外衣 | 先知的权柄 |
| Authority | 权柄 | 属灵的职分 |
| Anointing | 恩膏 | 神的能力和装备 |

### English Paraphrase

A cloak or mantle represents a covering and spiritual authority. Elijah's mantle symbolized his prophetic authority which passed to Elisha. To receive a cloak in a dream speaks of receiving spiritual authority and anointing.

### Chinese Interpretation

斗篷或外衣代表遮盖和属灵权柄。以利亚的外衣象征他的先知权柄，这权柄传给了以利沙。在梦中接受斗篷象征接受属灵权柄和恩膏。

### Core Points

1. **通常正面**: 代表权柄和恩膏
2. **职分转移**: 外衣可以传递
3. **遮盖象征**: 代表保护和权柄
4. **先知象征**: 特别与先知职分相关

### Narrative Snippets

- `[ns_dav_c031]` `[trigger: cloak_authority]` `[factor_trigger: dream_cloak AND dream_authority]` `[role: 主干]` A cloak or mantle speaks of spiritual authority and anointing—receiving one means receiving a calling. → 斗篷或外衣象征属灵权柄和恩膏——接受它意味着接受呼召。"""
    normalized_text_zh: str = """"""
    subject: str = "Cloak 斗篷/遮盖"
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
        l1_anchor="dvd_v1.0.0_cloak_斗篷_遮盖_001_L1",
    )
    version: str = "1.0.0"
