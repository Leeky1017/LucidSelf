"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.450574
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
    semantic_id="dvd_v1.0.0_honey_蜂蜜_甘甜_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Honey蜂蜜甘甜(SemanticEntry):
    """
    ### Source Text

> **Honey**: Speaks of the sweetness of the Lord, richness, abundance, prosperity a...
    """
    
    original_text: str = """### Source Text

> **Honey**: Speaks of the sweetness of the Lord, richness, abundance, prosperity and luxury. The Lord's nature and presence is likened to honey. Honey is also a picture of knowledge and wisdom.
> Negative: A scroll tasting like honey but bitter in stomach represents the world—sin that tastes sweet for a moment but leaves bitterness.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Honey | 蜂蜜 | 甘甜和丰盛 |
| Sweetness | 甘甜 | 主的性情 |
| Abundance | 丰盛 | 祝福和财富 |
| Wisdom | 智慧 | 知识和见识 |

### English Paraphrase

Honey speaks of the Lord's sweetness, richness, abundance and luxury. God's nature is likened to honey—also representing knowledge and wisdom. Negatively, honey that turns bitter represents the world—sin that tastes sweet but leaves emptiness.

### Chinese Interpretation

蜂蜜象征主的甘甜、丰富、丰盛和奢华。神的性情被比作蜂蜜——也代表知识和智慧。负面而言，变苦的蜂蜜代表世界——罪尝起来甜却留下空虚。

### Core Points

1. **正负皆可**: 蜂蜜结果决定含义
2. **神性象征**: 主的性情和同在
3. **智慧记号**: 知识和智慧
4. **世界警告**: 罪的虚假甘甜

### Narrative Snippets

- `[ns_dav_h012]` `[trigger: honey_lord]` `[factor_trigger: dream_honey AND dream_sweetness]` `[role: 主干]` Honey speaks of the sweetness of the Lord—His nature, richness, abundance and presence. → 蜂蜜象征主的甘甜——祂的性情、丰富、丰盛和同在。
- `[ns_dav_h013]` `[trigger: honey_bitter]` `[factor_trigger: dream_honey AND dream_bitterness]` `[role: 警告]` Sin tastes like honey for a moment but leaves bitterness and emptiness in the heart. → 罪一时尝起来如蜜，但在心中留下苦涩和空虚。"""
    normalized_text_zh: str = """"""
    subject: str = "Honey 蜂蜜/甘甜"
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
        l1_anchor="dvd_v1.0.0_honey_蜂蜜_甘甜_001_L1",
    )
    version: str = "1.0.0"
