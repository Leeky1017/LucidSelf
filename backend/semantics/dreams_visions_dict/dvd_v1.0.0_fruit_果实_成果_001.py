"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.412264
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
    semantic_id="dvd_v1.0.0_fruit_果实_成果_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Fruit果实成果(SemanticEntry):
    """
    ### Source Text

> **Fruit**: A picture of the results of your labor—spiritual or natural.
> Positiv...
    """
    
    original_text: str = """### Source Text

> **Fruit**: A picture of the results of your labor—spiritual or natural.
> Positive: Good fruit speaks of godly character and spiritual harvest. The fruit of the Spirit is love, joy, peace...
> Negative: Bad or rotten fruit speaks of the works of the flesh. No fruit indicates barrenness.
> Galatians 5:22 "But the fruit of the Spirit is love, joy, peace, longsuffering, gentleness, goodness, faith..."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Fruit | 果实 | 成果和品格 |
| Harvest | 收成 | 劳动的成果 |
| Spirit | 圣灵 | 圣灵的果子 |
| Rotten | 腐烂 | 肉体的工作 |

### English Paraphrase

Fruit represents the results of your labor—spiritual or natural. Good fruit speaks of godly character and harvest—the fruit of the Spirit. Bad or rotten fruit speaks of works of the flesh. No fruit indicates barrenness.

### Chinese Interpretation

果实代表你劳动的成果——属灵的或自然的。好果子象征敬虔的品格和收成——圣灵的果子。坏果子或烂果子象征肉体的工作。没有果子表示不结果。

### Core Points

1. **正负皆可**: 果实质量决定含义
2. **品格象征**: 圣灵九果
3. **收成记号**: 事工的成效
4. **不结果警告**: 可能表示生命枯竭

### Narrative Snippets

- `[ns_dav_f024]` `[trigger: fruit_spirit]` `[factor_trigger: dream_fruit AND dream_spirit]` `[role: 主干]` The fruit of the Spirit is love, joy, peace—good fruit speaks of godly character being formed. → 圣灵的果子是仁爱、喜乐、和平——好果子象征敬虔品格正在形成。"""
    normalized_text_zh: str = """"""
    subject: str = "Fruit 果实/成果"
    factor_refs: list = ['source_ref']
    
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
        l1_anchor="dvd_v1.0.0_fruit_果实_成果_001_L1",
    )
    version: str = "1.0.0"
