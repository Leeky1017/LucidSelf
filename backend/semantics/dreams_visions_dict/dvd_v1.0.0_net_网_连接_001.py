"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.433421
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
    semantic_id="dvd_v1.0.0_net_网_连接_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Net网连接(SemanticEntry):
    """
    ### Source Text

> **Net**: If positive, a net represents mass evangelism or connecting with others—...
    """
    
    original_text: str = """### Source Text

> **Net**: If positive, a net represents mass evangelism or connecting with others—being part of a group. Negatively, it speaks of the snare of the enemy.
> Positive: A net in fishing speaks of evangelism, provision and blessing. Being part of a network of believers.
> Negative: The enemy using a net to snare and steal. People bound in nets—negative words and curses spoken over them.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Net | 网 | 连接或网罗 |
| Evangelism | 传福音 | 得人如得鱼 |
| Network | 网络 | 信徒的团契 |
| Snare | 网罗 | 仇敌的陷阱 |

### English Paraphrase

A net positively represents evangelism, connecting with others, and being part of a group. In fishing, it speaks of provision and blessing. Negatively, it's the enemy's snare to steal. People bound in nets represent negative words and curses spoken over them.

### Chinese Interpretation

网正面代表传福音、与他人连接和成为群体的一部分。在捕鱼中，它象征供应和祝福。负面而言，它是仇敌偷窃的网罗。被绑在网中的人代表被说在他们身上的负面话和咒诅。

### Core Points

1. **正负皆可**: 使用方式决定含义
2. **传福音象征**: 得人如得鱼
3. **团契记号**: 信徒的连接
4. **网罗警告**: 仇敌的陷阱

### Narrative Snippets

- `[ns_dav_n009]` `[trigger: net_evangelism]` `[factor_trigger: dream_net AND dream_evangelism]` `[role: 主干]` A net in fishing speaks of evangelism, the Lord bringing provision and blessing. → 捕鱼中的网象征传福音，主带来供应和祝福。
- `[ns_dav_n010]` `[trigger: net_snare]` `[factor_trigger: dream_net AND dream_snare]` `[role: 警告]` People bound in nets represent negative words and curses spoken over them by the enemy. → 被绑在网中的人代表仇敌说在他们身上的负面话和咒诅。"""
    normalized_text_zh: str = """"""
    subject: str = "Net 网/连接"
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
        l1_anchor="dvd_v1.0.0_net_网_连接_001_L1",
    )
    version: str = "1.0.0"
