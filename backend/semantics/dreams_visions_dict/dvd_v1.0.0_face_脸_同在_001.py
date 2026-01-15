"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.412097
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
    semantic_id="dvd_v1.0.0_face_脸_同在_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Face脸同在(SemanticEntry):
    """
    ### Source Text

> **Face**: A picture of the presence of God or of a person. To see God's face is t...
    """
    
    original_text: str = """### Source Text

> **Face**: A picture of the presence of God or of a person. To see God's face is to see His favor. A negative face speaks of opposition.
> Numbers 6:25 "The LORD make his face shine upon you, and be gracious to you."
> Positive: God's face shining = favor. Negative: His face turned away = rejection.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Face | 脸 | 同在和恩惠 |
| Presence | 同在 | 神的临在 |
| Favor | 恩惠 | 神脸光照 |
| Opposition | 对抗 | 神转脸不看 |

### English Paraphrase

A face represents presence and favor. To see God's face is to experience His favor—His face shining upon you. A face turned away speaks of rejection or opposition. A distorted face indicates the enemy's presence.

### Chinese Interpretation

脸代表同在和恩惠。看见神的脸是经历祂的恩惠——祂的脸光照你。转离的脸象征拒绝或对抗。扭曲的脸表示仇敌的同在。

### Core Points

1. **正负皆可**: 脸的状态决定含义
2. **神的恩惠**: 脸光照代表祝福
3. **拒绝象征**: 转离的脸代表审判
4. **仇敌识别**: 扭曲的脸是邪灵

### Narrative Snippets

- `[ns_dav_f001]` `[trigger: face_favor]` `[factor_trigger: dream_face AND dream_favor]` `[role: 主干]` The LORD make his face shine upon you—His face represents favor and blessing. → 愿主使祂的脸光照你——祂的脸代表恩惠和祝福。
- `[ns_dav_f002]` `[trigger: face_reject]` `[factor_trigger: dream_face AND dream_rejection]` `[role: 警告]` God's face turned away speaks of rejection—seek His face through repentance. → 神转脸不看象征拒绝——要通过悔改寻求祂的面。"""
    normalized_text_zh: str = """"""
    subject: str = "Face 脸/同在"
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
        l1_anchor="dvd_v1.0.0_face_脸_同在_001_L1",
    )
    version: str = "1.0.0"
