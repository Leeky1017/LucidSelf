"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.412248
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
    semantic_id="dvd_v1.0.0_foxes_狐狸_欺骗_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Foxes狐狸欺骗(SemanticEntry):
    """
    ### Source Text

> **Foxes**: A picture of cunning, deception, and little sins that spoil.
> Song of...
    """
    
    original_text: str = """### Source Text

> **Foxes**: A picture of cunning, deception, and little sins that spoil.
> Song of Solomon 2:15 "Take us the foxes, the little foxes, that spoil the vines: for our vines have tender grapes."
> Foxes are subtle and sneaky—they destroy vineyards gradually. Little sins that seem insignificant can destroy relationships and ministries.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Foxes | 狐狸 | 狡猾和欺骗 |
| Cunning | 狡猾 | 阴险的手段 |
| Little sins | 小罪 | 看似无害却毁坏 |
| Spoil | 毁坏 | 渐进的破坏 |

### English Paraphrase

Foxes represent cunning, deception, and little sins that spoil. They are subtle and sneaky, destroying vineyards gradually. Little sins that seem insignificant can destroy relationships and ministries. Catch the foxes before they spoil the vines.

### Chinese Interpretation

狐狸代表狡猾、欺骗和毁坏的小罪。它们狡诈而诡秘，渐渐毁坏葡萄园。看似无害的小罪能毁坏关系和事工。在狐狸毁坏葡萄树之前抓住它们。

### Core Points

1. **始终负面**: 狐狸代表欺骗和罪
2. **渐进破坏**: 慢慢毁坏好事物
3. **小事重要**: 小罪能造成大破坏
4. **及时处理**: 要抓住小狐狸

### Narrative Snippets

- `[ns_dav_f022]` `[trigger: foxes_spoil]` `[factor_trigger: dream_foxes AND dream_spoil]` `[role: 警告]` Catch the little foxes that spoil the vines—little sins that seem insignificant can destroy much. → 要抓住毁坏葡萄树的小狐狸——看似无害的小罪能毁坏许多。"""
    normalized_text_zh: str = """"""
    subject: str = "Foxes 狐狸/欺骗"
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
        l1_anchor="dvd_v1.0.0_foxes_狐狸_欺骗_001_L1",
    )
    version: str = "1.0.0"
