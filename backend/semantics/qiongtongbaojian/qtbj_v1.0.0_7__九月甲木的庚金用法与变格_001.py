"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.619966
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
    semantic_id="qtbj_v1.0.0_7__九月甲木的庚金用法与变格_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 7九月甲木的庚金用法与变格(SemanticEntry):
    """
    - **原文（source_text）**：
  或四柱木多，用丙用丁，皆不足异，耑用庚金为妙。凡四季甲木，总不外乎庚金。譬如木为犁，能疏季土，非庚金为犁嘴，安能疏土？虽用丙丁，癸庚决不可少也。九月却...
    """
    
    original_text: str = """- **原文（source_text）**：
  或四柱木多，用丙用丁，皆不足异，耑用庚金为妙。凡四季甲木，总不外乎庚金。譬如木为犁，能疏季土，非庚金为犁嘴，安能疏土？虽用丙丁，癸庚决不可少也。九月却不取土妻庚子，当取水妻木子。
  凡甲木，多见戊己，定作弃命从才而看。从才格，取火妻土子。

- **分字分词释义**：
  - **皆不足异**：都不足为奇 / 常见配置 / 非最优
  - **耑用庚金**：专门用庚金 / 首选用神 / 妙法
  - **四季甲木**：辰戌丑未月的甲木 / 土旺月 / 需庚
  - **犁嘴**：犁的铁嘴 / 比喻庚金 / 疏土之器
  - **疏季土**：疏松四季土 / 甲木功能 / 需庚配合
  - **弃命从才**：放弃自身从属于财 / 变格 / 土多木弱
  - **火妻土子**：以火为妻、以土为子 / 从财格六亲 / 配置

- **规范化释义（primary_lang_explained）**：
  如果四柱木多，用丙火或丁火泄秀，都不足为奇，专门用庚金（制劫疏土）才是妙法。凡是四季月（辰戌丑未）的甲木，总离不开庚金。比方说，木是犁，能疏松四季土，但如果没有庚金作为犁嘴（铁器），怎么能疏土呢？虽然用丙丁火，但癸水和庚金是决不可少的。九月（戌月）此时不取土为妻庚为子（非用庚格），应当取水为妻木为子（可能是指用印比帮身的情况，或文本有误，待考）。
  凡是甲木，多见戊己土，定作“弃命从财”来看。从财格，取火（食伤生财）为妻，土（财）为子。

- **完整对等诠释（secondary_lang_full）**：
  If the pillars have abundant Wood, using Bing or Ding is not extraordinary; exclusively using Geng Metal is the wondrous way. Generally, Jia Wood in the Four Seasons (Earth Months) cannot do without Geng Metal. For example, Wood is the plough that can loosen the Seasonal Earth; but without Geng Metal as the ploughshare, how can it loosen the Earth? Although Bing/Ding are used, Gui and Geng are indispensable. In the 9th Month, do not take Earth as Wife and Geng as Child; instead take Water as Wife and Wood as Child.
  Generally for Jia Wood, if Wu/Ji are numerous, view it as "Abandon Life Follow Wealth". For Follow Wealth pattern, take Fire as Wife and Earth as Child.

- **核心要点**：
  - **犁嘴理论**：甲木疏土需庚金（铁器）配合。无庚木钝。
  - **从财格**：土多木弱，从财。

- **详细解说**：
  - “木为犁...庚为犁嘴”是非常精彩的象法比喻。甲木虽克土，但戌土厚重且燥，木折。需金修整甲木尖端，使其锋利，方能疏土。
  - “九月却不取土妻庚子...”这句在不同版本有争议。若用庚，理应土妻金子。这里说取水妻木子，可能指身弱需印比帮身的情况，或者原文传抄错误。徐乐吾注认为此时甲木凋零，可能先求生机（水木）。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_151]` `[trigger: 四季甲木]` `[factor_trigger: season_earth_month AND tiangan_jia AND tiangan_geng]` `[role: 主干]` 凡四季甲木，总不外乎庚金。譬如木为犁，能疏季土，非庚金为犁嘴，安能疏土？ → 《穷通宝鉴·三秋甲木》#5.7
  - `[ns_qttbj_152]` `[trigger: 从财格]` `[factor_trigger: tiangan_jia AND earth_excessive AND pattern_abandon_life_follow_wealth]` `[role: 条件分支]` 凡甲木，多见戊己，定作弃命从才而看，从才格，取火妻土子。 → 《穷通宝鉴·三秋甲木》#5.7"""
    normalized_text_zh: str = """"""
    subject: str = "7. 九月甲木的庚金用法与变格"
    factor_refs: list = ['ploughshare', 'loosen_seasonal_earth']
    
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
        book_id="qiongtongbaojian",
        chapter="",
        l1_anchor="qtbj_v1.0.0_7__九月甲木的庚金用法与变格_001_L1",
    )
    version: str = "1.0.0"
