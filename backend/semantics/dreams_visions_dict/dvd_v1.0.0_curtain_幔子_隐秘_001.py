"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.419932
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
    semantic_id="dvd_v1.0.0_curtain_幔子_隐秘_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Curtain幔子隐秘(SemanticEntry):
    """
    ### Source Text

> **Curtain**: This is the same as the word Veil used in Scriptures. A curtain spea...
    """
    
    original_text: str = """### Source Text

> **Curtain**: This is the same as the word Veil used in Scriptures. A curtain speaks of things that are hidden. Going behind the veil speaks of entering into intimate relationship with the Lord.
> Positive: Often the Lord hides things from us until we are ready. Seeing a curtain means He will soon reveal something He has been preparing.
> Negative: Hiding your heart behind a curtain speaks of putting on masks to hide your real self. Curtains prevent intimacy with the Lord.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Curtain | 幔子 | 隐藏和亲密 |
| Veil | 帕子 | 遮挡的事物 |
| Hidden | 隐藏 | 尚未显露 |
| Intimacy | 亲密 | 与主的深入关系 |

### English Paraphrase

A curtain (veil) speaks of things hidden. Going behind the veil means entering intimacy with the Lord. Positively, God hides things until we are ready—a curtain means He will soon reveal something. Negatively, hiding behind curtains means putting on masks, preventing intimacy with God.

### Chinese Interpretation

幔子（帕子）象征隐藏的事物。进入幔内意味着进入与主的亲密关系。正面而言，神隐藏事物直到我们预备好——幔子意味着祂即将揭示所预备的。负面而言，藏在幔子后面意味着戴上面具，阻碍与神的亲密。

### Core Points

1. **正负皆可**: 幔子的作用决定含义
2. **亲密入口**: 进入至圣所需要穿过幔子
3. **即将揭示**: 神预备好时会揭开
4. **面具警告**: 不要用幔子隐藏真我

### Narrative Snippets

- `[ns_dav_c051]` `[trigger: curtain_intimacy]` `[factor_trigger: dream_curtain AND dream_intimacy]` `[role: 正面]` Going behind the curtain speaks of entering into intimate relationship with the Lord—into His presence. → 进入幔内象征进入与主亲密的关系——进入祂的同在。
- `[ns_dav_c052]` `[trigger: curtain_mask]` `[factor_trigger: dream_curtain AND dream_mask]` `[role: 警告]` Hiding behind a curtain speaks of putting on masks—bitterness as curtains around your heart. → 藏在幔子后面象征戴上面具——苦毒如幔子包裹你的心。"""
    normalized_text_zh: str = """"""
    subject: str = "Curtain 幔子/隐秘"
    factor_refs: list = ['source_ref']
    
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
        l1_anchor="dvd_v1.0.0_curtain_幔子_隐秘_001_L1",
    )
    version: str = "1.0.0"
