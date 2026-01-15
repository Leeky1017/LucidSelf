"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.412255
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
    semantic_id="dvd_v1.0.0_frogs_青蛙_污秽_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Frogs青蛙污秽(SemanticEntry):
    """
    ### Source Text

> **Frogs**: A picture of unclean spirits and demonic deception.
> Revelation 16:13...
    """
    
    original_text: str = """### Source Text

> **Frogs**: A picture of unclean spirits and demonic deception.
> Revelation 16:13 "And I saw three unclean spirits like frogs come out of the mouth of the dragon, and out of the mouth of the beast, and out of the mouth of the false prophet."
> Frogs were a plague in Egypt. They represent unclean spirits and false prophecy.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Frogs | 青蛙 | 污秽的灵 |
| Unclean spirits | 污秽的灵 | 邪灵的一种 |
| Plague | 灾祸 | 神的审判 |
| False prophecy | 假预言 | 欺骗的话语 |

### English Paraphrase

Frogs represent unclean spirits and demonic deception. In Revelation, unclean spirits like frogs came from the dragon, beast, and false prophet. Frogs were a plague in Egypt—they represent unclean spirits and false prophecy.

### Chinese Interpretation

青蛙代表污秽的灵和邪灵的迷惑。在启示录中，污秽的灵如青蛙从龙、兽和假先知口中出来。青蛙是埃及的灾祸——它们代表污秽的灵和假预言。

### Core Points

1. **始终负面**: 青蛙代表污秽的灵
2. **假预言**: 欺骗性的话语
3. **灾祸记号**: 埃及十灾之一
4. **邪灵象征**: 从仇敌口中出来

### Narrative Snippets

- `[ns_dav_f023]` `[trigger: frogs_unclean]` `[factor_trigger: dream_frogs AND dream_unclean]` `[role: 警告]` Unclean spirits like frogs came out of the dragon's mouth—frogs represent demonic deception. → 污秽的灵如青蛙从龙口中出来——青蛙代表邪灵的迷惑。"""
    normalized_text_zh: str = """"""
    subject: str = "Frogs 青蛙/污秽"
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
        l1_anchor="dvd_v1.0.0_frogs_青蛙_污秽_001_L1",
    )
    version: str = "1.0.0"
