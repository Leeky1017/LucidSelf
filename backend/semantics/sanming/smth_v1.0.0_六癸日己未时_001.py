"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339681
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
    semantic_id="smth_v1.0.0_六癸日己未时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六癸日己未时(SemanticEntry):
    """
    - 原文（source_text）：
  六癸日生时癸未，鬼旺身衰福不齐。月气不通无救助，平常衣禄有相亏。
  癸日己未时，鬼旺身衰。癸以己为鬼，未上明暗二己得坐专位，癸水无气，浑浊不清，反复成败，若...
    """
    
    original_text: str = """- 原文（source_text）：
  六癸日生时癸未，鬼旺身衰福不齐。月气不通无救助，平常衣禄有相亏。
  癸日己未时，鬼旺身衰。癸以己为鬼，未上明暗二己得坐专位，癸水无气，浑浊不清，反复成败，若通月制又不通水气者，平常。

- 分字分词释义：
  - **鬼旺身衰**：己土七煞透出，未为煞库（且藏己土），煞旺；癸水在未为墓地（或养地？癸墓在辰，未为杀地），身衰。
  - **专位**：未为己土本气（一说土旺于未）。

- **规范化释义（primary_lang_explained）**：
  六癸日出生于己未时，己土七煞透干且得地，煞重身轻。癸水无气，格局浑浊。若不通身旺月气，又无制伏（食伤），主平常甚至贫贱。若有制伏，或身旺，方许富贵。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Gui Days with Ji-Wei Hour":

  - Ghost prosperous body declining fortune not complete—Ji Earth Seven-Killing reveals; Wei hides bright-dark two Ji sitting exclusive position.
  - If monthly qi not connected no rescue-help, ordinary clothing-salary has mutual loss.
  - Gui Water no qi, murky unclear, reversals and successes-failures; if connecting monthly control and not connecting Water qi, ordinary.
  - Key: Seven-Killing heavy body light needs control-transformation; body strong or with control can achieve.

- 核心要点：
  - **七煞格**：己未煞重。
  - **身弱**：忌煞攻身。
  - **喜制化**：喜金水木。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_229]` `[trigger: 鬼旺身衰]` `[factor_trigger: guiwang_shenshuai AND fu_buqi]` `[role: 主干]` 六癸日生时己未，鬼旺身衰福不齐。 → 《三命通会》卷九#六癸日己未时
  - `[ns_smth_09_230]` `[trigger: 月气不通]` `[factor_trigger: yueqi_butong AND wu_jiuzhu]` `[role: 主干依赖]` 月气不通无救助，平常衣禄有相亏。 → 《三命通会》卷九#六癸日己未时
  - `[ns_smth_09_231]` `[trigger: 明暗二己]` `[factor_trigger: ming_an_erji AND zhuanwei]` `[role: 条件分支]` 未上明暗二己得坐专位，癸水无气，浑浊不清，反复成败。 → 《三命通会》卷九#六癸日己未时
  - `[ns_smth_09_232]` `[trigger: 通月制方吉]` `[factor_trigger: tongyue_zhi_fangji AND you_zhifu]` `[role: 总结]` 若通月制又不通水气者，平常。若有制伏，身旺，方吉。 → 《三命通会》卷九#六癸日己未时"""
    normalized_text_zh: str = """"""
    subject: str = "六癸日己未时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_gui', 'bazi_semantic', 'bazi_state_factor_319', 'bazi_semantic', 'bazi_relation_factor_130', 'bazi_semantic', 'bazi_state_factor_320', 'bazi_semantic', 'hour_branch_wei', 'bazi_semantic', 'bazi_condition_water_2', 'bazi_semantic', 'source_ref', 'rel_smth_09_166', 'guiwang_shenshuai', 'rel_smth_09_167', 'tong_shuiqi_youzhi', 'rel_smth_09_168', 'yueqi_butong_wuzhu', 'evi_smth_09_166', 'guiwang_shenshuai', 'rule_guiwang_shenshuai1', 'evi_smth_09_167', 'hunzhuo_buqing', 'rule_hunzhuo_fanfu1', 'evi_smth_09_168', 'pingchang_yilu', 'rule_pingchang_yilu1', 'map_smth_09_111', 'map_smth_09_112']
    
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
        l1_anchor="smth_v1.0.0_六癸日己未时_001_L1",
    )
    version: str = "1.0.0"
