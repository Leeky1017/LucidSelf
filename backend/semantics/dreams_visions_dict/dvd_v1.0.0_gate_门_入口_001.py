"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.390638
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
    semantic_id="dvd_v1.0.0_gate_门_入口_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Gate门入口(SemanticEntry):
    """
    ### Source Text

> **Gate**: A picture of entrance and access—new directions and opportunities.
> Si...
    """
    
    original_text: str = """### Source Text

> **Gate**: A picture of entrance and access—new directions and opportunities.
> Similar to "Door." Positive: An open gate speaks of access being granted. Walking through a gate indicates entering a new season. Negative: A closed gate indicates blocked access. A gate of the enemy refers to demonic strongholds.
> Genesis 22:17 "...your seed shall possess the gate of his enemies."
> Matthew 16:18 "...the gates of hell shall not prevail against it."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Gate | 门 | 入口和通道 |
| Access | 通道 | 进入的权利 |
| Opportunity | 机会 | 新的方向 |
| Stronghold | 坚固营垒 | 仇敌的门 |

### English Paraphrase

A gate represents entrance and access—new directions and opportunities. An open gate speaks of access being granted. Walking through a gate indicates entering a new season. A closed gate indicates blocked access. Gates of hell refer to demonic strongholds that will not prevail.

### Chinese Interpretation

门代表入口和通道——新的方向和机会。敞开的门象征被授予通道。走过门表示进入新季节。关闭的门表示通道被阻挡。阴间的门指邪灵的坚固营垒，必不能得胜。

### Core Points

1. **正负皆可**: 门的状态决定含义
2. **新季节**: 走过门进入新阶段
3. **通道象征**: 进入某领域的权利
4. **得胜应许**: 阴间的门不能得胜

### Narrative Snippets

- `[ns_dav_g001]` `[trigger: gate_access]` `[factor_trigger: dream_gate AND dream_access]` `[role: 主干]` An open gate speaks of access being granted—walking through indicates entering a new season. → 敞开的门象征被授予通道——走过去表示进入新季节。
- `[ns_dav_g002]` `[trigger: gate_hell]` `[factor_trigger: dream_gate AND dream_hell]` `[role: 主干]` The gates of hell shall not prevail—demonic strongholds cannot stand against the Church. → 阴间的门不能得胜——邪灵的坚固营垒不能抵挡教会。"""
    normalized_text_zh: str = """"""
    subject: str = "Gate 门/入口"
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
        l1_anchor="dvd_v1.0.0_gate_门_入口_001_L1",
    )
    version: str = "1.0.0"
