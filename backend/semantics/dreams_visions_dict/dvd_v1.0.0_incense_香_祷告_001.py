"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.429237
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
    semantic_id="dvd_v1.0.0_incense_香_祷告_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Incense香祷告(SemanticEntry):
    """
    ### Source Text

> **Incense**: The burning of incense had a two-fold function: covering the smell o...
    """
    
    original_text: str = """### Source Text

> **Incense**: The burning of incense had a two-fold function: covering the smell of animal sacrifice and offering praise and prayer. In Revelation, the prayers of the saints are likened to incense. To dream or have a vision of burning incense indicates the Lord is calling you to intercede.
> Negative: Strange incense or incense to false gods speaks of praying in the flesh against God's will.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Incense | 香 | 祷告和赞美 |
| Prayer | 祷告 | 圣徒的祈祷 |
| Intercede | 代祷 | 为他人祷告 |
| Strange incense | 凡火 | 不属神的祷告 |

### English Paraphrase

Incense represents prayer and praise—covering sins with worship. Prayers of the saints are likened to incense. Burning incense indicates a call to intercession. Strange incense or incense to false gods speaks of praying in the flesh against God's will.

### Chinese Interpretation

香代表祷告和赞美——用敬拜遮盖罪。圣徒的祈祷被比作香。焚香表示蒙召代祷。凡火或向假神烧的香象征凭肉体祷告违背神的旨意。

### Core Points

1. **正负皆可**: 香的对象决定含义
2. **祷告象征**: 圣徒的祈祷如香
3. **代祷呼召**: 为神的百姓代求
4. **凡火警告**: 不按神旨意的祷告

### Narrative Snippets

- `[ns_dav_i006]` `[trigger: incense_prayer]` `[factor_trigger: dream_incense AND dream_prayer]` `[role: 主干]` Burning incense indicates the Lord is calling you to intercede on behalf of His people. → 焚香表示主呼召你为祂的百姓代祷。
- `[ns_dav_i007]` `[trigger: incense_strange]` `[factor_trigger: dream_incense AND dream_flesh]` `[role: 警告]` Strange incense speaks of praying in the flesh and against the will of God. → 凡火象征凭肉体祷告和违背神的旨意。"""
    normalized_text_zh: str = """"""
    subject: str = "Incense 香/祷告"
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
        l1_anchor="dvd_v1.0.0_incense_香_祷告_001_L1",
    )
    version: str = "1.0.0"
