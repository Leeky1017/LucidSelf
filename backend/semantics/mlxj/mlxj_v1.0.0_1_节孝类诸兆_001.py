"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.819299
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
    semantic_id="mlxj_v1.0.0_1_节孝类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1节孝类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 无双大吉：独握枢机，获利十倍
- 银瓶吉：黄白之资出自穴，武臣建旌节

**吉类**：
- 缇萦吉：上书救父，主司纶绋
- 曹娥吉：聪俊过人，孝闻远播
- ...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 无双大吉：独握枢机，获利十倍
- 银瓶吉：黄白之资出自穴，武臣建旌节

**吉类**：
- 缇萦吉：上书救父，主司纶绋
- 曹娥吉：聪俊过人，孝闻远播
- 绿珠吉：得奇宝异珍
- 谢小蛾吉：以片言动主

**贞吉否凶类**：
- 代戍女：更姓易名，甲紐服劳
- 瑞筠：终身勤劳之象
- 李烈妇：艰难坎坷中不失圆正之节

#### 节孝人物核心特征

| 人物 | 典故 | 梦象主应 |
|------|------|---------|
| 缇萦 | 上书救父 | 孝感动天 |
| 曹娥 | 投江救父 | 孝名远播 |
| 绿珠 | 坠楼殉节 | 得奇宝 |
| 银瓶 | 投井殉父 | 忠孝义烈 |"""
    normalized_text_zh: str = """"""
    subject: str = "1 节孝类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_节孝类诸兆_001_L1",
    )
    version: str = "1.0.0"
