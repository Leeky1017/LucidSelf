"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.597004
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
    semantic_id="qtbj_v1.0.0_2__五月戊土_午月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 2五月戊土午月(SemanticEntry):
    """
    - **原文（source_text）**：
  五月戊土，仲夏火炎，先看壬水，次取甲木，丙火酌用，用癸力微。
  壬甲两透，名君臣庆会，自然桃浪先声，权高位显，又得辛透年干，官居一品。
  一命、辛...
    """
    
    original_text: str = """- **原文（source_text）**：
  五月戊土，仲夏火炎，先看壬水，次取甲木，丙火酌用，用癸力微。
  壬甲两透，名君臣庆会，自然桃浪先声，权高位显，又得辛透年干，官居一品。
  一命、辛未、甲午、戊寅、壬子，壬甲两透。印旺杀高，出将入相，名播四夷。
  若支成火局，即透癸水，不能大济，是一杯水难济薪火也。人命合此，即好学不倦，亦不能成名，且主目疾。若得壬水出干，则非此比。
  又或土木重重，全无滴水，僧道孤贫之辈。

- **分字分词释义**：
  - **仲夏火炎**：盛夏火势炎热 / 午月特点 / 需水
  - **君臣庆会**：君主臣子欢庆聚会 / 壬甲两透 / 格局名
  - **桃浪先声**：桃花浪头先发声 / 科举高中 / 吉象
  - **权高位显**：权力高地位显赫 / 大贵 / 吉象
  - **出将入相**：出为将领入为宰相 / 极贵 / 吉象
  - **名播四夷**：名声传播四方蛮夷 / 大名 / 吉象
  - **杯水车薪**：一杯水救车薪之火 / 癸水无力 / 凶象
  - **目疾**：眼睛疾病 / 火土燥 / 凶象

- **规范化释义（primary_lang_explained）**：
  五月（午月）的戊土，仲夏火势炎热，先看壬水（调候/反克），次取甲木（疏土/生火/化杀？不，甲木在午月死地，此处主要用甲木生火还是制土？应是杀印相生或财滋弱杀，但午月火旺，甲木焚灭，故需壬水先润，再用甲木疏土）。丙火斟酌使用（火已旺），用癸水力量微弱（易被熬干）。
  壬水和甲木两透，叫“君臣庆会”（财杀相生），自然桃浪先声（科举高中），权高位显。如果又得辛金透出年干（伤官生财），官居一品。
  如果地支合成火局，即使透出癸水，也不能大济事，这是一杯水难救车薪之火。人命符合这种情况，即使好学不倦，也不能成名，而且主眼病（火土燥）。如果得到壬水出干，就不是这样比喻了（壬水力大）。
  又或者土木重重（比劫七杀），全无滴水，是僧道孤贫之辈（燥土不生金，木焚成灰）。

- **完整对等诠释（secondary_lang_full）**：
  Wu Earth in the 5th Month (Horse Month): Mid-summer Fire is blazing. First look for Ren Water, then take Jia Wood. Use Bing discreetly; Gui has weak power.
  If Ren and Jia are both revealed, it is "Ruler and Minister Celebrating Together", implying early success in exams, high power and status. Adding Xin revealed on Year Stem implies First Rank official.
  If branches form a Fire Frame, even if Gui reveals, it cannot help much; it is "A cup of water cannot save a wagon load of firewood on fire". Even if one studies tirelessly, fame is impossible, and eye disease is likely. If Ren reveals, it is different.
  Or if Earth and Wood are heavy without a drop of Water, it is a life of monks/Taoists, lonely and poor.

- **核心要点**：
  - **首要用神**：壬水（调候/财）。午月火炎土燥，非壬不救。
  - **配合**：甲木（疏土）。
  - **癸水无力**：杯水车薪，易被熬干。
  - **君臣庆会**：壬甲两透，极贵。

- **详细解说**：
  - 午月戊土羊刃（火生土旺），也是印旺。
  - 关键是“调候”。壬水通根（申子）有力，能制火润土，存得住。癸水无根易干。
  - “君臣庆会”：指财（壬）杀（甲）相生，财滋弱杀，杀印相生，格局大。
 
- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_508]` `[trigger: 午月戊土用神次序]` `[factor_trigger: month_wu AND tiangan_wu AND tiangan_ren AND tiangan_jia AND bing_careful AND gui_weak]` `[role: 主干]` 五月戊土，仲夏火炎，先看壬水，次取甲木，丙火酌用，用癸力微。 → 《穷通宝鉴·三夏戊土》#22.2
  - `[ns_qttbj_509]` `[trigger: 君臣庆会极贵]` `[factor_trigger: month_wu AND tiangan_wu AND tiangan_ren AND tiangan_jia AND ruler_minister]` `[role: 条件分支]` 壬甲两透，名君臣庆会，自然桃浪先声，权高位显。 → 《穷通宝鉴·三夏戊土》#22.2
  - `[ns_qttbj_510]` `[trigger: 辛透官居一品]` `[factor_trigger: month_wu AND tiangan_wu AND tiangan_ren AND tiangan_jia AND tiangan_xin AND first_rank_officer]` `[role: 条件分支]` 又得辛透年干，官居一品。 → 《穷通宝鉴·三夏戊土》#22.2
  - `[ns_qttbj_511]` `[trigger: 火局癸水杯水车薪]` `[factor_trigger: month_wu AND tiangan_wu AND dizhi_fire_frame AND tiangan_gui AND cup_water_wagon]` `[role: 例外处理]` 支成火局，即透癸水，不能大济，是一杯水难济薪火也。 → 《穷通宝鉴·三夏戊土》#22.2
  - `[ns_qttbj_512]` `[trigger: 火局癸水目疾]` `[factor_trigger: month_wu AND tiangan_wu AND dizhi_fire_frame AND tiangan_gui AND eye_disease]` `[role: 例外处理]` 人命合此，即好学不倦，亦不能成名，且主目疾。 → 《穷通宝鉴·三夏戊土》#22.2
  - `[ns_qttbj_513]` `[trigger: 土木重重无水僧道]` `[factor_trigger: month_wu AND tiangan_wu AND earth_wood_excessive AND NOT element_water AND monk_poor]` `[role: 例外处理]` 又或土木重重，全无滴水，僧道孤贫之辈。 → 《穷通宝鉴·三夏戊土》#22.2"""
    normalized_text_zh: str = """"""
    subject: str = "2. 五月戊土（午月）"
    factor_refs: list = ['ruler_minister', 'peach_waves', 'cup_water_wagon']
    
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
        l1_anchor="qtbj_v1.0.0_2__五月戊土_午月_001_L1",
    )
    version: str = "1.0.0"
