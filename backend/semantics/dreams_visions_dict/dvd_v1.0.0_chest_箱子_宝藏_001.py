"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.419759
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
    semantic_id="dvd_v1.0.0_chest_箱子_宝藏_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Chest箱子宝藏(SemanticEntry):
    """
    ### Source Text

> **Chest**: A treasure box. In dreams this often represents what is hidden within ...
    """
    
    original_text: str = """### Source Text

> **Chest**: A treasure box. In dreams this often represents what is hidden within a person.
> A chest is a container used to store treasures. To dream or see a vision of a chest speaks of the treasures that are either given to you or hidden in your heart.
> Matthew 6:21 "For where your treasure is, there will your heart be also."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Chest | 箱子 | 宝藏容器 |
| Treasure | 宝藏 | 心中隐藏的珍贵事物 |
| Heart | 心 | 人内在的核心 |
| Hidden | 隐藏 | 尚未显露的事物 |

### English Paraphrase

A chest represents a treasure box—what is hidden within a person. To dream of a chest speaks of treasures given to you or hidden in your heart. What you treasure reveals your heart's condition.

### Chinese Interpretation

箱子代表宝盒——人内心隐藏的事物。梦见箱子象征给予你的宝藏或心中隐藏的珍贵事物。你所珍惜的东西揭示你的心态。

### Core Points

1. **正负皆可**: 内容决定含义
2. **内心象征**: 代表心中隐藏的事物
3. **揭示价值**: 你珍惜什么就在乎什么
4. **恩赐容器**: 可能代表属灵恩赐

### Narrative Snippets

- `[ns_dav_c022]` `[trigger: chest_treasure]` `[factor_trigger: dream_chest AND dream_treasure]` `[role: 主干]` A chest speaks of treasures hidden in your heart—what you treasure reveals your heart's condition. → 箱子象征心中隐藏的宝藏，你所珍惜的揭示你的心态。"""
    normalized_text_zh: str = """"""
    subject: str = "Chest 箱子/宝藏"
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
        l1_anchor="dvd_v1.0.0_chest_箱子_宝藏_001_L1",
    )
    version: str = "1.0.0"
