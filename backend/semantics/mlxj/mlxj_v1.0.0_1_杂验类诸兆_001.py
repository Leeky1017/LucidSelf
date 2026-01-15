"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.827666
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
    semantic_id="mlxj_v1.0.0_1_杂验类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1杂验类诸兆(SemanticEntry):
    """
    #### 阴德报应

**吉类**：
- 得药疗母病：夏侯诉梦父告药在桑树
- 借钱千万：周犨贫梦天公借张车子钱
- 解监军祸：杨廷璋梦神人告有阴德
- 飞云渡免水厄：少年救人一命获报
- 赠金延算：...
    """
    
    original_text: str = """#### 阴德报应

**吉类**：
- 得药疗母病：夏侯诉梦父告药在桑树
- 借钱千万：周犨贫梦天公借张车子钱
- 解监军祸：杨廷璋梦神人告有阴德
- 飞云渡免水厄：少年救人一命获报
- 赠金延算：巨商梦神示中秋前后三日厄

#### 祸患应验

- 欠柴七千七百束：柳凌梦后月余卒
- 二十年前事：真德秀破杀僧案

#### 典故

- 杨廷璋与荆罕儒：同梦神人解祸
- 飞云渡少年：救失环女脱溺厄
- 巨商救妇人：赠钱后逃中秋之劫"""
    normalized_text_zh: str = """"""
    subject: str = "1 杂验类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_杂验类诸兆_001_L1",
    )
    version: str = "1.0.0"
