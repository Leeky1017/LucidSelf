"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157759
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
    semantic_id="smth_v1.0.0_六戊日己未时断_劫财入库与财官暗藏_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六戊日己未时断劫财入库与财官暗藏(SemanticEntry):
    """
    - 原文（source_text）：

  六戊日己未时断。

  六戊日生时己未，劫财入库财官藏；若逢冲破财官旺，不贵即富福禄长。戊日己未时，劫财入库，己土劫财入未库，未中有乙木官、丁火印，暗藏财官...
    """
    
    original_text: str = """- 原文（source_text）：

  六戊日己未时断。

  六戊日生时己未，劫财入库财官藏；若逢冲破财官旺，不贵即富福禄长。戊日己未时，劫财入库，己土劫财入未库，未中有乙木官、丁火印，暗藏财官。若生丑月，丑未相冲，冲开劫财库，财官得用。辰戌丑未月，杂气财官，大贵。

  戊子日己未时，子未相害，伤妻害子。春印旺，贵。夏身旺，吉。丑月冲库，大发。

  戊寅日己未时，寅未暗合，春印旺，贵。夏身旺，吉。

  戊辰日己未时，春印旺，贵。夏身旺，吉。丑月冲库，大发。

  戊午日己未时，午未合，合劫财。春印旺，贵。夏身旺，吉。

  戊申日己未时，春印旺，贵。秋财旺，行南运，富。

  戊戌日己未时，未戌刑，刑伤妻子。丑月冲库，大发。辰戌丑未年月，大贵。

  戊日己未时上逢，劫财入库财官藏；若逢冲破财官旺，不贵即富福禄长。戊日己未时准，劫财入库相逢。若还冲动发荣昌，不冲终为平常。

- 分字分词释义：

  - **劫财入库**：己土劫财入未库，劫财有储藏。
  - **财官暗藏**：未中暗藏乙木官、丁火印，间接关联财官。
  - **冲开发财**：丑冲未，冲开库位，财官得用。

- 规范化释义（primary_lang_explained）：

  本节讲「六戊日，己未时」：

  - 己土劫财入未库，未中暗藏官星、印星，间接关联财官；
  - 若生丑月或柱有丑字，丑未相冲，冲开库位，财官得用，大发；
  - 不冲则储而不发，平常衣禄。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Wu Days with Ji-Wei Hour":

  - Ji Earth Rob Wealth enters Wei treasury; Wei secretly contains Yi Wood Official and Ding Fire Seal—hidden wealth-official.
  - If born in Chou month or chart has Chou, Chou-Wei clash opens treasury—wealth-official become usable, great prosperity.
  - Without clash, stored but not released—ordinary livelihood.

- 核心要点：

  - 本格以「劫财入库」为核心，需冲开方能发用。
  - 暗藏官印，间接关联财官。
  - 冲开则大富大贵，不冲则平常。

- 详细解说：

  1. **劫财入库的特点**  
     - 未为火库，己土劫财入库有储藏；  
     - 未中暗藏乙木官、丁火印。

  2. **冲开的重要性**  
     - 丑冲未，冲开库位，财官得用；  
     - 若不冲，则储而不发。

- 校勘与字词辨析：

  - 「财官藏」形容财官隐藏于库中。
  - 「福禄长」指福禄长久。
  - **English**：
    - Fortune and salary lasting long.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_221]` `[trigger: 劫财入库]` `[factor_trigger: jiecai_ruku AND caiguan_cang]` `[role: 主干]` 六戊日生时己未，劫财入库财官藏。 → 《三命通会》卷八#六戊日己未时
  - `[ns_smth_08_222]` `[trigger: 冲破财官]` `[factor_trigger: chongpo_caiguan AND bugui_jifu]` `[role: 主干依赖]` 若逢冲破财官旺，不贵即富福禄长。 → 《三命通会》卷八#六戊日己未时
  - `[ns_smth_08_223]` `[trigger: 丑未相冲]` `[factor_trigger: chouwei_xiangchong AND da_fa]` `[role: 条件分支]` 若生丑月，丑未相冲，冲开劫财库，财官得用。 → 《三命通会》卷八#六戊日己未时
  - `[ns_smth_08_224]` `[trigger: 冲动荣昌]` `[factor_trigger: chongdong_rongchang AND bu_chong_pingchang]` `[role: 总结]` 若还冲动发荣昌，不冲终为平常。 → 《三命通会》卷八#六戊日己未时"""
    normalized_text_zh: str = """"""
    subject: str = "六戊日己未时断：劫财入库与财官暗藏"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_wu', 'bazi_semantic', 'bazi_state_jiecai', 'bazi_semantic', 'bazi_relation_factor_95', 'bazi_semantic', 'bazi_state_factor_211', 'bazi_semantic', 'hour_branch_wei', 'bazi_semantic', 'bazi_condition_factor_79', 'bazi_semantic', 'source_ref', 'rel_smth_08_166', 'jiecai_ruku', 'rel_smth_08_167', 'caiguan_ancang', 'rel_smth_08_168', 'youchong_youfa', 'evi_smth_08_166', 'jiecai_ruku', 'rule_jiecairuku', 'evi_smth_08_167', 'caiguan_ancang', 'rule_ancang3', 'evi_smth_08_168', 'chongkai_facai', 'rule_chongkai7', 'map_smth_08_111', 'map_smth_08_112']
    
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
        l1_anchor="smth_v1.0.0_六戊日己未时断_劫财入库与财官暗藏_001_L1",
    )
    version: str = "1.0.0"
