"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412172
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
    semantic_id="smth_v1.0.0_壬骑龙背格与壬辰之贵_001",
    book_id="sanming",
    engine_id="bazi"
)
class 壬骑龙背格与壬辰之贵(SemanticEntry):
    """
    - **原文（source_text）**：

  《喜忌篇》云：“阳水叠逢辰位，是壬骑龙背之乡。”此格以壬日坐辰，壬以丁为财，己为官，壬用支辰暗冲戌中丁、戊，壬日得财官之贵，柱中须辰多方能冲起，再得...
    """
    
    original_text: str = """- **原文（source_text）**：

  《喜忌篇》云：“阳水叠逢辰位，是壬骑龙背之乡。”此格以壬日坐辰，壬以丁为财，己为官，壬用支辰暗冲戌中丁、戊，壬日得财官之贵，柱中须辰多方能冲起，再得一寅字合住财官为妙，不宜财官显露，喜行身旺及伤官、食神运，忌南方财官之地。柱有丁巳午戌，只作财官论。若壬日坐寅，柱中辰多，亦取此格，以壬食甲、甲合己为壬官，甲生丁为壬财，辰能冲戌，寅以合之为贵。若壬辰日，年月时皆寅午火局，财生旺得地，财多不清，只为富命。双曰：壬辰日取辰多，暗冲起戌中火土金为财官印三奇，若三辰一寅为冲合贵气，有力，若壬辰日年月时皆寅，力轻，却用寅中甲木为食生财，故主富。柱中宜见丑未为贵，大怕己官、戊煞、乙伤、丁合不入格，纵辰多亦减分数，忌北方亥子运。又曰：壬辰为魁罡日，宜身旺，怕见财官，休否以运参详，若柱中全见申子，当以润下格论，运戊己，辰戌又冲，岁运并临，吉中反祸，此为骑龙走冲，不成格也。一命：己丑、戊辰、壬辰、庚子，甲子举人，戊辰年乙卯月死，正是己官煞太旺，克壬为凶。诗曰：壬辰日诞号骑龙，飞出官星在对冲，四柱辰多官爵显，寅多却作富家翁。又：阳水多逢辰字乡，壬骑龙背贵非常，柱中俱有寅辰字，富贵双全在庙堂。又：壬骑龙背喜非常，辰多寅字转发扬，大忌官星来破格，灾刑须见寿元伤。

- 分字分词释义：

  - **阳水叠逢辰位**：壬为阳水，辰为湿土藏水，壬日坐辰、地支多见辰，为“阳水乘辰土之龙”的结构。
  - **骑龙背**：以辰为“龙”，壬水乘辰而行，暗冲戌中财官，象征乘龙得势、借势发贵。
  - **支辰暗冲戌中丁、戊**：以辰冲戌，戌中藏丁火、戊土，分别为壬之财与官，通过冲动而显其用。
  - **财官显露 / 不宜显露**：财、官若直接透干，则格局易走向普通财官格；壬骑龙背贵在财官伏藏，由辰冲戌而动，不宜过多明透。
  - **寅字合住财官**：寅与戌、午合火局，一寅一辰既能合住冲起的财官，又能形成食神（甲木）生财、合官之势。
  - **魁罡日**：壬辰为四大魁罡之一，性刚烈，宜身旺而不受财官过制。
  - **润下格**：壬、癸水日配申子辰多见而成全水局，为另一种“润下”格局，与壬骑龙背判别不同。
  - **骑龙走冲**：辰多与戌多相冲，或运岁再加戊己、辰戌冲击，格局不稳，贵气反成祸源。

- **规范化释义（primary_lang_explained）**：

  壬骑龙背，是专为壬日而设的一种贵格。古人以辰为龙，“阳水叠逢辰位”是说壬日坐辰，且命局中多见辰土。壬日以丁火为财、己土为官，而戌中正藏丁、戊，平时伏而不显；当多辰冲戌时，戌中丁、戊被激发，财官随之而起，壬水似乎“骑”在龙背上，借辰土暗动戌中财官而发贵。格局以“辰多一寅”为妙：辰多以冲起戌中财官，一寅则合住、统摄之，使财官不致外泄，化为自身荣贵。
  
  需要注意的是：壬骑龙背贵在“暗动”，若财官透干太多，便成普通财官格，不再论作骑龙背。若壬日坐寅而多辰，也可以借食神甲木合己为官、甲生丁为财，同样用辰冲戌而成格。壬辰日则更为典型：若多辰一寅，暗冲戌中火土金为财、官、印三奇，乃贵格；若壬辰日而年月时皆寅午火局，则财多不清，只主富而不贵。
  
  壬辰本身又是魁罡日，性格刚烈，宜身旺而不宜财官太露；若柱中申子俱全，当以润下格另论。若再遇戊己运、辰戌对冲，大运岁运并临，则原本骑龙背之格反被冲坏，形成“骑龙走冲”，吉中藏祸。古人举壬辰日一命，财官过旺而克身，以示其戒。
  - **English**：
    - Special pattern terminology clarified; obscure classical references explained with accessible examples.

- **完整对等诠释（secondary_lang_full）**：
  The pattern known as "Ren Rides Dragon-Back" is a noble configuration designed specifically for Ren day-stems. Classical authors treat Chen as the Dragon: the phrase "Yang Water repeatedly meeting the position of Chen" describes a Ren day sitting on Chen with multiple Chen branches appearing throughout the chart. Ren takes Ding fire as wealth and Ji earth as official, and both Ding and Wu are stored inside Xu earth. When many Chen branches clash with Xu, they stir these hidden Ding and Wu so that wealth, official and even Seal power are activated from concealment. In this structure, Ren Water does not attack wealth and officials head-on, but rides on the back of Chen as a Dragon, borrowing its movement to set the buried stars in Xu into motion. The ideal layout is summarised as "many Chens with one Yin": the many Chen branches provide sufficient force to clash Xu and awaken the hidden fire and earth, while a single Yin branch joins the fire bureau, gathers the stirred-up stars and links Jia Wood, Ding fire and Ji earth into a coherent chain of Food, wealth and official authority.
  
  This pattern therefore values what is hidden and indirectly activated rather than officials and wealth plainly exposed on the stems. If wealth and officials are too openly revealed, the structure collapses back into ordinary wealth–official charts and is no longer judged as Riding the Dragon. We must also distinguish it from the "Run-Downward" water pattern in which Ren or Gui with Shen, Zi and Chen form a full water bureau; that configuration emphasises continuous moistening rather than secretly stirring the fire and earth in Xu. Ren Chen itself is a "Kui-Gang" day with a fierce, uncompromising nature, so the day-master must be strong and supported by Seals; if the body is weak while wealth and officials pile up, or if later fortune cycles bring heavy Wu and Ji earth and repeated Chen–Xu clashes, the Dragon-back becomes unstable and turns into "riding the dragon into violent clashes", where apparent nobility hides serious risk. In practice one must first judge whether the chart is truly in a hidden-activation mode or has simply become a water bureau, and then weigh the presence of Yin, the degree of exposure of wealth and officials, and the direction of the luck cycles before safely concluding that the chart can bear the honour promised by this pattern.

- 核心要点：

  - 壬骑龙背以**壬日多辰、暗冲戌中财官印**为核心，贵在伏而能发，不在财官明透。
  - 结构理想状态为“多辰一寅”：辰冲戌起财官，寅合火局统之，并以甲木生丁、合己，使财官印三奇有序运行。
  - 壬辰为魁罡日，宜身旺、煞印有情，忌财官过露与戊己重重冲破。
  - 与润下格要区分：若申子辰成全水局，则以润下论，不再勉强归入壬骑龙背。

- 详细解说：

  传统壬水格局中，有以润下为贵者，也有以骑龙背为奇者。润下偏重“水势连绵、泽被万物”，多见于水局成象；而壬骑龙背则强调“壬水乘辰、暗动戌中财官印”，更偏向于权柄与职位之贵。两者虽同为壬水格局，却在结构与用神上大不相同。
  
  壬骑龙背的关键结构可以拆为三层：
  - 第一层：**壬日坐辰，多逢辰土**，壬水有根且乘龙；
  - 第二层：**辰冲戌，动起戌中丁、戊**，使财官由伏而显；
  - 第三层：**寅字合局**，既合火局、又以甲木生丁、合己，使财官印形成一条有序的能量链条。
  在这种结构中，壬水不直接与财官搏斗，而是借辰、寅之力调度财官，这是“骑龙背”的妙处。
  
  然而，此格对“明露”和“过多”极为敏感：一方面，财官若透干过多，则从“暗冲起用”变成“明财明官”，壬骑龙背的特色不再；另一方面，壬辰虽为魁罡日，身旺则可任煞，身弱遇财官重重，却易被克折。因此原文反复强调：忌南方财官运、忌亥子北水运冲坏根基，也忌己官、戊煞、乙伤、丁合等杂神破格。
  
  在实务上，遇到壬日多辰、又兼见戌中财官印者，应先判断是“暗冲起用”还是“润下成局”；再看寅字有无、财官是否过露，以及身强身弱与大运流向，才能放心以壬骑龙背之贵论之。

- **校勘与字词辨析（双语）**：
  - **中文**：
    - 原文"阳水叠逢辰位，是壬骑龙背之乡"一句，为本格名称与意象来源，本稿据底本保留不改，仅在释义中解释为壬水乘辰之象。
    - 文中多处"壬辰日取辰多""壬辰为魁罡日"等句，提示读者注意区分一般壬日与壬辰日之特殊性，本稿在白话与详细解说中予以归纳。
    - "骑龙走冲"一语，用以形容辰戌冲及岁运并临而反成破格，本稿不另改字，仅在释义中说明其含义。
  - **English**：
    - The phrase "Yang Water repeatedly meeting Chen position is the territory of Ren Riding Dragon-Back" establishes the name and imagery of this pattern; this edition preserves the original wording and explains it as Ren Water mounting Chen.
    - Multiple passages such as "Ren-Chen day takes multiple Chen" and "Ren-Chen is a Kuigang day" remind readers to distinguish ordinary Ren days from the special Ren-Chen day; this edition summarizes these points in the vernacular explanation and detailed commentary.
    - The phrase "Riding-Dragon into-clash" describes how Chen-Xu clashes, especially when reinforced by fate cycles, can break the pattern; this edition keeps the original wording and clarifies its meaning in the glossary.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_001]` `[trigger: 壬骑龙背定义]` `[factor_trigger: ren_qi_longbei_presence]` `[role: 主干]` 阳水叠逢辰位，是壬骑龙背之乡。 → 《三命通会》卷六#壬骑龙背
  - `[ns_smth_06_002]` `[trigger: 暗冲财官]` `[factor_trigger: chen_chong_xu AND an_dong_cai_guan]` `[role: 主干依赖]` 壬用支辰暗冲戌中丁、戊，壬日得财官之贵。 → 《三命通会》卷六#壬骑龙背
  - `[ns_smth_06_003]` `[trigger: 辰多寅合]` `[factor_trigger: chen_duo_yin_he AND cai_guan_wei_miao]` `[role: 条件分支]` 柱中须辰多方能冲起，再得一寅字合住财官为妙。 → 《三命通会》卷六#壬骑龙背
  - `[ns_smth_06_004]` `[trigger: 骑龙发贵]` `[factor_trigger: qi_long_fa_gui AND guan_jue_xian]` `[role: 总结]` 壬辰日诞号骑龙，飞出官星在对冲，四柱辰多官爵显。 → 《三命通会》卷六#壬骑龙背"""
    normalized_text_zh: str = """"""
    subject: str = "壬骑龙背格与壬辰之贵"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_ren_marker', 'bazi_semantic', 'bazi_structure_chen_yin_config', 'bazi_semantic', 'bazi_state_strength', 'bazi_semantic', 'bazi_state_factor_4', 'bazi_semantic', 'bazi_condition_condition_1', 'bazi_semantic', 'bazi_condition_wu_ji_chen_xu', 'bazi_semantic', 'source_ref', 'rel_smth_06_001', 'ren_qi_longbei_presence', 'rel_smth_06_002', 'anchong_qiyong_score', 'rel_smth_06_003', 'wuji_zhongchong_risk', 'evi_smth_06_001', 'anchong_qiyong_score', 'rule_anchong', 'evi_smth_06_002', 'duochen_yiyin_config', 'rule_duochen', 'evi_smth_06_003', 'wuji_zhongchong_risk', 'rule_wuji', 'map_smth_06_001', 'map_smth_06_002']
    
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
        l1_anchor="smth_v1.0.0_壬骑龙背格与壬辰之贵_001_L1",
    )
    version: str = "1.0.0"
