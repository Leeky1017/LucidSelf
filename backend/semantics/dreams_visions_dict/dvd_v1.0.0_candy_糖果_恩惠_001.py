"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.419705
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
    semantic_id="dvd_v1.0.0_candy_糖果_恩惠_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Candy糖果恩惠(SemanticEntry):
    """
    ### Source Text

> **Candy**: A treat or small blessing from the Lord. In a negative light it speaks...
    """
    
    original_text: str = """### Source Text

> **Candy**: A treat or small blessing from the Lord. In a negative light it speaks of indulging the flesh.
> Positive: Candy or chocolate speaks of something that is a treat and a gift. The Lord wants to delight you—not only provide needs, but desires as well.
> Negative: Eating candy can speak of getting into the flesh—sweet in the mouth but bitter in the belly.
> Revelation 10:9 "Take it, and eat it up; and it will make your belly bitter, but it will be in your mouth sweet as honey."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Candy | 糖果 | 小祝福和款待 |
| Treat | 款待 | 超越需要的恩赐 |
| Delight | 喜悦 | 神渴望使你快乐 |
| Flesh indulgence | 肉体放纵 | 短暂满足后的苦涩 |

### English Paraphrase

Candy represents a treat or small blessing from the Lord—He desires to delight you beyond just meeting needs. Negatively, eating candy speaks of flesh indulgence—sweet at first but leading to emptiness and bitterness.

### Chinese Interpretation

糖果代表来自主的款待或小祝福——祂渴望使你喜悦，不仅满足需要，也满足心愿。负面而言，吃糖象征放纵肉体——起初甜蜜，最终空虚和苦涩。

### Core Points

1. **正负皆可**: 动机和结果决定含义
2. **喜悦恩赐**: 神想让你快乐
3. **肉体警告**: 在基督之外满足欲望会带来苦涩
4. **平衡需要**: 享受但不过度

### Narrative Snippets

- `[ns_dav_c010]` `[trigger: candy_blessing]` `[factor_trigger: dream_candy AND dream_blessing]` `[role: 主干]` Candy speaks of a treat and gift—the Lord wants to delight you, not only provide needs. → 糖果象征款待和恩赐，神渴望使你喜悦。
- `[ns_dav_c011]` `[trigger: candy_flesh]` `[factor_trigger: dream_candy AND dream_fleshly]` `[role: 警告]` Eating something sweet but feeling sick—the Lord is showing you that fleshly indulgences damage your spiritual life. → 吃甜食却感到恶心，表明肉体放纵正在损害灵性生命。"""
    normalized_text_zh: str = """"""
    subject: str = "Candy 糖果/恩惠"
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
        l1_anchor="dvd_v1.0.0_candy_糖果_恩惠_001_L1",
    )
    version: str = "1.0.0"
