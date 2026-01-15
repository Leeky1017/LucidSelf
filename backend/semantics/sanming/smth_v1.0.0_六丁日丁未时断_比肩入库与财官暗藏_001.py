"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157641
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
    semantic_id="smth_v1.0.0_六丁日丁未时断_比肩入库与财官暗藏_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六丁日丁未时断比肩入库与财官暗藏(SemanticEntry):
    """
    - 原文（source_text）：

  六丁日丁未时断。

  六丁日生时丁未，比肩入库财官藏；若逢冲破财官旺，不贵即富福禄长。丁日丁未时，比肩入库，丁火比肩入未库，未中有乙木印、己土食神，暗藏财...
    """
    
    original_text: str = """- 原文（source_text）：

  六丁日丁未时断。

  六丁日生时丁未，比肩入库财官藏；若逢冲破财官旺，不贵即富福禄长。丁日丁未时，比肩入库，丁火比肩入未库，未中有乙木印、己土食神，暗藏财官。若生丑月，丑未相冲，冲开比肩库，财官得用。辰戌丑未月，杂气财官，大贵。

  丁丑日丁未时，丑未相冲，冲开库位，大发。春身旺，贵。夏平，秋富，冬吉。

  丁卯日丁未时，卯未半合，春身旺，贵。秋财旺，行南运，富。

  丁巳日丁未时，贵。寅午戌月，身旺，大贵。

  丁未日丁未时，两未自刑，伤妻害子。春身旺，贵。丑月冲库，大发。

  丁酉日丁未时，酉未暗合，春身旺，贵。秋财旺，富。

  丁亥日丁未时，亥未半合，春身旺，贵。冬官旺，吉。

  丁日丁未时上逢，比肩入库财官藏；若逢冲破财官旺，不贵即富福禄长。丁日丁未时准，比肩入库相逢。若还冲动发荣昌，不冲终为平常。

- 分字分词释义：

  - **比肩入库**：丁火比肩入未库，比肩有储藏。
  - **财官暗藏**：未中暗藏乙木印、己土食神，间接关联财官。
  - **冲开发财**：丑冲未，冲开库位，财官得用。

- 规范化释义（primary_lang_explained）：

  本节讲「六丁日，丁未时」：

  - 丁火比肩入未库，未中暗藏印星、食神，间接关联财官；
  - 若生丑月或柱有丑字，丑未相冲，冲开库位，财官得用，大发；
  - 不冲则储而不发，平常衣禄。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ding Days with Ding-Wei Hour":

  - Ding Fire Shoulder enters Wei treasury; Wei secretly contains Yi Wood Seal and Ji Earth Food God—indirectly relating to wealth-official.
  - If born in Chou month or chart has Chou, Chou-Wei clash opens treasury position, wealth-official become usable, great prosperity.
  - Without clash, stored but not released—ordinary livelihood.

- 核心要点：

  - 本格以「比肩入库」为核心，需冲开方能发用。
  - 暗藏印食，间接关联财官。
  - 冲开则大富大贵，不冲则平常。

- 详细解说：

  1. **比肩入库的特点**  
     - 未为火库，丁火比肩入库有储藏；  
     - 未中暗藏乙木印、己土食神。

  2. **冲开的重要性**  
     - 丑冲未，冲开库位，财官得用；  
     - 若不冲，则储而不发。

- 校勘与字词辨析：

  - 「财官藏」形容财官隐藏于库中。
  - 「福禄长」指福禄长久。
  - **English**：
    - Fortune and salary lasting long.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_173]` `[trigger: 比肩入库]` `[factor_trigger: bijian_ruku AND caiguan_cang]` `[role: 主干]` 六丁日生时丁未，比肩入库财官藏。 → 《三命通会》卷八#六丁日丁未时
  - `[ns_smth_08_174]` `[trigger: 冲破财官]` `[factor_trigger: chongpo_caiguan AND bugui_jifu]` `[role: 主干依赖]` 若逢冲破财官旺，不贵即富福禄长。 → 《三命通会》卷八#六丁日丁未时
  - `[ns_smth_08_175]` `[trigger: 丑未相冲]` `[factor_trigger: chouwei_xiangchong AND da_fa]` `[role: 条件分支]` 若生丑月，丑未相冲，冲开比肩库，财官得用。 → 《三命通会》卷八#六丁日丁未时
  - `[ns_smth_08_176]` `[trigger: 冲动荣昌]` `[factor_trigger: chongdong_rongchang AND bu_chong_pingchang]` `[role: 总结]` 若还冲动发荣昌，不冲终为平常。 → 《三命通会》卷八#六丁日丁未时"""
    normalized_text_zh: str = """"""
    subject: str = "六丁日丁未时断：比肩入库与财官暗藏"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_ding', 'bazi_semantic', 'bazi_state_bijian_2', 'bazi_semantic', 'bazi_relation_factor_95', 'bazi_semantic', 'bazi_state_factor_211', 'bazi_semantic', 'hour_branch_wei', 'bazi_semantic', 'bazi_condition_factor_79', 'bazi_semantic', 'source_ref', 'rel_smth_08_130', 'bijian_ruku', 'rel_smth_08_131', 'caiguan_ancang', 'rel_smth_08_132', 'youchong_youfa', 'evi_smth_08_130', 'bijian_ruku', 'rule_biruku', 'evi_smth_08_131', 'caiguan_ancang', 'rule_ancang2', 'evi_smth_08_132', 'chongkai_facai', 'rule_chongkai3', 'map_smth_08_087', 'map_smth_08_088']
    
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
        l1_anchor="smth_v1.0.0_六丁日丁未时断_比肩入库与财官暗藏_001_L1",
    )
    version: str = "1.0.0"
