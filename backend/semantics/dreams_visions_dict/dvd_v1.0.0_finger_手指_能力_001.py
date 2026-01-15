"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.412156
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
    semantic_id="dvd_v1.0.0_finger_手指_能力_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Finger手指能力(SemanticEntry):
    """
    ### Source Text

> **Finger**: A picture of the power and ability of God. Also speaks of pointing di...
    """
    
    original_text: str = """### Source Text

> **Finger**: A picture of the power and ability of God. Also speaks of pointing direction.
> Positive: The finger of God wrote the commandments. The Holy Spirit is the finger of God working in our lives.
> Negative: A pointed finger speaks of accusation or judgment.
> Luke 11:20 "But if I with the finger of God cast out demons, then the kingdom of God has come upon you."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Finger | 手指 | 神的能力 |
| Power | 能力 | 行神迹的能力 |
| Direction | 方向 | 指引道路 |
| Accusation | 控告 | 指责和审判 |

### English Paraphrase

A finger represents God's power and ability—also pointing direction. The finger of God wrote the commandments and casts out demons. A pointed finger speaks of accusation or judgment. Missing fingers indicate lack of ability.

### Chinese Interpretation

手指代表神的能力——也指引方向。神的手指写下诫命并赶出邪灵。指着的手指象征控告或审判。缺少手指表示缺乏能力。

### Core Points

1. **正负皆可**: 手指动作决定含义
2. **神能象征**: 神的手指行神迹
3. **方向指引**: 指向道路和选择
4. **控告警告**: 指着的手指是控告

### Narrative Snippets

- `[ns_dav_f008]` `[trigger: finger_power]` `[factor_trigger: dream_finger AND dream_power]` `[role: 主干]` If I with the finger of God cast out demons—the finger represents God's power at work. → 我若靠着神的手指赶鬼——手指代表神能力的运作。
- `[ns_dav_f009]` `[trigger: finger_accuse]` `[factor_trigger: dream_finger AND dream_accusation]` `[role: 警告]` A pointed finger speaks of accusation—the enemy accusing you or you accusing others. → 指着的手指象征控告——仇敌控告你或你控告他人。"""
    normalized_text_zh: str = """"""
    subject: str = "Finger 手指/能力"
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
        l1_anchor="dvd_v1.0.0_finger_手指_能力_001_L1",
    )
    version: str = "1.0.0"
