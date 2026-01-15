"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339325
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
    semantic_id="smth_v1.0.0_六己日丙寅时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六己日丙寅时(SemanticEntry):
    """
    - 原文（source_text）：
  六己日生时丙寅，暗官明印好光辉。如通月气身强健，更看天干无甲己。
  己日丙寅时，官印生旺。己用甲为官，丙为印，寅上甲旺丙生。如果无破，通月气，身旺，贵；不通...
    """
    
    original_text: str = """- 原文（source_text）：
  六己日生时丙寅，暗官明印好光辉。如通月气身强健，更看天干无甲己。
  己日丙寅时，官印生旺。己用甲为官，丙为印，寅上甲旺丙生。如果无破，通月气，身旺，贵；不通，只是富。忌见甲己，化土为暗鬼；申冲寅，无倚落魄。

- 分字分词释义：
  - **暗官明印**：丙火印绶透干（明印）；寅中藏甲木正官，不透干（暗官）。
  - **官印生旺**：寅为火之长生（一说寅午戌合火），丙火得地；寅为木之禄旺，甲木得地。官印皆旺。
  - **甲己化土**：若天干透甲，甲己合化土（中正之合），若化格不成，反失官星之贵；或指甲己合而化土，寅中甲木（暗鬼）克身（此解较晦涩，通常甲己合为贵，此处恐指合绊官星或化气后官星变质）。

- **规范化释义（primary_lang_explained）**：
  六己日出生于丙寅时，丙火印绶透出，寅中藏甲木正官，官印相生，格局光辉。若日主身强通月气，且天干不透甲木来合己土（或不透己土争合），主大贵。若不通月气，亦主富。最忌申金冲寅木，冲散官印根基，主落魄无依。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ji Days with Bing-Yin Hour":

  - Bing Fire Direct Seal reveals; Jia Wood Direct Official hidden in Yin—forming "hidden official revealed seal" with radiant fortune.
  - If passing monthly qi with strong body and no Jia-Ji combination in stems, indicates great nobility; without monthly qi, still indicates wealth.
  - Taboo: Shen clashing Yin scatters official-seal foundation—leads to poverty and destitution.
  - Key: Official generates Seal, Seal generates Day Master—flowing qi structure is most auspicious.

- 核心要点：
  - **官印双全**：丙寅时，印透官藏，官印相生，贵气聚于时支。
  - **通月气**：身旺方能任财官。
  - **忌冲**：寅申冲为大忌，破禄破官。

- 详细解说：
  己土喜丙火太阳照耀，名为“得火而舒”。丙寅时，火土相生，寅中甲木正官生丙火印绶，印绶生己土日主，气势流通。只要日主有根（如生于巳午未月），或局中有比劫帮身，即成富贵之格。若见甲木透出，形成“官印双透”本佳，但原文疑虑“甲己化土为暗鬼”，可能是指若甲木被合化为土，则官星性质改变，或指甲木克己土（虽为正官，身弱亦忌）。一般而言，丙寅时多为好局，唯忌申冲。

- 校勘与字词辨析：
  - **“甲己化土为暗鬼”**：此句有争议。通常甲己合化土为化气格，若成格则贵。此处可能指在正格中，甲木本为官，若被合化，官星不存；或指甲木在寅中本旺，若化土则成比劫，而寅中甲木仍在暗克（暗鬼）。
  - **English**：
    - Annual fortune (大运) terminology explained; timing indicators treated as influence periods rather than fixed events.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_009]` `[trigger: 暗官明印]` `[factor_trigger: anguan_mingyin AND hao_guanghui]` `[role: 主干]` 六己日生时丙寅，暗官明印好光辉。 → 《三命通会》卷九#六己日丙寅时
  - `[ns_smth_09_010]` `[trigger: 通月身强]` `[factor_trigger: tongyue_shenqiang AND geng_kan_tiangan]` `[role: 主干依赖]` 如通月气身强健，更看天干无甲己。 → 《三命通会》卷九#六己日丙寅时
  - `[ns_smth_09_011]` `[trigger: 官印生旺]` `[factor_trigger: guanyin_shengwang AND gui_or_fu]` `[role: 条件分支]` 如果无破，通月气，身旺，贵；不通，只是富。 → 《三命通会》卷九#六己日丙寅时
  - `[ns_smth_09_012]` `[trigger: 忌申冲寅]` `[factor_trigger: ji_shen_chong_yin AND luopo]` `[role: 总结]` 申冲寅，无倔落魄。 → 《三命通会》卷九#六己日丙寅时"""
    normalized_text_zh: str = """"""
    subject: str = "六己日丙寅时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_ji', 'bazi_semantic', 'bazi_state_factor_255', 'bazi_semantic', 'bazi_relation_factor_110', 'bazi_semantic', 'bazi_state_jia_ji_earth', 'bazi_semantic', 'hour_branch_yin', 'bazi_semantic', 'bazi_condition_shen_yin', 'bazi_semantic', 'source_ref', 'rel_smth_09_007', 'anguan_mingyin', 'rel_smth_09_008', 'shenwang_tongyueqi', 'rel_smth_09_009', 'jishen_chongyin', 'evi_smth_09_007', 'anguan_mingyin', 'rule_anguan_mingyin1', 'evi_smth_09_008', 'shenwang_tongyueqi', 'rule_shenwang_tongyueqi2', 'evi_smth_09_009', 'jishen_chongyin', 'rule_shenchongyin1', 'map_smth_09_005', 'map_smth_09_006']
    
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
        l1_anchor="smth_v1.0.0_六己日丙寅时_001_L1",
    )
    version: str = "1.0.0"
