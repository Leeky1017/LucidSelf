"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.396144
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
    semantic_id="dvd_v1.0.0_make_up_化妆_形象_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class MakeUp化妆形象(SemanticEntry):
    """
    ### Source Text

> **Make-up**: The image that you intentionally present to the world. As a woman, b...
    """
    
    original_text: str = """### Source Text

> **Make-up**: The image that you intentionally present to the world. As a woman, beautiful make-up speaks of reflecting inner beauty on the outside. If you are not one to wear make-up and dream that you are, the Lord is telling you to let out some of your femininity.
> Negative: Stripped of make-up means loss of self-confidence. As a man wearing make-up—trying to be something you are not.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Make-up | 化妆 | 刻意呈现的形象 |
| Beauty | 美丽 | 内外一致 |
| Femininity | 女性特质 | 女性的温柔 |
| Stripped | 被剥去 | 失去自信 |

### English Paraphrase

Make-up represents the image you intentionally present. Beautiful make-up reflects inner beauty outwardly. If you don't usually wear make-up but dream of it, the Lord is saying to express your femininity. Being stripped of make-up means loss of self-confidence. A man wearing make-up means trying to be something you're not.

### Chinese Interpretation

化妆代表你刻意呈现的形象。美丽的化妆反映内在的美外显。如果你通常不化妆但梦见化妆，主在说要表达你的女性特质。被剥去化妆意味着失去自信。男人化妆意味着试图成为你不是的东西。

### Core Points

1. **正负皆可**: 化妆状态决定含义
2. **形象象征**: 向世界呈现的样子
3. **女性特质**: 可能需要表达温柔
4. **自信警告**: 被剥去可能是失去自信

### Narrative Snippets

- `[ns_dav_m001]` `[trigger: makeup_beauty]` `[factor_trigger: dream_makeup AND dream_beauty]` `[role: 主干]` Beautiful make-up speaks of reflecting the beauty on the inside on the outside. → 美丽的化妆象征将内在的美反映在外表上。
- `[ns_dav_m002]` `[trigger: makeup_stripped]` `[factor_trigger: dream_makeup AND dream_vulnerability]` `[role: 警告]` Being stripped of make-up means you have lost your self-confidence and feel vulnerable. → 被剥去化妆意味着你失去了自信，感到脆弱。"""
    normalized_text_zh: str = """"""
    subject: str = "Make-up 化妆/形象"
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
        l1_anchor="dvd_v1.0.0_make_up_化妆_形象_001_L1",
    )
    version: str = "1.0.0"
