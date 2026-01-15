"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.808930
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
    semantic_id="mlxj_v1.0.0_1_朱子梦论_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1朱子梦论(SemanticEntry):
    """
    #### 原文（source_text）

人之精神与天地阴阳流通，故昼之所为，夜之所梦，其善恶吉凶，各以类应。寤寐者，心之动静也。有思无思者，又动中之动静也；有梦无梦者，又静中之动静也。但寤阳而寐阴...
    """
    
    original_text: str = """#### 原文（source_text）

人之精神与天地阴阳流通，故昼之所为，夜之所梦，其善恶吉凶，各以类应。寤寐者，心之动静也。有思无思者，又动中之动静也；有梦无梦者，又静中之动静也。但寤阳而寐阴，寤清而寐浊，寤有主而寐无主，故寂然感通之妙，必于寤而言之。

周礼献吉梦，赠恶梦，其于天人相与之际，察之审而敬之至矣。

#### 规范化释义（primary_lang_explained）

朱子论梦：人之精神与天地阴阳流通，故昼之所为、夜之所梦，其善恶吉凶各以类应。

寤寐关系：
- 寤寐 = 心之动静
- 有思无思 = 动中之动静
- 有梦无梦 = 静中之动静

寤寐差异：
- 寤阳而寐阴
- 寤清而寐浊
- 寤有主而寐无主

故寂然感通之妙，必于寤而言之。周礼献吉梦、赠恶梦，其于天人相与之际，察之审而敬之至矣。"""
    normalized_text_zh: str = """"""
    subject: str = "1 朱子梦论"
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
        l1_anchor="mlxj_v1.0.0_1_朱子梦论_001_L1",
    )
    version: str = "1.0.0"
