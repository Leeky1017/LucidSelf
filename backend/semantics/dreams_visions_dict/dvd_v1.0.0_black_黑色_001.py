"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.424611
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
    semantic_id="dvd_v1.0.0_black_黑色_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Black黑色(SemanticEntry):
    """
    ### Source Text

> Black = mostly negative. Oppression, disease, contamination, ignorance, deception...
    """
    
    original_text: str = """### Source Text

> Black = mostly negative. Oppression, disease, contamination, ignorance, deception. Black person in dream depends on personal feelings—if comfortable, may be positive.

### English Paraphrase

Black = negative. Oppression, disease, deception. Context of dreamer's feelings matters.

### Chinese Interpretation（完整对等诠释）

黑色 = 负面。压制、疾病、欺骗。做梦者的感受背景很重要。

### Narrative Snippets

- `[ns_dav_b036]` `[trigger: 梦黑色]` `[factor_trigger: dream_symbol_black]` `[role: 主干]` Black = mostly negative—oppression, disease, ignorance. → Dreams Dictionary #Black"""
    normalized_text_zh: str = """"""
    subject: str = "Black 黑色"
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
        l1_anchor="dvd_v1.0.0_black_黑色_001_L1",
    )
    version: str = "1.0.0"
