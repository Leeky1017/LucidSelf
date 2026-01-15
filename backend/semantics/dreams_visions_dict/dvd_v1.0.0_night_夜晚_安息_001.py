"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.433436
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
    semantic_id="dvd_v1.0.0_night_夜晚_安息_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Night夜晚安息(SemanticEntry):
    """
    ### Source Text

> **Night**: A season of rest. Negatively it speaks of the hidden work of the enemy...
    """
    
    original_text: str = """### Source Text

> **Night**: A season of rest. Negatively it speaks of the hidden work of the enemy. During the night, God speaks to us in dreams and we find rest.
> Positive: A sunset means your hard work is over—time to rest and let God complete what He began. Midnight speaks of dramatic transition.
> Negative: Night falling with fear means the enemy is at work. Walking in darkness means getting back into God's light.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Night | 夜晚 | 安息或隐藏 |
| Rest | 安息 | 工作后的休息 |
| Midnight | 午夜 | 戏剧性的转变 |
| Darkness | 黑暗 | 仇敌的领域 |

### English Paraphrase

Night represents a season of rest—God speaks through dreams and we find rest. A sunset means work is over; time to rest while God completes what He began. Midnight speaks of dramatic transition. Night with fear means enemy is at work. Walking in darkness means needing God's light.

### Chinese Interpretation

夜晚代表安息的季节——神通过梦说话，我们得安息。日落意味着工作结束；是休息的时候，让神完成祂开始的。午夜象征戏剧性的转变。带着恐惧的夜晚意味着仇敌在工作。行在黑暗中意味着需要神的光。

### Core Points

1. **正负皆可**: 感受决定含义
2. **安息象征**: 工作后的休息
3. **转变记号**: 午夜是转折点
4. **黑暗警告**: 可能是仇敌的工作

### Narrative Snippets

- `[ns_dav_n011]` `[trigger: night_rest]` `[factor_trigger: dream_night AND dream_rest]` `[role: 主干]` Night is a season of rest—God speaks through dreams and we find renewal. → 夜晚是安息的季节——神通过梦说话，我们得更新。
- `[ns_dav_n012]` `[trigger: night_fear]` `[factor_trigger: dream_night AND dream_fear]` `[role: 警告]` Night falling with fear means the enemy is at work in this season. → 带着恐惧的夜晚降临意味着仇敌在这个季节工作。"""
    normalized_text_zh: str = """"""
    subject: str = "Night 夜晚/安息"
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
        l1_anchor="dvd_v1.0.0_night_夜晚_安息_001_L1",
    )
    version: str = "1.0.0"
