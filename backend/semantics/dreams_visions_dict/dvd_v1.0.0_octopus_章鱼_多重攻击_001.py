"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.433463
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
    semantic_id="dvd_v1.0.0_octopus_章鱼_多重攻击_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Octopus章鱼多重攻击(SemanticEntry):
    """
    ### Source Text

> **Octopus**: A work of the enemy. Specifically a combination of attacks on your h...
    """
    
    original_text: str = """### Source Text

> **Octopus**: A work of the enemy. Specifically a combination of attacks on your health or finances. Each time it was when seeking the Lord regarding physical attack. It is a good picture because it feels like facing many different attacks, but they all have the same source. You have authority in Jesus' name to tell the enemy to leave!

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Octopus | 章鱼 | 多重攻击 |
| Combination | 组合 | 多方面的攻击 |
| Source | 源头 | 同一个仇敌 |
| Authority | 权柄 | 耶稣的名 |

### English Paraphrase

An octopus represents the enemy's work—a combination of attacks on health or finances. It feels like many different attacks, but they have the same source. You have authority in Jesus' name to tell the enemy to leave!

### Chinese Interpretation

章鱼代表仇敌的工作——对健康或财务的多重攻击组合。感觉像面对许多不同的攻击，但它们有同一个源头。你有耶稣名的权柄命令仇敌离开！

### Core Points

1. **始终负面**: 章鱼代表仇敌
2. **多重攻击**: 同时面对多方面
3. **同一源头**: 所有攻击来自一处
4. **权柄对付**: 奉耶稣的名斥责

### Narrative Snippets

- `[ns_dav_o003]` `[trigger: octopus_attack]` `[factor_trigger: dream_octopus AND dream_attack]` `[role: 警告]` An octopus represents a combination of attacks from one source—you have authority in Jesus to command it to leave! → 章鱼代表来自一个源头的多重攻击组合——你有耶稣的权柄命令它离开！"""
    normalized_text_zh: str = """"""
    subject: str = "Octopus 章鱼/多重攻击"
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
        l1_anchor="dvd_v1.0.0_octopus_章鱼_多重攻击_001_L1",
    )
    version: str = "1.0.0"
