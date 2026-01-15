"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157347
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
    semantic_id="smth_v1.0.0_六乙日戊寅时断_败财背禄与成败参半_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六乙日戊寅时断败财背禄与成败参半(SemanticEntry):
    """
    - 原文（source_text）：

  六乙日戊寅时断。

  六乙日生时戊寅，败财背禄实伤身；有心无力多成败，止是平常衣禄人。六乙日戊寅时，败财背禄。乙用庚为官，寅中有丙，伤官背禄；用戊己为财，...
    """
    
    original_text: str = """- 原文（source_text）：

  六乙日戊寅时断。

  六乙日生时戊寅，败财背禄实伤身；有心无力多成败，止是平常衣禄人。六乙日戊寅时，败财背禄。乙用庚为官，寅中有丙，伤官背禄；用戊己为财，寅中甲旺，财败。为人作事，成败平常。通土气者，吉。

  乙丑日戊寅时高。生子年戌月者，富贵。辰戌，行木火运，威权.

  乙卯日戊寅时，刑中发福。秋生，贵.酉年遇辰戌丑未月，富.卯月建禄，午月印生，透官印，俱吉.

  乙巳日戊寅时，孤克，平常.若年月申庚，正官；丑辛，七煞，俱贵.辰月，北方运，吉.

  乙未日戊寅时，春生，有寿.秋贵显；夏平常；冬反复.辰戌且未，俱吉.岁运同.

  乙酉日戊寅时，春生富；夏平；秋贵、寿促；冬吉.

  乙亥日戊寅时，春吉；夏劳力；秋冬贵.子丑年月，贵至三品，有起有落，寿永.

  乙日寅时仔细推，为人招是又招非；运衰更遇空刑克，劳力劳心无定期.乙日戊寅时遇，就是暗损伤财.伤官背禄，柱中排.富贵妻儿刑害.运旺财官发福，运行比煞兴灾.六亲骨肉少和谐，自立自成自在.

- 分字分词释义：

  - **败财背禄**：财星受伤、官禄被背离，比喻赚钱难守、职位难稳.
  - **招是又招非**：易招惹是非、人情纠葛，象征互动复杂.
  - **刑中发福**：在刑冲、压力中反而得到突破机会.

- 规范化释义（primary_lang_explained）：

  本节讲「六乙日，戊寅时」：

  - 以败财、背禄为基调，表示在金钱与职位上多有起落与折损，有心无力之感较重；
  - 然而在特定年月与行运下，反而能在刑冲、竞争中发福，出现威权或三品之贵；
  - 亲缘、夫妻、子女关系上，多见刑克与摩擦，需要更多耐心经营.

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Yi Days with Wu-Yin Hour":

  - The fundamental tone is defeated wealth and abandoned fortune, indicating frequent rises and falls in money and position, with a strong sense of willing but unable.
  - However, under specific year-months and fortune cycles, one may instead prosper through punishment and competition, achieving authority or third-rank nobility.
  - In relationships with relatives, spouse, and children, punishment and friction are common, requiring more patience to manage.

- 核心要点：

  - 命局的主题是**压力之中求突破**，不能指望一路顺风；
  - 若能善用土气、官煞的正向一面，仍可在事业上站稳一席之地；
  - 在关系与财务上要特别小心「高风险博弈」，避免雪上加霜.

- 详细解说：

  1. **成败参半的节奏**  
     - 原文强调「成败平常」「有起有落」，说明此格难以一劳永逸；  
     - 可将每次失败视为调整策略的契机，而非终点.

  2. **刑克与自立**  
     - 多次提到刑害六亲，预示亲缘支持有限，更需自立自强；  
     - 现代语境下，可理解为：不必过度指望背景与人情，专注个人能力建设.

  3. **用神与行运**  
     - 通土气、行木火运、多见官印之时，往往是发挥的窗口；  
     - 在比劫旺、煞重而无制之运，则适合收缩、养精蓄锐，少做大博弈.

- 校勘与字词辨析：

  - 「招是又招非」等语，为性格与处境的写照，不指具体案件.
  - 「金刃」「恶死」等词，在本稿统一视为对高风险情境的形象化表达.
  - **English**：
    - Life stage predictions explained as probability indicators; metaphorical descriptions of fortune and misfortune contextualized; technical shensha terms demystified.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_057]` `[trigger: 败财背禄]` `[factor_trigger: baicai_beilu AND shi_shangshen]` `[role: 主干]` 六乙日生时戊寅，败财背禄实伤身。 → 《三命通会》卷八#六乙日戊寅时
  - `[ns_smth_08_058]` `[trigger: 有心无力]` `[factor_trigger: youxin_wuli AND duo_chengbai]` `[role: 主干依赖]` 有心无力多成败，止是平常衣禄人。 → 《三命通会》卷八#六乙日戊寅时
  - `[ns_smth_08_059]` `[trigger: 刑中发福]` `[factor_trigger: xingzhong_fafu AND qiu_sheng_gui]` `[role: 条件分支]` 刑中发福。秋生，贵。酉年遇辰戌丑未月，富。 → 《三命通会》卷八#六乙日戊寅时
  - `[ns_smth_08_060]` `[trigger: 自立自成]` `[factor_trigger: liuqin_buhe AND zili_zicheng]` `[role: 总结]` 六亲骨肉少和谐，自立自成自在。 → 《三命通会》卷八#六乙日戊寅时"""
    normalized_text_zh: str = """"""
    subject: str = "六乙日戊寅时断：败财背禄与成败参半"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_yi', 'bazi_semantic', 'bazi_state_factor_153', 'bazi_semantic', 'bazi_relation_factor_72', 'bazi_semantic', 'bazi_state_factor_154', 'bazi_semantic', 'hour_branch_yin', 'bazi_semantic', 'bazi_condition_earth', 'bazi_semantic', 'source_ref', 'rel_smth_08_043', 'baicai_beilu', 'rel_smth_08_044', 'xingzhong_fafu', 'rel_smth_08_045', 'tongtuqi', 'evi_smth_08_043', 'baicai_beilu', 'rule_baicai', 'evi_smth_08_044', 'xingzhong_fafu', 'rule_xingzhong', 'evi_smth_08_045', 'tongtuqi', 'rule_tongtu', 'map_smth_08_029', 'map_smth_08_030']
    
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
        l1_anchor="smth_v1.0.0_六乙日戊寅时断_败财背禄与成败参半_001_L1",
    )
    version: str = "1.0.0"
