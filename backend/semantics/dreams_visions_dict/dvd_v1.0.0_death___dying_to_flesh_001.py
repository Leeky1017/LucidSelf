"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.414611
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
    semantic_id="dvd_v1.0.0_death___dying_to_flesh_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class DeathDyingToFlesh(SemanticEntry):
    """
    **English**: Dying to flesh, transformation (rarely literal death). Spiritual death → resurrection. ...
    """
    
    original_text: str = """**English**: Dying to flesh, transformation (rarely literal death). Spiritual death → resurrection. Season ending, deliverance from sin.
**Chinese**: 向肉体死、转化(罕有字面死)。灵性死→复活。季节结束、从罪释放。
**Core**: Galatians 2:20 crucified with Christ. East: 死亡=转化(共通) + 向肉体死(Christian成圣)"""
    normalized_text_zh: str = """"""
    subject: str = "Death - Dying to Flesh"
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
        l1_anchor="dvd_v1.0.0_death___dying_to_flesh_001_L1",
    )
    version: str = "1.0.0"
