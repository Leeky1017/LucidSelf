"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.831782
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
    semantic_id="mlxj_v1.0.0_1_雾象_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1雾象(SemanticEntry):
    """
    #### 分类汇总

**凶类**：
- 黑雾迷身，开复合大凶：黑雾为瘴厉恶氛，迷复凶，有灾
- 雾迷宫室：烟绕屋宇，防回禄之灾
- 黄雾塞天凶：天地不明，日月不现，边疆有警

**贞吉否凶类**：
...
    """
    
    original_text: str = """#### 分类汇总

**凶类**：
- 黑雾迷身，开复合大凶：黑雾为瘴厉恶氛，迷复凶，有灾
- 雾迷宫室：烟绕屋宇，防回禄之灾
- 黄雾塞天凶：天地不明，日月不现，边疆有警

**贞吉否凶类**：
- 大雾中行：凡事皆有润泽至，但疾病未痊、讼事难明
- 露雾昏迷：蒙昧不明，不宜进前（曹操赤壁典故）

#### 典故素材

| 梦象 | 梦者 | 应验 | 出处 |
|------|------|------|------|
| 露雾昏迷 | 曹操 | 赤壁之败 | 三国 |"""
    normalized_text_zh: str = """"""
    subject: str = "1 雾象"
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
        l1_anchor="mlxj_v1.0.0_1_雾象_001_L1",
    )
    version: str = "1.0.0"
