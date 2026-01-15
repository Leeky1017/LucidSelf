"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.419751
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
    semantic_id="dvd_v1.0.0_chains_锁链_捆绑_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Chains锁链捆绑(SemanticEntry):
    """
    ### Source Text

> **Chains**: A picture of bondage and spiritual imprisonment.
> Just as in the cas...
    """
    
    original_text: str = """### Source Text

> **Chains**: A picture of bondage and spiritual imprisonment.
> Just as in the case with Delilah and Samson, the enemy seeks to bind you up so that you cannot move and then to destroy you. All is not lost though because you have the authority in the name of Jesus to break free.
> Judges 16:6 "And Delilah said to Samson, Tell me, I pray you, in which your great strength lies, and with which you might be bound to afflict you."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Chains | 锁链 | 捆绑和囚禁的象征 |
| Bondage | 捆绑 | 无法自由行动 |
| Authority | 权柄 | 奉耶稣的名得释放 |
| Affliction | 苦害 | 仇敌的攻击目的 |

### English Paraphrase

Chains represent bondage and spiritual imprisonment. Like Delilah binding Samson, the enemy seeks to restrict you so you cannot move, then destroy you. But you have authority in Jesus' name to break free from every chain.

### Chinese Interpretation

锁链代表捆绑和属灵的囚禁。就像大利拉捆绑参孙一样，仇敌试图限制你使你无法行动，然后毁灭你。但你有奉耶稣之名的权柄可以挣脱一切锁链。

### Core Points

1. **始终负面**: 锁链总是代表仇敌的工作
2. **释放可能**: 奉耶稣的名可以得自由
3. **识别来源**: 可能来自个人罪、世代咒诅或联结
4. **争战必要**: 需要属灵争战才能脱离

### Narrative Snippets

- `[ns_dav_c020]` `[trigger: chains_bondage]` `[factor_trigger: dream_chains AND dream_bondage]` `[role: 主干]` Chains speak of bondage and spiritual imprisonment—the enemy seeks to bind you so you cannot move. → 锁链象征捆绑和属灵囚禁，仇敌要束缚你使你无法行动。
- `[ns_dav_c021]` `[trigger: chains_authority]` `[factor_trigger: dream_chains AND dream_authority]` `[role: 解决]` You have authority in Jesus' name to break free from every chain of bondage. → 你有奉耶稣之名的权柄可以挣脱一切捆绑的锁链。"""
    normalized_text_zh: str = """"""
    subject: str = "Chains 锁链/捆绑"
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
        l1_anchor="dvd_v1.0.0_chains_锁链_捆绑_001_L1",
    )
    version: str = "1.0.0"
