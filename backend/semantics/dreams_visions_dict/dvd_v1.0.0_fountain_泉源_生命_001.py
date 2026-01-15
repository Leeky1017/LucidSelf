"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.412240
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
    semantic_id="dvd_v1.0.0_fountain_泉源_生命_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Fountain泉源生命(SemanticEntry):
    """
    ### Source Text

> **Fountain**: A picture of the source of life—the Holy Spirit flowing from within...
    """
    
    original_text: str = """### Source Text

> **Fountain**: A picture of the source of life—the Holy Spirit flowing from within.
> Positive: A flowing fountain speaks of the Spirit's life within you. Springs of living water.
> Negative: A dried-up fountain speaks of spiritual barrenness—the Spirit being quenched.
> John 4:14 "...the water that I shall give him shall be in him a well of water springing up into everlasting life."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Fountain | 泉源 | 生命的源头 |
| Living water | 活水 | 圣灵的涌流 |
| Spring | 泉 | 从里面涌出 |
| Dried up | 干涸 | 灵里枯竭 |

### English Paraphrase

A fountain represents the source of life—the Holy Spirit flowing from within. A flowing fountain speaks of the Spirit's life within you, springs of living water. A dried-up fountain speaks of spiritual barrenness—the Spirit being quenched.

### Chinese Interpretation

泉源代表生命的源头——圣灵从里面涌流。流动的泉源象征里面圣灵的生命，活水的泉源。干涸的泉源象征属灵的枯竭——圣灵被消灭。

### Core Points

1. **正负皆可**: 泉源状态决定含义
2. **圣灵象征**: 活水从里面涌出
3. **永生记号**: 涌流到永生
4. **枯竭警告**: 可能表示灵里消沉

### Narrative Snippets

- `[ns_dav_f021]` `[trigger: fountain_life]` `[factor_trigger: dream_fountain AND dream_life]` `[role: 主干]` The water I give shall be a well springing up into everlasting life—the fountain of the Spirit within. → 我所赐的水要在他里头成为泉源直涌到永生——里面圣灵的泉源。"""
    normalized_text_zh: str = """"""
    subject: str = "Fountain 泉源/生命"
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
        l1_anchor="dvd_v1.0.0_fountain_泉源_生命_001_L1",
    )
    version: str = "1.0.0"
