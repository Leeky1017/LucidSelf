"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.823576
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
    semantic_id="mlxj_v1.0.0_3_牛马类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 3牛马类诸兆(SemanticEntry):
    """
    #### 牛类汇总

**吉类**：
- 群牛下山吉：晚景荣华
- 牛涉大水吉：险中免难
- 骑牛吉：孝名高

**贞吉否凶类**：
- 牛作人言：幽冥假借，当以所言推占

**凶类**：
- 牛生二...
    """
    
    original_text: str = """#### 牛类汇总

**吉类**：
- 群牛下山吉：晚景荣华
- 牛涉大水吉：险中免难
- 骑牛吉：孝名高

**贞吉否凶类**：
- 牛作人言：幽冥假借，当以所言推占

**凶类**：
- 牛生二尾凶：失字（周缮典故）
- 牛止于穴下凶：牢狱之事
- 牛入寝室：有可丑者

#### 马类汇总

**大吉类**：
- 四马六马同驾吉：大贵
- 乘马升天：大贵

**吉类**：
- 马云中驰骋贞吉：出往愆期
- 乘马渡水：险难中得吉
- 驹吉：少阳之象

**凶类**：
- 马无蹄凶：立身无四正
- 乘马入山凶：崎岖行路难
- 马舞舍中凶：火起之兆

#### 典故

- 三马同槽：曹操梦之，恶司马懿
- 洗马：湿白米（威远军梅伯成典故）
- 董丰梦乘马南渡：坎离变化，得破冯昌杀妻案"""
    normalized_text_zh: str = """"""
    subject: str = "3 牛马类诸兆"
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
        l1_anchor="mlxj_v1.0.0_3_牛马类诸兆_001_L1",
    )
    version: str = "1.0.0"
