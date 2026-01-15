"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157797
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
    semantic_id="smth_v1.0.0_六戊日癸亥时断_正财临官与死处逢财_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六戊日癸亥时断正财临官与死处逢财(SemanticEntry):
    """
    - 原文（source_text）：

  六戊日癸亥时断。

  六戊日生时癸亥，正财临官死处逢；月通身旺财官旺，不贵即富福禄隆。戊日癸亥时，正财临官，癸水正财，甲木七煞，亥上甲长生癸禄旺，戊土死亥...
    """
    
    original_text: str = """- 原文（source_text）：

  六戊日癸亥时断。

  六戊日生时癸亥，正财临官死处逢；月通身旺财官旺，不贵即富福禄隆。戊日癸亥时，正财临官，癸水正财，甲木七煞，亥上甲长生癸禄旺，戊土死亥。若通身旺月，财官双美，大贵。身弱财官太重，平常。

  戊子日癸亥时，亥子相并，财官太旺。春印旺，贵。冬官旺，行南运，贵。

  戊寅日癸亥时，亥卯未月，官旺，行南运，大贵。寅午戌月，身旺，大贵。

  戊辰日癸亥时，春印旺，贵。夏身旺，吉。申子辰月，财旺，富。

  戊午日癸亥时，亥午暗合，春印旺，贵。夏身旺，吉。

  戊申日癸亥时，春印旺，贵。秋财旺，行南运，富。亥卯未月，官旺，贵。

  戊戌日癸亥时，春印旺，贵。夏身旺，吉。辰戌丑未月，大贵。

  戊日癸亥时上逢，正财临官喜身强；月通身旺财官旺，不贵即富福禄隆。戊日癸亥时准，财官同居相逢。若然身旺福无边，定主荣华富贵。

- 分字分词释义：

  - **正财临官**：癸水正财与甲木七煞同在亥上有气，财官同居。
  - **死处逢财**：戊土在亥为死地，但亥上财官双旺。
  - **财官双美**：财星与官星同旺的优良结构。

- 规范化释义（primary_lang_explained）：

  本节讲「六戊日，癸亥时」：

  - 癸水正财在亥得禄，甲木七煞在亥为长生，戊土在亥为死地，形成「死处逢财」的结构；
  - 若通身旺月，财官双美，大贵；身弱财官太重，则平常。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Wu Days with Gui-Hai Hour":

  - Gui Water Direct Wealth at Hai is at fortune; Jia Wood Seven-Killing at Hai is at longevity; Wu Earth at Hai is at death position—forming "life at death meeting wealth."
  - If connected with strong-body month, wealth-official double beauty achieves great nobility; if body is weak with heavy wealth-official, outcomes remain ordinary.

- 核心要点：

  - 本格以「正财临官」为核心，财官同居。
  - 身旺是关键，方能驾驭财官。
  - 死地逢财官，需身旺来化解。

- 详细解说：

  1. **正财临官的优势**  
     - 癸水正财在亥得禄，甲木七煞在亥为长生；  
     - 财官同居，形成双美结构。

  2. **死处逢财的风险**  
     - 戊土在亥为死地，日主力量较弱；  
     - 需要月令通火土之气，身旺方能用财官。

- 校勘与字词辨析：

  - 「福禄隆」形容福禄兴隆。
  - 「荣华富贵」形容显贵富裕。
  - **English**：
    - Describes glory, splendor, wealth and nobility.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_237]` `[trigger: 正财临官]` `[factor_trigger: zhengcai_linguan AND sichu_feng]` `[role: 主干]` 六戊日生时癸亥，正财临官死处逢。 → 《三命通会》卷八#六戊日癸亥时
  - `[ns_smth_08_238]` `[trigger: 财官旺]` `[factor_trigger: caiguan_wang AND bugui_jifu]` `[role: 主干依赖]` 月通身旺财官旺，不贵即富福禄隆。 → 《三命通会》卷八#六戊日癸亥时
  - `[ns_smth_08_239]` `[trigger: 身弱财重]` `[factor_trigger: shenruo_caizhong AND ping_chang]` `[role: 条件分支]` 身弱财官太重，平常。 → 《三命通会》卷八#六戊日癸亥时
  - `[ns_smth_08_240]` `[trigger: 荣华富贵]` `[factor_trigger: ronghua_fugui AND shenwang_fu]` `[role: 总结]` 若然身旺福无边，定主荣华富贵。 → 《三命通会》卷八#六戊日癸亥时"""
    normalized_text_zh: str = """"""
    subject: str = "六戊日癸亥时断：正财临官与死处逢财"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_wu', 'bazi_semantic', 'bazi_state_zhengcai_1', 'bazi_semantic', 'bazi_relation_factor_99', 'bazi_semantic', 'bazi_state_factor_264', 'bazi_semantic', 'hour_branch_hai', 'bazi_semantic', 'bazi_condition_factor_124', 'bazi_semantic', 'source_ref', 'rel_smth_08_178', 'zhengcai_linguan', 'rel_smth_08_179', 'sichu_fengcai', 'rel_smth_08_180', 'tongshenwang_yue', 'evi_smth_08_178', 'zhengcai_linguan', 'rule_linguandi2', 'evi_smth_08_179', 'sichu_fengcai', 'rule_fengcai2', 'evi_smth_08_180', 'caiguan_shuangmei', 'rule_shuangmei4', 'map_smth_08_119', 'map_smth_08_120']
    
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
        l1_anchor="smth_v1.0.0_六戊日癸亥时断_正财临官与死处逢财_001_L1",
    )
    version: str = "1.0.0"
