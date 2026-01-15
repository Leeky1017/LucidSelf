"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.842924
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
    semantic_id="mlxj_v1.0.0_1_将相类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1将相类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 梦见太公望：暮年际遇
- 梦见管仲：终佐齐桓
- 梦见诸葛亮：风云际会，鱼水投欢
- 梦见魏征：君明臣良
- 梦见范仲淹：身贵子奇
- 梦见司马光：史学专工...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 梦见太公望：暮年际遇
- 梦见管仲：终佐齐桓
- 梦见诸葛亮：风云际会，鱼水投欢
- 梦见魏征：君明臣良
- 梦见范仲淹：身贵子奇
- 梦见司马光：史学专工

**吉类**：
- 梦见李靖：功名利达，出征有功
- 梦见房玄龄：德位兼隆
- 梦见曹彬：文武兼全之佐

**贞吉否凶类**：
- 梦见韩信：得志于当时，而终不得保其身
- 梦见霍光：勋高望重，防骨肉之忧
- 梦见李德裕/牛僧孺：朋党之戒

#### 典故素材

| 梦象 | 梦者 | 应验 | 出处 |
|------|------|------|------|
| 梦李白 | 郭祥正母 | 生祥正有诗名 | 宋 |
| 梦范文正公遗诗 | 罗伦 | 及第而宦不达 | 明 |
| 梦孔子 | 谯周 | 明年卒 | 三国 |
| 梦文天祥 | 京师某人 | 朱状元寓其家 | 明 |"""
    normalized_text_zh: str = """"""
    subject: str = "1 将相类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_将相类诸兆_001_L1",
    )
    version: str = "1.0.0"
