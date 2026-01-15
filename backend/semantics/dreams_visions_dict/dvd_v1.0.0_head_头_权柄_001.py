"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.450549
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
    semantic_id="dvd_v1.0.0_head_头_权柄_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Head头权柄(SemanticEntry):
    """
    ### Source Text

> **Head**: The head speaks of a position of authority. The husband is the head of ...
    """
    
    original_text: str = """### Source Text

> **Head**: The head speaks of a position of authority. The husband is the head of the wife, as Christ is the head of the Church.
> Positive: Receiving a crown or having your head lifted speaks of being given authority and promotion.
> Negative: Losing your head speaks of losing your position and authority.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Head | 头 | 权柄的位置 |
| Authority | 权柄 | 领导的能力 |
| Crown | 冠冕 | 尊荣和晋升 |
| Church | 教会 | 基督的身体 |

### English Paraphrase

The head represents a position of authority—the husband is head of the wife as Christ is head of the Church. Receiving a crown or lifted head speaks of authority and promotion. Losing your head speaks of losing position and authority.

### Chinese Interpretation

头代表权柄的位置——丈夫是妻子的头，正如基督是教会的头。接受冠冕或抬头象征权柄和晋升。失去头象征失去地位和权柄。

### Core Points

1. **正负皆可**: 头的状态决定含义
2. **权柄象征**: 领导和管理的位置
3. **晋升记号**: 冠冕代表尊荣
4. **丧失警告**: 可能表示失去权柄

### Narrative Snippets

- `[ns_dav_h008]` `[trigger: head_authority]` `[factor_trigger: dream_head AND dream_authority]` `[role: 主干]` The head speaks of a position of authority—receiving a crown indicates promotion. → 头象征权柄的位置——接受冠冕表示晋升。"""
    normalized_text_zh: str = """"""
    subject: str = "Head 头/权柄"
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
        l1_anchor="dvd_v1.0.0_head_头_权柄_001_L1",
    )
    version: str = "1.0.0"
