"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.066807
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
    semantic_id="smth_v1.0.0_1_提纲主本与用神喜忌_001",
    book_id="sanming",
    engine_id="bazi"
)
class 1提纲主本与用神喜忌(SemanticEntry):
    """
    - 原文（source_text）：
  人禀天地，命属阴阳，生居覆载之中，尽在五行之内。
  欲知贵贱，先观月令乃提纲；次断吉凶，专用日干为主本。
  三元要成格局，四柱喜见财官。
  用神不可损伤...
    """
    
    original_text: str = """- 原文（source_text）：
  人禀天地，命属阴阳，生居覆载之中，尽在五行之内。
  欲知贵贱，先观月令乃提纲；次断吉凶，专用日干为主本。
  三元要成格局，四柱喜见财官。
  用神不可损伤，日主最宜健旺。
  年伤日干，名为本主不和；岁月时中，大怕官煞混杂。
  取用凭于生月，当推究其浅深；发觉在于日时，要消详于强弱。
  官星正气，忌见刑冲；时上偏财，怕逢兄弟。
  生气印绶，利官运，畏入财乡；七煞偏官，喜制伏，不宜太过。
  伤官复行官运，不测灾来；阳刃冲合岁君，勃然祸至。
  富而且贵，定因财旺生官；非夭即贫，必是身衰遇鬼。

- 分字分词释义：
  - **提纲**：月令。
  - **主本**：日干。
  - **三元**：天地人。
  - **浅深**：月令中人元司事。
  - **发觉**：运限发动，或晚年结果。
  - **生气**：印绶。
  - **鬼**：七煞。

- **规范化释义（primary_lang_explained）**：
  人受天地之气而生，命运属于阴阳五行的范畴。
  要判断贵贱，首先看月令提纲；要判断吉凶，专以日干为主本。
  天、地、人三元要构成格局，四柱中喜见财星和官星。
  用神（格局核心）不可受损伤，日主最宜健旺。
  年干克日干，叫本主不和（如父子不协）。岁月时中，最怕官煞混杂。
  取用神要凭月令，推究节气深浅；祸福的应验往往在日时（或运限），要详查强弱。
  正官星忌见刑冲。时上偏财格忌见比肩劫财（兄弟）。
  印绶格利于行官运（官印相生），怕入财乡（财坏印）。七煞格喜制伏（食神），但不宜制伏太过（尽法无民）。
  伤官格再行官运（伤官见官），会有不测之灾。阳刃格若冲合岁君（流年），大祸临头。
  富贵双全，一定是因为财旺生官（且身旺）。非贫即夭，必是因为身衰遇煞（鬼）。

- 核心要点：
  - **纲领**：月令提纲，日干为主。
  - **喜忌**：用神忌损，日主喜旺。
  - **格局**：财官印煞伤刃。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_11_037]` `[trigger: 月令提纲]` `[factor_trigger: yueling_tigang AND rigan_zhuben]` `[role: 主干]` 欲知贵贱，先观月令乃提纲；次断吉凶，专用日干为主本。 → 《三命通会》卷十一#提纲主本与用神喜忌
  - `[ns_smth_11_038]` `[trigger: 用神日主]` `[factor_trigger: yongshen_rizhu AND sunshang_jianwang]` `[role: 主干依赖]` 用神不可损伤，日主最宜健旺。 → 《三命通会》卷十一#提纲主本与用神喜忌
  - `[ns_smth_11_039]` `[trigger: 伤官见官]` `[factor_trigger: shangguan_jianguan AND yanggren_chongsui]` `[role: 条件分支]` 伤官复行官运，不测灾来；阳刃冲合岁君，勃然祸至。 → 《三命通会》卷十一#提纲主本与用神喜忌
  - `[ns_smth_11_040]` `[trigger: 财旺生官]` `[factor_trigger: caiwang_shengguan AND shenshuai_yugui]` `[role: 总结]` 富而且贵，定因财旺生官；非夭即贫，必是身衰遇鬼。 → 《三命通会》卷十一#提纲主本与用神喜忌"""
    normalized_text_zh: str = """"""
    subject: str = "1 提纲主本与用神喜忌"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_month_command_2', 'bazi_semantic', 'bazi_structure_factor_32', 'bazi_semantic', 'bazi_relation_factor_30', 'bazi_semantic', 'bazi_state_yongshen_2', 'bazi_semantic', 'bazi_state_factor_88', 'bazi_semantic', 'bazi_state_factor_299', 'bazi_semantic', 'source_ref', 'rel_smth_11_043', 'core_factor', 'rel_smth_11_044', 'cond_factor', 'rel_smth_11_045', 'risk_factor', 'evi_smth_11_043', 'core_factor', 'rule_name43', 'evi_smth_11_044', 'cond_factor', 'rule_name44', 'evi_smth_11_045', 'risk_factor', 'rule_name45', 'map_smth_11_029', 'map_smth_11_030']
    
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
        l1_anchor="smth_v1.0.0_1_提纲主本与用神喜忌_001_L1",
    )
    version: str = "1.0.0"
