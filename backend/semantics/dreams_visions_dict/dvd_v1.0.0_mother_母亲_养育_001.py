"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.396224
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
    semantic_id="dvd_v1.0.0_mother_母亲_养育_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Mother母亲养育(SemanticEntry):
    """
    ### Source Text

> **Mother**: A picture of nurturing, healing and restoration. The mother cares for...
    """
    
    original_text: str = """### Source Text

> **Mother**: A picture of nurturing, healing and restoration. The mother cares for and feeds the child—also lays down the law in the heart of a child, giving a pattern for life.
> Positive: If you have a good relationship with your mother, she could represent the church (Bride of Christ).
> Negative: If your relationship was bad, she could represent the flesh—pride, jealousy, anger. Seeing your actual mother may indicate generational curses or childhood hurts.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Mother | 母亲 | 养育和医治 |
| Nurturing | 养育 | 照顾和喂养 |
| Church | 教会 | 基督的新娘 |
| Generational | 世代的 | 咒诅的传承 |

### English Paraphrase

A mother represents nurturing, healing and restoration—caring for and feeding a child. With good relationship, she could represent the church. With bad relationship, she represents the flesh. Seeing your actual mother may indicate generational curses or childhood hurts needing healing.

### Chinese Interpretation

母亲代表养育、医治和恢复——照顾和喂养孩子。关系好时，她可能代表教会。关系不好时，她代表肉体。看见你真正的母亲可能表示世代咒诅或需要医治的童年伤害。

### Core Points

1. **正负皆可**: 关系决定含义
2. **养育象征**: 照顾和培养
3. **教会代表**: 正面时可代表教会
4. **咒诅警告**: 可能涉及世代咒诅

### Narrative Snippets

- `[ns_dav_m012]` `[trigger: mother_nurture]` `[factor_trigger: dream_mother AND dream_nurture]` `[role: 主干]` A mother speaks of nurturing, healing and restoration—caring for and feeding the child. → 母亲象征养育、医治和恢复——照顾和喂养孩子。
- `[ns_dav_m013]` `[trigger: mother_curse]` `[factor_trigger: dream_mother AND dream_curse]` `[role: 警告]` Seeing your actual mother may indicate generational curses or childhood hurts to address. → 看见你真正的母亲可能表示需要处理的世代咒诅或童年伤害。"""
    normalized_text_zh: str = """"""
    subject: str = "Mother 母亲/养育"
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
        l1_anchor="dvd_v1.0.0_mother_母亲_养育_001_L1",
    )
    version: str = "1.0.0"
