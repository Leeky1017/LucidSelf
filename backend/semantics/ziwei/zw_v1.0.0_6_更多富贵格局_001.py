"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.778476
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
    semantic_id="zw_v1.0.0_6_更多富贵格局_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 6更多富贵格局(SemanticEntry):
    """
    ##### 1.6.1 科明禄暗，位列三台

- 原文（断句）：

  科明禄暗，位列三台。假如甲生人安命亥宫，值科星守在命宫，又天禄居寅，则寅与亥合，故曰科明禄暗。

- 分字分词释义：

  - ...
    """
    
    original_text: str = """##### 1.6.1 科明禄暗，位列三台

- 原文（断句）：

  科明禄暗，位列三台。假如甲生人安命亥宫，值科星守在命宫，又天禄居寅，则寅与亥合，故曰科明禄暗。

- 分字分词释义：

  - **科明禄暗**：化科星明显守命，禄星暗合相助，明暗配合。
  - **位列三台**：官至三台高位（尚书台、中书台、门下台）。
  - **甲生人安命亥宫**：甲年生人命宫在亥宫。
  - **科星守命**：化科星在命宫守护。
  - **天禄居寅**：禄存在寅宫，与亥宫暗合。
  - **寅与亥合**：寅亥相合，六合之一。
  - **生来贫贱**：出生即贫穷低贱。
  - **劫空临财福**：地劫天空临财帛宫或福德宫。
  - **李广不封**：汉代名将李广一生未能封侯，比喻功名难成。
  - **擎羊逢力士**：擎羊遇到力士星，主刑克。

- 规范化释义（primary_lang_explained）：

  科明禄暗位列三台。如甲生人安命亥宫值科星守在命宫，又天禄居寅则寅与亥合，故曰科明禄暗。

- 核心要点：**科星明守命宫**，**禄存暗合**，主位列三台。

##### 1.6.2 日月同临，官居侯伯

- 原文（断句）：

  日月同临官居侯伯。假如命安丑宫，日月在未，命安未宫，日月在丑，谓之同临是也。诀云：日月同临论对宫，丙辛人遇福兴隆。

- 规范化释义（primary_lang_explained）：

  日月同临官居侯伯。如命安丑宫日月在未，命安未宫日月在丑，谓之同临是也。诀云日月同临论对宫，丙辛人遇福兴隆。

- 核心要点：**日月对宫照命**，**丙辛生人**福兴隆，主官居侯伯。

##### 1.6.3 巨机同宫，公卿之位

- 原文（断句）：

  巨机同宫，公卿之位；假如辛、乙生人，安命卯宫，二星守命，更遇昌左右上格，如丙生人次之，丁生人亦主平常，其余宫分，不在此论。

- 规范化释义（primary_lang_explained）：

  巨机同宫公卿之位。如辛乙生人安命卯宫二星守命更遇昌左右上格，如丙生人次之，丁生人亦主平常，其余宫分不在此论。

- 核心要点：**巨门天机卯宫同度**，**辛乙生人**为上格，主公卿之位。

##### 1.6.4 贪铃并守，将相之名

- 原文（断句）：

  贪铃并守，将相之名。假如辰戌丑未子宫安命值之，是为入庙，依此断。如加吉，惟子辰二宫坐守尤佳。戊己生人合格。

- 规范化释义（primary_lang_explained）：

  贪铃并守将相之名。如辰戌丑未子宫安命值之是为入庙依此断，如加吉惟子辰二宫坐守尤佳，戊己生人合格。

- 核心要点：**贪狼铃星**同守命宫，**辰戌丑未子入庙**，**戊己生人**主将相之名。

##### 1.6.5 天魁天钺，盖世文章

- 原文（断句）：

  天魁天钺，盖世文章；如身命坐魁，对宫天钺，身命坐钺，对宫天魁，是谓坐贵向贵，更会吉化，其贵必然矣。

- 规范化释义（primary_lang_explained）：

  天魁天钺盖世文章。如身命坐魁对宫天钺，身命坐钺对宫天魁，是谓坐贵向贵，更会吉化其贵必然。

- 核心要点：**魁钺坐守对照**，**坐贵向贵**，主盖世文章。

##### 1.6.6 天禄天马，惊人甲第

- 原文（断句）：

  天禄天马，惊人甲第，如寅、申巳亥四宫安命，值天禄、天马坐守命宫，更三合吉守照，依此断加杀不是。

- 规范化释义（primary_lang_explained）：

  天禄天马惊人甲第。如寅申巳亥四宫安命值天禄天马坐守命宫，更三合吉守照依此断，加杀不是。

- 核心要点：**禄马寅申巳亥**坐命，**三合吉照**，主惊人甲第。

##### 1.6.7 贪狼火星，居庙旺，名镇诸邦

- 原文（断句）：

  贪狼火星，居庙旺，名镇诸邦。如辰戌、丑未四宫安命，值此上格，三方吉化拱照尤美。如卯宫安命，无杀次之，加羊陀、劫空不是。

- 规范化释义（primary_lang_explained）：

  贪狼火星居庙旺名镇诸邦。如辰戌丑未四宫安命值此上格，三方吉化拱照尤美。如卯宫安命无杀次之，加羊陀劫空不是。

- 核心要点：**贪狼火星**（火贪格），**辰戌丑未入庙**，主名镇诸邦。

##### 1.6.8 巨日同宫，官封三代

- 原文（断句）：

  巨日同宫，官封三代；寅宫安命，值此无劫空四杀，上格申宫，次之，巳亥不为美。

- 规范化释义（primary_lang_explained）：

  巨日同宫官封三代。寅宫安命值此无劫空四杀为上格，申宫次之，巳亥不为美。

- 核心要点：**巨门太阳寅宫**同度，无凶杀，主官封三代。

##### 1.6.9 紫府朝垣，食禄万钟

- 原文（断句）：

  紫府朝垣，食禄万钟，如寅宫安命午戌宫，紫府来朝；申宫安命子、辰二宫，有紫府来朝，是为人君访臣之象，奇格也。更遇流禄巡逢，必然位至公卿。

- 规范化释义（primary_lang_explained）：

  紫府朝垣食禄万钟。如寅宫安命午戌宫紫府来朝，申宫安命子辰二宫有紫府来朝，是为人君访臣之象奇格也。更遇流禄巡逢必然位至公卿。

- 完整对等诠释（secondary_lang_full）：

  The extended prosperity patterns describe a family of superior configurations that promise high rank and abundant stipends. They include cases where Transformation of Authority and Transformation of Salary guard the Wealth and Fortune palaces, Sun and Moon mutually illuminate each other across the chart, Jumen and Tianji share one palace in dignified positions, Tanlang and Huoxing reside together in temple strength, Tiankui and Tianyue flank the Life Palace as "sitting noble facing noble", Tianlu and Tianma combine in mobile palaces, and Ziwei and Tianfu either occupy the same palace as the native or approach it from three directions. When these patterns are supported by benefic stars, placed in dignified signs, and matched with the appropriate day‑stem natives, they point to ministers and generals, brilliant examination success, and hereditary honors that can extend across several generations.
- 核心要点：**紫府朝垣**（寅申命，紫府来朝），**人君访臣之象**，主食禄万钟。

- 叙事素材（narrative_snippets）：

  - **日月并明**："日月并明佐九重"，太阳太阴同时入庙的极贵格局。
  - **机巨同宫**："巨机同宫公卿之位"，巨门天机在卯宫同度的贵格。
  - **火贪同宫**："贪火相逢无不贵"，贪狼火星同度入庙的暴发格。
  - **坐贵向贵**："天魁天钺临命，名之坐贵向贵"，魁钺夹命的贵人格。
  - **紫府朝垣**："紫府朝垣食禄万钟，人君访臣之象"，紫府三合来朝的极贵格。
  - **现代应用**：本批可作为识别"贵格结构"的参考——日月并明、机巨同宫、火贪同度、魁钺夹命、紫府朝垣皆为高格标志。

  **L2 叙事素材层（规范格式）**：

  - `[ns_zwds_j2_052]` `[trigger: 贪铃并守格]` `[factor_trigger: geju_tanlingbingshou]` `[role: 条件分支]` 贪铃并守格为贪狼铃星同守命宫入庙的贵格。 → 《骨髓赋》"贪铃并守，将相之名"
  - `[ns_zwds_j2_053]` `[trigger: 魁钺坐向格]` `[factor_trigger: geju_kuiyuezuoxiang]` `[role: 条件分支]` 魁钺坐向格为魁钺坐守对照的贵人格。 → 《骨髓赋》"坐贵向贵"
  - `[ns_zwds_j2_054]` `[trigger: 禄马交驰格]` `[factor_trigger: geju_lumajiaochi]` `[role: 条件分支]` 禄马交驰格为禄存天马同守命宫的贵格。 → 《骨髓赋》"天禄天马，惊人甲第"
  - `[ns_zwds_j2_055]` `[trigger: 火贪格]` `[factor_trigger: geju_huotan]` `[role: 条件分支]` 火贪格为贪狼火星同守入庙的暴发格。 → 《骨髓赋》"贪狼火星，名镇诸邦"
  - `[ns_zwds_j2_056]` `[trigger: 巨日同宫格]` `[factor_trigger: geju_juritonggong]` `[role: 条件分支]` 巨日同宫格为巨门太阳在寅宫同度的贵格。 → 《骨髓赋》"巨日同宫，官封三代"
  - `[ns_zwds_j2_057]` `[trigger: 紫府朝垣格]` `[factor_trigger: geju_zifuchaoyuan]` `[role: 条件分支]` 紫府朝垣格为紫府三合来朝的极贵格。 → 《骨髓赋》"紫府朝垣，食禄万钟"
  - `[ns_zwds_j2_058]` `[trigger: 日月并明格]` `[factor_trigger: geju_riyuebingming]` `[role: 条件分支]` 日月并明格为太阳太阴同时入庙的极贵格。 → 《骨髓赋》"日月并明佐九重"
  - `[ns_zwds_j2_059]` `[trigger: 机巨同宫格]` `[factor_trigger: geju_jijutonggong]` `[role: 条件分支]` 机巨同宫格为天机巨门在卯宫同度的贵格。 → 《骨髓赋》"巨机同宫公卿之位"
  - `[ns_zwds_j2_060]` `[trigger: 将相之名结果]` `[factor_trigger: result_jiangxiang_zhiming]` `[role: 结果]` 将相之名为官至将相的极贵结果。 → 《骨髓赋》"将相之名"
  - `[ns_zwds_j2_061]` `[trigger: 盖世文章结果]` `[factor_trigger: result_gaishi_wenzhang]` `[role: 结果]` 盖世文章为文章盖世、才华横溢的结果。 → 《骨髓赋》"盖世文章"
  - `[ns_zwds_j2_062]` `[trigger: 惊人甲第结果]` `[factor_trigger: result_jingren_jiadi]` `[role: 结果]` 惊人甲第为科甲及第、金榜题名的结果。 → 《骨髓赋》"惊人甲第"
  - `[ns_zwds_j2_063]` `[trigger: 名镇诸邦结果]` `[factor_trigger: result_mingzhen_zhubang]` `[role: 结果]` 名镇诸邦为威名远播、声震四方的结果。 → 《骨髓赋》"名镇诸邦"
  - `[ns_zwds_j2_064]` `[trigger: 官封三代结果]` `[factor_trigger: result_guanfeng_sandai]` `[role: 结果]` 官封三代为官爵延续三代的极贵结果。 → 《骨髓赋》"官封三代"
  - `[ns_zwds_j2_065]` `[trigger: 食禄万钟结果]` `[factor_trigger: result_shilu_wanzhong]` `[role: 结果]` 食禄万钟为俸禄丰厚的富贵结果。 → 《骨髓赋》"食禄万钟"
  - `[ns_zwds_j2_066]` `[trigger: 佐九重结果]` `[factor_trigger: result_zuo_jiuchong]` `[role: 结果]` 佐九重为辅佐帝王的极贵结果。 → 《骨髓赋》"佐九重"
  - `[ns_zwds_j2_067]` `[trigger: 人君访臣格]` `[factor_trigger: geju_renjunfangchen]` `[role: 条件分支]` 人君访臣格为紫府来朝命宫的极贵格。 → 《骨髓赋》"人君访臣之象""""
    normalized_text_zh: str = """"""
    subject: str = "6 更多富贵格局"
    factor_refs: list = ['combo_keminglu', 'combo_riyuetonglin', 'combo_jujitonggong', 'combo_huotan', 'combo_zuoguixianggui', 'combo_zifuchaoyuan', 'result_guanfengsandai', 'source_ref', 'rel_gengfugui_001', 'fugui_zileixing', 'rel_gengfugui_002', 'guiren_peihe', 'rel_gengfugui_003', 'fugui_laiyuan', 'evi_gengfugui_001', 'combo_keminglu', 'rule_keminglu', 'evi_gengfugui_002', 'combo_riyuetonglin', 'rule_riyuetonglin', 'evi_gengfugui_003', 'combo_zifuchaoyuan', 'rule_zifuchaoyuan', 'concept_high_pattern', 'concept_noble_support', 'concept_multi_path']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_6_更多富贵格局_001_L1",
    )
    version: str = "1.0.0"
