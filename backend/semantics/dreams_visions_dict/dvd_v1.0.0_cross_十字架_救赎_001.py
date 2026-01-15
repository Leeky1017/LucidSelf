"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.419908
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
    semantic_id="dvd_v1.0.0_cross_十字架_救赎_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Cross十字架救赎(SemanticEntry):
    """
    ### Source Text

> **Cross**: The cross speaks of an object that is cursed but also speaks of death ...
    """
    
    original_text: str = """### Source Text

> **Cross**: The cross speaks of an object that is cursed but also speaks of death and of redemption all at once.
> Positive: The Scriptures tell us to 'bear our cross' which means to enter into both the death and resurrection of the Lord Jesus Christ. It means to walk in His resurrection power.
> Negative: A cross as a piece of jewelry is more of an idol than a picture of redemption. A religious cross represents legalism.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Cross | 十字架 | 死亡与救赎 |
| Redemption | 救赎 | 基督的拯救工作 |
| Death | 死亡 | 向己死 |
| Resurrection | 复活 | 新生命的开始 |

### English Paraphrase

The cross speaks of death and redemption together. To bear our cross means entering into Christ's death and resurrection—walking in His resurrection power, letting go of striving. Negatively, a cross as jewelry is an idol, and a religious cross represents legalism.

### Chinese Interpretation

十字架同时象征死亡和救赎。背起我们的十字架意味着进入基督的死与复活——行走在祂复活的能力中，放下挣扎。负面而言，作为珠宝的十字架是偶像，宗教性的十字架代表律法主义。

### Core Points

1. **正负皆可**: 使用方式决定含义
2. **死与复活**: 两者不可分割
3. **向己死**: 让神掌权
4. **偶像警告**: 不要崇拜物件本身

### Narrative Snippets

- `[ns_dav_c045]` `[trigger: cross_bear]` `[factor_trigger: dream_cross AND dream_bear]` `[role: 主干]` To bear our cross means entering into Christ's death and resurrection—walking in His power, not our own. → 背起十字架意味着进入基督的死与复活——行走在祂的能力中，而非我们自己的。
- `[ns_dav_c046]` `[trigger: cross_idol]` `[factor_trigger: dream_cross AND dream_idol]` `[role: 警告]` A cross as jewelry is more of an idol—we serve the God upon the cross, not the object. → 作为珠宝的十字架更像偶像——我们服事十字架上的神，而非物件本身。"""
    normalized_text_zh: str = """"""
    subject: str = "Cross 十字架/救赎"
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
        l1_anchor="dvd_v1.0.0_cross_十字架_救赎_001_L1",
    )
    version: str = "1.0.0"
