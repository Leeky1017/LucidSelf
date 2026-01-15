"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578412
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
    semantic_id="qtbj_v1.0.0_2__十月辛金_亥月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 2十月辛金亥月(SemanticEntry):
    """
    - **原文（source_text）**：
  十月辛金，时值小阳，阳气渐升，寒气将降，先用壬水，次取丙火，壬丙两透，金榜题名，何也？盖辛金有壬水丙火，名金白水清，又在亥月故发。丙透壬藏，采芹之造。...
    """
    
    original_text: str = """- **原文（source_text）**：
  十月辛金，时值小阳，阳气渐升，寒气将降，先用壬水，次取丙火，壬丙两透，金榜题名，何也？盖辛金有壬水丙火，名金白水清，又在亥月故发。丙透壬藏，采芹之造。丙藏壬透，富有千金。壬丙在支，聪明之士。
  戊壬在柱，积富之人。或壬多无戊，名辛水汪洋，反成贫贱。戊多壬少，又主成名。或甲多戊少，因艺术而蓄金。
  若己多有戊，壬水被困，金被埋，不过诚实之人。或壬癸多无戊丙者，劳碌辛苦。十月辛金，先壬后丙，余皆参用。

- **分字分词释义**：
  - **小阳**：立冬时节 / 阳气初升 / 亥月特点
  - **金白水清**：金气清白水质澄澈 / 辛壬丙配合 / 格局名
  - **金榜题名**：科举高中 / 进士 / 吉象
  - **千金**：千两金 / 大富 / 吉象
  - **辛水汪洋**：辛金生水太多 / 壬多无戊 / 凶象
  - **艺术蓄金**：靠技艺积累财富 / 甲多戊少 / 次吉
  - **积富**：积累财富 / 戊壬配合 / 吉象
  - **劳碌辛苦**：辛勤劳累 / 壬癸多无戊丙 / 凶象

- **规范化释义（primary_lang_explained）**：
  十月（亥月）辛金，时值小阳（立冬），阳气渐升寒气将降，先用壬水（淘洗），次取丙火（暖局）。壬丙两透金榜题名。为何？因为辛金有壬水丙火，名"金白水清"，又在亥月故发（亥为壬水本家）。丙透壬藏采芹之造。丙藏壬透富有千金。壬丙在支聪明之士。
  戊壬在柱（戊土止水），积富之人。或壬多无戊名"辛水汪洋"（身弱财多）反成贫贱。戊多壬少又主成名。或甲多戊少因艺术而蓄金（伤官生财）。
  若己多有戊壬水被困金被埋不过诚实之人。或壬癸多无戊丙者劳碌辛苦。十月辛金先壬后丙余皆参用。

- **完整对等诠释（secondary_lang_full）**：
  Xin Metal in 10th Month (Pig Month): Small Yang time, yang qi rising cold descending. First Ren then Bing. Ren/Bing revealing Jinbang Imperial exam. Why? Xin Metal with Ren/Bing name "Gold White Water Clear" in Hai month manifests. Bing reveals Ren hidden scholar造. Bing hidden Ren reveals wealthy. Ren/Bing in branches clever scholar.
  Wu/Ren in pillars accumulated wealth. If Ren many without Wu name "Xin Water Vast" conversely poor. Wu many Ren few also成名. If Jia many Wu few wealth via arts.
  If Ji many with Wu Ren trapped Metal buried merely honest. If Ren/Gui many without Wu/Bing toil hardship. 10th month Xin: first Ren then Bing others参用.

- **核心要点**：
  - **首要用神**：壬丙配合。壬淘洗丙暖局
  - **格局**：金白水清（Xin+Ren+Bing）
  - **忌神**：壬多无戊（水泛）己戊困水埋金

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_374]` `[trigger: 辛生亥月]` `[factor_trigger: month_hai AND tiangan_xin AND tiangan_ren AND tiangan_bing]` `[role: 主干]` 十月辛金，时值小阳，先用壬水，次取丙火，壬丙两透，金榜题名。 → 《穷通宝鉴·三冬辛金》#34.2
  - `[ns_qttbj_375]` `[trigger: 金白水清]` `[factor_trigger: month_hai AND tiangan_xin AND tiangan_ren AND tiangan_bing AND gold_white_water_clear]` `[role: 条件分支]` 辛金有壬水丙火，名金白水清，又在亥月故发。 → 《穷通宝鉴·三冬辛金》#34.2
  - `[ns_qttbj_376]` `[trigger: 辛水汪洋]` `[factor_trigger: month_hai AND tiangan_xin AND ren_excessive AND NOT tiangan_wu]` `[role: 例外处理]` 或壬多无戊，名辛水汪洋，反成贫贱。 → 《穷通宝鉴·三冬辛金》#34.2"""
    normalized_text_zh: str = """"""
    subject: str = "2. 十月辛金（亥月）"
    factor_refs: list = ['small_yang_season', 'gold_white_water_clear', 'xin_water_vast']
    
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
        l1_anchor="qtbj_v1.0.0_2__十月辛金_亥月_001_L1",
    )
    version: str = "1.0.0"
