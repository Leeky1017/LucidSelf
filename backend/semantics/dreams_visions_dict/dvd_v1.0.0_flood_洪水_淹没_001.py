"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.412196
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
    semantic_id="dvd_v1.0.0_flood_洪水_淹没_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Flood洪水淹没(SemanticEntry):
    """
    ### Source Text

> **Flood**: A picture of being overwhelmed—either by the Spirit or by circumstance...
    """
    
    original_text: str = """### Source Text

> **Flood**: A picture of being overwhelmed—either by the Spirit or by circumstances.
> Positive: A flood of the Spirit bringing refreshing and cleansing. Negative: A flood of problems overwhelming you. The enemy's flood of lies and accusations.
> Isaiah 59:19 "When the enemy comes in like a flood, the Spirit of the LORD shall lift up a standard against him."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Flood | 洪水 | 被淹没 |
| Overwhelm | 淹没 | 超过承受能力 |
| Spirit | 圣灵 | 神的浇灌 |
| Enemy | 仇敌 | 攻击的浪潮 |

### English Paraphrase

A flood represents being overwhelmed—either by the Spirit or circumstances. A flood of the Spirit brings refreshing and cleansing. A flood of problems overwhelms you. When the enemy comes in like a flood, the Spirit raises a standard against him.

### Chinese Interpretation

洪水代表被淹没——无论是被圣灵还是环境。圣灵的洪水带来更新和洁净。问题的洪水淹没你。当仇敌如洪水涌来，主的灵必竖起大旗抵挡他。

### Core Points

1. **正负皆可**: 洪水来源决定含义
2. **圣灵浇灌**: 正面的属灵涌流
3. **问题淹没**: 负面的环境压迫
4. **得胜应许**: 主必竖起大旗

### Narrative Snippets

- `[ns_dav_f015]` `[trigger: flood_spirit]` `[factor_trigger: dream_flood AND dream_spirit]` `[role: 主干]` A flood of the Spirit brings refreshing and cleansing—the outpouring of God's presence. → 圣灵的洪水带来更新和洁净——神同在的浇灌。
- `[ns_dav_f016]` `[trigger: flood_enemy]` `[factor_trigger: dream_flood AND dream_enemy]` `[role: 警告]` When the enemy comes in like a flood, the Spirit of the LORD raises a standard against him. → 当仇敌如洪水涌来，主的灵必竖起大旗抵挡他。"""
    normalized_text_zh: str = """"""
    subject: str = "Flood 洪水/淹没"
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
        l1_anchor="dvd_v1.0.0_flood_洪水_淹没_001_L1",
    )
    version: str = "1.0.0"
