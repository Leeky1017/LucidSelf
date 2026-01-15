"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157357
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
    semantic_id="smth_v1.0.0_六乙日己卯时断_日禄归时与偏财临身_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六乙日己卯时断日禄归时与偏财临身(SemanticEntry):
    """
    - 原文（source_text）：

  六乙日己卯时断.

  （以下六乙日所忌月分与上同，时亦并论。）六乙日生逢己卯，时居日禄财临好；旺通木气贵无疑，酉土辛重亦可恼.乙日己卯时，禄入庙堂.乙木逢...
    """
    
    original_text: str = """- 原文（source_text）：

  六乙日己卯时断.

  （以下六乙日所忌月分与上同，时亦并论。）六乙日生逢己卯，时居日禄财临好；旺通木气贵无疑，酉土辛重亦可恼.乙日己卯时，禄入庙堂.乙木逢卯建禄，为人秀丽.通木火者，贵.见庚辛，为伤禄破命，患目疾.若生巳酉丑月，平常衣禄.辰戌丑未，吉.申月亦吉.

  乙丑日己卯时，高.中年大福.春生，身太旺，孤.夏贫.秋有疾.冬温厚.柱不见辛金，吉.若辰戌丑未月，金紫贵.

  乙卯日己卯时高，春生旺，为僧道，富足.夏平常.不见辛金，吉.秋带疾.冬温厚.卯丑年月，显达高寿.

  乙巳日己卯时，春孤贫；夏平；秋带疾；冬贵.午辰年月，地支一路相连，尤吉.

  乙未日己卯时，年月不见庚辛金，贵.秋生，看地厚薄.如生壬戌年月，三四品贵.

  乙酉日己卯时秀，初年破祖，中主发财.未年，孤刑.

  乙亥日己卯时，生寅巳月，不见庚辛，日禄归时格，显达清贵.纯卯年月，高僧羽士.戌，特达聪明，有财禄.

  日禄居时格不同，食神则马要相逢；伤官印运皆为吉，官不逢兮禄自丰.乙日时临己卯，偏财时禄归迎.辛金酉字不相刑，虎榜定标名姓.父母六亲难靠，雁行各自飞腾.文章光耀有才能，无破无冲贵命.

- 分字分词释义：

  - **日禄归时**：日主在时支得禄，比喻自身能量与时机高度契合.
  - **偏财时禄**：己土为偏财，临于时位，象征中晚年财运与资源机会.
  - **高僧羽士**：指出家、修道或高度精神化的生活方式.

- 规范化释义（primary_lang_explained）：

  本节讲「六乙日，己卯时」：

  - 乙木在卯得禄，形象为气质秀丽、自我实现感较强；
  - 若木火通达而不见庚辛，则多主清贵、文章与名声；
  - 部分组合则指向僧道、修行、离群索居等路径，中晚年偏财、禄位渐显.

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Yi Days with Ji-Mao Hour":

  - Yi Wood at Mao obtains its fortune, presenting an image of refined elegance and strong self-actualization.
  - When Wood-Fire flows through without Geng-Xin appearing, this typically indicates pure nobility, literary achievement, and reputation.
  - Some combinations point toward monastic or spiritual paths; in middle and later years, indirect wealth and fortune positions gradually emerge.

- 核心要点：

  - 这是一个**自我实现与财禄兼具、但亲缘支持有限**的结构；
  - 庚辛金重则易损禄伤身，需警惕过度竞争与眼疾之象；
  - 对精神性、修行、学术等方向，有明显的适配性.

- 详细解说：

  1. **日禄与人生重心**  
     - 日禄归时，多意味着人生重心偏向中后期的自我发挥；  
     - 早年不必急于求成，更重视积累与打基础.

  2. **修行与事业的双轨**  
     - 原文同时提到僧道、高僧羽士与金紫贵官，说明此格既可俗世成就，也可精神修行；  
     - 关键在于当事人如何选择与调和这两条路径.

  3. **亲缘与独立**  
     - 「父母六亲难靠」常见于乙日格局，提示情感上要学会自我支撑；  
     - 现代可通过建立志同道合的社群代偿部分家族支持的不足.

- 校勘与字词辨析：

  - 「日禄归时格」在本稿中视为自我能量与现实机会重叠的一种象征结构.
  - 「高僧羽士」不限定具体宗派，而泛指高度重视精神性的生活方式.
  - **English**：
    - Life stage predictions explained as probability indicators; metaphorical descriptions of fortune and misfortune contextualized; technical shensha terms demystified.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_061]` `[trigger: 日禄归时]` `[factor_trigger: rilu_guishi AND cai_lin_hao]` `[role: 主干]` 六乙日生逢己卯，时居日禄财临好。 → 《三命通会》卷八#六乙日己卯时
  - `[ns_smth_08_062]` `[trigger: 旺通木气]` `[factor_trigger: wang_tong_muqi AND gui_wu_yi]` `[role: 主干依赖]` 旺通木气贵无疑，酉土辛重亦可恼。 → 《三命通会》卷八#六乙日己卯时
  - `[ns_smth_08_063]` `[trigger: 无冲无破]` `[factor_trigger: wuchong_wupo AND guiming]` `[role: 条件分支]` 无破无冲贵命。 → 《三命通会》卷八#六乙日己卯时
  - `[ns_smth_08_064]` `[trigger: 虎榜标名]` `[factor_trigger: hubang_biaoming AND xin_bu_xingke]` `[role: 总结]` 辛金酉字不相刑，虎榜定标名姓。 → 《三命通会》卷八#六乙日己卯时"""
    normalized_text_zh: str = """"""
    subject: str = "六乙日己卯时断：日禄归时与偏财临身"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_yi', 'bazi_semantic', 'bazi_state_factor_345', 'bazi_semantic', 'bazi_relation_piancai', 'bazi_semantic', 'bazi_state_factor_156', 'bazi_semantic', 'hour_branch_mao', 'bazi_semantic', 'bazi_condition_geng_xin', 'bazi_semantic', 'source_ref', 'rel_smth_08_046', 'rilu_guishi', 'rel_smth_08_047', 'gaoseng_yushi', 'rel_smth_08_048', 'bujian_gengxin', 'evi_smth_08_046', 'rilu_guishi', 'rule_rilu_gui', 'evi_smth_08_047', 'gaoseng_yushi', 'rule_gaoseng', 'evi_smth_08_048', 'bujian_gengxin', 'rule_bujian', 'map_smth_08_031', 'map_smth_08_032']
    
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_六乙日己卯时断_日禄归时与偏财临身_001_L1",
    )
    version: str = "1.0.0"
