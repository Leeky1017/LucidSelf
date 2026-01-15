"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.424543
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
    semantic_id="dvd_v1.0.0_beelzebub_别西卜_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Beelzebub别西卜(SemanticEntry):
    """
    ### Source Text

> Beelzebub = "lord of flies", prince of demons. Linked to New Age movement. Large ...
    """
    
    original_text: str = """### Source Text

> Beelzebub = "lord of flies", prince of demons. Linked to New Age movement. Large ugly mixture of man and fly.

### English Paraphrase

Beelzebub = prince demon, lord of flies. Associated with New Age, false teachings.

### Chinese Interpretation（完整对等诠释）

别西卜 = 鬼王，苍蝇之主。与新时代运动、假教导相关。

### Narrative Snippets

- `[ns_dav_b031]` `[trigger: 梦别西卜]` `[factor_trigger: dream_symbol_beelzebub]` `[role: 主干]` Beelzebub = prince demon, New Age linked—always negative. → Dreams Dictionary #Beelzebub"""
    normalized_text_zh: str = """"""
    subject: str = "Beelzebub 别西卜"
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
        l1_anchor="dvd_v1.0.0_beelzebub_别西卜_001_L1",
    )
    version: str = "1.0.0"
