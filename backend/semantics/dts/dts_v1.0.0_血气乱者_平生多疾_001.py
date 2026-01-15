"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997708
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
    semantic_id="dts_v1.0.0_血气乱者_平生多疾_001",
    book_id="dts",
    engine_id="bazi"
)
class 血气乱者平生多疾(SemanticEntry):
    """
    - **原文（source_text）**：
  血气乱者，平生多疾。

- 原注（原文注解）：
 　　反逆、上下不通、来往不顺，皆为乱。

- 分字分词释义：
  - 血气：气血、五行流通之路径。
...
    """
    
    original_text: str = """- **原文（source_text）**：
  血气乱者，平生多疾。

- 原注（原文注解）：
 　　反逆、上下不通、来往不顺，皆为乱。

- 分字分词释义：
  - 血气：气血、五行流通之路径。
  - 乱：紊乱、错配、失序。
  - 平生：一生、终生。
  - 多疾：多病多痛、疾病缠绵。

- 规范化释义（primary_lang_explained）：
  所谓"血气乱"，是指五行生克反逆、上下不通、来往不顺：或本该相生却反相伐，或本该降泄却反上冲，令气血运行错乱。此等命局，往往一生多病多痛，易有旧病缠绵、反复发作之象。

- **核心要点**：
  - “乱”重在路径错配：该通的不通、该降的不降；
  - 多见反逆冲伐、上下断截、来往受阻；
  - 病象多为反复、迁延，难得真正调匀。

- 详细解说：
  与"和"相对，"乱"不是单指某一行太旺或太弱，而是整个生克路线上出现紊乱：如木应生火却被金截，水应下行却被土塞，或寒热燥湿错置，使脏腑经络失去协调。命盘中若喜用被截、忌神横行，行运再遇反逆冲伐，易显现为血压不稳、循环失常、易出血或淤堵之类问题，久而久之，平生多疾。

- 校勘与字词辨析：
  - "反逆、上下不通、来往不顺"：三语分别从方向（逆行）、层次（上下）、流动（往来）刻画"乱"的不同侧面。

- **L2-术语对齐（Term Glossary）**：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 血气乱 | Disordered Blood-Qi | 气血运行错配 | Mismatched qi-blood circulation | xueqiluan | new_candidate |
| 反逆 | Reversal Flow | 运行方向相反 | Qi against proper direction | fanni | new_candidate |
| 上下不通 | Blocked Upper-Lower | 上下阻塞 | Blockage upper-lower body | shangxia_butong | new_candidate |
| 来往不顺 | Impaired Circulation | 往返受阻 | Obstructed circulation routes | laiwang_bushun | new_candidate |
| 迁延反复 | Recurrent-Prolonged | 症状反复 | Symptoms recur over time | qianyan_fanfu | new_candidate |

- **次语种完整诠释（secondary_lang_full）**：  
  "Blood and Qi disordered" describes channels where flow is reversed, blocked between upper and lower, or jerky and uneven. What should nourish instead damages, what should descend instead rushes upward. Charts with such patterns tend to bring a lifetime of recurring ailments: symptoms that come and go, never fully settling, because the underlying routes of movement are wrongly wired."""
    normalized_text_zh: str = """忌神若直入五脏，等于把本该护身之气换成克身之气：木来过旺乘土则伤脾，火来过甚入金则损肺，土入水则病肾，金入木则病肝，水入火则病心。旺则有馀成实证，衰则不足成虚损，皆为“病凶”。"""
    subject: str = "血气乱者，平生多疾。"
    factor_refs: list = ['source_ref', 'rel_dts_jb2_001', 'xueqiluan', 'rel_dts_jb2_002', 'shangxia_butong', 'rel_dts_jb2_003', 'qianyan_fanfu', 'evi_dts_jb2_001', 'xueqiluan', 'rule_jibing_disorder', 'evi_dts_jb2_002', 'rule_jibing_chaos', 'evi_dts_jb2_003', 'rule_jibing_recurrence_pattern', 'concept_disorder', 'concept_blockage', 'concept_recurrence', 'engine_id', 'jibing_circulation_mismatch', 'circulation_path', 'bazi_calculator', 'jibing_circulation_stability', 'circulation_stability', 'bazi_semantic', 'jibing_chronicity', 'chronicity', 'bazi_semantic', 'jibing_relapse_risk', 'relapse_risk', 'bazi_rule_engine', 'jibing_yongshen_damage', 'yongshen_damage', 'bazi_rule_engine', 'jibing_transient_boundary', 'boundary', 'bazi_rule_engine', 'jibing_harmful_god', 'jibing_five_viscera', 'jibing_enter_viscera', 'jibing_excess_pattern', 'jibing_deficient_pattern', 'engine_id', 'jibing_harmful_qi_organ_layer', 'organ_involvement_level', 'bazi_semantic', 'jibing_affected_viscera', 'affected_organ', 'bazi_semantic', 'jibing_harmful_qi_profile', 'harmful_qi_profile', 'bazi_calculator', 'jibing_pattern_nature', 'pattern_nature', 'bazi_semantic', 'jibing_organ_damage_risk', 'organ_damage_risk', 'bazi_rule_engine', 'jibing_organ_boundary_flag', 'boundary', 'bazi_rule_engine', 'jibing_guest_god', 'jibing_six_meridians', 'jibing_roaming_meridians', 'jibing_superficial_disorder', 'jibing_minor_calamity', 'engine_id', 'jibing_guest_qi_layer', 'guest_qi_layer', 'bazi_semantic', 'jibing_affected_outer_system', 'affected_system', 'bazi_semantic', 'jibing_reversibility', 'reversibility', 'bazi_semantic', 'jibing_guest_qi_intensity', 'guest_qi_intensity', 'bazi_calculator', 'jibing_descent_risk', 'descent_risk', 'bazi_rule_engine', 'jibing_minor_boundary_flag', 'boundary', 'bazi_rule_engine']
    
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
        book_id="dts",
        chapter="",
        l1_anchor="dts_v1.0.0_血气乱者_平生多疾_001_L1",
    )
    version: str = "1.0.0"
