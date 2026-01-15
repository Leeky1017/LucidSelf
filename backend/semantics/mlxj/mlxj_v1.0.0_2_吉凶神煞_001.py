"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.845132
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
    semantic_id="mlxj_v1.0.0_2_吉凶神煞_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2吉凶神煞(SemanticEntry):
    """
    #### 原文摘要

**吉神**：天德、月德、天乙贵人、日禄、驿马

**凶煞**：
- 月杀：主破财伤人（正丑二戌三未四辰...）
- 三坼：主坟墓不安（正月起丑二月寅...）
- 六害穿心：六害...
    """
    
    original_text: str = """#### 原文摘要

**吉神**：天德、月德、天乙贵人、日禄、驿马

**凶煞**：
- 月杀：主破财伤人（正丑二戌三未四辰...）
- 三坼：主坟墓不安（正月起丑二月寅...）
- 六害穿心：六害祸非轻（子未不堪亲，丑害午，寅巳嗔，卯害辰，申害亥，酉戌相逢转见深）"""
    normalized_text_zh: str = """"""
    subject: str = "2 吉凶神煞"
    factor_refs: list = ['source_ref']
    
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
        book_id="mlxj",
        chapter="",
        l1_anchor="mlxj_v1.0.0_2_吉凶神煞_001_L1",
    )
    version: str = "1.0.0"
