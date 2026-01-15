"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.739860
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
    semantic_id="zw_v1.0.0_批贵命_天梁庙午化禄格_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 批贵命天梁庙午化禄格(SemanticEntry):
    """
    - 分字分词释义：

  - **天梁庙午**：天梁星在午宫入庙守命，清高尊贵的基础配置。
  - **化禄**：四化之一，天梁化禄则清高贵莫当。
  - **左右夹局**：左辅右彼夹命宫，增强辅佐与...
    """
    
    original_text: str = """- 分字分词释义：

  - **天梁庙午**：天梁星在午宫入庙守命，清高尊贵的基础配置。
  - **化禄**：四化之一，天梁化禄则清高贵莫当。
  - **左右夹局**：左辅右彼夹命宫，增强辅佐与贵人力量。
  - **化科化权交加拱**：化科与化权星从三方交加拱照命宫，主定拜皇恩入帝乡。
  - **步蟾折桂**：科举登第的比喻，蟾宫指月、折桂指高中。
  - **广施善政牧斯民**：官居县令后广施善政，清官理想的实现。
  - **古稀唱阳关**：晚年七十岁迀无求的人生归宿，阳关为送别曲。

- **原文（source_text）**：  
  命旺身强格理良，三方四正吉星彰，天梁庙午守命局，化禄清高贵莫当。天寿旺台辅强，左右夹局喜非常。化科化权交加拱，定拜皇恩入帝乡。百岁双亲膺紫诰，二宫逢陷雁孤单。贞临三位，配淑贤良。子星得地，克绍书香。且论目今行某限，某生不喜见擎羊。一交某限吉星聚，游泮还期帮补粮。当此步蟾而折桂，鹿鸣宴上喜洋洋。蓝袍脱换青袍着，闾里争先睹道傍。灿灿奎娄联碧汉，录录丝竹奏弦楼。再入某限科禄地，春兰三战夺魁名。官居县令承恩宠，广施善政牧斯民。男儿大志从斯展，到此英名正烈轰。某限也应防一厄，梧岗风木慎忧刑。幸得尚有祥星集，蟾从触后展光明。某限官乡名显赫，重擢拔擢耀神京。于公大厦容车马，谢氏之兰庭下生。古稀一到春光逝，唱罢阳关别故人。

- **规范化释义（primary_lang_explained）**：  
  此为批断「天梁庙午·化禄格」的标准套语。天梁于午宫入庙守命，化禄则清高尊贵无比。命旺身强，三方四正吉星彰显，左右夹局，化科化权交加拱照，定拜皇恩入帝乡。套语从游泮（入学）、步蟾折桂（科举）、官居县令、广施善政，到古稀之年唱罢阳关，铺陈完整的清官仕途生涯。

- **完整对等诠释（secondary_lang_full）**：  
  This template interprets the "Tian Liang in Temple at Wu, Transforming into Lu" pattern. Tian Liang in temple position at Wu Palace guards Life; transforming into Lu brings supreme noble refinement. Life and Body both strong, triad shows auspicious stars, Left and Right flank, Ke and Quan converge—destined for imperial grace. The template traces from school entry through examination success to county magistracy with benevolent governance, ending at seventy singing farewell songs.

- **核心要点**：  
  1. 适用格局：天梁庙午守命，化禄清高。  
  2. 吉星配置：左右夹局，化科化权交加拱。  
  3. 清官特征：官居县令、广施善政牧斯民。"""
    normalized_text_zh: str = """"""
    subject: str = "批贵命·天梁庙午化禄格"
    factor_refs: list = ['star_tianliang_miaowu', 'sihua_hualu', 'pattern_zuoyou_jiaju', 'pattern_keqian_jiagong', 'symbol_buchan_zhegui', 'trait_shanzheng_mumin', 'source_ref', 'rel_vol7_07_001', 'star_tianliang_miaowu', 'rel_vol7_07_002', 'pattern_zuoyou_jiaju', 'rel_vol7_07_003', 'pattern_keqian_jiagong', 'rel_vol7_07_004', 'symbol_buchan_zhegui', 'evi_vol7_07_001', 'rule_tianliang_miaowu_hualu', 'evi_vol7_07_002', 'rule_zuoyou_kequan_baihuang', 'evi_vol7_07_003', 'trait_shanzheng_mumin', 'rule_shanzheng_mumin', 'concept_refined_noble', 'concept_benevolent_governance', 'concept_longevity_retirement']
    
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
        l1_anchor="zw_v1.0.0_批贵命_天梁庙午化禄格_001_L1",
    )
    version: str = "1.0.0"
