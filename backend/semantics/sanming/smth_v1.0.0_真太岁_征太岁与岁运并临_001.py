"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264358
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
    semantic_id="smth_v1.0.0_真太岁_征太岁与岁运并临_001",
    book_id="sanming",
    engine_id="bazi"
)
class 真太岁征太岁与岁运并临(SemanticEntry):
    """
    - **原文（source_text）**：  
  又有真太岁、征太岁之说，经云：生时相逢真太岁。假如甲子生人，又见甲子年，谓之真太岁。又各转趾煞，要大运日主与太岁相和相顺，其年则吉。若值刑冲破害，...
    """
    
    original_text: str = """- **原文（source_text）**：  
  又有真太岁、征太岁之说，经云：生时相逢真太岁。假如甲子生人，又见甲子年，谓之真太岁。又各转趾煞，要大运日主与太岁相和相顺，其年则吉。若值刑冲破害，与太岁互相战克则凶。如癸巳日逄丁亥流年日，干支冲克太岁，曰征运，干支伤冲太岁，亦曰征太岁干。支冲日干，支亦日征，其年则凶，灾祸未免。又如甲子流年，又是甲子运，谓之岁运并临，独羊刃七煞为凶，财官印绶亦吉。经云：岁运并临，灾殃立至。此指羊刃言也。又如甲子日见甲子太岁，谓之日年相并，如君子得之，谓之君臣庆会，其年利奏对，有面君之喜。若当省土人得之，有登荐仕进之象。又要与岁君帝座和恊，方为奇特。若是常俗小人遇之，最为不善。若生时相和，为灾稍轻。故经云：太岁当头立，诸神不敢当。

- **规范化释义（primary_lang_explained）**：  
  本段将太岁的不同特殊形态系统化：一是“真太岁”，如甲子日生又逢甲子年，生时与流年完全同柱；二是“征太岁/征运”，如癸巳日遇丁亥流年，日、时与太岁形成强烈冲克，被视为主动触犯太岁之象；三是“岁运并临”，如甲子流年又走甲子大运，年运同柱。作者指出，这些格局本身并非一概为凶：岁运并临时，若所临为财官印绶，反而有利于发福，只是逢羊刃七煞时特别危险，故有“岁运并临，灾殃立至”之语，多是就羊刃言。日年相并（甲子日见甲子太岁）若为君子或当省土之人所遇，则是“君臣庆会”，主奏对面君、仕进荐举之喜；若为常俗小人，则可能因权势过度而招祸。总之，“太岁当头立”代表年运权重极高，所有吉凶都会被放大，应结合格局与身份一并看待。

- **完整对等诠释（secondary_lang_full）**：  
  This section gives a taxonomy of special Tai Sui configurations. "True Tai Sui" describes the coincidence of natal and annual pillars—for example, a person born in Jia‑Zi who encounters a Jia‑Zi year. "Confronting Tai Sui" or "attacking the luck" refers to circumstances where the day and hour pillars severely clash with the annual Tai Sui, such as Gui‑Si day meeting Ding‑Hai year, producing strong stem‑branch conflicts. "Year and luck coinciding" arises when the annual pillar and the major‑luck pillar are identical, as in Jia‑Zi year during a Jia‑Zi decade. The text stresses that these are not uniformly disastrous: when the coinciding pillar represents Wealth, Officer, or Seal, it can bring substantial advancement, while overlap with Yang Blade or heavy Killings is genuinely dangerous, hence aphorisms like "when year and luck coincide, calamity comes swiftly," which are context‑dependent. When the day and year are the same pillar, noble persons experience this as a "ruler‑minister celebration," enjoying direct access to authority, whereas ordinary people may misuse such concentrated power and invite trouble. The key idea is that when Tai Sui stands "right on the head," its influence dominates, magnifying both fortune and misfortune depending on the chart and social position.

- **核心要点**：
  - 真太岁、征太岁、岁运并临等，都是太岁与日柱/大运关系特别紧张或特别同气的情形。
  - 岁运并临并非必凶，关键在所并之神是财官印纶还是羊刃七煞。
  - 日年相并对君子为“君臣庆会”，对小人则易因权势集中而招祸。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_097]` `[trigger: 真太岁]` `[factor_trigger: zhen_taisui AND shengshi_xiangfeng]` `[role: 主干]` 假如甲子生人，又见甲子年，谓之真太岁。 → 《三命通会》卷十#真太岁征太岁与岁运并临
  - `[ns_smth_10_098]` `[trigger: 岁运并临]` `[factor_trigger: suiyun_binglin AND yangran_qisha]` `[role: 主干依赖]` 岁运并临，独羊刃七煞为凶，财官印纶亦吉。 → 《三命通会》卷十#真太岁征太岁与岁运并临
  - `[ns_smth_10_099]` `[trigger: 君臣庆会]` `[factor_trigger: junchen_qinghui AND mian_jun_zhi_xi]` `[role: 条件分支]` 如君子得之，谓之君臣庆会，其年利奏对，有面君之喜。 → 《三命通会》卷十#真太岁征太岁与岁运并临
  - `[ns_smth_10_100]` `[trigger: 常俗小人]` `[factor_trigger: changsu_xiaoren AND zui_wei_bushan]` `[role: 总结]` 若是常俗小人遇之，最为不善。 → 《三命通会》卷十#真太岁征太岁与岁运并临

- **详细解说**：  
  在建模时，这一段提示我们将“太岁与日柱、大运的同柱或强冲”作为独立因子：一类是完全重合（真太岁、岁运并临、日年相并），一类是强烈冲战（征太岁）。对前者，需要结合所代表的十神类别与命主社会角色来判断其偏吉偏凶；对后者，则可直接作为高危年份加权。特别是“太岁当头立”，意味着无论吉神凶煞，其效应都被放大，因此需要把年运的权重显式提高。

- **校勘与字词辨析（双语）**：
  - **中文**：“转趾煞”在此与征太岁相关，多指干支与太岁形成伏吟反吟之类强烈作用，后文仍有展开。
  - **English**: The term "ruler‑minister celebration" signifies harmonious overlap of authority structures; it is not inherently moral, and its outcome depends on the character and position of the native."""
    normalized_text_zh: str = """"""
    subject: str = "真太岁、征太岁与岁运并临"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_真太岁_征太岁与岁运并临_001_L1",
    )
    version: str = "1.0.0"
