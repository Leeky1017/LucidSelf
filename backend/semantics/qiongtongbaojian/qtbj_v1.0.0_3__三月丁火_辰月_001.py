"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.596865
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
    semantic_id="qtbj_v1.0.0_3__三月丁火_辰月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 3三月丁火辰月(SemanticEntry):
    """
    - **原文（source_text）**：
  三月丁火，戊土司令，泄弱丁气，先用甲木引丁制土，次看庚金。
  庚甲两透，定主科甲。或一藏一透，终非白丁。
  或支成木局，取庚为先。得庚透，丁癸不透...
    """
    
    original_text: str = """- **原文（source_text）**：
  三月丁火，戊土司令，泄弱丁气，先用甲木引丁制土，次看庚金。
  庚甲两透，定主科甲。或一藏一透，终非白丁。
  或支成木局，取庚为先。得庚透，丁癸不透，亦有异路功名。
  或支成水局，加以壬透，名杀重身轻，必夭折天年。或遭凶死。或戊己两透，廊庙之客。若一甲破，定是常人。

- **分字分词释义**：
  - **戊土司令**：戊土掌管时令 / 辰月 / 伤官当权
  - **泄弱丁气**：泄耗减弱丁火气势 / 伤官泄身 / 病象
  - **引丁制土**：引燃丁火制约土气 / 甲木功能 / 核心
  - **终非白丁**：终究不是普通百姓 / 有功名 / 次等
  - **廊庙之客**：朝廷殿堂的座上客 / 高官 / 食伤制杀
  - **夭折天年**：提前结束寿命 / 杀重身轻 / 极凶

- **规范化释义（primary_lang_explained）**：
  三月（辰月）的丁火，戊土（伤官）司令，泄弱了丁火的气势。先用甲木（印）引燃丁火并制约戊土（伤官配印），其次看庚金（劈甲）。
  庚金和甲木两透，定主科甲功名。如果一个藏支一个透干，终究不是白丁（普通百姓）。
  如果地支合成木局（印旺），取庚金（财）为先（损印）。得到庚金透出，丁火癸水不透（避免比劫争财或七杀泄财），也有异路功名。
  如果地支合成水局，加上壬水透出，叫“杀重身轻”，必定夭折短寿，或者遭遇凶死。如果戊己土两透（食伤制杀），是廊庙之客（高官）。如果被一个甲木破了土（印制食伤，导致杀无制），定是常人。

- **完整对等诠释（secondary_lang_full）**：
  Ding Fire in the 3rd Month (Dragon Month): Wu Earth commands, leaking the weak Ding Qi. First use Jia Wood to ignite Ding and control Earth (Seal matching Hurting Officer), then look at Geng Metal.
  If Geng and Jia are both revealed, Civil Service is certain. If one hidden and one revealed, one is not a commoner.
  If branches form a Wood frame, prioritize Geng. If Geng is revealed and Ding/Gui are not, it implies alternative fame.
  If branches form a Water frame and Ren is revealed, it is "Heavy Killing Weak Body", implying premature death or violent end. If Wu/Ji are both revealed (to control Killing), one is a guest of the Temple/Court (High Official). If one Jia breaks the Earth, one is certainly ordinary.

- **核心要点**：
  - **伤官配印**：辰月土旺泄丁，喜甲木制土生身。
  - **劈甲**：甲木需庚金劈，故庚甲配合最佳。
  - **杀重身轻**：水局壬透，丁火极弱，必夭。
  - **食伤制杀**：水多喜戊制。此时忌甲木破戊。

- **详细解说**：
  - 辰月伤官当令，丁火气泄。
  - “先甲后庚”：甲是根本（生身），庚是工具（劈甲）。
  - 这里的矛盾在于：一般喜甲制土，但在杀重（水多）需土制杀时，甲木反成忌神（制去救星戊土）。需灵活辨析。
- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_270]` `[trigger: 辰月丁火]` `[factor_trigger: month_chen AND tiangan_ding AND tiangan_jia AND tiangan_geng AND hurting_officer_match_seal]` `[role: 主干]` 三月丁火，戊土司令，泄弱丁气，先用甲木引丁制土，次看庚金。 → 《穷通宝鉴·三春丁火》#16.3
  - `[ns_qttbj_271]` `[trigger: 廊庙之客]` `[factor_trigger: month_chen AND tiangan_ding AND dizhi_water_frame AND tiangan_ren AND tiangan_wu AND tiangan_ji AND food_injury_control_killing]` `[role: 条件分支]` 支成水局，加以壬透，名杀重身轻，必夭折天年。或戊己两透，廊庙之客。 → 《穷通宝鉴·三春丁火》#16.3
  - `[ns_qttbj_272]` `[trigger: 伤官配印]` `[factor_trigger: month_chen AND tiangan_ding AND tiangan_geng AND tiangan_jia AND hurting_officer_match_seal]` `[role: 条件分支]` 庚甲两透，定主科甲。或一藏一透，终非白丁。 → 《穷通宝鉴·三春丁火》#16.3"""
    normalized_text_zh: str = """"""
    subject: str = "3. 三月丁火（辰月）"
    factor_refs: list = ['court_guest', 'killing_heavy_body_weak', 'commoner']
    
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
        l1_anchor="qtbj_v1.0.0_3__三月丁火_辰月_001_L1",
    )
    version: str = "1.0.0"
