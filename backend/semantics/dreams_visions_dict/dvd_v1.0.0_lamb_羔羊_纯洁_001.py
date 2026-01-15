"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.443881
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
    semantic_id="dvd_v1.0.0_lamb_羔羊_纯洁_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Lamb羔羊纯洁(SemanticEntry):
    """
    ### Source Text

> **Lamb**: An image of innocence and meekness. A young lamb represents a new belie...
    """
    
    original_text: str = """### Source Text

> **Lamb**: An image of innocence and meekness. A young lamb represents a new believer.
> Jesus the Lamb of God: The final lamb slain on the altar—after Him, burnt sacrifice was no longer necessary. A slain lamb confirms the covenant and finished work.
> Positive: Being sent out as lambs among wolves means walking in innocence while Jesus stands in power.
> Negative: Lambs being beaten speaks of believers being abused by leaders.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Lamb | 羔羊 | 纯洁和温顺 |
| Innocence | 纯洁 | 无罪的状态 |
| Lamb of God | 神的羔羊 | 耶稣基督 |
| Slain | 被杀 | 祭祀的牺牲 |

### English Paraphrase

A lamb represents innocence and meekness—a new believer. Jesus is the Lamb of God, the final sacrifice. A slain lamb confirms the covenant. Being sent as lambs among wolves means walking in innocence while Jesus stands in power. Lambs being beaten speaks of believers abused by leaders.

### Chinese Interpretation

羔羊代表纯洁和温顺——新信徒。耶稣是神的羔羊，最后的祭物。被杀的羔羊确认约。被差遣如羊进入狼群意味着行在纯洁中而耶稣站在能力中。羔羊被打象征信徒被领袖虐待。

### Core Points

1. **正负皆可**: 羔羊状态决定含义
2. **纯洁象征**: 无辜和温顺
3. **基督羔羊**: 神的羔羊是耶稣
4. **虐待警告**: 可能指信徒受害

### Narrative Snippets

- `[ns_dav_l003]` `[trigger: lamb_god]` `[factor_trigger: dream_lamb AND dream_sacrifice]` `[role: 主干]` Jesus is the Lamb of God—the final sacrifice confirming the covenant work completed. → 耶稣是神的羔羊——确认约的工作已完成的最后祭物。
- `[ns_dav_l004]` `[trigger: lamb_abuse]` `[factor_trigger: dream_lamb AND dream_abuse]` `[role: 警告]` Lambs being beaten speaks of believers being abused by the leaders over them. → 羔羊被打象征信徒被管辖他们的领袖虐待。"""
    normalized_text_zh: str = """"""
    subject: str = "Lamb 羔羊/纯洁"
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
        l1_anchor="dvd_v1.0.0_lamb_羔羊_纯洁_001_L1",
    )
    version: str = "1.0.0"
