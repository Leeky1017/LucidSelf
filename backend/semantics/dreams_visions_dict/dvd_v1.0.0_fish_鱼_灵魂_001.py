"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.412172
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
    semantic_id="dvd_v1.0.0_fish_鱼_灵魂_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Fish鱼灵魂(SemanticEntry):
    """
    ### Source Text

> **Fish**: A picture of souls or people. Also represents provision.
> Positive: Ca...
    """
    
    original_text: str = """### Source Text

> **Fish**: A picture of souls or people. Also represents provision.
> Positive: Catching fish speaks of evangelism. The disciples were called to be fishers of men. Fish also represents miraculous provision (loaves and fishes).
> Negative: Dead fish or rotten fish speaks of lifeless souls or contaminated ministry.
> Matthew 4:19 "Follow me, and I will make you fishers of men."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Fish | 鱼 | 灵魂和供应 |
| Souls | 灵魂 | 需要拯救的人 |
| Provision | 供应 | 神迹供应 |
| Evangelism | 传福音 | 得人渔夫 |

### English Paraphrase

Fish represent souls or people—also provision. Catching fish speaks of evangelism, being fishers of men. Fish also represents miraculous provision. Dead or rotten fish speaks of lifeless souls or contaminated ministry.

### Chinese Interpretation

鱼代表灵魂或人——也代表供应。捕鱼象征传福音，作得人的渔夫。鱼也代表神迹的供应。死鱼或烂鱼象征没有生命的灵魂或污染的事工。

### Core Points

1. **正负皆可**: 鱼的状态决定含义
2. **灵魂象征**: 需要拯救的人
3. **传道呼召**: 得人的渔夫
4. **供应记号**: 五饼二鱼的神迹

### Narrative Snippets

- `[ns_dav_f012]` `[trigger: fish_souls]` `[factor_trigger: dream_fish AND dream_souls]` `[role: 主干]` Follow me and I will make you fishers of men—fish represent souls to be won for the Kingdom. → 来跟从我，我要叫你们得人如得鱼——鱼代表要为神国赢得的灵魂。"""
    normalized_text_zh: str = """"""
    subject: str = "Fish 鱼/灵魂"
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
        l1_anchor="dvd_v1.0.0_fish_鱼_灵魂_001_L1",
    )
    version: str = "1.0.0"
