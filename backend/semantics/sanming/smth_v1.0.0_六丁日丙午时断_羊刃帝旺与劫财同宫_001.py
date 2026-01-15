"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157630
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
    semantic_id="smth_v1.0.0_六丁日丙午时断_羊刃帝旺与劫财同宫_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六丁日丙午时断羊刃帝旺与劫财同宫(SemanticEntry):
    """
    - 原文（source_text）：

  六丁日丙午时断。

  六丁日生时丙午，羊刃帝旺劫财同；柱有官煞来制合，富贵荣华福禄隆。丁日丙午时，羊刃帝旺，丁火禄午，丙为劫财，午上帝旺，丁坐羊刃，若通身...
    """
    
    original_text: str = """- 原文（source_text）：

  六丁日丙午时断。

  六丁日生时丙午，羊刃帝旺劫财同；柱有官煞来制合，富贵荣华福禄隆。丁日丙午时，羊刃帝旺，丁火禄午，丙为劫财，午上帝旺，丁坐羊刃，若通身旺月，无官煞制合，主人性急傲物，刑妻克子。有官煞制刃，大贵。

  丁丑日丙午时，丑刑午，刑伤妻子。春身旺，行金水运，贵。秋财旺，富。冬官旺，贵。

  丁卯日丙午时，卯午相破，伤妻害子。春身旺，贵。夏平，秋富，冬吉。

  丁巳日丙午时，贵。寅午戌月，身旺，行金水运，大贵。亥子申月，官煞制刃，贵。

  丁未日丙午时，午未合，春身旺，行金水运，贵。秋财旺，富。

  丁酉日丙午时，卯酉冲，午酉破，伤妻害子。春身旺，行金水运，贵。

  丁亥日丙午时，亥午暗合，春身旺，贵。冬官旺制刃，大贵。

  丁日丙午时上逢，羊刃帝旺劫财同；柱有官煞来制合，富贵荣华福禄隆。丁日丙午时准，羊刃帝旺相逢。若无官煞祸相寻，有制方成贵显。

- 分字分词释义：

  - **羊刃帝旺**：午为丁火帝旺之地，又为羊刃位，身极旺。
  - **劫财同宫**：丙火劫财与丁火同在午位，劫财帮身。
  - **官煞制刃**：官星或七煞制约羊刃，刚柔并济。

- 规范化释义（primary_lang_explained）：

  本节讲「六丁日，丙午时」：

  - 丁火在午为帝旺兼羊刃，丙火劫财同在午位，身极旺；
  - 若无官煞制合，则性急傲物、刑妻克子；有官煞制刃，则大贵。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ding Days with Bing-Wu Hour":

  - Ding Fire at Wu is emperor-prosperity combined with sheep-blade; Bing Fire Rob-Wealth is also at Wu—body extremely strong.
  - Without official-killing control, the person becomes impatient and arrogant, harming spouse and children; with official-killing controlling blade, great nobility is achieved.

- 核心要点：

  - 本格以「羊刃帝旺」为核心，身极旺。
  - 劫财同宫帮身，但羊刃无制是风险。
  - 需要官煞制刃，方能化险为夷。

- 详细解说：

  1. **羊刃帝旺的特点**  
     - 午为丁火帝旺，日主极旺；羊刃主刚强、好斗；  
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
  - `[ns_smth_08_169]` `[trigger: 羊刃帝旺]` `[factor_trigger: yangren_diwang AND jiecai_tong]` `[role: 主干]` 六丁日生时丙午，羊刃帝旺劫财同。 → 《三命通会》卷八#六丁日丙午时
  - `[ns_smth_08_170]` `[trigger: 官煞制合]` `[factor_trigger: guansha_zhihe AND fugui_ronghua]` `[role: 主干依赖]` 柱有官煞来制合，富贵荣华福禄隆。 → 《三命通会》卷八#六丁日丙午时
  - `[ns_smth_08_171]` `[trigger: 无官煞祸]` `[factor_trigger: wu_guansha_huo AND xingji_aowu]` `[role: 条件分支]` 若无官煞制合，主人性急傲物，刑妻克子。 → 《三命通会》卷八#六丁日丙午时
  - `[ns_smth_08_172]` `[trigger: 有制贵显]` `[factor_trigger: youzhi_guixian AND wu_guan_huo]` `[role: 总结]` 若无官煞祸相寻，有制方成贵显。 → 《三命通会》卷八#六丁日丙午时"""
    normalized_text_zh: str = """"""
    subject: str = "六丁日丙午时断：羊刃帝旺与劫财同宫"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_ding', 'bazi_semantic', 'bazi_state_yangren_3', 'bazi_semantic', 'bazi_relation_jiecai', 'bazi_semantic', 'bazi_state_factor_210', 'bazi_semantic', 'hour_branch_wu', 'bazi_semantic', 'bazi_condition_factor_75', 'bazi_semantic', 'source_ref', 'rel_smth_08_127', 'yangren_diwang', 'rel_smth_08_128', 'jiecai_tonggong', 'rel_smth_08_129', 'youguansha_zhi', 'evi_smth_08_127', 'yangren_diwang', 'rule_diwang3', 'evi_smth_08_128', 'jiecai_tonggong', 'rule_tonggong', 'evi_smth_08_129', 'guansha_zhiren', 'rule_zhiren2', 'map_smth_08_085', 'map_smth_08_086']
    
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
        l1_anchor="smth_v1.0.0_六丁日丙午时断_羊刃帝旺与劫财同宫_001_L1",
    )
    version: str = "1.0.0"
