"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.419673
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
    semantic_id="dvd_v1.0.0_calf_牛犊_新生_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Calf牛犊新生(SemanticEntry):
    """
    ### Source Text

> **Calf**: A new birth. A new blessing or gift to be given to you. Often relates t...
    """
    
    original_text: str = """### Source Text

> **Calf**: A new birth. A new blessing or gift to be given to you. Often relates to business and finances.
> Positive: A calf speaks of a new birth, new blessing or new gift. Cattle speak of business and production.
> Negative: A calf instead of a fully-grown cow could indicate immaturity. A golden calf speaks of idolatry.
> Psalms 29:6 "He makes them also to skip like a calf; Lebanon and Sirion like a young unicorn."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Calf | 牛犊 | 新生和新祝福的象征 |
| New birth | 新生 | 新事物的开始 |
| Business | 事业 | 财务和生产活动 |
| Golden calf | 金牛犊 | 偶像崇拜的象征 |

### English Paraphrase

A calf represents new birth, blessing, or gift—often relating to business and finances. In a positive context, it speaks of joy and exuberance. Negatively, it could indicate immaturity or, as a golden calf, idolatry and putting things above God.

### Chinese Interpretation

牛犊代表新生、祝福或恩赐——通常与事业和财务相关。正面而言，它象征喜乐和活力。负面而言，可能表示不成熟，或作为金牛犊，象征偶像崇拜和将事物置于神之上。

### Core Points

1. **正负皆可**: 上下文决定含义
2. **财务关联**: 常与事业和生产相关
3. **喜乐象征**: 正面时代表活力和祝福
4. **偶像警告**: 金牛犊象征将事物凌驾于神之上

### Narrative Snippets

- `[ns_dav_c004]` `[trigger: calf_newbirth]` `[factor_trigger: dream_calf AND dream_newbirth]` `[role: 主干]` A calf speaks of a new birth, new blessing or gift—often relates to business and finances. → 牛犊象征新生、祝福或恩赐，常与事业财务相关。
- `[ns_dav_c005]` `[trigger: calf_idol]` `[factor_trigger: dream_golden_calf AND dream_idolatry]` `[role: 警告]` A golden calf has a very negative connotation—this speaks of idolatry or things put above the Lord. → 金牛犊是极负面的象征，代表偶像崇拜。"""
    normalized_text_zh: str = """"""
    subject: str = "Calf 牛犊/新生"
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
        l1_anchor="dvd_v1.0.0_calf_牛犊_新生_001_L1",
    )
    version: str = "1.0.0"
