"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.424392
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
    semantic_id="dvd_v1.0.0_barnabas_巴拿巴_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Barnabas巴拿巴(SemanticEntry):
    """
    ### Source Text

> Barnabas = "son of consolation" (Acts 4:36). Encourager who vouched for Paul, men...
    """
    
    original_text: str = """### Source Text

> Barnabas = "son of consolation" (Acts 4:36). Encourager who vouched for Paul, mentored Mark. To be a Barnabas = encourager and motivator.

### English Paraphrase

Barnabas = encourager. One who believes in others when no one else does.

### Chinese Interpretation（完整对等诠释）

巴拿巴 = 鼓励者。当无人相信时相信他人的人。

### Narrative Snippets

- `[ns_dav_b020]` `[trigger: 梦巴拿巴]` `[factor_trigger: dream_symbol_barnabas]` `[role: 主干]` Barnabas = encourager, son of consolation. → Dreams Dictionary #Barnabas"""
    normalized_text_zh: str = """"""
    subject: str = "Barnabas 巴拿巴"
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
        l1_anchor="dvd_v1.0.0_barnabas_巴拿巴_001_L1",
    )
    version: str = "1.0.0"
