"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.783939
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
    semantic_id="mlxj_v1.0.0_2_天类诸征_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2天类诸征(SemanticEntry):
    """
    #### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 虞 | 帝尧 | 上天 | 登帝位 |
| 周 | 穆子 | 天压己 ...
    """
    
    original_text: str = """#### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 虞 | 帝尧 | 上天 | 登帝位 |
| 周 | 穆子 | 天压己 | 得牛助胜 |
| 春秋 | 郑文公妾 | 天与己兰 | 生贵子 |

#### 天压己典故

周穆子梦天压己弗胜，顾见人黑而上偻，深目而𢔾喙，号之曰"牛"，助之乃胜。后果遇庚宗妇人献雉之子，形貌如梦中所见，遂使为𥪡。"""
    normalized_text_zh: str = """"""
    subject: str = "2 天类诸征"
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
        l1_anchor="mlxj_v1.0.0_2_天类诸征_001_L1",
    )
    version: str = "1.0.0"
