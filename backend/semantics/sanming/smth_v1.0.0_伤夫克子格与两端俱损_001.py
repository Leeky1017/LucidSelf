"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.436518
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
    semantic_id="smth_v1.0.0_伤夫克子格与两端俱损_001",
    book_id="sanming",
    engine_id="bazi"
)
class 伤夫克子格与两端俱损(SemanticEntry):
    """
    - 原文（source_text）：

  伤夫克子。

  伤夫克子者，乃夫星干支失位，生月失时，柱中又逢冲克，时支亦不生扶，兼且印绶重逢，盗夫之气，克子之甚，夫子不能旺，反绝于时是也。如一命：丙子...
    """
    
    original_text: str = """- 原文（source_text）：

  伤夫克子。

  伤夫克子者，乃夫星干支失位，生月失时，柱中又逢冲克，时支亦不生扶，兼且印绶重逢，盗夫之气，克子之甚，夫子不能旺，反绝于时是也。如一命：丙子、庚子、乙亥、丙子。乙木以庚金为夫星，十一月金寒水冷，又金死子地，支亥子水盗金气尽，柱无土生助，伤官木多，故伤其夫。乙木以丙火为子，引至子时，乃水旺火灭之地。虽年时干二火，被群水相克，夫子皆亡，故曰伤夫克子，余仿此推。

- 分字分词释义：

  - **伤夫克子**：夫星受伤、子星被克，两端皆不利。
  - **夫星干支失位，生月失时**：夫星在天干、地支所处之位皆不得令，且在出生月份上无气。
  - **印绶重逢，盗夫之气**：印星过多，把本该属于夫星的气势“盗”去扶身。
  - **夫子不能旺，反绝于时**：最终在时柱体现为夫子两端皆难以兴旺。

- **规范化释义（primary_lang_explained）**：

  “伤夫克子格”是前两格的极端情形：

  - 夫星失位无气，又被支中之水盗气、克制，难以成立；
  - 子星引至子时水旺之地，被群水克灭，难以得到生扶；
  - 再加上印绶过重、伤官木多，进一步分散与削弱了夫子两端的力量，形成“两端俱损”的结构。

- **完整对等诠释（secondary_lang_full）**：

  The "Hurt Husband and Injured Children" pattern marks a configuration in which both the spouse line and the child line are under heavy strain. The spouse star is misplaced in stem and branch, out of season and repeatedly drained by Water or other elements, while Seal and other supporting stars keep pulling qi back to the self. The child star is led to a place like Zi, where Water is overwhelmingly strong and Fire is extinguished, so that the line representing offspring has little room to grow. When both ends of the family axis are weakened in this way, the time pillar shows a late life in which neither partner nor children can easily become a stable source of support.

  For a contemporary reader, this structure does not decree disasters for loved ones. Instead, it points to a family system under pressure: the native may carry strong needs for safety and self‑protection, investing heavily in personal survival, work, or original family ties, while having limited capacity to consistently nurture a partner or children. Without awareness, this can result in relationships where everyone feels overburdened and under‑supported. With awareness, it becomes an invitation to gradually rebuild support networks, share load more fairly, and seek help early when signs of burnout or relational breakdown appear.

- 核心要点：

  - 夫星、子星同时处于弱势甚至绝地，是“伤夫克子”的根本特征。
  - 印绶过多、伤官太盛，会把原本可供夫子发展的气势抽走。
  - 这是对家庭结构压力较大的一类命局，需要特别注意平衡。

- 详细解说：

  1. **印绶与夫星的竞争**  
     - 印绶虽能护身，但过多时容易抢夺夫星、子星之气；  
     - 在现实中，常表现为命主重视自我价值、安全感与原生家庭，而对伴侣与子女的投入相对不足。

  2. **环境与行运的放大效应**  
     - 若行运再加重水气或印绶，可能放大家庭与亲子层面的压力；  
     - 反之，行运若能带来适度的财星、比肩，或对水气有所节制，便有机会缓和格局。

  3. **现代视角下的应对**  
     - 若命局显“伤夫克子”，比起恐惧，更重要的是及早觉察自己在关系中的位置与行为模式；  
     - 通过沟通、家庭治疗、亲职教育等方式，也有可能重建夫子两端的支持系统。

- 校勘与字词辨析：

  - “夫子皆亡”一语，古书用以强调极端不利，本稿不作字面理解，仅保留为“夫子两端压力极大”的象征说法。
  - 文中“印绶重逢、伤官木多”等术语，在本稿统一视为气势分配问题，而非神秘吉凶符号。
  - **English**：
    - Configuration issue; not mysterious fortune symbols.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_07_049]` `[trigger: 伤夫克子定义]` `[factor_trigger: shangfu_kezi_ge]` `[role: 主干]` 伤夫克子。 → 《三命通会》卷七#伤夫克子
  - `[ns_smth_07_050]` `[trigger: 双端失位]` `[factor_trigger: fuxing_shiwei AND yinshou_chongfeng]` `[role: 主干依赖]` 乃夫星干支失位，生月失时，柱中又逢冲克...兼且印绶重逢，盗夫之气，克子之甚。 → 《三命通会》卷七#伤夫克子
  - `[ns_smth_07_051]` `[trigger: 反绝于时]` `[factor_trigger: fuzi_buneng_wang AND fan_jue_yushi]` `[role: 条件分支]` 夫子不能旺，反绝于时是也。 → 《三命通会》卷七#伤夫克子
  - `[ns_smth_07_052]` `[trigger: 夫子皆亡]` `[factor_trigger: fuzi_jie_wang]` `[role: 总结]` 夫子皆亡，故曰伤夫克子。 → 《三命通会》卷七#伤夫克子"""
    normalized_text_zh: str = """"""
    subject: str = "伤夫克子格与两端俱损"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_zi_degree', 'bazi_semantic', 'bazi_structure_zi_degree_1', 'bazi_semantic', 'bazi_state_water_2', 'bazi_semantic', 'bazi_factor_11', 'bazi_semantic', 'source_ref', 'rel_smth_07_034', 'fuzi_shousun', 'rel_smth_07_035', 'yinxu_qiangqi', 'rel_smth_07_036', 'waibu_zhichi', 'evi_smth_07_034', 'fuzi_shousun', 'rule_shangfukezi', 'evi_smth_07_035', 'yinxu_qiangqi', 'rule_yinxu', 'evi_smth_07_036', 'waibu_zhichi', 'rule_jieyuan', 'map_smth_07_023', 'map_smth_07_024']
    
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
        l1_anchor="smth_v1.0.0_伤夫克子格与两端俱损_001_L1",
    )
    version: str = "1.0.0"
