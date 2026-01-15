"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157450
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
    semantic_id="smth_v1.0.0_六丙日戊子时断_财官生旺与食神相会_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六丙日戊子时断财官生旺与食神相会(SemanticEntry):
    """
    - 原文（source_text）：

  六丙日戊子时断。

  六丙日生时戊子，财官生旺遇食神；月气相扶为最贵，身衰无倚是常人。丙日戊子时，官旺财生，丙用辛为财，癸为官，丙合辛，戊合癸，子中癸旺辛...
    """
    
    original_text: str = """- 原文（source_text）：

  六丙日戊子时断。

  六丙日生时戊子，财官生旺遇食神；月气相扶为最贵，身衰无倚是常人。丙日戊子时，官旺财生，丙用辛为财，癸为官，丙合辛，戊合癸，子中癸旺辛生，丙火无气。若通火气，月有倚托者贵；不通贫下。通木气亦吉。

  丙子日戊子时，寅巳卯未月，木能生火，大贵。冬月，丙火无气，贫夭。戌月，行火土运，五六品贵。忌丁巳月，夭；己酉月，破家失土，身贱。

  丙寅日戊子时，生卯丑月，清贵。寅戌，平常。夏月身旺，柱有水金方吉。子月正官，大贵。忌癸巳月，刑；癸亥月，恶死；己酉月，大败。

  丙辰日戊子时，丙辰为日德格，喜见官星。若生戌月，身旺最宜，武贵。寅月，行金水运，中贵。申月三合，合煞有印，贵。忌己巳月，凶死；己亥月，自刑死；癸丑月，破祖恶死。

  丙午日戊子时，丙午为日刃格，要官煞制合。生辰戌丑未月，大富。亥卯未寅年月，大贵，申巳，文贵三品，武贵不永。纯子，为子午双包贵格。忌丁巳月，恶死；丁亥月，自刑恶死；辛丑月，孤独。

  丙申日戊子时，巳午年月，行东北运，风宪，子月，行木火运，三品。丑七品，酉亥，虽遇贵反贱。忌癸巳月，中年刑。乙酉月，破败。

  丙戌日戊子时，春生，印绶最吉。夏，身太旺，平常。秋，财旺身衰，有寄托则贵。纯酉年月，文进之贵。忌己亥月，死不全尸；癸丑月，贫夭。

  活计生涯四季隆，丙逢戊子食官同；无伤晚岁皆成就，吉处遭凶险处通。丙子时逢戊子，官星食福同排。午丁未遇且沉埋，交通中年大快。父母妻子喜合。胸中隐匿文才。若逢好运一时来，富贵清闲自在。

- 分字分词释义：

  - **财官生旺**：辛金偏财与癸水正官在子上皆有气，形成财官双旺的结构。
  - **食神相会**：戊土食神与官星癸水相合，食神制官的同时又与官合。
  - **日德格**：丙辰日为日德格，喜见官星，忌刑冲克害。
  - **日刃格**：丙午日为日刃格，羊刃在日支，需官煞制合方吉。
  - **子午双包**：子午相冲形成特殊格局，若配合得当可成贵格。

- 规范化释义（primary_lang_explained）：

  本节讲「六丙日，戊子时」：

  - 丙火日主在子上无气，但子中癸水正官旺盛、辛金偏财有生，戊土食神与癸官相合；
  - 若月令通火气或木气，身有倚托，则财官可用，主贵；若不通月气，身弱无依，则贫下；
  - 六丙日（子、寅、辰、午、申、戌）各有不同格局特点，需视具体配合而定。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Bing Days with Wu-Zi Hour":

  - Bing Fire day-master has no energy at Zi, but Zi contains prosperous Gui Water (Direct Official) and Xin Metal (Indirect Wealth) with life; Wu Earth (Food God) combines with Gui Official.
  - If monthly pillar channels Fire or Wood energy with proper support, then Wealth-Official are usable, indicating nobility; if not connected to monthly energy, weak body without support indicates poverty.
  - The six Bing days (Zi, Yin, Chen, Wu, Shen, Xu) each have different pattern characteristics requiring specific combination analysis.

- 核心要点：

  - 本格以「财官生旺」为核心，但需身旺方能承担。
  - 食神合官形成制约与合作的双重关系。
  - 歌诀强调：无伤晚岁皆成就，关键在于运势配合。

- 详细解说：

  1. **财官生旺的用法**  
     - 子中癸水正官当令，辛金偏财得生；  
     - 若丙火身旺能承担，则财官为用，主仕途与财运。

  2. **身衰无倚的风险**  
     - 丙火在子为胎地，力量较弱；  
     - 若月令不通火木之气，身弱无依，难以驾驭财官。

  3. **六丙日的格局差异**  
     - 丙辰日德、丙午日刃，各有特殊格局规则；  
     - 需根据日支特点，配合月令与行运综合判断。

- 校勘与字词辨析：

  - 「子午双包」为特殊格局名，本稿保留其传统称谓。
  - 「交通中年大快」指中年后运势通畅，发展顺利。
  - **English**：
    - Fortune flows smoothly after middle age; development proceeds well.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_097]` `[trigger: 财官生旺]` `[factor_trigger: caiguan_shengwang AND yu_shishen]` `[role: 主干]` 六丙日生时戊子，财官生旺遇食神。 → 《三命通会》卷八#六丙日戊子时
  - `[ns_smth_08_098]` `[trigger: 月气相扶]` `[factor_trigger: yueqi_xiangfu AND wei_zui_gui]` `[role: 主干依赖]` 月气相扶为最贵，身衰无倚是常人。 → 《三命通会》卷八#六丙日戊子时
  - `[ns_smth_08_099]` `[trigger: 日德日刃]` `[factor_trigger: ride_riren AND xi_jian_guan]` `[role: 条件分支]` 丙辰为日德格，喜见官星。丙午为日刃格，要官煞制合。 → 《三命通会》卷八#六丙日戊子时
  - `[ns_smth_08_100]` `[trigger: 晚岁成就]` `[factor_trigger: wansui_chengjiu AND wu_shang]` `[role: 总结]` 无伤晚岁皆成就，吉处遭凶险处通。 → 《三命通会》卷八#六丙日戊子时"""
    normalized_text_zh: str = """"""
    subject: str = "六丙日戊子时断：财官生旺与食神相会"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_bing', 'bazi_semantic', 'bazi_state_factor_167', 'bazi_semantic', 'bazi_relation_shishen_4', 'bazi_semantic', 'bazi_state_factor_168', 'bazi_semantic', 'hour_branch_zi', 'bazi_semantic', 'bazi_condition_fire_wood', 'bazi_semantic', 'source_ref', 'rel_smth_08_073', 'caiguan_shengwang', 'rel_smth_08_074', 'shishen_heguan', 'rel_smth_08_075', 'tonghuomu_qi', 'evi_smth_08_073', 'caiguan_shengwang', 'rule_caiguan', 'evi_smth_08_074', 'shishen_heguan', 'rule_heguan', 'evi_smth_08_075', 'shenshuai_wuyi', 'rule_shenshuai', 'map_smth_08_049', 'map_smth_08_050']
    
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
        l1_anchor="smth_v1.0.0_六丙日戊子时断_财官生旺与食神相会_001_L1",
    )
    version: str = "1.0.0"
