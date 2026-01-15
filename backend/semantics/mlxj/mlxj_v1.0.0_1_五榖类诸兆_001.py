"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.798217
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
    semantic_id="mlxj_v1.0.0_1_五榖类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1五榖类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 人送糕至大吉：糕=高，诸事高升
- 面大吉：诸事和调，众心顺适

**吉类**：
- 裹粽吉：生男育女
- 解粽吉：解衣推食
- 食饼：前后圆合
- 食圆子...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 人送糕至大吉：糕=高，诸事高升
- 面大吉：诸事和调，众心顺适

**吉类**：
- 裹粽吉：生男育女
- 解粽吉：解衣推食
- 食饼：前后圆合
- 食圆子吉：团圆之象

#### 糕类象征

| 梦象 | 主应 |
|------|------|
| 人送糕至 | 铨选高擢，婚姻高门 |
| 食饼 | 婚姻成就，交易兼并 |
| 裹粽 | 生男育女，裹根之征 |
| 解粽 | 解衣推食，受恩宠 |"""
    normalized_text_zh: str = """"""
    subject: str = "1 五榖类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_五榖类诸兆_001_L1",
    )
    version: str = "1.0.0"
