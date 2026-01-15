"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.821478
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
    semantic_id="mlxj_v1.0.0_1_工作类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1工作类诸兆(SemanticEntry):
    """
    #### 分类汇总

**斧凿类**：
- 斧吉：刚断锋芒，乾健而顺
- 凿贞吉否凶：受苦开心，凶中有吉
- 圆凿吉：婉转玲珑，渐渐亨通

**锯刨类**：
- 锯吉：齿牙钝利，口吐青莲，直道而行
-...
    """
    
    original_text: str = """#### 分类汇总

**斧凿类**：
- 斧吉：刚断锋芒，乾健而顺
- 凿贞吉否凶：受苦开心，凶中有吉
- 圆凿吉：婉转玲珑，渐渐亨通

**锯刨类**：
- 锯吉：齿牙钝利，口吐青莲，直道而行
- 推爮吉：抱负惊人
- 墨斗竹䈜吉：委曲求全，枉者直屈者伸

**炉冶类**：
- 炼炉大吉：穷则思变，变则通
- 囚人梦炉：刑罚之坷
- 风箱风车吉：家人卦，内正外正

#### 工具象征体系

| 工具 | 象征 | 主应 |
|------|------|------|
| 斧 | 刚断 | 君子道长 |
| 凿 | 开心 | 凶中有吉 |
| 锯 | 齿牙 | 直道而行 |
| 墨斗 | 曲直 | 委曲求全 |
| 炉 | 变化 | 穷变通达 |"""
    normalized_text_zh: str = """"""
    subject: str = "1 工作类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_工作类诸兆_001_L1",
    )
    version: str = "1.0.0"
