"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.798237
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
    semantic_id="mlxj_v1.0.0_2_杂物类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2杂物类诸兆(SemanticEntry):
    """
    #### 吞食异物

**吉类**：
- 吞书：益智慧，长识见（唐僖宗典故）
- 吞珠吉：贵重瑞征
- 吞玉大吉：荣显佳兆

**凶类**：
- 吞炭凶：寒心事，失音
- 吞针：剌人肠肚，天各二方
-...
    """
    
    original_text: str = """#### 吞食异物

**吉类**：
- 吞书：益智慧，长识见（唐僖宗典故）
- 吞珠吉：贵重瑞征
- 吞玉大吉：荣显佳兆

**凶类**：
- 吞炭凶：寒心事，失音
- 吞针：剌人肠肚，天各二方
- 吞毡：出塞之兆，迍邅不达"""
    normalized_text_zh: str = """"""
    subject: str = "2 杂物类诸兆"
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
        l1_anchor="mlxj_v1.0.0_2_杂物类诸兆_001_L1",
    )
    version: str = "1.0.0"
