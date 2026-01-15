"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.450592
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
    semantic_id="dvd_v1.0.0_horseshoe_马蹄铁_迷信_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Horseshoe马蹄铁迷信(SemanticEntry):
    """
    ### Source Text

> **Horseshoe**: Many believe in the superstition that the horseshoe brings good lu...
    """
    
    original_text: str = """### Source Text

> **Horseshoe**: Many believe in the superstition that the horseshoe brings good luck. This has no place in the Body of Christ. If you see a horseshoe when praying for someone, the Lord is telling you they have held onto superstitious beliefs.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Horseshoe | 马蹄铁 | 迷信的象征 |
| Superstition | 迷信 | 不属于神的信念 |
| Luck | 运气 | 虚假的保护 |
| Beliefs | 信念 | 需要对付的 |

### English Paraphrase

A horseshoe represents superstitious beliefs that have no place in the Body of Christ. If you see a horseshoe when praying for someone, the Lord is indicating they have held onto superstitious beliefs that need to be addressed.

### Chinese Interpretation

马蹄铁代表在基督身体中没有位置的迷信信念。如果你为某人祷告时看见马蹄铁，主在表明他们持有需要处理的迷信信念。

### Core Points

1. **始终负面**: 马蹄铁代表迷信
2. **错误信念**: 不属于神的信念
3. **需要对付**: 必须弃绝迷信
4. **代祷提示**: 为人祷告时的指引

### Narrative Snippets

- `[ns_dav_h016]` `[trigger: horseshoe_superstition]` `[factor_trigger: dream_horseshoe AND dream_superstition]` `[role: 警告]` A horseshoe represents superstitious beliefs that have no place in the Body of Christ. → 马蹄铁代表在基督身体中没有位置的迷信信念。"""
    normalized_text_zh: str = """"""
    subject: str = "Horseshoe 马蹄铁/迷信"
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
        l1_anchor="dvd_v1.0.0_horseshoe_马蹄铁_迷信_001_L1",
    )
    version: str = "1.0.0"
