"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.798202
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
    semantic_id="mlxj_v1.0.0_2_泉茗类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2泉茗类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 饮天河水：大贵
- 饮海潮大吉：当朝沐恩，名扬四海
- 饮江湖水大吉：心广体胖，发荣滋长

**吉类**：
- 饮天泉吉：沾膏泽之兆
- 冰雪化水饮之：先难...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 饮天河水：大贵
- 饮海潮大吉：当朝沐恩，名扬四海
- 饮江湖水大吉：心广体胖，发荣滋长

**吉类**：
- 饮天泉吉：沾膏泽之兆
- 冰雪化水饮之：先难后易，绝处逢生
- 饮山泉：恬澹清凉
- 饮池沼水：举子赴春官

**茶汤类**：
| 汤类 | 主应 |
|------|------|
| 生姜汤 | 御寒通神，治病回生 |
| 豆荚汤 | 亲戚来会 |
| 糖汤 | 修斋设醮 |
| 薄荷汤 | 除烦热解焦躁 |
| 木樨汤 | 折桂，生贵子 |
| 蜜汤大吉 | 门庭喜庆，家室安宁 |"""
    normalized_text_zh: str = """"""
    subject: str = "2 泉茗类诸兆"
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
        l1_anchor="mlxj_v1.0.0_2_泉茗类诸兆_001_L1",
    )
    version: str = "1.0.0"
