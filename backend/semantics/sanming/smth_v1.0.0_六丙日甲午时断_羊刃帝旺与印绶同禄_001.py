"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157509
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
    semantic_id="smth_v1.0.0_六丙日甲午时断_羊刃帝旺与印绶同禄_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六丙日甲午时断羊刃帝旺与印绶同禄(SemanticEntry):
    """
    - 原文（source_text）：

  六丙日甲午时断。

  六丙日生时甲午，印绶同禄坐羊刃；有官有煞方为贵，岁运冲刃损妻身。丙日甲午时，印禄归垣，丙用甲为印，坐禄乘羊刃。若通火气月者，为人性急...
    """
    
    original_text: str = """- 原文（source_text）：

  六丙日甲午时断。

  六丙日生时甲午，印绶同禄坐羊刃；有官有煞方为贵，岁运冲刃损妻身。丙日甲午时，印禄归垣，丙用甲为印，坐禄乘羊刃。若通火气月者，为人性急傲物，不利妻子。通官煞月者，贵；不通，无官刑冲，平常人。

  丙子日甲午时，子为正官，丙身旺，可化官为贵。若卯戌辰巳年月，印绶有助，高。丑未，杂气财官，水土运，贵。午戌年月，不吉。

  丙寅日甲午时，高，虽印绶有气，却坐建旺羊刃，克妻。行西运官煞，吉；行东运印，凶。寅丑申亥月，大贵。巳酉丑月，合煞，有制，吉。余皆吉。

  丙辰日甲午时，不贵即富。子丒辰亥年月，行北运，贵。酉戌，行金水运，大贵。

  丙午日甲午时，身旺无依。亥子申酉月、年月有癸字，贵。辰戌丑未月，财官有气，吉。

  丙申日甲午时，寅卯辰巳午月，印身俱旺，行北运，大贵。申子辰会官，干透印者大贵。巳酉丑合煞，未戌俱吉。

  丙戌日甲午时，不利子，春夏财官不旺，秋冬官煞混杂，俱平常。辰戌丑未月，行官煞运，大贵。

  丙日甲午时中遇，羊刃须官煞来制；岁运一到则富贵，无官刃旺祸滋多。丙日时逢甲午，羊刃倒戈非细。若无官煞定凶虞，命里带来多愧。刑伤骨肉得亏，官煞制刃发贵。火明木秀印生身，富贵双全之辈。

- 分字分词释义：

  - **羊刃帝旺**：午为丙火帝旺之地，又为羊刃位，主刚强好斗。
  - **印绶同禄**：甲木正印与丙火同在午位，印禄归垣。
  - **羊刃倒戈**：羊刃无制则凶，如倒戈伤主。

- 规范化释义（primary_lang_explained）：

  本节讲「六丙日，甲午时」：

  - 丙火在午为帝旺兼羊刃，甲木正印坐禄于午，形成「印禄归垣」的结构；
  - 羊刃主刚强，若无官煞制合，则性急傲物、不利妻子；
  - 歌诀强调：羊刃须官煞来制，无官刃旺祸滋多。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Bing Days with Jia-Wu Hour":

  - Bing Fire at Wu reaches Emperor-Prosperity combined with Sheep-Blade; Jia Wood Direct Seal sits at fortune position on Wu, forming "seal-fortune unity."
  - Sheep-blade indicates extreme strength; without official-killing control, the person becomes impetuous and arrogant, harming spouse and children.
  - The verse emphasizes: sheep-blade requires official-killing control; without official, blade prosperity brings many misfortunes.

- 核心要点：

  - 本格以「羊刃帝旺」为核心，身极旺。
  - 印绶同禄是优势，但羊刃无制是风险。
  - 需要官煞制刃，方能化险为夷。

- 详细解说：

  1. **羊刃帝旺的特点**  
     - 午为丙火帝旺，日主极旺；羊刃主刚强、好斗；  
     - 若无官煞制合，则性格偏激，容易伤害身边人。

  2. **官煞制刃的必要性**  
     - 羊刃太旺，需要官煞来制约；  
     - 有官煞制刃，则刚柔并济，可成就大贵。

- 校勘与字词辨析：

  - 「倒戈」比喻羊刃无制时反伤日主或伤害他人。
  - 「火明木秀印生身」描述印生身的优良状态。
  - **English**：
    - Describes excellent state of Seal generating body.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_121]` `[trigger: 羊刃帝旺]` `[factor_trigger: yangren_diwang AND zuoyangren]` `[role: 主干]` 六丙日生时甲午，印绶同禄坐羊刃。 → 《三命通会》卷八#六丙日甲午时
  - `[ns_smth_08_122]` `[trigger: 官煞为贵]` `[factor_trigger: guansha_weigui AND fang_wei_gui]` `[role: 主干依赖]` 有官有煞方为贵，岁运冲刃损妻身。 → 《三命通会》卷八#六丙日甲午时
  - `[ns_smth_08_123]` `[trigger: 通官煞月]` `[factor_trigger: tong_guansha_yue AND gui_xian]` `[role: 条件分支]` 通官煞月者，贵；不通，无官刑冲，平常人。 → 《三命通会》卷八#六丙日甲午时
  - `[ns_smth_08_124]` `[trigger: 火明木秀]` `[factor_trigger: huoming_muxiu AND yin_sheng_shen]` `[role: 总结]` 火明木秀印生身。 → 《三命通会》卷八#六丙日甲午时"""
    normalized_text_zh: str = """"""
    subject: str = "六丙日甲午时断：羊刃帝旺与印绶同禄"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_bing', 'bazi_semantic', 'bazi_state_yangren_3', 'bazi_semantic', 'bazi_relation_factor_79', 'bazi_semantic', 'bazi_state_factor_210', 'bazi_semantic', 'hour_branch_wu', 'bazi_semantic', 'bazi_condition_factor_53', 'bazi_semantic', 'source_ref', 'rel_smth_08_091', 'yangren_diwang', 'rel_smth_08_092', 'guansha_zhiren', 'rel_smth_08_093', 'tongguansha_yue', 'evi_smth_08_091', 'yangren_diwang', 'rule_diwang', 'evi_smth_08_092', 'yinxu_tonglu', 'rule_tonglu', 'evi_smth_08_093', 'guansha_zhiren', 'rule_zhiren', 'map_smth_08_061', 'map_smth_08_062']
    
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
        l1_anchor="smth_v1.0.0_六丙日甲午时断_羊刃帝旺与印绶同禄_001_L1",
    )
    version: str = "1.0.0"
