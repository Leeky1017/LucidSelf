"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.390701
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
    semantic_id="dvd_v1.0.0_grapes_葡萄_果实_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Grapes葡萄果实(SemanticEntry):
    """
    ### Source Text

> **Grapes**: A picture of fruit, blessing, and abundance. Also speaks of spiritual...
    """
    
    original_text: str = """### Source Text

> **Grapes**: A picture of fruit, blessing, and abundance. Also speaks of spiritual maturity.
> Positive: Grapes represent the fruit of the land—blessing and provision. Wine made from grapes speaks of joy. Clusters of grapes indicate abundant blessing.
> Negative: Sour grapes speak of bitterness passed down. Wild grapes indicate corruption.
> Numbers 13:23 "...they cut down a branch with one cluster of grapes..."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Grapes | 葡萄 | 果实和祝福 |
| Abundance | 丰盛 | 神的供应 |
| Wine | 酒 | 喜乐 |
| Sour | 酸 | 苦毒 |

### English Paraphrase

Grapes represent fruit, blessing, and abundance—also spiritual maturity. Grapes represent the fruit of the land and provision. Wine made from grapes speaks of joy. Clusters indicate abundant blessing. Sour grapes speak of bitterness; wild grapes indicate corruption.

### Chinese Interpretation

葡萄代表果实、祝福和丰盛——也代表属灵的成熟。葡萄代表地土的果实和供应。葡萄酿的酒象征喜乐。成串的葡萄表示丰盛的祝福。酸葡萄象征苦毒；野葡萄表示败坏。

### Core Points

1. **正负皆可**: 葡萄状态决定含义
2. **丰盛祝福**: 应许之地的果实
3. **喜乐象征**: 葡萄酒代表喜乐
4. **苦毒警告**: 酸葡萄是世代苦毒

### Narrative Snippets

- `[ns_dav_g009]` `[trigger: grapes_blessing]` `[factor_trigger: dream_grapes AND dream_blessing]` `[role: 主干]` Grapes represent the fruit of the land—blessing, abundance, and provision from the Lord. → 葡萄代表地土的果实——来自主的祝福、丰盛和供应。
- `[ns_dav_g010]` `[trigger: grapes_sour]` `[factor_trigger: dream_grapes AND dream_bitterness]` `[role: 警告]` Sour grapes speak of bitterness passed down from generation to generation. → 酸葡萄象征从一代传到下一代的苦毒。"""
    normalized_text_zh: str = """"""
    subject: str = "Grapes 葡萄/果实"
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
        l1_anchor="dvd_v1.0.0_grapes_葡萄_果实_001_L1",
    )
    version: str = "1.0.0"
