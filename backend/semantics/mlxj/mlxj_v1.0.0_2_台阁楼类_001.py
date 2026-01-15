"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.814364
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
    semantic_id="mlxj_v1.0.0_2_台阁楼类_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2台阁楼类(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 万岁楼吉：贵者事几，老者寿征
- 台榭楼阁：心胸精气旺足

**吉类**：
- 登台遇龙蛇贞吉：董遵诲典故
- 楼台高阁：气旺精足

**凶类**：
- 迷...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 万岁楼吉：贵者事几，老者寿征
- 台榭楼阁：心胸精气旺足

**吉类**：
- 登台遇龙蛇贞吉：董遵诲典故
- 楼台高阁：气旺精足

**凶类**：
- 迷楼凶：隋炀帝典故，迷而不悟
- 登白台四望无所见凶：乐平王丕典故

#### 楼台象征

| 楼名 | 主应 |
|------|------|
| 万岁楼 | 贵者事几，老者寿征 |
| 迷楼 | 迷而不悟，大凶 |
| 乌台 | 御史之职 |
| 岳阳楼 | 文章之象 |"""
    normalized_text_zh: str = """"""
    subject: str = "2 台阁楼类"
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
        l1_anchor="mlxj_v1.0.0_2_台阁楼类_001_L1",
    )
    version: str = "1.0.0"
