"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339600
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
    semantic_id="smth_v1.0.0_六辛日戊戌时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六辛日戊戌时(SemanticEntry):
    """
    - 原文（source_text）：
  六辛日生时戊戌，印绶生身坐禄堂。有托福人难靠祖，不通月气是平常。
  辛日戊戌时，禄同印堂同居。辛以戌为禄堂，戌上有明戊为印绶；以丙、丁为官，戌上戊土正位，丙...
    """
    
    original_text: str = """- 原文（source_text）：
  六辛日生时戊戌，印绶生身坐禄堂。有托福人难靠祖，不通月气是平常。
  辛日戊戌时，禄同印堂同居。辛以戌为禄堂，戌上有明戊为印绶；以丙、丁为官，戌上戊土正位，丙、丁火局。若有倚托通月气者，难为祖业。不通，平常。

- 分字分词释义：
  - **禄堂**：此处“戌为禄堂”恐有误，辛禄在酉。戌为金之余气（西方），或指辛金冠带位（戌）。古法有时以戌为辛之“印库”或“火库”。原文可能指“印绶之禄”（戊禄在巳，旺午，戌为墓？）。或指“戌为戊土之禄”（戊禄在巳，戌非禄）。存疑。可能指辛金在戌得地（冠带）。
  - **丙丁火局**：戌为火库。

- **规范化释义（primary_lang_explained）**：
  六辛日出生于戊戌时，戊土正印透出，坐戌土厚地（印绶有力），生助日主。戌为火库（官煞库）。若日主有倚托通月气，虽不靠祖业，亦能白手起家。若不通月气，平常之命。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Xin Days with Wu-Xu Hour":

  - Seal generates body sitting Salary Hall—Wu Earth Direct Seal reveals sitting on Xu Earth, printing prosperous.
  - With support blessed person difficult to rely on ancestors; without monthly qi connection is ordinary.
  - Xu is Fire treasury; if connecting monthly qi with support, can start from scratch achieving success.
  - Key: Seal pattern fears dry Earth brittle Metal; requires Water moistening for proper generation.

- 核心要点：
  - **印绶格**：戊土生身，喜官煞生印。
  - **燥土脆金**：戌为燥土，不生金反脆金，喜水润。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_137]` `[trigger: 印纶生身]` `[factor_trigger: yinshou_shengshen AND zuo_lutang]` `[role: 主干]` 六辛日生时戊戌，印纶生身坐禄堂。 → 《三命通会》卷九#六辛日戊戌时
  - `[ns_smth_09_138]` `[trigger: 有托难靠祖]` `[factor_trigger: youtuo_nankaozhu AND butong_pingchang]` `[role: 主干依赖]` 有托福人难靠祖，不通月气是平常。 → 《三命通会》卷九#六辛日戊戌时
  - `[ns_smth_09_139]` `[trigger: 印纶旺相]` `[factor_trigger: yinshou_wangxiang AND shengzhu_jin]` `[role: 条件分支]` 辛以戌为禄堂，戌上有明戊为印纶。 → 《三命通会》卷九#六辛日戊戌时
  - `[ns_smth_09_140]` `[trigger: 通月气吉]` `[factor_trigger: tongyueqi_ji AND youtuo]` `[role: 总结]` 若有倚托通月气者，难为祖业。不通，平常。 → 《三命通会》卷九#六辛日戊戌时"""
    normalized_text_zh: str = """"""
    subject: str = "六辛日戊戌时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_xin', 'bazi_semantic', 'bazi_state_factor_303', 'bazi_semantic', 'bazi_relation_earth_metal', 'bazi_semantic', 'bazi_state_factor_304', 'bazi_semantic', 'hour_branch_xu', 'bazi_semantic', 'bazi_condition_water', 'bazi_semantic', 'source_ref', 'rel_smth_09_103', 'yinshou_shengshen', 'rel_smth_09_104', 'zaotu_cuijin', 'rel_smth_09_105', 'tong_yueqi_jian_shui', 'evi_smth_09_103', 'yinshou_shengshen', 'rule_yinshou_shengshen1', 'evi_smth_09_104', 'zaotu_cuijin', 'rule_zaotu_cuijin1', 'evi_smth_09_105', 'nankao_zhuye', 'rule_nankao_zhuye1', 'map_smth_09_069', 'map_smth_09_070']
    
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
        l1_anchor="smth_v1.0.0_六辛日戊戌时_001_L1",
    )
    version: str = "1.0.0"
