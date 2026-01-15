"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.817512
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
    semantic_id="mlxj_v1.0.0_1_口齿类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1口齿类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 口内生莲花吉：胎孕生男，婚姻和合
- 二口吉：吕字为佳音（辽主典故）
- 口中出毫大吉：王思聪典故
- 口衔头发大吉：争讼得胜
- 齿咬人头大吉：文明名盛
...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 口内生莲花吉：胎孕生男，婚姻和合
- 二口吉：吕字为佳音（辽主典故）
- 口中出毫大吉：王思聪典故
- 口衔头发大吉：争讼得胜
- 齿咬人头大吉：文明名盛

**吉类**：
- 净口吉：口净气清之象
- 步入他人之口吉：有人荐举之兆
- 人唾口中吉：得人精气，文章进逵
- 洗齿吉：口舌散除，是非消解
- 齿长大吉：位高爵尊，寿长嗣盛

**凶类**：
- 口变小凶：小口舌之兆
- 口中粉碎凶：大祸将至
- 口流延凶：贪杯之象
- 口吐火焰凶：心火炎熏
- 齿身被人拔去大凶：亲丁被害
- 牙落无血凶：亡父母丧

#### 口齿与亲属对应

| 齿位 | 对应亲属 |
|------|---------|
| 上唇齿左 | 父 |
| 上唇齿右 | 母 |
| 盘牙 | 祖孙 |
| 下唇齿左 | 男 |
| 下唇齿右 | 女 |"""
    normalized_text_zh: str = """"""
    subject: str = "1 口齿类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_口齿类诸兆_001_L1",
    )
    version: str = "1.0.0"
