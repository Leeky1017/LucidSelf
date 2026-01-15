"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.339763
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
    semantic_id="smth_v1.0.0_六壬日甲辰时_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六壬日甲辰时(SemanticEntry):
    """
    - 原文（source_text）：
  六壬日生时甲辰，壬骑龙背坐食神。柱中有托无刑害，必是荣华富贵人。
  壬日甲辰时，亦为壬骑龙背。壬以甲为食神，辰上壬水合局，甲有生气，食神旺相，通月气者富贵福...
    """
    
    original_text: str = """- 原文（source_text）：
  六壬日生时甲辰，壬骑龙背坐食神。柱中有托无刑害，必是荣华富贵人。
  壬日甲辰时，亦为壬骑龙背。壬以甲为食神，辰上壬水合局，甲有生气，食神旺相，通月气者富贵福厚。冬月，行卯运，不利。

- 分字分词释义：
  - **壬骑龙背**：通常指壬辰日，此处泛指壬日坐辰时。辰为龙。
  - **坐食神**：甲木食神透干。
  - **合局**：申子辰合水局，或壬入辰库。

- **规范化释义（primary_lang_explained）**：
  六壬日出生于甲辰时，甲木食神透出，辰为水库，壬水有根（或合局）。甲木在辰有余气（木之衰地，但湿土养木），食神有力。若日主有倚托（通月气），无刑冲破害，主荣华富贵。冬月生人（水旺），若行卯运（死地），不利（木多水缩或伤官见官？存疑）。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ren Days with Jia-Chen Hour":

  - Ren rides Dragon-back sits Eating God—Jia Wood Eating God reveals; Chen is Water treasury; Ren Water has root.
  - If pillars have support no punishment-harm, must be glorious-splendor wealthy-noble person.
  - Also making Ren Rides Dragon-Back; Chen above Ren Water combines bureau; Jia has life-qi; Eating God prosperous; connecting monthly qi, wealthy-noble fortune thick.
  - Key: Eating God pattern with Water treasury root; winter month traveling Mao luck unfavorable.

- 核心要点：
  - **食神格**：甲木透。
  - **墓库**：辰为水库。
  - **壬骑龙背**：借辰土之力。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_09_161]` `[trigger: 壬骑龙背]` `[factor_trigger: renqi_longbei AND zuo_shishen]` `[role: 主干]` 六壬日生时甲辰，壬骑龙背坐食神。 → 《三命通会》卷九#六壬日甲辰时
  - `[ns_smth_09_162]` `[trigger: 有托无刑]` `[factor_trigger: youtuo_wuxing AND ronghua_fugui]` `[role: 主干依赖]` 柱中有托无刑害，必是荣华富贵人。 → 《三命通会》卷九#六壬日甲辰时
  - `[ns_smth_09_163]` `[trigger: 食神旺相]` `[factor_trigger: shishen_wangxiang AND tongyueqi_fugui]` `[role: 条件分支]` 辰上壬水合局，甲有生气，食神旺相，通月气者富贵福厚。 → 《三命通会》卷九#六壬日甲辰时
  - `[ns_smth_09_164]` `[trigger: 冬月卯运]` `[factor_trigger: dongyue_maoyun AND buli]` `[role: 总结]` 冬月，行卯运，不利。 → 《三命通会》卷九#六壬日甲辰时"""
    normalized_text_zh: str = """"""
    subject: str = "六壬日甲辰时"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'day_master_ren', 'bazi_semantic', 'bazi_state_ren', 'bazi_semantic', 'bazi_relation_shishen_8', 'bazi_semantic', 'bazi_state_factor_334', 'bazi_semantic', 'hour_branch_chen', 'bazi_semantic', 'bazi_condition_xinghai', 'bazi_semantic', 'source_ref', 'rel_smth_09_121', 'renqi_longbei', 'rel_smth_09_122', 'tong_yueqi_wu_xinghai', 'rel_smth_09_123', 'renqi_longbei', 'evi_smth_09_121', 'renqi_longbei', 'rule_renqi_longbei1', 'evi_smth_09_122', 'tong_yueqi_wu_xinghai', 'rule_tong_yueqi_wu_xinghai1', 'evi_smth_09_123', 'dongyue_xingmaoyun', 'rule_dongyue_xingmaoyun1', 'map_smth_09_081', 'map_smth_09_082']
    
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
        l1_anchor="smth_v1.0.0_六壬日甲辰时_001_L1",
    )
    version: str = "1.0.0"
