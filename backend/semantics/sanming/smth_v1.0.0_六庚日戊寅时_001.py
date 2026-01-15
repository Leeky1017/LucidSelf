"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339447
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
    semantic_id="smth_v1.0.0_六庚日戊寅时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六庚日戊寅时(SemanticEntry):
    """
    - 原文（source_text）：
  六庚日生时戊寅，火生金绝福高人。月通从革或秋降，却做皇家柱石臣。
  庚日戊寅时，火生金绝。庚以丙为鬼，戊为倒食。寅上有明戊、合癸化火，庚金气绝。若不通金旺月...
    """
    
    original_text: str = """- 原文（source_text）：
  六庚日生时戊寅，火生金绝福高人。月通从革或秋降，却做皇家柱石臣。
  庚日戊寅时，火生金绝。庚以丙为鬼，戊为倒食。寅上有明戊、合癸化火，庚金气绝。若不通金旺月，无救助者，夭贱贫下。巳月，庚长生，丙健旺，身鬼俱强；运行西方，勇暴，武贵。申酉丑戌月，金火合局，化鬼为官，更得身强运，贵。

- 分字分词释义：
  - **火生金绝**：寅中藏丙火（煞），长生；庚金在寅为绝地。故云“火生（旺）金绝”。
  - **倒食**：戊土为偏印（枭神）。
  - **从革**：金之正格，或指金旺之月。

- **规范化释义（primary_lang_explained）**：
  六庚日出生于戊寅时，七煞丙火在寅长生，日主庚金在寅绝地，煞旺身绝。若生于秋月（从革）或四季土月，日主身强，能任七煞，化煞为权，主大贵（柱石臣）。若不通金气，身弱煞重，又无救助，主夭贱贫下。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Geng Days with Wu-Yin Hour":

  - Fire born Metal extinct—Bing Fire Seven-Killing at Yin is at longevity; Geng Metal at Yin is in extinction; Wu Earth Partial Seal reveals.
  - If monthly qi connects to Metal reformation (autumn) or descends in autumn, becomes pillar-stone minister of the imperial family.
  - Without Metal-prosperous monthly qi and no rescue, indicates early death poverty and low status.
  - Key: Extinction meeting life (Seal generates); killing-seal mutual generation transforms killing into authority.

- 核心要点：
  - **绝处逢生**：庚绝于寅，但有时上戊土相生。
  - **煞印相生**：寅中丙火生戊土，戊土生庚金，格局有情。
  - **身旺**：关键在身旺，身弱则被煞克。

- 详细解说：
  此格极具张力。寅为火土长生之地，丙戊同宫。戊土偏印透干，坐长生，生身有力。虽然庚金绝于寅，但“绝处逢生”（印生）。若日主有根（申酉），或生于秋月，则成“煞印相生”或“食神制煞”（若有壬水）之贵格。若身太弱，则戊土亦难生金（土多金埋或火多土焦），反受其害。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_057]` `[trigger: 火生金绝]` `[factor_trigger: huosheng_jinjue AND fu_gaoren]` `[role: 主干]` 六庚日生时戊寅，火生金绝福高人。 → 《三命通会》卷九#六庚日戊寅时
  - `[ns_smth_09_058]` `[trigger: 月通从革]` `[factor_trigger: yue_tong_congge AND huangjia_zhushi]` `[role: 主干依赖]` 月通从革或秋降，却做皇家柱石臣。 → 《三命通会》卷九#六庚日戊寅时
  - `[ns_smth_09_059]` `[trigger: 不通无救]` `[factor_trigger: butong_wujiu AND yaojian_pinxia]` `[role: 条件分支]` 若不通金旺月，无救助者，夷贱贫下。 → 《三命通会》卷九#六庚日戊寅时
  - `[ns_smth_09_060]` `[trigger: 化鬼为官]` `[factor_trigger: huagui_weiguan AND gui]` `[role: 总结]` 金火合局，化鬼为官，更得身强运，贵。 → 《三命通会》卷九#六庚日戊寅时"""
    normalized_text_zh: str = """"""
    subject: str = "六庚日戊寅时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_geng', 'bazi_semantic', 'bazi_state_fire_metal', 'bazi_semantic', 'bazi_relation_factor_121', 'bazi_semantic', 'bazi_state_factor_272', 'bazi_semantic', 'hour_branch_yin', 'bazi_semantic', 'bazi_condition_metal_4', 'bazi_semantic', 'source_ref', 'rel_smth_09_043', 'huosheng_jinjue', 'rel_smth_09_044', 'shayin_xiangsheng', 'rel_smth_09_045', 'tong_jinwang_yue', 'evi_smth_09_043', 'huosheng_jinjue', 'rule_huosheng_jinjue1', 'evi_smth_09_044', 'tong_jinwang_yue', 'rule_congge_qiujiang1', 'evi_smth_09_045', 'zhushi_chen', 'rule_zhushi_chen1', 'map_smth_09_029', 'map_smth_09_030']
    
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
        l1_anchor="smth_v1.0.0_六庚日戊寅时_001_L1",
    )
    version: str = "1.0.0"
