"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.405293
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
    semantic_id="dvd_v1.0.0_poison_毒药_苦毒_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Poison毒药苦毒(SemanticEntry):
    """
    ### Source Text

> **Poison**: The most common interpretation is the presence of bitterness and nega...
    """
    
    original_text: str = """### Source Text

> **Poison**: The most common interpretation is the presence of bitterness and negative words. To dream of drinking poison indicates feeding on things deadly to your spirit—websites, teachings, or books without Christ's spirit. Bitterness, fear and guilt are poison in your spirit.

### Key Terms

| English | Chinese | Definition |
|---------|---------|------------|
| Poison | 毒药 | 苦毒和负面话 |
| Bitterness | 苦毒 | 污染的情绪 |
| Deadly | 致命的 | 对灵的伤害 |
| Words | 话语 | 负面的咒诅 |

### English Paraphrase

Poison represents bitterness and negative words. Drinking poison indicates feeding on deadly things—materials without Christ's spirit. Bitterness, fear and guilt are poison to your spirit—polluting yourself and defiling others around you.

### Chinese Interpretation

毒药代表苦毒和负面话语。喝毒象征吃进致命的东西——没有基督之灵的材料。苦毒、恐惧和内疚是你灵里的毒——污染自己和玷污周围的人。

### Core Points

1. **始终负面**: 毒药没有正面含义
2. **苦毒象征**: 情感的毒素
3. **话语咒诅**: 负面话的力量
4. **污染警告**: 影响自己和他人

### Narrative Snippets

- `[ns_dav_p011]` `[trigger: poison_bitterness]` `[factor_trigger: dream_poison AND dream_bitterness]` `[role: 警告]` Poison represents bitterness—polluting your own spirit and defiling everyone around you. → 毒药代表苦毒——污染你自己的灵和玷污你周围的每个人。"""
    normalized_text_zh: str = """"""
    subject: str = "Poison 毒药/苦毒"
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
        l1_anchor="dvd_v1.0.0_poison_毒药_苦毒_001_L1",
    )
    version: str = "1.0.0"
