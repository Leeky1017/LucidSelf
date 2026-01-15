"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.433490
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
    semantic_id="dvd_v1.0.0_owl_猫头鹰_智慧或荒凉_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Owl猫头鹰智慧或荒凉(SemanticEntry):
    """
    ### Source Text

> **Owl**: In many cultures, an owl is a picture of wisdom—if your dream is positiv...
    """
    
    original_text: str = """### Source Text

> **Owl**: In many cultures, an owl is a picture of wisdom—if your dream is positive, it may represent wisdom.
> Negative: In the Word, an owl is always negative. Owls were unclean, nocturnal, and inhabited wilderness. They speak of desolation and barrenness—proof that the enemy has accomplished his work. Seeing an owl when praying indicates a demonic stronghold.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Owl | 猫头鹰 | 智慧或荒凉 |
| Wisdom | 智慧 | 文化中的含义 |
| Desolation | 荒凉 | 仇敌的成就 |
| Unclean | 不洁 | 圣经中的含义 |

### English Paraphrase

In many cultures, an owl represents wisdom—in a positive dream, it may mean wisdom. In Scripture, an owl is always negative—unclean, nocturnal, inhabiting wilderness. It speaks of desolation and barrenness—the enemy's accomplished work. Seeing an owl in prayer indicates a demonic stronghold.

### Chinese Interpretation

在许多文化中，猫头鹰代表智慧——在正面的梦中，它可能意味着智慧。在圣经中，猫头鹰总是负面的——不洁的，夜行的，栖息在荒野。它象征荒凉和贫瘠——仇敌完成的工作。祷告中看见猫头鹰表示邪灵的据点。

### Core Points

1. **正负皆可**: 文化和圣经含义不同
2. **智慧象征**: 文化中可能代表智慧
3. **荒凉记号**: 圣经中代表荒废
4. **仇敌据点**: 可能是邪灵工作

### Narrative Snippets

- `[ns_dav_o008]` `[trigger: owl_wisdom]` `[factor_trigger: dream_owl AND dream_wisdom]` `[role: 主干]` In many cultures, an owl represents wisdom—if positive, it may indicate the need for wisdom. → 在许多文化中，猫头鹰代表智慧——如果是正面的，它可能表示需要智慧。
- `[ns_dav_o009]` `[trigger: owl_desolation]` `[factor_trigger: dream_owl AND dream_desolation]` `[role: 警告]` In Scripture, an owl speaks of desolation and barrenness—indicating a demonic stronghold. → 在圣经中，猫头鹰象征荒凉和贫瘠——表示邪灵的据点。"""
    normalized_text_zh: str = """"""
    subject: str = "Owl 猫头鹰/智慧或荒凉"
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
        l1_anchor="dvd_v1.0.0_owl_猫头鹰_智慧或荒凉_001_L1",
    )
    version: str = "1.0.0"
