"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.802951
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
    semantic_id="mlxj_v1.0.0_2_竹荻类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2竹荻类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 竹大吉：冲霄之干，君子之名，介直之节

**吉类**：
- 慈孝竹：孝悌
- 潇湘竹：神驰千里
- 方竹：正直不阿
- 山上竹：出人头地
- 义竹吉：得清名...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 竹大吉：冲霄之干，君子之名，介直之节

**吉类**：
- 慈孝竹：孝悌
- 潇湘竹：神驰千里
- 方竹：正直不阿
- 山上竹：出人头地
- 义竹吉：得清名，遇义友
- 孝竹吉：儿孙绕膝
- 种竹吉：得良友

**凶类**：
- 竹被风敲：生烦恼
- 竹被雨淋：忧郁堪憎
- 斑竹入兆：两地泪零

#### 典故

- 河阴尉王君炳梦老妪赠竹：竹字两个，二子俱中选"""
    normalized_text_zh: str = """"""
    subject: str = "2 竹荻类诸兆"
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
        book_id="mlxj",
        chapter="",
        l1_anchor="mlxj_v1.0.0_2_竹荻类诸兆_001_L1",
    )
    version: str = "1.0.0"
