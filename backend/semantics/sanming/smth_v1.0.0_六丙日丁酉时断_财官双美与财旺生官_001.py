"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157538
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
    semantic_id="smth_v1.0.0_六丙日丁酉时断_财官双美与财旺生官_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六丙日丁酉时断财官双美与财旺生官(SemanticEntry):
    """
    - 原文（source_text）：

  六丙日丁酉时断。

  六丙日生时丁酉，月中财旺福非轻；运行官旺加身位，金紫功名冠士英。丙日丁酉时，财旺生官，丙以辛为财，癸为官，丁为劫，酉上辛旺癸生，丁坐...
    """
    
    original_text: str = """- 原文（source_text）：

  六丙日丁酉时断。

  六丙日生时丁酉，月中财旺福非轻；运行官旺加身位，金紫功名冠士英。丙日丁酉时，财旺生官，丙以辛为财，癸为官，丁为劫，酉上辛旺癸生，丁坐败乡。柱有比肩帮身，喜通金水月，身旺者大贵。不通月气，平常。

  丙子日丁酉时，子酉相破，伤妻害子。纯子，行金运，清贵。午未戌亥年月，俱吉。

  丙寅日丁酉时，寅酉比肩，有木气月者贵。巳酉丑、申子辰，无破者贵。

  丙辰日丁酉时，日德格，年月无壬戊，运行北方，大贵。若金水太旺，身弱，平常。

  丙午日丁酉时，日刃格，年月有癸酉制合，更通金水旺气，大贵。

  丙申日丁酉时，贵显。春秋金木运，贵。夏火运，平。亥子丑月，行北运，大贵。

  丙戌日丁酉时，子月，水官；申酉，金财，俱贵。戌月，平常。寅卯，印绶；辰丑未，杂气财官，俱吉。

  丁丙酉时号建财，若逢官旺发科魁；运中禄马无冲破，冠带衣冠出将才。丙日时逢丁酉，财官酉地根深。若还禄旺不刑冲，富贵人人钦敬。

- 分字分词释义：

  - **财官双美**：辛金偏财与癸水正官在酉上皆有气，财官双旺。
  - **财旺生官**：辛金财星生助癸水官星，形成财官相生的结构。
  - **建财**：财星在建禄位，财源稳固。

- 规范化释义（primary_lang_explained）：

  本节讲「六丙日，丁酉时」：

  - 酉上辛金偏财旺盛，癸水正官得生，丁火劫财在酉为败地，形成「财旺生官」的结构；
  - 若柱有比肩帮身，且通金水月气，身旺者大贵；不通月气，则平常。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Bing Days with Ding-You Hour":

  - At You, Xin Metal Indirect Wealth is prosperous, Gui Water Direct Official receives support; Ding Fire Rob-Wealth at You is at decline position—forming a "prosperous wealth generating official" structure.
  - If the chart has Companion to help body and connects with Metal-Water monthly energy, strong body achieves great nobility; without monthly connection, outcomes remain ordinary.

- 核心要点：

  - 本格以「财官双美」为核心，结构优良。
  - 需身旺方能用财官，身弱则难承担。
  - 最忌食伤透露、傲物气高。

- 详细解说：

  1. **财官双美的优势**  
     - 酉为辛金建禄，财星旺盛；癸水官星得辛金生助；  
     - 形成「财旺生官」的良性结构。

  2. **身旺的必要性**  
     - 丁火劫财在酉为败地，帮身有限；  
     - 需要柱有比肩或通身旺月气，方能用财官。

- 校勘与字词辨析：

  - 「冠带衣冠出将才」形容功成名就、出将入相。
  - 「中运发达利名」指中年运势通畅，名利双收。
  - **English**：
    - Middle-age fortune flows smoothly; both fame and profit gained.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_133]` `[trigger: 财官双美]` `[factor_trigger: caiguan_shuangmei AND fu_fei_qing]` `[role: 主干]` 六丙日生时丁酉，月中财旺福非轻。 → 《三命通会》卷八#六丙日丁酉时
  - `[ns_smth_08_134]` `[trigger: 财旺生官]` `[factor_trigger: caiwang_shengguan AND jiashen_wei]` `[role: 主干依赖]` 运行官旺加身位，金紫功名冠士英。 → 《三命通会》卷八#六丙日丁酉时
  - `[ns_smth_08_135]` `[trigger: 禄旺不刑]` `[factor_trigger: luwang_buxing AND fugui_qinjing]` `[role: 条件分支]` 若还禄旺不刑冲，富贵人人钦敬。 → 《三命通会》卷八#六丙日丁酉时
  - `[ns_smth_08_136]` `[trigger: 冠带衣冠]` `[factor_trigger: guandai_yiguan AND chu_jiangcai]` `[role: 总结]` 冠带衣冠出将才。 → 《三命通会》卷八#六丙日丁酉时"""
    normalized_text_zh: str = """"""
    subject: str = "六丙日丁酉时断：财官双美与财旺生官"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_bing', 'bazi_semantic', 'bazi_state_factor_264', 'bazi_semantic', 'bazi_state_factor_299', 'bazi_semantic', 'bazi_state_factor_180', 'bazi_semantic', 'hour_branch_you', 'bazi_semantic', 'bazi_condition_factor_55', 'bazi_semantic', 'source_ref', 'rel_smth_08_100', 'caiguan_shuangmei', 'rel_smth_08_101', 'caiwang_shengguan', 'rel_smth_08_102', 'shenwang_yongcaiguan', 'evi_smth_08_100', 'caiguan_shuangmei', 'rule_shuangmei', 'evi_smth_08_101', 'caiwang_shengguan', 'rule_shengguan', 'evi_smth_08_102', 'jiancai', 'rule_jiancai', 'map_smth_08_067', 'map_smth_08_068']
    
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
        l1_anchor="smth_v1.0.0_六丙日丁酉时断_财官双美与财旺生官_001_L1",
    )
    version: str = "1.0.0"
