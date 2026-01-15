"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.793487
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
    semantic_id="mlxj_v1.0.0_2_星象诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2星象诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 大星明朗大吉：公卿之应，禄位显
- 星芒光彩：文章盛进，女人夫荣子贵
- 文昌星大吉：文明才名大利
- 手执斗杓吉：执掌朝纲，权倾四海
- 三星照户大吉：贵...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 大星明朗大吉：公卿之应，禄位显
- 星芒光彩：文章盛进，女人夫荣子贵
- 文昌星大吉：文明才名大利
- 手执斗杓吉：执掌朝纲，权倾四海
- 三星照户大吉：贵至三公，富有三世
- 星堕卧内吉：文士应列宿当大魁
- 吞星吉：当大贵

**吉类**：
- 星行动吉：权位升迁，改旧图新
- 星行列整：兄弟协睦，子孙茂盛
- 足履星枢：爵位崇高，威权在手（高欢典故）

**凶类**：
- 星辰散乱：群工散乱，大臣忧危
- 流星堕地凶：命应倾，官非

**贞吉否凶类**：
- 星流不落：迁移之兆，病人有救

#### 典故素材

| 梦象 | 梦者 | 应验 | 出处 |
|------|------|------|------|
| 文昌星降 | 吕思诚母冯氏 | 生吕思诚，目有神光 | 元 |
| 履众星而行 | 高欢 | 代魏为帝 | 北齐 |
| 立北斗下，列第七位 | 袁郭 | 第七名登第 | 唐 |"""
    normalized_text_zh: str = """"""
    subject: str = "2 星象诸兆"
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
        l1_anchor="mlxj_v1.0.0_2_星象诸兆_001_L1",
    )
    version: str = "1.0.0"
