"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.450490
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
    semantic_id="dvd_v1.0.0_hair_头发_形象_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Hair头发形象(SemanticEntry):
    """
    ### Source Text

> **Hair**: Hair is a picture of the image we present to the world. A woman's hair ...
    """
    
    original_text: str = """### Source Text

> **Hair**: Hair is a picture of the image we present to the world. A woman's hair is a picture of her covering—her husband or spiritual authority.
> Positive: Beautiful hair means confidence. Changing hair indicates going through a change in personal image.
> Negative: Damaged hair speaks of conflict and insecurity. For a man, long hair is shame—rejecting masculinity. Losing hair speaks of not being under authority.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Hair | 头发 | 向世界呈现的形象 |
| Covering | 遮盖 | 女性的属灵保护 |
| Image | 形象 | 个人呈现 |
| Authority | 权柄 | 属灵遮盖 |

### English Paraphrase

Hair represents the image we present to the world. For women, long hair represents covering under husband or spiritual authority. Beautiful hair indicates confidence; damaged hair speaks of conflict and insecurity. For men, long hair represents rejecting masculinity.

### Chinese Interpretation

头发代表我们向世界呈现的形象。对女性，长发代表在丈夫或属灵权柄下的遮盖。美丽的头发表示自信；受损的头发象征冲突和不安全感。对男性，长发代表拒绝男性气质。

### Core Points

1. **正负皆可**: 头发状态决定含义
2. **形象象征**: 向世界呈现的形象
3. **遮盖含义**: 女性的属灵保护
4. **权柄记号**: 在权柄下的标志

### Narrative Snippets

- `[ns_dav_h001]` `[trigger: hair_image]` `[factor_trigger: dream_hair AND dream_image]` `[role: 主干]` Hair is a picture of the image we present to the world—beautiful hair means confidence. → 头发是我们向世界呈现的形象——美丽的头发意味着自信。
- `[ns_dav_h002]` `[trigger: hair_covering]` `[factor_trigger: dream_hair AND dream_covering]` `[role: 主干]` A woman's hair is a picture of her covering—her husband or spiritual authority. → 女性的头发是她遮盖的象征——她的丈夫或属灵权柄。"""
    normalized_text_zh: str = """"""
    subject: str = "Hair 头发/形象"
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
        l1_anchor="dvd_v1.0.0_hair_头发_形象_001_L1",
    )
    version: str = "1.0.0"
