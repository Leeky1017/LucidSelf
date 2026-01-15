"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578614
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
    semantic_id="qtbj_v1.0.0_2__三夏壬水_巳午未月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 2三夏壬水巳午未月(SemanticEntry):
    """
    - **原文（source_text）**：
  **四月壬水**，丙火司权，水弱极矣，专取壬水比肩为助，次取辛金发源，且暗合丙火，庚金为佐。壬辛两透，金榜有名，或癸辛两出，加以甲透，亦主异路之荣。无...
    """
    
    original_text: str = """- **原文（source_text）**：
  **四月壬水**，丙火司权，水弱极矣，专取壬水比肩为助，次取辛金发源，且暗合丙火，庚金为佐。壬辛两透，金榜有名，或癸辛两出，加以甲透，亦主异路之荣。无甲者、富贵门下之客。
  如无壬，木少火多者，又作弃命从才格，因妻致富。癸透者残疾。
  或四柱多金得地，则极弱复强，须用巳中戊土，亦主名利双全。
  **五月壬水**，丁旺壬弱，取癸为用，取庚为佐。无庚不能发水，无癸不能伤丁。五月壬水，辛癸亦可参用，其理与四月皆同。
  庚癸两透，科甲必然，庚壬两透，官居极品。有庚无壬癸者、常人。
  或支成火局，全无金水，名才多身弱，富屋贫人。若又甲乙多者，僧道之命。
  **六月壬水**，己土当权，丁火退气，先用辛金癸水，次用甲木噼土。六月壬水，先辛后甲，次取癸水。辛甲两透，富贵清高。
  或一派己土，此假从杀格，为人奸诈，且主孤贫，得甲乙出制可救。凡土居生旺之地，须用木制方妙。或支成木局，泄水太过，当用金水为贵。

- **分字分词释义**：
  - **丙火司权**：丙火当令掌权 / 巳月 / 水绝
  - **水弱极矣**：水极其虚弱 / 夏水涸 / 需比肩
  - **暗合丙火**：辛金暗合丙火 / 辛丙合 / 合杀
  - **弃命从才**：舍弃日主从财星 / 变格 / 因妻致富
  - **丁旺壬弱**：丁火旺壬水弱 / 午月 / 官旺身弱
  - **才多身弱**：财多身弱 / 火多水少 / 凶象
  - **富屋贫人**：住富人房子的穷人 / 有名无实 / 凶象
  - **己土当权**：己土当令 / 未月 / 土旺
  - **噼土**：劈开土 / 甲木制土 / 用神
  - **假从杀格**：假从七杀格 / 似从非从 / 变格

- **规范化释义（primary_lang_explained）**：
  **四月（巳月）壬水**：丙火司权，水弱极矣。专取壬水比肩为助，次取辛金发源（且辛暗合丙火），庚金为佐。壬辛两透，金榜有名。如无壬，木少火多者，作"弃命从才格"，因妻致富。
  **五月（午月）壬水**：丁旺壬弱，取癸为用（伤丁），取庚为佐（发水）。无庚不能发水，无癸不能伤丁。庚癸两透，科甲必然。或支成火局，全无金水，名"才多身弱"，富屋贫人。
  **六月（未月）壬水**：己土当权，丁火退气。先用辛金（发源）、癸水（助身），次用甲木劈土（疏己土）。辛甲两透，富贵清高。或一派己土，为"假从杀格"，为人奸诈孤贫，得甲乙出制可救。

- **完整对等诠释（secondary_lang_full）**：
  **4th Month (Snake) Ren Water**: Bing Fire commands, Water extremely weak. Focus on Ren Parallel help, next Xin Metal source (also secret combine Bing), Geng assist. Ren/Xin revealing, exam fame. If no Ren, Wood scarce Fire many, "Abandon Life Follow Wealth Pattern", wealth via wife.
  **5th Month (Horse) Ren Water**: Ding prosperous Ren weak. Take Gui to use (hurt Ding), Geng to assist (generate Water). Without Geng cannot generate, without Gui cannot hurt Ding. Geng/Gui revealing, exam success certain. If Fire Frame, no Metal/Water, "Wealth Heavy Body Weak", poor man in rich house.
  **6th Month (Goat) Ren Water**: Ji Earth commands, Ding Fire retreating. First use Xin (source) Gui (help), then Jia split Earth. Xin/Jia revealing, wealthy noble pure. If all Ji Earth, "Fake Follow Killing Pattern", cunning/poor, Jia/Yi control can save.

- **核心要点**：
  - **四五月**：火旺水弱，喜比劫（壬癸）帮身，印绶（庚辛）生身。
  - **六月**：土旺金相，喜辛金发源，甲木疏土。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_387]` `[trigger: 壬生巳月]` `[factor_trigger: month_si AND tiangan_ren AND shishen_parallel AND tiangan_xin]` `[role: 主干]` 四月壬水，丙火司权，水弱极矣，专取壬水比肩为助，次取辛金发源。 → 《穷通宝鉴·论壬水》#36.2
  - `[ns_qttbj_388]` `[trigger: 壬生午月]` `[factor_trigger: month_wu AND tiangan_ren AND tiangan_gui AND tiangan_geng]` `[role: 主干]` 五月壬水，丁旺壬弱，取癸为用，取庚为佐。无庚不能发水，无癸不能伤丁。 → 《穷通宝鉴·论壬水》#36.2
  - `[ns_qttbj_389]` `[trigger: 壬生未月]` `[factor_trigger: month_wei AND tiangan_ren AND tiangan_xin AND tiangan_gui AND tiangan_jia]` `[role: 主干]` 六月壬水，己土当权，丁火退气，先用辛金癸水，次用甲木噼土。 → 《穷通宝鉴·论壬水》#36.2
  - `[ns_qttbj_390]` `[trigger: 才多身弱]` `[factor_trigger: month_wu AND tiangan_ren AND dizhi_fire_frame AND NOT element_metal AND NOT element_water AND rich_house_poor_man]` `[role: 例外处理]` 或支成火局，全无金水，名才多身弱，富屋贫人。 → 《穷通宝鉴·论壬水》#36.2"""
    normalized_text_zh: str = """"""
    subject: str = "2. 三夏壬水（巳午未月）"
    factor_refs: list = ['abandon_follow_wealth', 'rich_house_poor_man', 'fake_follow_killing']
    
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
        l1_anchor="qtbj_v1.0.0_2__三夏壬水_巳午未月_001_L1",
    )
    version: str = "1.0.0"
