"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.831766
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
    semantic_id="mlxj_v1.0.0_2_雨象_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2雨象(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 大雨中考试吉：功名大利
- 在雨中饮食：锦衣玉食，君恩赐宴
- 大雨中庭水泛大吉：财利盈箱，万事丰殷
- 坐狱中见大雨吉：遇赦或遇良医
- 雨中乘舟车大吉：...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 大雨中考试吉：功名大利
- 在雨中饮食：锦衣玉食，君恩赐宴
- 大雨中庭水泛大吉：财利盈箱，万事丰殷
- 坐狱中见大雨吉：遇赦或遇良医
- 雨中乘舟车大吉：名利咸亨

**凶类**：
- 雨湿衣凶：病祸临身，忧愁多悔
- 大雨破墙屋凶：败国亡家之兆

**贞吉否凶类**：
- 雨中戴帽：加冠迁位大富贵，但求名时不得出头（王监书典故）
- 天雨忙奔欲寻躲：避难趋吉，未为不祥
- 张伞遮雨：必有私情佳偶事至

#### 典故素材

| 梦象 | 梦者 | 应验 | 出处 |
|------|------|------|------|
| 雨中戴帽 | 王监书 | 恩泽未沾渥，不得官 | 宋 |"""
    normalized_text_zh: str = """"""
    subject: str = "2 雨象"
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
        l1_anchor="mlxj_v1.0.0_2_雨象_001_L1",
    )
    version: str = "1.0.0"
