"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.450601
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
    semantic_id="dvd_v1.0.0_house_房屋_生命_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class House房屋生命(SemanticEntry):
    """
    ### Source Text

> **House**: A house in a dream is a representation of your life.
> Positive: House...
    """
    
    original_text: str = """### Source Text

> **House**: A house in a dream is a representation of your life.
> Positive: House being built onto means the Lord is adding to your life. Renovation speaks of total rearrangement. Finding a new room indicates a hidden talent to tap into. Moving to a new house means leaving the past behind.
> Negative: Snakes entering means enemy has license. Destroyed house indicates attack. Broken foundation means unsound doctrine.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| House | 房屋 | 你的生命 |
| Renovation | 装修 | 全面重整 |
| Room | 房间 | 隐藏的才干 |
| Foundation | 根基 | 教义的基础 |

### English Paraphrase

A house represents your life. Being built onto means God is adding to your life. Renovation speaks of total rearrangement. A new room indicates hidden talents. Moving to a new house means leaving the past. Snakes entering indicate enemy license. Destroyed house shows attack. Broken foundation means unsound doctrine.

### Chinese Interpretation

房屋代表你的生命。被建造扩展意味着神在添加你的生命。装修象征全面重整。新房间表示隐藏的才干。搬到新房子意味着离开过去。蛇进入表示仇敌有许可。被毁坏的房屋显示攻击。破裂的根基意味着不健全的教义。

### Core Points

1. **正负皆可**: 房屋状态决定含义
2. **生命象征**: 代表你的整个生命
3. **改变记号**: 装修和新房间
4. **根基警告**: 教义基础需要检验

### Narrative Snippets

- `[ns_dav_h017]` `[trigger: house_life]` `[factor_trigger: dream_house AND dream_life]` `[role: 主干]` A house in a dream is a representation of your life—being built onto means God is adding to you. → 梦中的房屋代表你的生命——被建造扩展意味着神在添加你。
- `[ns_dav_h018]` `[trigger: house_foundation]` `[factor_trigger: dream_house AND dream_foundation]` `[role: 警告]` A broken foundation speaks of unsound doctrine having a bad effect on your spiritual life. → 破裂的根基象征不健全的教义对你属灵生命有坏影响。"""
    normalized_text_zh: str = """"""
    subject: str = "House 房屋/生命"
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
        l1_anchor="dvd_v1.0.0_house_房屋_生命_001_L1",
    )
    version: str = "1.0.0"
