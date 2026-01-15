"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412649
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
    semantic_id="smth_v1.0.0_天元坐财与身财相称_001",
    book_id="sanming",
    engine_id="bazi"
)
class 天元坐财与身财相称(SemanticEntry):
    """
    - **原文（source_text）**：

  天元坐财：如庚辰、辛卯日，春生，甲乙木为财，喜戊己印生身，壬癸食生财，忌庚辛金劫夺，切不可岁逢官煞，即春月金弱，不能胜任，反不为福。甲午、乙未日夏生...
    """
    
    original_text: str = """- **原文（source_text）**：

  天元坐财：如庚辰、辛卯日，春生，甲乙木为财，喜戊己印生身，壬癸食生财，忌庚辛金劫夺，切不可岁逢官煞，即春月金弱，不能胜任，反不为福。甲午、乙未日夏生，己土为财；甲辰日夏生，戊土为财；丙戌、丁丑日秋生，辛金为财，喜忌俱与前同。惟壬午、癸巳二日，禄马同乡，不专以财论。

- 分字分词释义：

  - **天元坐财**：日元（天元）在日支上直接坐财星，如庚辰、辛卯等例，日干脚下即为其财源。
  - **喜戊己印生身，壬癸食生财**：印星生身，使日主有力；食神生财，使财源有根，两者配合方为佳局。
  - **忌庚辛金劫夺**：比劫来分夺财星，则“天元坐财”的优势被削弱甚至反转。
  - **切不可岁逢官煞，即春月金弱，不能胜任**：春季金弱之时，再行官煞运，等于以虚弱之金强行当官，反不为福。

- **规范化释义（primary_lang_explained）**：

  天元坐财，意指一个人“脚下就踩着钱”：日元所临之日支本身就是财星所在。若再得印生身、食生财，便形成身财相称、内外相济的格局，往往主：

  - 有稳定、可持续的收入来源；
  - 通过自身专业或能力（食神）不断生成新的财路；
  - 既能守财，也能适度运用。

  但若比劫重重来分夺，或在用财之时日主过弱、行官煞不当，则脚下之财反成绊脚石：要位而不胜任，要财而不堪负重。

- 核心要点：

  - 天元坐财贵在**身财相称**：身强能任财，财有生源，方为吉。
  - 忌比劫分夺与官煞过重，尤其在金弱季节行官煞之运。
  - 需结合季节（时令）、印比与食伤配置，综合判断能否“坐得住财”。

- 详细解说：

  可以把天元坐财视为一种“先天优势位”：脚下有库、有资源，只要自身具备一定能力，就容易在相同起点中占得先机。但这并不保证一生无忧——

  - 若教育、性格与行运支持得好，则此优势可转化为长期稳定的物质基础；
  - 若性情偏急、比劫重、好高骛远，则容易在投资、扩张或赌博式决策中反覆耗损脚下之财。

- **校勘与字词辨析（双语）**：

  - 原文对各日干（庚辰、辛卯、甲午、乙未、甲辰、丙戌、丁丑等）的细节较多，本稿选取其共通原则加以归纳，具体日柱可在应用篇中另行展开。
  - 对“壬午、癸巳二日禄马同乡，不专以财论”一句，本稿在此仅点出其特殊性，提醒实占时需另行结合禄马格与其他条文综合判断。
  - **English**：
    - Should be judged comprehensively with other clauses rather than in isolation.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_117]` `[trigger: 天元坐财]` `[factor_trigger: rizhi_caixin AND jiaoxia_youcai]` `[role: 主干]` 天元坐财，如庚辰、辛卯日，日元脚下即为其财源。 → 《三命通会》卷六#天元坐财
  - `[ns_smth_06_118]` `[trigger: 印生身食生财]` `[factor_trigger: yin_shenshen AND shi_shengcai]` `[role: 主干依赖]` 喜戊己印生身，壬癸食生财，忌庚辛金劫夺。 → 《三命通会》卷六#天元坐财
  - `[ns_smth_06_119]` `[trigger: 金弱不胜]` `[factor_trigger: chunyue_jinruo AND guansha_bunengsheng]` `[role: 条件分支]` 切不可岁逢官煕，即春月金弱，不能胜任，反不为福。 → 《三命通会》卷六#天元坐财
  - `[ns_smth_06_120]` `[trigger: 身财相称]` `[factor_trigger: shen_qiang AND cai_keyong]` `[role: 总结]` 身财相称：身强能任财，财有生源，方为吉。 → 《三命通会》卷六#天元坐财"""
    normalized_text_zh: str = """"""
    subject: str = "天元坐财与身财相称"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_33', 'bazi_semantic', 'new_candidate', 'bazi_semantic', 'bazi_state_factor_22', 'bazi_semantic', 'bazi_state_degree_21', 'bazi_semantic', 'bazi_condition_factor_186', 'bazi_semantic', 'bazi_condition_factor_187', 'bazi_semantic', 'source_ref', 'rel_smth_06_115', 'tianyuan_zuocai_presence', 'rel_smth_06_116', 'shencai_pingheng', 'rel_smth_06_117', 'bijie_jieduo_risk', 'evi_smth_06_115', 'tianyuan_zuocai_presence', 'rule_zuocai', 'evi_smth_06_116', 'shencai_pingheng', 'rule_xiangcheng', 'evi_smth_06_117', 'bijie_jieduo_risk', 'rule_jieduo', 'map_smth_06_077', 'map_smth_06_078']
    
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
        l1_anchor="smth_v1.0.0_天元坐财与身财相称_001_L1",
    )
    version: str = "1.0.0"
