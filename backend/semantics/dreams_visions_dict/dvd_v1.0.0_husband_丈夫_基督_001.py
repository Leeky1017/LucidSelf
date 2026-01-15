"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.450610
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
    semantic_id="dvd_v1.0.0_husband_丈夫_基督_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Husband丈夫基督(SemanticEntry):
    """
    ### Source Text

> **Husband**: Your husband often represents your recreated spirit in Christ or you...
    """
    
    original_text: str = """### Source Text

> **Husband**: Your husband often represents your recreated spirit in Christ or your relationship with Jesus.
> Positive: Husband taking you somewhere means your spirit is leading you in a new direction. Trying to make love but interrupted means something is preventing intimate time with the Lord.
> Negative: If your husband is negative in real life, he represents sin, pride, flesh, fear or insecurity. Ex-husband represents the flesh.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Husband | 丈夫 | 基督或灵 |
| Spirit | 灵 | 重生的灵 |
| Intimacy | 亲密 | 与主的关系 |
| Ex-husband | 前夫 | 肉体的象征 |

### English Paraphrase

Your husband often represents your recreated spirit in Christ or relationship with Jesus. Being taken somewhere means your spirit is leading you. Interrupted intimacy indicates something preventing time with the Lord. A negative husband represents sin, pride, flesh or fear. Ex-husband represents the flesh.

### Chinese Interpretation

你的丈夫常代表你在基督里重生的灵或与耶稣的关系。被带到某处意味着你的灵在引导你。被打断的亲密表示有东西阻止与主的时间。负面的丈夫代表罪、骄傲、肉体或恐惧。前夫代表肉体。

### Core Points

1. **正负皆可**: 丈夫形象决定含义
2. **基督象征**: 常代表与主的关系
3. **亲密记号**: 与主相交的时间
4. **肉体警告**: 前夫代表肉体

### Narrative Snippets

- `[ns_dav_h019]` `[trigger: husband_christ]` `[factor_trigger: dream_husband AND dream_christ]` `[role: 主干]` Your husband often represents your relationship with Jesus—the Groom desiring intimacy with His bride. → 你的丈夫常代表你与耶稣的关系——新郎渴望与新娘亲密。
- `[ns_dav_h020]` `[trigger: husband_ex]` `[factor_trigger: dream_husband AND dream_flesh]` `[role: 警告]` An ex-husband represents the flesh—you have been released from the law to be married to Christ. → 前夫代表肉体——你已从律法中被释放，好嫁给基督。"""
    normalized_text_zh: str = """"""
    subject: str = "Husband 丈夫/基督"
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
        l1_anchor="dvd_v1.0.0_husband_丈夫_基督_001_L1",
    )
    version: str = "1.0.0"
