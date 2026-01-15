"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.424400
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
    semantic_id="dvd_v1.0.0_barrel_桶_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Barrel桶(SemanticEntry):
    """
    ### Source Text

> Barrel = same as barn but smaller measure. Sustained provision that doesn't run o...
    """
    
    original_text: str = """### Source Text

> Barrel = same as barn but smaller measure. Sustained provision that doesn't run out (1 Kgs 17:16).

### English Paraphrase

Barrel = smaller sustained blessing. Elijah's widow—provision that doesn't run out.

### Chinese Interpretation（完整对等诠释）

桶 = 较小的持续祝福。以利亚的寡妇——不会用尽的供应。

### Narrative Snippets

- `[ns_dav_b021]` `[trigger: 梦桶]` `[factor_trigger: dream_symbol_barrel]` `[role: 主干]` Barrel = smaller sustained blessing. → Dreams Dictionary #Barrel"""
    normalized_text_zh: str = """"""
    subject: str = "Barrel 桶"
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
        l1_anchor="dvd_v1.0.0_barrel_桶_001_L1",
    )
    version: str = "1.0.0"
