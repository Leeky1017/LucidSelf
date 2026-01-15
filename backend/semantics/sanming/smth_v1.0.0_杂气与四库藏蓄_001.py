"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412767
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
    semantic_id="smth_v1.0.0_杂气与四库藏蓄_001",
    book_id="sanming",
    engine_id="bazi"
)
class 杂气与四库藏蓄(SemanticEntry):
    """
    - **原文（source_text）**：

  论杂气：杂气者，乃辰戌丑未。辰中有乙戊癸，为水土库；戌中有辛戊丁，为火库；丑中有癸辛己，为金库；未中有丁己乙，为木库。各随所藏之气而言，看我日干，或...
    """
    
    original_text: str = """- **原文（source_text）**：

  论杂气：杂气者，乃辰戌丑未。辰中有乙戊癸，为水土库；戌中有辛戊丁，为火库；丑中有癸辛己，为金库；未中有丁己乙，为木库。各随所藏之气而言，看我日干，或为官，或为财，或为印。官系福身之物，财是养命之源，印乃资身之本，在人最为切要。四库各藏三件，乃天地不正之气，故以“杂”言也。《经》云：财官印绶全备，藏蓄于四季之中是也。此格喜透露冲刑，忌压伏，其余喜忌消息，与前正气财官印同。假令六甲日生得丑月，以丑中辛金为官，己土为财，癸水为印，看天干透出何字为福次，分节气浅深，何物当令，大概透财者富，透官者贵，印绶享父祖见成之福，受宣敕荫庇之贵。如无透出，冲刑少许兼身旺为妙。忌身弱，冲刑太过，则福聚之气散矣。如柱元有破害之物，再不可遇此等运，再行则为太过，冲坏秀气，反不为吉。元无破害，喜冲刑运。《景鉴》云：杂气财官，身旺有冲而发，若太过反受孤贫是也。又云：杂气财官格，要四柱财星多，便为好命，若四柱别入他格，依他格断。又云：杂气财官有正官格、偏官格、正财格、偏财格，杂气印绶有正印格、偏印格，须分偏正。若偏官，亦要少许制伏则可。若墓库重叠，元无刑冲，不透贵气，兼有戊己压其上，最难发于少年。故曰：“财官锁闭少年，不发墓中人”是也。又曰：四库亦是衰养冠带之乡。若时上见为时墓格，与月上同论，但发较晚。如丁亥、戊子、丙申、己丑，丙用丑墓为财库，行未运冲丑库发财。见壬，辰为官库，至戌运冲辰库发官。倘柱中别有戊辰、己丑压伏库上，则不能发财发官，难作好命看。若有冲见合，则又不能冲矣。又曰：月临库地，东西南北四隅之气，如未木行东方，戌火行南方，辰水行北方，丑土行西方之类。

- 分字分词释义：

  - **杂气**：相对于“正气”而言，指四库地支中所藏的多重五行之气，结构复杂、变化多端。
  - **财官印绶全备，藏蓄于四季之中**：四库往往暗藏财官印多种能量，是“藏而未发”的潜力区。

- **规范化释义（primary_lang_explained）**：

  杂气格不宜简单视为“杂乱”，更合理的理解是“潜藏多重可能”：

  - 若能透出适当的财官印，并配合冲刑得宜，则可在特定运程中集中爆发；
  - 若被戊己重压、久居不冲，则成“锁闭之库”，主少年不发或晚发。

- 核心要点：

  - 杂气重在**库与潜力**，喜适度透出与适度冲刑。
  - 过度冲刑则散气，完全不冲则闭塞，皆非佳局。

- 详细解说：

  对现代命理实践而言，杂气格提示：

  - 有些人的起点看似平常，实则在某些阶段会因结构被“冲开”而爆发；
  - 判断时需详看哪一类气为当令、哪一类被压伏，以及岁运如何触发。

- **校勘与字词辨析（双语）**：

  - “财官锁闭少年，不发墓中人”一语，本稿在白话中仅以“少年不显、需待中晚年方见机会”释之，不作死板凶断。
  - **English**：
    - Flexible interpretation; avoids rigid inauspicious verdicts.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_161]` `[trigger: 杂气定义]` `[factor_trigger: zaqi_presence AND siku_cangxu]` `[role: 主干]` 杂气者，乃辰戌丑未。各随所藏之气而言。 → 《三命通会》卷六#论杂气
  - `[ns_smth_06_162]` `[trigger: 财官印藏]` `[factor_trigger: caiguanyin_quanbei AND cangxu_siji]` `[role: 主干依赖]` 财官印纶全备，藏蓄于四季之中。 → 《三命通会》卷六#论杂气
  - `[ns_smth_06_163]` `[trigger: 喜透露冲刑]` `[factor_trigger: xi_toulu AND xi_chongxing]` `[role: 条件分支]` 此格喜透露冲刑，忌压伏。 → 《三命通会》卷六#论杂气
  - `[ns_smth_06_164]` `[trigger: 透财富透官贵]` `[factor_trigger: toucai_fu AND touguan_gui]` `[role: 总结]` 大概透财者富，透官者贵。 → 《三命通会》卷六#论杂气"""
    normalized_text_zh: str = """"""
    subject: str = "杂气与四库藏蓄"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_42', 'bazi_semantic', 'new_candidate', 'bazi_semantic', 'bazi_state_degree_30', 'bazi_semantic', 'bazi_state_degree_31', 'bazi_semantic', 'bazi_condition_factor_202', 'bazi_semantic', 'bazi_condition_factor_203', 'bazi_semantic', 'source_ref', 'rel_smth_06_148', 'zaqi_ge_presence', 'rel_smth_06_149', 'toulu_chengdu', 'rel_smth_06_150', 'yafu_risk', 'evi_smth_06_148', 'zaqi_ge_presence', 'rule_zaqi', 'evi_smth_06_149', 'toulu_chengdu', 'rule_toulu', 'evi_smth_06_150', 'chongxing_taiguo_risk', 'rule_qisan', 'map_smth_06_099', 'map_smth_06_100']
    
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
        l1_anchor="smth_v1.0.0_杂气与四库藏蓄_001_L1",
    )
    version: str = "1.0.0"
