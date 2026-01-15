"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.396196
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
    semantic_id="dvd_v1.0.0_milk_奶_基础教导_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Milk奶基础教导(SemanticEntry):
    """
    ### Source Text

> **Milk**: A basic need for survival. It is the building block of the first stages...
    """
    
    original_text: str = """### Source Text

> **Milk**: A basic need for survival. It is the building block of the first stages of life—your basic needs. Spiritually, milk represents the first steps to understanding the Word—doctrinal basics.
> Positive: Drinking milk means being strengthened. Milk flowing with honey speaks of blessing and abundance.
> Negative: Sour milk speaks of opportunities gone bad. Needing milk means immaturity—not ready for meaty things.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Milk | 奶 | 基础的需要 |
| Basics | 基础 | 信仰的根基 |
| Sour | 酸 | 过去的机会 |
| Immaturity | 不成熟 | 需要成长 |

### English Paraphrase

Milk represents basic survival needs and the building blocks of life. Spiritually, milk is the first steps of understanding the Word—doctrinal basics. Drinking milk strengthens you. Milk and honey speaks of blessing. Sour milk means opportunities passed. Needing only milk indicates immaturity.

### Chinese Interpretation

奶代表基本的生存需要和生命的基石。属灵上，奶是理解话语的第一步——教义的基础。喝奶使你强壮。奶与蜜象征祝福。酸奶意味着机会已过。只需要奶表示不成熟。

### Core Points

1. **正负皆可**: 奶的状态决定含义
2. **基础象征**: 信仰的根基教导
3. **祝福记号**: 奶与蜜是丰盛
4. **成熟警告**: 只喝奶是不成熟

### Narrative Snippets

- `[ns_dav_m007]` `[trigger: milk_basics]` `[factor_trigger: dream_milk AND dream_basics]` `[role: 主干]` Milk represents the first steps to understanding the Word—the building blocks of your faith. → 奶代表理解话语的第一步——你信仰的基石。
- `[ns_dav_m008]` `[trigger: milk_sour]` `[factor_trigger: dream_milk AND dream_sour]` `[role: 警告]` Sour milk speaks of opportunities that have gone bad—a season that has passed. → 酸奶象征已经变坏的机会——已过去的季节。"""
    normalized_text_zh: str = """"""
    subject: str = "Milk 奶/基础教导"
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
        l1_anchor="dvd_v1.0.0_milk_奶_基础教导_001_L1",
    )
    version: str = "1.0.0"
