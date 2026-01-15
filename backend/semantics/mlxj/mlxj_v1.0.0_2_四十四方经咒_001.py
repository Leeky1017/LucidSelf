"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.816074
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
    semantic_id="mlxj_v1.0.0_2_四十四方经咒_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2四十四方经咒(SemanticEntry):
    """
    #### 原文

四十四方经云：夜卧将欲合眼时，先以手抚心三过，闭目叩齿三通，微咒一遍。咒曰：

**大灵九宫，大乙守房，百神参位，魂魄和同，长生不死，塞邪灭凶。**

如此祝之，冥心而睡，则魂魄守舍...
    """
    
    original_text: str = """#### 原文

四十四方经云：夜卧将欲合眼时，先以手抚心三过，闭目叩齿三通，微咒一遍。咒曰：

**大灵九宫，大乙守房，百神参位，魂魄和同，长生不死，塞邪灭凶。**

如此祝之，冥心而睡，则魂魄守舍，眠卧清宁，邪梦不入，永获贞吉也。

#### 咒语分析

| 句式 | 内涵 |
|------|------|
| 大灵九宫 | 召请九宫神灵 |
| 大乙守房 | 太一神守护寝室 |
| 百神参位 | 众神各就其位 |
| 魂魄和同 | 魂魄和谐统一 |
| 长生不死 | 祈求长寿 |
| 塞邪灭凶 | 阻塞邪气消灭凶险 |

#### 行咒步骤

1. 夜卧将欲合眼时
2. 以手抚心三过
3. 闭目叩齿三通
4. 微咒（默念）一遍"""
    normalized_text_zh: str = """"""
    subject: str = "2 四十四方经咒"
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
        l1_anchor="mlxj_v1.0.0_2_四十四方经咒_001_L1",
    )
    version: str = "1.0.0"
