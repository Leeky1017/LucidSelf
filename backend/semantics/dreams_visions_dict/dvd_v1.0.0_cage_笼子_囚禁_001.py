"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.419634
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
    semantic_id="dvd_v1.0.0_cage_笼子_囚禁_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Cage笼子囚禁(SemanticEntry):
    """
    ### Source Text

> **Cage**: To have your freedom taken away. A place of restriction and oppression....
    """
    
    original_text: str = """### Source Text

> **Cage**: To have your freedom taken away. A place of restriction and oppression.
> In dreaming that you are in a cage or being held captive, it would represent your lack of freedom. This would indicate that you are bound either by your circumstance, by your past or by some form of oppression.
> Jeremiah 5:26-27: "For among my people are found wicked men: they lay wait, as he that sets snares; they set a trap, they catch men. As a cage is full of birds, so are their houses full of deceit."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Cage | 笼子 | 限制自由的象征 |
| Restriction | 限制 | 阻碍行动或成长 |
| Oppression | 压迫 | 精神或情感的束缚 |
| Bondage | 捆绑 | 被过去或环境困住 |

### English Paraphrase

A cage represents the loss of freedom and a state of restriction or oppression. In dreams, being in a cage signifies being bound by circumstances, past experiences, or some form of spiritual oppression. The enemy keeps you in bondage while the Lord gives freedom.

### Chinese Interpretation

笼子代表失去自由和处于限制或压迫的状态。在梦中，被关在笼子里象征着被环境、过去的经历或某种形式的属灵压迫所束缚。仇敌将人困在捆绑中，但主赐予自由。

### Core Points

1. **始终负面**: 笼子在梦境和异象中几乎没有正面含义
2. **捆绑象征**: 代表恶者的诡计和陷阱
3. **自我限制**: 有时人会将自己关在笼子里
4. **需要释放**: 呼召祷告和争战

### Narrative Snippets

- `[ns_dav_c001]` `[trigger: cage_bondage]` `[factor_trigger: dream_cage AND dream_bondage]` `[role: 主干]` A cage in an internal dream represents your lack of freedom—you are bound by circumstance, past, or oppression. → 笼子象征失去自由，被环境、过去或压迫所困。"""
    normalized_text_zh: str = """"""
    subject: str = "Cage 笼子/囚禁"
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
        l1_anchor="dvd_v1.0.0_cage_笼子_囚禁_001_L1",
    )
    version: str = "1.0.0"
