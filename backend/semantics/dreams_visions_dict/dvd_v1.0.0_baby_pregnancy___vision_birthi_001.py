"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.414592
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
    semantic_id="dvd_v1.0.0_baby_pregnancy___vision_birthi_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class BabyPregnancyVisionBirthi(SemanticEntry):
    """
    **English**: New ministry/vision (NOT literal pregnancy usually). Pregnancy = gestation, birth = lau...
    """
    
    original_text: str = """**English**: New ministry/vision (NOT literal pregnancy usually). Pregnancy = gestation, birth = launch, baby = new beginning. Miscarriage = vision lost.
**Chinese**: 新事工/异象(通常非字面怀孕)。怀孕=孕育、生产=启动、婴儿=新开始。流产=异象失。
**Core**: Rarely literal. Test thoroughly. East: 怀孕=新事物(共通) + 事工(Christian)"""
    normalized_text_zh: str = """"""
    subject: str = "Baby/Pregnancy - Vision Birthing"
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
        l1_anchor="dvd_v1.0.0_baby_pregnancy___vision_birthi_001_L1",
    )
    version: str = "1.0.0"
