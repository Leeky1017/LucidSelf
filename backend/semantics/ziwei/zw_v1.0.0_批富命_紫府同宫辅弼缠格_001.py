"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.739879
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
    semantic_id="zw_v1.0.0_批富命_紫府同宫辅弼缠格_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 批富命紫府同宫辅弼缠格(SemanticEntry):
    """
    - 分字分词释义：

  - **紫府同宫**：紫微与天府同守一宫，帝星与财库合一的富贵基础。
  - **辅彼缠绑**：左辅右彼缠绕命宫，增强辅佐与贵人力量。
  - **金星司财库**：金性星曜守...
    """
    
    original_text: str = """- 分字分词释义：

  - **紫府同宫**：紫微与天府同守一宫，帝星与财库合一的富贵基础。
  - **辅彼缠绑**：左辅右彼缠绕命宫，增强辅佐与贵人力量。
  - **金星司财库**：金性星曜守财宫，主早富如春申君。
  - **名利自然全**：虽无官星吉曜，名誉与利益自然双全。
  - **田畔添田**：财富不断积累，田产越来越多的富商意象。
  - **楼竖碍月**：高楼林立、产业连云的巨富意象。
  - **春申君**：战国四公子之一，富可敌国的典故。

- **原文（source_text）**：  
  紫府同宫旺，喜得辅弼缠。才官无吉曜，名利自然全。当生不合局格理，难将贵宿作虚言。三方又见擎陀混，应别青云足下生。妙得金星司财库，期君早富并春申。命主临财匕巨万，尊星守命福盈余。纵逢克化何为害，君子小人泾渭明。太阳星陷父先逝，太阴光照母年延。棠棣花枝坠，恶杀在其垣。贪狼居妻佐，硬配没刑煎。儿宫北斗无南斗，彩莲生见后，麒麟试论千。今限某星，此星恶虐要调停。落花不是无春色，只为春光转换频。某岁又交某星限，某星得地主昌荣更妙，喜色重重吉，明珠常捧掌中珍。向阳花木春无限，得水鱼龙气象新。四九年临某限里，车行蜀道阻其轮。交来某限星庙晤，雨过江山一昼屏。东邻告借纷然至，西空偿钱不住停。某年某限行吉得，人安物泰喜洋盈，田畔添田屋畔屋，楼竖碍月业连云。某年之内某月里，八珍汤散服频频。尚幸大限无杀忌，还夸老景愈安宁。老梅冒雪香犹在，伫看枝兰绕膝荣。某年之内春已艾，子规啼血恨长城。

- **规范化释义（primary_lang_explained）**：  
  此为批断「紫府同宫·辅弼缠」富命格局的标准套语。紫微天府同宫且得辅弼缠绑，虽无官星吉曜，名利自然双全。关键在于「金星司财库」——金星守财宫则早富如春申君。套语详论财运起伏：田畔添田、楼竖碍月，呈现富商巨贾的财富积累；同时也有六亲宫位的吉凶论述。

- **完整对等诠释（secondary_lang_full）**：  
  This template interprets the "Zi Wei‑Tian Fu Co‑located, Fu Bi Encircling" wealth fate pattern. Zi Wei and Tian Fu share a palace with Zuo Fu You Bi attending; though lacking Career star auspice, fame and profit come naturally. Key: "Metal Star governs the Treasury"—Metal in Wealth Palace brings early riches like Lord Chunshen. The template details wealth fluctuations: fields added to fields, towers blocking the moon—depicting merchant accumulation.

- **核心要点**：  
  1. 适用格局：紫府同宫，辅弼缠绑，金星司财库。  
  2. 富命特征：名利自然全，田畔添田楼竖碍月。  
  3. 六亲特征：太阳陷父先逝，太阴光照母年延。"""
    normalized_text_zh: str = """"""
    subject: str = "批富命·紫府同宫辅弼缠格"
    factor_refs: list = ['pattern_zifu_tonggong', 'pattern_fubi_chanbang', 'pattern_jinxing_sicaiku', 'symbol_tianpan_tiantian', 'symbol_loushu_aiyue', 'allusion_chunshenjun', 'source_ref', 'rel_vol7_08_001', 'pattern_zifu_tonggong', 'rel_vol7_08_002', 'pattern_jinxing_sicaiku', 'rel_vol7_08_003', 'result_zifu_fuming', 'evi_vol7_08_001', 'rule_zifu_fubi_fuming', 'evi_vol7_08_002', 'rule_jinxing_caiku_zaofu', 'evi_vol7_08_003', 'rule_tianpan_loushu_jufu', 'concept_imperial_treasury', 'concept_early_wealth', 'concept_merchant_empire']
    
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
        l1_anchor="zw_v1.0.0_批富命_紫府同宫辅弼缠格_001_L1",
    )
    version: str = "1.0.0"
