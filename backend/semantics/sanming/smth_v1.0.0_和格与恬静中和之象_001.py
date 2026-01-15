"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.436400
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
    semantic_id="smth_v1.0.0_和格与恬静中和之象_001",
    book_id="sanming",
    engine_id="bazi"
)
class 和格与恬静中和之象(SemanticEntry):
    """
    - 原文（source_text）：

  和者恬静也.如身柔弱，独有一位夫星，柱无冲破、攻击之神，禀其中和之气，则为和也.如壬辰、辛亥、己卯、己巳，己用甲为夫，亥乃生长之地，得天时地利；甲以辛为官，...
    """
    
    original_text: str = """- 原文（source_text）：

  和者恬静也.如身柔弱，独有一位夫星，柱无冲破、攻击之神，禀其中和之气，则为和也.如壬辰、辛亥、己卯、己巳，己用甲为夫，亥乃生长之地，得天时地利；甲以辛为官，金生于巳，巳以金为子，亦生于巳，谓之夫行官星，子得长生，故主益夫旺子.虽自坐卯支为煞，有巳中庚制，为去煞留官之论，女命之贵也.

- 分字分词释义：

  - **和者恬静也**：和，指性情恬淡、气势中和，不偏不激.
  - **身柔弱，独有一位夫星**：日主略偏柔弱，只一位夫星为主，不见多重争合.
  - **柱无冲破、攻击之神**：四柱无严重刑冲、克害夫星之神，格局相对平稳.
  - **夫行官星，子得长生**：夫星能行其官职，子星得长生之地，比喻夫子两端俱有发展.

- **规范化释义（primary_lang_explained）**：

  “和”格与“纯”格相近，但更强调**中和与恬静**：日主略弱而不绝，夫星单一而稳，命局中缺少剧烈冲克与争夺，使得婚姻与家庭多走中道、以温和为主.

  原例壬辰、辛亥、己卯、己巳：己土以甲木为夫，亥为甲之生长之地，有天时地利；甲以辛为官，辛金生于巳，巳中庚金又可制卯中煞气，是为“去煞留官”；子星得长生，故原文以“益夫旺子”概之.

- 核心要点：

  - 日主稍柔，夫星得中和之气，不宜过刚过激.
  - 命局少冲少破，关系模式较少极端对抗.
  - 去煞留官，保留夫星清正的一面.

- 详细解说：

  1. **相处氛围的“和”**  
     - 女命身柔而夫星有力，常见于在关系中乐于协商、懂得退让的一类；  
     - 若配合财印适中，多主家庭氛围稳定，虽未必惊艳显贵，却能细水长流.

  2. **结构上的“去煞留官”**  
     - 原例中卯为煞，巳中庚金能制之，体现“外在矛盾被化解”的结构；  
     - 现代可理解为：关系中虽有潜在冲突，但有足够的理性与制度（官星）来调和.

  3. **对身弱的平衡要求**  
     - 身柔弱并非坏事，关键在于是否仍能保持自我判断；  
     - 若身过弱而夫星过强，则容易走向过度依附，此时需借印星、比肩等扶助.

  “和格”更像是一种在人格与关系模式上都趋向温和、平衡的状态，不以刚烈见长，而以稳定、细腻见长.

 - **完整对等诠释（secondary_lang_full）**：

   The pattern of "Harmony" describes a chart where the overall tone of relationship is gentle and balanced. The Day Master tends to be on the softer or slightly weaker side, while a single spouse star stands out clearly and is not harassed by heavy clashes or competing candidates. Instead of intense struggle, the main motif is mutual accommodation: the partner has enough strength and position to take responsibility, and the native has enough inner softness and flexibility to cooperate without erasing herself.

   In the example, Ji Earth uses Jia Wood as the spouse star. Jia Wood receives the support of Hai as its growth place, representing favourable timing and environment for the partner. Jia then takes Xin Metal as its Officer, and Metal is born in Si, where it also becomes the child star's home. Within this configuration, harmful Sha is largely contained – symbolised by Geng Metal in Si restraining the Sha in Mao – so that what remains is the upright Officer function. Thus both spouse and children are able to develop, and the household operates more through calm negotiation than through open conflict.

   For a modern reader, the He pattern points to a life in which one primary partnership is sustained by moderate power on both sides, low levels of overt conflict, and a shared willingness to keep the relationship "within bounds". It favours long-term companionship and steady support over dramatic highs and lows, and is well suited to people who value emotional safety and quiet cooperation more than intensity or dominance.

- 校勘与字词辨析：

  - 原文例命中“女命之贵也”，本稿理解为格局清明、能在家庭与关系中扮演稳定角色，不专以官爵衡量.
  - “和者恬静也”一句，本稿在白话中整体展开为性情、结构与关系氛围三层.
  - **English**：
    - Spirit-star (shensha) terms demystified; fortune cycle descriptions treated as developmental tendencies.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_07_013]` `[trigger: 和格定义]` `[factor_trigger: he_ge_tianjing]` `[role: 主干]` 和者恬静也。 → 《三命通会》卷七#和格
  - `[ns_smth_07_014]` `[trigger: 身柔夫单]` `[factor_trigger: shen_rouruo AND du_yi_fu_xing]` `[role: 主干依赖]` 如身柔弱，独有一位夫星，柱无冲破、攻击之神，禀其中和之气，则为和也。 → 《三命通会》卷七#和格
  - `[ns_smth_07_015]` `[trigger: 益夫旺子]` `[factor_trigger: yi_fu_wang_zi]` `[role: 条件分支]` 谓之夫行官星，子得长生，故主益夫旺子。 → 《三命通会》卷七#和格
  - `[ns_smth_07_016]` `[trigger: 去煞留官]` `[factor_trigger: qu_sha_liu_guan]` `[role: 总结]` 去煞留官之论，女命之贵也。 → 《三命通会》卷七#和格"""
    normalized_text_zh: str = """"""
    subject: str = "和格与恬静中和之象"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_90', 'bazi_semantic', 'bazi_structure_factor_91', 'bazi_semantic', 'bazi_state_relation_2', 'bazi_semantic', 'bazi_state_day_master_7', 'bazi_semantic', 'source_ref', 'rel_smth_07_007', 'fuxing_danyi', 'rel_smth_07_008', 'guanxi_chongtu_fuhe', 'rel_smth_07_009', 'zhonghe_zhiqi', 'evi_smth_07_007', 'fuxing_danyi', 'rule_hege', 'evi_smth_07_008', 'guanxi_chongtu_fuhe', 'rule_dichongtu', 'evi_smth_07_009', 'qusha_liuguan', 'rule_liuguan', 'map_smth_07_005', 'map_smth_07_006']
    
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
        l1_anchor="smth_v1.0.0_和格与恬静中和之象_001_L1",
    )
    version: str = "1.0.0"
