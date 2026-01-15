"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412608
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
    semantic_id="smth_v1.0.0_正财与养命之源_001",
    book_id="sanming",
    engine_id="bazi"
)
class 正财与养命之源(SemanticEntry):
    """
    - **原文（source_text）**：

  正财者，乃甲见己、乙见戊之例。受我克制，为我之妻。譬如人娶妻，妻赍财嫁我，我必精神康强，而后可享用；若衰微不振，虽妻财丰厚，但能目视，终不得用。故财...
    """
    
    original_text: str = """- **原文（source_text）**：

  正财者，乃甲见己、乙见戊之例。受我克制，为我之妻。譬如人娶妻，妻赍财嫁我，我必精神康强，而后可享用；若衰微不振，虽妻财丰厚，但能目视，终不得用。故财要得时乘旺，不偏正混乱，不重叠多见，自家日主有力，皆能发福。若财多身弱，柱无印助；财少身强，柱有比劫，太过不及，皆不为福。《珞》云：若月令得财局，身衰逢印资助，当作富论，如先见印，却怕见财。《独步》云：先财后印，反成其福；先印后财，反成其辱是也。用财不宜明露，柱见比劫，则宜透出，使人共见，则不能夺。赋云：财宜藏，藏则丰厚，露则浮荡是也。凡财格，喜见官星显露，别无伤损，或更食生印助日主健旺，富贵双全。如干支见煞，亦能享用，即“逢财看煞”之义。大怕枭，夺则不能生；刃劫则不能享；库逢空则不能聚。余以例推。又曰：财为养命之源，凡人八字不可无财，但不要太多，多则不清。若柱原无财而行财运，乃有名无实；如财多身弱，又行官乡、财旺之地，见财盗气、官克身，不惟不发禄，且祸患百出。

- 分字分词释义：

  - **正财者，乃甲见己、乙见戊之例**：以我克者为财；甲克己土、乙克戊土，属正财，喻正妻、正当所得之财。
  - **受我克制，为我之妻**：财属我所制伏与支配的资源，如同妻携嫁资而来，由我运用。
  - **精神康强，而后可享用**：日主须身健气足，方能承受与驾驭财星，否则“有财而无福享”。
  - **财要得时乘旺，不偏正混乱，不重叠多见**：财星宜得令而适度，不可偏正杂陈、数量失衡。
  - **财宜藏，藏则丰厚，露则浮荡**：财星宜多伏藏于支库，少在天干满天飞露，露则易散、不聚。
  - **先财后印 / 先印后财**：若先行财运后行印运，反成助身之福；若先印后财，则易有“退位”之辱，提示运程先后次序的重要。

- **规范化释义（primary_lang_explained）**：

  正财，在格局上既代表养命之源，也象征婚姻中的“正妻之财”。原文以“妻赍财嫁我”的比喻说明：财不是凭空而来，而是在我方身强、能承受的前提下，由外界汇入、被我所用。

  因此，论正财有几个关键：一是财星本身要得令而不混乱，不能偏、正杂陈、重叠成灾；二是日主必须有足够的气力承载——财多身弱、财少身强、印比失衡，都会使财象偏离“养命之源”而成为拖累；三是财的形态宜含蓄不暴露，藏于库、伏于支，较之明露天干，更利于聚敛与长久。

- 核心要点：

  - 正财是**养命之源与正当所得之财**，重在稳定、可持续，而非暴利。
  - 日主身强、财得其时且有印比调剂，方能成“财格可用”。
  - 财宜藏不宜露，宜清不宜杂；多则不清，少而得地反为美。
  - 运程上“先财后印”为佳，先印后财则易有身退、位移之象。

- 详细解说：

  在实务判断中，可以从三层来看正财：

  1. **量与势**：财多而身弱，往往是“机会太多、承载不足”，容易在压力与诱惑中筋疲力尽；财少而身强，则可能“一点资源反复压榨”，更需印比扶身、避免比劫分夺。
  2. **形态与位置**：藏于支库的财，多主基础稳固、累积缓慢；透干而多、又无根者，多主财来财去、虚名虚利。原文强调“财宜藏”，即是对“浮财”与“实财”的区分。
  3. **与官印的关系**：理想状态是“财生官、官生印、印生身”，形成有序循环；若财多生煞、枭印夺食，或比劫重重分财，则格局由“养命之源”转为“内耗之源”。

  综合而言，正财更多对应一种**稳态的生活资源系统**：适度、有根、有序，强身而不伤身。命局中见正财美者，不必皆富甲一方，但多主衣食有源、有家业可守。

- **校勘与字词辨析（双语）**：

  - 原文中关于“先财后印”“先印后财”的句子，历来解读不一，本稿依据上下文，将其理解为“运程先后次序对福祸的影响”，而非对财、印本身吉凶的简单颠倒。
  - “财宜藏，藏则丰厚，露则浮荡”一语，本稿在白话中以“实财 / 虚财”二分来呈现，便于现代读者理解。
  - 文中诸如“逢财看煞”等术语，本稿在本节只作提点，具体格局另在相关章节展开，不于此赘述。
  - **English**：
    - Details expanded in dedicated sections; not repeated here.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_101]` `[trigger: 养命之源]` `[factor_trigger: zhengcai_presence AND yangming_zhiyuan]` `[role: 主干]` 财为养命之源，凡人八字不可无财，但不要太多，多则不清。 → 《三命通会》卷六#正财
  - `[ns_smth_06_102]` `[trigger: 精神康强]` `[factor_trigger: rizhu_shenwang AND cai_keyong]` `[role: 主干依赖]` 我必精神康强，而后可享用；若衰微不振，虽妻财丰厚，但能目视，终不得用。 → 《三命通会》卷六#正财
  - `[ns_smth_06_103]` `[trigger: 财宜藏]` `[factor_trigger: cai_zang AND fenghou]` `[role: 条件分支]` 财宜藏，藏则丰厚，露则浮荡。 → 《三命通会》卷六#正财
  - `[ns_smth_06_104]` `[trigger: 财身平衡]` `[factor_trigger: caiduo_shenruo OR caishao_shenqiang]` `[role: 总结]` 若财多身弱，柱无印助；财少身强，柱有比劫，太过不及，皆不为福。 → 《三命通会》卷六#正财"""
    normalized_text_zh: str = """"""
    subject: str = "正财与养命之源"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_zhengcai_marker', 'bazi_semantic', 'bazi_structure_zhengcai', 'bazi_semantic', 'bazi_state_factor_20', 'bazi_semantic', 'bazi_state_degree_16', 'bazi_semantic', 'bazi_condition_factor_180', 'bazi_semantic', 'bazi_condition_factor_181', 'bazi_semantic', 'source_ref', 'rel_smth_06_103', 'zhengcai_ge_presence', 'rel_smth_06_104', 'caishen_pingheng', 'rel_smth_06_105', 'bijie_duocai_risk', 'evi_smth_06_103', 'zhengcai_ge_presence', 'rule_zhengcai', 'evi_smth_06_104', 'caishen_pingheng', 'rule_pingheng', 'evi_smth_06_105', 'bijie_duocai_risk', 'rule_duocai', 'map_smth_06_069', 'map_smth_06_070']
    
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
        l1_anchor="smth_v1.0.0_正财与养命之源_001_L1",
    )
    version: str = "1.0.0"
