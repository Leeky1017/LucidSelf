"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.819306
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
    semantic_id="mlxj_v1.0.0_1_宠嬖悍妒类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1宠嬖悍妒类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大凶类**：
- 妹喜大凶：蛊惑君心，国必丧家必亡
- 妲己大凶：更有妖邪之象，精怪作变
- 虢国夫人凶：因亲得贵，祸不旋踵

**贞吉否凶类**：
- 买臣妻：夫妻离异，先...
    """
    
    original_text: str = """#### 分类汇总

**大凶类**：
- 妹喜大凶：蛊惑君心，国必丧家必亡
- 妲己大凶：更有妖邪之象，精怪作变
- 虢国夫人凶：因亲得贵，祸不旋踵

**贞吉否凶类**：
- 买臣妻：夫妻离异，先困后亨
- 苏若兰：骄傲则凶，谦恭则吉
- 十一娘吉：有丈夫之概，而多嫉心
- 韩佗胄妻：内人所苦，覆灭宗嗣
- 长舌妇：巧言令色，浸润之谮

#### 警戒要点

宠嬖悍妒类梦象多为警戒之兆：
- 主阴人起祸、内难将临
- 主夫纲失坠、女人当权
- 主口舌是非、搅乱家庭
- 修省则可化凶为吉"""
    normalized_text_zh: str = """"""
    subject: str = "1 宠嬖悍妒类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_宠嬖悍妒类诸兆_001_L1",
    )
    version: str = "1.0.0"
