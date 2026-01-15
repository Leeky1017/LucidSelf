"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.795272
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
    semantic_id="mlxj_v1.0.0_1_牧具类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1牧具类诸兆(SemanticEntry):
    """
    #### 分类汇总

**马槽**：
- 群马渡河：得国如受大封
- 三马一槽：魏武帝典故（防司马氏）

**马鞍踏凳**：
- 贵人梦之：劳役
- 富人梦之：安宁
- 贫穷梦之：利益
- 病人梦之：...
    """
    
    original_text: str = """#### 分类汇总

**马槽**：
- 群马渡河：得国如受大封
- 三马一槽：魏武帝典故（防司马氏）

**马鞍踏凳**：
- 贵人梦之：劳役
- 富人梦之：安宁
- 贫穷梦之：利益
- 病人梦之：得愈

**鞭**：
- 平安梦之：得戒御不虞之策
- 险难梦之：消灾除暴

#### 农具类诸兆

**斗斛**：
- 梦此在天：为雷电
- 梦此为魁星：神鬼
- 梦顶之首上：有险事
- 梦负背上：灾消祸减

**箩担**：
- 主任重道远，财聚事冗
- 人君梦之有物无人：求贤未遂
- 贫士梦之：远行
- 庶人梦之：财利"""
    normalized_text_zh: str = """"""
    subject: str = "1 牧具类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_牧具类诸兆_001_L1",
    )
    version: str = "1.0.0"
