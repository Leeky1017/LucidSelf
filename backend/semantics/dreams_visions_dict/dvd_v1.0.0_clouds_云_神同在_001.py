"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.419818
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
    semantic_id="dvd_v1.0.0_clouds_云_神同在_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Clouds云神同在(SemanticEntry):
    """
    ### Source Text

> **Clouds**: Often a picture of the presence of God. Also can represent a coming c...
    """
    
    original_text: str = """### Source Text

> **Clouds**: Often a picture of the presence of God. Also can represent a coming change.
> The cloud of God's presence led Israel through the wilderness. To see clouds in a vision often speaks of the presence and glory of the Lord. Storm clouds can represent trouble coming.
> Exodus 13:21 "And the LORD went before them by day in a pillar of a cloud."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Clouds | 云 | 神的同在 |
| Presence | 同在 | 神的荣耀临到 |
| Glory | 荣耀 | 神显现的形式 |
| Storm | 风暴 | 麻烦或改变 |

### English Paraphrase

Clouds often represent the presence and glory of God. The pillar of cloud led Israel through the wilderness. To see clouds in a vision speaks of God's presence. Storm clouds can represent trouble coming or a time of shaking.

### Chinese Interpretation

云常常代表神的同在和荣耀。云柱引导以色列人走过旷野。在异象中看见云象征神的同在。风暴云可能代表麻烦来临或震动的时刻。

### Core Points

1. **正负皆可**: 云的类型决定含义
2. **神同在**: 最常见的正面含义
3. **引导象征**: 神用云柱引导祂的百姓
4. **风暴警告**: 风暴云代表麻烦或改变

### Narrative Snippets

- `[ns_dav_c032]` `[trigger: clouds_presence]` `[factor_trigger: dream_clouds AND dream_presence]` `[role: 主干]` Clouds often represent the presence and glory of God—the pillar of cloud led Israel through the wilderness. → 云常常代表神的同在和荣耀——云柱引导以色列人走过旷野。
- `[ns_dav_c033]` `[trigger: clouds_storm]` `[factor_trigger: dream_clouds AND dream_storm]` `[role: 警告]` Storm clouds can represent trouble coming or a time of shaking and change. → 风暴云可能代表麻烦来临或震动和改变的时刻。"""
    normalized_text_zh: str = """"""
    subject: str = "Clouds 云/神同在"
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
        l1_anchor="dvd_v1.0.0_clouds_云_神同在_001_L1",
    )
    version: str = "1.0.0"
