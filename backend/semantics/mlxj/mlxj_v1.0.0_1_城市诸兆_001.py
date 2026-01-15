"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.826001
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
    semantic_id="mlxj_v1.0.0_1_城市诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1城市诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 登城大吉：高明处世，荣华富贵
- 修筑城垣吉：重修基宇，家业亨通
- 城上有棺吉：棺=官，迁官高职
- 城上金碧如宝石：成金成玉，财利环围

**吉类**：...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 登城大吉：高明处世，荣华富贵
- 修筑城垣吉：重修基宇，家业亨通
- 城上有棺吉：棺=官，迁官高职
- 城上金碧如宝石：成金成玉，财利环围

**吉类**：
- 游城见宫殿楼台：升之高，环之转，移椽迁居
- 骑马环城走吉：文人挂名魁首，武士戈鸣戟动

**凶类**：
- 城毁凶：家庭变异，萧墙祸起
- 城门开无数鬼出：兵戈变起/名魁辈出（因人而异）

**贞吉否凶类**：
- 雷电环城：有权有势，有动有变
- 城上哭：平人主远行，女人主孤宿

#### 典故素材

| 梦象 | 梦者 | 应验 | 出处 |
|------|------|------|------|
| 上广陵城 | 荀伯玉 | 见二青衣小儿语「草中肃」 | 南齐 |
| 城郭玉璋 | 某人 | 连得三子皆贵 | 古 |"""
    normalized_text_zh: str = """"""
    subject: str = "1 城市诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_城市诸兆_001_L1",
    )
    version: str = "1.0.0"
