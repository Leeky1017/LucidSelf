"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.778515
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
    semantic_id="zw_v1.0.0_女命骨髓赋注解_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 女命骨髓赋注解(SemanticEntry):
    """
    #### 2.1 总论：女命格局特点

- 原文（断句）：

  府相之星女命缠，必当子贵与夫贤。廉贞清白能相守，更有天同理亦然。端正紫微太阳星，早遇贤夫性可凭。太阳寅到午，遇吉终是福。左辅天魁为福。...
    """
    
    original_text: str = """#### 2.1 总论：女命格局特点

- 原文（断句）：

  府相之星女命缠，必当子贵与夫贤。廉贞清白能相守，更有天同理亦然。端正紫微太阳星，早遇贤夫性可凭。太阳寅到午，遇吉终是福。左辅天魁为福。

- 分字分词释义：

  - **府相之星**：天府与天相二星。
  - **女命缠**：女命命宫有此二星守护。
  - **子贵夫贤**：子女显贵，丈夫贤德。
  - **廉贞清白**：廉贞星主清白贞洁。
  - **能相守**：能保持贞节、守住婚姻。
  - **天同理亦然**：天同星亦主福德和睦。
  - **端正紫微太阳**：紫微太阳主端庄正派。
  - **早遇贤夫**：年轻时即能嫁得贤德丈夫。
  - **性可凭**：性情可靠值得信赖。
  - **太阳寅到午**：太阳从寅宫到午宫逐渐升起得辉。
  - **遇吉终是福**：遇到吉星最终主福。
  - **左辅天魁为福**：左辅天魁守命主贵人相助为福。

- 规范化释义（primary_lang_explained）：

  府相之星女命缠必当子贵与夫贤。廉贞清白能相守，更有天同理亦然。端正紫微太阳星早遇贤夫性可凭。太阳寅到午遇吉终是福。左辅天魁为福。

- 核心要点：

  1. **女命吉星**：府相、廉贞清白、天同、紫微太阳、左辅天魁
  2. **主旺夫益子**：子贵夫贤、封诰命妇
  3. **入庙为福**：太阳寅到午遇吉终是福
  4. **生人配合**：甲庚丙丁辛等生人各有吉格

#### 2.2 府相守命：子贵夫贤

- 原文（断句）：

  府相之星女命缠，必当子贵与夫贤，午宫安命二星坐守，甲生人合格；子宫安命二星坐守，巳生人合格；申宫安命二星坐守，庚生人合格，必作命妇荣膺封诰是也。

- 规范化释义（primary_lang_explained）：

  府相之星女命缠必当子贵与夫贤。午宫安命二星坐守甲生人合格，子宫安命二星坐守巳生人合格，申宫安命二星坐守庚生人合格，必作命妇荣膺封诰是也。

- 核心要点：
  - 天府天相女命守照，主子贵夫贤
  - 午宫甲生人、子宫巳生人、申宫庚生人为合格
  - 必作命妇，荣膺封诰

---

#### 2.3 廉贞清白：能相守

- 原文（断句）：

  廉贞清白能相守，此星未宫坐命，甲生人合格；申宫坐命，癸生人合格；寅宫坐命，巳生人合格，俱为上格看。

- 规范化释义（primary_lang_explained）：

  廉贞清白能相守。此星未宫坐命甲生人合格，申宫坐命癸生人合格，寅宫坐命巳生人合格，俱为上格看。

- 核心要点：
  - 廉贞女命主清白能守
  - 未宫甲生人、申宫癸生人、寅宫巳生人为上格
  - 强调贞洁守节

---

#### 2.4 天同理亦然

- 原文（断句）：

  更有天同理亦然。此星寅宫坐命，甲生人合格；卯宫坐命，甲生人合格；戌宫坐命，丁生人合格；巳宫坐命，丙、辛生人合格；亥宫坐命，丙、午生人合格，俱主富贵。

- 规范化释义（primary_lang_explained）：

  更有天同理亦然。此星寅宫坐命甲生人合格，卯宫坐命甲生人合格，戌宫坐命丁生人合格，巳宫坐命丙辛生人合格，亥宫坐命丙午生人合格，俱主富贵。

- 核心要点：
  - 天同女命主福德安乐
  - 多个宫位与生人组合
  - 俱主富贵

---

#### 2.5 紫微太阳：早遇贤夫

- 原文（断句）：

  端正紫微太阳星，早遇贤夫性可凭。子巳亥三宫安命二星坐守，主富贵。

- 规范化释义（primary_lang_explained）：

  端正紫微太阳星早遇贤夫性可凭。子巳亥三宫安命二星坐守主富贵。

- 核心要点：
  - 紫微太阳主端正贤德
  - 早遇贤夫，性情可凭
  - 子巳亥三宫主富贵

---

#### 2.6 太阳寅到午：遇吉终是福

- 原文（断句）：

  太阳寅到午，遇吉终是福。太阳午宫安命，定主富贵，陷地平常。

- 规范化释义（primary_lang_explained）：

  太阳寅到午遇吉终是福。太阳午宫安命定主富贵，陷地平常。

- 核心要点：
  - 太阳寅卯辰巳午为得辉
  - 午宫最佳，定主富贵
  - 陷地平常

---

#### 2.7 左辅天魁为福

- 原文（断句）：

  左辅天魁为福。

- 规范化释义（primary_lang_explained）：
  左辅天魁为福。

- 核心要点：
  - 左辅天魁主贵人相助
  - 女命遇之为福

- 叙事素材（narrative_snippets）：

  - **女命总则**："女命首看夫星子息"，女命以夫妻宫、子女宫为首要判断。
  - **天同守命**："天同戌宫守命，夫妻常和"，天同入庙主婚姻和睦。
  - **文曲淫奔**："文曲守命多淫"，文曲入陷地女命主风流。
  - **太阳得辉**："太阳寅到午遇吉终是福"，太阳入庙女命主富贵。
  - **贵人相助**："左辅天魁为福"，辅魁入命主贵人相助。
  - **现代应用**：女命判断可参考夫妻宫子女宫的吉凶，太阳庙旺、辅魁入命皆为吉象。

- 完整对等诠释（secondary_lang_full）：

  The Women's Destiny Bone-Marrow Verse sets out specialised criteria for reading female charts in Ziwei Doushu. It judges fortune less by the woman's own career and more by her husband's status, her children's prospects and her moral standing. The question is not only whether she is comfortable, but whether she is recognised as a worthy wife and mother within the family and social order. Key auspicious patterns include those where Tianfu and Tianxiang guard the Life palace in suitable locations for particular birth stems, promising noble sons and a virtuous, capable husband and corresponding in traditional society to ranked consort honours. Lianzhen in clean, dignified positions represents chastity, integrity and the ability to keep faith under pressure. Tiantong in well supported combinations brings blessing, ease and a gentle temperament. Ziwei together with the Sun in prominent palaces gives a dignified, upright character that attracts a good match early in life. When the Sun itself stands in bright positions such as Yin, Mao, Chen, Si or Wu and is supported by benefics, it signifies visible honour and a life that feels warm and meaningful; in weak positions the same Sun produces only ordinary results. Auxiliary benefics such as Zuofu and Tiankui act as protective patrons, indicating elders and networks willing to help the woman at turning points. Behind these techniques stands a Confucian value system that treats the husband as a main channel of honour, the children as a main channel of blessing and personal virtue as the root of both. The verse therefore pays close attention to triple coordination between palace, birth stem and star dignity, and it is highly sensitive to whether malefics disturb the Life, Spouse and Children houses. Compared with male charts that emphasise personal office and achievement, this framework reads female charts through relational positioning: the quality of marriage, offspring and family reputation, and whether the chart can support a life of protection rather than one of exposure and vulnerability."""
    normalized_text_zh: str = """"""
    subject: str = "女命骨髓赋注解"
    factor_refs: list = ['combo_fuxiang', 'result_ziguifuxian', 'rank_fenggao', 'trait_qingbai', 'trait_wangfuyizi', 'trait_duanzhengxiande', 'source_ref', 'rel_nvming_001', 'nvming_tixi', 'rel_nvming_002', 'sanchong_peihe', 'rel_nvming_003', 'dexing_pinggu', 'evi_nvming_001', 'combo_fuxiang', 'rule_fuxiang_nvming', 'evi_nvming_002', 'trait_qingbai', 'rule_lianzhen_qingbai', 'concept_female_fortune', 'concept_family_blessing', 'concept_virtue_foundation']
    
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
        l1_anchor="zw_v1.0.0_女命骨髓赋注解_001_L1",
    )
    version: str = "1.0.0"
