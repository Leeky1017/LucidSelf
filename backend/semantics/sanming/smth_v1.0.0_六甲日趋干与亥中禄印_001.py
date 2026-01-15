"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412397
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
    semantic_id="smth_v1.0.0_六甲日趋干与亥中禄印_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六甲日趋干与亥中禄印(SemanticEntry):
    """
    - **原文（source_text）**：

  此格乃六甲日见亥。亥，天门之位，北极之垣，甲木赖之长生。又亥能合出寅中本禄，与趋艮同。忌寅字填实，巳字刑冲。又曰：甲见亥时，亥有壬禄为印，喜见辛金生...
    """
    
    original_text: str = """- **原文（source_text）**：

  此格乃六甲日见亥。亥，天门之位，北极之垣，甲木赖之长生。又亥能合出寅中本禄，与趋艮同。忌寅字填实，巳字刑冲。又曰：甲见亥时，亥有壬禄为印，喜见辛金生印，不喜见财，柱有卯合亥，即不能合寅中禄矣，若身弱遇巳酉丑局，金神太多，岁运重见，生灾。《相心赋》云：六甲趋干，主仁慈刚介心平。《真宝赋》云：六甲趋干，透印绶为佳，财星叠见，位列名卿。《千里马》云：壬趋艮，甲趋干，清朝名士。诗曰：趋干六甲最为奇，甲日生人得亥时，岁运若逢财旺处，官灾患难来寻之，详诗与赋，有忌财喜财不同，余见透印忌财，身旺喜财。

- 分字分词释义：

  - **六甲日见亥**：指六个甲日（甲子、甲寅、甲辰、甲午、甲申、甲戌）见亥时或亥支，为“趋干”之基本条件。
  - **亥为天门、北极之垣，甲赖之长生**：亥水为甲木之长生之地，象征甲木根源所在，故“趋干”即趋向根本之气。
  - **亥能合出寅中本禄，与趋艮同**：通过亥与寅之间的关系，引出寅中甲禄，与前节六壬趋艮合出亥中禄的思路相似。
  - **亥有壬禄为印，喜见辛金生印，不喜见财**：亥中藏壬水为甲之印绶，辛金又能生壬水，故喜辛见印；财星过多则耗印，主官灾患难。
  - **卯合亥则不能合寅中禄**：卯若合亥，亥之力量被卯牵制，难再合引寅中甲禄，格局受损。
  - **身弱遇巳酉丑局、金神太多则生灾**：甲木本柔，若身弱而又逢巳酉丑等金局，金多克木，虽有印禄亦难承受。
  - **透印绶为佳，财星叠见则位列名卿或致官灾**：原文对于“喜财”与“忌财”有不同说法，本稿以“身旺可喜财、身弱忌财”加以调和。

- **规范化释义（primary_lang_explained）**：

  六甲趋干格，是六个甲日见亥所成的一种“趋向长生之地、合出本禄并得印绶”的格局。甲木之长生在亥，亥中又藏壬水为印，若再有辛金生壬，则构成“辛生壬印，壬印生甲”的生扶链条。同时，亥还可与寅发生关系，将寅中甲禄合引出来，使甲木既得禄，又得印。
  
  因此，本格的精华在于：甲日身旺、得亥印生、又能引出寅中本禄，而不为寅、巳、卯、财星等因素所破。寅字填实，则禄位过满、难以灵动；巳字刑冲，则破坏亥寅之间的连结；卯合亥，则使亥失去合寅之力。若再身弱而逢巳酉丑等金局、或岁运财旺之乡，则印被财耗、木被金伤，原本“仁慈刚介”的甲木之德，反而因外力过强而折损。

- 核心要点：

  - 本格以**六甲日 + 亥为关键支位**为骨架，兼具禄与印两重资源。
  - 亥既为甲之长生，又藏壬印，并能合出寅中甲禄，是“趋干”的枢纽所在。
  - 忌寅填实、巳刑冲、卯合亥以及财星过多，皆会削弱或破坏禄印结构。
  - 身旺者可稍取财以行用；身弱者宜重印而忌财、忌金局，方能保格。

- 详细解说：

  与六壬趋艮相比，六甲趋干的侧重点略有不同：前者重在壬禄暗出，兼带财官印；后者则重在甲木“回归根本之气”，以印绶护禄。亥为“天门”，在甲木体系中既是长生之源，又是印禄汇聚之处——故“趋干”实为趋向根本、回归本源。
  
  结构上，可以理解为：
  
  1. 亥中壬水为印，辛金生壬，形成金生水、水生木的正向链条；
  2. 亥与寅之间的关系，使寅中甲禄得以被引动，为甲日提供稳定的地位与资源；
   3. 若再有适量财星，则可在身旺、印足的前提下，将禄印所带来的权势转化为实际的物质与职位收益。
      原文诸赋中，既有“透印绶为佳”的说法，也有“岁运若逢财旺处，官灾患难来寻之”的警示，其关键在于：身旺则可喜财，身弱则宜忌财；一味强调“喜财”或“一味忌财”都不全面，需要结合具体局势权衡。
      - **校勘与字词辨析（双语）**：
      - 原文“亥，天门之位，北极之垣，甲木赖之长生”一句，本稿保留并在白话中解释为“亥为甲木根源与长生之地”。
   - 对“亥能合出寅中本禄，与趋艮同”之句，本稿在释义中对照前节六壬趋艮，指出两者皆以合引本禄，只是起用之干不同。
   - 关于“忌财喜财”的不同说法，本稿在详细解说中以“视身旺身弱而定”加以折中说明，不简单偏向其一。
  - **English**：
    - The sentence "Hai is Heaven's Gate, North Pole enclosure, where Jia wood relies on for long life" is preserved; vernacular explains "Hai is Jia wood's root and long-life position."
    - Regarding whether "multiple Hai can gather nobility," this edition provides a balanced explanation based on "depending on body strength" without simply favoring one view.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_061]` `[trigger: 六甲趋干定义]` `[factor_trigger: liujia_qugan_presence]` `[role: 主干]` 此格乃六甲日见亥。亥，天门之位，北极之垣，甲木赖之长生。 → 《三命通会》卷六#六甲趋干
  - `[ns_smth_06_062]` `[trigger: 亥合出禄]` `[factor_trigger: hai_he_chu_yin_lu]` `[role: 主干依赖]` 亥能合出寅中本禄，与趋艮同。 → 《三命通会》卷六#六甲趋干
  - `[ns_smth_06_063]` `[trigger: 忌寅填巳冲]` `[factor_trigger: ji_yin_tianshi OR ji_si_chong]` `[role: 条件分支]` 忌寅字填实，巳字刑冲。 → 《三命通会》卷六#六甲趋干
  - `[ns_smth_06_064]` `[trigger: 仁慈刚介]` `[factor_trigger: renci_gangjie_xinping]` `[role: 总结]` 《相心赋》云：六甲趋干，主仁慈刚介心平。 → 《三命通会》卷六#六甲趋干

---"""
    normalized_text_zh: str = """"""
    subject: str = "六甲日趋干与亥中禄印"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_jia_1', 'bazi_semantic', 'bazi_condition_hai_1', 'bazi_semantic', 'bazi_condition_xin_ren', 'bazi_semantic', 'bazi_state_yin_si', 'bazi_semantic', 'bazi_condition_factor_148', 'bazi_semantic', 'source_ref', 'rel_smth_06_046', 'liujia_qugan_presence', 'rel_smth_06_047', 'xinsheng_renyin', 'rel_smth_06_048', 'yintian_sichong', 'evi_smth_06_046', 'haiwei_shuniu', 'rule_qugan', 'evi_smth_06_047', 'xinsheng_renyin', 'rule_xinyin', 'evi_smth_06_048', 'yintian_sichong', 'rule_tianchong', 'map_smth_06_031', 'map_smth_06_032']
    
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
        l1_anchor="smth_v1.0.0_六甲日趋干与亥中禄印_001_L1",
    )
    version: str = "1.0.0"
