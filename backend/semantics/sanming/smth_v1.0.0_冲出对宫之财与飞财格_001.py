"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412270
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
    semantic_id="smth_v1.0.0_冲出对宫之财与飞财格_001",
    book_id="sanming",
    engine_id="bazi"
)
class 冲出对宫之财与飞财格(SemanticEntry):
    """
    - **原文（source_text）**：
    日干同月干，日支同时支，冲出对宫之财是也。得此格当发财禄，忌泄气，凶。如壬申日生，时支亦申，二申冲出寅中甲丙为财为用，岁运遇子则化成水局。如日干是...
    """
    
    original_text: str = """- **原文（source_text）**：
    日干同月干，日支同时支，冲出对宫之财是也。得此格当发财禄，忌泄气，凶。如壬申日生，时支亦申，二申冲出寅中甲丙为财为用，岁运遇子则化成水局。如日干是庚被局，泄气伤官，不能生财，岁君、柱内再逢七煞克身，必死。盖飞财格，支辰不可变化他局故也。如戊寅、己未、戊寅、甲寅，三寅一甲七煞，六月全无财气，比肩甚旺，却得三寅冲出申中长生之水为财，运行西北，资财巨万。
    - 分字分词释义：
    - **日干同月干，日支同时支**：日柱与月柱（或时柱）天干相同、地支相同，形成“干支重叠”的结构，为飞财格的基本形态。
  - **冲出对宫之财**：通过两个相同的地支冲对宫之支，将对宫所藏之财星冲出显用。
  - **壬申日、申时冲出寅中甲丙为财为用**：以壬申日、申时为例，两申冲寅，对宫寅中甲木、丙火皆为壬水之财（甲为偏财、丙为正财）。
  - **忌泄气**：若日干本身被局中结构严重泄气（如庚金被水局泄），则即便飞出之财旺盛，也难以真正为我所用。
  - **支辰不可变化他局**：参与冲财的支神，不能再被合化为他局，否则财气被合走，不为我用。
  - **三寅一甲七煞**：指戊寅、己未、戊寅、甲寅一类命局中，寅木重重、甲木为七煞，却因重寅冲出申中之水为财。
    - 白话原意：
    飞财格，是以“重叠之支冲出对宫财星”为特征的发财格。其基本条件是：日干与月干（或时干）相同，日支与时支相同，两重支位彼此相冲，对向一个藏财的宫位，把其中的财星冲出来为我所用。典型如壬申日生、申时再逢申：
    二申冲寅，对宫寅中藏甲木、丙火，皆可为壬水之财；若岁运又逢子水，使申子辰会局，则须谨慎——一则财气可能被化入水局，二则庚金日主若被水泄，反不利财用。
    又如戊寅、己未、戊寅、甲寅之类：表面是“七煞重重、无财可言”，但三寅一甲冲向申位，冲出申中壬水长生之财。若运行西北金水之地，反而能成巨富之命。可见飞财格的妙处在于：财星原本不在明处，而是藏在对宫，被重支一冲而起。

    - **完整对等诠释（secondary_lang_full）**：
      The "Flying Wealth" pattern describes a way of making money where the stem and branch of the day are repeated by the month or hour, and the doubled branch clashes the opposite palace to drive out wealth that is normally hidden. The classical example is a Ren‑Shen day with Shen also at the hour: the two Shens clash the opposite Yin, forcing out Jia Wood and Bing Fire, both of which count as wealth for Ren Water. Under favourable conditions this wealth does not simply appear in small, steady amounts, but arrives in sudden bursts—opportunities, windfalls or ventures that pay off quickly.

      The same logic applies in charts like Wu‑Yin, Ji‑Wei, Wu‑Yin, Jia‑Yin: on the surface there is "nothing but hostile stars and no clear wealth," yet three Yin branches and one Jia clash the opposite Shen, releasing Ren Water in its place of growth. When the chart then walks through supportive western metal‑and‑water territories, this released wealth can accumulate into great fortunes. The pattern demands care, however. If the day‑stem is heavily drained by the surrounding structure, or if the branches that are supposed to clash are instead pulled into other combinations—such as being absorbed into a water or fire bureau—the flying wealth leaks away or is taken over by others. In practice, the chart must be judged on whether it truly has a clean pair of repeated branches, a solid opposite‑palace store of wealth, and luck cycles that allow the clash to function without destroying the body.

    - 核心要点：
    - 飞财格以**日干月干同、日支时支同、重支冲出对宫财星**为基本结构。
  - 发财的前提是日主不能被严重泄气或被七煞重重克制，否则飞出的财反为祸端。
  - 参与冲财的支辰不可再合化成他局，否则财气被合走，不为我用。
  - 命局原无明财、反而七煞比肩过盛者，若合飞财格，多有“暗处发财、横获资财”的特征。
    - 详细解说：
    飞财之“飞”，在于财星并非静止，而是通过冲动而被“飞出”对宫，转而为我所用。此类格局与前述破财格有表面相似：都从冲、破、刑等动作里取财。但破财重在“无财可见而破中取财”，飞财则重在“重叠之支冲出对宫财星”，二者不可混为一谈。
    在壬申日、申时的例子中，壬水日主得申为长生，又得比肩同类之助；两申冲寅，使寅中甲丙之财飞出。若命局中再有适当的土、金以制水、泄火，则财气可循序流转，不致泛滥成灾。反之，若日干为庚金而落入水局，则庚金被水局严重泄耗，再逢七煞，容易应在伤身、灾病，而非发财。
    对于“支辰不可变化他局”的要求，关键在于防止财气被别的合局夺走。例如参与冲财的申、寅若再被合入申子辰水局或寅午戌火局，则财星之气不再专为日主所用，而成他局之气，飞财格的力量也随之削弱。
    - **校勘与字词辨析（双语）**：
   - **校勘与字词辨析（双语）**：

  - 原文“日干同月干，日支同时支，冲出对宫之财是也”一句，为飞财格的定义，本稿据底本保留，仅以现代标点分句。
  - “戊寅、己未、戊寅、甲寅，三寅一甲七煞”一例，本稿保留原文表述，仅在白话中解释其为“以重寅冲申出水为财”的结构，不另改命局。
  - “支辰不可变化他局”一语，容易被今人忽略，本稿在释义与详细解说中反复强调其为成格关键条件之一。
  - **English**：
    - The definition "Day-stem same as month-stem, day-branch same as hour-branch, clashing out the opposite-palace wealth" is preserved with modern punctuation only.
    - The example "Wu-Yin, Ji-Wei, Wu-Yin, Jia-Yin, three Yin one Jia seven-kill" is kept; vernacular explanation clarifies it as "using multiple Yin to clash Shen and release water as wealth."
    - The phrase "branch configuration must not transform into another formation" is repeatedly emphasized as a key condition for pattern success.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_021]` `[trigger: 飞财格定义]` `[factor_trigger: feicai_ge_presence]` `[role: 主干]` 日干同月干，日支同时支，冲出对宫之财是也。 → 《三命通会》卷六#飞财格
  - `[ns_smth_06_022]` `[trigger: 二申冲财]` `[factor_trigger: er_shen_chong_yin AND jia_bing_wei_cai]` `[role: 主干依赖]` 壬申日生，时支亦申，二申冲出寅中甲丙为财为用。 → 《三命通会》卷六#飞财格
  - `[ns_smth_06_023]` `[trigger: 支辰不化]` `[factor_trigger: zhi_chen_bu_bian_hua]` `[role: 条件分支]` 支辰不可变化他局故也。 → 《三命通会》卷六#飞财格
  - `[ns_smth_06_024]` `[trigger: 资财巨万]` `[factor_trigger: san_yin_chong_shen AND zi_cai_ju_wan]` `[role: 总结]` 三寅一甲七煞...却得三寅冲出申中长生之水为财，运行西北，资财巨万。 → 《三命通会》卷六#飞财格"""
    normalized_text_zh: str = """"""
    subject: str = "冲出对宫之财与飞财格"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_10', 'bazi_semantic', 'bazi_structure_config_2', 'bazi_semantic', 'bazi_state_day_master', 'bazi_semantic', 'bazi_state_hehua_degree', 'bazi_semantic', 'bazi_condition_factor_137', 'bazi_semantic', 'bazi_condition_factor_138', 'bazi_semantic', 'source_ref', 'rel_smth_06_016', 'feicai_ge_presence', 'rel_smth_06_017', 'rizhu_chengzai_feicai', 'rel_smth_06_018', 'feicai_nianfen_risk', 'evi_smth_06_016', 'duigong_cangcai_config', 'rule_feicai', 'evi_smth_06_017', 'rizhu_chengzai_feicai', 'rule_xieqi', 'evi_smth_06_018', 'chongchu_hequan_score', 'rule_bianhua', 'map_smth_06_011', 'map_smth_06_012']
    
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
        l1_anchor="smth_v1.0.0_冲出对宫之财与飞财格_001_L1",
    )
    version: str = "1.0.0"
