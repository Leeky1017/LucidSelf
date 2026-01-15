"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699941
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
    semantic_id="zw_v1.0.0_廪生之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 廪生之命(SemanticEntry):
    """
    - 分字分词释义：

  - **无正曜**：命宫缺少主星坐守，多主出身资源有限。
  - **府相朝垣**：天府天相在三方朝拱命宫，主吉星护持。
  - **廉禄拱冲**：廉贞与禄星形成拱冲格局，主...
    """
    
    original_text: str = """- 分字分词释义：

  - **无正曜**：命宫缺少主星坐守，多主出身资源有限。
  - **府相朝垣**：天府天相在三方朝拱命宫，主吉星护持。
  - **廉禄拱冲**：廉贞与禄星形成拱冲格局，主有才禄来源。
  - **福德宫吉集**：福德宫聚集多吉星，主精神资源丰厚。
  - **劫空冲命**：劫煎与空亡直接冲击命宫，主根基受损。
  - **文昌陷于天伤**：文昌星落在伤损之地，主学业或精神受创。
  - **阳男木三局**：廪生命盘的五行局数，木三局主生发学业。

- **原文（source_text）**：  
  廪生之命。阳男木三局。此命无正曜，多主庶毋，所生得府相朝垣，廉禄拱冲，福德宫吉集，故亦受朝廷作养，但寿终不得长，以劫空冲命，文昌陷于天伤故也。

- **规范化释义（primary_lang_explained）**：  
  廪生命为阳男木三局，「无正曜」说明命宫缺少主星加持，多主出身非嫡系或资源有限，但「得府相朝垣，廉禄拱冲，福德宫吉集」，表示仍有天府、天相等吉星在三方朝拱，廉贞与禄星拱冲，福德宫聚集多吉星——即便出身不高，也能凭资质与努力获得国家的「廪生」待遇，受朝廷供养读书。  
  然而命局亦埋下寿命隐忧：「以劫空冲命，文昌陷于天伤」，说明劫空冲击命宫，而文昌星又落陷于天伤之地，容易在身体、精神或学业进程上遭遇严重打击，使得寿终不得长。此命例体现「能得培养但难以长久享用」的结构：人被制度看见并资助，却在寿命或健康上留有缺口。

- **完整对等诠释（secondary_lang_full）**：  
  The "stipended student" is a Yang Wood native with no principal star in the Life palace, often read as lower birth or weaker innate backing. Yet Fu and Xiang stars form a court around the relevant palaces; Lian Zhen and Lu interact; and the Fortune house gathers benefics. These indicate state support and recognition—he becomes a "linseng," a student whose study is funded by the court.  
  Still, Jie and Kong directly attack the Life palace, and Wen Chang falls into a "Tian Shang" injury position. This combination points to significant vulnerability in health, mental resilience or the continuity of study: his life is not long. The chart exemplifies a destiny in which one receives institutional nourishment and scholarly identity but cannot enjoy a full lifespan.

- **核心要点**：  
  1. 命宫无正曜却得府相朝垣、廉禄拱冲，象征出身平常却获体制供养读书。  
  2. 劫空冲命、文昌陷天伤，预示身心或学业链条上存在严重断点。  
  3. 命例呈现「能被培养、难以久享」——有身份、有供养，却寿命偏短。"""
    normalized_text_zh: str = """"""
    subject: str = "廪生之命"
    factor_refs: list = ['quality_wu_zhengyao', 'pattern_fuxiang_chaoyuan', 'pattern_lianlu_gongchong', 'palace_fude_jiji', 'malefic_jiekong_chongming', 'malefic_wenchang_tianshang']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_廪生之命_001_L1",
    )
    version: str = "1.0.0"
