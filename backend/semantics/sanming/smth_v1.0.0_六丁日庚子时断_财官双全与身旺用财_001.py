"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157572
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
    semantic_id="smth_v1.0.0_六丁日庚子时断_财官双全与身旺用财_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六丁日庚子时断财官双全与身旺用财(SemanticEntry):
    """
    - 原文（source_text）：

  六丁日庚子时断。

  六丁日生逢庚子，财旺官生喜气新；月有倚托身强健，一举成名天下知。丁日庚子时，财官双全，丁以壬为官，庚为财，子上壬旺庚生，喜忌详月气。...
    """
    
    original_text: str = """- 原文（source_text）：

  六丁日庚子时断。

  六丁日生逢庚子，财旺官生喜气新；月有倚托身强健，一举成名天下知。丁日庚子时，财官双全，丁以壬为官，庚为财，子上壬旺庚生，喜忌详月气。若通身旺月者，大贵；不通月气，身弱财官反为祸。

  丁丑日庚子时，子丑合，丑为官库，富贵。春财生官；夏，身旺用财；秋，财旺；冬，水旺身弱，贫。卯戌年月，行南运，贵。

  丁卯日庚子时，身旺用财官，贵。巳酉丑月，合财；亥卯未月，合印，俱吉。申子辰月，官旺；寅午戌月，身旺，俱大贵。

  丁巳日庚子时，贵。春夏身旺，秋财旺，冬官旺，俱吉。辰戌丑未月，杂气财官，大贵。

  丁未日庚子时，官星入库，若冲开，贵。卯未寅午年月，行西北运，大贵。

  丁酉日庚子时，寅巳午月，身旺用财官，大贵。申酉，财旺；亥子，官旺，俱吉。

  丁亥日庚子时，双官禄旺，若通身旺月者，文章显达，大贵。不通，平常。

  丁日时逢庚子全，财官双美福无边；柱中身旺通月气，定主功名冠士贤。丁日时临庚子，官星财旺同排。若还身旺福悠哉，定主荣华富贵。

- 分字分词释义：

  - **财官双全**：庚金正财与壬水正官在子上皆有气，财官双旺。
  - **财旺官生**：庚金财星生助壬水官星，形成财官相生的结构。
  - **身旺用财**：日主身旺方能驾驭财官，否则反受其累。

- 规范化释义（primary_lang_explained）：

  本节讲「六丁日，庚子时」：

  - 庚金正财与壬水正官在子上皆有气，形成「财官双全」的结构；
  - 若月令通身旺之气，身强健可用财官，则大贵；若身弱财官重，反为祸患。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ding Days with Geng-Zi Hour":

  - Geng Metal Direct Wealth and Ren Water Direct Official both have energy at Zi, forming "wealth-official double complete."
  - If monthly pillar connects with strong-body energy, body is healthy and can utilize wealth-official, achieving great nobility; if body is weak with heavy wealth-official, this becomes harmful.

- 核心要点：

  - 本格以「财官双全」为核心，结构优良。
  - 身旺是关键，方能驾驭财官。
  - 歌诀强调：身旺通月气，定主功名冠士贤。

- 详细解说：

  1. **财官双全的优势**  
     - 子上壬水正官当令，庚金正财得生；  
     - 财官相生，形成良性循环。

  2. **身旺的必要性**  
     - 丁火在子为胎地，力量较弱；  
     - 需要月令通火木之气，身旺方能用财官。

- 校勘与字词辨析：

  - 「一举成名天下知」形容科举登第、名扬四海。
  - 「福悠哉」指福禄悠长，安享富贵。
  - **English**：
    - Long-lasting fortune; enjoying wealth and comfort.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_145]` `[trigger: 财官双全]` `[factor_trigger: caiguan_shuangquan AND xiqi_xin]` `[role: 主干]` 六丁日生逢庚子，财旺官生喜气新。 → 《三命通会》卷八#六丁日庚子时
  - `[ns_smth_08_146]` `[trigger: 身强健]` `[factor_trigger: shenqiang_jian AND yi_ju_chengming]` `[role: 主干依赖]` 月有倚托身强健，一举成名天下知。 → 《三命通会》卷八#六丁日庚子时
  - `[ns_smth_08_147]` `[trigger: 身旺通月]` `[factor_trigger: shenwang_tongyue AND da_gui]` `[role: 条件分支]` 若通身旺月者，大贵；不通月气，身弱财官反为祸。 → 《三命通会》卷八#六丁日庚子时
  - `[ns_smth_08_148]` `[trigger: 荣华富贵]` `[factor_trigger: ronghua_fugui AND fu_youai]` `[role: 总结]` 若还身旺福悠哉，定主荣华富贵。 → 《三命通会》卷八#六丁日庚子时"""
    normalized_text_zh: str = """"""
    subject: str = "六丁日庚子时断：财官双全与身旺用财"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_ding', 'bazi_semantic', 'bazi_state_factor_183', 'bazi_semantic', 'bazi_relation_factor_83', 'bazi_semantic', 'bazi_state_factor_213', 'bazi_semantic', 'hour_branch_zi', 'bazi_semantic', 'bazi_condition_factor_124', 'bazi_semantic', 'source_ref', 'rel_smth_08_109', 'caiguan_shuangquan', 'rel_smth_08_110', 'caiwang_guansheng', 'rel_smth_08_111', 'tongshenwang_yue', 'evi_smth_08_109', 'caiguan_shuangquan', 'rule_shuangquan', 'evi_smth_08_110', 'caiwang_guansheng', 'rule_guansheng', 'evi_smth_08_111', 'shenwang_yongcai', 'rule_yongcai2', 'map_smth_08_073', 'map_smth_08_074']
    
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
        l1_anchor="smth_v1.0.0_六丁日庚子时断_财官双全与身旺用财_001_L1",
    )
    version: str = "1.0.0"
