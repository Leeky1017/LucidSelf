"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339508
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
    semantic_id="smth_v1.0.0_六辛日戊子时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六辛日戊子时(SemanticEntry):
    """
    - 原文（source_text）：
  六辛日生时戊子，印绶学堂坐食神。不见丙丁同午破，必是荣华贵显人。
  辛日戊子时，六阴朝阳。辛金子上长生学堂。辛以戊为印，癸为食，时上明戊暗癸，柱中不见丙丁午...
    """
    
    original_text: str = """- 原文（source_text）：
  六辛日生时戊子，印绶学堂坐食神。不见丙丁同午破，必是荣华贵显人。
  辛日戊子时，六阴朝阳。辛金子上长生学堂。辛以戊为印，癸为食，时上明戊暗癸，柱中不见丙丁午字，冲开；通身旺月，大贵；犯者不贵。不通月气，通运，亦贵。

- 分字分词释义：
  - **六阴朝阳**：辛为阴金，子为阴水，子中癸水动丙火（官），朝向巳火（阳），名六阴朝阳。
  - **印绶学堂**：戊为印，子为辛金长生之地（学堂）。
  - **食神**：子中癸水为食神。

- **规范化释义（primary_lang_explained）**：
  六辛日出生于戊子时，为六阴朝阳格（或印绶食神格）。辛金在子长生，且戊土印绶生身，癸水食神吐秀。若柱中不见丙丁官煞及午字冲破子水，且日主身旺，主大贵。若犯丙丁午字，则破格不贵。若不通月气，行运相助亦贵。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Xin Days with Wu-Zi Hour":

  - Seal-Academy sitting Eating God; Six-Yin Facing Yang pattern—Xin Metal at Zi is in Long Life Academy position.
  - Wu Earth Seal reveals with Gui Water Eating God hidden; if no Bing-Ding-Wu (Official/Killing/clash), definitely a glorious noble prominent person.
  - If passing body-prosperous month, great nobility; violators not noble; without monthly qi but luck connects, also noble.
  - Key: Six-Yin Facing Yang fears filling in (Bing-Ding-Wu); Long Life Academy indicates literary talent.

- 核心要点：
  - **六阴朝阳**：辛日子时，忌填实（丙丁午）。
  - **长生学堂**：辛长生在子，主文章才智。
  - **印食双全**：戊印癸食，秀气。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_097]` `[trigger: 印绶学堂]` `[factor_trigger: yinshou_xuetang AND zuo_shishen]` `[role: 主干]` 六辛日生时戊子，印绶学堂坐食神。 → 《三命通会》卷九#六辛日戊子时
  - `[ns_smth_09_098]` `[trigger: 不见丙丁午]` `[factor_trigger: bujian_bingdingwu AND ronghua_guixian]` `[role: 主干依赖]` 不见丙丁同午破，必是荣华贵显人。 → 《三命通会》卷九#六辛日戊子时
  - `[ns_smth_09_099]` `[trigger: 通身旺月]` `[factor_trigger: tong_shenwang_yue AND dagui]` `[role: 条件分支]` 通身旺月，大贵；犯者不贵。 → 《三命通会》卷九#六辛日戊子时
  - `[ns_smth_09_100]` `[trigger: 不通通运]` `[factor_trigger: butong_tongyun AND yigui]` `[role: 总结]` 不通月气，通运，亦贵。 → 《三命通会》卷九#六辛日戊子时"""
    normalized_text_zh: str = """"""
    subject: str = "六辛日戊子时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_xin', 'bazi_semantic', 'bazi_state_factor_287', 'bazi_semantic', 'bazi_relation_factor_123', 'bazi_semantic', 'bazi_state_factor_288', 'bazi_semantic', 'hour_branch_zi', 'bazi_semantic', 'bazi_condition_bing_ding_wu', 'bazi_semantic', 'source_ref', 'rel_smth_09_073', 'liuyin_chaoyang', 'rel_smth_09_074', 'liuyin_chaoyang', 'rel_smth_09_075', 'shenwang_tongyueqi', 'evi_smth_09_073', 'yinshi_shuangquan', 'rule_yinshi_shuangquan1', 'evi_smth_09_074', 'wubingdingwu', 'rule_wubingdingwu1', 'evi_smth_09_075', 'shenwang_tongyueqi', 'rule_ronghua_guixian1', 'map_smth_09_049', 'map_smth_09_050']
    
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
        l1_anchor="smth_v1.0.0_六辛日戊子时_001_L1",
    )
    version: str = "1.0.0"
