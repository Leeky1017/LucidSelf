"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339707
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
    semantic_id="smth_v1.0.0_六癸日壬戌时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六癸日壬戌时(SemanticEntry):
    """
    - 原文（source_text）：
  六癸日生日壬戌，支内正官生财库。月兼有救贵多成，倚托若无终不富。
  癸日壬戌时，水火既济，癸用丙丁为财，戊土为官，戊与癸合旺，为人智谋，通月气有倚托者贵；不...
    """
    
    original_text: str = """- 原文（source_text）：
  六癸日生日壬戌，支内正官生财库。月兼有救贵多成，倚托若无终不富。
  癸日壬戌时，水火既济，癸用丙丁为财，戊土为官，戊与癸合旺，为人智谋，通月气有倚托者贵；不通，平常；通火土月气，富贵双全；运气通，亦吉。

- 分字分词释义：
  - **正官生财库**：戌中戊土（官）、丁火（财）、辛金（印）。
  - **水火既济**：癸水与戌中丁火。
  - **戊癸合**：日主合官。

- **规范化释义（primary_lang_explained）**：
  六癸日出生于壬戌时，戌中财官印俱全，且戊土正官与癸水相合，财官有情。壬水劫财帮身。若通月气有倚托，主富贵。若生于火土月（财官月），更是富贵双全。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Gui Days with Ren-Xu Hour":

  - Branch inside Proper Official generates Wealth treasury—Xu contains Wu Earth (Official), Ding Fire (Wealth), Xin Metal (Seal).
  - If month also has rescue noble mostly accomplished; without support eventually not wealthy.
  - Water-Fire mutual completion; Wu-Gui combine prosperous; intelligent with schemes; connecting monthly qi with support, noble; connecting Fire-Earth month, wealthy-noble double complete.
  - Key: Official combines body with Wealth treasury; body strong to handle.

- 核心要点：
  - **财官库**：戌为火库（财），亦藏官。
  - **官星合身**：戊癸合。
  - **劫财帮身**：壬水透。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_gui_renxu_001]` `[trigger: 财官入库]` `[factor_trigger: gui_renxu AND caiguan_ruku]` `[role: 主干]` 癸日壬戌时，支内正官生财库，戌中财官印俱全。 → 《三命通会》卷九#六癸日壬戌时
  - `[ns_smth_09_gui_renxu_002]` `[trigger: 水火既济]` `[factor_trigger: shuihuo_jiji AND zhi_mouquan]` `[role: 主干依赖]` 水火既济，癸用丙丁为财，戊土为官，戊与癸合旺，为人智谋。 → 《三命通会》卷九#六癸日壬戌时
  - `[ns_smth_09_gui_renxu_003]` `[trigger: 通火土月]` `[factor_trigger: tong_huotu_yueqi AND fugui_shuangquan]` `[role: 条件分支]` 通月气有倔托者贵；通火土月气，富贵双全。 → 《三命通会》卷九#六癸日壬戌时
  - `[ns_smth_09_gui_renxu_004]` `[trigger: 倔托若无]` `[factor_trigger: yituo_ruowu AND zhong_bufu]` `[role: 总结]` 月兼有救贵多成，倔托若无终不富。 → 《三命通会》卷九#六癸日壬戌时"""
    normalized_text_zh: str = """"""
    subject: str = "六癸日壬戌时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_gui', 'bazi_semantic', 'bazi_state_factor_325', 'bazi_semantic', 'bazi_relation_factor_132', 'bazi_semantic', 'bazi_state_water_fire', 'bazi_semantic', 'hour_branch_xu', 'bazi_semantic', 'bazi_condition_fire_earth_3', 'bazi_semantic', 'source_ref', 'rel_smth_09_175', 'caiguan_ruku', 'rel_smth_09_176', 'tong_huotu_yueqi', 'rel_smth_09_177', 'yituo_ruowu', 'evi_smth_09_175', 'caiguan_ruku', 'rule_caiguan_ruku1', 'evi_smth_09_176', 'fugui_shuangquan', 'rule_fugui_shuangquan1', 'evi_smth_09_177', 'zhong_bufu', 'rule_wuyituo_bufu1', 'map_smth_09_117', 'map_smth_09_118']
    
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
        l1_anchor="smth_v1.0.0_六癸日壬戌时_001_L1",
    )
    version: str = "1.0.0"
