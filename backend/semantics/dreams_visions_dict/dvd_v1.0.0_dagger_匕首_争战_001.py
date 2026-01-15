"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.401902
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
    semantic_id="dvd_v1.0.0_dagger_匕首_争战_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Dagger匕首争战(SemanticEntry):
    """
    ### Source Text

> **Dagger**: A picture of spiritual warfare.
> Although not a very powerful weapon...
    """
    
    original_text: str = """### Source Text

> **Dagger**: A picture of spiritual warfare.
> Although not a very powerful weapon like a sword, the dagger can also speak of a spiritual warfare function. It speaks of spiritual warfare on an intimate level—helping people break free of bondage one person at a time. This is not a public ministry but a 'one on one' ministry.
> Negative: The dagger was not by any means an instrument of honor. Usually hidden from sight, used in close combat—a deadly weapon speaking of destruction and violence.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Dagger | 匕首 | 属灵争战的工具 |
| Warfare | 争战 | 一对一的服事 |
| Intimate | 亲密的 | 个人层面的帮助 |
| Violence | 暴力 | 负面时代表毁灭 |

### English Paraphrase

A dagger represents spiritual warfare on an intimate level—helping people break free one person at a time. It can also speak of a Teaching Ministry starting out. Negatively, daggers are hidden deadly weapons speaking of destruction and violence, used in pagan rituals.

### Chinese Interpretation

匕首代表亲密层面的属灵争战——一次帮助一个人得自由。它也可能象征正在起步的教导事工。负面而言，匕首是隐藏的致命武器，代表毁灭和暴力，在异教仪式中使用。

### Core Points

1. **正负皆可**: 使用目的决定含义
2. **一对一服事**: 不是公开的事工
3. **教导起步**: 可能代表教导事工开始
4. **暴力警告**: 负面时象征毁灭

### Narrative Snippets

- `[ns_dav_d001]` `[trigger: dagger_warfare]` `[factor_trigger: dream_dagger AND dream_warfare]` `[role: 主干]` A dagger speaks of spiritual warfare on an intimate level—helping people break free one at a time. → 匕首象征亲密层面的属灵争战——一次帮助一个人得自由。
- `[ns_dav_d002]` `[trigger: dagger_violence]` `[factor_trigger: dream_dagger AND dream_pagan]` `[role: 警告]` Daggers are known to be used in pagan rituals—a hidden deadly weapon of destruction. → 匕首常用于异教仪式——隐藏的致命毁灭武器。"""
    normalized_text_zh: str = """"""
    subject: str = "Dagger 匕首/争战"
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
        l1_anchor="dvd_v1.0.0_dagger_匕首_争战_001_L1",
    )
    version: str = "1.0.0"
