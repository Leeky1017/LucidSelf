"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.450530
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
    semantic_id="dvd_v1.0.0_harp_竖琴_音乐_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Harp竖琴音乐(SemanticEntry):
    """
    ### Source Text

> **Harp**: Represents psalmody and music—the gift of being inspired musically by t...
    """
    
    original_text: str = """### Source Text

> **Harp**: Represents psalmody and music—the gift of being inspired musically by the Lord. Angels playing harps represent worship angels. If the Lord gives someone a harp or stringed instrument, He desires to give them a spiritual gift.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Harp | 竖琴 | 诗歌和音乐 |
| Psalmody | 诗歌 | 受圣灵感动的音乐 |
| Worship | 敬拜 | 对神的赞美 |
| Gift | 恩赐 | 属灵的能力 |

### English Paraphrase

A harp represents psalmody and the gift of being inspired musically by the Lord. Angels playing harps are worship angels. Receiving a harp or stringed instrument indicates receiving a spiritual gift for Christ-inspired music.

### Chinese Interpretation

竖琴代表诗歌和被主感动作音乐的恩赐。弹竖琴的天使是敬拜天使。接受竖琴或弦乐器表示接受受基督启示的音乐恩赐。

### Core Points

1. **通常正面**: 竖琴代表敬拜和恩赐
2. **音乐恩赐**: 被圣灵感动作音乐
3. **敬拜象征**: 对神的赞美和敬拜
4. **先知歌唱**: 先知性的诗歌

### Narrative Snippets

- `[ns_dav_h005]` `[trigger: harp_worship]` `[factor_trigger: dream_harp AND dream_worship]` `[role: 主干]` A harp represents psalmody and Christ-inspired music—a spiritual gift for worship. → 竖琴代表诗歌和受基督启示的音乐——敬拜的属灵恩赐。"""
    normalized_text_zh: str = """"""
    subject: str = "Harp 竖琴/音乐"
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
        l1_anchor="dvd_v1.0.0_harp_竖琴_音乐_001_L1",
    )
    version: str = "1.0.0"
