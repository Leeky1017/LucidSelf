"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157368
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
    semantic_id="smth_v1.0.0_六乙日庚辰时断_金水清白与妻贤子贵_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六乙日庚辰时断金水清白与妻贤子贵(SemanticEntry):
    """
    - 原文（source_text）：

  六乙日庚辰时断。

  六乙日生时庚辰，水白金清化象真；壬从辛酉通官贵，却防目疾减精神。乙日庚辰时，妻贤子贵。乙合庚化金，若通申巳酉丑月，为人秀丽，主贵，却...
    """
    
    original_text: str = """- 原文（source_text）：

  六乙日庚辰时断。

  六乙日生时庚辰，水白金清化象真；壬从辛酉通官贵，却防目疾减精神。乙日庚辰时，妻贤子贵。乙合庚化金，若通申巳酉丑月，为人秀丽，主贵，却防目疾。如不见化，以壬为印，庚为官，辰土癸水合局，乙木有托，行东南运，贵显平和。

  乙丑日庚辰时，破祖克父，身弱，忌疾。通月气者，贵。子申年月，天干透甲戊，合三奇，大贵。

  乙卯日庚辰时，富贵。通火土年月，大贵。

  乙巳日庚辰时，作事成败。僧道富贵，带疾。常人刑克妻子。申子辰卯巳年月，贵。

  乙未日庚辰时，亥卯身，身旺；巳申，官旺。天干透煞印，皆贵。丑酉纯煞，柱有火制，亦吉。戌丑年月，四库全，大贵。

  乙酉日庚辰时，亥子年月，干透戊癸，贵。寅巳午月，官煞有制，吉。纯酉化金，主厚福。

  乙亥日庚辰时，不贵则富。若年月癸戊一化，申卯两旺，巳丑酉会金，行木土运，位至金紫。

  乙庚相会贵无疑，阴木阳金正合时；运吉身强无冲破，升迁自有贵人提。乙日庚辰时正，天官守库乾元。青年虎榜姓名传，禀性温良恭俭。士庶妻贤子贵，财人禄位升迁。南离戊癸火相连，富贵之中当险。

- 分字分词释义：

  - **水白金清**：水与金之气清纯，比喻人格清朗、气质秀洁。
  - **化金**：乙庚合金，象征将木性柔和与金性果决融合。
  - **天官守库**：官星守在库地，暗示权位稳固但也需承担责任与风险。

- 规范化释义（primary_lang_explained）：

  本节讲「六乙日，庚辰时」：

  - 乙木合庚化金，配以辰中水土，若得申酉等金地相应，多主贵显、清秀、妻贤子贵；
  - 若结构中化金有成、印绶得用，则更能在文武场域上取得名声；
  - 同时也提示有目疾、妻子刑克等潜在问题，需要留意健康与亲密关系的平衡。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Yi Days with Geng-Chen Hour":

  - Yi Wood combines with Geng to transform into Metal; paired with Water-Earth in Chen, when corresponding to Metal positions like Shen-You, this typically indicates nobility, refined elegance, and virtuous wife with worthy children.
  - When the Metal transformation succeeds and Seal is properly utilized, one can achieve greater fame in civil or military domains.
  - At the same time, potential issues with eye ailments and spouse conflicts are noted, requiring attention to health and intimate relationship balance.

- 核心要点：

  - 这是一个**金水清贵、以家庭为核心支点**的格局；
  - 「不贵则富」说明纵使不入仕途，也容易凭实业、资源获得丰厚回报；
  - 但在高位、高财富下，仍需警惕健康与风险事件的「暗线」。

- 详细解说：

  1. **夫妻与子女主题**  
     - 原文多处强调「妻贤子贵」，说明关系经营良好时，可形成稳固支持系统；  
     - 常人遇刑克结构，则需在人际边界与沟通上多下功夫。

  2. **清贵与险象并存**  
     - 「富贵之中当险」提示在高位置也可能遭遇突发变局；  
     - 现代可理解为：在职场与投资中，越高处越要重视风控与合规。

  3. **化金与性格组合**  
     - 乙庚合金将柔与刚结合，可成温良而有原则的性格；  
     - 行运不佳时，也可能在坚持与执拗之间摇摆，需要保持反思。

- 校勘与字词辨析：

  - 「水白金清」不作额外术语，本稿直译为气质清朗、行事干净利落。
  - 「天官守库」用来描绘权位与资源的集中，不单指具体神煞。
  - **English**：
    - Concentration of qi sources; not referring to specific spirit-stars alone.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_065]` `[trigger: 水白金清]` `[factor_trigger: shuibai_jinqing AND huaxiang_zhen]` `[role: 主干]` 六乙日生时庚辰，水白金清化象真。 → 《三命通会》卷八#六乙日庚辰时
  - `[ns_smth_08_066]` `[trigger: 妻贤子贵]` `[factor_trigger: qixian_zigui AND yigeng_hejin]` `[role: 主干依赖]` 乙合庚化金...妻贤子贵。 → 《三命通会》卷八#六乙日庚辰时
  - `[ns_smth_08_067]` `[trigger: 通金气月]` `[factor_trigger: tong_jinqi_yue AND xiuli_zhugui]` `[role: 条件分支]` 若通申巳酉丑月，为人秀丽，主贵，却防目疾。 → 《三命通会》卷八#六乙日庚辰时
  - `[ns_smth_08_068]` `[trigger: 贵人提携]` `[factor_trigger: guiren_tiqi AND wuchong_po]` `[role: 总结]` 运吉身强无冲破，升迁自有贵人提。 → 《三命通会》卷八#六乙日庚辰时"""
    normalized_text_zh: str = """"""
    subject: str = "六乙日庚辰时断：金水清白与妻贤子贵"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_yi', 'bazi_semantic', 'bazi_state_yi_geng_metal', 'bazi_semantic', 'bazi_relation_water_metal', 'bazi_semantic', 'bazi_state_zi_2', 'bazi_semantic', 'hour_branch_chen', 'bazi_semantic', 'bazi_condition_metal_1', 'bazi_semantic', 'source_ref', 'rel_smth_08_049', 'yigeng_hejin', 'rel_smth_08_050', 'shuibai_jinqing', 'rel_smth_08_051', 'tongjinqi_yue', 'evi_smth_08_049', 'yigeng_hejin', 'rule_yigeng', 'evi_smth_08_050', 'shuibai_jinqing', 'rule_jinqing', 'evi_smth_08_051', 'qixian_zigui', 'rule_qixian', 'map_smth_08_033', 'map_smth_08_034']
    
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
        l1_anchor="smth_v1.0.0_六乙日庚辰时断_金水清白与妻贤子贵_001_L1",
    )
    version: str = "1.0.0"
