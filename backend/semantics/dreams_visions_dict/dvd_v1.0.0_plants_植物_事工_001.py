"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.405285
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
    semantic_id="dvd_v1.0.0_plants_植物_事工_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Plants植物事工(SemanticEntry):
    """
    ### Source Text

> **Plants**: The work of your hands or God's work in your ministry. Plants are sea...
    """
    
    original_text: str = """### Source Text

> **Plants**: The work of your hands or God's work in your ministry. Plants are seasonal and represent a specific season in your life. A new ministry is like a seedling; a mature ministry is a sturdy tree. Flourishing plant means going in the right direction.
> Negative: A seasonal plant that dies represents a season that has ended. Dead plant from lack of water means lacking the Spirit of God.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Plants | 植物 | 手的工作 |
| Season | 季节 | 生命的阶段 |
| Flourishing | 繁茂 | 方向正确 |
| Dead | 死亡 | 季节结束 |

### English Paraphrase

Plants represent your work or God's work in ministry. They are seasonal—representing life stages. A seedling is new ministry; a sturdy tree is mature ministry. Flourishing means right direction. A dead plant means a season has ended. Death from lack of water means lacking God's Spirit.

### Chinese Interpretation

植物代表你的工作或神在事工中的工作。它们是季节性的——代表生命的阶段。幼苗是新事工；茁壮的树是成熟的事工。繁茂意味着方向正确。死亡的植物意味着季节结束。因缺水而死意味着缺乏神的灵。

### Core Points

1. **正负皆可**: 植物状态决定含义
2. **事工象征**: 手中的工作
3. **季节记号**: 生命的不同阶段
4. **缺乏警告**: 可能缺少神的灵

### Narrative Snippets

- `[ns_dav_p009]` `[trigger: plants_flourish]` `[factor_trigger: dream_plants AND dream_flourish]` `[role: 主干]` A flourishing plant means whatever you are working on, you are going in the right direction! → 繁茂的植物意味着无论你在做什么，你都在正确的方向上！
- `[ns_dav_p010]` `[trigger: plants_dead]` `[factor_trigger: dream_plants AND dream_dead]` `[role: 警告]` A plant that dies from lack of water means you are lacking the Spirit of God in this area. → 因缺水而死的植物意味着你在这个领域缺乏神的灵。"""
    normalized_text_zh: str = """"""
    subject: str = "Plants 植物/事工"
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
        l1_anchor="dvd_v1.0.0_plants_植物_事工_001_L1",
    )
    version: str = "1.0.0"
