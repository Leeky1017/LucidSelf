"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.429324
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
    semantic_id="dvd_v1.0.0_kiss_亲吻_接纳_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Kiss亲吻接纳(SemanticEntry):
    """
    ### Source Text

> **Kiss**: A kiss speaks of intimacy and being vulnerable. It also speaks of openi...
    """
    
    original_text: str = """### Source Text

> **Kiss**: A kiss speaks of intimacy and being vulnerable. It also speaks of opening your heart to others. Kissing a person means accepting whatever that person represents.
> Positive: A kiss in Scripture was a greeting and sign of respect. The Lord giving you a kiss shows His affection.
> Negative: Judas' kiss is the perfect picture of betrayal—words that seem innocent but carry poison.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Kiss | 亲吻 | 亲密和接纳 |
| Intimacy | 亲密 | 敞开的心 |
| Vulnerable | 脆弱 | 愿意敞开 |
| Betrayal | 背叛 | 犹大之吻 |

### English Paraphrase

A kiss speaks of intimacy and vulnerability—opening your heart to others. Kissing means accepting what that person represents. The Lord's kiss shows His affection. Judas' kiss represents betrayal—words that seem innocent but carry poison.

### Chinese Interpretation

亲吻象征亲密和脆弱——向他人敞开你的心。亲吻意味着接受那人所代表的。主的亲吻显示祂的慈爱。犹大之吻代表背叛——看似无害却带着毒素的话语。

### Core Points

1. **正负皆可**: 对象决定含义
2. **亲密象征**: 敞开和接纳
3. **主的爱**: 神的慈爱表达
4. **背叛警告**: 犹大之吻是背叛

### Narrative Snippets

- `[ns_dav_j005]` `[trigger: kiss_accept]` `[factor_trigger: dream_kiss AND dream_acceptance]` `[role: 主干]` Kissing a person means accepting whatever that person represents in your life. → 亲吻一个人意味着接受那人在你生命中所代表的。
- `[ns_dav_j006]` `[trigger: kiss_betrayal]` `[factor_trigger: dream_kiss AND dream_betrayal]` `[role: 警告]` Judas' kiss represents betrayal—words that seem innocent but carry poison and destruction. → 犹大之吻代表背叛——看似无害却带着毒素和毁灭的话语。"""
    normalized_text_zh: str = """"""
    subject: str = "Kiss 亲吻/接纳"
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
        l1_anchor="dvd_v1.0.0_kiss_亲吻_接纳_001_L1",
    )
    version: str = "1.0.0"
