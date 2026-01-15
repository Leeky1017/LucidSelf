"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412519
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
    semantic_id="smth_v1.0.0_食神同窠与本家之福_001",
    book_id="sanming",
    engine_id="bazi"
)
class 食神同窠与本家之福(SemanticEntry):
    """
    - **原文（source_text）**：

  食神同窠：谓甲食丙，甲子人见丙子之类，十三位即同，乃本家物也，得此者不贵即富。月不如日，日不如时，若互换生旺带禄，贵者大贵。如韩魏公：戊申、庚申、庚...
    """
    
    original_text: str = """- **原文（source_text）**：

  食神同窠：谓甲食丙，甲子人见丙子之类，十三位即同，乃本家物也，得此者不贵即富。月不如日，日不如时，若互换生旺带禄，贵者大贵。如韩魏公：戊申、庚申、庚辰、庚辰；宋秦桧：庚午、己丑、乙卯、壬午；又明王崇古少保：乙亥、辛巳、戊申、庚申是也。如倒食本家，甲子年见壬子时，庚子年见戊子时，亦贵，但损子。

- 分字分词释义：

  - **食神同窠**：日主与食神同居一支，如甲子见丙子，日、时同为子，食神与日主“同窠而居”。
  - **十三位即同**：指天干地支在节气中的位置相同或极近，属同一“家门”的气场。
  - **本家物也**：比喻食神之福来自“自家门户”，非外来偶得。
  - **月不如日，日不如时**：食神落在时支的影响最大，其次是日支，再次为月支。

- **规范化释义（primary_lang_explained）**：

  食神同窠格，强调的是“我与食神同处一室”的亲近关系。以甲子见丙子为例，甲以丙为食，食神与日主同在子位，且同属一旬一气，象征福分与才华既来自自家根基，又能被本人直接消化、运用。

  原文以韩魏公、秦桧、王崇古等命例为证，说明此类格局若再配合官、财、印等吉神，不仅衣食丰足，而且多主显达。若倒食同窠（如甲子见壬子等），则虽仍有贵象，却往往在子嗣方面有所折损。

- 核心要点：

  - 以**日主与食神同居一支**为特征，尤重时支同窠。
  - 多主福自本家、才自本源，而非全倚外缘。
  - 需防偏印（倒食）同窠，以免在子嗣与健康上付出代价。

- 详细解说：

  与一般食神格相比，食神同窠更强调“同源性”与“可掌控性”：

  - 福分多来自家世基础、早年教育与自身天赋，而非后天投机；
  - 人的性情往往较为温厚、内向，善于在熟悉环境中施展才华；
  - 若行运再遇食神、印绶生助，则如家族中多代积累的福份在某一代集中释放。

  然而，一旦偏印或七煞同窠，便可能出现“自家之物反成内耗”的情形：例如倒食同窠，既克制食神，又牵连子息宫，往往应于子嗣稀少或子女缘分较薄。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_105]` `[trigger: 食神同窠]` `[factor_trigger: shishen_tongke AND benjia_wu]` `[role: 主干]` 食神同窠者，甲食丙，甲子人见丙子，十三位即同，乃本家物也。 → 《三命通会》卷六#食神同窠与本家之福
  - `[ns_smth_06_106]` `[trigger: 位置优先]` `[factor_trigger: yue_buru_ri AND ri_buru_shi]` `[role: 主干依赖]` 月不如日，日不如时，若互换生旺带禄，贵者大贵。 → 《三命通会》卷六#食神同窠与本家之福
  - `[ns_smth_06_107]` `[trigger: 倒食同窠]` `[factor_trigger: daoshi_tongke AND sunzi]` `[role: 条件分支]` 倒食本家，甲子年见壬子时，亦贵，但损子。 → 《三命通会》卷六#食神同窠与本家之福
  - `[ns_smth_06_108]` `[trigger: 同窠效应]` `[factor_trigger: shishen_tongke AND bugui_jifu]` `[role: 总结]` 得食神同窠者，不贵即富，福自本家、才自本源。 → 《三命通会》卷六#食神同窠与本家之福

- **校勘与字词辨析（双语）**：

  - “十三位即同”一语，本稿不作精细历法考据，而以“同支、同旬、同气”概括其意。
  - 命例所引人物，仅用以说明格局层次，本稿不对史实作再考证。
  - “不贵即富”在本稿中理解为“要么显达，要么厚实富足”，并非所有命例皆兼而有之。
  - **English**：
    - The example charts are summarized for common patterns; not all cases have every feature mentioned."""
    normalized_text_zh: str = """"""
    subject: str = "食神同窠与本家之福"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_shishen_marker', 'bazi_semantic', 'bazi_structure_factor_81', 'bazi_semantic', 'bazi_state_degree_9', 'bazi_semantic', 'bazi_state_shishen_pianyin', 'bazi_semantic', 'bazi_condition_pianyin_1', 'bazi_semantic', 'bazi_condition_factor_166', 'bazi_semantic', 'source_ref', 'rel_smth_06_079', 'shishen_tongke_presence', 'rel_smth_06_080', 'huhuan_shengwan_dailu', 'rel_smth_06_081', 'pianyin_keshi_risk', 'evi_smth_06_079', 'shishen_tongke_presence', 'rule_tongke', 'evi_smth_06_080', 'tongke_weizhi_cengji', 'rule_weizhi', 'evi_smth_06_081', 'shishen_pianyin_qufen', 'rule_daoshi', 'map_smth_06_053', 'map_smth_06_054']
    
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
        l1_anchor="smth_v1.0.0_食神同窠与本家之福_001_L1",
    )
    version: str = "1.0.0"
