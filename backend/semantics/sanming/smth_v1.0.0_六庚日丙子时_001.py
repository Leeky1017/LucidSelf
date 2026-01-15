"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339427
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
    semantic_id="smth_v1.0.0_六庚日丙子时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六庚日丙子时(SemanticEntry):
    """
    - 原文（source_text）：
  六庚日生时丙子，身鬼俱衰退神强。有托荣华无托贱，鬼逢生旺寿难长。
  庚日丙子时，身鬼俱衰弱。庚以癸为伤，丙为鬼。子上庚死、丙火无气、癸水健旺。若身有倚托，吉...
    """
    
    original_text: str = """- 原文（source_text）：
  六庚日生时丙子，身鬼俱衰退神强。有托荣华无托贱，鬼逢生旺寿难长。
  庚日丙子时，身鬼俱衰弱。庚以癸为伤，丙为鬼。子上庚死、丙火无气、癸水健旺。若身有倚托，吉；无倚托，又行身衰鬼旺运，飘风夭贱。通火气月，要行西运，贵。身弱不然。

- 分字分词释义：
  - **身鬼俱衰**：庚金日主在子为死地（身衰），丙火七煞在子为胎地（受克，无气，故云鬼衰）。
  - **退神强**：子上癸水伤官健旺（临官），伤官为退气之神（相对于财官而言，或者指庚金在子为死，气退）。
  - **有托**：指日主在地支有根气（如申、酉、巳、丑等），或有印绶生身。

- **规范化释义（primary_lang_explained）**：
  六庚日出生于丙子时，日主庚金与七煞丙火皆处于衰弱之地，而伤官癸水却很强旺。若日主有根基倚托，尚可荣华；若无倚托，又行身弱煞旺之运，恐漂泊夭贱。若生于火旺之月，需行西方金运帮身，方贵。若身弱又逢煞旺，寿命难长。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Geng Days with Bing-Zi Hour":

  - Body and Ghost both declining—Geng Metal at Zi is in death position; Bing Fire Seven-Killing at Zi has no qi; Gui Water Hurting Official is robust.
  - With support indicates glory; without support indicates poverty; if killing encounters prosperous phase, longevity is difficult.
  - If born in Fire-prosperous month, must travel Western Metal luck for nobility; weak body cannot achieve this.
  - Key: Hurting Official controls killing but body too weak; support (Seal or Parallel) is essential.

- 核心要点：
  - **时上七煞**：丙火为煞，坐子水受制，煞无力。
  - **伤官旺**：子水伤官旺，克制七煞。
  - **身弱**：庚在子死，需印比帮身。

- 详细解说：
  此格为“伤官制煞”，但问题在于日主太弱。庚金坐子，泄气太重；丙火七煞虽受制，但若行运助煞，身弱难当。故首重身旺。若身强（如庚申、庚辰日），则伤官制煞，格局清纯，主贵。若身弱，则为克泄交加，贫贱夭折。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_049]` `[trigger: 身鬼俱衰]` `[factor_trigger: shengui_jushuai AND tuishen_qiang]` `[role: 主干]` 六庚日生时丙子，身鬼俱衰退神强。 → 《三命通会》卷九#六庚日丙子时
  - `[ns_smth_09_050]` `[trigger: 有托荣华]` `[factor_trigger: youtuo_ronghua AND wutuo_jian]` `[role: 主干依赖]` 有托荣华无托贱，鬼逢生旺寿难长。 → 《三命通会》卷九#六庚日丙子时
  - `[ns_smth_09_051]` `[trigger: 通火气月]` `[factor_trigger: tong_huoqi_yue AND xing_xiyun_gui]` `[role: 条件分支]` 通火气月，要行西运，贵。 → 《三命通会》卷九#六庚日丙子时
  - `[ns_smth_09_052]` `[trigger: 身弱不然]` `[factor_trigger: shenruo_buran AND yaojian]` `[role: 总结]` 身弱不然。 → 《三命通会》卷九#六庚日丙子时"""
    normalized_text_zh: str = """"""
    subject: str = "六庚日丙子时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_geng', 'bazi_semantic', 'bazi_state_factor_270', 'bazi_semantic', 'bazi_relation_shangguan_10', 'bazi_semantic', 'bazi_state_factor_271', 'bazi_semantic', 'hour_branch_zi', 'bazi_semantic', 'bazi_condition_factor_121', 'bazi_semantic', 'source_ref', 'rel_smth_09_037', 'shengui_jushuai', 'rel_smth_09_038', 'shangguan_zhisha', 'rel_smth_09_039', 'youtuo_ronghua', 'evi_smth_09_037', 'shengui_jushuai', 'rule_shengui_jushuai1', 'evi_smth_09_038', 'youtuo_ronghua', 'rule_youtuo_ronghua1', 'evi_smth_09_039', 'shengui_jushuai', 'rule_gui_shengwang1', 'map_smth_09_025', 'map_smth_09_026']
    
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
        l1_anchor="smth_v1.0.0_六庚日丙子时_001_L1",
    )
    version: str = "1.0.0"
