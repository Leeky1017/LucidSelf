"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157601
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
    semantic_id="smth_v1.0.0_六丁日癸卯时断_偏官临印与身旺制煞_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六丁日癸卯时断偏官临印与身旺制煞(SemanticEntry):
    """
    - 原文（source_text）：

  六丁日癸卯时断。

  六丁日生时癸卯，偏官临印喜身强；若无金水来伤印，富贵荣华福禄长。丁日癸卯时，偏官临印，丁用癸为偏官，乙为印，卯上乙旺癸沐浴，若通身旺...
    """
    
    original_text: str = """- 原文（source_text）：

  六丁日癸卯时断。

  六丁日生时癸卯，偏官临印喜身强；若无金水来伤印，富贵荣华福禄长。丁日癸卯时，偏官临印，丁用癸为偏官，乙为印，卯上乙旺癸沐浴，若通身旺月，无财坏印、无官混煞者，大贵。有财官，平常。

  丁丑日癸卯时，丑刑卯，刑伤妻子。春身旺，贵。夏平，秋富，冬吉。

  丁卯日癸卯时，身强印旺，科名有望。春大贵。夏平，秋富，冬官旺，吉。

  丁巳日癸卯时，贵。春身旺，夏平，秋富，冬吉。寅午戌年月，大贵。

  丁未日癸卯时，亥卯未月，印旺，大贵。寅午戌月，身旺制煞，贵。

  丁酉日癸卯时，卯酉相冲，伤妻害子。春吉，夏平，秋凶，冬吉。寅午戌、亥卯未年月，贵。

  丁亥日癸卯时，亥卯未月，印旺，大贵。寅午戌月，身旺制煞，贵。申子辰月，官煞混杂，平。

  丁日癸卯时上排，偏官临印最为奇；柱无财官来混杂，定主荣华富贵齐。丁日癸卯时准，偏官临印相逢。若然身旺福无边，定主文章贵显。

- 分字分词释义：

  - **偏官临印**：癸水七煞在卯上沐浴，乙木偏印在卯为建禄，煞临印地。
  - **身旺制煞**：日主身旺可以制伏七煞，化险为夷。
  - **无财坏印**：若无财星克制印绶，则印绶可用。

- 规范化释义（primary_lang_explained）：

  本节讲「六丁日，癸卯时」：

  - 癸水七煞在卯为沐浴，乙木偏印在卯为建禄，形成「偏官临印」的结构；
  - 若通身旺月，无财坏印、无官混煞，则大贵；有财官，则平常。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Ding Days with Gui-Mao Hour":

  - Gui Water Seven-Killing at Mao is at bathing; Yi Wood Indirect Seal at Mao is prosperous—forming "seven-killing approaching seal."
  - If connected with strong-body month, without wealth destroying seal or official mixing killing, this achieves great nobility; with wealth-official present, outcomes remain ordinary.

- 核心要点：

  - 本格以「偏官临印」为核心，印制煞为关键。
  - 身旺制煞、印制煞，形成良性结构。
  - 最忌财坏印、官煞混杂。

- 详细解说：

  1. **偏官临印的用法**  
     - 癸水七煞在卯为沐浴，力量较弱；  
     - 乙木偏印在卯为建禄，印星有力可制煞。

  2. **身旺制煞的优势**  
     - 若身旺，可驾驭七煞为权威；  
     - 印制煞、身制煞，形成双重保护。

- 校勘与字词辨析：

  - 「科名有望」指科举功名可期。
  - 「富贵齐」形容富贵兼得。
  - **English**：
    - Describes wealth and nobility both attained.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_157]` `[trigger: 偏官临印]` `[factor_trigger: pianguan_linyin AND xi_shenqiang]` `[role: 主干]` 六丁日生时癸卯，偏官临印喜身强。 → 《三命通会》卷八#六丁日癸卯时
  - `[ns_smth_08_158]` `[trigger: 无金水伤]` `[factor_trigger: wu_jinshui_shang AND fugui_ronghua]` `[role: 主干依赖]` 若无金水来伤印，富贵荣华福禄长。 → 《三命通会》卷八#六丁日癸卯时
  - `[ns_smth_08_159]` `[trigger: 无财坏印]` `[factor_trigger: wucai_huaiyin AND wu_guan_hunsha]` `[role: 条件分支]` 若通身旺月，无财坏印、无官混煞者，大贵。 → 《三命通会》卷八#六丁日癸卯时
  - `[ns_smth_08_160]` `[trigger: 富贵齐]` `[factor_trigger: fugui_qi AND wenzhang_gui_xian]` `[role: 总结]` 柱无财官来混杂，定主荣华富贵齐。 → 《三命通会》卷八#六丁日癸卯时"""
    normalized_text_zh: str = """"""
    subject: str = "六丁日癸卯时断：偏官临印与身旺制煞"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_ding', 'bazi_semantic', 'bazi_state_factor_189', 'bazi_semantic', 'bazi_condition_factor_43', 'bazi_semantic', 'bazi_state_factor_190', 'bazi_semantic', 'hour_branch_mao', 'bazi_semantic', 'bazi_condition_factor_124', 'bazi_semantic', 'source_ref', 'rel_smth_08_118', 'pianguan_linyin', 'rel_smth_08_119', 'shenwang_zhisha', 'rel_smth_08_120', 'tongshenwang_yue', 'evi_smth_08_118', 'pianguan_linyin', 'rule_linyin', 'evi_smth_08_119', 'shenwang_zhisha', 'rule_zhisha', 'evi_smth_08_120', 'wucai_huaiyin', 'rule_wucai', 'map_smth_08_079', 'map_smth_08_080']
    
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
        l1_anchor="smth_v1.0.0_六丁日癸卯时断_偏官临印与身旺制煞_001_L1",
    )
    version: str = "1.0.0"
