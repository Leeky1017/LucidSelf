"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.450558
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
    semantic_id="dvd_v1.0.0_heart_心_情感_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Heart心情感(SemanticEntry):
    """
    ### Source Text

> **Heart**: Your heart symbolizes your feelings and emotions.
> Positive: A heart ...
    """
    
    original_text: str = """### Source Text

> **Heart**: Your heart symbolizes your feelings and emotions.
> Positive: A heart being healed shows the Lord has healed a hurt from the past. A heart can speak of love.
> Negative: A bleeding, broken or wounded heart speaks of emotional pain from past hurts. A stony heart indicates someone who has closed off their feelings.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Heart | 心 | 情感和感受 |
| Love | 爱 | 心的正面表达 |
| Wounded | 受伤 | 过去的伤害 |
| Stony | 石头的 | 封闭的心 |

### English Paraphrase

The heart symbolizes feelings and emotions. A healed heart shows God has healed past hurts. A heart can speak of love. A bleeding, broken or wounded heart speaks of emotional pain. A stony heart indicates someone who has closed off feelings to others and God.

### Chinese Interpretation

心象征感受和情感。被医治的心表明神已医治过去的伤害。心可以代表爱。流血、破碎或受伤的心象征情感上的痛苦。石头心表示某人已对他人和神封闭了感受。

### Core Points

1. **正负皆可**: 心的状态决定含义
2. **情感象征**: 感受和情感的中心
3. **医治需要**: 神能医治破碎的心
4. **封闭警告**: 石头心阻挡神的声音

### Narrative Snippets

- `[ns_dav_h009]` `[trigger: heart_heal]` `[factor_trigger: dream_heart AND dream_healing]` `[role: 主干]` He heals the broken in heart and binds up their wounds—God restores emotional hurts. → 祂医好伤心的人，裹好他们的伤处——神恢复情感上的伤害。
- `[ns_dav_h010]` `[trigger: heart_stony]` `[factor_trigger: dream_heart AND dream_stony]` `[role: 警告]` A stony heart indicates someone who has closed off their feelings to others and the Lord. → 石头心表示某人已对他人和主封闭了感受。"""
    normalized_text_zh: str = """"""
    subject: str = "Heart 心/情感"
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
        l1_anchor="dvd_v1.0.0_heart_心_情感_001_L1",
    )
    version: str = "1.0.0"
