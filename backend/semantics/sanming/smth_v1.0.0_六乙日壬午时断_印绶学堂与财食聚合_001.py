"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157389
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
    semantic_id="smth_v1.0.0_六乙日壬午时断_印绶学堂与财食聚合_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六乙日壬午时断印绶学堂与财食聚合(SemanticEntry):
    """
    - 原文（source_text）：

  六乙日壬午时断。

  六乙日生时壬午，印绶生身财食聚；月通水木禄丰盈，不通月气平常数。乙日壬午时，印绶学堂，乙木长生在午，见壬为印，用丁为食，己为财，午上...
    """
    
    original_text: str = """- 原文（source_text）：

  六乙日壬午时断。

  六乙日生时壬午，印绶生身财食聚；月通水木禄丰盈，不通月气平常数。乙日壬午时，印绶学堂，乙木长生在午，见壬为印，用丁为食，己为财，午上丁己建旺，若通水月气者，文章秀丽；不通月气，平常衣禄，通运亦好。

  乙丒日壬午时，春夏多富贵。秋冬官印，或纯煞透干，尤吉。

  乙卯日壬午时高，丑月，入杂气财官；申酉月，身煞两停，俱主显贵。纯午酉年月，三四品；辰戌，平常。

  乙巳日壬午时吉，春夏富贵。秋冬平常。

  乙未日壬午时，寅卯身旺，亥子印旺，丑月财官印三奇，俱主贵显。申月正官，尤吉，若庚午、丁亥年月，食神同窠，就食见禄，富贵。

  乙酉日壬午时，春吉。秋夏平常。柱纯乙酉，透庚合化，或见印助，大贵。

  乙亥日壬午时，春身旺，夏福厚，秋反复，冬吉庆。

  乙日生逢壬午时，月通水木贵人钦；运行官旺无冲破，家业丰隆事称心。乙日时逢壬午，食神印绶同宫。无冲无破不相刑，信是声名响应。词馆清秀高士，文章出众超群，贵人喜见小人憎，中末峥嵘之命。

- 分字分词释义：

  - **印绶学堂**：壬水为乙木之印，午为乙木长生之地，印绶与学堂同居，象征文学修养与知识积累。
  - **财食聚**：午中藏丁火（食神）、己土（偏财），食神与财星同聚于时支，形成生发链条。
  - **食神同窠**：食神与日主同居旺地，形成「就食见禄」的优良结构。
  - **词馆清秀**：比喻文章才华出众，适合从事文职或学术工作。

- 规范化释义（primary_lang_explained）：

  本节讲「六乙日，壬午时」：

  - 乙木在午为长生，壬水为印绶，午中又藏丁火食神、己土偏财，形成印绶生身、食神生财的连环结构；
  - 若月令通水木之气，则印绶有根，文章秀丽，禄位丰盈；若不通月气，则只是平常衣禄，但行运得当仍可发达；
  - 六乙日（丑、卯、巳、未、酉、亥）各有吉凶差异，需视月令与年月配合而定。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Yi Days with Ren-Wu Hour":

  - Yi Wood at Wu reaches Long Life; Ren Water serves as Seal, while Wu hides Ding Fire (Food God) and Ji Earth (Indirect Wealth), forming a chain structure of Seal supporting body and Food God generating wealth.
  - When monthly pillar channels Water-Wood energy, the Seal is rooted, producing refined literary talent and abundant fortune; without monthly energy connection, it remains ordinary livelihood, though good fortune cycles can still bring success.
  - The six Yi days (Chou, Mao, Si, Wei, You, Hai) each have different fortunes depending on monthly pillar and year-month combinations.

- 核心要点：

  - 本格以「印绶学堂」为核心，强调文学才华与知识积累。
  - 午中财食聚合，形成食神生财的良性结构。
  - 歌诀强调：若无冲破刑克，则声名响应、家业丰隆。

- 详细解说：

  1. **印绶学堂的用法**  
     - 壬水为乙木正印，午为乙木长生，印绶与长生同位，主文学修养深厚；  
     - 若月令通水气，印绶有根，则文章秀丽，适合从事文职、学术或教育工作。

  2. **财食聚合的结构**  
     - 午中藏丁火（食神）、己土（偏财），食神生财，财星有源；  
     - 若能配合身旺，则财源稳定，生活富足。

  3. **六乙日的差异**  
     - 乙丑、乙卯、乙巳、乙未、乙酉、乙亥六日，因日支所带的根气不同，吉凶有别；  
     - 春夏身旺时较吉，秋冬需看官印配合。

- 校勘与字词辨析：

  - 「词馆清秀高士」形容文人气质，本稿保留其象征意义，不作具体官职解读。
  - 「中末峥嵘」指中年后运势渐佳，与「先难后易」同义。
  - **English**：
    - Improvement over time; synonymous with "difficult first, easy later."

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_073]` `[trigger: 印绶学堂]` `[factor_trigger: yinxu_xuetang AND caishi_ju]` `[role: 主干]` 六乙日生时壬午，印绶生身财食聚。 → 《三命通会》卷八#六乙日壬午时
  - `[ns_smth_08_074]` `[trigger: 通水木气]` `[factor_trigger: tong_shuimu AND lu_fengying]` `[role: 主干依赖]` 月通水木禄丰盈，不通月气平常数。 → 《三命通会》卷八#六乙日壬午时
  - `[ns_smth_08_075]` `[trigger: 食神同窠]` `[factor_trigger: shishen_tongke AND jiu_shi_jian_lu]` `[role: 条件分支]` 食神同窠，就食见禄，富贵。 → 《三命通会》卷八#六乙日壬午时
  - `[ns_smth_08_076]` `[trigger: 声名响应]` `[factor_trigger: shengming_xiangying AND wuchong_wupo]` `[role: 总结]` 无冲无破不相刑，信是声名响应。 → 《三命通会》卷八#六乙日壬午时"""
    normalized_text_zh: str = """"""
    subject: str = "六乙日壬午时断：印绶学堂与财食聚合"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_yi', 'bazi_semantic', 'bazi_state_factor_158', 'bazi_semantic', 'bazi_relation_factor_74', 'bazi_semantic', 'bazi_state_factor_159', 'bazi_semantic', 'hour_branch_wu', 'bazi_semantic', 'bazi_condition_water_wood', 'bazi_semantic', 'source_ref', 'rel_smth_08_055', 'yinxu_xuetang', 'rel_smth_08_056', 'caishi_juhe', 'rel_smth_08_057', 'tongshuimu_qi', 'evi_smth_08_055', 'yinxu_xuetang', 'rule_xuetang', 'evi_smth_08_056', 'caishi_juhe', 'rule_caishi', 'evi_smth_08_057', 'tongshuimu_qi', 'rule_tongqi', 'map_smth_08_037', 'map_smth_08_038']
    
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
        l1_anchor="smth_v1.0.0_六乙日壬午时断_印绶学堂与财食聚合_001_L1",
    )
    version: str = "1.0.0"
