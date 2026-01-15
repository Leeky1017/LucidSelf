"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.424489
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
    semantic_id="dvd_v1.0.0_bats_蝙蝠_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Bats蝙蝠(SemanticEntry):
    """
    ### Source Text

> Bats = creatures of night, negative. Work of enemy, often tied to occultism (Lev ...
    """
    
    original_text: str = """### Source Text

> Bats = creatures of night, negative. Work of enemy, often tied to occultism (Lev 11:19).

### English Paraphrase

Bats = demonic, occult. Night creatures representing enemy's work.

### Chinese Interpretation（完整对等诠释）

蝙蝠 = 魔鬼的、邪术的。夜间生物代表仇敌的工作。

### Narrative Snippets

- `[ns_dav_b027]` `[trigger: 梦蝙蝠]` `[factor_trigger: dream_symbol_bats]` `[role: 主干]` Bats = demonic, occult influence—always negative. → Dreams Dictionary #Bats"""
    normalized_text_zh: str = """"""
    subject: str = "Bats 蝙蝠"
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
        l1_anchor="dvd_v1.0.0_bats_蝙蝠_001_L1",
    )
    version: str = "1.0.0"
