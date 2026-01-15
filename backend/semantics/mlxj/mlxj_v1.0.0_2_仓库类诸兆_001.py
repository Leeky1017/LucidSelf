"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.814387
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
    semantic_id="mlxj_v1.0.0_2_仓库类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2仓库类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 内帑御库大吉：少者天禄，老者天年
- 太仓吉：刑文伟典故

**吉类**：
- 仓廪盈足：年丰民足
- 武库：学博才高

**凶类**：
- 仓廪虚耗：年荒...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 内帑御库大吉：少者天禄，老者天年
- 太仓吉：刑文伟典故

**吉类**：
- 仓廪盈足：年丰民足
- 武库：学博才高

**凶类**：
- 仓廪虚耗：年荒国乱
- 府库虚耗：下人凶

#### 仓库与身份对应

| 梦象 | 上人 | 下人 |
|------|------|------|
| 仓廪盈足 | 凶 | 吉 |
| 府库盈足 | 凶 | 吉 |"""
    normalized_text_zh: str = """"""
    subject: str = "2 仓库类诸兆"
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
        l1_anchor="mlxj_v1.0.0_2_仓库类诸兆_001_L1",
    )
    version: str = "1.0.0"
