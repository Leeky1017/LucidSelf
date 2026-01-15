"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.396243
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
    semantic_id="dvd_v1.0.0_mountain_山_挑战_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Mountain山挑战(SemanticEntry):
    """
    ### Source Text

> **Mountain**: A new journey and obtaining new heights. It can also be an obstacle...
    """
    
    original_text: str = """### Source Text

> **Mountain**: A new journey and obtaining new heights. It can also be an obstacle to conquer.
> Positive: A mountain in prophetic dreams is a promotion opportunity—receiving anointing. Moses experienced God's glory on the mountain!
> Negative: A mountain in your path speaks of an obstacle the enemy put there. But you can speak to the mountain and cast it into the sea!

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Mountain | 山 | 旅程和高度 |
| Promotion | 晋升 | 属灵的提升 |
| Obstacle | 障碍 | 需要克服的 |
| Glory | 荣耀 | 神的同在 |

### English Paraphrase

A mountain represents a new journey and obtaining new heights—or an obstacle to conquer. Positively, it's a promotion opportunity for anointing. Moses experienced God's glory on the mountain. Negatively, it's an obstacle from the enemy—but you can speak to it and cast it into the sea!

### Chinese Interpretation

山代表新的旅程和达到新的高度——或需要克服的障碍。正面而言，它是接受恩膏的晋升机会。摩西在山上经历了神的荣耀。负面而言，它是仇敌设置的障碍——但你可以向它说话，把它投到海里！

### Core Points

1. **正负皆可**: 上下文决定含义
2. **晋升象征**: 属灵的提升机会
3. **神的同在**: 山顶经历荣耀
4. **克服障碍**: 可以命令它挪去

### Narrative Snippets

- `[ns_dav_m016]` `[trigger: mountain_glory]` `[factor_trigger: dream_mountain AND dream_glory]` `[role: 主干]` A mountain is an opportunity for promotion—Moses experienced God's glory on the mountain! → 山是晋升的机会——摩西在山上经历了神的荣耀！
- `[ns_dav_m017]` `[trigger: mountain_obstacle]` `[factor_trigger: dream_mountain AND dream_obstacle]` `[role: 警告]` A mountain in your path speaks of an obstacle—but you can command it to be cast into the sea! → 你路上的山象征障碍——但你可以命令它被投到海里！"""
    normalized_text_zh: str = """"""
    subject: str = "Mountain 山/挑战"
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
        l1_anchor="dvd_v1.0.0_mountain_山_挑战_001_L1",
    )
    version: str = "1.0.0"
