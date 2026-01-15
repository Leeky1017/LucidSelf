"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.450519
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
    semantic_id="dvd_v1.0.0_hand_手_能力_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Hand手能力(SemanticEntry):
    """
    ### Source Text

> **Hand**: In an internal dream, your hand is a picture of your strength and abili...
    """
    
    original_text: str = """### Source Text

> **Hand**: In an internal dream, your hand is a picture of your strength and abilities. In a prophetic dream or vision, it is a picture of the blessing and deliverance of the Lord.
> Right Hand: Speaks of a place of honor and power—an appointed position.
> Negative: A black hand speaks of the work of the enemy—stealing blessings.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Hand | 手 | 能力和祝福 |
| Strength | 力量 | 个人能力 |
| Right hand | 右手 | 尊荣和权能的位置 |
| Black hand | 黑手 | 仇敌的工作 |

### English Paraphrase

The hand represents strength and abilities in internal dreams. In prophetic dreams, it pictures God's blessing and deliverance. The right hand speaks of honor and power. A black hand indicates the enemy's work to steal blessings.

### Chinese Interpretation

在内在梦中，手代表力量和能力。在先知性梦中，它象征神的祝福和拯救。右手象征尊荣和权能。黑手表示仇敌偷窃祝福的工作。

### Core Points

1. **正负皆可**: 手的颜色和动作决定含义
2. **能力象征**: 个人的力量和才干
3. **神能记号**: 神的祝福和拯救
4. **仇敌警告**: 黑手是偷窃的工作

### Narrative Snippets

- `[ns_dav_h003]` `[trigger: hand_blessing]` `[factor_trigger: dream_hand AND dream_blessing]` `[role: 主干]` The hand is a picture of the blessing and deliverance of the Lord—fighting for us and providing. → 手是主祝福和拯救的象征——为我们争战和供应。
- `[ns_dav_h004]` `[trigger: hand_enemy]` `[factor_trigger: dream_hand AND dream_enemy]` `[role: 警告]` A black hand in the spirit speaks of the work of the enemy—seeking to steal blessings. → 灵里的黑手象征仇敌的工作——企图偷窃祝福。"""
    normalized_text_zh: str = """"""
    subject: str = "Hand 手/能力"
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
        l1_anchor="dvd_v1.0.0_hand_手_能力_001_L1",
    )
    version: str = "1.0.0"
