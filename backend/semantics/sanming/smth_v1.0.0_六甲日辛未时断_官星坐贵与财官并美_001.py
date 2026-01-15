"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157263
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
    semantic_id="smth_v1.0.0_六甲日辛未时断_官星坐贵与财官并美_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六甲日辛未时断官星坐贵与财官并美(SemanticEntry):
    """
    - 原文（source_text）：

  六甲日辛未时断.

  六甲日生辛未时，官星坐贵最为奇；月逢金气须荣贵，财禄相停敢断之。甲日辛未时，时贵逢官，甲见辛为官，未有天乙贵；己为财，未中己土得气，...
    """
    
    original_text: str = """- 原文（source_text）：

  六甲日辛未时断.

  六甲日生辛未时，官星坐贵最为奇；月逢金气须荣贵，财禄相停敢断之。甲日辛未时，时贵逢官，甲见辛为官，未有天乙贵；己为财，未中己土得气，若通木气月，有寄托者富；通土气月者，富贵双全.

  甲子日辛未时，辰戌丑未及己酉月，土金地方，文贵显达.

  甲寅日辛未时，寅申月贵.纯酉丑年月，大贵.

  甲辰日辛未时，辰戌丑未月，富.巳酉丑子年月，贵.

  甲午日辛未时，春吉；夏凶；秋身弱难任官禄；冬贵.

  甲申日辛未时，春吉，夏辛苦，秋显达，冬根基别立贵.子丑月，大贵.

  甲戌日辛未时，先刑后贵.寅卯酉丑年月贵，子申年月，位至贵显.

  甲逢辛未是财官，平步青云路不难；不比退毛鸡化凤，得时飞上彩云路.甲日时逢辛未，财官守库相扶；贵人财禄是良图，初苦未终荣富.君子迁官进职，常人丰厚充腴；刑冲破害柱中无，定得青云之路.

- 分字分词释义：

  - **官星坐贵**：官星落在有贵人、天乙之地，比喻地位与平台较佳.
  - **财禄相停**：财星与禄位相互配合，暗指物质与职位兼备.
  - **先刑后贵**：早年在家庭或人际上有刑克、波折，之后逐渐转贵.

- 规范化释义（primary_lang_explained）：

  本节论「六甲日，辛未时」：

  - 未中己土为偏财又带天乙贵人，辛金为官星，形成财官并见、官坐贵地的结构；
  - 若月令通木气、土气，使身财官三者有承接，则多主富贵双全；
  - 不同甲日与月令，或偏于文贵、或偏于财厚、或早年有刑、后期方贵，但整体基调偏吉.

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Jia Days with Xin-Wei Hour":

  - Wei contains Ji Earth as Indirect Wealth plus Tianyi Noble, while Xin Metal serves as the Official star, forming a "Wealth-Official together with Official sitting on Noble" structure.
  - When monthly pillars channel Wood or Earth energy, allowing Day Master, Wealth, and Official to connect, this typically indicates both wealth and nobility.
  - Different Jia days and monthly pillars may lean toward literary nobility, substantial wealth, or early hardship followed by later nobility, but the overall tone is auspicious.

- 核心要点：

  - 这是一个典型的**财官两得**结构，关键在于日主能否承载；
  - 通木气则身有寄托，通土金则财官得地，对应不同的富贵方向；
  - 当「刑」与「劳」出现在早年时，可视作为后续成就打基础的过程.

- 详细解说：

  1. **财官并见的利与弊**  
     - 财多生官，易得资源与职位，也易被物质牵制；  
     - 若缺乏印绶生身，容易成为「为位所役」，压力感较重.

  2. **不同甲日的侧重**  
     - 甲子、甲寅多偏文贵与名声；甲辰偏财厚；甲申、甲戌则有「先刑后贵」「根基别立」等特点；  
     - 可理解为：同样的辛未时格，有人通过学问、有人通过实业、有人通过体制路线获得成就.

  3. **现代视角应用**  
     - 此类命局宜正途发展，重视专业能力与制度内晋升；  
     - 需注意平衡对财富的追求与身心承载，避免过度透支.

- 校勘与字词辨析：

  - 「天乙贵」按传统神煞理解，本稿仅作「环境与机缘较佳」的象征处理.
  - 「鸡化凤」一喻，用以形容阶层跃迁，并非预言具体身份变化.
  - **English**：
    - Life stage predictions explained as probability indicators; metaphorical descriptions of fortune and misfortune contextualized; technical shensha terms demystified.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_029]` `[trigger: 官星坐贵]` `[factor_trigger: guanxing_zuogui AND zui_wei_qi]` `[role: 主干]` 六甲日生辛未时，官星坐贵最为奇。 → 《三命通会》卷八#六甲日辛未时
  - `[ns_smth_08_030]` `[trigger: 财禄相停]` `[factor_trigger: cailu_xiangting AND gan_duanzhi]` `[role: 主干依赖]` 月逢金气须荣贵，财禄相停敢断之。 → 《三命通会》卷八#六甲日辛未时
  - `[ns_smth_08_031]` `[trigger: 通木通土]` `[factor_trigger: tongmuqi_fu OR tongtuqi_fugui]` `[role: 条件分支]` 若通木气月，有寄托者富；通土气月者，富贵双全。 → 《三命通会》卷八#六甲日辛未时
  - `[ns_smth_08_032]` `[trigger: 青云之路]` `[factor_trigger: qingyun_zhilu AND wu_xingchong]` `[role: 总结]` 刑冲破害柱中无，定得青云之路。 → 《三命通会》卷八#六甲日辛未时"""
    normalized_text_zh: str = """"""
    subject: str = "六甲日辛未时断：官星坐贵与财官并美"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_jia', 'bazi_semantic', 'bazi_state_factor_145', 'bazi_semantic', 'bazi_relation_factor_68', 'bazi_semantic', 'bazi_state_factor_146', 'bazi_semantic', 'hour_branch_wei', 'bazi_semantic', 'bazi_condition_wood_earth', 'bazi_semantic', 'source_ref', 'rel_smth_08_022', 'guanxing_zuogui', 'rel_smth_08_023', 'xianxing_hougui', 'rel_smth_08_024', 'tongmu_tongtu', 'evi_smth_08_022', 'guanxing_zuogui', 'rule_zuogui', 'evi_smth_08_023', 'xianxing_hougui', 'rule_xianxing', 'evi_smth_08_024', 'tongmu_tongtu', 'rule_tongqi', 'map_smth_08_015', 'map_smth_08_016']
    
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
        l1_anchor="smth_v1.0.0_六甲日辛未时断_官星坐贵与财官并美_001_L1",
    )
    version: str = "1.0.0"
