"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157499
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
    semantic_id="smth_v1.0.0_六丙日癸巳时断_日禄归时与正官坐贵_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六丙日癸巳时断日禄归时与正官坐贵(SemanticEntry):
    """
    - 原文（source_text）：

  六丙日癸巳时断。

  六丙日生时癸巳，日禄归时又遇官；不见巳寅壬癸月，功名唾于得何难。丙日癸巳时，日禄归时，丙火巳上见癸为正官，坐贵。柱无壬己并寅亥，冲刑...
    """
    
    original_text: str = """- 原文（source_text）：

  六丙日癸巳时断。

  六丙日生时癸巳，日禄归时又遇官；不见巳寅壬癸月，功名唾于得何难。丙日癸巳时，日禄归时，丙火巳上见癸为正官，坐贵。柱无壬己并寅亥，冲刑者贵，有则否。官通水旺，丙通木旺，无有不贵。

  丙子日癸巳时，丙禄在巳，癸禄在巳，互换禄马，岁月无壬巳寅亥冲破，近侍风宪，位至公侯。

  丙寅日癸巳时，春月，干支无水，文进绣衣，荣妻荫子。卯戌申酉年月，二三品贵。

  丙辰日癸巳时，不利祖宗。酉戌寅丑年月，魁罡格，通身旺，贵。

  丙午日癸巳时，丑辰月，杂气财官，贵显。寅月，丙长生；巳月，丙建禄，天干透财印者大贵，宜戒酒。子，官旺；酉，财旺，俱吉。

  丙申日癸巳时，身坐偏官、偏财，不贵即富。

  丙戌日癸巳时，卯戌丑未月，贵，不永。寅亥年月，风宪，嫌冲刑，宜戒酒。

  丙日时逢癸巳真，号为正贵喜相亲；柱中年月无冲破，必是荣华富贵人。丙日时逢癸巳，正官禄马稀奇。算来妻子早难为，官禄冲克最忌。君子文名出众，常人财禄有余。黄金白玉出沉泥，运至时来偏聚。

- 分字分词释义：

  - **日禄归时**：日主之禄位落在时支，如丙火禄在巳，时支为巳。
  - **正官坐贵**：癸水正官坐于巳，巳为丙火贵人位。
  - **互换禄马**：丙禄在巳、癸禄在巳，形成禄马互换的结构。
  - **功名唾于得何难**：功名如唾手可得，比喻容易获取。

- 规范化释义（primary_lang_explained）：

  本节讲「六丙日，癸巳时」：

  - 丙火日禄在巳，时支为巳，形成「日禄归时」格；癸水正官坐于巳，巳为丙火贵人位，官星坐贵；
  - 若柱中无壬己并寅亥冲刑，则功名可得，位至公侯；
  - 歌诀强调：正官禄马稀奇，无冲破者必是荣华富贵人。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Bing Days with Gui-Si Hour":

  - Bing Fire's fortune is at Si, hour-branch is Si, forming "Day Fortune Returns to Hour" pattern; Gui Water Direct Official sits at Si, which is Bing Fire's noble position—official star seated on noble.
  - If the chart lacks Ren-Ji combined with Yin-Hai clash-punishment, achievement comes easily, reaching duke-level positions.
  - The verse emphasizes: direct official with fortune-horse is extraordinary; without clash or break, this is certainly a person of glory and riches.

- 核心要点：

  - 本格以「日禄归时」为核心，结构优良。
  - 正官坐贵，形成官贵双美的结构。
  - 最忌壬己并见、寅亥冲刑。

- 详细解说：

  1. **日禄归时的优势**  
     - 丙火禄在巳，时支为巳，禄位归时；  
     - 主晚年福禄丰厚，子孙有靠。

  2. **正官坐贵的加持**  
     - 癸水正官坐于巳，巳为丙火天乙贵人；  
     - 官星与贵人同位，主仕途显达、贵人扶持。

  3. **冲刑的忌讳**  
     - 寅亥冲巳，破坏禄位；壬己并见，杂乱格局；  
     - 需要柱中清纯，方能发挥格局优势。

- 校勘与字词辨析：

  - 「黄金白玉出沉泥」比喻出身平凡但能显贵。
  - 「宜戒酒」提示此格者可能有酗酒倾向，需要节制。
  - **English**：
    - May have drinking tendencies; moderation required.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_117]` `[trigger: 日禄归时]` `[factor_trigger: rilu_guishi AND you_yu_guan]` `[role: 主干]` 六丙日生时癸巳，日禄归时又遇官。 → 《三命通会》卷八#六丙日癸巳时
  - `[ns_smth_08_118]` `[trigger: 正官坐贵]` `[factor_trigger: zhengguan_zuogui AND gongming_tuo]` `[role: 主干依赖]` 不见巳寅壬癸月，功名唾于得何难。 → 《三命通会》卷八#六丙日癸巳时
  - `[ns_smth_08_119]` `[trigger: 互换禄马]` `[factor_trigger: huhuan_luma AND wei_zhi_gonghou]` `[role: 条件分支]` 丙禄在巳，癸禄在巳，互换禄马....位至公侯。 → 《三命通会》卷八#六丙日癸巳时
  - `[ns_smth_08_120]` `[trigger: 荣华富贵]` `[factor_trigger: ronghua_fugui AND wu_chongpo]` `[role: 总结]` 柱中年月无冲破，必是荣华富贵人。 → 《三命通会》卷八#六丙日癸巳时"""
    normalized_text_zh: str = """"""
    subject: str = "六丙日癸巳时断：日禄归时与正官坐贵"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_bing', 'bazi_semantic', 'bazi_state_factor_345', 'bazi_semantic', 'bazi_relation_zhenguan_1', 'bazi_semantic', 'bazi_state_factor_175', 'bazi_semantic', 'hour_branch_si', 'bazi_semantic', 'bazi_condition_factor_52', 'bazi_semantic', 'source_ref', 'rel_smth_08_088', 'rilu_guishi', 'rel_smth_08_089', 'zhengguan_zuogui', 'rel_smth_08_090', 'wuchong_wupo', 'evi_smth_08_088', 'rilu_guishi', 'rule_rilu', 'evi_smth_08_089', 'zhengguan_zuogui', 'rule_zuogui', 'evi_smth_08_090', 'huhuan_luma', 'rule_huhuan', 'map_smth_08_059', 'map_smth_08_060']
    
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
        l1_anchor="smth_v1.0.0_六丙日癸巳时断_日禄归时与正官坐贵_001_L1",
    )
    version: str = "1.0.0"
