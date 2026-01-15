"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157419
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
    semantic_id="smth_v1.0.0_六乙日乙酉时断_身绝鬼旺与化金之象_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六乙日乙酉时断身绝鬼旺与化金之象(SemanticEntry):
    """
    - 原文（source_text）：

  六乙日乙酉时断。

  六乙日生时乙酉，得逢金局火为奇；用神遇木重重见，鬼绝寿伤反无依。乙日乙酉时，身绝鬼旺，乙以辛为鬼，酉上辛旺乙绝。若通巳酉丑月，化金局...
    """
    
    original_text: str = """- 原文（source_text）：

  六乙日乙酉时断。

  六乙日生时乙酉，得逢金局火为奇；用神遇木重重见，鬼绝寿伤反无依。乙日乙酉时，身绝鬼旺，乙以辛为鬼，酉上辛旺乙绝。若通巳酉丑月，化金局者贵。如用神坐木，身旺不化，又见于酉，不夭必贫。

  乙丒日乙酉时高，生巳酉丑月，合金局，更行西运，大贵。寅午戌月，贫下。亥卯未月，吉。纯子年月，行南运，一二品贵。寅月火金，七品贵。申月水木，金紫贵。

  乙卯日乙酉时，月通金局者贵。未寅年月，官至一二品。

  乙巳日乙酉时，春吉。夏，伤官有制，好。秋，木弱金重，夭，不然有疾。冬，福厚亦夭。

  乙未日乙酉时，拱贵格，无刑破者贵，有申填实则非。亥卯月，行西运，贵。

  乙酉日乙酉时，旺处自刑，年月火土重，主灾。若通月气，透出印食，行火木运，大贵。地支纯酉，化成金象，但带印绶，贵不可言。最怕岁运遇官。

  乙亥日乙酉时，春生，仁寿格，贵。寅月，行金火运，大贵。

  日干是乙时临酉，假煞为权身旺奇；身弱遇官徒费力，功名须待运通时。乙日时临乙酉，诞辰乙木无忧。其中权贵任求谋，无破功名定有。妻子早年克害，财源雨散云收。迁宗移祖免忧愁。中末家资成就。

- 分字分词释义：

  - **身绝鬼旺**：乙木在酉为绝地，辛金七煞在酉为建禄，形成身弱煞强的格局。
  - **化金局**：巳酉丑三合金局，乙木从化为金，可转危为安。
  - **拱贵格**：地支拱合贵人位，无填实则成格。
  - **假煞为权**：七煞有制化后转为有力的权威与执行力。

- 规范化释义（primary_lang_explained）：

  本节讲「六乙日，乙酉时」：

  - 乙木在酉为绝地，辛金七煞在酉旺盛，形成身弱煞强的险局；
  - 若能通巳酉丑月，三合化金，则可从煞化贵；若身旺不化，又无救助，则不夭必贫；
  - 歌诀提示：身弱遇官徒劳无功，需待运势配合方能成就。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Yi Days with Yi-You Hour":

  - Yi Wood at You reaches extinction while Xin Metal Seven-Killing at You is prosperous, forming a dangerous pattern of weak self and strong killing.
  - If able to connect with Si-You-Chou months and transform into Metal formation, one can turn danger into nobility by following killing; if body is strong but doesn't transform and lacks rescue, the result is either early death or poverty.
  - The verse indicates: when body is weak meeting Official, efforts are futile—achievement awaits fortune cycle alignment.

- 核心要点：

  - 本格以「身绝鬼旺」为核心，结构偏险。
  - 能否化金是关键：化则贵，不化则凶。
  - 歌诀强调：身旺方能假煞为权，身弱则功名难成。

- 详细解说：

  1. **身绝鬼旺的风险**  
     - 乙木在酉为绝地，力量衰微；辛金七煞在酉为建禄，力量强旺；  
     - 若无救助，身弱煞强，主凶厄或贫困。

  2. **化金局的转机**  
     - 若月令为巳或丑，与酉三合化金；  
     - 乙木从化为金，不再与煞对抗，反可借煞之力成就。

  3. **六乙日的差异**  
     - 乙酉日乙酉时为「旺处自刑」，尤其需要注意；  
     - 春生身旺者较吉，秋冬身弱煞强者凶险。

- 校勘与字词辨析：

  - 「迁宗移祖免忧愁」指改换门庭、另立根基，与「改祖离亲」同义。
  - 「中末家资成就」强调此格晚年方能积累财富。
  - **English**：
    - Pattern emphasizes wealth accumulation only in later years.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_085]` `[trigger: 身绝鬼旺]` `[factor_trigger: shenjue_guiwang AND huo_wei_qi]` `[role: 主干]` 六乙日生时乙酉，得逢金局火为奇。 → 《三命通会》卷八#六乙日乙酉时
  - `[ns_smth_08_086]` `[trigger: 化金局]` `[factor_trigger: huajin_ju AND tong_siyouchou]` `[role: 主干依赖]` 若通巳酉丑月，化金局者贵。 → 《三命通会》卷八#六乙日乙酉时
  - `[ns_smth_08_087]` `[trigger: 假煞为权]` `[factor_trigger: jiasha_weiquan AND shenwang_qi]` `[role: 条件分支]` 假煞为权身旺奇，身弱遇官徒费力。 → 《三命通会》卷八#六乙日乙酉时
  - `[ns_smth_08_088]` `[trigger: 迁宗移祖]` `[factor_trigger: qianzong_yizu AND zhongmo_chengjiu]` `[role: 总结]` 迁宗移祖免忧愁，中末家资成就。 → 《三命通会》卷八#六乙日乙酉时"""
    normalized_text_zh: str = """"""
    subject: str = "六乙日乙酉时断：身绝鬼旺与化金之象"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_yi', 'bazi_semantic', 'bazi_state_factor_163', 'bazi_semantic', 'bazi_relation_metal', 'bazi_semantic', 'bazi_state_factor_164', 'bazi_semantic', 'hour_branch_you', 'bazi_semantic', 'bazi_condition_metal_2', 'bazi_semantic', 'source_ref', 'rel_smth_08_064', 'shenjue_guiwang', 'rel_smth_08_065', 'huajin_ju', 'rel_smth_08_066', 'tongjin_juyue', 'evi_smth_08_064', 'shenjue_guiwang', 'rule_shenjue', 'evi_smth_08_065', 'huajin_ju', 'rule_huajin', 'evi_smth_08_066', 'jiasha_weiquan', 'rule_jiasha', 'map_smth_08_043', 'map_smth_08_044']
    
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
        l1_anchor="smth_v1.0.0_六乙日乙酉时断_身绝鬼旺与化金之象_001_L1",
    )
    version: str = "1.0.0"
