"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.433390
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
    semantic_id="dvd_v1.0.0_neck_颈_力量_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Neck颈力量(SemanticEntry):
    """
    ### Source Text

> **Neck**: A neck holds up and turns the head—speaks of strength and direction. A ...
    """
    
    original_text: str = """### Source Text

> **Neck**: A neck holds up and turns the head—speaks of strength and direction. A broken neck means instant death, so it also pictures your life.
> Positive: Laying down your neck means giving your life for someone. A strong neck is a picture of strength.
> Negative: A yoke on your neck speaks of cares put on you by others. Stiff-necked speaks of stubbornness and pride.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Neck | 颈 | 力量和方向 |
| Yoke | 轭 | 被强加的重担 |
| Stiff-necked | 硬着颈项 | 顽固和骄傲 |
| Strength | 力量 | 支撑的能力 |

### English Paraphrase

The neck holds up and turns the head—speaking of strength and direction. A broken neck means death, so it pictures your life. Laying down your neck means giving your life for others. A strong neck is strength. A yoke speaks of cares imposed by others. Stiff-necked means stubbornness and pride.

### Chinese Interpretation

颈支撑和转动头——象征力量和方向。颈断意味着死亡，所以它象征你的生命。舍下你的颈意味着为他人舍命。强壮的颈是力量。轭象征被他人强加的重担。硬着颈项意味着顽固和骄傲。

### Core Points

1. **正负皆可**: 状态决定含义
2. **力量象征**: 支撑和方向
3. **舍命记号**: 为他人舍下
4. **骄傲警告**: 硬颈是顽固

### Narrative Snippets

- `[ns_dav_n005]` `[trigger: neck_strength]` `[factor_trigger: dream_neck AND dream_strength]` `[role: 主干]` A strong neck is a picture of strength—supporting the head and determining direction. → 强壮的颈是力量的象征——支撑头并决定方向。
- `[ns_dav_n006]` `[trigger: neck_stiff]` `[factor_trigger: dream_neck AND dream_stubbornness]` `[role: 警告]` Stiff-necked speaks of being stubborn and insisting on doing your own thing instead of obeying the Lord. → 硬着颈项象征顽固和坚持自己的方式而不顺服主。"""
    normalized_text_zh: str = """"""
    subject: str = "Neck 颈/力量"
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
        l1_anchor="dvd_v1.0.0_neck_颈_力量_001_L1",
    )
    version: str = "1.0.0"
