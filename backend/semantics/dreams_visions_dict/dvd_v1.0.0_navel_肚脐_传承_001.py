"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.433375
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
    semantic_id="dvd_v1.0.0_navel_肚脐_传承_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Navel肚脐传承(SemanticEntry):
    """
    ### Source Text

> **Navel**: Your belly button is proof of your heritage and also a place of weakne...
    """
    
    original_text: str = """### Source Text

> **Navel**: Your belly button is proof of your heritage and also a place of weakness. It points to the middle of you—a representation of who you are and where you come from.
> Positive: Speaks of vulnerability and intimacy.
> Negative: A dirty or damaged navel indicates struggling with vulnerability or defilement—likely referring to a generational curse.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Navel | 肚脐 | 传承和脆弱 |
| Heritage | 传承 | 来源和血统 |
| Vulnerability | 脆弱 | 最弱的地方 |
| Generational | 世代的 | 咒诅的来源 |

### English Paraphrase

Your navel is proof of heritage and a place of weakness—representing who you are and where you come from. It speaks of vulnerability and intimacy. A dirty or damaged navel indicates struggling with vulnerability or defilement—likely a generational curse the Lord is exposing.

### Chinese Interpretation

肚脐是传承的证明也是脆弱的地方——代表你是谁和你从哪里来。它象征脆弱和亲密。脏的或受损的肚脐表示与脆弱或玷污的挣扎——很可能是主正在揭露的世代咒诅。

### Core Points

1. **正负皆可**: 状态决定含义
2. **传承象征**: 血统和来源
3. **亲密记号**: 脆弱处的亲密
4. **咒诅警告**: 可能是世代咒诅

### Narrative Snippets

- `[ns_dav_n003]` `[trigger: navel_heritage]` `[factor_trigger: dream_navel AND dream_heritage]` `[role: 主干]` Your navel is proof of your heritage—representing who you are and where you come from. → 肚脐是你传承的证明——代表你是谁和你从哪里来。
- `[ns_dav_n004]` `[trigger: navel_curse]` `[factor_trigger: dream_navel AND dream_curse]` `[role: 警告]` A damaged navel likely refers to a generational curse the Lord is exposing in your life. → 受损的肚脐很可能指主正在你生命中揭露的世代咒诅。"""
    normalized_text_zh: str = """"""
    subject: str = "Navel 肚脐/传承"
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
        l1_anchor="dvd_v1.0.0_navel_肚脐_传承_001_L1",
    )
    version: str = "1.0.0"
