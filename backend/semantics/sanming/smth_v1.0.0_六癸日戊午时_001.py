"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339672
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
    semantic_id="smth_v1.0.0_六癸日戊午时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六癸日戊午时(SemanticEntry):
    """
    - 原文（source_text）：
  六癸日生时戊午，化火临时帝旺乡。运喜东南木火地，为官清正禄荣昌。
  癸日戊午时，化气成火局，癸合戊化火，午上帝旺，合局而贵，身旺不化癸水，地方之气引到南方，...
    """
    
    original_text: str = """- 原文（source_text）：
  六癸日生时戊午，化火临时帝旺乡。运喜东南木火地，为官清正禄荣昌。
  癸日戊午时，化气成火局，癸合戊化火，午上帝旺，合局而贵，身旺不化癸水，地方之气引到南方，癸水无气，贵而寿促，东方运吉。

- 分字分词释义：
  - **化火**：戊癸合化火。
  - **帝旺乡**：午为火之帝旺。
  - **身旺不化**：若癸水有根，不从化，则为正官格（身弱官旺）。

- **规范化释义（primary_lang_explained）**：
  六癸日出生于戊午时，戊癸合化火，午为火之帝旺，化象得地，主贵。若生于春夏木火地，运喜东南，官职清正荣昌。若日主身旺不化（如生于金水月），则戊土为正官，午为财，财官双美。若身弱无气，虽贵但寿促。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Gui Days with Wu-Wu Hour":

  - Transform Fire approaching time Emperor-Prosperous land—Wu-Gui combine transforming Fire; Wu is Fire's Emperor Prosperous position.
  - Luck likes East-South Wood-Fire land; being official pure-upright Salary glorious-prosperous.
  - If combining pattern completes and noble, body prosperous not transforming Gui Water, southern qi guides, Gui Water no qi, noble but short lifespan.
  - Key: Transformation pattern requires Fire prosperous support; non-transformation sees Official-Wealth double beautiful.

- 核心要点：
  - **化火格**：戊癸化火，喜火旺。
  - **正官格**：不化，财官旺，喜身旺。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_225]` `[trigger: 化火帝旺]` `[factor_trigger: huahuo_diwang AND wu_gui_he]` `[role: 主干]` 六癸日生时戊午，化火临时帝旺乡。 → 《三命通会》卷九#六癸日戊午时
  - `[ns_smth_09_226]` `[trigger: 运喜东南]` `[factor_trigger: yun_xi_dongnan AND guanqing_lurongchang]` `[role: 主干依赖]` 运喜东南木火地，为官清正禄荣昌。 → 《三命通会》卷九#六癸日戊午时
  - `[ns_smth_09_227]` `[trigger: 合局而贵]` `[factor_trigger: heju_ergui AND huahuo_chenxiang]` `[role: 条件分支]` 癸合戊化火，午上帝旺，合局而贵。 → 《三命通会》卷九#六癸日戊午时
  - `[ns_smth_09_228]` `[trigger: 贵而寿促]` `[factor_trigger: gui_er_shoucu AND shenruo_wuqi]` `[role: 总结]` 身旺不化癸水，地方之气引到南方，癸水无气，贵而寿促。 → 《三命通会》卷九#六癸日戊午时"""
    normalized_text_zh: str = """"""
    subject: str = "六癸日戊午时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_gui', 'bazi_semantic', 'bazi_state_wu_gui_fire', 'bazi_semantic', 'bazi_relation_zhenguan_3', 'bazi_semantic', 'bazi_state_factor_318', 'bazi_semantic', 'hour_branch_wu', 'bazi_semantic', 'bazi_condition_wood_fire_2', 'bazi_semantic', 'source_ref', 'rel_smth_09_163', 'wugui_huahuo', 'rel_smth_09_164', 'tong_muhuo_yueqi', 'rel_smth_09_165', 'shenruo_huaqi', 'evi_smth_09_163', 'diwang_xiang', 'rule_huahuo_diwang1', 'evi_smth_09_164', 'guanqing_lurongchang', 'rule_dongnan_lurongchang1', 'evi_smth_09_165', 'gui_shoucu', 'rule_guishoucu1', 'map_smth_09_109', 'map_smth_09_110']
    
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
        l1_anchor="smth_v1.0.0_六癸日戊午时_001_L1",
    )
    version: str = "1.0.0"
