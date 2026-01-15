"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.433407
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
    semantic_id="dvd_v1.0.0_necklace_项链_约_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Necklace项链约(SemanticEntry):
    """
    ### Source Text

> **Necklace**: Speaks of a position and also a picture of the things you believe. ...
    """
    
    original_text: str = """### Source Text

> **Necklace**: Speaks of a position and also a picture of the things you believe. The Israelites were told to tie the law of God around their necks—a picture of covenant and His promises.
> Positive: The Lord giving you a necklace reminds you of your position in covenant with Him—honor and promotion.
> Negative: A heavy or black necklace speaks of bondage—believing the enemy's words instead of God's.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Necklace | 项链 | 位置和信念 |
| Covenant | 约 | 神的应许 |
| Position | 位置 | 在约中的地位 |
| Bondage | 捆绑 | 仇敌的话 |

### English Paraphrase

A necklace speaks of position and beliefs. Israelites tied God's law around their necks—a picture of covenant and promises. The Lord giving you a necklace reminds you of your covenant position—honor and promotion. A heavy or black necklace speaks of bondage—believing the enemy's words.

### Chinese Interpretation

项链象征位置和信念。以色列人把神的律法系在颈上——约和应许的象征。主给你项链提醒你在约中的位置——尊荣和晋升。沉重或黑色的项链象征捆绑——相信仇敌的话而非神的话。

### Core Points

1. **正负皆可**: 项链性质决定含义
2. **约的象征**: 神的律法和应许
3. **尊荣记号**: 在约中的位置
4. **捆绑警告**: 黑色项链是捆绑

### Narrative Snippets

- `[ns_dav_n007]` `[trigger: necklace_covenant]` `[factor_trigger: dream_necklace AND dream_covenant]` `[role: 主干]` The Lord giving you a necklace reminds you of your covenant position—honor and blessing. → 主给你项链提醒你在约中的位置——尊荣和祝福。
- `[ns_dav_n008]` `[trigger: necklace_bondage]` `[factor_trigger: dream_necklace AND dream_bondage]` `[role: 警告]` A heavy or black necklace speaks of bondage—believing the enemy's words instead of God's. → 沉重或黑色的项链象征捆绑——相信仇敌的话而非神的话。"""
    normalized_text_zh: str = """"""
    subject: str = "Necklace 项链/约"
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
        l1_anchor="dvd_v1.0.0_necklace_项链_约_001_L1",
    )
    version: str = "1.0.0"
