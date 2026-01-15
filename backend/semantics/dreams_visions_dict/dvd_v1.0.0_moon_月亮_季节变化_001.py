"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.396233
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
    semantic_id="dvd_v1.0.0_moon_月亮_季节变化_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Moon月亮季节变化(SemanticEntry):
    """
    ### Source Text

> **Moon**: A change of season in your life. Because the moon only rises in the eve...
    """
    
    original_text: str = """### Source Text

> **Moon**: A change of season in your life. Because the moon only rises in the evening, it shares the same interpretation as 'Night.'
> Negative: The moon and stars were often the object of pagan worship. Star signs and zodiac represent the spirit of divination—demonic.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Moon | 月亮 | 季节变化 |
| Season | 季节 | 生命的阶段 |
| Night | 夜晚 | 隐藏的工作 |
| Divination | 占卜 | 邪术的灵 |

### English Paraphrase

The moon represents a change of season in your life—shares interpretation with 'Night.' Negatively, moon and stars were objects of pagan worship. Star signs and zodiac represent the spirit of divination—demonic.

### Chinese Interpretation

月亮代表你生命中季节的变化——与"夜晚"有相同的解释。负面而言，月亮和星星是异教崇拜的对象。星座和黄道代表占卜的灵——邪灵的。

### Core Points

1. **正负皆可**: 上下文决定含义
2. **季节象征**: 生命阶段的转变
3. **夜晚相关**: 隐藏的工作
4. **占卜警告**: 星座是邪术

### Narrative Snippets

- `[ns_dav_m014]` `[trigger: moon_season]` `[factor_trigger: dream_moon AND dream_season]` `[role: 主干]` The moon represents a change of season in your life—a new phase beginning. → 月亮代表你生命中季节的变化——新阶段的开始。
- `[ns_dav_m015]` `[trigger: moon_divination]` `[factor_trigger: dream_moon AND dream_divination]` `[role: 警告]` Star signs and zodiac represent the spirit of divination—demonic influence. → 星座和黄道代表占卜的灵——邪灵的影响。"""
    normalized_text_zh: str = """"""
    subject: str = "Moon 月亮/季节变化"
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
        l1_anchor="dvd_v1.0.0_moon_月亮_季节变化_001_L1",
    )
    version: str = "1.0.0"
