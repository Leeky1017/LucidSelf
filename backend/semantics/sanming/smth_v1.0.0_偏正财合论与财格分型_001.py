"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412701
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
    semantic_id="smth_v1.0.0_偏正财合论与财格分型_001",
    book_id="sanming",
    engine_id="bazi"
)
class 偏正财合论与财格分型(SemanticEntry):
    """
    - **原文（source_text）**：

  偏正财合论：《精纪》有生成财，如甲乙见戊己土为财，申子辰上坐生旺库，戊申、戊辰、戊子支干成合是也。凡命入贵格，除贵外，须主大富，仍多历钱谷之任；若不...
    """
    
    original_text: str = """- **原文（source_text）**：

  偏正财合论：《精纪》有生成财，如甲乙见戊己土为财，申子辰上坐生旺库，戊申、戊辰、戊子支干成合是也。凡命入贵格，除贵外，须主大富，仍多历钱谷之任；若不入贵格，又无福神助，亦是富豪百姓。若自生自旺，如甲人见戊午、己亥之例，主富。余仿此。有生合财，如甲人见戊癸，己人见癸戊，庚人见甲己等类，主成立富贵。有子母财，如木命人见火月、土日时之类，主平生多见喜事。有类财煞，寅午戌人见乙庚，巳酉丑人见丁壬，申子辰人见戊癸，亥卯未人见甲号，一名幽微煞，主名利并行。有财会煞，寅午戌人见辛丑，巳酉丑人见乙未，申子辰人见丙戌，亥卯未人见戊辰，此妻财聚会之神，遇者主富足及有美妻横财，却防妻人毒药害命。有名位财，乃食神中见库，如戊子火人见庚戌，戊食庚，火库在戌，克金为财，逢此者一生受禄。有长生财，如甲用戊己为财见戊申，癸用丙丁为财见丙寅之例，此类多得外财。又曰：术者多以甲见戊、乙见己类为财，不知甲己见丙辛、丙辛见戊癸等类为真财，生居有气旺相之位，主富盛。又纳音本干自见真五行，如乙亥人月日时中见庚，乙亥纳音火，乙庚真金，干头自是财也，此名天财，主富足优逸。若纳音反制克干头，如丁卯火却能制乙庚金，此名鬼财，主一生得世财，或为豪猾胥吏起家。戊寅、戊申得丙辛，乙酉、乙卯得戊癸，准此，更带辰戌丑未，主为艺术，大获世财。

- 分字分词释义：

  - **生成财、生合财、子母财等**：从不同组合与流通方式，区分财格的来源与表现形态。
  - **财会煞、类财煞**：财星与煞星相会，既有名利并行、聚财横发的机会，也暗藏危险与代价。
  - **名位财、长生财**：通过食神、长生之地等路径产生的财，多与名誉、外财或特定职业相关。

- **规范化释义（primary_lang_explained）**：

  偏财与正财并非“一把尺子量到底”，原文通过“生成财、子母财、财会煞、名位财、长生财”等多种名目，提示我们：

  - 财的**来源**可以不同：有的是先天家业（生成财），有的是婚姻与亲属（子母财），有的是职业与专业技能（名位财），有的是外地机缘（长生财）、有的是险中取利（财会煞、类财煞）。
  - 财的**路径**也可以不同：有的通过食神生发，有的通过合化而来，有的则在库中等待时机被打开。

- 核心要点：

  - 财格判断不应只看“多少”，还要看**来源、路径与承担的代价**。
  - 财会煞、类财煞等组合，往往对应“名利并行、福祸相倚”的人生轨迹。
  - 纳音与天干真五行的互动，可形成“天财”或“鬼财”等更细致的分类，对从事艺术、技术、经商等人尤有参考价值。

- 详细解说：

  在现代实践中，可以用“财格分型”的思路来吸收本节内容：

  - 对于同样“财多”的人，有的适合做长线积累（生成财、长生财），有的适合在专业岗位中通过技能获利（名位财），有的则适合从事高风险高收益行业（财会煞）。
  - 判断时需结合行运：在“适配型”财运到来时，顺势而为可成就事业；在不适配的运程里强行追逐某类财，反易招灾。

- **校勘与字词辨析（双语）**：

  - 本节名目繁多，本稿不一一逐条立专格，而是以“财格分型”的方式融通处理，避免读者被名词淹没。
  - “天财 / 鬼财”等术语，本稿以“天生机缘之财 / 世俗权术之财”加以对照理解，不作迷信化解释。
  - **English**：
    - Rational interpretation provided; avoids superstitious explanations.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_137]` `[trigger: 财格分型]` `[factor_trigger: pianzhenghclun AND caige_fenxing]` `[role: 主干]` 生成财、生合财、子母财、财会煚、名位财、长生财……财的来源、路径各不相同。 → 《三命通会》卷六#偏正财合论
  - `[ns_smth_06_138]` `[trigger: 入贵格大富]` `[factor_trigger: rugui_ge AND dafu]` `[role: 主干依赖]` 凡命入贵格，除贵外，须主大富，仍多历钱谷之任。 → 《三命通会》卷六#偏正财合论
  - `[ns_smth_06_139]` `[trigger: 天财鬼财]` `[factor_trigger: tiancai OR guicai]` `[role: 条件分支]` 纳音本干自见真五行，此名天财，主富足优逸。反制克干头，此名鬼财。 → 《三命通会》卷六#偏正财合论
  - `[ns_smth_06_140]` `[trigger: 财会煚防害]` `[factor_trigger: caihui_sha AND fang_duhai]` `[role: 总结]` 财会煚……主富足及有美妻横财，却防妻人毒药害命。 → 《三命通会》卷六#偏正财合论"""
    normalized_text_zh: str = """"""
    subject: str = "偏正财合论与财格分型"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_36', 'bazi_semantic', 'new_candidate', 'bazi_semantic', 'bazi_state_strength_6', 'bazi_semantic', 'bazi_state_factor_26', 'bazi_semantic', 'bazi_condition_factor_195', 'bazi_semantic', 'bazi_condition_factor_196', 'bazi_semantic', 'source_ref', 'rel_smth_06_130', 'caige_fenxing', 'rel_smth_06_131', 'caige_qiangdu', 'rel_smth_06_132', 'fushen_zhuli', 'evi_smth_06_130', 'caige_fenxing', 'rule_fenxing', 'evi_smth_06_131', 'guige_peihe', 'rule_jiangui', 'evi_smth_06_132', 'caisha_huihe_risk', 'rule_huisha', 'map_smth_06_087', 'map_smth_06_088']
    
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
        l1_anchor="smth_v1.0.0_偏正财合论与财格分型_001_L1",
    )
    version: str = "1.0.0"
