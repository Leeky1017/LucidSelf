"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339498
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
    semantic_id="smth_v1.0.0_六庚日丁亥时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六庚日丁亥时(SemanticEntry):
    """
    - 原文（source_text）：
  六庚日生时丁亥，官星失地自身衰。不通月气难成福，若见魁罡却妙哉。
  庚日丁亥时，庚以甲为财，壬为食，丁为官。亥上丁火无气，壬旺甲生，庚金失地，难任财食。若不...
    """
    
    original_text: str = """- 原文（source_text）：
  六庚日生时丁亥，官星失地自身衰。不通月气难成福，若见魁罡却妙哉。
  庚日丁亥时，庚以甲为财，壬为食，丁为官。亥上丁火无气，壬旺甲生，庚金失地，难任财食。若不通身旺月，不能成福；通月气、有阴土扶身者，发财。官星有助，稍贵。庚戌、庚辰此二日魁罡，不宜财官生旺；时逢丁亥，反贵。

- 分字分词释义：
  - **官星失地**：丁火官星在亥为胎地（受壬水合克），无气。
  - **自身衰**：庚金在亥为病地，身弱。
  - **魁罡妙**：魁罡日（庚辰、庚戌）喜身旺，忌财官旺。丁亥时官星无气，反而符合魁罡喜忌（但也需看具体组合，一般魁罡忌见官，丁亥官星无力，故不忌？或指亥中壬水合丁，去官留煞？原文意指魁罡忌官旺，此时官衰，反吉）。

- **规范化释义（primary_lang_explained）**：
  六庚日出生于丁亥时，丁火官星在亥无气，日主庚金亦在病地，身官两衰。若不通身旺月气，难成福。若通月气，且有己土（阴土）扶身，可发财（食神生财）。若是庚辰、庚戌魁罡日，因魁罡忌官旺，丁亥时官星衰弱，反主贵。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Geng Days with Ding-Hai Hour":

  - Official star lost ground, self also declining—Ding Fire Official at Hai has no qi; Geng Metal at Hai is in sick position.
  - Without passing monthly qi, difficult to achieve fortune; if meeting Kui-Gang (Geng-Chen/Geng-Xu), turns wonderful instead.
  - If passing monthly qi with Yin Earth supporting body, can develop wealth; Official star with assistance, slightly noble.
  - Key: Body-Official both weak requires support; Kui-Gang days fear prosperous Official, here Official weak turns auspicious.

- 核心要点：
  - **官印格/食神格**：丁官透，亥含壬甲。
  - **身弱**：亥泄金气，重在帮身。
  - **魁罡特例**：魁罡忌官，官衰反吉。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_093]` `[trigger: 官星失地]` `[factor_trigger: guanxing_shidi AND zishen_shuai]` `[role: 主干]` 六庚日生时丁亥，官星失地自身衰。 → 《三命通会》卷九#六庚日丁亥时
  - `[ns_smth_09_094]` `[trigger: 不通难成福]` `[factor_trigger: butong_nanchengfu AND kuigang_miaozai]` `[role: 主干依赖]` 不通月气难成福，若见魁罡却妙哉。 → 《三命通会》卷九#六庚日丁亥时
  - `[ns_smth_09_095]` `[trigger: 通月气印土]` `[factor_trigger: tongyueqi_yintu AND facai]` `[role: 条件分支]` 通月气、有阴土扶身者，发财。 → 《三命通会》卷九#六庚日丁亥时
  - `[ns_smth_09_096]` `[trigger: 魁罡反贵]` `[factor_trigger: kuigang_fangui AND guanshuai_ji]` `[role: 总结]` 庚戌、庚辰此二日魁罡，时逢丁亥，反贵。 → 《三命通会》卷九#六庚日丁亥时"""
    normalized_text_zh: str = """"""
    subject: str = "六庚日丁亥时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_geng', 'bazi_semantic', 'bazi_state_factor_285', 'bazi_semantic', 'bazi_relation_factor_122', 'bazi_semantic', 'bazi_state_factor_286', 'bazi_semantic', 'hour_branch_hai', 'bazi_semantic', 'bazi_condition_earth_2', 'bazi_semantic', 'source_ref', 'rel_smth_09_070', 'shenguan_liangshuai', 'rel_smth_09_071', 'tong_yintu_fushen', 'rel_smth_09_072', 'kuigang_miao', 'evi_smth_09_070', 'shenguan_liangshuai', 'rule_shenguan_liangshuai1', 'evi_smth_09_071', 'tong_yintu_fushen', 'rule_butong_yueqi_nanfufu1', 'evi_smth_09_072', 'kuigang_miao', 'rule_kuigang_dinghai1', 'map_smth_09_047', 'map_smth_09_048']
    
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
        l1_anchor="smth_v1.0.0_六庚日丁亥时_001_L1",
    )
    version: str = "1.0.0"
