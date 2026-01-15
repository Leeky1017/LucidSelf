"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.412188
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
    semantic_id="dvd_v1.0.0_flies_苍蝇_邪灵_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Flies苍蝇邪灵(SemanticEntry):
    """
    ### Source Text

> **Flies**: A picture of demonic activity and unclean spirits. Beelzebub means "lo...
    """
    
    original_text: str = """### Source Text

> **Flies**: A picture of demonic activity and unclean spirits. Beelzebub means "lord of the flies."
> Flies gather around decay and death. In dreams, flies speak of demonic harassment and contamination. A swarm of flies indicates intense spiritual attack.
> Ecclesiastes 10:1 "Dead flies cause the ointment of the apothecary to send forth a stinking savor."

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Flies | 苍蝇 | 邪灵活动 |
| Beelzebub | 别西卜 | 苍蝇之主 |
| Contamination | 污染 | 灵里的不洁 |
| Decay | 腐烂 | 死亡和毁坏 |

### English Paraphrase

Flies represent demonic activity and unclean spirits—Beelzebub means "lord of the flies." Flies gather around decay and death. In dreams, they speak of demonic harassment and contamination. A swarm indicates intense spiritual attack.

### Chinese Interpretation

苍蝇代表邪灵活动和污秽的灵——别西卜意思是"苍蝇之主"。苍蝇聚集在腐烂和死亡周围。在梦中，它们象征邪灵的骚扰和污染。成群的苍蝇表示强烈的属灵攻击。

### Core Points

1. **始终负面**: 苍蝇代表邪灵
2. **腐烂象征**: 聚集在死亡周围
3. **污染警告**: 灵里的污秽
4. **攻击程度**: 成群表示强烈攻击

### Narrative Snippets

- `[ns_dav_f014]` `[trigger: flies_demonic]` `[factor_trigger: dream_flies AND dream_demonic]` `[role: 警告]` Flies represent demonic activity—Beelzebub the "lord of the flies" speaks of unclean spirits. → 苍蝇代表邪灵活动——别西卜"苍蝇之主"代表污秽的灵。"""
    normalized_text_zh: str = """"""
    subject: str = "Flies 苍蝇/邪灵"
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
        l1_anchor="dvd_v1.0.0_flies_苍蝇_邪灵_001_L1",
    )
    version: str = "1.0.0"
