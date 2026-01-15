"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157681
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
    semantic_id="smth_v1.0.0_六丁日辛亥时断_财临官地与死处逢财_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六丁日辛亥时断财临官地与死处逢财(SemanticEntry):
    """
    - 原文（source_text）：

  六丁日辛亥时断。

  六丁日生时辛亥，财临官地死处逢；月通身旺财官旺，不贵即富福禄隆。丁日辛亥时，财临官地，辛金偏财，壬水正官，亥上壬旺辛长生，丁火死亥。...
    """
    
    original_text: str = """- 原文（source_text）：

  六丁日辛亥时断。

  六丁日生时辛亥，财临官地死处逢；月通身旺财官旺，不贵即富福禄隆。丁日辛亥时，财临官地，辛金偏财，壬水正官，亥上壬旺辛长生，丁火死亥。若通身旺月，财官双美，大贵。身弱财官太重，平常。

  丁丑日辛亥时，亥丑半合，春身旺，贵。冬官旺，行南运，贵。

  丁卯日辛亥时，亥卯半合，春身旺，大贵。冬官旺，行南运，贵。

  丁巳日辛亥时，亥巳相冲，伤妻害子。春身旺，贵。冬官旺，吉。

  丁未日辛亥时，亥未半合，春身旺，贵。冬官旺，吉。

  丁酉日辛亥时，春身旺，行金水运，贵。秋财旺，行南运，富。

  丁亥日辛亥时，两亥自刑，伤妻害子。春身旺，贵。冬官旺，行南运，贵。

  丁日辛亥时上逢，财临官地喜身强；月通身旺财官旺，不贵即富福禄隆。丁日辛亥时准，财官同居相逢。若然身旺福无边，定主荣华富贵。

- 分字分词释义：

  - **财临官地**：辛金偏财与壬水正官同在亥上有气，财官同居。
  - **死处逢财**：丁火在亥为死地，但亥上财官双旺。
  - **财官双美**：财星与官星同旺的优良结构。

- 规范化释义（primary_lang_explained）：

  本节讲「六丁日，辛亥时」：

  - 辛金偏财在亥为长生，壬水正官在亥得禄，丁火在亥为死地，形成「死处逢财」的结构；
  - 若通身旺月，财官双美，大贵；身弱财官太重，则平常。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ding Days with Xin-Hai Hour":

  - Xin Metal Indirect Wealth at Hai is at long life; Ren Water Direct Official at Hai is prosperous; Ding Fire at Hai is at death position—forming "life at death meeting wealth."
  - If connected with strong-body month, wealth-official double beauty achieves great nobility; if body is weak with heavy wealth-official, outcomes remain ordinary.

- 核心要点：

  - 本格以「财临官地」为核心，财官同居。
  - 身旺是关键，方能驾驭财官。
  - 死地逢财官，需身旺来化解。

- 详细解说：

  1. **财临官地的优势**  
     - 辛金偏财在亥为长生，壬水正官在亥得禄；  
     - 财官同居，形成双美结构。

  2. **死处逢财的风险**  
     - 丁火在亥为死地，日主力量较弱；  
     - 需要月令通火木之气，身旺方能用财官。

- 校勘与字词辨析：

  - 「福禄隆」形容福禄兴隆。
  - 「荣华富贵」形容显贵富裕。
  - **English**：
    - Describes glory, splendor, wealth and nobility.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_189]` `[trigger: 财临官地]` `[factor_trigger: cailin_guandi AND sichu_feng]` `[role: 主干]` 六丁日生时辛亥，财临官地死处逢。 → 《三命通会》卷八#六丁日辛亥时
  - `[ns_smth_08_190]` `[trigger: 财官旺]` `[factor_trigger: caiguan_wang AND bugui_jifu]` `[role: 主干依赖]` 月通身旺财官旺，不贵即富福禄隆。 → 《三命通会》卷八#六丁日辛亥时
  - `[ns_smth_08_191]` `[trigger: 身弱财重]` `[factor_trigger: shenruo_caizhong AND ping_chang]` `[role: 条件分支]` 身弱财官太重，平常。 → 《三命通会》卷八#六丁日辛亥时
  - `[ns_smth_08_192]` `[trigger: 荣华富贵]` `[factor_trigger: ronghua_fugui AND shenwang_fu]` `[role: 总结]` 若然身旺福无边，定主荣华富贵。 → 《三命通会》卷八#六丁日辛亥时"""
    normalized_text_zh: str = """"""
    subject: str = "六丁日辛亥时断：财临官地与死处逢财"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_ding', 'bazi_semantic', 'bazi_state_factor_201', 'bazi_semantic', 'bazi_relation_factor_99', 'bazi_semantic', 'bazi_state_factor_264', 'bazi_semantic', 'hour_branch_hai', 'bazi_semantic', 'bazi_condition_factor_124', 'bazi_semantic', 'source_ref', 'rel_smth_08_142', 'cailin_guandi', 'rel_smth_08_143', 'sichu_fengcai', 'rel_smth_08_144', 'tongshenwang_yue', 'evi_smth_08_142', 'cailin_guandi', 'rule_linguandi', 'evi_smth_08_143', 'sichu_fengcai', 'rule_fengcai', 'evi_smth_08_144', 'caiguan_shuangmei', 'rule_shuangmei3', 'map_smth_08_095', 'map_smth_08_096']
    
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
        l1_anchor="smth_v1.0.0_六丁日辛亥时断_财临官地与死处逢财_001_L1",
    )
    version: str = "1.0.0"
