"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.789182
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
    semantic_id="mlxj_v1.0.0_4_五神环传吉凶图_001",
    book_id="mlxj",
    engine_id="dream"
)
class 4五神环传吉凶图(SemanticEntry):
    """
    #### 原文摘要

**环传吉图**：梦五神所属事物，自肝而达心，自心而达脾，自脾而达肺，自肺而达肾，自肾而复达肝，得相生之气而形于神魂之交者，是为顺环而占吉。

**环传凶图**：梦五神所属事物，...
    """
    
    original_text: str = """#### 原文摘要

**环传吉图**：梦五神所属事物，自肝而达心，自心而达脾，自脾而达肺，自肺而达肾，自肾而复达肝，得相生之气而形于神魂之交者，是为顺环而占吉。

**环传凶图**：梦五神所属事物，自肺而入肝，自肝而入脾，自脾而入肾，自肾而入心，自心而复入肺，得相克之数而形于神魂之会者，是为逆环而占凶。

#### 核心要点

- **顺环吉**：肝→心→脾→肺→肾→肝（木→火→土→金→水→木）
- **逆环凶**：肺→肝→脾→肾→心→肺（金→木→土→水→火→金）
- 顺环为相生之气，主吉
- 逆环为相克之数，主凶"""
    normalized_text_zh: str = """"""
    subject: str = "4 五神环传吉凶图"
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
        l1_anchor="mlxj_v1.0.0_4_五神环传吉凶图_001_L1",
    )
    version: str = "1.0.0"
