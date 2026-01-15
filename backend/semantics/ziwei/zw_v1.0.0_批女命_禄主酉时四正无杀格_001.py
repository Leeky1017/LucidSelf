"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.740005
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
    semantic_id="zw_v1.0.0_批女命_禄主酉时四正无杀格_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 批女命禄主酉时四正无杀格(SemanticEntry):
    """
    - 分字分词释义：

  - **禄主甲酉时**：禄主为甲木，生于酉时，贵妇命的核心时辰配置。
  - **四正无杀劫空**：四正宫位无七杀、劫空等凶星，主贵无破。
  - **巳酉金水白局**：巳酉...
    """
    
    original_text: str = """- 分字分词释义：

  - **禄主甲酉时**：禄主为甲木，生于酉时，贵妇命的核心时辰配置。
  - **四正无杀劫空**：四正宫位无七杀、劫空等凶星，主贵无破。
  - **巳酉金水白局**：巳酉宫位形成金水白局，女命贵格配置。
  - **两国之封**：极贵的误命封号，主嫁入王侯之家。
  - **桃夭**：《诗经》婚嫁典故，二八上下咏桃夭。
  - **内助持家**：贤内助主持家务，闻门内助光。
  - **配夫冠乌纱**：嫁入官嬦之家，夫君必作凤凰池上客。

- **原文（source_text）**：  
  意贞端正。禄主甲生时逢酉刻，四正无杀劫大空，两国之封端可得，对宫吉曜聚成团。巳酉邀成金水白，福德宫中紫微缠玉石，沙金谁解测。配夫端的冠乌纱，必作凤凰池上客。育儿双双千里驹，骐骥腾轩非在百。淑人性格禀风霜，端正仪容倾国色。命坐寅上酉时生命，主太阳无陷慝，列星部位尽辉光，珠翠盈头光绚赫。十一二岁在劫乡，青苗还忌生蟊贼。二八上下咏桃夭，其余养好花异特。某限又到劫空宫，座上雍凡头春拍塞。五六之内雨消消，园中粉蝶慵翻拍。四八星限又加祥，闻门内助光。家宅熊罴频飞入，帐中荣捧掌珠承祖脉。大井之年六九傍，杯中蛇影心疑惑。巳外滔滔乐太平，夫荣子贵乌台柏。五福悠全孰典傅，寿赠令人称啧啧。八卦过来七十将，马鬣高风藏素魂。

- **规范化释义（primary_lang_explained）**：  
  此为批断贵妇命格的标准套语。核心条件：禄主甲生于酉时，四正无杀劫空亡，对宫吉曜聚会，巳酉成金水白局，福德宫紫微缠绑。此格主「两国之封」（极贵诰命）、「配夫冠乌纱」（嫁官宦）、「育儿千里驹」（子女出众）。套语从少年劫乡、二八桃夭（婚嫁）、内助持家、夫荣子贵，到七十寿终，铺陈完整的贵妇人生。

- **完整对等诠释（secondary_lang_full）**：  
  This template interprets the noble lady fate pattern. Core conditions: Lu Master born under Jia at You hour, four cardinal positions free of malefics and voids, opposite palace gathering auspicious stars, Si‑You forming Metal‑Water white configuration, Fortune Palace with Zi Wei. This pattern indicates "enfeoffment of two kingdoms" (supreme noble title), "husband wearing official cap" (marrying into officialdom), "children like thousand‑li horses" (outstanding offspring). The template traces from youth tribulations through marriage, domestic management, husband's glory and children's success, to death at seventy.

- **核心要点**：  
  1. 适用格局：禄主甲酉时生，四正无杀劫空，巳酉金水白局。  
  2. 贵妇特征：两国之封、配夫冠乌纱、夫荣子贵。  
  3. 人生周期：少年劫乡、二八桃夭、内助持家、寿至七十。"""
    normalized_text_zh: str = """"""
    subject: str = "批女命·禄主酉时四正无杀格"
    factor_refs: list = ['time_luzhu_jia_youshi', 'pattern_sizheng_wusha', 'pattern_siyou_jinshuibai', 'symbol_liangguozhifeng', 'symbol_taoyao', 'trait_neizhu_chijia', 'source_ref', 'rel_vol7_15_001', 'time_luzhu_jia_youshi', 'rel_vol7_15_002', 'pattern_siyou_jinshuibai', 'rel_vol7_15_003', 'symbol_taoyao', 'rel_vol7_15_004', 'trait_neizhu_chijia', 'evi_vol7_15_001', 'rule_luzhu_youshi_guifu', 'evi_vol7_15_002', 'pattern_siyou_jinshuibai', 'rule_siyou_jinshuibai_gui', 'evi_vol7_15_003', 'result_guifu_ming', 'rule_furong_zigui', 'concept_noble_lady', 'concept_peach_marriage', 'concept_inner_helper']
    
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
        l1_anchor="zw_v1.0.0_批女命_禄主酉时四正无杀格_001_L1",
    )
    version: str = "1.0.0"
