"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.793473
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
    semantic_id="mlxj_v1.0.0_3_月类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 3月类诸兆(SemanticEntry):
    """
    #### 原文摘要与分类

**大吉类**：
- 月圆明亮大吉：光华圆满，凡事遂意
- 月入怀大吉：孕贵女之象（王政君典故）
- 登山擎月大吉：乘龙娇婿，功名秋榜首
- 月出海中吉：财源兴发，子姓连生...
    """
    
    original_text: str = """#### 原文摘要与分类

**大吉类**：
- 月圆明亮大吉：光华圆满，凡事遂意
- 月入怀大吉：孕贵女之象（王政君典故）
- 登山擎月大吉：乘龙娇婿，功名秋榜首
- 月出海中吉：财源兴发，子姓连生
- 抱月大吉：妇人得大贵女，男子得贤美妻
- 吞月轮大吉：贵人入腹，文人才学日进
- 月中折桂大吉：文士不必占，已显兆
- 月华大吉：贵富寿美贵秀

**凶类**：
- 月暗凶：孕妇则吉，余主母忧妻灾
- 月坠落凶：国母凶忧，诸事不祥
- 月忽云遮凶：下人欺上，讼不理名不遂
- 波底映月凶：功名子嗣如水中月
- 月坠井中大凶：兔逢窟阱，功名不遂

**贞吉否凶类**：
- 捉月：独利文人，卯年折桂
- 月入楼悬梁上：家室光荣，女人主悬梁自缢
- 儿从月中堕：孕妇主胎落，以手取之为产贵

#### 典故素材

| 梦象 | 梦者 | 应验 | 出处 |
|------|------|------|------|
| 月入怀 | 王禁妻李氏 | 生女政君，后为成帝母 | 汉 |
| 掌月轮吞之 | 尉迟裴氏 | 生神僧，慈恩教主 | 唐 |
| 挟子入月中 | 何仲举母 | 子登唐长兴进士 | 唐 |
| 月中有花 | 试官 | 月鲁不花中式浙闱第一 | 元 |"""
    normalized_text_zh: str = """"""
    subject: str = "3 月类诸兆"
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
        l1_anchor="mlxj_v1.0.0_3_月类诸兆_001_L1",
    )
    version: str = "1.0.0"
