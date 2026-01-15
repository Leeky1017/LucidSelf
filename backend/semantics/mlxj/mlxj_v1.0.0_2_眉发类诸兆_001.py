"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.817503
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
    semantic_id="mlxj_v1.0.0_2_眉发类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2眉发类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 眉忽白大吉：福寿白眉之兆
- 两眉尽落吉：颧上光光，长生贵显
- 发垂颡齐眉大吉：男得美妇，女得良人
- 披发戴冠吉：通亨之兆
- 自看后髪大吉：生贵子，成...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 眉忽白大吉：福寿白眉之兆
- 两眉尽落吉：颧上光光，长生贵显
- 发垂颡齐眉大吉：男得美妇，女得良人
- 披发戴冠吉：通亨之兆
- 自看后髪大吉：生贵子，成家立业

**吉类**：
- 眉生目下吉：应有良媒来
- 画眉吉：高年延龄，童子得贤傅
- 剃眉吉：安闲富贵之兆
- 披发游市廛中吉：利获千金
- 开一窍在发际下吉：学者大贵

**凶类**：
- 落一眉凶：夭折孤贫之梦
- 眉分四段凶：男女有灾
- 露顶披发盖面大凶：赵持满典故
- 发藏角内凶：髡刑之兆
- 髡凶：子忧父母，女忧夫

#### 眉发象征体系

| 部位 | 象征 | 吉兆 | 凶兆 |
|------|------|------|------|
| 眉 | 祥云护日 | 白/长/齐 | 落/断/分 |
| 发 | 法度/寿命 | 垂齐/戴冠 | 髡/露/盖面 |
| 后发 | 子孙后福 | 茂盛 | 衰败 |"""
    normalized_text_zh: str = """"""
    subject: str = "2 眉发类诸兆"
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
        l1_anchor="mlxj_v1.0.0_2_眉发类诸兆_001_L1",
    )
    version: str = "1.0.0"
