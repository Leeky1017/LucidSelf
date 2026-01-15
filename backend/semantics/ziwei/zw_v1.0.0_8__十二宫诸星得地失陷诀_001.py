"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.778568
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
    semantic_id="zw_v1.0.0_8__十二宫诸星得地失陷诀_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 8十二宫诸星得地失陷诀(SemanticEntry):
    """
    - 分字分词释义：

  - **十二宫诸星得地**：十二个宫位各自适合的星曜配置。
  - **失陷**：星曜落入不利之宫位，力量减弱。
  - **得地合格**：星曜落入适宜位置，形成吉格。
  ...
    """
    
    original_text: str = """- 分字分词释义：

  - **十二宫诸星得地**：十二个宫位各自适合的星曜配置。
  - **失陷**：星曜落入不利之宫位，力量减弱。
  - **得地合格**：星曜落入适宜位置，形成吉格。
  - **子宫贪狼杀阴星**：子宫安命，贪狼七杀太阴星守照。
  - **机梁相拱**：天机天梁从三方拱照命宫。
  - **福兴隆**：福德兴旺、运势昌隆。
  - **日月朝**：太阳太阴从对宫或三方朝照命宫。
  - **正坐**：星曜在本宫坐守。
  - **对照**：星曜在对宫照命。
  - **百事通**：诸事顺遂、无所不通。
  - **男官女封**：男命官运亨通，女命受封诰命。

#### 7.1 十二宫得地合格诀

##### 子宫安命（得地）

- 原文（断句）：子宫贪狼杀阴星，机梁相拱福兴隆。庚辛乙癸生人美，一生富贵足盈丰。

- 规范化释义（primary_lang_explained）：

  子宫贪狼杀阴星机梁相拱福兴隆。庚辛乙癸生人美一生富贵足盈丰。

- 核心要点：贪狼七杀太阴+机梁拱，庚辛乙癸生人吉

##### 丑宫安命（得地）

- 原文（断句）：丑宫立命日月朝，丙戊辛人福禄饶。正坐平常中局论，对照富贵祸皆消。

- 规范化释义（primary_lang_explained）：

  丑宫立命日月朝丙戊辛人福禄饶。正坐平常中局论对照富贵祸皆消。

- 核心要点：日月朝照，丙戊辛生人福禄，对照优于正坐

##### 寅宫安命（得地）

- 原文（断句）：寅宫巨日足丰隆，七杀天梁百事通。甲巳庚人皆为吉，男子为官女受封。

- 规范化释义（primary_lang_explained）：

  寅宫巨日足丰隆七杀天梁百事通。甲巳庚人皆为吉男子为官女受封。

- 核心要点：巨门太阳+七杀天梁，甲巳庚生人男官女封

##### 卯宫安命（得地）

- 原文（断句）：卯宫机巨武曲逢。辛乙生人福气隆。男子为官糜廏禄，女人享福受褒封。

- 规范化释义（primary_lang_explained）：

  卯宫机巨武曲逢辛乙生人福气隆。男子为官糜廏禄女人享福受褒封。

- 核心要点：天机巨门武曲，辛乙生人男官女封

##### 辰宫安命（得地）

- 原文（断句）：辰位机梁坐命宫，天府戌地最盈丰。腰金衣紫真荣显，富华荣贵直到终。

- 规范化释义（primary_lang_explained）：

  辰位机梁坐命宫天府戌地最盈丰。腰金衣紫真荣显富华荣贵直到终。

- 核心要点：天机天梁坐命，天府戌宫对照，腰金衣紫

##### 巳宫安命（得地）

- 原文（断句）：巳位天机天相临，紫府朝垣福更深。戊辛壬丙皆为贵，一生顺遂少灾侵。

- 规范化释义（primary_lang_explained）：

  巳位天机天相临紫府朝垣福更深。戊辛壬丙皆为贵一生顺遂少灾侵。

- 核心要点：天机天相+紫府朝垣，戊辛壬丙生人顺遂

##### 午宫安命（得地）

- 原文（断句）：午宫紫府太阳同，机梁破杀喜相逢。甲丁巳癸生人福，一世风光廪禄丰。

- 规范化释义（primary_lang_explained）：

  午宫紫府太阳同机梁破杀喜相逢。甲丁巳癸生人福一世风光廪禄丰。

- 核心要点：紫府太阳+机梁破杀，甲丁巳癸生人风光

##### 未宫安命（得地）

- 原文（断句）：未宫紫武廉贞同，日月巨门喜相逢。女人值此全福寿，男子逢之位三公。

- 规范化释义（primary_lang_explained）：

  未宫紫武廉贞同日月巨门喜相逢。女人值此全福寿男子逢之位三公。

- 核心要点：紫微武曲廉贞+日月巨门，女全福寿男位三公

##### 申宫安命（得地）

- 原文（断句）：申宫紫帝贞梁同，武曲巨门喜相逢。甲庚癸人如得遇，一生富贵逞英雄。

- 规范化释义（primary_lang_explained）：

  申宫紫帝贞梁同武曲巨门喜相逢。甲庚癸人如得遇一生富贵逞英雄。

- 核心要点：紫微廉贞天梁+武曲巨门，甲庚癸生人英雄

##### 酉宫安命（得地）

- 原文（断句）：酉宫最喜太阴逢，巨日又逢当面冲。辛乙生人为贵格，一生福禄永亨通。

- 规范化释义（primary_lang_explained）：

  酉宫最喜太阴逢巨日又逢当面冲。辛乙生人为贵格一生福禄永亨通。

- 核心要点：太阴+巨日对冲，辛乙生人贵格

##### 戌宫安命（得地）

- 原文（断句）：戌宫紫破对冲辰，富而不贵有虚名，更加吉曜多权禄，只利开张贸易人。

- 规范化释义（primary_lang_explained）：

  戌宫紫破对冲辰富而不贵有虚名，更加吉曜多权禄只利开张贸易人。

- 核心要点：紫微破军对冲辰，富而不贵，利贸易

##### 亥宫安命（得地）

- 原文（断句）：亥宫巨喜太阴逢，若人值此福禄隆。男命逢之皆称意，富贵荣华直到终。

- 规范化释义（primary_lang_explained）：

  亥宫巨喜太阴逢若人值此福禄隆。男命逢之皆称意富贵荣华直到终。

- 核心要点：巨门太阴，男命称意富贵荣华

- 完整对等诠释（secondary_lang_full）：

  The twelve-palace auspicious-positioning formula sets out which star combinations give the Life palace solid ground and clear advantages in each of the twelve locations. It does not merely say that one place is good and another bad, but links each position with specific constellations, birth stems and types of success, so that one can choose Life placement with a concrete standard.
  When the Life palace is in Zi, Tanlang, Qisha and Taiyin guarding Life and supported at a distance by Tianji and Tianliang make fortune rise and flourish, especially for Geng, Xin, Yi and Gui natives who then enjoy abundant wealth and rank. In Chou, the Sun and Moon shining toward the Life palace from opposing positions bring rich blessings to Bing, Wu and Xin natives; in this case an opposite-illumination configuration is even better than having the luminaries sit directly on Life. In Yin, combinations of Jumen and the Sun with Qisha and Tianliang enable the native to handle many matters and are especially favorable for Jia, Si and Geng births, giving men office rank and women noble titles. In Mao, Tianji, Jumen and Wuqu together also bring civil and military advancement for Xin and Yi natives. In Chen, Tianji and Tianliang sitting on Life while Tianfu looks across from Xu is compared to wearing a golden belt and purple robe, a symbol of first-class official status. In Si, Tianji and Tianxiang together with Ziwei and Tianfu facing the court give smooth progress and few disasters for Wu, Xin, Ren and Bing births. In Wu, elaborate groupings of Ziwei, Tianfu, the Sun, Tianji, Tianliang, Pojun and Qisha bring glory and rich salaries for Jia, Ding, Si and Gui natives.
  In Wei, Ziwei, Wuqu and Lianzhen joined by the Sun, Moon and Jumen promise complete blessings and long life for women and the rank of the Three Dukes for men. In Shen, combinations of Ziwei, Lianzhen and Tianliang with Wuqu and Jumen support heroic achievement for Jia, Geng and Gui natives. In You, Taiyin together with Jumen and the Sun standing face to face across from the Life palace form a powerful direct opposition, giving Xin and Yi natives a noble pattern with long-lasting success. In Xu, Ziwei and Pojun opposing from Chen bring wealth without nobility and point to trade and commerce rather than official office. In Hai, Jumen and Taiyin together make male natives particularly pleased with their lot, enjoying wealth, honor and lasting prosperity.
  Across all twelve positions, the method is to judge whether the Life palace receives dignified benefic stars in appropriate combinations, whether three-directional convergences form, and whether the birth heavenly stem matches the configuration. Only when these three layers align does a placement count as truly auspicious ground for the Life palace.

- 叙事素材（narrative_snippets）：

  - **子宫发福**：命在子宫而贪狼七杀太阴得地、机梁遥拱时，庚辛乙癸生人多见财禄丰足、家门兴隆。
  - **日月对照**：丑宫立命，日月分守对宫照命，看似不及同宫，实则“远光照命”，多为靠外缘与贵人而起的福格。
  - **机梁紫府朝垣**：辰巳等宫天机天梁、紫府朝垣成局，如“腰金衣紫”，仕途稳步累进，少有大起大落。
  - **男女殊途同荣**：不少宫位格局下，男命偏向官职名位，女命则偏向福寿封赠，同一富格在性别上呈现不同舞台。
  - **得地三条件**：星在庙旺、三方吉拱、生年相合三者俱足，方是真正“得地合格”，否则只是外形华美而内里空虚。

- L2-术语对齐（Term Glossary·7.1）：

  | 中文术语 | 英文术语 | 中文定义 | 英文定义 |
  |---------|---------|---------|---------|
  | 得地 | Auspicious Positioning | 星曜在特定宫位入庙旺的吉利配置 | Benefic star configuration achieving temple-wang in specific palaces |
  | 失陷 | Debilitation Positioning | 星曜在特定宫位落陷的凶险配置 | Malefic star configuration falling into debilitation in specific palaces |
  | 对照 | Opposite Illumination | 迁移宫星曜对宫照命 | Stars in Migration Palace illuminating Life from opposite position |
  | 正坐 | Direct Positioning | 星曜直接坐守命宫 | Stars directly guarding Life Palace |
  | 三方会照 | Three-Directional Convergence | 命宫三方四正的星曜会合照应 | Convergence of stars from three directions and four cardinals |
  | 腰金衣紫 | Waist-Gold Robe-Purple | 高官显贵的象征 | Symbol of high official nobility |

---

#### 8.1 十二宫失陷破格诀

##### 子丑宫安命（失陷）

- 原文（断句）：子火天机丑巨铃，此星落陷果为真。纵然化吉不为美，任他富贵不清宁。

- 规范化释义（primary_lang_explained）：

  子火天机丑巨铃此星落陷果为真。纵然化吉不为美任他富贵不清宁。

- 核心要点：子火（火星）天机、丑巨门铃星，化吉亦不美

##### 寅宫安命（失陷）

- 原文（断句）：寅上机昌曲月逢，虽然吉拱不昌隆。男为伴仆女娼婢，若非夭折即贫穷。

- 规范化释义（primary_lang_explained）：

  寅上机昌曲月逢虽然吉拱不昌隆。男为伴仆女娼婢若非夭折即贫穷。

- 核心要点：天机昌曲太阴，男仆女婢或贫夭

##### 卯辰宫安命（失陷）

- 原文（断句）：卯上太阴擎羊逢，辰宫巨宿紫微同。纵然化吉非全美，若非加杀到头凶。

- 规范化释义（primary_lang_explained）：

  卯上太阴擎羊逢辰宫巨宿紫微同。纵然化吉非全美若非加杀到头凶。

- 核心要点：卯太阴擎羊、辰巨门紫微，化吉非全美

##### 巳宫安命（失陷）

- 原文（断句）：巳宫武月天梁巨，贪宿廉贞共到蛇。三方吉曜皆不贵，下贱贫穷度岁华。

- 规范化释义（primary_lang_explained）：

  巳宫武月天梁巨贪宿廉贞共到蛇。三方吉曜皆不贵下贱贫穷度岁华。

- 核心要点：武曲太阴天梁巨门贪狼廉贞聚巳，下贱贫穷

##### 午宫安命（失陷）

- 原文（断句）：午宫贪巨月昌从，羊刃三合最嫌冲。虽然化吉居仕路，横破横成到老穷。

- 规范化释义（primary_lang_explained）：

  午宫贪巨月昌从羊刃三合最嫌冲。虽然化吉居仕路横破横成到老穷。

- 核心要点：贪巨月昌+羊刃，横破横成到老穷

##### 未宫安命（失陷）

- 原文（断句）：未宫巨宿太阳嫌，纵少灾危有克伤。劳碌奔波官事至，随缘下贱度时光。

- 规范化释义（primary_lang_explained）：

  未宫巨宿太阳嫌纵少灾危有克伤。劳碌奔波官事至随缘下贱度时光。

- 核心要点：巨门太阳未宫，劳碌奔波官事

##### 申酉宫安命（失陷）

- 原文（断句）：申宫机巨为破格，男人浪荡女人贫。二宫若然桃花见，男女逢之总不荣。

- 规范化释义（primary_lang_explained）：

  申宫机巨为破格男人浪荡女人贫。二宫若然桃花见男女逢之总不荣。

- 核心要点：天机巨门申酉，男浪荡女贫

##### 戌宫安命（失陷）

- 原文（断句）：戌上紫破若相逢，天同太阳皆主凶。男女孤寒更夭折，随缘勤苦免贫穷。

- 规范化释义（primary_lang_explained）：

  戌上紫破若相逢天同太阳皆主凶。男女孤寒更夭折随缘勤苦免贫穷。

- 核心要点：紫微破军+天同太阳戌宫，孤寒夭折

- 完整对等诠释（secondary_lang_full）：

  The twelve-palace debilitation and breaking standards warn of placements where important stars fall into weakness or harmful configurations when the Life palace is in certain locations. These rules explain why some charts remain troubled and lowly even when benefic transformations appear on the surface: the underlying star-palace relationship is fundamentally misaligned.
  When the Life palace is in Zi or Chou, Huoxing together with Tianji in Zi and Jumen with Lingxing in Chou mark true debilitation; even if some stars transform to auspicious, wealth and rank do not bring peace. In Yin, Tianji, Wenchang, Wenqu and Taiyin appear to be benefics, but when gathered in the wrong way they bring only mixed results: men are tied to servants or lowly work, women often fall into entertainment or servitude, and some charts show either early death or persistent poverty. In Mao and Chen, Taiyin with Qingyang in Mao and Jumen with Ziwei in Chen can look auspicious by transformation yet in fact are incomplete; once further malefics are added the configuration turns decisively adverse. In Si, a crowd of stars such as Wuqu, Taiyin, Tianliang, Jumen, Tanlang and Lianzhen gathering there may seem impressive, but as a group they still do not form a true noble pattern and easily indicate a life of low status and poverty.
  In Wu, Tanlang, Jumen, Taiyin and Wenchang together with Qingyang and other sharp stars form a pattern of repeated windfalls and sudden collapses: gains arrive abruptly yet are overturned just as abruptly, so that in the end poverty remains. In Wei, Jumen and the Sun often show toil, lawsuits and hard work, with a life spent drifting at the lower edges of society. In Shen and You, combinations of Tianji and Jumen can break standard patterns, making men dissolute and women impoverished; with additional peach-blossom indications, neither gender gains lasting honor. In Xu, Ziwei, Pojun, Tiantong and the Sun together all tend toward misfortune: loneliness, cold hardship and sometimes early death, with only unremitting effort preventing utter destitution.
  The central lesson of these debilitation rules is that when stars stand in the wrong places, or in the wrong combinations, their intrinsic weakness overrides any later auspicious transformation. Real judgment must therefore begin by checking whether the Life palace and key stars are on firm ground or in fallen, trapped positions; only then can benefic influences be trusted to bear fruit.

- 叙事素材（narrative_snippets）：

  - **化吉不救失陷**：子丑宫火星、天机、巨门、铃星等落陷，即便偶有化吉，仍难改“富贵不清宁”的基调。
  - **表面吉拱，里里破格**：寅宫机昌曲月聚、卯辰太阴紫微表面文气十足，却因位置不当，反主男仆女婢、贫困夭折。
  - **人多星杂不成局**：巳宫武月梁巨贪廉齐聚，看似星多气旺，实则三方吉曜皆难成贵，终归下贱贫穷度日。
  - **横破横成的午宫**：午宫贪巨月昌加羊刃，往往是一夜暴富、一夜破尽的命，临终仍觉“到老穷”。
  - **陷地难逃终局**：未宫巨日、戌宫紫破、申酉机巨等，哪怕一时得利，终因陷地失辉而走向劳苦、孤寒或早夭。"""
    normalized_text_zh: str = """"""
    subject: str = "8. 十二宫诸星得地失陷诀"
    factor_refs: list = ['state_shixian', 'state_poge', 'principle_huajibumei', 'state_hengpohengcheng', 'state_guhanyaozhe', 'state_xiajianpinqiong', 'source_ref', 'rel_12gong_001', 'gongwei_peizhi', 'rel_12gong_002', 'shengnian_peihe', 'rel_12gong_003', 'shixian_poge', 'evi_12gong_001', 'gongwei_peizhi', 'rule_zigong_dedi', 'evi_12gong_002', 'state_shixian', 'rule_wangdi_xiandi', 'concept_palace_config', 'concept_dignity', 'concept_year_match']
    
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
        l1_anchor="zw_v1.0.0_8__十二宫诸星得地失陷诀_001_L1",
    )
    version: str = "1.0.0"
