"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.443962
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
    semantic_id="dvd_v1.0.0_lion_狮子_王权_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Lion狮子王权(SemanticEntry):
    """
    ### Source Text

> **Lion**: Royalty, strength, the Lord Jesus and defender of the righteous. On a n...
    """
    
    original_text: str = """### Source Text

> **Lion**: Royalty, strength, the Lord Jesus and defender of the righteous. On a negative note: destruction, Satan, uncleanness and theft.
> Positive: Jesus is the Lion of the tribe of Judah—your defender as a king of strength, able to protect you.
> Negative: The enemy is referred to as a roaring lion seeking whom he may devour. In negative context, a lion represents a spirit of destruction.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Lion | 狮子 | 王权和力量 |
| Lion of Judah | 犹大的狮子 | 耶稣基督 |
| Roaring lion | 吼叫的狮子 | 撒但 |
| Destruction | 毁灭 | 仇敌的工作 |

### English Paraphrase

A lion represents royalty, strength, and Jesus as defender. The Lion of the tribe of Judah is Christ—your king of strength and protector. Negatively, a roaring lion is Satan seeking to devour. A lion in negative context represents a spirit of destruction.

### Chinese Interpretation

狮子代表王权、力量和耶稣作为保护者。犹大支派的狮子是基督——你力量的王和保护者。负面而言，吼叫的狮子是撒但寻找可吞吃的人。负面语境中的狮子代表毁灭的灵。

### Core Points

1. **正负皆可**: 狮子阵营决定含义
2. **王权象征**: 力量和保护
3. **基督狮子**: 犹大支派的狮子
4. **仇敌警告**: 撒但如吼叫的狮子

### Narrative Snippets

- `[ns_dav_l011]` `[trigger: lion_judah]` `[factor_trigger: dream_lion AND dream_judah]` `[role: 主干]` The Lion of the tribe of Judah is Jesus—your defender, king of strength, able to protect you. → 犹大支派的狮子是耶稣——你的保护者，力量的王，能保护你。
- `[ns_dav_l012]` `[trigger: lion_enemy]` `[factor_trigger: dream_lion AND dream_enemy]` `[role: 警告]` The devil as a roaring lion walks about seeking whom he may devour. → 魔鬼如同吼叫的狮子遍地游行，寻找可吞吃的人。"""
    normalized_text_zh: str = """"""
    subject: str = "Lion 狮子/王权"
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
        l1_anchor="dvd_v1.0.0_lion_狮子_王权_001_L1",
    )
    version: str = "1.0.0"
