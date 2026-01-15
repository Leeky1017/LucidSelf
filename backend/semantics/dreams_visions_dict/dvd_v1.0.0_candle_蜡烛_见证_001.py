"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.419695
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
    semantic_id="dvd_v1.0.0_candle_蜡烛_见证_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Candle蜡烛见证(SemanticEntry):
    """
    ### Source Text

> **Candle**: Your testimony before the world as a believer. The life and passion t...
    """
    
    original_text: str = """### Source Text

> **Candle**: Your testimony before the world as a believer. The life and passion that you have for life.
> A Candle speaks of light and the Spirit of the Lord within you. It speaks of your testimony before the world.
> Proverbs 20:27 "The spirit of man is the candle of the LORD, searching all the rooms of the inward man."
> Negative: To dream of your candle being blown out is a picture of demotivation and discouragement.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Candle | 蜡烛 | 见证和内在之光 |
| Testimony | 见证 | 在世人面前的表现 |
| Light | 光 | 主的灵在人里面 |
| Blown out | 熄灭 | 失去热情或被压制 |

### English Paraphrase

A candle represents your testimony before the world and the Spirit of the Lord within you. It speaks of light, passion, and zeal. To have your candle lit speaks of renewed passion. A candle being blown out represents demotivation and allowing circumstances to hide God's light in you.

### Chinese Interpretation

蜡烛代表你在世人面前的见证和主的灵在你里面。它象征光、热情和热心。蜡烛被点燃象征热情更新。蜡烛熄灭代表失去动力，让环境压制了神在你里面的光。

### Core Points

1. **正负皆可**: 点燃或熄灭决定含义
2. **内在之光**: 人的灵是耶和华的灯
3. **见证象征**: 你的生命如何向世人发光
4. **热情指标**: 反映对神和生命的热忱

### Narrative Snippets

- `[ns_dav_c008]` `[trigger: candle_light]` `[factor_trigger: dream_candle AND dream_testimony]` `[role: 主干]` A candle speaks of light and your testimony before the world—the Spirit of the Lord within you. → 蜡烛象征光和见证，是主的灵在你里面。
- `[ns_dav_c009]` `[trigger: candle_blownout]` `[factor_trigger: dream_candle AND dream_demotivation]` `[role: 警告]` Your candle being blown out is a picture of demotivation—allowing others to hide God's spirit in you. → 蜡烛熄灭象征失去动力，让他人压制了神的灵。"""
    normalized_text_zh: str = """"""
    subject: str = "Candle 蜡烛/见证"
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
        l1_anchor="dvd_v1.0.0_candle_蜡烛_见证_001_L1",
    )
    version: str = "1.0.0"
