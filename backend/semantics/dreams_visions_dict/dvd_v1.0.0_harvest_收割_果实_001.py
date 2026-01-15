"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.450540
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
    semantic_id="dvd_v1.0.0_harvest_收割_果实_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Harvest收割果实(SemanticEntry):
    """
    ### Source Text

> **Harvest**: Reaping the financial and spiritual fruits of your hard labor. A har...
    """
    
    original_text: str = """### Source Text

> **Harvest**: Reaping the financial and spiritual fruits of your hard labor. A harvest only comes after you have worked hard and allowed the Lord to do His part. In ministry, a harvest is also a picture of reaching the lost.
> Negative: Weeds in your harvest mean you did not work according to God's plan or the enemy got in.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Harvest | 收割 | 劳动的果实 |
| Fruit | 果实 | 财务和属灵的收成 |
| Lost | 失丧的 | 需要拯救的灵魂 |
| Weeds | 杂草 | 仇敌的破坏 |

### English Paraphrase

Harvest represents reaping the fruits of your hard labor—financial and spiritual. A sickle in hand means the harvest is ready. In ministry, it pictures reaching the lost. Weeds in harvest indicate enemy interference or not following God's plan.

### Chinese Interpretation

收割代表收取你辛劳的果实——财务和属灵的。手中有镰刀意味着收割的时候到了。在事工中，它象征接触失丧的人。收割中有杂草表示仇敌的干扰或没有按神的计划行事。

### Core Points

1. **正负皆可**: 收成状态决定含义
2. **劳动成果**: 辛勤工作的回报
3. **传道呼召**: 得人如得鱼
4. **杂草警告**: 可能表示仇敌干扰

### Narrative Snippets

- `[ns_dav_h006]` `[trigger: harvest_fruit]` `[factor_trigger: dream_harvest AND dream_fruit]` `[role: 主干]` Harvest represents reaping the financial and spiritual fruits of your hard labor. → 收割代表收取你辛劳的财务和属灵果实。
- `[ns_dav_h007]` `[trigger: harvest_lost]` `[factor_trigger: dream_harvest AND dream_souls]` `[role: 主干]` In ministry, a harvest is a picture of reaching the lost for the Lord. → 在事工中，收割象征为主接触失丧的人。"""
    normalized_text_zh: str = """"""
    subject: str = "Harvest 收割/果实"
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
        l1_anchor="dvd_v1.0.0_harvest_收割_果实_001_L1",
    )
    version: str = "1.0.0"
