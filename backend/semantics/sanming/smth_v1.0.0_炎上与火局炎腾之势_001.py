"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412815
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
    semantic_id="smth_v1.0.0_炎上与火局炎腾之势_001",
    book_id="sanming",
    engine_id="bazi"
)
class 炎上与火局炎腾之势(SemanticEntry):
    """
    - **原文（source_text）**：

  丙丁日遇寅午戌局，柱中须有寅字带印为入格，无寅止是九流近贵之命，若火自旺，无亥水相济，不贵。喜东北方运，忌见辰丑戊己，晦火光明，多主眼疾，或患风气，...
    """
    
    original_text: str = """- **原文（source_text）**：

  丙丁日遇寅午戌局，柱中须有寅字带印为入格，无寅止是九流近贵之命，若火自旺，无亥水相济，不贵。喜东北方运，忌见辰丑戊己，晦火光明，多主眼疾，或患风气，柱有木制成贵，忌水金乡，怕冲。诗曰：丙丁日坐寅午戌，火炎上格从此出，无寅无亥不成名，忌逢土晦主残疾。

- 分字分词释义：

  - **炎上**：火性本炎上，向上腾举，象征显达、外放与光明之势。
  - **丙丁日遇寅午戌局**：日主为丙丁火，三支成寅午戌火局，火势极旺，有炎上之象。
  - **须有寅字带印为入格**：寅中藏丙戊甲，其中甲木为印，既为火之源，又为火之根，故须见寅印以成真格。
  - **无寅止是九流近贵之命**：若只见午戌而无寅印，火虽旺而少根，多为“近贵”而不算上格。
  - **火自旺，无亥水相济，不贵**：火若过旺而不见亥水调剂，则成燥烈之火，难成贵格。
  - **喜东北方运，忌见辰丑戊己，晦火光明**：东北多指寅卯辰、丑寅等运程，有助于木火相生；辰丑土重则晦火之光，易生疾患。

- **规范化释义（primary_lang_explained）**：

  炎上格，是以丙丁火日配合寅午戌火局而成的一种“火势腾空”的格局。火性本向上，象征人的表现欲、上升动力与外显的光明；当日主又落在寅午戌之中，且真有寅印护持时，就好像一束火焰在有根、有柴、有风的条件下向上腾跃，容易在名声、事业上脱颖而出。

  但原文也提醒：若只有火局而无寅印，或火旺却无亥水相济，则此“炎上”容易演成燥烈之火——外在看似辉煌，却因根基不足或调剂不够，而在健康、眼目或情绪上出现隐忧。若行运又多逢晦火之土，或者冲破局中平衡，则更宜警惕残疾、风气之类的问题。

- 核心要点：

  - 以**丙丁日 + 寅午戌火局**为基础，且宜见寅印、亥水以调剂，方为上乘炎上格。
  - 火局成而无寅印者，多为“近贵”，需谨慎评估根基与持续性。
  - 土重晦火、金水相冲之时，易损伤眼目与身体，亦可能在声名上遭遇折损。

- 详细解说：

  与曲直格偏重木德之仁寿不同，炎上格突出的是火德之明与上升。寅午戌三支合火局，寅为生发之门、午为火旺之极、戌为火库与余热之所，三者合一，象征一个人从起步、登高到收束的完整火程。若局中再有亥水相济，则火不至于燥烈，容易体现在文化、学术、仕途或公众领域的亮眼表现。

  实务判断时，需特别关注两点：一是寅印是否真实存在、且不过度受制，这关系到命主是否有内在修养与学习能力来支撑外在之名；二是行运是否帮助火水调和，避免过多晦火之土或克制过甚之金水，以免炎上之势变成“虚火上炎”，导致眼目疾患、神经系统问题或名誉上的波折。

- **校勘与字词辨析（双语）**：

  - 原文“丙丁日遇寅午戌局，柱中须有寅字带印为入格”一句，本稿在释义中明确“寅”为印根之重心，而不单作火局一支看待。
  - “九流近贵”一语，本稿理解为“有贵而不极”“在边缘层级”的象征说法，不作贬义人品之断。
  - 对“喜东北方运，忌见辰丑戊己”之句，本稿将其归纳为对木火帮扶与土重晦火两类行运倾向的提示，而不逐条罗列具体运程推算。
  - **English**：
    - Does not list specific fortune-cycle calculations clause by clause.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_181]` `[trigger: 炎上定义]` `[factor_trigger: yanshang_presence AND yinwuxu_huoju]` `[role: 主干]` 丙丁日遇寅午戌局，柱中须有寅字带印为入格。 → 《三命通会》卷六#炎上
  - `[ns_smth_06_182]` `[trigger: 火势腾空]` `[factor_trigger: huoshi_tengkong AND mingda_waifang]` `[role: 主干依赖]` 火性本炎上，向上腾举，象征显达、外放与光明之势。 → 《三命通会》卷六#炎上
  - `[ns_smth_06_183]` `[trigger: 无寅九流]` `[factor_trigger: wuyin_zhiyou_wuxu AND jiuliu_jingui]` `[role: 条件分支]` 无寅止是九流近贵之命。 → 《三命通会》卷六#炎上
  - `[ns_smth_06_184]` `[trigger: 忌土晦火]` `[factor_trigger: jitu_huihuo AND yan_ji]` `[role: 总结]` 忌见辰丑戊己，晦火光明，多主眼疾。 → 《三命通会》卷六#炎上"""
    normalized_text_zh: str = """"""
    subject: str = "炎上与火局炎腾之势"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_45', 'bazi_semantic', 'bazi_structure_fire', 'bazi_semantic', 'bazi_state_yin_degree', 'bazi_semantic', 'bazi_state_fire_degree', 'bazi_semantic', 'bazi_condition_hai_water_fire_condition', 'bazi_semantic', 'bazi_condition_earth_fire', 'bazi_semantic', 'source_ref', 'rel_smth_06_163', 'yanshang_ge_presence', 'rel_smth_06_164', 'yinzi_ruge', 'rel_smth_06_165', 'haishui_jihuo', 'evi_smth_06_163', 'yanshang_ge_presence', 'rule_yanshang', 'evi_smth_06_164', 'yinzi_ruge', 'rule_daiyin', 'evi_smth_06_165', 'tuhuihuo_risk', 'rule_tuhuihuo', 'map_smth_06_109', 'map_smth_06_110']
    
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
        l1_anchor="smth_v1.0.0_炎上与火局炎腾之势_001_L1",
    )
    version: str = "1.0.0"
