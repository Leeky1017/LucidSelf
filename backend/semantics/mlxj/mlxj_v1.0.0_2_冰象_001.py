"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.831805
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
    semantic_id="mlxj_v1.0.0_2_冰象_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2冰象(SemanticEntry):
    """
    #### 分类汇总

**吉类**：
- 水结冰吉：财源结聚，婚姻就，交易成
- 立冰上与冰下人语：令狐策典故

**凶类**：
- 冰解：大不祥，功名未得，冰消瓦解（但争讼疾病者为解散之象）

**...
    """
    
    original_text: str = """#### 分类汇总

**吉类**：
- 水结冰吉：财源结聚，婚姻就，交易成
- 立冰上与冰下人语：令狐策典故

**凶类**：
- 冰解：大不祥，功名未得，冰消瓦解（但争讼疾病者为解散之象）

**贞吉否凶类**：
- 冰拥成山：易成易败，乍辱乍荣

#### 典故素材

| 梦象 | 梦者 | 应验 | 出处 |
|------|------|------|------|
| 立冰上与冰下人语 | 令狐策 | - | - |"""
    normalized_text_zh: str = """"""
    subject: str = "2 冰象"
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
        l1_anchor="mlxj_v1.0.0_2_冰象_001_L1",
    )
    version: str = "1.0.0"
