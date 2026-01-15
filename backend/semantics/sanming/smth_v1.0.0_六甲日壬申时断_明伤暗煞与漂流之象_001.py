"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157277
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
    semantic_id="smth_v1.0.0_六甲日壬申时断_明伤暗煞与漂流之象_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六甲日壬申时断明伤暗煞与漂流之象(SemanticEntry):
    """
    - 原文（source_text）：

  六甲生时遇壬申，明伤暗鬼坐其身；柱无丙戊秋冬旺，坎坷飘流无定人.甲日壬申时，甲木绝在申，申上壬水长生，庚金建禄，明伤暗鬼，甲旺化鬼为官，犹不免凶暴.若生秋庚...
    """
    
    original_text: str = """- 原文（source_text）：

  六甲生时遇壬申，明伤暗鬼坐其身；柱无丙戊秋冬旺，坎坷飘流无定人.甲日壬申时，甲木绝在申，申上壬水长生，庚金建禄，明伤暗鬼，甲旺化鬼为官，犹不免凶暴.若生秋庚旺，生冬壬旺，柱无丙戊制伏，漂流之象.若巳午月，大吉；强横透庚，作煞论，运行北方，贵.

  甲子日壬申时，申子辰、亥月，水泛木漂，移根换叶，玉堂金马之贵.水土运，凶.

  甲寅日壬申时，旺中有失.辰戌丑未月，勾陈得位；寅午戌月，偏官有制；秋月，行东南运，俱贵.

  甲辰日壬申时，寅辰年月，文章显贵；透丙戊尤美.

  甲午日壬申时，申子辰月，改姓更宗，敦厚之命；午月贵.

  甲申日壬申时，寅月，身煞两停；卯月，以刃合煞，俱贵.子辰年月，以煞化印；巳午火月，七煞有制，俱吉.最怕煞旺身弱，大凶.

  甲戌日壬申时，辰戌丑未月，衣锦有成；亥月学堂；寅月建禄，俱贵.午酉月，寿促，不然贫贱.

  甲日时逢喜遇申，偏官偏印怕刑冲；欲求名利终难定，有救须教运气通.甲日时逢壬申，倒食暗鬼相侵.生逢身旺主昌荣，身弱性情不定.雁侣六亲少力，谋为自立自成.运行吉地显声名，运弱平常之命.

- 分字分词释义：

  - **明伤暗鬼**：表面有伤官，内里藏七煞，象征一体两面：才气与风险并存.
  - **水泛木漂 / 移根换叶**：木被水浮起，比喻人生迁徙频繁、根基多有更换.
  - **改姓更宗**：从象征意义看，可理解为家庭结构或身份归属发生较大变动.

- 规范化释义（primary_lang_explained）：

  本节谈「六甲日，壬申时」：

  - 甲木绝于申，申上壬水长生、庚金建禄，一方面有才学与机敏，一方面又有煞气潜伏，若缺少丙火、戊土制衡，易显「凶暴」与漂泊；
  - 得巳午等火月时，煞被制、印得生，反能化鬼为官，成为有权之贵；
  - 在不同甲日与月令下，有的主改姓易宗，有的主衣锦有成，有的则寿夭、贫贱，体现结构的高度两极性.

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Jia Days with Ren-Shen Hour":

  - Jia Wood is extinct at Shen; on Shen, Ren Water reaches long life while Geng Metal establishes its fortune—creating "visible Hurting Officer with hidden Ghost." Without Bing Fire and Wu Earth control, this shows "violence" and drifting tendencies.
  - When born in Si-Wu Fire months, the Ghost is controlled and Seal is generated, transforming Ghost into Official for authoritative nobility.
  - Across different Jia days and monthly pillars, some indicate changing surname and clan, others indicate accomplished splendor, still others indicate shortened lifespan or poverty—reflecting the structure's extreme polarity.

- 核心要点：

  - 这是一个**流动性很强**的格局：环境、人际、职业都可能多次变化；
  - 关键在于：是否有印星与火土制煞，决定其走向是贵显还是漂泊；
  - 身强者可凭才智与意志驾驭七煞，身弱者则易在关系与情绪上反复无常.

- 详细解说：

  1. **「漂流」的多重含义**  
     - 可以是地理上的迁移，也可以是职业与身份上的多次转换；  
     - 若能在变化中保持学习能力与伦理底线，反而塑造出独特的履历与宽广视野.

  2. **七煞结构的用与忌**  
     - 七煞配印、配食时，多主决断力、行动力与突破力；  
     - 七煞无制、身弱时，则可能表现为攻击性、人际冲突、不稳定情绪.

  3. **现代建议**  
     - 适合在需要应对复杂局面的领域工作，如风控、司法、管理等；  
     - 建议刻意经营稳定关系与长期项目，以抵消结构上的「漂流」倾向.

- 校勘与字词辨析：

  - 「坎坷飘流无定人」本稿理解为多变与折返，并不牢固预言具体漂泊地理位置.
  - 「改姓更宗」等语，统一视作家庭与身份结构变化的象征表达.
  - **English**：
    - Life stage predictions explained as probability indicators; metaphorical descriptions of fortune and misfortune contextualized; technical shensha terms demystified.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_033]` `[trigger: 明伤暗鬼]` `[factor_trigger: mingshang_angui AND zuo_qishen]` `[role: 主干]` 六甲生时遇壬申，明伤暗鬼坐其身。 → 《三命通会》卷八#六甲日壬申时
  - `[ns_smth_08_034]` `[trigger: 漂流之象]` `[factor_trigger: wu_bingwu AND qiudong_wang]` `[role: 主干依赖]` 柱无丙戊秋冬旺，坎坷飘流无定人。 → 《三命通会》卷八#六甲日壬申时
  - `[ns_smth_08_035]` `[trigger: 巳午火月]` `[factor_trigger: siwu_huoyue AND da_ji]` `[role: 条件分支]` 若巳午月，大吉；强横透庚，作煞论，运行北方，贵。 → 《三命通会》卷八#六甲日壬申时
  - `[ns_smth_08_036]` `[trigger: 自立自成]` `[factor_trigger: yanlu_shaoli AND zili_zicheng]` `[role: 总结]` 雁侣六亲少力，谋为自立自成。 → 《三命通会》卷八#六甲日壬申时"""
    normalized_text_zh: str = """"""
    subject: str = "六甲日壬申时断：明伤暗煞与漂流之象"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_jia', 'bazi_semantic', 'bazi_state_day_master_5', 'bazi_semantic', 'bazi_relation_factor_69', 'bazi_semantic', 'bazi_state_water_wood', 'bazi_semantic', 'hour_branch_shen', 'bazi_semantic', 'bazi_condition_bing_wu', 'bazi_semantic', 'source_ref', 'rel_smth_08_025', 'rizhu_juedi', 'rel_smth_08_026', 'shuifan_mupiao', 'rel_smth_08_027', 'bingwu_zhisha', 'evi_smth_08_025', 'rizhu_juedi', 'rule_juedi', 'evi_smth_08_026', 'shuifan_mupiao', 'rule_shuifan', 'evi_smth_08_027', 'bingwu_zhisha', 'rule_zhifu', 'map_smth_08_017', 'map_smth_08_018']
    
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
        l1_anchor="smth_v1.0.0_六甲日壬申时断_明伤暗煞与漂流之象_001_L1",
    )
    version: str = "1.0.0"
