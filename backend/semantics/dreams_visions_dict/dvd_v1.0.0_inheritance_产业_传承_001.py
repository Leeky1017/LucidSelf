"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.429252
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
    semantic_id="dvd_v1.0.0_inheritance_产业_传承_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Inheritance产业传承(SemanticEntry):
    """
    ### Source Text

> **Inheritance**: To enter into the fruit of another person's labor. Receiving an ...
    """
    
    original_text: str = """### Source Text

> **Inheritance**: To enter into the fruit of another person's labor. Receiving an inheritance speaks of receiving the fruits of another's labor—the best of what they have. Through Christ, we share in His inheritance. All that belongs to God now belongs to us!
> Negative: Receiving an inheritance from a deceased family member could indicate you have inherited a generational curse.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Inheritance | 产业 | 他人劳动的果实 |
| Fruits | 果实 | 最好的部分 |
| Christ | 基督 | 我们在祂里面的产业 |
| Curse | 咒诅 | 世代的咒诅 |

### English Paraphrase

Inheritance means entering into the fruit of another's labor—receiving the best they have. Through Christ, we share in His inheritance; all that belongs to God now belongs to us. Negatively, receiving inheritance from deceased family may indicate a generational curse.

### Chinese Interpretation

产业意味着进入他人劳动的果实——接受他们最好的。通过基督，我们分享祂的产业；属于神的一切现在都属于我们。负面而言，从去世家人那里接受产业可能表示世代咒诅。

### Core Points

1. **正负皆可**: 来源决定含义
2. **果实传承**: 他人劳动的最好部分
3. **基督产业**: 在祂里面的份
4. **咒诅警告**: 可能是世代咒诅

### Narrative Snippets

- `[ns_dav_i008]` `[trigger: inheritance_christ]` `[factor_trigger: dream_inheritance AND dream_christ]` `[role: 主干]` Through Christ, we share in His inheritance—all that belongs to God now belongs to us! → 通过基督，我们分享祂的产业——属于神的一切现在都属于我们！
- `[ns_dav_i009]` `[trigger: inheritance_curse]` `[factor_trigger: dream_inheritance AND dream_curse]` `[role: 警告]` Receiving inheritance from deceased family may indicate you have inherited a generational curse. → 从去世家人那里接受产业可能表示你继承了世代咒诅。"""
    normalized_text_zh: str = """"""
    subject: str = "Inheritance 产业/传承"
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
        l1_anchor="dvd_v1.0.0_inheritance_产业_传承_001_L1",
    )
    version: str = "1.0.0"
