"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264243
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
    semantic_id="smth_v1.0.0_天元神趣与化象真机_001",
    book_id="sanming",
    engine_id="bazi"
)
class 天元神趣与化象真机(SemanticEntry):
    """
    - 原文（source_text）：
  《天元神趣经》云：凡推人命，先详日下，兴衰变用，分局天地，方成造化。贵贱明于上下，兴衰尽在干支。四时中妙理穷通，五行内荣枯自禀。
  是以春生甲乙居寅卯，岂怕...
    """
    
    original_text: str = """- 原文（source_text）：
  《天元神趣经》云：凡推人命，先详日下，兴衰变用，分局天地，方成造化。贵贱明于上下，兴衰尽在干支。四时中妙理穷通，五行内荣枯自禀。
  是以春生甲乙居寅卯，岂怕庚辛？夏长丙丁乘巳午，何愁壬癸？庚辛值兑，秋生兮离火难侵；壬癸逢乾，冬降兮戊己怎克？土生四季，得时而遇鬼，其伤无害。设使五行失地而逢克，其灾不愈。
  又若化格成象，须分衰旺相停；尤宜配合之中，要识往来去路。
  金绝艮北，火没乾西，木落坤南而无形，水到巽东而无位。此乃阳干皆死，遇合而以类相从，妻若潜形，但见局中而可决。阴生四正，时旺者身贵家荣；死绝墓衰，类伤干尤为不足。
  化气入格不破，大显贵者，十有八九；化气失局有伤，论显荣者，百无一二。
  最高最贵者，居旺处三位，须要相扶；至贱至贫者，居衰处四柱，难寻造化玄。
  象在地支之中，配合在天干之内。象成旺用，皆生火土之中，四柱无伤，直列朝廷之上；支中畏惧，亦须声誉非贫；运至衰乡，必主灾咎。
  化成造化，各居于衰墓绝乡，象成杂局，遇合犹如不遇。
  夫行旺运，妻乃从夫；妻运扶持，夫从妻论。
  己身临鬼，须明天地之中，象旺象衰，要识荣枯贵贱。身衰鬼旺，应须肢体伤残；身旺鬼衰，定作凶徒之命；鬼身皆衰，男必飘蓬，女作师尼。
  伏身潜匿，自居高名；月气相伤，此乃伏象。官鬼皆全，遐龄不遂。
  干中破败，乃有技艺以随身；支乃生全，难仗六亲而独立。
  五行属于其象，皆在十二支中。先分南北与东西，次看三合内别认。详六亲者，从象而推之；审富贵者，官禄而两说。
  有禄盛者，鳏寡孤独；有官鬼者，残疾夭寿。身如显化，自身无气，本性全亏。假五行成象，平生窘迫，岂得祖宗之财；显福显盈，因犯别房父母。
  从象论引用为气，化象论天地相停。从中有贵有贱，化内有富有贫。从中贵显，得时而位列朝中；化内成局，运转而成封帝侧。从象衰而至老驱驱，化象伏而平生碌碌。

- 分字分词释义：
  - **日下**：指日主。
  - **上下**：指天干地支。
  - **春生甲乙**：春月木旺，身强不怕官煞（庚辛）。
  - **金绝艮北**：金在艮（丑寅之间，近北）为绝地（金生巳，绝寅）。
  - **化格成象**：天干化气，地支成局（象）。
  - **三位**：指财官印三奇，或指天、地、人三元。
  - **伏身潜匿**：指日主无根气，或从格（伏象）。
  - **鬼旺身衰**：煞重身轻。
  - **身旺鬼衰**：身强煞浅，制煞太过。

- **规范化释义（primary_lang_explained）**：
  推命首先看日主兴衰。如果在当令季节，身强，则不怕官煞克制（如春木不怕金，夏火不怕水）。若失令失地，再逢克制，则灾难深重。
  论化气格，要看衰旺是否相当，配合是否有情。阳干在死绝之地（如金绝艮北），若遇合化（乙庚化金？或阳随阴化），可以从妻（从财）或从象。阴干生于四正（子午卯酉），若得时旺，主贵。化气入格不破，多主大贵；破格则贫贱。
  最贵者，居于旺处，得三奇相扶。最贱者，居于衰处，四柱无气。
  象（地支局）与配合（天干）要协调。象成旺用（如火土成象），无伤破，主贵。若支中有忌神（畏惧），虽然不贫，但难免灾咎。
  化气若居衰墓绝乡，或杂乱，虽合不化。
  身衰鬼旺（煞重身轻），主残疾；身旺鬼衰（制煞太过），主凶徒（好勇斗狠）。鬼身皆衰，漂泊无依。
  伏象（从格或日主极弱），若月气相伤（不从），则平常。
  从象（从格）要看引用的气势，化象（化格）要看天地是否相停（干支一气）。从化得时成局，皆贵；衰伏则劳碌。

- 核心要点：
  - **身旺任煞**：得时者不怕鬼。
  - **化气从象**：化格从格要得时成局，忌破损。
  - **鬼身平衡**：身煞两停为贵，偏枯为凶。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_045]` `[trigger: 先详日下]` `[factor_trigger: xianxiang_rixia AND xingshuai_bianyong]` `[role: 主干]` 凡推人命，先详日下，兴衰变用，分局天地，方成造化。 → 《三命通会》卷十#天元神趣与化象真机
  - `[ns_smth_10_046]` `[trigger: 春生甲乙]` `[factor_trigger: chunsheng_jiayi AND qipa_gengxin]` `[role: 主干依赖]` 春生甲乙居寅卯，岂怕庚辛？夏长丙丁乘巳午，何愁壬癸？ → 《三命通会》卷十#天元神趣与化象真机
  - `[ns_smth_10_047]` `[trigger: 化气入格]` `[factor_trigger: huaqi_ruge AND shibajiugui]` `[role: 条件分支]` 化气入格不破，大显贵者，十有八九；化气失局有伤，论显荣者，百无一二。 → 《三命通会》卷十#天元神趣与化象真机
  - `[ns_smth_10_048]` `[trigger: 鬼旺身衰]` `[factor_trigger: guiwang_shenshuai AND zhiti_shangcan]` `[role: 总结]` 身衰鬼旺，应须肢体伤残；身旺鬼衰，定作凶徒之命。 → 《三命通会》卷十#天元神趣与化象真机"""
    normalized_text_zh: str = """"""
    subject: str = "天元神趣与化象真机"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_69', 'bazi_semantic', 'bazi_structure_factor_70', 'bazi_semantic', 'bazi_state_factor_319', 'bazi_semantic', 'bazi_state_factor_236', 'bazi_semantic', 'bazi_condition_factor_102', 'bazi_semantic', 'source_ref', 'rel_smth_10_040', 'huage_congxiang', 'rel_smth_10_041', 'guiwang_shenshuai', 'rel_smth_10_042', 'shenwang_guishuai', 'evi_smth_10_040', 'deshi_chengju', 'rule_deshi_chengju1', 'evi_smth_10_041', 'canji_fengxian', 'rule_guiwang_shenshuai1', 'evi_smth_10_042', 'xiongbao_qingxiang', 'rule_shenwang_guishuai1', 'map_smth_10_027', 'map_smth_10_028']
    
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
        l1_anchor="smth_v1.0.0_天元神趣与化象真机_001_L1",
    )
    version: str = "1.0.0"
