"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.401958
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
    semantic_id="dvd_v1.0.0_daughter_女儿_果实_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Daughter女儿果实(SemanticEntry):
    """
    ### Source Text

> **Daughter**: In an internal dream, your daughter speaks of the things you have b...
    """
    
    original_text: str = """### Source Text

> **Daughter**: In an internal dream, your daughter speaks of the things you have borne in the spirit—your ministry. They could also speak of the positive forces of the spirit: faith, hope and love.
> My daughters have always represented my love and my faith in my dreams. Identify your relationship with your daughter and you will discover what they represent.
> Visions: If you see the daughter of someone you are ministering to, the Lord could be indicating their daughter needs ministry.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Daughter | 女儿 | 灵里所结的果实 |
| Ministry | 事工 | 你生出的属灵儿女 |
| Faith | 信心 | 正面的灵力 |
| Relationship | 关系 | 决定梦中含义 |

### English Paraphrase

In internal dreams, your daughter represents things borne in the spirit—your ministry or positive spiritual forces (faith, hope, love). Your relationship with your daughter determines what she represents. In visions, someone's daughter may indicate she needs ministry.

### Chinese Interpretation

在内在梦中，你的女儿代表灵里所结的果实——你的事工或正面的属灵力量（信、望、爱）。你与女儿的关系决定她在梦中代表什么。在异象中，某人的女儿可能表示她需要服事。

### Core Points

1. **正负皆可**: 关系决定含义
2. **事工果实**: 代表你所生出的
3. **灵力象征**: 信望爱的正面力量
4. **异象指引**: 可能指向实际需要

### Narrative Snippets

- `[ns_dav_d005]` `[trigger: daughter_ministry]` `[factor_trigger: dream_daughter AND dream_ministry]` `[role: 主干]` Your daughter in dreams speaks of things you have borne in the spirit—your ministry and spiritual fruit. → 梦中的女儿象征你灵里所结的果实——你的事工和属灵果实。"""
    normalized_text_zh: str = """"""
    subject: str = "Daughter 女儿/果实"
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
        l1_anchor="dvd_v1.0.0_daughter_女儿_果实_001_L1",
    )
    version: str = "1.0.0"
