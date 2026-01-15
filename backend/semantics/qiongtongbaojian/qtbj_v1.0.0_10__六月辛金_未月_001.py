"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578493
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
    semantic_id="qtbj_v1.0.0_10__六月辛金_未月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 10六月辛金未月(SemanticEntry):
    """
    - **原文（source_text）**：
  六月辛金，己土当权，辅助太多，恐掩金光，先用壬水，取庚佐之。壬庚两透，科甲功名，即不出干，藏支得所，亦有荣华。但忌戊出，得甲制之，方吉。甲须隔位，恐贪...
    """
    
    original_text: str = """- **原文（source_text）**：
  六月辛金，己土当权，辅助太多，恐掩金光，先用壬水，取庚佐之。壬庚两透，科甲功名，即不出干，藏支得所，亦有荣华。但忌戊出，得甲制之，方吉。甲须隔位，恐贪己合，反掩金光，又塞壬水之流，下贱之格。又忌庚出制甲。或只有未中一己，见了壬水，又为湿泥。不可见甲，甲出，反作平人。总以一壬一己，见庚无甲，方妙﹐与五月用己壬同。
  或丁乙出干，又有庚壬者，显贵。无壬者、否。或支成木局，得壬透，又有庚金发水之源，可云富贵。

- **分字分词释义**：
  - **己土当权**：己土当令掌权 / 未月 / 印旺
  - **辅助太多**：帮助太过 / 土多 / 忌象
  - **掩金光**：遮掩金的光辉 / 土多埋金 / 凶象
  - **隔位**：相隔位置 / 甲己不邻 / 防合
  - **贪己合**：甲木贪恋合己 / 甲己合土 / 凶象
  - **塞壬水之流**：堵塞壬水流动 / 甲合己土克水 / 凶象
  - **下贱之格**：低下卑贱格局 / 甲贪合 / 凶象
  - **湿泥**：湿润泥土 / 一己一壬 / 生金
  - **发水之源**：发出水的源头 / 庚生壬 / 用神

- **规范化释义（primary_lang_explained）**：
  六月（未月）辛金己土当权辅助太多恐掩金光先用壬水取庚佐之。壬庚两透科甲功名即不出干藏支得所亦有荣华。但忌戊出得甲制之方吉。甲须隔位恐贪己合反掩金光又塞壬水之流下贱之格。又忌庚出制甲。或只有未中一己见了壬水又为湿泥不可见甲甲出反作平人。总以一壬一己见庚无甲方妙与五月用己壬同。
  或丁乙出干又有庚壬者显贵。无壬者否。或支成木局得壬透又有庚金发水之源可云富贵。

- **完整对等诠释（secondary_lang_full）**：
  Xin Metal in 6th Month (Goat Month): Ji Earth commanding assistance too-much fear covering Metal-光 first-use Ren Water take Geng assist. Ren/Geng revealing imperial-exam fame even not revealing hidden branches得所 also有荣华. But fear Wu revealing gaining Jia制之 then-auspicious. Jia must隔位 fear greedy Ji合 conversely covering Metal-光 also blocking Ren Water flow lowly pattern. Also fear Geng revealing制Jia. Or only有Goat-palace one Ji seeing Ren Water also為wet-mud cannot見Jia Jia revealing conversely ordinary. Generally one-Ren one-Ji seeing Geng without-Jia才妙 same as 5th month using Ji/Ren.
  Or Ding/Yi revealing also有Geng/Ren prominent-noble. Without Ren否. Or branches form Wood Frame gaining Ren revealing also有Geng Metal generating Water源 can-say wealth-nobility.

- **核心要点**：
  - **首要用神**：壬水庚金
  - **配合**：一壬一己（湿泥生金）
  - **忌神**：戊土太多甲木贪合

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_425]` `[trigger: 辛生未月]` `[factor_trigger: month_wei AND tiangan_xin AND tiangan_ren AND tiangan_geng]` `[role: 主干]` 六月辛金，己土当权，辅助太多，恐掩金光，先用壬水，取庚佐之。 → 《穷通宝鉴·三夏辛金》#34.10
  - `[ns_qttbj_426]` `[trigger: 壬庚两透]` `[factor_trigger: month_wei AND tiangan_xin AND ren_revealed AND geng_revealed]` `[role: 条件分支]` 壬庚两透，科甲功名，即不出干，藏支得所，亦有荣华。 → 《穷通宝鉴·三夏辛金》#34.10
  - `[ns_qttbj_427]` `[trigger: 甲贪己合]` `[factor_trigger: month_wei AND tiangan_xin AND tiangan_jia AND jia_ji_adjacent AND greedy_ji_he]` `[role: 例外处理]` 甲须隔位，恐贪己合，反掩金光，又塞壬水之流，下贱之格。 → 《穷通宝鉴·三夏辛金》#34.10"""
    normalized_text_zh: str = """"""
    subject: str = "10. 六月辛金（未月）"
    factor_refs: list = ['cover_metal_guang', 'greedy_ji_he', 'wet_mud']
    
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
        book_id="qiongtongbaojian",
        chapter="",
        l1_anchor="qtbj_v1.0.0_10__六月辛金_未月_001_L1",
    )
    version: str = "1.0.0"
