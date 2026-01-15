"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339581
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
    semantic_id="smth_v1.0.0_六辛日丙申时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六辛日丙申时(SemanticEntry):
    """
    - 原文（source_text）：
  辛日生时遇丙申，月通金火转精神。化成金水逢金地，聚福能为富贵人。
  辛日丙申时，丙辛化水，申上长生。若月通巳酉丑金气者，精神秀丽，文章聚福。通火气旺、有倚托...
    """
    
    original_text: str = """- 原文（source_text）：
  辛日生时遇丙申，月通金火转精神。化成金水逢金地，聚福能为富贵人。
  辛日丙申时，丙辛化水，申上长生。若月通巳酉丑金气者，精神秀丽，文章聚福。通火气旺、有倚托者，贵。辛酉、辛未最妙，不成化象。申上官星无气，平常衣禄。

- 分字分词释义：
  - **丙辛化水**：丙辛合化水（化气格）。
  - **申上长生**：水长生在申，化象得地。
  - **金火转精神**：若不化，丙火官星与辛金日主，金火辉煌。

- **规范化释义（primary_lang_explained）**：
  六辛日出生于丙申时，丙辛相合。若生于申子辰水局或冬月，化水成功，且申为水长生，主秀丽文章。若生于金月（巳酉丑），金水相涵，亦贵。若生于火月，官星旺，有倚托（身旺），亦贵。若不化，丙官在申无气（病地），平常。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Xin Days with Bing-Shen Hour":

  - Month connecting Metal-Fire turns spirit—Bing-Xin combine transforming Water; Shen is Water's Long Life position.
  - If transforming into Metal-Water encountering Metal land, gathering fortune can become wealthy noble person.
  - If month connects Si-You-Chou Metal qi, spirit elegant literary, article gathers fortune; connecting Fire qi prosperous with support, noble.
  - Key: Transformation pattern requires support; non-transformation sees Official star weak at Shen, ordinary fortune.

- 核心要点：
  - **化气格**：丙辛化水，喜水旺金生。
  - **正官格**：不化，看官星力度。
  - **归禄**：申为庚禄，辛之旺地（帝旺）。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_129]` `[trigger: 丙辛化水]` `[factor_trigger: bingxin_huashui AND zhuan_jingshen]` `[role: 主干]` 辛日生时遇丙申，月通金火转精神。 → 《三命通会》卷九#六辛日丙申时
  - `[ns_smth_09_130]` `[trigger: 化成金水]` `[factor_trigger: huacheng_jinshui AND feng_jindi]` `[role: 主干依赖]` 化成金水逢金地，聚福能为富贵人。 → 《三命通会》卷九#六辛日丙申时
  - `[ns_smth_09_131]` `[trigger: 通金气者]` `[factor_trigger: tong_jinqi_zhe AND jingshen_xiuli]` `[role: 条件分支]` 若月通巳酉丑金气者，精神秀丽，文章聚福。 → 《三命通会》卷九#六辛日丙申时
  - `[ns_smth_09_132]` `[trigger: 官星无气]` `[factor_trigger: guanxing_wuqi AND pingchang_yilu]` `[role: 总结]` 申上官星无气，平常衣禄。 → 《三命通会》卷九#六辛日丙申时"""
    normalized_text_zh: str = """"""
    subject: str = "六辛日丙申时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_xin', 'bazi_semantic', 'bazi_state_bing_xin_water', 'bazi_semantic', 'bazi_relation_metal_fire_2', 'bazi_semantic', 'bazi_state_factor_300', 'bazi_semantic', 'hour_branch_shen', 'bazi_semantic', 'bazi_condition_metal_water_2', 'bazi_semantic', 'source_ref', 'rel_smth_09_097', 'bingxin_huashui', 'rel_smth_09_098', 'bingxin_huashui', 'rel_smth_09_099', 'jinhuo_zhuanshen', 'evi_smth_09_097', 'bingxin_huashui', 'rule_bingxin_huashui1', 'evi_smth_09_098', 'wenzhang_jufu', 'rule_wenzhang_jufu1', 'evi_smth_09_099', 'jinhuo_zhuanshen', 'rule_jinhuo_zhuanshen1', 'map_smth_09_065', 'map_smth_09_066']
    
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
        l1_anchor="smth_v1.0.0_六辛日丙申时_001_L1",
    )
    version: str = "1.0.0"
