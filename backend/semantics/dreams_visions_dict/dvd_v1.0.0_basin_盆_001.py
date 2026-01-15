"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.424437
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
    semantic_id="dvd_v1.0.0_basin_盆_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Basin盆(SemanticEntry):
    """
    ### Source Text

> Basin = cleansing a particular aspect, feet washing (John 13:5). Daily activity t...
    """
    
    original_text: str = """### Source Text

> Basin = cleansing a particular aspect, feet washing (John 13:5). Daily activity to cleanse of worldly contamination.

### English Paraphrase

Basin = partial cleansing, feet washing. Daily purification from world's curses.

### Chinese Interpretation（完整对等诠释）

盆 = 局部洁净，洗脚。每日从世界咒诅中净化。

### Narrative Snippets

- `[ns_dav_b025]` `[trigger: 梦盆]` `[factor_trigger: dream_symbol_basin]` `[role: 主干]` Basin = partial cleansing, daily foot washing. → Dreams Dictionary #Basin"""
    normalized_text_zh: str = """"""
    subject: str = "Basin 盆"
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
        l1_anchor="dvd_v1.0.0_basin_盆_001_L1",
    )
    version: str = "1.0.0"
