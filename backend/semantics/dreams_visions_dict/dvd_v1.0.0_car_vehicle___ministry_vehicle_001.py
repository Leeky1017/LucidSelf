"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.414510
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
    semantic_id="dvd_v1.0.0_car_vehicle___ministry_vehicle_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class CarVehicleMinistryVehicle(SemanticEntry):
    """
    **English**: Ministry vehicle, calling execution. Type = style (sports = fast, truck = heavy-load). ...
    """
    
    original_text: str = """**English**: Ministry vehicle, calling execution. Type = style (sports = fast, truck = heavy-load). Position: driver = leading, passenger = following. Condition reflects ministry health.
**Chinese**: 事工载具、呼召执行。车型=风格。驾驶=领导、乘客=跟随。状况反映事工健康。
**Core**: Christian-specific (not in Jung/Freud). East: 车辆=事工(Christian特有)"""
    normalized_text_zh: str = """"""
    subject: str = "Car/Vehicle - Ministry Vehicle"
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
        l1_anchor="dvd_v1.0.0_car_vehicle___ministry_vehicle_001_L1",
    )
    version: str = "1.0.0"
