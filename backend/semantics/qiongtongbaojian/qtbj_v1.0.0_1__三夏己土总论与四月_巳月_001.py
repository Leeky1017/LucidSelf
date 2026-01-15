"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.597096
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
    semantic_id="qtbj_v1.0.0_1__三夏己土总论与四月_巳月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1三夏己土总论与四月巳月(SemanticEntry):
    """
    - **原文（source_text）**：
  三夏己土，杂气才官，禾稼在田，最喜甘沛，取癸为要，次用丙火。夏无太阳，禾稼不长，故无癸曰旱田，无丙曰孤阴。
  或丙癸两透，又加辛金生癸，此富贵之格，...
    """
    
    original_text: str = """- **原文（source_text）**：
  三夏己土，杂气才官，禾稼在田，最喜甘沛，取癸为要，次用丙火。夏无太阳，禾稼不长，故无癸曰旱田，无丙曰孤阴。
  或丙癸两透，又加辛金生癸，此富贵之格，名水火既济，鼎甲之人。却忌戊癸化合。
  或有丙无癸，有壬亦可，但不大发。
  或一派丙火烈土，加以丁火制辛，癸水无根，如七八月之间旱，则苗藁矣，此命孤苦零丁。或有甲木，又见丙火重重，无滴水解炎，亦孤贫到老。
  如有壬水，又见庚辛，此又不作孤看，但恐目疾，心肾肝脏之灾。若壬水有根，辛金得地，又非此而论。或壬癸并出，破火润土，此人聪慧特达，富中取贵，又转祸为福也。
  用癸者、金妻水子。用丙者，木妻火子。

- **分字分词释义**：
  - **禾稼在田**：庄稼在田里 / 夏月特点 / 需水
  - **甘沛**：甘霜雨沛 / 癸水 / 用神
  - **旱田**：干旱田地 / 无癸 / 凶象
  - **孤阴**：孤独阴冷 / 无丙 / 凶象
  - **水火既济**：水火相济 / 丙癸辛配合 / 格局名
  - **鼎甲之人**：状元榜眠探花 / 极贵 / 吉象
  - **苗藁**：禾苗枯槁 / 无水 / 凶象
  - **孤苦零丁**：孤独苦难无依 / 火旺无水 / 凶象
  - **转祸为福**：转祸害为福气 / 壬癸并出 / 吉象

- **规范化释义（primary_lang_explained）**：
  夏天的己土，杂气财官（指未月？或统称），禾稼在田里，最喜欢甘霖雨水（癸水），取癸水为首要，其次用丙火。夏天没有太阳，禾稼不能生长，所以没有癸水叫“旱田”，没有丙火叫“孤阴”。
  如果丙火癸水两透，又加上辛金（食神）生癸水，这是富贵之格，叫“水火既济”，是鼎甲（状元榜眼探花）之人。却忌讳戊土与癸水化合（合火或合绊）。
  如果有丙火无癸水，有壬水也可以，但不会大发（壬水不如癸水贴切）。
  如果一派丙火烈土，加上丁火制约辛金，癸水无根，就像七八月之间的旱灾，禾苗都枯槁了，这命孤苦零丁。或者有甲木，又见到丙火重重，没有一点水来解炎，也是孤贫到老。
  如果有壬水，又见到庚辛金（发水源），这就不作孤苦看，但恐怕有眼病（火克金？水受克？），或心肾肝脏的灾病。如果壬水有根，辛金得地，又不是这样论（则吉）。或者壬水癸水并出，破火润土，这人聪慧特达，富中取贵，又能转祸为福。

- **完整对等诠释（secondary_lang_full）**：
  Ji Earth in the Three Summer Months: Mixed Qi Wealth/Officer; crops are in the fields; most likes sweet rain. Prioritize Gui, then Bing. Without Sun in Summer, crops don't grow; thus without Gui it is "Drought Field", without Bing it is "Lonely Yin".
  If Bing and Gui both reveal, adding Xin to generate Gui, this is a wealthy/noble pattern, "Water/Fire Completed", a person of "Ding Jia" (Top 3 in exams). But dread Wu-Gui combination.
  With Bing but no Gui, Ren is acceptable, but not greatly prosperous.
  If there is a mass of Bing Fire/Scorched Earth, plus Ding controlling Xin, and Gui has no root, it is like a drought in the 7th/8th month; seedlings wither. This life is lonely and destitute. Or with Jia, seeing heavy Bing, without a drop of water to relieve heat, also lonely/poor till old age.
  If there is Ren Water, and Geng/Xin appear, do not view as lonely, but fear eye disease or heart/kidney/liver disasters. If Ren is rooted and Xin grounded, it is different (auspicious). Or if Ren/Gui both appear to break Fire and moisten Earth, the person is intelligent and outstanding, obtaining nobility amidst wealth, turning disaster to fortune.

- **核心要点**：
  - **首要用神**：癸水（润）。夏土燥，非水不救。
  - **配合**：丙（阳气）、辛（发水源）。
  - **水火既济**：丙癸辛配合，极贵。
  - **旱田**：无水则苗枯，孤贫。

- **详细解说**：
  - 三夏（巳午未）火旺土相。
  - 己土为田园，夏月最怕干枯。
  - “无癸曰旱田”：指无法生长庄稼。
  - “无丙曰孤阴”：指虽有水但无阳光，庄稼易霉烂（如梅雨季）。
  - 最佳气象是“阳光雨露”，即丙癸既济。
 
- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_589]` `[trigger: 三夏己土癸为要丙为辅]` `[factor_trigger: ji_born_summer AND likes_gui_moisten_field AND tiangan_gui AND tiangan_bing]` `[role: 主干]` 三夏己土，禾稼在田，最喜甘沛，取癸为要，次用丙火。 → 《穷通宝鉴·三夏己土》#26.1
  - `[ns_qttbj_590]` `[trigger: 夏无太阳禾稼不长]` `[factor_trigger: ji_born_summer AND NOT tiangan_bing AND crops_grains AND drought_field]` `[role: 主干依赖]` 夏无太阳，禾稼不长。 → 《穷通宝鉴·三夏己土》#26.1
  - `[ns_qttbj_591]` `[trigger: 无癸曰旱田无丙曰孤阴]` `[factor_trigger: ji_born_summer AND ((NOT tiangan_gui AND drought_field) OR (NOT tiangan_bing AND lonely_yin))]` `[role: 条件分支]` 故无癸曰旱田，无丙曰孤阴。 → 《穷通宝鉴·三夏己土》#26.1
  - `[ns_qttbj_592]` `[trigger: 丙癸辛水火既济鼎甲之人]` `[factor_trigger: ji_born_summer AND tiangan_bing AND tiangan_gui AND tiangan_xin AND water_fire_completed AND top_three]` `[role: 条件分支]` 丙癸两透，又加辛金生癸，此富贵之格，名水火既济，鼎甲之人。 → 《穷通宝鉴·三夏己土》#26.1
  - `[ns_qttbj_593]` `[trigger: 忌戊癸化合坏水火既济]` `[factor_trigger: ji_born_summer AND tiangan_wu AND tiangan_gui AND wu_gui_combine AND NOT water_fire_completed]` `[role: 例外处理]` 水火既济之格，却忌戊癸化合。 → 《穷通宝鉴·三夏己土》#26.1
  - `[ns_qttbj_594]` `[trigger: 有丙无癸得壬不大发]` `[factor_trigger: ji_born_summer AND tiangan_bing AND NOT tiangan_gui AND tiangan_ren AND moderate_weath]` `[role: 条件分支]` 或有丙无癸，有壬亦可，但不大发。 → 《穷通宝鉴·三夏己土》#26.1
  - `[ns_qttbj_595]` `[trigger: 一派丙火丁制辛癸无根苗藁孤苦]` `[factor_trigger: ji_born_summer AND fire_excessive AND tiangan_bing AND tiangan_ding AND tiangan_xin AND NOT gui_rooted AND withered_seedlings AND lonely_poor]` `[role: 例外处理]` 一派丙火烈土，加以丁火制辛，癸水无根，如七八月之间旱，则苗藁矣，此命孤苦零丁。 → 《穷通宝鉴·三夏己土》#26.1
  - `[ns_qttbj_596]` `[trigger: 甲见丙重重无水孤贫到老]` `[factor_trigger: ji_born_summer AND tiangan_jia AND fire_excessive AND NOT (tiangan_ren OR tiangan_gui) AND lonely_poor]` `[role: 例外处理]` 或有甲木，又见丙火重重，无滴水解炎，亦孤贫到老。 → 《穷通宝鉴·三夏己土》#26.1
  - `[ns_qttbj_597]` `[trigger: 壬水庚辛发源不作孤看惟恐目疾]` `[factor_trigger: ji_born_summer AND tiangan_ren AND (tiangan_geng OR tiangan_xin) AND water_rooted AND eye_disease_risk]` `[role: 条件分支]` 如有壬水，又见庚辛，此又不作孤看，但恐目疾，心肾肝脏之灾。 → 《穷通宝鉴·三夏己土》#26.1
  - `[ns_qttbj_598]` `[trigger: 壬癸并出破火润土转祸为福]` `[factor_trigger: ji_born_summer AND tiangan_ren AND tiangan_gui AND break_fire AND moisten_earth AND turn_misfortune_blessing]` `[role: 总结]` 或壬癸并出，破火润土，此人聪慧特达，富中取贵，又转祸为福。 → 《穷通宝鉴·三夏己土》#26.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 三夏己土总论与四月（巳月）"
    factor_refs: list = ['drought_field', 'withered_seedlings', 'top_three', 'water_fire_completed']
    
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
        l1_anchor="qtbj_v1.0.0_1__三夏己土总论与四月_巳月_001_L1",
    )
    version: str = "1.0.0"
