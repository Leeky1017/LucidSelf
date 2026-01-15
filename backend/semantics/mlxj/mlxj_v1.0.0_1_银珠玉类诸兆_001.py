"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.785829
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
    semantic_id="mlxj_v1.0.0_1_银珠玉类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1银珠玉类诸兆(SemanticEntry):
    """
    #### 银类汇总

**吉类**：
- 黄银吉：光辉祥瑞
- 银灯吉：行事不暗昧
- 银砚大吉：文字成珠玑
- 银甲吉：名当第一

**贞吉否凶类**：
- 银贞吉否凶：艮止不动
- 银钩凶：勾引私...
    """
    
    original_text: str = """#### 银类汇总

**吉类**：
- 黄银吉：光辉祥瑞
- 银灯吉：行事不暗昧
- 银砚大吉：文字成珠玑
- 银甲吉：名当第一

**贞吉否凶类**：
- 银贞吉否凶：艮止不动
- 银钩凶：勾引私情
- 银杯双飞至凶：悲也

#### 珠玉类汇总

**大吉类**：
- 玉光𤇄烁：名利兼得
- 吞玉大吉：荣显佳兆
- 香玉大吉：德之芳馨
- 两手捧玉大吉：成大器

**吉类**：
- 玉盘玉枕玉带吉：帝王之宝
- 玉箸吉：邵康节母典故
- 玉环吉：否极泰来
- 种玉吉：阳雍伯典故

**凶类**：
- 泣玉贞吉否凶：有志莫伸
- 玉玦：决断/残缺
- 衔璧凶：屈辱丧亡"""
    normalized_text_zh: str = """"""
    subject: str = "1 银珠玉类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_银珠玉类诸兆_001_L1",
    )
    version: str = "1.0.0"
