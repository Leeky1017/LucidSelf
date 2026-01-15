"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.419793
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
    semantic_id="dvd_v1.0.0_circumcision_割礼_分别_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Circumcision割礼分别(SemanticEntry):
    """
    ### Source Text

> **Circumcision**: A picture of cutting away the flesh and being set apart for the...
    """
    
    original_text: str = """### Source Text

> **Circumcision**: A picture of cutting away the flesh and being set apart for the Lord.
> In the Old Testament, circumcision was the sign of the covenant. Spiritually, it speaks of cutting away the works of the flesh and being wholly devoted to God.
> Romans 2:29 "But he is a Jew, which is one inwardly; and circumcision is that of the heart, in the spirit."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Circumcision | 割礼 | 切除肉体 |
| Covenant | 约 | 与神的盟约 |
| Set apart | 分别为圣 | 完全献给神 |
| Heart | 心 | 属灵的割礼在心里 |

### English Paraphrase

Circumcision represents cutting away the flesh and being set apart for the Lord. It is the sign of covenant with God. Spiritually, it speaks of cutting away fleshly works and being wholly devoted to God—circumcision of the heart.

### Chinese Interpretation

割礼代表切除肉体并分别为圣归给主。它是与神立约的记号。属灵上，它象征切除肉体的行为并完全献给神——心的割礼。

### Core Points

1. **通常正面**: 代表圣洁和分别
2. **约的记号**: 与神立约的象征
3. **心的工作**: 内在的改变比外在更重要
4. **肉体对付**: 需要切除肉体的行为

### Narrative Snippets

- `[ns_dav_c028]` `[trigger: circumcision_heart]` `[factor_trigger: dream_circumcision AND dream_heart]` `[role: 主干]` Circumcision speaks of cutting away the flesh and being set apart—circumcision of the heart in the spirit. → 割礼象征切除肉体并分别为圣——灵里心的割礼。"""
    normalized_text_zh: str = """"""
    subject: str = "Circumcision 割礼/分别"
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
        l1_anchor="dvd_v1.0.0_circumcision_割礼_分别_001_L1",
    )
    version: str = "1.0.0"
