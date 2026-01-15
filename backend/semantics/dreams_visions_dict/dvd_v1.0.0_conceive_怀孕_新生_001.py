"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.419890
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
    semantic_id="dvd_v1.0.0_conceive_怀孕_新生_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Conceive怀孕新生(SemanticEntry):
    """
    ### Source Text

> **Conceive**: The start of something new in your life.
> To conceive a baby means...
    """
    
    original_text: str = """### Source Text

> **Conceive**: The start of something new in your life.
> To conceive a baby means that something new has started to take place in you. When the Holy Spirit came on Mary, she conceived Jesus.
> Positive: Dreaming of falling pregnant is often a good sign that the Lord is doing something new.
> Negative: Not everything we conceive is positive—consider Ananias and Sapphira who conceived a lie.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Conceive | 怀孕 | 新事物的开始 |
| New birth | 新生 | 灵里的新开始 |
| Miracle | 神迹 | 超自然的孕育 |
| Sin | 罪 | 心中可能怀的恶念 |

### English Paraphrase

Conceiving represents the start of something new in your life. When the Holy Spirit came on Mary, she conceived Jesus. Dreaming of falling pregnant is often a good sign of new beginnings. Negatively, we can also conceive sin and lies in our hearts.

### Chinese Interpretation

怀孕代表生命中新事物的开始。当圣灵降临在马利亚身上时，她怀了耶稣。梦见怀孕通常是新开始的好兆头。负面而言，我们也可能在心中怀着罪和谎言。

### Core Points

1. **正负皆可**: 怀的内容决定含义
2. **新开始**: 神正在做新事
3. **成长需要**: 怀孕后需要呵护直到成熟
4. **心态重要**: 心中可能怀善也可能怀恶

### Narrative Snippets

- `[ns_dav_c041]` `[trigger: conceive_new]` `[factor_trigger: dream_conceive AND dream_new]` `[role: 主干]` To conceive means something new has started in you—the Lord is doing a new thing. → 怀孕意味着新事物已在你里面开始——主正在做新事。
- `[ns_dav_c042]` `[trigger: conceive_sin]` `[factor_trigger: dream_conceive AND dream_sin]` `[role: 警告]` Not everything we conceive is positive—we can conceive sin and bitterness in our hearts. → 不是所有怀的都是正面的——我们可能在心中怀着罪和苦毒。"""
    normalized_text_zh: str = """"""
    subject: str = "Conceive 怀孕/新生"
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
        l1_anchor="dvd_v1.0.0_conceive_怀孕_新生_001_L1",
    )
    version: str = "1.0.0"
