"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412296
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
    semantic_id="smth_v1.0.0_辛癸日寅丑刑合巳禄_001",
    book_id="sanming",
    engine_id="bazi"
)
class 辛癸日寅丑刑合巳禄(SemanticEntry):
    """
    - **原文（source_text）**：

  此格乃辛癸日见丑寅，取寅刑、丑合，刑合出巳中丙戊为辛癸官星，更得一酉字合贵为妙，有刑无合，禄不能住，柱见申巳，即不入格。如壬戌、辛亥、辛丑、庚寅，甲...
    """
    
    original_text: str = """- **原文（source_text）**：

  此格乃辛癸日见丑寅，取寅刑、丑合，刑合出巳中丙戊为辛癸官星，更得一酉字合贵为妙，有刑无合，禄不能住，柱见申巳，即不入格。如壬戌、辛亥、辛丑、庚寅，甲戌、辛未、癸丑、甲寅，二命合格为贵。诗曰：辛癸日生岁月时，若逢寅丑便为奇，寅刑丑合巳中禄，此是功名福贵基。

- 分字分词释义：

  - **辛癸日见丑寅**：仅针对辛日、癸日，柱中同时见丑与寅二支，为格局成立的基础条件。
  - **取寅刑、丑合**：以寅木刑丑土、丑土合巳火的关系，牵动巳中藏丙戊，使其禄气外显。
  - **刑合出巳中丙戊为辛癸官星**：辛以丙为官，癸以戊为官，二者禄在巳宫，经寅刑丑合之力而被引动。
  - **更得一酉字合贵为妙**：若柱中再见酉金，与巳丑成金火土之合局，则官禄之气更纯、更稳。
  - **有刑无合，禄不能住**：若只有寅刑丑而无合住之力，则虽有禄气外动，却难以久留为用。
  - **柱见申巳，即不入格**：若命局再见申、巳等支，破坏原有刑合之平衡，则不再以此格论。

- **规范化释义（primary_lang_explained）**：

  虎午奔巳格，是专为辛日、癸日设计的一种“刑合起官禄”格。辛以丙火为官、癸以戊土为官，而丙、戊二星的禄地皆在巳宫。若命局中同时出现寅、丑，则可借寅刑丑、丑合巳的关系，把巳中丙戊之禄引动出来，成为辛、癸可用的官星与禄位。
  
  在此过程中，寅如虎、午如马、巳为巢，古人以“虎午奔巳”形容寅午之气奔赴巳宫，使巳中禄气飞扬。若再加一酉字，与巳丑形成合局，则官禄更稳，不易散失。反之，若只有寅刑丑而无合局，或命局再见申、巳等支，破坏原有结构，则“禄不能住”，格局难以成就。
  
  原文列举壬戌、辛亥、辛丑、庚寅；甲戌、辛未、癸丑、甲寅等命局为例，说明凡辛癸日得寅丑齐聚、又有合局护禄者，多主功名福贵。“辛癸日生岁月时，若逢寅丑便为奇，寅刑丑合巳中禄，此是功名福贵基”即为此意的总括。

- 核心要点：

  - 虎午奔巳仅适用于**辛日、癸日**，且命局须同时见寅、丑。
  - 关键结构是：寅刑丑、丑合巳，刑合一体，牵出巳中丙戊为辛癸之官星与禄位。
  - 合局之力（如酉字）可稳住禄气；若有刑无合，或再见申巳破局，则禄不久留。
  - 日主身旺、能任官煞，是此格由“有禄”转为“有贵”的前提条件。

- 详细解说：

  从结构类型看，虎午奔巳与子遥巳禄、丑遥巳禄等格一脉相承，都是围绕“巳中禄气”做文章，只是起用方式不同：
  
  - 子遥巳禄以子中癸遥合巳中戊，引动巳禄；
  - 丑遥巳禄以丑刑巳、再合申酉，冲出并合住巳中丙戊；
  - 虎午奔巳则以寅刑丑、丑合巳之“刑合并用”来牵出巳中禄气。
  
  这种“刑中有合”的结构，一方面使禄气得以启动，另一方面也保留了一定的紧张度：若日主身弱或局中再添刑冲，则容易由有功名之机转为官非是非。因此原文又以“柱见申巳，即不入格”告诫：一旦再添申、巳，便会使原有巳中禄气或被过度冲动、或被争合夺禄，格局不再清纯。
  
  实务判断时，可按以下路径考察：
  1. 确认日主为辛或癸，且命局中实有寅、丑两支；
  2. 检查巳中丙戊是否确被寅刑丑合的结构所牵动，而非仅停留在理论可能；
  3. 观察是否有酉等合局支神护禄，避免禄气四散；
  4. 查看是否再见申巳等破格支位，如有则降格或另以官煞格论。

- **校勘与字词辨析（双语）**：

  - 原文“寅刑丑合巳中禄”在古本中未必逐字具现，本稿据上下文与歌诀意旨归纳为“寅刑丑、丑合巳，引动巳中禄气”，在释义中予以明确。
  - “柱见申巳，即不入格”一句，点出申、巳对本格的破坏，本稿保留原语，只在详细解说中展开其结构原因。
  - “虎午奔巳”之名，象征寅午之气奔赴巳宫，本稿未改名号，仅在白话部分解释其象义来源。
  - **English**：
    - The phrase "Yin punishes Chou, combines Si palace salary" is reconstructed from context; this edition explains it as "Yin punishes Chou, Chou combines Si, activating the salary qi in Si."
    - The sentence "if the chart has Shen or Si, it does not qualify" is preserved; the detailed explanation expands on its structural reasoning.
    - The name "Tiger-Horse Rushing to Si" symbolizes Yin-Wu qi rushing toward Si palace; this edition keeps the name and explains its imagery.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_029]` `[trigger: 虎午奔巳定义]` `[factor_trigger: huwu_bensi_presence]` `[role: 主干]` 辛癸日见丑寅，取寅刑、丑合，刑合出巳中丙戊为辛癸官星。 → 《三命通会》卷六#虎午奔巳
  - `[ns_smth_06_030]` `[trigger: 酉字合贵]` `[factor_trigger: you_zi_he_gui]` `[role: 主干依赖]` 更得一酉字合贵为妙。 → 《三命通会》卷六#虎午奔巳
  - `[ns_smth_06_031]` `[trigger: 有刑无合]` `[factor_trigger: you_xing_wu_he OR zhu_jian_shen_si]` `[role: 条件分支]` 有刑无合，禄不能住，柱见申巳，即不入格。 → 《三命通会》卷六#虎午奔巳
  - `[ns_smth_06_032]` `[trigger: 功名福贵]` `[factor_trigger: yin_xing_chou_he_si]` `[role: 总结]` 寅刑丑合巳中禄，此是功名福贵基。 → 《三命通会》卷六#虎午奔巳

---

- **完整对等诠释（secondary_lang_full）**：
  The "Tiger-Horse Rushing to Si" pattern is a punishment-and-combination configuration designed for Xin and Gui days. Xin takes Bing fire as its Proper Official and Gui takes Wu earth as its Proper Official; both stars have their salary seats in Si. When the chart contains both Yin and Chou together, the structure uses "Yin punishes Chou, Chou combines with Si" to set the salary qi of Bing and Wu in motion. The imagery is of a Tiger (Yin) and Horse (Wu) charging toward the Snake's lair (Si), stirring up the hidden official stars and bringing them out for use.
  
  The key requirement is that punishment and combination must work in tandem: Yin punishes Chou to create movement, while Chou combines with Si to channel and hold the released qi. If there is punishment without combination—that is, Yin stirs Chou but nothing gathers the outcome—then the salary qi escapes and cannot serve the day-master. An additional You branch is ideal, because it forms a metal trine with Si and Chou that stabilises and purifies the official star once it has been drawn out.
  
  However, if the chart also contains Shen or Si explicitly, the delicate balance is destroyed. Under these conditions the pattern no longer holds and one must judge the chart by ordinary official-and-Seal standards. When the structure is intact, and the day-master is strong enough to bear the official star, this pattern often correlates with examination success and noble rank."""
    normalized_text_zh: str = """"""
    subject: str = "辛癸日寅丑刑合巳禄"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_wu_si_marker', 'bazi_semantic', 'bazi_structure_yin_chou_si_config', 'bazi_semantic', 'bazi_state_strength_2', 'bazi_semantic', 'bazi_state_you_degree', 'bazi_semantic', 'bazi_condition_shen_si', 'bazi_semantic', 'bazi_condition_day_master_condition_1', 'bazi_semantic', 'source_ref', 'rel_smth_06_022', 'huwu_bensi_presence', 'rel_smth_06_023', 'xinghe_yiti_score', 'rel_smth_06_024', 'shensi_poge_risk', 'evi_smth_06_022', 'yinchou_xinghe_si', 'rule_huwu', 'evi_smth_06_023', 'xinghe_yiti_score', 'rule_xinghe', 'evi_smth_06_024', 'shensi_poge_risk', 'rule_poge', 'map_smth_06_015', 'map_smth_06_016']
    
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
        l1_anchor="smth_v1.0.0_辛癸日寅丑刑合巳禄_001_L1",
    )
    version: str = "1.0.0"
