"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.436493
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
    semantic_id="smth_v1.0.0_旺夫克子格与福力偏向_001",
    book_id="sanming",
    engine_id="bazi"
)
class 旺夫克子格与福力偏向(SemanticEntry):
    """
    - 原文（source_text）：

  旺夫克子。

  夫女人有旺夫伤子者何？此法皆时上推之。时为归宿之地，夫子二星，引归于时；夫星生旺，子星衰败是也。如一命：丙戌、丙申、丁巳、辛亥。丁坐巳，自...
    """
    
    original_text: str = """- 原文（source_text）：

  旺夫克子。

  夫女人有旺夫伤子者何？此法皆时上推之。时为归宿之地，夫子二星，引归于时；夫星生旺，子星衰败是也。如一命：丙戌、丙申、丁巳、辛亥。丁坐巳，自旺，以壬水为夫，时上乃是夫星临官之地，月支申金，乃夫星长生之地。以辛金为财，七月金旺，二丙相比，皆坐夫之财印，故主夫聪秀富贵。丁以戊为子息之垣，引至时上见亥，亥中甲木能克戊土，乃子星被克而难得也，故主旺夫伤子，余仿此推。

- 分字分词释义：

  - **旺夫克子**：夫星极旺、子星受损，福力偏向伴侣一端，而对子嗣一端不利。
  - **时为归宿之地**：时柱主晚年、结果与归宿，是观察夫子最终落点的关键。
  - **夫子二星引归于时**：夫星、子星皆要看其在时柱是否得生、得地，以定“终局”。
  - **夫星生旺、子星衰败**：夫星在长生、临官、帝旺等地，而子星落绝地、被克制，形成福力偏向。

- **规范化释义（primary_lang_explained）**：

  本节说明一种“对夫有利、对子不利”的格局：

  - 通过时柱来看夫星、子星最终所到之处；
  - 若夫星在时上得长生、临官、帝旺，且有财印生扶，则多主伴侣聪秀富贵、事业顺行；
  - 若子星引至时上反落绝地，且再被其他五行克制，则多主子息难得或与子缘薄。

  原例中，夫星壬水在亥时临官，申金为夫之长生之地，又有辛金为财助夫，故夫端兴盛；而子星戊土被亥中甲木所克，故以“伤子”言之。

- **完整对等诠释（secondary_lang_full）**：

  In this pattern, the life story leans strongly toward the spouse line. The time pillar, which symbolises late life and overall outcome, gives the spouse star a place of strength – positions such as Changsheng, Lin'guan or Diwang – and further supports it with Wealth and Seal. Under such a structure, the partner is more likely to receive resources, opportunities, and emotional focus, and the shared path of the couple tends to become the centre of gravity in the native's life.

  By contrast, the child star is led into a place of depletion or active control at that same time pillar. This may show up as fewer children, delayed childbearing, physical or emotional distance, or simply a life in which there is less room to pour energy into parenting. Rather than predicting concrete harm, the chart is better read as pointing out an imbalance: if one does nothing, it is easy to pour most strength into the spouse and joint endeavours, while the child line quietly bears the cost. With awareness, the native can consciously re-balance time, care, and practical support so that the "favouring of the spouse" does not turn into a long-term deficit for the bond with children.

- 核心要点：

  - 以时柱为归宿，以夫子二星的旺衰配合来判断福力偏向。
  - 夫星旺、子星弱，则易见“旺夫克子”之象。
  - 此“克”指结构上的不利倾向，并非必然的现实悲剧。

- 详细解说：

  1. **为什么重看时柱**  
     - 时为晚景与归宿，夫子星最终在时上如何落位，往往决定一生的重心；  
     - 若夫星在时得旺地，表示伴侣在命主一生后段仍是重要支柱。

  2. **夫星与子星的此消彼长**  
     - 当资源（财印、行运）主要流向夫星，而子星落绝地或受克时，往往意味着家庭资源更多投入到伴侣与其事业；  
     - 子女一端可能表现为数量偏少、相处疏离、或在教育资源分配上的不足。

  3. **现代阅读方式**  
     - 不必将“旺夫克子”视为宿命，而可理解为：命主的关系重心偏向伴侣与两人共同事业；  
     - 若有此结构，可有意识地在亲子关系上投入更多时间与照顾，以平衡命局暗示的偏向。

- 校勘与字词辨析：

  - “伤子”与“克子”在本节中统一理解为对子嗣一端较为不利，不作具体灾祸的直接断定。
  - 例命中的行文，本稿以现代标点整理，仅在语序上略作理顺，不改动原意。
  - **English**：
    - Sequence slightly reorganized; original meaning unchanged.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_07_041]` `[trigger: 旺夫克子定义]` `[factor_trigger: wangfu_kezi_ge]` `[role: 主干]` 旺夫克子。 → 《三命通会》卷七#旺夫克子
  - `[ns_smth_07_042]` `[trigger: 时为归宿]` `[factor_trigger: shi_wei_guisu AND fuzi_yin_gui]` `[role: 主干依赖]` 时为归宿之地，夫子二星，引归于时；夫星生旺，子星衰败是也。 → 《三命通会》卷七#旺夫克子
  - `[ns_smth_07_043]` `[trigger: 子星被克]` `[factor_trigger: zixing_bei_ke AND nan_de]` `[role: 条件分支]` 丁以戊为子息之垣，引至时上见亥，亥中甲木能克戊土，乃子星被克而难得也。 → 《三命通会》卷七#旺夫克子
  - `[ns_smth_07_044]` `[trigger: 主旺夫伤子]` `[factor_trigger: zhu_wangfu_shangzi]` `[role: 总结]` 故主旺夫伤子，余仿此推。 → 《三命通会》卷七#旺夫克子"""
    normalized_text_zh: str = """"""
    subject: str = "旺夫克子格与福力偏向"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_zi_2', 'bazi_semantic', 'bazi_structure_hour_pillar', 'bazi_semantic', 'bazi_state_factor_353', 'bazi_semantic', 'bazi_state_zi_relation', 'bazi_semantic', 'source_ref', 'rel_smth_07_028', 'fuzi_fuli_fenpei', 'rel_smth_07_029', 'shizhu_guisu', 'rel_smth_07_030', 'qinzi_qinmidu', 'evi_smth_07_028', 'fuzi_fuli_fenpei', 'rule_wangfukezi', 'evi_smth_07_029', 'shizhu_guisu', 'rule_shizhu', 'evi_smth_07_030', 'qinzi_qinmidu', 'rule_zibeike', 'map_smth_07_019', 'map_smth_07_020']
    
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
        l1_anchor="smth_v1.0.0_旺夫克子格与福力偏向_001_L1",
    )
    version: str = "1.0.0"
