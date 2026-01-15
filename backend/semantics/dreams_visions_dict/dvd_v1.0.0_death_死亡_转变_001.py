"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.401990
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
    semantic_id="dvd_v1.0.0_death_死亡_转变_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Death死亡转变(SemanticEntry):
    """
    ### Source Text

> **Death**: A call to spiritual death that will lead to resurrection. Negatively i...
    """
    
    original_text: str = """### Source Text

> **Death**: A call to spiritual death that will lead to resurrection. Negatively it speaks of the work of the enemy.
> Dreaming of dead bodies and coffins often refers to things in your flesh being brought to death. Do not panic! It is important to identify the person dying. An unknown male figure—intellect being brought to death. An unknown female—creative side being brought to death.
> Revelation 21:4 "And God shall wipe away all tears...there shall be no more death."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Death | 死亡 | 属灵的死和复活 |
| Flesh | 肉体 | 需要死去的部分 |
| Resurrection | 复活 | 死后的新生 |
| Enemy | 仇敌 | 偷窃生命的工作 |

### English Paraphrase

Death represents a call to spiritual death leading to resurrection. Dreaming of dead bodies often refers to flesh being brought to death. Identify the dying person: unknown male = intellect dying; unknown female = creativity dying. Negatively, it speaks of the enemy's work stealing life.

### Chinese Interpretation

死亡代表属灵死亡的呼召，通向复活。梦见尸体常常指肉体正在被处死。辨认死去的人：不认识的男性=理智被处死；不认识的女性=创造力被处死。负面而言，它象征仇敌偷窃生命的工作。

### Core Points

1. **正负皆可**: 上下文决定含义
2. **肉体对付**: 旧人需要死去
3. **复活预备**: 死亡是新生的前奏
4. **辨认对象**: 死去的人代表什么

### Narrative Snippets

- `[ns_dav_d010]` `[trigger: death_flesh]` `[factor_trigger: dream_death AND dream_flesh]` `[role: 主干]` Dreaming of dead bodies often refers to things in your flesh being brought to death—do not panic. → 梦见尸体常指你肉体中的事物正在被处死——不要惊慌。
- `[ns_dav_d011]` `[trigger: death_enemy]` `[factor_trigger: dream_death AND dream_enemy]` `[role: 警告]` Satan is the author of death—in the spirit, death is epitomized as darkness and evil. → 撒但是死亡的制造者——在灵里，死亡是黑暗和邪恶的化身。"""
    normalized_text_zh: str = """"""
    subject: str = "Death 死亡/转变"
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
        l1_anchor="dvd_v1.0.0_death_死亡_转变_001_L1",
    )
    version: str = "1.0.0"
