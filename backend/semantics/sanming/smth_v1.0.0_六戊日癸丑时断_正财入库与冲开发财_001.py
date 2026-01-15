"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157700
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
    semantic_id="smth_v1.0.0_六戊日癸丑时断_正财入库与冲开发财_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六戊日癸丑时断正财入库与冲开发财(SemanticEntry):
    """
    - 原文（source_text）：

  六戊日癸丑时断。

  六戊日生时癸丑，正财入库待冲逢；若逢未字冲开库，定主财源广进通。戊日癸丑时，正财入库，癸水正财入丑库，戊癸合化火，若生未月，丑未相冲...
    """
    
    original_text: str = """- 原文（source_text）：

  六戊日癸丑时断。

  六戊日生时癸丑，正财入库待冲逢；若逢未字冲开库，定主财源广进通。戊日癸丑时，正财入库，癸水正财入丑库，戊癸合化火，若生未月，丑未相冲，冲开财库，大发财。辰戌丑未月，杂气财官，大贵。

  戊子日癸丑时，子丑合，合财，富。春印旺，贵。夏身旺，吉。

  戊寅日癸丑时，寅为长生，身旺用财，贵。丑未月，冲库，大发。

  戊辰日癸丑时，辰丑比肩，春印旺，贵。未月冲库，大发。

  戊午日癸丑时，丑刑午，刑伤妻子。春印旺，贵。夏身旺，吉。

  戊申日癸丑时，巳酉丑月，合财，大富。寅午戌月，身旺，大贵。

  戊戌日癸丑时，丑戌刑，刑伤妻子。未月冲库，大发。辰戌丑未年月，大贵。

  戊日癸丑时上逢，正财入库待冲逢；运行未字冲开库，定主财源广进通。戊日癸丑时准，正财入库相逢。若还冲动发荣昌，不冲终为平常。

- 分字分词释义：

  - **正财入库**：癸水正财入丑库，财源有储藏。
  - **戊癸合化**：戊土与癸水相合，有化火之象。
  - **冲开发财**：未冲丑，冲开财库，财源涌出。

- 规范化释义（primary_lang_explained）：

  本节讲「六戊日，癸丑时」：

  - 癸水正财入丑库，财源有储藏；戊癸相合，有化火之象；
  - 若生未月或柱有未字，丑未相冲，冲开财库，大发财；
  - 不冲则财源储而不发，平常衣禄。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Wu Days with Gui-Chou Hour":

  - Gui Water Direct Wealth enters Chou treasury; Wu-Gui combine with fire transformation potential.
  - If born in Wei month or chart has Wei, Chou-Wei clash opens wealth treasury leading to great riches.
  - Without clash, wealth remains stored but not released—ordinary livelihood.

- 核心要点：

  - 本格以「正财入库」为核心，需冲开方能发用。
  - 戊癸合化是特点，但需看是否真化。
  - 冲开则财源广进，不冲则平常。

- 详细解说：

  1. **正财入库的特点**  
     - 丑为金库（也藏水气），癸水正财入库有储藏；  
     - 需要未冲或行运冲开，方能发挥。

  2. **戊癸合化的影响**  
     - 戊土与癸水相合，有化火之象；  
     - 若化成，则财变为印，性质改变。

- 校勘与字词辨析：

  - 「待冲逢」形容财库等待冲开后方能发挥。
  - 「发荣昌」形容发达兴旺。
  - **English**：
    - Describes prospering and flourishing.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_197]` `[trigger: 正财入库]` `[factor_trigger: zhengcai_ruku AND dai_chong_feng]` `[role: 主干]` 六戊日生时癸丑，正财入库待冲逢。 → 《三命通会》卷八#六戊日癸丑时
  - `[ns_smth_08_198]` `[trigger: 未字冲库]` `[factor_trigger: weizi_chongku AND caiyuan_guang]` `[role: 主干依赖]` 若逢未字冲开库，定主财源广进通。 → 《三命通会》卷八#六戊日癸丑时
  - `[ns_smth_08_199]` `[trigger: 戊癸合化]` `[factor_trigger: wugui_hehua AND hua_huo_xiang]` `[role: 条件分支]` 戊癸合化火，若化成，则财变为印。 → 《三命通会》卷八#六戊日癸丑时
  - `[ns_smth_08_200]` `[trigger: 冲动荣昌]` `[factor_trigger: chongdong_rongchang AND bu_chong_pingchang]` `[role: 总结]` 若还冲动发荣昌，不冲终为平常。 → 《三命通会》卷八#六戊日癸丑时"""
    normalized_text_zh: str = """"""
    subject: str = "六戊日癸丑时断：正财入库与冲开发财"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_wu', 'bazi_semantic', 'bazi_state_zhengcai', 'bazi_semantic', 'bazi_relation_wu_gui_hehua_1', 'bazi_semantic', 'bazi_state_factor_211', 'bazi_semantic', 'hour_branch_chou', 'bazi_semantic', 'bazi_condition_factor_79', 'bazi_semantic', 'source_ref', 'rel_smth_08_148', 'zhengcai_ruku', 'rel_smth_08_149', 'wugui_hehua', 'rel_smth_08_150', 'youchong_youfa', 'evi_smth_08_148', 'zhengcai_ruku', 'rule_zhengcairuku', 'evi_smth_08_149', 'wugui_hehua', 'rule_wugui', 'evi_smth_08_150', 'chongkai_facai', 'rule_chongkai5', 'map_smth_08_099', 'map_smth_08_100']
    
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
        l1_anchor="smth_v1.0.0_六戊日癸丑时断_正财入库与冲开发财_001_L1",
    )
    version: str = "1.0.0"
