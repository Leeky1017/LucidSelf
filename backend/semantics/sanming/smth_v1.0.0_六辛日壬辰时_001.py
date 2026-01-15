"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339547
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
    semantic_id="smth_v1.0.0_六辛日壬辰时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六辛日壬辰时(SemanticEntry):
    """
    - 原文（source_text）：
  六辛日生时壬辰，伤官伤尽倍精神。四柱火虚防克害，九流技艺卜医人。
  辛日壬辰时，暗金沉水底。辛用丙为官，壬为伤官，辰水库，丙辛无气，壬水合局。若年月透丙，是...
    """
    
    original_text: str = """- 原文（source_text）：
  六辛日生时壬辰，伤官伤尽倍精神。四柱火虚防克害，九流技艺卜医人。
  辛日壬辰时，暗金沉水底。辛用丙为官，壬为伤官，辰水库，丙辛无气，壬水合局。若年月透丙，是伤官见官，刑祸百端，为人气高夸大，秀而不实。不通月气、无倚托者，为人反复成败，为医卜艺术。柱有木火身旺，行东南运、贵。

- 分字分词释义：
  - **伤官伤尽**：壬水伤官透干，辰为水库，伤官旺。若四柱无官星（丙火），为伤官伤尽，主贵（倍精神）。
  - **暗金沉水底**：辛金生壬水，水多金沉。
  - **火虚**：官星无气或受伤。

- **规范化释义（primary_lang_explained）**：
  六辛日出生于壬辰时，壬水伤官透出，辰为水库，伤官势旺。若四柱无官星（火虚），构成伤官伤尽格，精神倍增，主贵。若见官星而无气，则为伤官见官，主克害。若不通月气身弱，多为九流技艺、医卜之人。若身旺有财（木火），行东南运，主贵。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Xin Days with Ren-Chen Hour":

  - Hurting Official hurts completely, spirit doubled—Ren Water Hurting Official reveals; Chen is Water treasury; if no Fire (Official), pure pattern.
  - If four pillars Fire empty, guard against harm; nine-stream techniques divination-medicine person.
  - If year-month reveal Bing, is Hurting Official seeing Official, punishment disasters hundred-fold, character arrogant boastful, elegant but unreal.
  - Key: Hurting Official hurts completely fears seeing Official; body strong with Wealth traveling southeast indicates nobility.

- 核心要点：
  - **伤官伤尽**：喜身旺，忌见官。
  - **水多金沉**：忌金寒水冷，喜火土（但在伤官伤尽格中，火为忌，土为喜）。
  - **墓库**：辰为墓库。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_113]` `[trigger: 伤官伤尽]` `[factor_trigger: shangguan_shangjin AND bei_jingshen]` `[role: 主干]` 六辛日生时壬辰，伤官伤尽倍精神。 → 《三命通会》卷九#六辛日壬辰时
  - `[ns_smth_09_114]` `[trigger: 火虚防克害]` `[factor_trigger: huoxu_fang_kehai AND jiuliu_jiyi]` `[role: 主干依赖]` 四柱火虚防克害，九流技艺卜医人。 → 《三命通会》卷九#六辛日壬辰时
  - `[ns_smth_09_115]` `[trigger: 伤官见官]` `[factor_trigger: shangguan_jianguan AND xing_huo_baidan]` `[role: 条件分支]` 若年月透丙，是伤官见官，刑祸百端。 → 《三命通会》卷九#六辛日壬辰时
  - `[ns_smth_09_116]` `[trigger: 身旺行运贵]` `[factor_trigger: shenwang_xingyun_gui AND dongnan_yun]` `[role: 总结]` 柱有木火身旺，行东南运，贵。 → 《三命通会》卷九#六辛日壬辰时"""
    normalized_text_zh: str = """"""
    subject: str = "六辛日壬辰时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_xin', 'bazi_semantic', 'bazi_state_shangguan_10', 'bazi_semantic', 'bazi_relation_metal_water', 'bazi_semantic', 'bazi_state_factor_293', 'bazi_semantic', 'hour_branch_chen', 'bazi_semantic', 'bazi_condition_factor_127', 'bazi_semantic', 'source_ref', 'rel_smth_09_085', 'shangguan_shangjin', 'rel_smth_09_086', 'shangguan_shangjin', 'rel_smth_09_087', 'shangguan_shangjin', 'evi_smth_09_085', 'shangguan_shangjin', 'rule_shangguan_shangjin1', 'evi_smth_09_086', 'shangguan_jian_guan', 'rule_shangguan_jianguan1', 'evi_smth_09_087', 'jiuliu_jiyi', 'rule_jiuliu_jiyi1', 'map_smth_09_057', 'map_smth_09_058']
    
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
        l1_anchor="smth_v1.0.0_六辛日壬辰时_001_L1",
    )
    version: str = "1.0.0"
