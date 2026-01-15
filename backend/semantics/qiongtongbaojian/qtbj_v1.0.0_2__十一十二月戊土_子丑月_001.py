"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.597055
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
    semantic_id="qtbj_v1.0.0_2__十一十二月戊土_子丑月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 2十一十二月戊土子丑月(SemanticEntry):
    """
    - **原文（source_text）**：
  十一二月严寒冰冻，丙火为专，甲木为佐。
  丙甲两透，桃浪之人，丙出甲藏，采芹食饩。丙藏甲出，佐杂前程。有丙无甲者，豪富。有甲无丙者，清贫。丙甲全无，...
    """
    
    original_text: str = """- **原文（source_text）**：
  十一二月严寒冰冻，丙火为专，甲木为佐。
  丙甲两透，桃浪之人，丙出甲藏，采芹食饩。丙藏甲出，佐杂前程。有丙无甲者，豪富。有甲无丙者，清贫。丙甲全无，下流之造。
  或一派丙火，加以丙透，运值火土，弱中复强，又一壬透，主清高荣禄。乏壬、僧道孤寒。
  或一派壬水，不见比劫，可作从才而论。即有比劫，得甲出干，又主富贵，若寒土无丙，虽有甲木，亦是内虚外实之人。
  或二癸透月时，名为争合，终属劳碌之人。得一己出干制癸，反为忠义之士，舍己从人而论。
  年月透辛金者，又属土金伤官，异路功名可许。以金为妻、水为子。

- **分字分词释义**：
  - **严寒冰冻**：极寒结冰、土冻不灵 / 子丑月特点 / 调候首要
  - **丙火为专**：专门使用丙火 / 解冻暖土 / 首要用神
  - **桃浪**：科举及第 / 进士 / 贵格
  - **采芹食饩**：入学食俸 / 秀才待遇 / 中等功名
  - **佐杂**：佐贰杂职 / 小官吏 / 次等功名
  - **豪富**：巨富 / 有印无杀 / 偏于财富
  - **清贫**：穷困 / 有杀无印 / 贫格
  - **从才**：从财格 / 水多顺势 / 变格
  - **争合**：争相合化 / 二癸合戊 / 凶象
  - **舍己从人**：舍弃私欲顺从正理 / 己土制癸 / 救应

- **规范化释义（primary_lang_explained）**：
  十一月（子月）十二月（丑月）严寒冰冻，专用丙火（解冻），甲木辅佐（生火/疏土）。
  丙火甲木两透，科举及第（桃浪）的人。丙火透出甲木藏支，秀才食饩。丙火藏支甲木透出，佐杂（小官）前程。有丙火无甲木，豪富（有印无杀）。有甲木无丙火，清贫（杀重无印）。丙甲全无，下流的命造。
  如果一派丙火，加上丙火透出，大运遇到火土，戊土由弱转强，又见一个壬水透出（反克/既济），主清高荣禄。缺乏壬水，僧道孤寒（火炎土燥）。
  如果一派壬水，不见比劫，可以作“从财格”论。即使有比劫，得到甲木出干（化杀/泄财生杀），又主富贵。如果寒土没有丙火，虽然有甲木，也是“内虚外实”的人。
  如果两个癸水透在月时，叫“争合”（戊癸合），终究属于劳碌的人。得到一个己土出干制约癸水，反而是忠义之士，按“舍己从人”（舍弃私情服从正理）论。
  年月透出辛金的人，属于“土金伤官”，可以许诺异路功名。以金为妻，水为子。

- **完整对等诠释（secondary_lang_full）**：
  Wu Earth in the 11th/12th Months (Rat/Ox): Severe cold and freezing; exclusively use Bing, with Jia as assistant.
  If Bing and Jia are both revealed, one passes exams. Bing revealed and Jia hidden implies a Xiucai receiving stipend. Bing hidden and Jia revealed implies minor official career. With Bing but no Jia, wealthy. With Jia but no Bing, poor. Without Bing/Jia, a lowly life.
  If there is a mass of Bing Fire, and Bing reveals, with Luck in Fire/Earth, Weakness turns to Strength; having one Ren reveal implies purity and glory. Lacking Ren, one is a monk/Taoist, lonely and cold.
  If there is a mass of Ren Water without Parallels, view as "Follow Wealth". Even with Parallels, if Jia reveals, it implies wealth and nobility. If Cold Earth lacks Bing, even with Jia, one is "Hollow Inside Solid Outside".
  If two Guis reveal in Month/Hour, it is "Competing to Combine", implying a life of toil. Obtaining one Ji to control Gui makes a loyal and righteous person, "Sacrificing Self to Follow Others".
  If Xin reveals in Year/Month, it is Earth-Metal Hurting Officer, promising alternative fame. Metal as Wife, Water as Child.

- **核心要点**：
  - **严寒专用**：子丑月冻土，非丙不暖，非甲不灵。
  - **丙甲配置**：两透贵，有丙富，有甲贫。
  - **从财**：水多无劫，从财。
  - **争合**：二癸争戊，劳碌。喜己土解围。

- **详细解说**：
  - 子丑月，戊土处死墓之地。
  - 关键在于“解冻”。丙火是太阳，不可或缺。
  - “内虚外实”：指有甲疏土（外表有威仪），但无丙生身（内在无生气），故虚。
  - “争合”：戊癸合在冬月易化火（见丙）或化水（见水局），若争合则情专志乱。
 
- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_548]` `[trigger: 冬月戊土专用丙甲]` `[factor_trigger: (month_zi OR month_chou) AND tiangan_wu AND tiangan_bing AND tiangan_jia AND severe_cold]` `[role: 主干]` 十一二月严寒冰冻，丙火为专，甲木为佐。 → 《穷通宝鉴·三冬戊土》#24.2
  - `[ns_qttbj_549]` `[trigger: 丙甲两透桃浪之人]` `[factor_trigger: (month_zi OR month_chou) AND tiangan_wu AND tiangan_bing AND tiangan_jia AND peach_waves]` `[role: 条件分支]` 丙甲两透，桃浪之人。 → 《穷通宝鉴·三冬戊土》#24.2
  - `[ns_qttbj_550]` `[trigger: 丙出甲藏采芹食饩]` `[factor_trigger: (month_zi OR month_chou) AND tiangan_wu AND bing_revealed AND jia_in_branch AND xiucai_stipend]` `[role: 条件分支]` 丙出甲藏，采芹食饩。 → 《穷通宝鉴·三冬戊土》#24.2
  - `[ns_qttbj_551]` `[trigger: 丙藏甲出佐杂前程]` `[factor_trigger: (month_zi OR month_chou) AND tiangan_wu AND bing_in_branch AND tiangan_jia AND minor_official]` `[role: 条件分支]` 丙藏甲出，佐杂前程。 → 《穷通宝鉴·三冬戊土》#24.2
  - `[ns_qttbj_552]` `[trigger: 有丙无甲豪富]` `[factor_trigger: (month_zi OR month_chou) AND tiangan_wu AND tiangan_bing AND NOT tiangan_jia AND wealthy_only]` `[role: 条件分支]` 有丙无甲者，豪富。 → 《穷通宝鉴·三冬戊土》#24.2
  - `[ns_qttbj_553]` `[trigger: 有甲无丙清贫]` `[factor_trigger: (month_zi OR month_chou) AND tiangan_wu AND tiangan_jia AND NOT tiangan_bing AND poor_scholar]` `[role: 条件分支]` 有甲无丙者，清贫。 → 《穷通宝鉴·三冬戊土》#24.2
  - `[ns_qttbj_554]` `[trigger: 丙甲全无下流之造]` `[factor_trigger: (month_zi OR month_chou) AND tiangan_wu AND NOT tiangan_bing AND NOT tiangan_jia AND lowly_status]` `[role: 例外处理]` 丙甲全无，下流之造。 → 《穷通宝鉴·三冬戊土》#24.2
  - `[ns_qttbj_555]` `[trigger: 一派丙火逢壬清高荣禄]` `[factor_trigger: (month_zi OR month_chou) AND tiangan_wu AND fire_excessive AND tiangan_bing AND tiangan_ren AND clear_noble]` `[role: 条件分支]` 一派丙火，加以丙透，运值火土，又一壬透，主清高荣禄。 → 《穷通宝鉴·三冬戊土》#24.2
  - `[ns_qttbj_556]` `[trigger: 乏壬僧道孤寒]` `[factor_trigger: (month_zi OR month_chou) AND tiangan_wu AND fire_excessive AND tiangan_bing AND NOT tiangan_ren AND monk_poor]` `[role: 例外处理]` 乏壬，僧道孤寒。 → 《穷通宝鉴·三冬戊土》#24.2
  - `[ns_qttbj_557]` `[trigger: 一派壬水从财与甲出富贵]` `[factor_trigger: (month_zi OR month_chou) AND tiangan_wu AND ren_multiple AND NOT parallels_present AND follow_wealth_pattern]` `[role: 条件分支]` 或一派壬水，不见比劫，可作从才而论；即有比劫，得甲出干，又主富贵。 → 《穷通宝鉴·三冬戊土》#24.2
  - `[ns_qttbj_558]` `[trigger: 二癸争合劳碌与己出忠义]` `[factor_trigger: (month_zi OR month_chou) AND tiangan_wu AND gui_double AND competing_combination_toil]` `[role: 例外处理]` 或二癸透月时，名为争合，终属劳碌之人；得一己出干制癸，反为忠义之士。 → 《穷通宝鉴·三冬戊土》#24.2
  - `[ns_qttbj_559]` `[trigger: 年月透辛土金伤官异路功名]` `[factor_trigger: (month_zi OR month_chou) AND tiangan_wu AND tiangan_xin AND hurting_officer_pattern AND alternate_fame]` `[role: 条件分支]` 年月透辛金者，又属土金伤官，异路功名可许。 → 《穷通宝鉴·三冬戊土》#24.2"""
    normalized_text_zh: str = """"""
    subject: str = "2. 十一十二月戊土（子丑月）"
    factor_refs: list = ['peach_waves', 'minor_official', 'hollow_inside_solid']
    
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
        l1_anchor="qtbj_v1.0.0_2__十一十二月戊土_子丑月_001_L1",
    )
    version: str = "1.0.0"
