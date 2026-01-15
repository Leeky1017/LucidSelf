"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157748
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
    semantic_id="smth_v1.0.0_六戊日戊午时断_羊刃帝旺与比肩同禄_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六戊日戊午时断羊刃帝旺与比肩同禄(SemanticEntry):
    """
    - 原文（source_text）：

  六戊日戊午时断。

  六戊日生时戊午，羊刃帝旺比肩同；柱有官煞来制合，富贵荣华福禄隆。戊日戊午时，羊刃帝旺，戊土在午为帝旺兼羊刃，戊土比肩同在午。若通身旺...
    """
    
    original_text: str = """- 原文（source_text）：

  六戊日戊午时断。

  六戊日生时戊午，羊刃帝旺比肩同；柱有官煞来制合，富贵荣华福禄隆。戊日戊午时，羊刃帝旺，戊土在午为帝旺兼羊刃，戊土比肩同在午。若通身旺月，无官煞制合，主人性急傲物，刑妻克子。有官煞制刃，大贵。

  戊子日戊午时，子午相冲，伤妻害子。春印旺，贵。夏身旺，吉。冬官旺制刃，贵。

  戊寅日戊午时，寅午半合，身旺。春印旺，贵。夏身旺，吉。冬官旺制刃，大贵。

  戊辰日戊午时，春印旺，贵。夏身旺，吉。申子辰月，官旺制刃，大贵。

  戊午日戊午时，两午自刑，伤妻害子。春印旺，贵。夏身旺，吉。冬官旺制刃，贵。

  戊申日戊午时，春印旺，贵。夏身旺，吉。申子辰月，官旺制刃，贵。

  戊戌日戊午时，寅午戌月，身旺。春印旺，贵。冬官旺制刃，大贵。

  戊日戊午时上逢，羊刃帝旺比肩同；柱有官煞来制合，富贵荣华福禄隆。戊日戊午时准，羊刃帝旺相逢。若无官煞祸相寻，有制方成贵显。

- 分字分词释义：

  - **羊刃帝旺**：午为戊土帝旺之地，又为羊刃位，身极旺。
  - **比肩同禄**：戊土比肩与日主同在午位，比肩帮身。
  - **官煞制刃**：官星或七煞制约羊刃，刚柔并济。

- 规范化释义（primary_lang_explained）：

  本节讲「六戊日，戊午时」：

  - 戊土在午为帝旺兼羊刃，戊土比肩同在午位，身极旺；
  - 若无官煞制合，则性急傲物、刑妻克子；有官煞制刃，则大贵。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Wu Days with Wu-Wu Hour":

  - Wu Earth at Wu is emperor-prosperity combined with sheep-blade; Wu Earth Shoulder also at Wu position—body extremely strong.
  - Without official-killing control, indicates impatient and arrogant nature harming spouse and children; with official-killing controlling blade, achieves great nobility.

- 核心要点：

  - 本格以「羊刃帝旺」为核心，身极旺。
  - 比肩同禄帮身，但羊刃无制是风险。
  - 需要官煞制刃，方能化险为夷。

- 详细解说：

  1. **羊刃帝旺的特点**  
     - 午为戊土帝旺，日主极旺；羊刃主刚强、好斗；  
     - 若无官煞制合，则性格偏激，容易伤害身边人。

  2. **官煞制刃的必要性**  
     - 羊刃太旺，需要官煞来制约；  
     - 有官煞制刃，则刚柔并济，可成就大贵。

- 校勘与字词辨析：

  - 「性急傲物」形容性格急躁、目中无人。
  - 「福禄隆」形容福禄兴隆。
  - **English**：
    - Describes flourishing fortune and salary.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_217]` `[trigger: 羊刃帝旺]` `[factor_trigger: yangren_diwang AND bijian_tong]` `[role: 主干]` 六戊日生时戊午，羊刃帝旺比肩同。 → 《三命通会》卷八#六戊日戊午时
  - `[ns_smth_08_218]` `[trigger: 官煞制合]` `[factor_trigger: guansha_zhihe AND fugui_ronghua]` `[role: 主干依赖]` 柱有官煞来制合，富贵荣华福禄隆。 → 《三命通会》卷八#六戊日戊午时
  - `[ns_smth_08_219]` `[trigger: 无官煞祸]` `[factor_trigger: wu_guansha_huo AND xingji_aowu]` `[role: 条件分支]` 若无官煞制合，主人性急傲物，刑妻克子。 → 《三命通会》卷八#六戊日戊午时
  - `[ns_smth_08_220]` `[trigger: 有制贵显]` `[factor_trigger: youzhi_guixian AND wu_guan_huo]` `[role: 总结]` 若无官煞祸相寻，有制方成贵显。 → 《三命通会》卷八#六戊日戊午时"""
    normalized_text_zh: str = """"""
    subject: str = "六戊日戊午时断：羊刃帝旺与比肩同禄"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_wu', 'bazi_semantic', 'bazi_state_yangren_3', 'bazi_semantic', 'bazi_relation_bijian_1', 'bazi_semantic', 'bazi_state_factor_210', 'bazi_semantic', 'hour_branch_wu', 'bazi_semantic', 'bazi_condition_factor_75', 'bazi_semantic', 'source_ref', 'rel_smth_08_163', 'yangren_diwang', 'rel_smth_08_164', 'bijian_tonglu', 'rel_smth_08_165', 'youguansha_zhi', 'evi_smth_08_163', 'yangren_diwang', 'rule_diwang6', 'evi_smth_08_164', 'bijian_tonglu', 'rule_tonglu', 'evi_smth_08_165', 'guansha_zhiren', 'rule_zhiren3', 'map_smth_08_109', 'map_smth_08_110']
    
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
        l1_anchor="smth_v1.0.0_六戊日戊午时断_羊刃帝旺与比肩同禄_001_L1",
    )
    version: str = "1.0.0"
