"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.402027
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
    semantic_id="dvd_v1.0.0_disease_疾病_不洁_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Disease疾病不洁(SemanticEntry):
    """
    ### Source Text

> **Disease**: Disease is never a positive picture. It speaks of sin, being unclean...
    """
    
    original_text: str = """### Source Text

> **Disease**: Disease is never a positive picture. It speaks of sin, being unclean and of contamination. It also speaks of being under a curse.
> Deuteronomy 28:60 "Moreover he will bring upon you all the diseases of Egypt, which you were afraid of; and they will cleave to you."
> Leviticus 13:46 "...he is unclean: he shall dwell alone; without the camp shall his habitation be."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Disease | 疾病 | 罪和不洁 |
| Unclean | 不洁 | 与污染相关 |
| Curse | 咒诅 | 违背神的后果 |
| Contamination | 污染 | 灵里的感染 |

### English Paraphrase

Disease is never positive—it represents sin, uncleanness, and contamination. It speaks of being under a curse. In Scripture, the diseased were separated and lived outside the camp. Disease indicates something wrong spiritually that needs healing.

### Chinese Interpretation

疾病从来不是正面的——它代表罪、不洁和污染。它象征处于咒诅之下。在圣经中，有病的人被分别出来住在营外。疾病表明属灵上有问题需要医治。

### Core Points

1. **始终负面**: 疾病没有正面含义
2. **罪的结果**: 与不顺服相关
3. **咒诅象征**: 可能来自世代
4. **需要医治**: 呼求神的医治

### Narrative Snippets

- `[ns_dav_d017]` `[trigger: disease_sin]` `[factor_trigger: dream_disease AND dream_sin]` `[role: 主干]` Disease is never positive—it speaks of sin, being unclean and being under a curse. → 疾病从来不是正面的——它象征罪、不洁和处于咒诅之下。"""
    normalized_text_zh: str = """"""
    subject: str = "Disease 疾病/不洁"
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
        l1_anchor="dvd_v1.0.0_disease_疾病_不洁_001_L1",
    )
    version: str = "1.0.0"
