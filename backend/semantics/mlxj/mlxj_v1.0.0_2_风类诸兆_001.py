"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.831748
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
    semantic_id="mlxj_v1.0.0_2_风类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2风类诸兆(SemanticEntry):
    """
    #### 分类汇总

**吉类**：
- 风送云开，见三光：风捲云去无踪，光明亮运通达，主否去泰生
- 彩云生：云为山川气，彩为光明象，主子秀年丰
- 祥云四起：黄利四季，青春、赤夏、白秋、黑冬，应时...
    """
    
    original_text: str = """#### 分类汇总

**吉类**：
- 风送云开，见三光：风捲云去无踪，光明亮运通达，主否去泰生
- 彩云生：云为山川气，彩为光明象，主子秀年丰
- 祥云四起：黄利四季，青春、赤夏、白秋、黑冬，应时者吉
- 红云黄云从地而起：彩色云从地起，主爵位升迁、家业兴隆

**凶类**：
- 狂风骤雨：主朝廷有威命号令，常人诸事有阻
- 风走砂石，吹尘垢：地不宁，有忧事，下害上（黄帝梦典故）
- 云遮星斗：群臣窃柄，婢仆专权（元顺帝梦典故）

**贞吉否凶类**：
- 风忽止：贵人谢印归山，文人束书改业
- 塞外风起：行师防贼，商贾防掠

#### 典故素材

| 梦象 | 梦者 | 应验 | 出处 |
|------|------|------|------|
| 大风吹尘垢 | 黄帝 | 得风后于海隅，登为相 | 上古 |
| 黑云自西北来 | 元顺帝 | 京师北敌之乱，百寮残毁 | 元 |"""
    normalized_text_zh: str = """"""
    subject: str = "2 风类诸兆"
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
        l1_anchor="mlxj_v1.0.0_2_风类诸兆_001_L1",
    )
    version: str = "1.0.0"
