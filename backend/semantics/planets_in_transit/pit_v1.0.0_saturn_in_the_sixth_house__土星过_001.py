"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.318449
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
    semantic_id="pit_v1.0.0_saturn_in_the_sixth_house__土星过_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SaturnInTheSixthHouse土星过(SemanticEntry):
    """
    **Source Text** (Lines 12392-12421):
> Critical time. When Saturn leaves 6H and enters 7H, efforts w...
    """
    
    original_text: str = """**Source Text** (Lines 12392-12421):
> Critical time. When Saturn leaves 6H and enters 7H, efforts will bear fruit if handled properly. Like preparing for debut—put everything in order for maximum impact. Very heavy responsibility and hard work. May not feel equal to challenge. Difficult to live up to employers' demands, may not be recognized adequately yet. Effectiveness as human being tested. Get performance into shape before more public position in next house. Conserve energies for efficiency. Scattered energies won't be enough. Health may suffer from extra burst of energy. Sixth is health house—attend to health. Body is tool needing care. Both body and mind must be in shape for emergence.

**English Paraphrase**: Critical—preparing for debut. Heavy responsibility and work. May feel inadequate. Effectiveness tested. Get performance in shape. Conserve energies. Health important—body and mind must be ready for emergence.

**Complete Chinese Interpretation**: 关键——为首演做准备。沉重的责任和工作。可能感到不够格。有效性被测试。调整表现。保存精力。健康重要——身心必须为出现做好准备。

**Narrative Snippets**:
- `[ns_pit_sa006]` `[trigger: saturn_transit_house_6]` `[factor_trigger: astro_transit_saturn AND astro_house_6]` `[role: 主干]` Preparing for debut. Heavy work and responsibility. Get performance in shape. Health important. → PIT Ch10 Saturn-6H"""
    normalized_text_zh: str = """"""
    subject: str = "Saturn in the Sixth House (土星过境第六宫)"
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
        book_id="planets_in_transit",
        chapter="",
        l1_anchor="pit_v1.0.0_saturn_in_the_sixth_house__土星过_001_L1",
    )
    version: str = "1.0.0"
