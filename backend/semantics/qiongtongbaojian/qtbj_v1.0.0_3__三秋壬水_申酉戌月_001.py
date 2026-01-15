"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578626
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
    semantic_id="qtbj_v1.0.0_3__三秋壬水_申酉戌月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 3三秋壬水申酉戌月(SemanticEntry):
    """
    - **原文（source_text）**：
  **七月壬水**，庚金司令，壬得申之长生，源流自远，转弱为强，专用戊土，次取丁火佐戊制庚。但用辰戌之戊，不用申中受病之戊。戊丁俱透，科甲生员。戊透天干...
    """
    
    original_text: str = """- **原文（source_text）**：
  **七月壬水**，庚金司令，壬得申之长生，源流自远，转弱为强，专用戊土，次取丁火佐戊制庚。但用辰戌之戊，不用申中受病之戊。戊丁俱透，科甲生员。戊透天干，丁藏午戌，恩封可待。
  或四柱多壬，戊又透干，名假杀化权，阆苑之仙。支中见甲，亦不忌也。
  或戊多而透，得一甲制，略富贵，无甲常人。或一派甲木，又见火多，无庚出者，别祖离乡，随缘度日。
  **八月壬水**，辛金司权，正金白水清，忌戊土为病，专用甲木。甲木一透制戊，壬水澈底澄清，名高翰苑。若甲出时干，功名显达，设见庚破，又属常人。即甲藏支、无庚，秀才可许。
  或无戊、多金水者，主人清才浊，困苦寒儒。无甲用金，发水之源，名独水三犯庚辛，号曰体全之象。
  **九月壬水**，进气，其性特厚，若一派壬水，见一甲、制戌中之戊，戊又出干，斯用丙火。此格清贵极矣，正合一将当关，群邪自伏。
  或一派戊土，无一己庚杂乱，得一甲透时干。玉堂清贵。
  九月壬水，专用甲木，次用丙火。用土者，火妻土子。

- **分字分词释义**：
  - **庚金司令**：庚金当令 / 申月 / 印旺
  - **源流自远**：水源远流长 / 长生之地 / 身强
  - **转弱为强**：由弱变强 / 得印生 / 格局变化
  - **假杀化权**：假七杀化为权柄 / 戊透多壬 / 格局名
  - **阆苑之仙**：蓬莱仙境之仙人 / 大贵 / 吉象
  - **金白水清**：金气清白水质澄澈 / 酉月壬水 / 吉象
  - **澈底澄清**：彻底澄清 / 甲木制土 / 吉象
  - **翰苑**：翰林院 / 高官 / 吉象
  - **独水三犯庚辛**：单独水遇多金 / 从印格 / 格局名
  - **玉堂清贵**：翰林之贵 / 甲透戊制 / 吉象

- **规范化释义（primary_lang_explained）**：
  **七月（申月）壬水**：庚金司令，壬得申长生，源流自远，转弱为强。专用戊土（堤防），次取丁火佐戊制庚（丁火生土制金）。戊丁俱透，科甲生员。或四柱多壬，戊又透干，名"假杀化权"，阆苑之仙（贵格）。
  **八月（酉月）壬水**：辛金司权，正"金白水清"。忌戊土为病（己土亦忌，混浊），专用甲木（去土）。甲木一透制戊，壬水彻底澄清，名高翰苑。无戊、多金水者，人清才浊，困苦寒儒。若无甲用金（印），名"独水三犯庚辛"，号曰"体全之象"（从印）。
  **九月（戌月）壬水**：壬水进气，其性特厚。若一派壬水，见一甲制戌中之戊，戊又出干，斯用丙火（食神生财制杀？不，甲制戊，丙暖局）。专用甲木（疏土），次用丙火（暖局）。

- **完整对等诠释（secondary_lang_full）**：
  **7th Month (Monkey) Ren Water**: Geng commands, Ren gets Longevity in Shen, strong source. Focus on Wu Earth (dike), then Ding Fire (assist Wu, control Geng). Wu/Ding revealing, exam fame. If many Ren, Wu revealing, "Fake Killing Transforming Power", very noble.
  **8th Month (Rooster) Ren Water**: Xin commands, "Gold White Water Clear". Fear Wu Earth sickness, focus on Jia Wood (control Earth). Jia revealing controlling Wu, Ren thoroughly clear, high fame. If no Wu, many Metal/Water, clear person but muddy talent, poor scholar. If no Jia use Metal, "Single Water Violating Geng/Xin Thrice", "Body Complete Image".
  **9th Month (Dog) Ren Water**: Ren Qi advancing, nature thick. If many Ren, see one Jia controlling Xu's Wu, Wu revealing, use Bing. Focus on Jia Wood (dredge), then Bing Fire.

- **核心要点**：
  - **七月**：母旺子相，喜戊土堤防，丁火辅佐。
  - **八月**：金白水清，忌土混浊，喜甲木去土。
  - **九月**：土旺水气进，喜甲木疏土，丙火暖局。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_433]` `[trigger: 壬生申月]` `[factor_trigger: month_shen AND tiangan_ren AND tiangan_wu AND tiangan_ding AND source_flow_far]` `[role: 主干]` 七月壬水，庚金司令，壬得申之长生，源流自远，转弱为强，专用戊土。 → 《穷通宝鉴·论壬水》#36.3
  - `[ns_qttbj_434]` `[trigger: 假杀化权]` `[factor_trigger: month_shen AND tiangan_ren AND ren_multiple AND wu_revealed AND fake_killing_power]` `[role: 条件分支]` 或四柱多壬，戊又透干，名假杀化权，阆苑之仙。 → 《穷通宝鉴·论壬水》#36.3
  - `[ns_qttbj_435]` `[trigger: 壬生酉月]` `[factor_trigger: month_you AND tiangan_ren AND tiangan_jia AND gold_white_water_clear]` `[role: 主干]` 八月壬水，辛金司权，正金白水清，忌戊土为病，专用甲木。 → 《穷通宝鉴·论壬水》#36.3
  - `[ns_qttbj_436]` `[trigger: 壬生戌月]` `[factor_trigger: month_xu AND tiangan_ren AND tiangan_jia AND tiangan_bing AND qi_advancing]` `[role: 主干]` 九月壬水，进气，其性特厚，专用甲木，次用丙火。 → 《穷通宝鉴·论壬水》#36.3"""
    normalized_text_zh: str = """"""
    subject: str = "3. 三秋壬水（申酉戌月）"
    factor_refs: list = ['fake_killing_power', 'gold_white_water_clear', 'body_complete_image']
    
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
        l1_anchor="qtbj_v1.0.0_3__三秋壬水_申酉戌月_001_L1",
    )
    version: str = "1.0.0"
