"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339556
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
    semantic_id="smth_v1.0.0_六辛日癸巳时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六辛日癸巳时(SemanticEntry):
    """
    - 原文（source_text）：
  六辛日生时癸巳，贵气无伤官印强。月气有通兼倚托，早年荣贵姓名香。
  辛日癸巳时，官印扶身。辛以丙为官，戊为印，癸为食神。巳上丙戊健旺，癸合化火，赤白文章。若...
    """
    
    original_text: str = """- 原文（source_text）：
  六辛日生时癸巳，贵气无伤官印强。月气有通兼倚托，早年荣贵姓名香。
  辛日癸巳时，官印扶身。辛以丙为官，戊为印，癸为食神。巳上丙戊健旺，癸合化火，赤白文章。若有倚托、通月气者，显达；若月不通，运通，亦贵。

- 分字分词释义：
  - **官印扶身**：巳中丙（官）戊（印）同宫相生，扶助日主。
  - **癸合化火**：癸水与巳中戊土合（戊癸合），化火（官），或癸水制丙（食神制杀？此处丙为官）。原文“癸合化火”可能指戊癸化火，助起官星。
  - **赤白文章**：赤（火）白（金），金火辉煌，主文章。

- **规范化释义（primary_lang_explained）**：
  六辛日出生于癸巳时，巳中丙火正官、戊土正印健旺，官印相生扶身。癸水食神透出，若与戊合化火（或被戊制），不伤官星。若日主有倚托通月气，早年显达。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Xin Days with Gui-Si Hour":

  - Noble qi unharmed, Official-Seal strong—Si contains Bing Fire Official and Wu Earth Seal both healthy and prosperous.
  - If monthly qi connects with support, early years glorious noble name fragrant.
  - Gui Water Eating God combines transforming Fire (Wu-Gui combine), red-white article (literary talent); with support and monthly qi, prominent.
  - Key: Official-Seal mutual generation supports body; Si is Xin's Long Life position, body not weak.

- 核心要点：
  - **官印双全**：巳为金长生，官印旺。
  - **食神生财/合官**：癸水作用关键。
  - **身旺**：长生之地，身不弱。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_117]` `[trigger: 贵气无伤]` `[factor_trigger: guiqi_wushang AND guanyin_qiang]` `[role: 主干]` 六辛日生时癸巳，贵气无伤官印强。 → 《三命通会》卷九#六辛日癸巳时
  - `[ns_smth_09_118]` `[trigger: 通月气倚托]` `[factor_trigger: tong_yueqi_yituo AND zaonian_ronggui]` `[role: 主干依赖]` 月气有通兼倚托，早年荣贵姓名香。 → 《三命通会》卷九#六辛日癸巳时
  - `[ns_smth_09_119]` `[trigger: 官印扶身]` `[factor_trigger: guanyin_fushen AND chibai_wenzhang]` `[role: 条件分支]` 官印扶身，癸合化火，赤白文章。 → 《三命通会》卷九#六辛日癸巳时
  - `[ns_smth_09_120]` `[trigger: 运通亦贵]` `[factor_trigger: yuntong_yigui AND xianda]` `[role: 总结]` 若月不通，运通，亦贵。 → 《三命通会》卷九#六辛日癸巳时"""
    normalized_text_zh: str = """"""
    subject: str = "六辛日癸巳时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_xin', 'bazi_semantic', 'bazi_state_factor_294', 'bazi_semantic', 'bazi_relation_wu_gui_hehua_1', 'bazi_semantic', 'bazi_state_factor_295', 'bazi_semantic', 'hour_branch_si', 'bazi_semantic', 'bazi_condition_factor_133', 'bazi_semantic', 'source_ref', 'rel_smth_09_088', 'guanyin_fushen', 'rel_smth_09_089', 'guanyin_fushen', 'rel_smth_09_090', 'shishen_poguan', 'evi_smth_09_088', 'guanyin_fushen', 'rule_guanyin_fushen1', 'evi_smth_09_089', 'wu_gui_hehua', 'rule_wugui_hehuo1', 'evi_smth_09_090', 'tong_yueqi_youtuo', 'rule_tongyueqi_youtuo1', 'map_smth_09_059', 'map_smth_09_060']
    
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
        l1_anchor="smth_v1.0.0_六辛日癸巳时_001_L1",
    )
    version: str = "1.0.0"
