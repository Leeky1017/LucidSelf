"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412671
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
    semantic_id="smth_v1.0.0_时上偏财与晚年机会_001",
    book_id="sanming",
    engine_id="bazi"
)
class 时上偏财与晚年机会(SemanticEntry):
    """
    - **原文（source_text）**：

  时上偏财：《喜忌篇》云：时上偏财，怕逢兄弟。如甲日见戊辰或甲戌时之例。喜见辛官、壬癸生助，忌庚煞、乙劫。柱中不宜再见戊己。若身太旺，运东方寅卯则失财...
    """
    
    original_text: str = """- **原文（source_text）**：

  时上偏财：《喜忌篇》云：时上偏财，怕逢兄弟。如甲日见戊辰或甲戌时之例。喜见辛官、壬癸生助，忌庚煞、乙劫。柱中不宜再见戊己。若身太旺，运东方寅卯则失财，余干例推。此与时上偏官格相似，只要一位，不宜多逢，天元透出为妙，支内所藏次之。柱有官印相助，日主健旺，便作好命看。大怕年月冲破，兄弟辈出，则福气不全。古诗云：时上偏财冲最忌，兄弟之辈皆为畏，喜行身旺官禄乡，别无透出方为贵。

- 分字分词释义：

  - **时上偏财**：偏财落在时柱，如甲日见戊辰、甲戌时等，偏重晚年、子息与身外机缘。
  - **怕逢兄弟**：兄弟比劫来分夺时上偏财，等于“晚年之财被同辈分食”，故为大忌。
  - **喜辛官、壬癸生助**：以官星、印星生扶偏财，使其有序流通而不至于乱耗。
  - **只要一位，不宜多逢**：时上偏财以一位为佳，多则成杂，易乱心志。

- **规范化释义（primary_lang_explained）**：

  时上偏财，多主中晚年出现的偏财机会：投资、合作、子息或外缘带来的项目等。原文强调几点：

  - 若有官印相生、身势健旺，则此类机会可化为稳定的事业或长期收益；
  - 若兄弟比劫过多，或年月来冲时支，则多应在“晚年财来财去、家中纷争”的场景中。

- 核心要点：

  - 时上偏财看**后半生的偏财与子息相关机缘**。
  - 喜官印相助、身旺能任；忌兄弟比劫冲夺与多重偏财叠见。
  - 一位为妙，多则杂乱，易劳心劳力、财不聚。

- 详细解说：

  结合现代生活，可以把时上偏财理解为：在人生后半段，通过创业合作、子女事业、跨界转型等方式获得的非传统收入。若命局与行运配合得宜，这些偏财往往能在原有基础上再造第二春；若结构失衡，则可能体现为：

  - 反复投入合作项目，收益不稳；
  - 与兄弟、朋友之间因钱生隙；
  - 晚年为子女、亲友之事频频操心财务。

- **校勘与字词辨析（双语）**：

  - 原文“喜行身旺官禄乡，别无透出方为贵”一句，本稿理解为：以身旺为前提，行官禄之运而不再额外透出偏财，反而能稳中有升；偏财宜简不宜繁。
  - **English**：
    - Indirect wealth should be simple not complex; principle noted.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_125]` `[trigger: 时上偏财]` `[factor_trigger: shizhu_piancai AND wannian_jihui]` `[role: 主干]` 时上偏财，怕逢兄弟。如甲日见戊辰或甲戌时之例。 → 《三命通会》卷六#时上偏财
  - `[ns_smth_06_126]` `[trigger: 只要一位]` `[factor_trigger: piancai_yiwei AND buyiduofeng]` `[role: 主干依赖]` 只要一位，不宜多逢，天元透出为妙。 → 《三命通会》卷六#时上偏财
  - `[ns_smth_06_127]` `[trigger: 兄弟辈出]` `[factor_trigger: xiongdi_beichu AND fuqi_buquan]` `[role: 条件分支]` 大怕年月冲破，兄弟辈出，则福气不全。 → 《三命通会》卷六#时上偏财
  - `[ns_smth_06_128]` `[trigger: 身旺官禄乡]` `[factor_trigger: shenwang_guanlu AND biewutouchu]` `[role: 总结]` 喜行身旺官禄乡，别无透出方为贵。 → 《三命通会》卷六#时上偏财"""
    normalized_text_zh: str = """"""
    subject: str = "时上偏财与晚年机会"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_piancai_marker_1', 'bazi_semantic', 'bazi_structure_hour_pillar_piancai_combo', 'bazi_semantic', 'bazi_state_piancai', 'bazi_semantic', 'bazi_state_state_1', 'bazi_semantic', 'bazi_condition_factor_190', 'bazi_semantic', 'bazi_condition_factor_191', 'bazi_semantic', 'source_ref', 'rel_smth_06_121', 'shishang_piancai_presence', 'rel_smth_06_122', 'piancai_shuliang', 'rel_smth_06_123', 'nianyue_chongpo_risk', 'evi_smth_06_121', 'shishang_piancai_presence', 'rule_shishang', 'evi_smth_06_122', 'piancai_shuliang', 'rule_yiwei', 'evi_smth_06_123', 'nianyue_chongpo_risk', 'rule_chongpo', 'map_smth_06_081', 'map_smth_06_082']
    
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
        l1_anchor="smth_v1.0.0_时上偏财与晚年机会_001_L1",
    )
    version: str = "1.0.0"
