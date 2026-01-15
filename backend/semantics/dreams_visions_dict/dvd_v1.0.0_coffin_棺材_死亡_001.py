"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.419859
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
    semantic_id="dvd_v1.0.0_coffin_棺材_死亡_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Coffin棺材死亡(SemanticEntry):
    """
    ### Source Text

> **Coffin**: A picture of death to the flesh or of a season ending. Can also speak...
    """
    
    original_text: str = """### Source Text

> **Coffin**: A picture of death to the flesh or of a season ending. Can also speak of the work of the enemy.
> Dreaming of coffins and dead bodies often refers to things in your flesh that are being brought to death. Do not panic—this need not be literal death.
> Positive: Old things passing away so the new can come. Negative: The work of the enemy stealing life.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Coffin | 棺材 | 死亡和结束 |
| Death | 死亡 | 肉体或季节的终结 |
| Flesh | 肉体 | 需要死去的旧人 |
| Resurrection | 复活 | 死后的新生 |

### English Paraphrase

A coffin represents death to the flesh or a season ending. Dreaming of coffins often refers to things in your flesh being brought to death—old issues dying so the new can come. Negatively, it can speak of the enemy's work stealing life.

### Chinese Interpretation

棺材代表肉体的死亡或季节的终结。梦见棺材常常指肉体中的事物正在被处死——旧问题死去以便新事物来临。负面而言，它可能象征仇敌偷窃生命的工作。

### Core Points

1. **正负皆可**: 上下文决定含义
2. **肉体对付**: 旧人需要被钉死
3. **季节转换**: 旧季节结束新季节开始
4. **复活预备**: 死亡是复活的前奏

### Narrative Snippets

- `[ns_dav_c037]` `[trigger: coffin_flesh]` `[factor_trigger: dream_coffin AND dream_flesh_death]` `[role: 主干]` Dreaming of coffins often refers to things in your flesh being brought to death—old issues dying. → 梦见棺材常指肉体中的事物正在被处死——旧问题正在死去。
- `[ns_dav_c038]` `[trigger: coffin_enemy]` `[factor_trigger: dream_coffin AND dream_enemy]` `[role: 警告]` In a negative context, a coffin speaks of the work of the enemy stealing life and destiny. → 负面而言，棺材象征仇敌偷窃生命和命定的工作。"""
    normalized_text_zh: str = """"""
    subject: str = "Coffin 棺材/死亡"
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
        l1_anchor="dvd_v1.0.0_coffin_棺材_死亡_001_L1",
    )
    version: str = "1.0.0"
