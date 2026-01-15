"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.409482
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
    semantic_id="dvd_v1.0.0_ears_耳朵_听觉_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Ears耳朵听觉(SemanticEntry):
    """
    ### Source Text

> **Ears**: A picture of hearing—either spiritual hearing or the ability to hear th...
    """
    
    original_text: str = """### Source Text

> **Ears**: A picture of hearing—either spiritual hearing or the ability to hear the voice of God.
> Positive: To have your ear anointed in dreams speaks of receiving the ability to hear the Lord clearly. To receive an ear from someone means you receive their spiritual hearing.
> Negative: Closed ears speak of refusing to hear—either the voice of God or of other people.
> Revelation 2:7 "He that has an ear, let him hear what the Spirit says to the churches."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Ears | 耳朵 | 属灵的听觉 |
| Hearing | 听 | 听神的声音 |
| Anointed | 膏抹 | 被装备来听 |
| Closed | 关闭 | 拒绝听从 |

### English Paraphrase

Ears represent hearing—the ability to hear God's voice. Having your ear anointed means receiving clear spiritual hearing. Receiving someone's ear means inheriting their spiritual sensitivity. Closed ears speak of refusing to hear God or others.

### Chinese Interpretation

耳朵代表听觉——听神声音的能力。耳朵被膏抹意味着接受清晰的属灵听觉。接受某人的耳朵意味着继承他们的属灵敏感度。关闭的耳朵象征拒绝听神或他人。

### Core Points

1. **正负皆可**: 耳朵状态决定含义
2. **属灵听觉**: 听神的声音
3. **恩膏装备**: 被膏抹来听得更清楚
4. **关闭警告**: 拒绝听从是危险的

### Narrative Snippets

- `[ns_dav_e005]` `[trigger: ears_anointed]` `[factor_trigger: dream_ears AND dream_anointed]` `[role: 主干]` Having your ear anointed speaks of receiving the ability to hear the Lord clearly. → 耳朵被膏抹象征接受清晰听主声音的能力。
- `[ns_dav_e006]` `[trigger: ears_closed]` `[factor_trigger: dream_ears AND dream_closed]` `[role: 警告]` Closed ears speak of refusing to hear—either the voice of God or of other people. → 关闭的耳朵象征拒绝听——无论是神的声音还是他人的声音。"""
    normalized_text_zh: str = """"""
    subject: str = "Ears 耳朵/听觉"
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
        l1_anchor="dvd_v1.0.0_ears_耳朵_听觉_001_L1",
    )
    version: str = "1.0.0"
