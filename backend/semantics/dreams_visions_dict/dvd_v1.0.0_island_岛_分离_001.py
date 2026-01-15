"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.429276
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
    semantic_id="dvd_v1.0.0_island_岛_分离_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Island岛分离(SemanticEntry):
    """
    ### Source Text

> **Island**: The picture of being separated and cut off from others.
> Positive: I...
    """
    
    original_text: str = """### Source Text

> **Island**: The picture of being separated and cut off from others.
> Positive: If the dream or vision is positive, the Lord is leading you to be separated to Him for a season—to receive more anointing or training.
> Negative: When it is not the Lord doing the separating but you, it means you have cut yourself off from others and the Lord. A picture of the Spirit of Independence.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Island | 岛 | 分离和隔绝 |
| Separated | 分别 | 被分别归主 |
| Cut off | 隔绝 | 与他人断绝 |
| Independence | 独立 | 不依赖神和人 |

### English Paraphrase

An island represents being separated and cut off from others. Positively, the Lord is leading you to be separated to Him for a season—for anointing or training. Negatively, you have cut yourself off from others and the Lord—a Spirit of Independence.

### Chinese Interpretation

岛代表被分离和与他人隔绝。正面而言，主正带领你在一个季节中分别归祂——为了恩膏或训练。负面而言，你已把自己与他人和主隔绝——独立的灵。

### Core Points

1. **正负皆可**: 分离者决定含义
2. **分别归主**: 正面的隔离
3. **训练季节**: 为接受更多恩膏
4. **独立警告**: 不健康的自我隔离

### Narrative Snippets

- `[ns_dav_i012]` `[trigger: island_lord]` `[factor_trigger: dream_island AND dream_separation]` `[role: 主干]` The Lord is leading you to be separated to Him for a season—to receive more anointing or training. → 主正带领你在一个季节中分别归祂——为接受更多恩膏或训练。
- `[ns_dav_i013]` `[trigger: island_independence]` `[factor_trigger: dream_island AND dream_independence]` `[role: 警告]` When you cut yourself off from others and the Lord, it is a Spirit of Independence. → 当你把自己与他人和主隔绝时，这是独立的灵。"""
    normalized_text_zh: str = """"""
    subject: str = "Island 岛/分离"
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
        l1_anchor="dvd_v1.0.0_island_岛_分离_001_L1",
    )
    version: str = "1.0.0"
