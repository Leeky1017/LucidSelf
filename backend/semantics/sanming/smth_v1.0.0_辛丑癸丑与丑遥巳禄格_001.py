"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412229
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
    semantic_id="smth_v1.0.0_辛丑癸丑与丑遥巳禄格_001",
    book_id="sanming",
    engine_id="bazi"
)
class 辛丑癸丑与丑遥巳禄格(SemanticEntry):
    """
    - **原文（source_text）**：

  《喜忌篇》云：辛、癸日多逢丑地，不喜官星，岁时逢子巳二宫，虚名虚利。此格只有辛丑、癸丑二日，辛以丙为官，癸以戊为官，丙戊禄在巳，惟丑能破巳，柱中多逢...
    """
    
    original_text: str = """- **原文（source_text）**：

  《喜忌篇》云：辛、癸日多逢丑地，不喜官星，岁时逢子巳二宫，虚名虚利。此格只有辛丑、癸丑二日，辛以丙为官，癸以戊为官，丙戊禄在巳，惟丑能破巳，柱中多逢丑地，则丙戊之禄出，辛癸遥合得官星，忌见子绊未冲，巳字填实，不过虚名虚利而已，岁运同论。辛丑日宜生秋月，癸丑日宜生冬月，柱中金水多方合此局，再见申酉，得一合住巳字，不致贵气走出为妙。无丙丁巳午，辛日之纯粹，无戊己巳午，癸日之纯粹，再无冲绊，为人淳厚，富贵双全，略见损伤，亦主富足。若生辰戌丑未月，当以杂气取用，逢卯辰申酉亥时，亦不作此格。如辛日生丙寅、丙午、丙戌月，只以官星论，如生甲寅，以木取火，可用财官。癸日土多，以官煞论，见癸亥时，以拱禄论，生金旺月，以印绶论，生火旺月，以财星论，如生甲寅月，伤官不妨，宜行官星得地及身旺运，多贵。此格与辛亥、癸亥飞天禄马大同。经云：辛癸日合禄，平生富有余。诗曰：辛日癸日多逢丑，名为遥巳合官星，莫言不喜官星旺，谁信官来反有成。又：辛丑癸丑二日干，丑能破巳巳藏官，丑字多见方为妙，不宜子字住中间。又：辛癸无官众丑遥，巳中丙戊禄来朝，支元喜见酉申合，入格应须贵禄饶；辛忌丙丁兼巳午，癸嫌戊己马蛇枭，子来绊丑心真懒，格局如轻福亦消。

- 分字分词释义：

  - **辛、癸日多逢丑地，不喜官星**：辛、癸二日若本局多丑土，一般不喜官星明露；此格则以“丑破巳禄、遥合官星”为奇。
  - **丑遥巳禄**：辛丑、癸丑二日，丑能刑破巳，巳中丙戊禄被冲出，辛、癸因而得其官禄，故名“丑遥巳禄”。
  - **丙戊禄在巳，惟丑能破巳**：丙、戊二星之禄位在巳宫，必须丑土刑破巳地，其禄气方能由隐而显。
  - **辛以丙为官，癸以戊为官**：对应十干生克：辛金以丙火为正官，癸水以戊土为正官。
  - **子绊未冲、巳字填实**：子水合丑、未土冲巳，皆会使“遥合”之势受阻或巳字被填实，致贵气难以流行。
  - **辛日之纯粹 / 癸日之纯粹**：辛丑日不宜见丙丁巳午太多，以免官星太露或火旺伤金；癸丑日不宜见戊己巳午太多，以免土火重重坏水。
  - **杂气取用**：生于辰戌丑未等杂气月令时，不适宜再勉强以丑遥巳禄取用，而应依杂气格另择用神。
  - **飞天禄马**：与辛亥、癸亥飞天禄马格相近，皆以远处起禄、合官为特点。

- **规范化释义（primary_lang_explained）**：

  丑遥巳禄，是专门针对辛丑、癸丑二日的遥合禄官格。辛日以丙火为官，癸日以戊土为官，而丙、戊二星的禄地都在巳宫。平常辛、癸多逢丑土时，并不喜欢官星明明白白透出；但若在岁运或柱中又逢巳、子等支，则会出现“丑遥巳禄”的特殊结构：
  
  丑能刑破巳，使巳中丙戊禄气外泄；辛、癸再借丑与巳之间的关系遥合官星、禄星，于是本来“不喜官星”的辛、癸，反而因“遥巳合官”而得贵。原文强调：辛丑宜生秋月、癸丑宜生冬月，柱中金水多、再见申酉以合巳字，使贵气不致走失；并且辛日不宜火太重，癸日不宜土火太重，以保持“金水纯粹”。
  
  若月令在辰戌丑未等杂气之地，或时支逢卯辰申酉亥等，结构复杂，则不宜勉强按丑遥巳禄论贵，而应依杂气论用。又若辛日生于丙寅、丙午、丙戌等火旺月，只能按官星旺地论，不作遥巳禄看；癸日土多时，则按官煞格、拱禄格、印绶格或财星格另论。整体而言，此格与辛亥、癸亥飞天禄马同类，皆属“远处起禄、暗合官星”的格局。

- **完整对等诠释（secondary_lang_full）**：
  The "Chou Remote-Si Salary" configuration is a companion pattern reserved for Xin-Chou and Gui-Chou days. Xin takes Bing fire as its Proper Official, and Gui takes Wu earth as its Proper Official; both stars have their salary seats in Si. In ordinary charts where Xin or Gui repeatedly encounter Chou earth, strong officials on the stems are not welcome, because open fire and earth easily melt metal or exhaust water. Here, however, the repeated presence of Chou acts as the key: Chou can punish and break Si, cracking open the gate of Si so that the salary qi of Bing and Wu leaks out. Once that salary qi is released, Xin and Gui can reach across via the Chou–Si relationship to connect with their officials and salaries, turning what would usually be an inconvenient cluster of Chou earth into the carrier that delivers hidden rank from a distance.
  
  The original text emphasises that this pattern is at its best when metal and water dominate the chart—autumn months for Xin-Chou and winter months for Gui-Chou—and when additional Shen or You branches are present to clasp and contain Si so that the salary qi that has been broken out does not escape. This is called the "purity" of Xin or Gui: fire and earth should not be so heavy that they burn or dry up the water. Months of mixed qi such as Chen, Xu, Chou or Wei, or hours filled with branches that complicate the structure, are not suitable for insisting on Chou Remote-Si Salary and should instead be judged according to mixed-qi or flying-salary patterns. In practice we must confirm that Si is truly being activated from a distance, that the salary qi of Bing and Wu can both be drawn out and held, and that later fortunes do not introduce excessive fire, heavy earth or entangling clashes such as Zi tying Chou. Otherwise the chart may bear the name of the pattern while the promised nobility is reduced to mere comfortable wealth.

- 核心要点：

  - 丑遥巳禄仅限**辛丑、癸丑二日**，以丑刑巳、冲出巳中丙戊禄为起点。
  - 格局成立的关键在于：金水偏旺、巳禄可破而不致被填实，辛、癸得以遥合其官禄。
  - 火、土太重会破坏“辛日之纯粹”“癸日之纯粹”，使格局转为普通官煞或财印格。
  - 杂气月令、支神繁杂时，不宜勉强套用丑遥巳禄，而应按杂气格、飞天禄马等另行取用。

- 详细解说：

  从结构上看，丑遥巳禄与子遥巳禄、飞天禄马等格，均属于“遥处起官禄”的体系：官、禄之根藏在巳宫，辛、癸本身身弱或不喜官太露，因此需要借丑、子等支的刑冲合拱，将巳中禄气引出，再通过合局而化为自己可用的官禄。
  
  对辛丑日而言，金气偏重，若再见丙丁巳午过多，则火旺金熔，官星虽显，反而易成克身之害；故才有“无丙丁巳午，辛日之纯粹”之说。对癸丑日而言，水本不强，若再逢戊己巳午重重，则土火并盛，水势不支，“癸日之纯粹”被破；此时即便有丑遥巳禄之名，实际也难言真贵。原文又言“再见申酉，得一合住巳字，不致贵气走出”，正是强调：巳中禄气一旦被刑破引出，还需申酉金局来摄住，使其不致四散无根。
  
  实务判断时，可以按以下次第：
  1. 确认日主为辛丑或癸丑，且巳中丙戊禄确有被引动的可能；
  2. 察看巳中丙戊禄是否能被引动、有无午冲子、丑绊子等破格因素。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_009]` `[trigger: 丑遥巳禄定义]` `[factor_trigger: chou_yao_si_lu_presence]` `[role: 主干]` 辛、癸日多逢丑地，不喜官星，岁时逢子巳二宫，虚名虚利。 → 《三命通会》卷六#丑遥巳禄
  - `[ns_smth_06_010]` `[trigger: 丑破巳禄]` `[factor_trigger: chou_po_si AND bing_wu_lu_chu]` `[role: 主干依赖]` 此格只有辛丑、癸丑二日，辛以丙为官，癸以戊为官，丙戊禄在巳，惟丑能破巳。 → 《三命通会》卷六#丑遥巳禄
  - `[ns_smth_06_011]` `[trigger: 纯粹条件]` `[factor_trigger: xin_ri_chuncui OR gui_ri_chuncui]` `[role: 条件分支]` 无丙丁巳午，辛日之纯粹，无戊己巳午，癸日之纯粹。 → 《三命通会》卷六#丑遥巳禄
  - `[ns_smth_06_012]` `[trigger: 富有余]` `[factor_trigger: xin_gui_he_lu]` `[role: 总结]` 辛癸日合禄，平生富有余。 → 《三命通会》卷六#丑遥巳禄"""
    normalized_text_zh: str = """"""
    subject: str = "辛丑癸丑与丑遥巳禄格"
    factor_refs: list = ['engine_id', 'bazi_structure_chou_si_marker', 'bazi_structure_chou_si_1', 'bazi_state_metal_water', 'bazi_state_shen_you_degree', 'bazi_condition_fire_earth_condition', 'bazi_condition_month_command', 'source_ref', 'rel_smth_06_007', 'chouyao_silu_presence', 'rel_smth_06_008', 'jinshui_chuncu_score', 'rel_smth_06_009', 'huotu_guowang_risk', 'evi_smth_06_007', 'chou_xingpo_si', 'rule_chouyao', 'evi_smth_06_008', 'jinshui_chuncu_score', 'rule_jinshui', 'evi_smth_06_009', 'huotu_guowang_risk', 'rule_chuncu', 'map_smth_06_005', 'map_smth_06_006']
    
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
        l1_anchor="smth_v1.0.0_辛丑癸丑与丑遥巳禄格_001_L1",
    )
    version: str = "1.0.0"
