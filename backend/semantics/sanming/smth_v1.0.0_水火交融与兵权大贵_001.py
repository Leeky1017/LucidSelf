"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.458289
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
    semantic_id="smth_v1.0.0_水火交融与兵权大贵_001",
    book_id="sanming",
    engine_id="bazi"
)
class 水火交融与兵权大贵(SemanticEntry):
    """
    - **原文（source_text）**：
  经云：火若遇水成既济，兵权万里。如辛巳、辛丑、丙子、戊子，丙日临子，坐下正官，月时引旺，重逢奇仪。丙以癸为官，癸以戊为官，互换见官。丙合辛财生官，化为...
    """
    
    original_text: str = """- **原文（source_text）**：
  经云：火若遇水成既济，兵权万里。如辛巳、辛丑、丙子、戊子，丙日临子，坐下正官，月时引旺，重逢奇仪。丙以癸为官，癸以戊为官，互换见官。丙合辛财生官，化为真水。戊子时，戊合子中癸，化为真火，入水火既济格，大贵。

- 分字分词释义：
  - **水火既济**：出自《易》，指水火交融而各得其所，比喻刚柔调和、动静相济，此处指火日主得水官相配且不相害之格。
  - **兵权万里**：形容掌兵之权，统辖范围广远，多主武职显贵。
  - **互换见官**：丙以癸为官，癸又以戊为官，彼此在局中互相见到对方的官星，成环环相生之势。
  - **丙合辛财生官**：丙火与辛金相合，辛为丙之财，财生官，故有"财生官"之象。
  - **化为真水 / 真火**：指在一定条件下五行合化成功，水火虽相对，却能分别在不同层面成局而不相冲毁。

- **规范化释义（primary_lang_explained）**：
  本节论火日主与水官星既济的格局。原文以辛巳、辛丑、丙子、戊子一造为例：丙日坐子水，为正官在坐；月干辛金为丙之财，可以生官；时干戊土又为癸水之官，形成丙官癸、癸官戊、戊又合子中癸水的互见结构。水火表面相克，但在此局中，却因中间金、土的生合而实现了水火既济，最终形成兵权在握的大贵之格。

- **完整对等诠释（secondary_lang_full）**：
  The phrase 'when fire meets water it forms Already Accomplished and commands troops for ten thousand miles' describes a pattern in which a fire day-master is paired with water officials in a way that balances rather than destroys. In the example chart Xin-Si, Xin-Chou, Bing-Zi and Wu-Zi, Bing fire sits on Zi water, so the proper official is directly under the day-master. The month stem Xin metal is Bing's wealth and can generate Gui water as official; the hour stem Wu earth is the official of Gui, so Bing takes Gui as official and Gui takes Wu as official, forming a chain where officials see one another in turn. Bing combining with Xin wealth produces the water official, and Wu at Wu-Zi hour combines with the Gui hidden in Zi to return to fire. Thus water and fire each have their own formation and roots, interacting through wealth and earth instead of clashing head-on. This is the true 'water and fire Already Accomplished' configuration that gives great martial authority.


- 核心要点：
  - 水火既济格，重在**火日主与水官星之间不直接相冲，而通过财、印等环节调和**。
  - 当财星能生官，官又能得根，且日主不弱，则多主武职、军权等需要刚柔并济之职位。
  - 若水火直接对冲、无中介调和，则多主性情急躁、灾病官非，不能以既济论。

- 详细解说：
  在五行关系中，火克金、金生水、水克火，若结构失衡，易成相互消耗之局；但若以适当顺序排列，使克中有生、生中有合，则可构成类似"循环系统"的结构。本节例命正是通过辛金、癸水、戊土的互相关联，将原本相冲的水火调和为既济之局：丙火不直接被癸水扑灭，而是以辛金为媒介生出癸官；戊土又为癸水之官，并通过时支子水得根，于是水火各有所依，共同构成武贵之命。
  
  实务判断中，如见火日主坐水官、再配以金财与土官互相牵引，且行运不破此结构，往往主掌兵权、统领边防或带武性之权力职位。但若行运冲破子水或破合，使水火再度直接对立，则既济之象转为相克，反主官非灾病。

- 校勘与字词辨析：
  - **"既济"**：为《易经》卦名，本义为事情已成，此处引申为水火交融、格局完备。
  - "重逢奇仪"中的"奇仪"，指特殊而合宜的五行组合，现代可理解为结构上十分巧妙的格局。
  - **English**：
    - Understood as structurally ingenious pattern.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_05_040]` `[trigger: 水火既济]` `[factor_trigger: shuihuo_jiji_presence]` `[role: 主干]` 火若遇水成既济，兵权万里。 → 《三命通会》卷五#水火既济
  - `[ns_smth_05_041]` `[trigger: 互换见官]` `[factor_trigger: huhuan_jianguan AND cai_sheng_guan]` `[role: 主干依赖]` 丙以癸为官，癸以戊为官，互换见官。丙合辛财生官，化为真水。 → 《三命通会》卷五#水火既济
  - `[ns_smth_05_042]` `[trigger: 水火各成]` `[factor_trigger: shui_huo_ge_cheng AND bu_xiang_chong_hui]` `[role: 条件分支]` 水火虽相对，却能分别在不同层面成局而不相冲毁。 → 《三命通会》卷五#水火既济
  - `[ns_smth_05_043]` `[trigger: 刚柔并济]` `[factor_trigger: gang_rou_bing_ji AND wu_zhi_dagui]` `[role: 总结]` 多主武职、军权等需要刚柔并济之职位。 → 《三命通会》卷五#水火既济"""
    normalized_text_zh: str = """"""
    subject: str = "水火交融与兵权大贵"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'shuihuo_jiji_presence', 'bazi_semantic', 'cai_yin_zhongjie_config', 'bazi_semantic', 'shuihuo_tiaohe_score', 'bazi_semantic', 'xunhuan_wanzheng_score', 'bazi_semantic', 'gangrou_bingji', 'bazi_semantic', 'xingyun_poju_risk', 'bazi_semantic', 'source_ref', 'rel_smth_05_031', 'shuihuo_jiji_presence', 'rel_smth_05_032', 'xunhuan_wanzheng_score', 'rel_smth_05_033', 'xingyun_poju_risk', 'evi_smth_05_031', 'shuihuo_jiji_config', 'rule_jiji', 'evi_smth_05_032', 'cai_yin_zhongjie_config', 'rule_xunhuan', 'evi_smth_05_033', 'shuihuo_tiaohe_score', 'rule_dagui', 'map_smth_05_021', 'map_smth_05_022']
    
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
        l1_anchor="smth_v1.0.0_水火交融与兵权大贵_001_L1",
    )
    version: str = "1.0.0"
