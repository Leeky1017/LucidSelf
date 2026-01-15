"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157520
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
    semantic_id="smth_v1.0.0_六丙日乙未时断_食神入库与偏财暗藏_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六丙日乙未时断食神入库与偏财暗藏(SemanticEntry):
    """
    - 原文（source_text）：

  六丙日乙未时断。

  六丙日生时乙未，食神入库火通明；身旺富贵并周全，若值伤官平常命。丙日乙未时，食神入库，丙以乙为倒食，未中乙木无力，丙合辛财，未合乙木...
    """
    
    original_text: str = """- 原文（source_text）：

  六丙日乙未时断。

  六丙日生时乙未，食神入库火通明；身旺富贵并周全，若值伤官平常命。丙日乙未时，食神入库，丙以乙为倒食，未中乙木无力，丙合辛财，未合乙木，有暗辛金财，火生身旺，发财。然月令当如何？若火太旺，喜月气通金水者贵；火弱，通木火者亦贵。

  丙子日乙未时，子未相害，自成家立业。子月，行南运，贵。卯丑，行金水运，俱贵。寅、木火运亦贵。年月无水，行北运，大贵。

  丙寅日乙未时，刑妻克子，自立家业。春，行金水运，贵。秋，行木火运，风宪。

  丙辰日乙未时，贵，寅午戌、亥卯未年月，贵显。巳酉丑，行北运，风宪。子丑，行水运，大贵。

  丙午日乙未时好，月通金水气者贵。无水，行北运亦贵。酉月，正财；子，正官；卯，倒食，俱贵。丑月，杂气财官，大贵。

  丙申日乙未时，辰午亥年月，官居六卿。戌月，合火，行西北运，官至二品。

  丙戌日乙未时，春秋，行金水运，官至三品。夏冬平。丑月，玉堂学士。辰戌丑未年月，财丰。

  时逢乙未食神地，丙午丙寅富贵人；月气不通天地暗，如无金水是常伦。丙日乙未时准，食神入库相当。若能通局亦荣昌。否则常人模样。

- 分字分词释义：

  - **食神入库**：乙木食神入未库，食神有收藏。
  - **偏财暗藏**：未中暗藏辛金偏财，财源隐秘。
  - **火通明**：丙火明亮，得木生助则更加光明。

- 规范化释义（primary_lang_explained）：

  本节讲「六丙日，乙未时」：

  - 乙木（食神/偏印）入未库，未中暗藏辛金偏财，丙火身旺可发财；
  - 若火太旺，喜月令通金水来制衡；火弱，通木火来生助亦贵。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Bing Days with Yi-Wei Hour":

  - Yi Wood (Food God/Indirect Seal) enters Wei treasury; Wei secretly contains Xin Metal Indirect Wealth; with strong Bing Fire body, wealth can be obtained.
  - If fire is too prosperous, prefer monthly pillar connecting Metal-Water for balance; if fire is weak, connecting Wood-Fire for support also brings nobility.

- 核心要点：

  - 本格以「食神入库」为核心，结构偏储藏。
  - 暗藏偏财，财源隐秘但可得。
  - 需要金水来平衡，否则火旺无财。

- 详细解说：

  1. **食神入库的特点**  
     - 乙木入未库，食神有收藏；  
     - 需要冲开或行运配合，方能发挥食神的生财功能。

  2. **平衡的重要性**  
     - 火旺喜金水来制衡；火弱喜木火来生助；  
     - 需要根据日主强弱来判断用神。

- 校勘与字词辨析：

  - 「天地暗」形容命局不明朗，缺乏亮点。
  - 「资财宏广」指财富丰厚、家业兴旺。
  - **English**：
    - Refers to abundant wealth and flourishing family enterprise.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_125]` `[trigger: 食神入库]` `[factor_trigger: shishen_ruku AND huo_tongming]` `[role: 主干]` 六丙日生时乙未，食神入库火通明。 → 《三命通会》卷八#六丙日乙未时
  - `[ns_smth_08_126]` `[trigger: 身旺富贵]` `[factor_trigger: shenwang_fugui AND bing_zhouquan]` `[role: 主干依赖]` 身旺富贵并周全，若值伤官平常命。 → 《三命通会》卷八#六丙日乙未时
  - `[ns_smth_08_127]` `[trigger: 通金水贵]` `[factor_trigger: tong_jinshui AND huo_tai_wang]` `[role: 条件分支]` 若火太旺，喜月气通金水者贵。 → 《三命通会》卷八#六丙日乙未时
  - `[ns_smth_08_128]` `[trigger: 通局荣昌]` `[factor_trigger: tongju_rongchang AND fou_changren]` `[role: 总结]` 若能通局亦荣昌，否则常人模样。 → 《三命通会》卷八#六丙日乙未时"""
    normalized_text_zh: str = """"""
    subject: str = "六丙日乙未时断：食神入库与偏财暗藏"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_bing', 'bazi_semantic', 'bazi_state_shishen_4', 'bazi_semantic', 'bazi_relation_piancai_1', 'bazi_semantic', 'bazi_state_fire_1', 'bazi_semantic', 'hour_branch_wei', 'bazi_semantic', 'bazi_condition_metal_water_1', 'bazi_semantic', 'source_ref', 'rel_smth_08_094', 'shishen_ruku', 'rel_smth_08_095', 'piancai_ancang', 'rel_smth_08_096', 'jinshui_pingheng', 'evi_smth_08_094', 'shishen_ruku', 'rule_ruku', 'evi_smth_08_095', 'piancai_ancang', 'rule_ancang', 'evi_smth_08_096', 'huo_tongming', 'rule_tongming', 'map_smth_08_063', 'map_smth_08_064']
    
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
        l1_anchor="smth_v1.0.0_六丙日乙未时断_食神入库与偏财暗藏_001_L1",
    )
    version: str = "1.0.0"
