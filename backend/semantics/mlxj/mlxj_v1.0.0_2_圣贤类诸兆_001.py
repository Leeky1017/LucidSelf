"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.842916
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
    semantic_id="mlxj_v1.0.0_2_圣贤类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2圣贤类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 梦见孔子：文学超迈，德业崇隆
- 梦见孟子：道学有传，文才超越
- 梦见周公：非无志于世务者
- 梦见老子：益算知礼，清净为宗
- 梦见诸葛武侯：风云际会
...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 梦见孔子：文学超迈，德业崇隆
- 梦见孟子：道学有传，文才超越
- 梦见周公：非无志于世务者
- 梦见老子：益算知礼，清净为宗
- 梦见诸葛武侯：风云际会
- 梦见范蠡：非贵则富，终始安享

**吉类**：
- 梦见管仲：佳征
- 梦见子产：柄国之政，推惠爱民
- 梦见晏婴：柄政清操
- 梦见曾参：德进名高
- 梦见子贡：庙廷之器

**凶类**：
- 梦见阳虎：外是心非之变
- 梦见巨无霸：爪牙角毒之害

**贞吉否凶类**：
- 梦见屈原：神灵欲依其地，或灵气托生
- 梦见李膺：发高第而防小人嫉忌

#### 圣贤应验模式

| 应验类型 | 说明 | 例证 |
|---------|------|------|
| 托生转世 | 圣贤来托生，产奇子 | 郭祥正母梦李白而生祥正 |
| 赐福降感 | 神灵赐福指点 | 罗伦梦范文正公遗诗 |
| 促算警示 | 提示寿命将尽 | 谯周梦见孔子，明年卒 |
| 冥中祈请 | 神灵有所求 | 王陵呼贾逵庙 |"""
    normalized_text_zh: str = """"""
    subject: str = "2 圣贤类诸兆"
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
        l1_anchor="mlxj_v1.0.0_2_圣贤类诸兆_001_L1",
    )
    version: str = "1.0.0"
