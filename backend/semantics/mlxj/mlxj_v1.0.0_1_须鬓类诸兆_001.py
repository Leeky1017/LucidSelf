"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.817519
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
    semantic_id="mlxj_v1.0.0_1_须鬓类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1须鬓类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 无须眉大吉：上下光辉（孔丘典故）
- 与以帝须大吉：周必大梦典故
- 须长过身大吉：有余之兆
- 须髯尽白大吉：寿征（郑叔通典故）
- 鬓上穿珠大吉：垂缨大...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 无须眉大吉：上下光辉（孔丘典故）
- 与以帝须大吉：周必大梦典故
- 须长过身大吉：有余之兆
- 须髯尽白大吉：寿征（郑叔通典故）
- 鬓上穿珠大吉：垂缨大贵

**吉类**：
- 胡须吉：清疏长润者不贵则富
- 添须吉：升官添禄益寿
- 人剃髭吉：削篆替职
- 须鬓飘扬如旌缨吉：名显誉扬
- 鬓长连须吉：朋友宾客

**凶类**：
- 须鬓忽落凶：子孙亡，妻孥殒
- 须从口中生凶：语言难忍

#### 须鬓核心象征

- 须=丈夫福寿之征
- 鬓=年岁寿命之象
- 须白=寿征
- 须长=有余
- 须落=亲丁殒殁"""
    normalized_text_zh: str = """"""
    subject: str = "1 须鬓类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_须鬓类诸兆_001_L1",
    )
    version: str = "1.0.0"
