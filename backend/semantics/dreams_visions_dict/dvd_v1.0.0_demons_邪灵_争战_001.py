"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.401999
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
    semantic_id="dvd_v1.0.0_demons_邪灵_争战_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Demons邪灵争战(SemanticEntry):
    """
    ### Source Text

> **Demons**: It is common to see demons both in dreams and visions. Seeing these b...
    """
    
    original_text: str = """### Source Text

> **Demons**: It is common to see demons both in dreams and visions. Seeing these beings indicates you are functioning in the gift of discerning of spirits.
> The Lord will reveal these at His bidding. If you are having demonic manifestations you cannot control, the enemy has been given license in your life.
> Ephesians 6:12 "For we wrestle not against flesh and blood, but against principalities, against powers..."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Demons | 邪灵 | 堕落天使 |
| Discerning | 辨别 | 属灵的恩赐 |
| Principalities | 执政的 | 邪灵等级 |
| License | 许可 | 仇敌进入的门 |

### English Paraphrase

Seeing demons in dreams and visions indicates the gift of discerning of spirits. Different levels exist: principalities (spirits of infirmity), power demons (depression, deception), ruler demons (occult), and princes (territorial spirits). Uncontrollable encounters indicate the enemy has license in your life.

### Chinese Interpretation

在梦和异象中看见邪灵表明你有辨别诸灵的恩赐。存在不同等级：执政的（疾病的灵）、掌权的（抑郁、迷惑）、管辖的（邪术）、和王子（地域性的灵）。无法控制的遭遇表明仇敌在你生命中有许可。

### Core Points

1. **辨别恩赐**: 看见邪灵是恩赐的运作
2. **等级体系**: 不同层次的邪灵
3. **敞开门户**: 可能表示生命中有破口
4. **需要处理**: 若无法控制需要得释放

### Narrative Snippets

- `[ns_dav_d012]` `[trigger: demons_discern]` `[factor_trigger: dream_demons AND dream_discernment]` `[role: 主干]` Seeing demons indicates you are functioning in the gift of discerning of spirits. → 看见邪灵表明你正在运作辨别诸灵的恩赐。
- `[ns_dav_d013]` `[trigger: demons_license]` `[factor_trigger: dream_demons AND dream_license]` `[role: 警告]` If you have demonic manifestations you cannot control, the enemy has been given license in your life. → 如果你有无法控制的邪灵显现，仇敌已在你生命中得到许可。"""
    normalized_text_zh: str = """"""
    subject: str = "Demons 邪灵/争战"
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
        l1_anchor="dvd_v1.0.0_demons_邪灵_争战_001_L1",
    )
    version: str = "1.0.0"
