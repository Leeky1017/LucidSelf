"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.414630
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
    semantic_id="dvd_v1.0.0_colors___biblical_codes_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class ColorsBiblicalCodes(SemanticEntry):
    """
    **English**: White (purity), Red (blood/warfare), Blue (Spirit/heaven), Gold (glory), Black (sin/dea...
    """
    
    original_text: str = """**English**: White (purity), Red (blood/warfare), Blue (Spirit/heaven), Gold (glory), Black (sin/death), Purple (royalty), Green (life/growth).
**Chinese**: 白(纯洁)、红(宝血/争战)、蓝(灵/天)、金(荣耀)、黑(罪/死)、紫(王权)、绿(生命/成长)。
**Core**: Tabernacle patterns (Exodus 25-40). East: 颜色(类似五行) + 圣经义"""
    normalized_text_zh: str = """"""
    subject: str = "Colors - Biblical Codes"
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
        l1_anchor="dvd_v1.0.0_colors___biblical_codes_001_L1",
    )
    version: str = "1.0.0"
