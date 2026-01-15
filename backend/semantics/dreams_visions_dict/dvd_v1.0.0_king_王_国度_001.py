"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.443834
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
    semantic_id="dvd_v1.0.0_king_王_国度_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class King王国度(SemanticEntry):
    """
    ### Source Text

> **King**: A representation of a specific realm of authority and leadership. A kin...
    """
    
    original_text: str = """### Source Text

> **King**: A representation of a specific realm of authority and leadership. A king is placed over a specific kingdom. The Lord Jesus is our King and High Priest over the Kingdom of Heaven.
> Positive: Dreaming of being made a king means the Lord is calling you to rise up in your position in Christ.
> Negative: Losing your position as king means you are not walking in Christ's authority.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| King | 王 | 权柄和领导 |
| Kingdom | 国度 | 统治的范围 |
| Authority | 权柄 | 在基督里的位置 |
| Position | 位置 | 被赋予的角色 |

### English Paraphrase

A king represents a realm of authority and leadership over a specific kingdom. Jesus is our King over the Kingdom of Heaven. Being made a king means the Lord is calling you to rise up in your position in Christ. Losing kingship means not walking in Christ's authority.

### Chinese Interpretation

王代表一个特定国度的权柄和领导范围。耶稣是我们在天国的王。被立为王意味着主呼召你在基督里的位置上兴起。失去王位意味着没有行在基督的权柄中。

### Core Points

1. **正负皆可**: 王位状态决定含义
2. **权柄象征**: 领导和统治的位置
3. **基督为王**: 耶稣是天国的王
4. **位置警告**: 可能失去权柄

### Narrative Snippets

- `[ns_dav_k003]` `[trigger: king_rise]` `[factor_trigger: dream_king AND dream_rise]` `[role: 主干]` Being made a king means the Lord is calling you to rise up in your position in Christ. → 被立为王意味着主呼召你在基督里的位置上兴起。
- `[ns_dav_k004]` `[trigger: king_lose]` `[factor_trigger: dream_king AND dream_lose]` `[role: 警告]` Losing your position as king means you are not walking in the authority Christ has given you. → 失去王位意味着你没有行在基督赐给你的权柄中。"""
    normalized_text_zh: str = """"""
    subject: str = "King 王/国度"
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
        l1_anchor="dvd_v1.0.0_king_王_国度_001_L1",
    )
    version: str = "1.0.0"
