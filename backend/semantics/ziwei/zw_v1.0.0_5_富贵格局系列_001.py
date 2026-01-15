"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.778462
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
    semantic_id="zw_v1.0.0_5_富贵格局系列_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 5富贵格局系列(SemanticEntry):
    """
    ##### 1.5.1 出世荣华：权禄守财福之位

- 原文（断句）：

  出世荣华，权禄守财福之位，权禄守财帛，福德入庙吉多，定主荣华，身命值之亦然。

- 分字分词释义：

  - **出世荣华...
    """
    
    original_text: str = """##### 1.5.1 出世荣华：权禄守财福之位

- 原文（断句）：

  出世荣华，权禄守财福之位，权禄守财帛，福德入庙吉多，定主荣华，身命值之亦然。

- 分字分词释义：

  - **出世荣华**：一出生就享有荣华富贵，先天带贵。
  - **权禄守财福之位**：化权化禄守在财帛宫和福德宫。
  - **财帛入庙吉多**：财帛宫有吉星入庙，多有吉曜拱照。
  - **福德入庙**：福德宫星曜处于庙旺状态。
  - **文昌文曲**：北斗文星，主科甲功名与才艺。
  - **多学多能**：学识广博、才艺多端。
  - **左辅右弼**：辅佐之星，主敦厚可靠的品格。
  - **克守克厚**：性情谨慎守成、敦厚踏实。
  - **辰戌巳亥卯酉**：六个宫位，昌曲守此六宫为得地。

- 规范化释义（primary_lang_explained）：

  出世荣华为权禄守财福之位。化权化禄守财帛福德二宫入庙吉多，定主荣华，身命值之亦然。

- 核心要点：**化权化禄**守财帛、福德二宫，入庙吉多，主出世荣华。

##### 1.5.2 文昌文曲：为人多学多能

- 原文（断句）：

  文昌、文曲。为人多学多能，左辅右弼，秉性克守克厚，假如辰戌、巳亥、卯酉安命，遇昌曲二星是也。

- 规范化释义（primary_lang_explained）：

  文昌文曲为人多学多能，左辅右弼秉性克守克厚。如辰戌巳亥卯酉安命遇昌曲二星是也。

- 核心要点：**昌曲**守命多学多能，**辅弼**守命克守克厚。

##### 1.5.3 七杀朝斗，爵禄荣昌

- 原文（断句）：

  七杀朝斗，爵禄荣昌。假如寅、申、子、午四宫安身命，七杀值之是也。亦要左右、魁钺、昌曲坐照拱合，一生富贵荣华，或遇吉限尤美。若加杀不是。

  紫府同宫，终身福厚。如寅、申二宫安命，值紫微、天府同宫，三方有左右魁钺拱照，必主富贵，终身福厚。甲生人化吉最美。

  紫微居午，无杀凑，位至公卿；假如甲丁己生人，安命午宫值之，入格生大贵，其余官亦主富足，或小贵，若加杀不是。

  天府临戌，有星扶，腰金衣紫。假如甲己生人，安命戌宫值之，依此断，加杀不是。要有魁钺左右禄权科，主大富贵。如无此吉星，亦平常。

  科权禄拱，名誉昭彰；此为三化星。如身命坐守，一化财帛、官禄宫，二化来合，是三合守照，谓之科权禄拱是也。加左右，位至三公。

  武曲庙垣，威名赫奕。假如辰、戌二宫安命值之上格，丑未安命次之，宜见权、禄、左右、昌、曲诸吉星，则依此断。

- 规范化释义（primary_lang_explained）：

  出世荣华为权禄守财福之位。化权化禄守财帛福德二宫入庙吉多，定主荣华，身命值之亦然。

  文昌文曲为人多学多能，左辅右弼秉性克守克厚。如辰戌巳亥卯酉安命遇昌曲二星是也。

  七杀朝斗爵禄荣昌。如寅申子午四宫安身命七杀值之是也。亦要左右魁钺昌曲坐照拱合，一生富贵荣华，或遇吉限尤美。若加杀不是。

  紫府同宫终身福厚。如寅申二宫安命值紫微天府同宫，三方有左右魁钺拱照必主富贵终身福厚。甲生人化吉最美。

  紫微居午无杀凑位至公卿。如甲丁己生人安命午宫值之入格生大贵，其余官亦主富足或小贵，若加杀不是。

  天府临戌有星扶腰金衣紫。如甲己生人安命戌宫值之依此断，加杀不是。要有魁钺左右禄权科主大富贵，如无此吉星亦平常。

  科权禄拱名誉昭彰，此为三化星。如身命坐守，一化财帛官禄宫，二化来合，是三合守照谓之科权禄拱是也。加左右位至三公。

  武曲庙垣威名赫奕。如辰戌二宫安命值之为上格，丑未安命次之，宜见权禄左右昌曲诸吉星则依此断。

- 核心要点：
  - **化权化禄**守财帛、福德二宫，入庙吉多，主出世荣华。
  - **文昌文曲**守命多学多能，**辅弼**守命克守克厚。
  - **七杀朝斗**：七杀在寅申子午四宫入庙。
  - **需吉拱照**：左右魁钺昌曲拱照，方主富贵。
  - **加杀破格**：若加凶杀则格局破败。
  - **紫府寅申同宫**，三方吉拱，主富贵福厚，**甲生人**尤吉。
  - **紫微午宫**入庙，无杀凑合，**甲丁己生人**位至公卿。
  - **天府戌宫**，有吉星扶持，**甲己生人**腰金衣紫。
  - **化科化权化禄**三化星拱照身命，主名誉昭彰，加辅弼位至三公。
  - **武曲辰戌**入庙为上格，丑未次之，见吉星则威名赫奕。

- 完整对等诠释（secondary_lang_full）：

  This series of prosperity patterns outlines the structural requirements for achieving the highest tiers of wealth and nobility. When Transformation of Authority and Transformation of Salary guard the Wealth and Fortune palaces in dignified positions with many benefics, one is destined for worldly glory. Wenchang and Wenqu in the Life Palace indicate a person of extensive learning and versatile talents, while Zuo Fu and You Bi in the same position reveal a steady and reliable character. The "Qisha Facing Dipper" pattern requires the Seventh Killing star to occupy one of the four cardinal palaces (Yin, Shen, Zi, Wu) in temple dignity, supported by Zuo-You, Kui-Yue, and Chang-Qu through aspect or conjunction—only then does it promise lifelong honor and prosperity. Ziwei and Tianfu sharing the same palace in Yin or Shen, with three-directional benefic support, brings enduring fortune, especially auspicious for those born in Jia year. Ziwei alone in Wu palace without malefic intrusion can elevate Jia, Ding, or Ji natives to ministerial rank. Tianfu in Xu palace, supported by Kui-Yue, Zuo-You, and Lu-Quan-Ke transformations, grants the insignia of high office. The Three Transformations (Ke-Quan-Lu) flanking the Life Palace illuminate one's reputation, and with Zuo-You assistance, can reach the Three Ducal ranks. Wuqu in Chen or Xu temples with benefic support produces resounding military fame. Throughout these patterns, the key principle remains: principal stars must occupy designated positions, receive benefic support from three directions, and match appropriate day-stem natives—any malefic intrusion breaks the pattern.

- 叙事素材（narrative_snippets）：

  - **化权化禄**："化权化禄守财帛福德二宫，入庙吉多，主出世荣华"，三化星守关键宫位的富贵格局。
  - **七杀朝斗**："七杀寅申子午四宫入庙，七杀朝斗，爵禄荣昌"，七杀入庙加吉拱的贵格。
  - **紫府同宫**："紫府寅申同宫，三方吉拱，主富贵福厚"，帝星库星同宫的上等格局。
  - **三化拱命**："科权禄拱名誉昭彰，加左右位至三公"，三化星拱照身命的极贵格局。
  - **武曲威名**："武曲庙垣威名赫奕，辰戌安命值之为上格"，武曲入庙的军武富贵格。
  - **现代应用**：本批口诀可作为判断高格局的"模式库"——对照主星位置、三方配置、日干匹配三要素。

  **L2 叙事素材层（规范格式）**：

  - `[ns_zwds_j2_037]` `[trigger: 七杀朝斗格]` `[factor_trigger: geju_qishachaodou]` `[role: 条件分支]` 七杀朝斗格为七杀在寅申子午四宫入庙的贵格。 → 《骨髓赋》"七杀朝斗，爵禄荣昌"
  - `[ns_zwds_j2_038]` `[trigger: 紫府同宫格]` `[factor_trigger: geju_zifutonggong]` `[role: 条件分支]` 紫府同宫格为紫微天府同在寅申宫的上等格局。 → 《骨髓赋》"紫府同宫，终身福厚"
  - `[ns_zwds_j2_039]` `[trigger: 紫微居午格]` `[factor_trigger: geju_ziweijuwu]` `[role: 条件分支]` 紫微居午格为紫微在午宫无杀凑的贵格。 → 《骨髓赋》"紫微居午，位至公卿"
  - `[ns_zwds_j2_040]` `[trigger: 天府临戌格]` `[factor_trigger: geju_tianfulinxu]` `[role: 条件分支]` 天府临戌格为天府在戌宫有吉星扶持的贵格。 → 《骨髓赋》"天府临戌，腰金衣紫"
  - `[ns_zwds_j2_041]` `[trigger: 科权禄拱格]` `[factor_trigger: geju_kequanlugong]` `[role: 条件分支]` 科权禄拱格为三化星拱照身命的极贵格局。 → 《骨髓赋》"科权禄拱，名誉昭彰"
  - `[ns_zwds_j2_042]` `[trigger: 武曲庙垣格]` `[factor_trigger: geju_wuqumiaoyuan]` `[role: 条件分支]` 武曲庙垣格为武曲在辰戌入庙的武职贵格。 → 《骨髓赋》"武曲庙垣，威名赫奕"
  - `[ns_zwds_j2_043]` `[trigger: 四化禄]` `[factor_trigger: sihua_hualu]` `[role: 主干]` 四化禄为年干所化之禄星，主财禄增益。 → 《骨髓赋》"化禄"
  - `[ns_zwds_j2_044]` `[trigger: 出世荣华结果]` `[factor_trigger: result_chushi_ronghua]` `[role: 结果]` 出世荣华为命格高贵、一生富贵荣华的结果。 → 《骨髓赋》"出世荣华"
  - `[ns_zwds_j2_045]` `[trigger: 爵禄荣昌结果]` `[factor_trigger: result_juelu_rongchang]` `[role: 结果]` 爵禄荣昌为官爵财禄俱全的富贵结果。 → 《骨髓赋》"爵禄荣昌"
  - `[ns_zwds_j2_046]` `[trigger: 位至公卿结果]` `[factor_trigger: result_weizhi_gongqing]` `[role: 结果]` 位至公卿为官至极品、位列公卿的结果。 → 《骨髓赋》"位至公卿"
  - `[ns_zwds_j2_047]` `[trigger: 腰金衣紫结果]` `[factor_trigger: result_yaojin_yizi]` `[role: 结果]` 腰金衣紫为富贵显达、身着官服的结果。 → 《骨髓赋》"腰金衣紫"
  - `[ns_zwds_j2_048]` `[trigger: 威名赫奕结果]` `[factor_trigger: result_weiming_heyi]` `[role: 结果]` 威名赫奕为武职显赫、声名远播的结果。 → 《骨髓赋》"威名赫奕"
  - `[ns_zwds_j2_049]` `[trigger: 终身福厚结果]` `[factor_trigger: result_zhongshen_fuhou]` `[role: 结果]` 终身福厚为一生福禄丰厚的结果。 → 《骨髓赋》"终身福厚"
  - `[ns_zwds_j2_050]` `[trigger: 社会角色]` `[factor_trigger: shehui_juese]` `[role: 结果]` 社会角色为命主在社会中的身份地位。 → 《骨髓赋》
  - `[ns_zwds_j2_051]` `[trigger: 职业命格]` `[factor_trigger: zhiye_mingge]` `[role: 主干]` 职业命格为命盘所显示的职业倾向。 → 《骨髓赋》"""
    normalized_text_zh: str = """"""
    subject: str = "5 富贵格局系列"
    factor_refs: list = ['combo_qishachaodou', 'combo_zifutonggong', 'term_sanhua', 'result_yaojinyizi', 'result_chushironghua', 'trait_duoxueduoneng', 'source_ref', 'rel_fugui_001', 'fugui_geju_type', 'rel_fugui_002', 'jixing_peihe', 'rel_fugui_003', 'geju_poge', 'evi_fugui_001', 'combo_qishachaodou', 'rule_qishachaodou', 'evi_fugui_002', 'combo_zifutonggong', 'rule_zifutonggong', 'evi_fugui_003', 'term_sanhua', 'rule_sanhuagong', 'concept_noble_pattern', 'concept_support_system']
    
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
        l1_anchor="zw_v1.0.0_5_富贵格局系列_001_L1",
    )
    version: str = "1.0.0"
