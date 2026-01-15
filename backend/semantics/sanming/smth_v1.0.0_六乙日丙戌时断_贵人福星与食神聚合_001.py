"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157429
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
    semantic_id="smth_v1.0.0_六乙日丙戌时断_贵人福星与食神聚合_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六乙日丙戌时断贵人福星与食神聚合(SemanticEntry):
    """
    - 原文（source_text）：

  六乙日丙戌时断。

  六乙日生时丙戌，鬼败临身有损伤；若不气通身旺月，孤贫劳碌苦难当。乙日丙戌时，鬼败临身，乙用庚为官，见丙背禄，戌中有辛余气、丙丁库，食...
    """
    
    original_text: str = """- 原文（source_text）：

  六乙日丙戌时断。

  六乙日生时丙戌，鬼败临身有损伤；若不气通身旺月，孤贫劳碌苦难当。乙日丙戌时，鬼败临身，乙用庚为官，见丙背禄，戌中有辛余气、丙丁库，食神制煞，若柱透庚，伤官见官，刑害百端；年月有寅午，丙火合局，即一木叠逢火位，主人傲物气高，衣禄平常，残疾，不然寿促。通身旺月气者，吉。

  乙丒日丙戌时，春身旺，吉。夏，伤官太重。秋，劳力辛苦。冬亥子，印绶带伤官，极贵。戌月，木火运，七品贵。纯戌年月，天干透庚丙者，大贵。寅午合火者夭。

  乙卯日丙戌时，寅卯月，运西运，六七品贵。子月印绶；丑月杂气，刑出财官，俱贵。

  乙巳日丙戌时，吉。丑戌未年月，风宪六卿。亥月，行东运，翰院清贵。

  乙未日丙戌时，旺处凶。卯午未戌年月，贵显。

  乙酉日丙戌时，春身旺，冬印旺，大贵。夏巳午，秋酉戌，俱贵。亦看天干如何？丁未、甲辰，生计辛苦；一生遇贵。丑月刑。戌吉。

  乙亥日丙戌时，血疾。亥子卯未寅月，遇贵发福；天干透伤官生财，尤吉。

  枯木相逢局，逢春叶更生；晚年方得地，花发再重荣。乙日丙戌时火库，藏辛遇丑乃吉昌；若也运逢凶克害，算来此命且如常。乙日相逢丙戌，伤官库木枝枯。不临辛丑钥匙无。难倚六亲父母，雁侣分飞不睦，于人心悲成疏。要知发福改门闾，此命后甜先苦。

- 分字分词释义：

  - **鬼败临身**：七煞（鬼）处败地，但仍对日主构成压力。
  - **伤官背禄**：丙火伤官克制庚金正官，形成「背禄」（破坏官禄）之象。
  - **枯木逢春**：比喻早年困顿，晚年得势，重新焕发生机。
  - **后甜先苦**：人生先经历困难，后来享受福禄。

- 规范化释义（primary_lang_explained）：

  本节讲「六乙日，丙戌时」：

  - 丙火伤官克制庚金正官，形成「背禄」之象；戌中虽有辛金余气，但被丙火所伤；
  - 若年月再有寅午合火，火旺木焚，主人傲物气高、衣禄平常，甚至残疾或寿促；
  - 歌诀以「枯木逢春」比喻此格的晚发特点：先苦后甜，晚年方能发福。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Yi Days with Bing-Xu Hour":

  - Bing Fire (Hurting Official) overcomes Geng Metal (Direct Official), forming a pattern of "against fortune." Though Xu contains Xin Metal residual energy, it is harmed by Bing Fire.
  - If year-month additionally contains Yin-Wu combining into Fire, fire becomes too strong and burns wood—the person becomes arrogant, livelihood remains ordinary, possibly disabled or short-lived.
  - The verse uses "withered tree meets spring" to describe this pattern's late-blooming characteristic: first bitter then sweet, fortune arrives only in later years.

- 核心要点：

  - 本格以「伤官背禄」为核心，结构偏凶。
  - 火旺木焚是主要风险，需要身旺月气来化解。
  - 歌诀强调：先苦后甜，晚年发福。

- 详细解说：

  1. **伤官背禄的困境**  
     - 丙火伤官克制庚金正官，破坏了官禄的根基；  
     - 若官星被伤，则仕途不顺、名利难成。

  2. **火旺木焚的风险**  
     - 若年月有寅午，与戌三合火局，火势太旺；  
     - 乙木虽生火，但火旺则木焚，主健康或寿元受损。

  3. **枯木逢春的转机**  
     - 若能通身旺月气，或行印绶运，可得滋润；  
     - 晚年运势配合，仍可「花发再重荣」。

- 校勘与字词辨析：

  - 「雁侣分飞不睦」形容兄弟姐妹各奔东西，关系疏远。
  - 「改门闾」与「改祖离亲」同义，指自立门户、另起炉灶。
  - **English**：
    - Meaning: establishing one's own household, starting anew.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_089]` `[trigger: 鬼败临身]` `[factor_trigger: guibai_linshen AND you_sunshang]` `[role: 主干]` 六乙日生时丙戌，鬼败临身有损伤。 → 《三命通会》卷八#六乙日丙戌时
  - `[ns_smth_08_090]` `[trigger: 伤官背禄]` `[factor_trigger: shangguan_beilu AND gupin_laolu]` `[role: 主干依赖]` 若不气通身旺月，孤贫劳碌苦难当。 → 《三命通会》卷八#六乙日丙戌时
  - `[ns_smth_08_091]` `[trigger: 枯木逢春]` `[factor_trigger: kumu_fengchun AND ye_geng_sheng]` `[role: 条件分支]` 枯木相逢局，逢春叶更生。 → 《三命通会》卷八#六乙日丙戌时
  - `[ns_smth_08_092]` `[trigger: 后甜先苦]` `[factor_trigger: houtian_xianku AND gaimen_lu]` `[role: 总结]` 要知发福改门闾，此命后甜先苦。 → 《三命通会》卷八#六乙日丙戌时"""
    normalized_text_zh: str = """"""
    subject: str = "六乙日丙戌时断：贵人福星与食神聚合"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_yi', 'bazi_semantic', 'bazi_state_shangguan_5', 'bazi_semantic', 'bazi_relation_fire_wood', 'bazi_semantic', 'bazi_state_wood_3', 'bazi_semantic', 'hour_branch_xu', 'bazi_semantic', 'bazi_condition_factor_124', 'bazi_semantic', 'source_ref', 'rel_smth_08_067', 'shangguan_beilu', 'rel_smth_08_068', 'huowang_mufen', 'rel_smth_08_069', 'tongshenwang_yue', 'evi_smth_08_067', 'shangguan_beilu', 'rule_beilu', 'evi_smth_08_068', 'huowang_mufen', 'rule_huowang', 'evi_smth_08_069', 'kumu_fengchun', 'rule_kumu', 'map_smth_08_045', 'map_smth_08_046']
    
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
        l1_anchor="smth_v1.0.0_六乙日丙戌时断_贵人福星与食神聚合_001_L1",
    )
    version: str = "1.0.0"
