"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.409492
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
    semantic_id="dvd_v1.0.0_earthquake_地震_震动_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Earthquake地震震动(SemanticEntry):
    """
    ### Source Text

> **Earthquake**: A shaking—either in the spirit or in your life. A sudden change o...
    """
    
    original_text: str = """### Source Text

> **Earthquake**: A shaking—either in the spirit or in your life. A sudden change of events.
> Acts 16:26 "Suddenly there was a great earthquake, so that the foundations of the prison were shaken: and immediately all the doors were opened, and every one's bands were loosed."
> Positive: The Lord shaking loose everything that needs to go—releasing captives. Negative: The enemy shaking up your world and causing instability.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Earthquake | 地震 | 震动和改变 |
| Shaking | 震动 | 除去需要去掉的 |
| Sudden change | 突变 | 事件的突然转变 |
| Release | 释放 | 囚犯得自由 |

### English Paraphrase

An earthquake represents shaking—either in the spirit or your life. Positively, the Lord shakes loose what needs to go, releasing captives and opening doors. Negatively, the enemy shakes your world causing instability and fear. Things will never be the same after the shaking.

### Chinese Interpretation

地震代表震动——无论在灵里还是生活中。正面而言，主震掉需要去掉的，释放囚犯并打开门。负面而言，仇敌摇动你的世界造成不稳定和恐惧。震动之后事情将不再相同。

### Core Points

1. **正负皆可**: 震动来源决定含义
2. **释放能力**: 主的震动释放被囚的
3. **根基动摇**: 改变已建立的事物
4. **不再相同**: 震动后事情永远改变

### Narrative Snippets

- `[ns_dav_e007]` `[trigger: earthquake_release]` `[factor_trigger: dream_earthquake AND dream_release]` `[role: 主干]` A great earthquake shook the foundations—immediately all doors were opened and everyone's bands were loosed. → 大地震震动了根基——立刻所有门都打开，众人的锁链都松开了。
- `[ns_dav_e008]` `[trigger: earthquake_enemy]` `[factor_trigger: dream_earthquake AND dream_enemy]` `[role: 警告]` The enemy shaking your world causes instability—things will never be the same after the shaking. → 仇敌摇动你的世界造成不稳定——震动后事情将不再相同。"""
    normalized_text_zh: str = """"""
    subject: str = "Earthquake 地震/震动"
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
        l1_anchor="dvd_v1.0.0_earthquake_地震_震动_001_L1",
    )
    version: str = "1.0.0"
