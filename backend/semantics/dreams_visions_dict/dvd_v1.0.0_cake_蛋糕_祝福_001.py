"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.419663
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
    semantic_id="dvd_v1.0.0_cake_蛋糕_祝福_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Cake蛋糕祝福(SemanticEntry):
    """
    ### Source Text

> **Cake**: Provision for your desires and not only your needs.
> A cake speaks of ...
    """
    
    original_text: str = """### Source Text

> **Cake**: Provision for your desires and not only your needs.
> A cake speaks of fun, enjoyment and blessing. It speaks of receiving a gift and something that is enjoyable.
> Negative: "To have your cake and eat it" speaks of strife, contention and vainglory. A cake that is not fully baked speaks of being 'half-baked' meaning that your commitment is lacking.
> Hosea 7:8 "Ephraim, he has mixed himself among the people; Ephraim is a cake not turned."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Cake | 蛋糕 | 享受和祝福的象征 |
| Provision | 供应 | 超越需要的给予 |
| Blessing | 祝福 | 来自神的恩赐 |
| Half-baked | 半生不熟 | 缺乏承诺或不完整 |

### English Paraphrase

A cake represents provision for desires beyond basic needs—fun, enjoyment, and blessing. It speaks of receiving gifts. Negatively, a half-baked cake indicates lacking commitment, and "having your cake and eat it" speaks of strife and vainglory.

### Chinese Interpretation

蛋糕代表超越基本需要的供应——乐趣、享受和祝福。它象征着接受礼物。负面而言，半熟的蛋糕表示缺乏承诺，"既要蛋糕又要吃掉它"象征纷争和虚荣。

### Core Points

1. **正负皆可**: 状态决定吉凶
2. **享受象征**: 神不仅满足需要，也满足渴望
3. **承诺测试**: 半熟蛋糕警示不完整的委身
4. **混杂警告**: 与世俗混合会带来咒诅

### Narrative Snippets

- `[ns_dav_c002]` `[trigger: cake_blessing]` `[factor_trigger: dream_cake AND dream_blessing]` `[role: 主干]` A cake speaks of fun, enjoyment and blessing—God desires to give you treats, not only needs. → 蛋糕象征乐趣、享受和祝福，神渴望满足你的心愿。
- `[ns_dav_c003]` `[trigger: cake_halfbaked]` `[factor_trigger: dream_cake AND dream_incomplete]` `[role: 条件]` A cake not fully baked speaks of 'half-baked' commitment—your dedication is lacking. → 半熟的蛋糕象征委身不完整。"""
    normalized_text_zh: str = """"""
    subject: str = "Cake 蛋糕/祝福"
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
        l1_anchor="dvd_v1.0.0_cake_蛋糕_祝福_001_L1",
    )
    version: str = "1.0.0"
