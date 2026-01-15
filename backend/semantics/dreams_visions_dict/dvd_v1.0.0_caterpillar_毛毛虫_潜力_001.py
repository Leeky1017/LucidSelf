"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.419725
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
    semantic_id="dvd_v1.0.0_caterpillar_毛毛虫_潜力_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Caterpillar毛毛虫潜力(SemanticEntry):
    """
    ### Source Text

> **Caterpillar**: A promise of potential. A picture of immaturity leading to matur...
    """
    
    original_text: str = """### Source Text

> **Caterpillar**: A promise of potential. A picture of immaturity leading to maturity.
> The caterpillar, although a worm, does not stay that way because it is destined for greatness.
> Positive: Seeing a caterpillar indicates the Lord sees potential in you and desires to take you through transformation.
> Negative: In a negative context, the caterpillar symbolizes a spirit of destruction sent to eat the blessing God has given you.
> Joel 1:4 "That which the caterpillar has eaten..."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Caterpillar | 毛毛虫 | 潜力和转变的象征 |
| Potential | 潜力 | 尚未实现的能力 |
| Transformation | 转变 | 从不成熟到成熟 |
| Destruction | 毁灭 | 吞噬祝福的灵 |

### English Paraphrase

A caterpillar represents promise and potential—a picture of immaturity destined for greatness. The Lord sees what you can become and desires to take you through transformation. Negatively, it symbolizes a spirit of destruction that consumes God's blessings.

### Chinese Interpretation

毛毛虫代表应许和潜力——不成熟但注定伟大的画面。主看见你能成为什么，渴望带你经历转变。负面而言，它象征吞噬神祝福的毁灭之灵。

### Core Points

1. **正负皆可**: 上下文决定含义
2. **潜力象征**: 虽是虫却注定伟大
3. **转变过程**: 神要带你经历变化
4. **毁灭警告**: 可能代表偷窃祝福的灵

### Narrative Snippets

- `[ns_dav_c014]` `[trigger: caterpillar_potential]` `[factor_trigger: dream_caterpillar AND dream_potential]` `[role: 主干]` Seeing a caterpillar indicates the Lord sees potential in you—destined for greatness through transformation. → 毛毛虫表明主看见你的潜力，注定要经历荣耀的转变。
- `[ns_dav_c015]` `[trigger: caterpillar_destruction]` `[factor_trigger: dream_caterpillar AND dream_destruction]` `[role: 警告]` In a negative context, the caterpillar symbolizes a spirit of destruction eating the blessing God has given. → 负面时，毛毛虫象征吞噬神祝福的毁灭之灵。"""
    normalized_text_zh: str = """"""
    subject: str = "Caterpillar 毛毛虫/潜力"
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
        l1_anchor="dvd_v1.0.0_caterpillar_毛毛虫_潜力_001_L1",
    )
    version: str = "1.0.0"
