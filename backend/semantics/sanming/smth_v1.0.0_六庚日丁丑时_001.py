"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339438
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
    semantic_id="smth_v1.0.0_六庚日丁丑时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六庚日丁丑时(SemanticEntry):
    """
    - 原文（source_text）：
  六庚日生时丁丑，贵地逢官火太轻。木火运通轩冕客，不通独立只虚名。
  庚日丁丑时，金重火轻。庚以丁为官，以己为印，丑上丁火气轻，己土正位。若通木火气月，官印逢...
    """
    
    original_text: str = """- 原文（source_text）：
  六庚日生时丁丑，贵地逢官火太轻。木火运通轩冕客，不通独立只虚名。
  庚日丁丑时，金重火轻。庚以丁为官，以己为印，丑上丁火气轻，己土正位。若通木火气月，官印逢生旺，贵；不通，虚名而已。通火土生旺月，富；不通，运遇亦主名声。

- 分字分词释义：
  - **金重火轻**：丑为金库，又是庚金墓地（一说庚长生巳，墓丑，但丑土生金，金气不弱），丁火在丑为墓地（或衰地），故火轻。
  - **贵地**：丑为天乙贵人（庚辛逢马虎，一说牛羊，庚丑为贵人）。
  - **官印**：丁为官，丑中己土为印。

- **规范化释义（primary_lang_explained）**：
  六庚日出生于丁丑时，庚金得库，丁火官星微弱。丑为贵人之地，且藏正印。若生于木火旺月，官星得助，印绶生身，主贵（轩冕客）。若不通木火气，官星无力，只有虚名。若通火土运，主富。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Geng Days with Ding-Chou Hour":

  - Noble ground encounters Official but Fire too light—Geng Metal is heavy at Chou (treasury); Ding Fire Official is weak.
  - If Wood-Fire luck connects, becomes carriage-and-cap guest (high official); without connection, only empty fame.
  - If passing Fire-Earth prosperous month, indicates wealth; without monthly qi, luck encounter still brings fame.
  - Key: Official star needs strengthening through Wood generating Fire; Chou treasury provides noble support.

- 核心要点：
  - **官印相生**：丁官己印，但官星弱，需财（木）生官。
  - **墓库**：庚归丑库，身有根。
  - **贵人**：时临天乙贵人。

- 详细解说：
  此格关键在于扶起官星。丁火在丑，犹如雪中之火，气势微弱。必须局中有木生火，或行南方火运，官星得地，方能发福。若金水太旺，丁火受伤，则名为官，实无权。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_053]` `[trigger: 贵地逢官]` `[factor_trigger: guidi_fengguan AND huo_taiqing]` `[role: 主干]` 六庚日生时丁丑，贵地逢官火太轻。 → 《三命通会》卷九#六庚日丁丑时
  - `[ns_smth_09_054]` `[trigger: 木火运通]` `[factor_trigger: muhuo_yuntong AND xuanmian_ke]` `[role: 主干依赖]` 木火运通轩冕客，不通独立只虚名。 → 《三命通会》卷九#六庚日丁丑时
  - `[ns_smth_09_055]` `[trigger: 通火土月]` `[factor_trigger: tong_huotu_yue AND fu]` `[role: 条件分支]` 通火土生旺月，富。 → 《三命通会》卷九#六庚日丁丑时
  - `[ns_smth_09_056]` `[trigger: 运遇名声]` `[factor_trigger: yunyv_mingsheng AND butong_yi]` `[role: 总结]` 不通，运遇亦主名声。 → 《三命通会》卷九#六庚日丁丑时"""
    normalized_text_zh: str = """"""
    subject: str = "六庚日丁丑时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_geng', 'bazi_semantic', 'bazi_state_metal_fire_2', 'bazi_semantic', 'bazi_state_factor_342', 'bazi_semantic', 'bazi_state_yi', 'bazi_semantic', 'hour_branch_chou', 'bazi_semantic', 'bazi_condition_wood_fire_2', 'bazi_semantic', 'source_ref', 'rel_smth_09_040', 'jinzhong_huoqing', 'rel_smth_09_041', 'tianyi_guiren', 'rel_smth_09_042', 'tong_muhuo_yueqi', 'evi_smth_09_040', 'jinzhong_huoqing', 'rule_jinzhong_huoqing1', 'evi_smth_09_041', 'tong_muhuo_yueqi', 'rule_muhuo_xuanmian1', 'evi_smth_09_042', 'jinzhong_huoqing', 'rule_butong_xuming1', 'map_smth_09_027', 'map_smth_09_028']
    
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
        l1_anchor="smth_v1.0.0_六庚日丁丑时_001_L1",
    )
    version: str = "1.0.0"
