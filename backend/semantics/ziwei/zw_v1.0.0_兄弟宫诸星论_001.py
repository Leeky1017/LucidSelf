"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.636621
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
    semantic_id="zw_v1.0.0_兄弟宫诸星论_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 兄弟宫诸星论(SemanticEntry):
    """
    #### 原文（断句）：

兄弟宫诸星论。紫微在兄弟宫，有倚靠年长之兄。天府同，三人；天相同，三四人；破军同，亦有三人，或各胞生。加羊陀火铃空劫克害，有则欠和。天机在兄弟宫，庙旺有二人。与巨门同，一人...
    """
    
    original_text: str = """#### 原文（断句）：

兄弟宫诸星论。紫微在兄弟宫，有倚靠年长之兄。天府同，三人；天相同，三四人；破军同，亦有三人，或各胞生。加羊陀火铃空劫克害，有则欠和。天机在兄弟宫，庙旺有二人。与巨门同，一人；陷地相背不一心。天梁同，二人；太阴同，二三人。见羊陀火铃，虽有而克。太阳在兄弟宫，庙旺三人。与巨门同，无杀加，有三人；太阴同，五人。陷地不和欠力，加羊陀火铃空劫，更克减半。【以下各星详断从略】

#### 分字分词释义：

- **兄弟宫**：十二宫之一，专论兄弟姐妹之数量、和睦程度、助力大小。
- **倚靠年长之兄**：有年长兄长可依靠，兄弟中有助力者。
- **各胞生**：各自不同胞所生，指非同父同母兄弟、异母异父兄弟。
- **克害**：刑克伤害，兄弟间不睦或有夭折者。
- **相背不一心**：兄弟意见不合，各怀心思，难以齐心协力。
- **庙旺**：星曜处于庙旺之地，力量强盛，主吉象增强。
- **陷地**：星曜处于落陷之地，力量衰弱，主凶象加重。
- **羊陀火铃空劫**：六煞星，主减损、刑克、破耗。
- **昌曲左右**：文昌文曲左辅右弼四吉星，主增益、和睦。
- **斗君**：流年斗君，用以推断流年各宫运势。

#### 规范化释义（primary_lang_explained）：

兄弟宫专门论断命主兄弟姐妹的多寡、关系和睦与否、能否相互扶持。各星曜入此宫，吉凶不同：紫微主有可依靠的兄长；天机庙旺主二人，陷地则不和；太阳庙旺主三人，陷地减半且不睦；武曲主二人但不合；天同主四五人；天府主五人。若与其他主星同宫，人数会有变化。加吉星（昌曲左右）则增加人数且和睦；加煞星（羊陀火铃空劫）则减少人数并主刑克不和。流年斗君入兄弟宫，逢吉则该年兄弟和睦，逢凶则有争斗刑伤。

#### 完整对等诠释（secondary_lang_full·1兄弟宫）：

The Siblings Palace in Zi Wei Dou Shu describes not only how many brothers and sisters a native is likely to have, but also how close, dependable and harmonious those relationships will be. When benefic, dignified stars occupy this house, siblings tend to be numerous and supportive, with at least one elder sibling who can be leaned on. When harsher or weakened stars dominate, the picture shifts toward fewer siblings, emotional distance, rivalry or even literal loss through separation or death. Each major star carries its own pattern: imperial or treasury stars suggest many siblings and a stable clan network, while solitary, aggressive stars point to being an only child, half‑siblings from different parents, or siblings who pull in very different directions.

The story is further shaped by which stars share the same house and what kind of helpers or malefics join them. Auspicious assistants like Wen Chang, Wen Qu, Zuo Fu and You Bi can both increase the headcount and soften conflicts, turning siblings into allies, study partners or business partners. Malefics such as Yang Blade, Tuo Luo, Fire and Bell, or the emptiness pair, reduce the number of siblings or mark serious quarrels and injuries between them. The moving year marker, Doujun, highlights timing: when it passes through the Siblings Palace under good aspects, the year tends to bring mutual support, family celebrations and helpful contacts through brothers and sisters; when it meets heavy affliction there, the same year is more likely to bring disputes, financial strain or events that temporarily strain the sibling bond.

#### 核心要点：

1. **数量判断基准**：主星庙旺则兄弟多，陷弱则少；不同主星入守，基础人数不同。
2. **吉凶星调整**：吉星（昌曲左右）加会则增加人数、促进和睦；煞星（羊陀火铃空劫）会照则减少人数、主刑克不和。
3. **星曜同宫变化**：主星与其他主星同宫时，人数与和睦度会发生显著变化，需综合判断。
4. **庙陷影响关键**：同一主星在庙旺与陷弱时，结果差异极大，陷地加煞尤为凶险。
5. **流年斗君应用**：斗君过度入兄弟宫，逢吉星主该年兄弟和睦顺遂，逢凶杀主该年有争斗刑伤。

#### 详细解说：

兄弟宫在紫微斗数中属六亲宫之一，与父母宫、夫妻宫、子女宫并列，专门用来推断命主与兄弟姐妹的关系。本卷四以"诸星论"的方式，逐一列出十四主星、四化、辅佐诸星及六煞星入兄弟宫时的吉凶情况，提供了系统化的判断标准。

判断逻辑有三层：
1. **基础层**：看主星本身的庙旺陷弱。庙旺则兄弟数量多且有助力，陷弱则少且不和。例如紫微、天府这类帝星、库星，本身就主人数多；而七杀、破军这类孤克之星，则主孤单或刑克。
2. **组合层**：看主星是否与其他主星同宫。同宫组合会改变基础人数与和睦度。例如太阳太阴同宫，日月并明，主五六人；而武曲七杀同宫，金戈杀气重，只一人且不和。
3. **修正层**：看吉星煞星的加会情况。昌曲左右等吉星能增加人数、改善关系；羊陀火铃空劫等煞星则减少人数、制造刑克。

特别需要注意的是"各胞生"的概念，即非同父同母的兄弟姐妹。在古代社会，一夫多妻制下，同父异母的情况很常见，因此命书特别标注这类情况。现代应用时，可以理解为同父异母、继兄弟姐妹、堂兄弟姐妹等广义的兄弟姐妹关系。

流年斗君入兄弟宫的判断，是紫微斗数流年推运的重要内容。斗君每年行一宫，当行至兄弟宫时，该年与兄弟姐妹的互动最为频繁。若遇吉星吉化，则主该年兄弟间多有喜事、互相扶持；若遇凶星凶化，则主该年有争执、破财、甚至刑伤。

#### 校勘与字词辨析：

- 原文"无移三人"中"移"字，各版本写法不一。有作"异"者，意为"无异于三人"；有作"疑"者，意为"无疑三人"。本稿取"移"，理解为"虽有移动变化，仍约三人"之意。
- "垂违"一词，意为"相违背、不一致"。"垂"通"捶"，有背离之意。
- 原文中屡见"加"字，指加会、会照之意，非相加之算术义。
- "宜各人"当读为"宜各自独立、分居"之意，避免聚在一起产生冲突。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："紫府同宫守兄弟，手足五六皆和美，左右相扶事业成，一门荣贵传家业。"此句常用于说明紫微天府同守兄弟宫的吉象，象征兄弟众多、互相扶持、家门兴旺。
- **反面叙事**："羊陀火铃冲兄弟，纵有骨肉也分离，不是早夭便刑克，独自一人度岁时。"此句用于煞星重临兄弟宫的凶象警示，提示兄弟稀少或关系失和。
- **现代转化**：某企业家命主兄弟宫紫微天府加会左右，实际有兄弟五人，创业时兄弟联合出资，分工明确，公司上市后兄弟皆为股东，家族事业蒸蒸日上。此例验证"帝座库星主兄弟众多且互助"的论断。

**L2 叙事素材层（规范格式）**：

- `[ns_zwds_j4_001]` `[trigger: 兄弟宫论断]` `[factor_trigger: palace_xiongdi]` `[role: 主干]` 兄弟宫主论手足数量与关系和睦。 → 《紫微斗数全书·卷四》兄弟宫
- `[ns_zwds_j4_002]` `[trigger: 紫府守兄弟]` `[factor_trigger: star_ziwei AND star_tianfu AND palace_xiongdi]` `[role: 条件分支]` 紫府同守兄弟宫主手足五六人和美互助。 → 《卷四》"紫府同宫守兄弟"
- `[ns_zwds_j4_003]` `[trigger: 煞星冲兄弟]` `[factor_trigger: xiongxing_chong AND palace_xiongdi]` `[role: 条件分支]` 煞星冲兄弟宫主兄弟稀少或刑克。 → 《卷四》"羊陀火铃冲兄弟"
- `[ns_zwds_j4_004]` `[trigger: 兄弟数量]` `[factor_trigger: xiongdi_shuliang]` `[role: 结果]` 兄弟数量由兄弟宫星曜组合推断。 → 《卷四》兄弟宫
- `[ns_zwds_j4_005]` `[trigger: 兄弟和睦]` `[factor_trigger: xiongdi_hemu]` `[role: 结果]` 兄弟和睦由吉星守照判断。 → 《卷四》兄弟宫
- `[ns_zwds_j4_006]` `[trigger: 兄弟刑克]` `[factor_trigger: xiongdi_xingke]` `[role: 结果]` 兄弟刑克由煞星守照判断。 → 《卷四》兄弟宫
- `[ns_zwds_j4_007]` `[trigger: 兄弟助力]` `[factor_trigger: xiongdi_zhuli]` `[role: 结果]` 兄弟助力为兄弟间相互扶持的程度。 → 《卷四》兄弟宫
- `[ns_zwds_j4_008]` `[trigger: 合伙关系]` `[factor_trigger: hehuo_guanxi]` `[role: 主干]` 合伙关系可参照兄弟宫判断。 → 《卷四》兄弟宫现代应用
- `[ns_zwds_j4_036]` `[trigger: 白虎星]` `[factor_trigger: star_baihu]` `[role: 主干]` 白虎为凶星，主血光刑伤官非。 → 《卷四》
- `[ns_zwds_j4_037]` `[trigger: 官符星]` `[factor_trigger: star_guanfu]` `[role: 主干]` 官符为讼星，主官非诉讼是非。 → 《卷四》
- `[ns_zwds_j4_038]` `[trigger: 流月巡行概念]` `[factor_trigger: concept_liuyuexunxing]` `[role: 主干]` 流月巡行概念为流月运势的巡行规则。 → 《卷四》
- `[ns_zwds_j4_039]` `[trigger: 文明极盛结果]` `[factor_trigger: result_wenmingjishi]` `[role: 结果]` 文明极盛结果为文采声名极盛的判断。 → 《卷四》
- `[ns_zwds_j4_040]` `[trigger: 截空星]` `[factor_trigger: star_jiekong]` `[role: 主干]` 截空为空星，主空亡虚耗。 → 《卷四》
- `[ns_zwds_j4_041]` `[trigger: 困厄结果]` `[factor_trigger: result_kune]` `[role: 结果]` 困厄结果为困顿厄运的凶险判断。 → 《卷四》
- `[ns_zwds_j4_042]` `[trigger: 显示结果]` `[factor_trigger: result_xianshi]` `[role: 结果]` 显示结果为命格显达的判断。 → 《卷四》
- `[ns_zwds_j4_043]` `[trigger: 贪狼化忌四化]` `[factor_trigger: sihua_tanlangji]` `[role: 条件分支]` 贪狼化忌四化为贪狼化忌的配置。 → 《卷四》
- `[ns_zwds_j4_044]` `[trigger: 廉贞将军星]` `[factor_trigger: star_lianzhenjiang]` `[role: 主干]` 廉贞将军星为廉贞的将军属性。 → 《卷四》
- `[ns_zwds_j4_045]` `[trigger: 流羊陀星]` `[factor_trigger: star_liuyangtuo]` `[role: 主干]` 流羊陀星为流年擎羊陀罗。 → 《卷四》
- `[ns_zwds_j4_046]` `[trigger: 双禄格]` `[factor_trigger: pattern_shuanglu]` `[role: 条件分支]` 双禄格为禄存化禄同会的贵格。 → 《卷四》
- `[ns_zwds_j4_047]` `[trigger: 地网铃格]` `[factor_trigger: pattern_diwangling]` `[role: 条件分支]` 地网铃格为地网遇铃星的凶险配置。 → 《卷四》
- `[ns_zwds_j4_048]` `[trigger: 晚年殁结果]` `[factor_trigger: result_wannianmo]` `[role: 结果]` 晚年殁结果为晚年寿终的判断。 → 《卷四》
- `[ns_zwds_j4_049]` `[trigger: 机梁格]` `[factor_trigger: pattern_jiliang]` `[role: 条件分支]` 机梁格为天机天梁同宫的格局。 → 《卷四》
- `[ns_zwds_j4_050]` `[trigger: 土埋社稷格]` `[factor_trigger: pattern_tumaishedi]` `[role: 条件分支]` 土埋社稷格为凶险的格局配置。 → 《卷四》
- `[ns_zwds_j4_051]` `[trigger: 天伤星曜]` `[factor_trigger: star_tianshangxing]` `[role: 主干]` 天伤星曜主伤灾意外。 → 《卷四》
- `[ns_zwds_j4_052]` `[trigger: 木浴白位]` `[factor_trigger: pos_muyubai]` `[role: 主干]` 木浴白位为特定宫位的五行配置。 → 《卷四》
- `[ns_zwds_j4_053]` `[trigger: 多重凶格]` `[factor_trigger: pattern_duochongxiong]` `[role: 条件分支]` 多重凶格为多个凶星叠加的配置。 → 《卷四》
- `[ns_zwds_j4_054]` `[trigger: 卯生忌]` `[factor_trigger: taboo_maoshengji]` `[role: 条件分支]` 卯生忌为卯年生人特定的忌讳。 → 《卷四》
- `[ns_zwds_j4_055]` `[trigger: 地网忌格]` `[factor_trigger: pattern_diwangji]` `[role: 条件分支]` 地网忌格为地网遇化忌的凶险配置。 → 《卷四》
- `[ns_zwds_j4_056]` `[trigger: 日月权禄格]` `[factor_trigger: pattern_riyuequanlu]` `[role: 条件分支]` 日月权禄格为日月逢权禄的贵格。 → 《卷四》
- `[ns_zwds_j4_057]` `[trigger: 芳泊结果]` `[factor_trigger: result_fangbo]` `[role: 结果]` 芳泊结果为漂泊流离的判断。 → 《卷四》
- `[ns_zwds_j4_058]` `[trigger: 劫空冲格]` `[factor_trigger: pattern_jiekongchong]` `[role: 条件分支]` 劫空冲格为地劫地空冲照的配置。 → 《卷四》
- `[ns_zwds_j4_059]` `[trigger: 福不全结果]` `[factor_trigger: result_fubuquan]` `[role: 结果]` 福不全结果为福气不全的判断。 → 《卷四》
- `[ns_zwds_j4_060]` `[trigger: 丹墀贵格]` `[factor_trigger: pattern_danchigui]` `[role: 条件分支]` 丹墀贵格为朝廷显贵的格局。 → 《卷四》
- `[ns_zwds_j4_061]` `[trigger: 商人行动]` `[factor_trigger: action_shangren]` `[role: 主干]` 商人行动为经商行为类型。 → 《卷四》
- `[ns_zwds_j4_062]` `[trigger: 狐联栖典]` `[factor_trigger: allusion_hulianqi]` `[role: 主干]` 狐联栖典为狐仙托寄的典故。 → 《卷四》
- `[ns_zwds_j4_063]` `[trigger: 金谷典]` `[factor_trigger: allusion_jingu]` `[role: 主干]` 金谷典为石崇金谷园的典故。 → 《卷四》
- `[ns_zwds_j4_064]` `[trigger: 陶朱典]` `[factor_trigger: allusion_taozhu]` `[role: 主干]` 陶朱典为范蠡陶朱公的典故。 → 《卷四》
- `[ns_zwds_j4_065]` `[trigger: 水火平衡]` `[factor_trigger: balance_shuihuo]` `[role: 主干]` 水火平衡为水火二行的平衡关系。 → 《卷四》
- `[ns_zwds_j4_066]` `[trigger: 性格格局]` `[factor_trigger: character_pattern]` `[role: 主干]` 性格格局为性格类型的判断。 → 《卷四》
- `[ns_zwds_j4_067]` `[trigger: 成就层级]` `[factor_trigger: chengjiu_cengci]` `[role: 主干]` 成就层级为事业成就的分层。 → 《卷四》
- `[ns_zwds_j4_068]` `[trigger: 梁林甲午组合]` `[factor_trigger: combo_lianglin_jiawu]` `[role: 条件分支]` 梁林甲午组合为天梁林冲在甲午的配置。 → 《卷四》
- `[ns_zwds_j4_069]` `[trigger: 梁月冲破组合]` `[factor_trigger: combo_liangyue_chongpo]` `[role: 条件分支]` 梁月冲破组合为天梁太阴冲破的配置。 → 《卷四》
- `[ns_zwds_j4_070]` `[trigger: 仁义四海组合]` `[factor_trigger: combo_renyi_sihai]` `[role: 条件分支]` 仁义四海组合为仁义遍四海的配置。 → 《卷四》
- `[ns_zwds_j4_071]` `[trigger: 三方煞组合]` `[factor_trigger: combo_sanfang_sha]` `[role: 条件分支]` 三方煞组合为三方遇煞的配置。 → 《卷四》
- `[ns_zwds_j4_072]` `[trigger: 四正忌组合]` `[factor_trigger: combo_sizheng_ji]` `[role: 条件分支]` 四正忌组合为四正宫遇忌的配置。 → 《卷四》
- `[ns_zwds_j4_073]` `[trigger: 同时遇谋组合]` `[factor_trigger: combo_tongshi_yumou]` `[role: 条件分支]` 同时遇谋组合为同时遇到谋害的配置。 → 《卷四》
- `[ns_zwds_j4_074]` `[trigger: 羊陀七杀组合]` `[factor_trigger: combo_yangtuo_qisha]` `[role: 条件分支]` 羊陀七杀组合为擎羊陀罗遇七杀的配置。 → 《卷四》
- `[ns_zwds_j4_075]` `[trigger: 后人坐贵条件]` `[factor_trigger: condition_houren_zuogui]` `[role: 条件分支]` 后人坐贵条件为后人得贵的条件。 → 《卷四》
- `[ns_zwds_j4_076]` `[trigger: 火忌不入条件]` `[factor_trigger: condition_huoji_buru]` `[role: 条件分支]` 火忌不入条件为火星化忌不入的条件。 → 《卷四》
- `[ns_zwds_j4_077]` `[trigger: 申人九龄条件]` `[factor_trigger: condition_shenren_jiuling]` `[role: 条件分支]` 申人九龄条件为申年生人九岁限的条件。 → 《卷四》
- `[ns_zwds_j4_078]` `[trigger: 申人有忌条件]` `[factor_trigger: condition_shenren_youji]` `[role: 条件分支]` 申人有忌条件为申年生人有忌的条件。 → 《卷四》
- `[ns_zwds_j4_079]` `[trigger: 阳刃有地条件]` `[factor_trigger: condition_yangren_youdi]` `[role: 条件分支]` 阳刃有地条件为阳刃得地的条件。 → 《卷四》
- `[ns_zwds_j4_080]` `[trigger: 子生人忌寅年条件]` `[factor_trigger: condition_zishengren_ji_yinnian]` `[role: 条件分支]` 子生人忌寅年条件为子年生人忌寅年的条件。 → 《卷四》
- `[ns_zwds_j4_081]` `[trigger: 禄主入地缺陷]` `[factor_trigger: defect_luzhu_ruodi]` `[role: 条件分支]` 禄主入地缺陷为禄主入地的缺陷配置。 → 《卷四》
- `[ns_zwds_j4_082]` `[trigger: 地域因素]` `[factor_trigger: diyu_yinsu]` `[role: 主干]` 地域因素为地理位置的影响因素。 → 《卷四》
- `[ns_zwds_j4_083]` `[trigger: 官灾事件]` `[factor_trigger: event_guanzai]` `[role: 结果]` 官灾事件为官司灾祸的结果。 → 《卷四》
- `[ns_zwds_j4_084]` `[trigger: 封诰体系]` `[factor_trigger: fenggao_tixi]` `[role: 主干]` 封诰体系为封诰贵人的体系。 → 《卷四》
- `[ns_zwds_j4_085]` `[trigger: 五行框架]` `[factor_trigger: frame_wuxing]` `[role: 主干]` 五行框架为五行生克的框架。 → 《卷四》
- `[ns_zwds_j4_086]` `[trigger: 陀罗破军凶]` `[factor_trigger: malefic_tuoluo_poju]` `[role: 条件分支]` 陀罗破军凶为陀罗与破军的凶险配置。 → 《卷四》
- `[ns_zwds_j4_087]` `[trigger: 陀罗天空凶]` `[factor_trigger: malefic_tuoluo_tiankong]` `[role: 条件分支]` 陀罗天空凶为陀罗与天空的凶险配置。 → 《卷四》
- `[ns_zwds_j4_088]` `[trigger: 陀罗天使凶]` `[factor_trigger: malefic_tuoluo_tianshi]` `[role: 条件分支]` 陀罗天使凶为陀罗与天使的凶险配置。 → 《卷四》
- `[ns_zwds_j4_089]` `[trigger: 陀罗天刑凶]` `[factor_trigger: malefic_tuoluo_tianxing]` `[role: 条件分支]` 陀罗天刑凶为陀罗与天刑的凶险配置。 → 《卷四》
- `[ns_zwds_j4_090]` `[trigger: 文星逢廉凶]` `[factor_trigger: malefic_wenxing_fenglian]` `[role: 条件分支]` 文星逢廉凶为文星逢廉贞的凶险配置。 → 《卷四》
- `[ns_zwds_j4_091]` `[trigger: 小限丧门凶]` `[factor_trigger: malefic_xiaoxian_sangmen]` `[role: 条件分支]` 小限丧门凶为小限遇丧门的凶险配置。 → 《卷四》
- `[ns_zwds_j4_092]` `[trigger: 星忌会合凶]` `[factor_trigger: malefic_xingji_huihe]` `[role: 条件分支]` 星忌会合凶为星曜与忌会合的凶险配置。 → 《卷四》
- `[ns_zwds_j4_093]` `[trigger: 星气无子凶]` `[factor_trigger: malefic_xingqi_wuzi]` `[role: 条件分支]` 星气无子凶为星气无子的凶险配置。 → 《卷四》
- `[ns_zwds_j4_094]` `[trigger: 星伤哭凶]` `[factor_trigger: malefic_xingshangku]` `[role: 条件分支]` 星伤哭凶为星伤天哭的凶险配置。 → 《卷四》
- `[ns_zwds_j4_095]` `[trigger: 兄弟落陷凶]` `[factor_trigger: malefic_xiongdi_luoxian]` `[role: 条件分支]` 兄弟落陷凶为兄弟宫落陷的凶险配置。 → 《卷四》
- `[ns_zwds_j4_096]` `[trigger: 羊火凶格]` `[factor_trigger: malefic_yanghuo]` `[role: 条件分支]` 羊火凶格为擎羊火星的凶险配置。 → 《卷四》
- `[ns_zwds_j4_097]` `[trigger: 羊铃合会凶]` `[factor_trigger: malefic_yangling_hehe]` `[role: 条件分支]` 羊铃合会凶为擎羊铃星合会的凶险配置。 → 《卷四》
- `[ns_zwds_j4_098]` `[trigger: 羊铃忌并忌凶]` `[factor_trigger: malefic_yangling_ji_bingji]` `[role: 条件分支]` 羊铃忌并忌凶为羊铃与忌并忌的凶险配置。 → 《卷四》
- `[ns_zwds_j4_099]` `[trigger: 羊陀侍并凶]` `[factor_trigger: malefic_yangtuo_shibing]` `[role: 条件分支]` 羊陀侍并凶为羊陀侍并的凶险配置。 → 《卷四》
- `[ns_zwds_j4_100]` `[trigger: 羊陀太岁叠并凶]` `[factor_trigger: malefic_yangtuo_taisui_diebing]` `[role: 条件分支]` 羊陀太岁叠并凶为羊陀与太岁叠并的凶险配置。 → 《卷四》
- `[ns_zwds_j4_101]` `[trigger: 夭忌福德凶]` `[factor_trigger: malefic_yaoji_fude]` `[role: 条件分支]` 夭忌福德凶为夭忌在福德的凶险配置。 → 《卷四》
- `[ns_zwds_j4_102]` `[trigger: 阴辰羊陀凶]` `[factor_trigger: malefic_yinchen_yangtuo]` `[role: 条件分支]` 阴辰羊陀凶为太阴在辰遇羊陀的凶险配置。 → 《卷四》
- `[ns_zwds_j4_103]` `[trigger: 紫系火空飞廉凶]` `[factor_trigger: malefic_zixi_huokong_feilian]` `[role: 条件分支]` 紫系火空飞廉凶为紫系与火空飞廉的凶险配置。 → 《卷四》
- `[ns_zwds_j4_104]` `[trigger: 衰中带旺机制]` `[factor_trigger: mech_shuaizhong_daiwang]` `[role: 主干]` 衰中带旺机制为衰中带旺的运作机制。 → 《卷四》
- `[ns_zwds_j4_105]` `[trigger: 占位符元素]` `[factor_trigger: meta_placeholder]` `[role: 主干]` 占位符元素为占位的元素。 → 《卷四》
- `[ns_zwds_j4_106]` `[trigger: 落井方法]` `[factor_trigger: method_luojing]` `[role: 主干]` 落井方法为落井推断的方法。 → 《卷四》
- `[ns_zwds_j4_107]` `[trigger: 兼办论之修饰]` `[factor_trigger: modifier_jianbanlunzhi]` `[role: 主干]` 兼办论之修饰为兼办论断的修饰。 → 《卷四》
- `[ns_zwds_j4_108]` `[trigger: 身宫]` `[factor_trigger: palace_body]` `[role: 主干]` 身宫为紫微斗数的身宫位置。 → 《卷四》
- `[ns_zwds_j4_109]` `[trigger: 墓宫]` `[factor_trigger: palace_mu]` `[role: 主干]` 墓宫为辰戌丑未四墓宫的统称。 → 《卷四》
- `[ns_zwds_j4_110]` `[trigger: 四限宫]` `[factor_trigger: palace_sixian]` `[role: 主干]` 四限宫为四个限运宫位的统称。 → 《卷四》
- `[ns_zwds_j4_111]` `[trigger: 倦守结果]` `[factor_trigger: result_juanshou]` `[role: 结果]` 倦守结果为倦守的判断。 → 《卷四》
- `[ns_zwds_j4_112]` `[trigger: 爵禄荣结果]` `[factor_trigger: result_juelurong]` `[role: 结果]` 爵禄荣结果为爵禄荣的判断。 → 《卷四》
- `[ns_zwds_j4_113]` `[trigger: 巨富结果]` `[factor_trigger: result_jufu]` `[role: 结果]` 巨富结果为巨富的判断。 → 《卷四》
- `[ns_zwds_j4_114]` `[trigger: 科禄雀折结果]` `[factor_trigger: result_kelu_quezhe]` `[role: 结果]` 科禄雀折结果为科禄雀折的判断。 → 《卷四》
- `[ns_zwds_j4_115]` `[trigger: 空门结果]` `[factor_trigger: result_kongmen]` `[role: 结果]` 空门结果为空门的判断。 → 《卷四》
- `[ns_zwds_j4_116]` `[trigger: 立达结果]` `[factor_trigger: result_lida]` `[role: 结果]` 立达结果为立达的判断。 → 《卷四》
- `[ns_zwds_j4_117]` `[trigger: 利人结果]` `[factor_trigger: result_liren]` `[role: 结果]` 利人结果为利人的判断。 → 《卷四》
- `[ns_zwds_j4_118]` `[trigger: 流荡结果]` `[factor_trigger: result_liudang]` `[role: 结果]` 流荡结果为流荡的判断。 → 《卷四》
- `[ns_zwds_j4_119]` `[trigger: 立业正荣结果]` `[factor_trigger: result_liye_zhengrong]` `[role: 结果]` 立业正荣结果为立业正荣的判断。 → 《卷四》
- `[ns_zwds_j4_120]` `[trigger: 禄倒结果]` `[factor_trigger: result_ludao]` `[role: 结果]` 禄倒结果为禄倒的判断。 → 《卷四》
- `[ns_zwds_j4_121]` `[trigger: 冒险结果]` `[factor_trigger: result_maoxian]` `[role: 结果]` 冒险结果为冒险的判断。 → 《卷四》
- `[ns_zwds_j4_122]` `[trigger: 美结果]` `[factor_trigger: result_mei]` `[role: 结果]` 美结果为美的判断。 → 《卷四》
- `[ns_zwds_j4_123]` `[trigger: 命难逃结果]` `[factor_trigger: result_ming_nantao]` `[role: 结果]` 命难逃结果为命难逃的判断。 → 《卷四》
- `[ns_zwds_j4_124]` `[trigger: 命虚结果]` `[factor_trigger: result_mingxu]` `[role: 结果]` 命虚结果为命虚的判断。 → 《卷四》
- `[ns_zwds_j4_125]` `[trigger: 命遇生阳结果]` `[factor_trigger: result_mingyushengyang]` `[role: 结果]` 命遇生阳结果为命遇生阳的判断。 → 《卷四》
- `[ns_zwds_j4_126]` `[trigger: 命中结果]` `[factor_trigger: result_mingzhong]` `[role: 结果]` 命中结果为命中的判断。 → 《卷四》
- `[ns_zwds_j4_127]` `[trigger: 南国结果]` `[factor_trigger: result_nanguo]` `[role: 结果]` 南国结果为南国的判断。 → 《卷四》
- `[ns_zwds_j4_128]` `[trigger: 纳宿贤佐结果]` `[factor_trigger: result_nasu_xianzuo]` `[role: 结果]` 纳宿贤佐结果为纳宿贤佐的判断。 → 《卷四》
- `[ns_zwds_j4_129]` `[trigger: 破败结果]` `[factor_trigger: result_pobai]` `[role: 结果]` 破败结果为破败的判断。 → 《卷四》
- `[ns_zwds_j4_130]` `[trigger: 破败损寿结果]` `[factor_trigger: result_pobaisunshou]` `[role: 结果]` 破败损寿结果为破败损寿的判断。 → 《卷四》
- `[ns_zwds_j4_131]` `[trigger: 破军福命结果]` `[factor_trigger: result_pojun_fuming]` `[role: 结果]` 破军福命结果为破军福命的判断。 → 《卷四》
- `[ns_zwds_j4_132]` `[trigger: 妻兼无疑结果]` `[factor_trigger: result_qi_jian_wuyi]` `[role: 结果]` 妻兼无疑结果为妻兼无疑的判断。 → 《卷四》
- `[ns_zwds_j4_133]` `[trigger: 妻夫益益结果]` `[factor_trigger: result_qifu_yiyi]` `[role: 结果]` 妻夫益益结果为妻夫益益的判断。 → 《卷四》
- `[ns_zwds_j4_134]` `[trigger: 清闲结果]` `[factor_trigger: result_qingxian]` `[role: 结果]` 清闲结果为清闲的判断。 → 《卷四》
- `[ns_zwds_j4_135]` `[trigger: 却结果]` `[factor_trigger: result_que]` `[role: 结果]` 却结果为却的判断。 → 《卷四》
- `[ns_zwds_j4_136]` `[trigger: 不宜寅申时机]` `[factor_trigger: timing_buyi_yinshen]` `[role: 主干]` 不宜寅申时机为不宜寅申的时机。 → 《卷四》
- `[ns_zwds_j4_137]` `[trigger: 大限本身时机]` `[factor_trigger: timing_daxian_benshen]` `[role: 主干]` 大限本身时机为大限本身的时机。 → 《卷四》
- `[ns_zwds_j4_138]` `[trigger: 大限辰太阳时机]` `[factor_trigger: timing_daxian_chen_taiyang]` `[role: 主干]` 大限辰太阳时机为大限辰太阳的时机。 → 《卷四》
- `[ns_zwds_j4_139]` `[trigger: 大限夹地小限时机]` `[factor_trigger: timing_daxian_jiadi_xiaoxian]` `[role: 主干]` 大限夹地小限时机为大限夹地小限的时机。 → 《卷四》
- `[ns_zwds_j4_140]` `[trigger: 大限绝地时机]` `[factor_trigger: timing_daxian_jiedi]` `[role: 主干]` 大限绝地时机为大限绝地的时机。 → 《卷四》
- `[ns_zwds_j4_141]` `[trigger: 大限擎羊时机]` `[factor_trigger: timing_daxian_qingyang]` `[role: 主干]` 大限擎羊时机为大限擎羊的时机。 → 《卷四》
- `[ns_zwds_j4_142]` `[trigger: 大限衰时机]` `[factor_trigger: timing_daxian_shuai]` `[role: 主干]` 大限衰时机为大限衰的时机。 → 《卷四》
- `[ns_zwds_j4_143]` `[trigger: 大限死宫时机]` `[factor_trigger: timing_daxian_sigong]` `[role: 主干]` 大限死宫时机为大限死宫的时机。 → 《卷四》
- `[ns_zwds_j4_144]` `[trigger: 大限太岁时机]` `[factor_trigger: timing_daxian_taisui]` `[role: 主干]` 大限太岁时机为大限太岁的时机。 → 《卷四》
- `[ns_zwds_j4_145]` `[trigger: 大限太岁天使时机]` `[factor_trigger: timing_daxian_taisui_tianshi]` `[role: 主干]` 大限太岁天使时机为大限太岁天使的时机。 → 《卷四》
- `[ns_zwds_j4_146]` `[trigger: 大限天罗时机]` `[factor_trigger: timing_daxian_tianluo]` `[role: 主干]` 大限天罗时机为大限天罗的时机。 → 《卷四》
- `[ns_zwds_j4_147]` `[trigger: 大限天使擎羊时机]` `[factor_trigger: timing_daxian_tianshi_qingyang]` `[role: 主干]` 大限天使擎羊时机为大限天使擎羊的时机。 → 《卷四》
- `[ns_zwds_j4_148]` `[trigger: 大限午时机]` `[factor_trigger: timing_daxian_wu]` `[role: 主干]` 大限午时机为大限午的时机。 → 《卷四》
- `[ns_zwds_j4_149]` `[trigger: 大小地网时机]` `[factor_trigger: timing_daxiao_diwang]` `[role: 主干]` 大小地网时机为大小地网的时机。 → 《卷四》
- `[ns_zwds_j4_150]` `[trigger: 大小限天伤时机]` `[factor_trigger: timing_daxiaoxian_tianshang]` `[role: 主干]` 大小限天伤时机为大小限天伤的时机。 → 《卷四》
- `[ns_zwds_j4_151]` `[trigger: 二限地网时机]` `[factor_trigger: timing_erxian_diwang]` `[role: 主干]` 二限地网时机为二限地网的时机。 → 《卷四》
- `[ns_zwds_j4_152]` `[trigger: 忌太岁冲时机]` `[factor_trigger: timing_ji_taisui_chong]` `[role: 主干]` 忌太岁冲时机为忌太岁冲的时机。 → 《卷四》
- `[ns_zwds_j4_153]` `[trigger: 流昌绝卯时机]` `[factor_trigger: timing_liuchang_juemao]` `[role: 主干]` 流昌绝卯时机为流昌绝卯的时机。 → 《卷四》
- `[ns_zwds_j4_154]` `[trigger: 流羊巨门化忌时机]` `[factor_trigger: timing_liuyang_jumen_huaji]` `[role: 主干]` 流羊巨门化忌时机为流羊巨门化忌的时机。 → 《卷四》
- `[ns_zwds_j4_155]` `[trigger: 流羊流陀时机]` `[factor_trigger: timing_liuyang_liutuo]` `[role: 主干]` 流羊流陀时机为流羊流陀的时机。 → 《卷四》
- `[ns_zwds_j4_156]` `[trigger: 流羊陀冲命时机]` `[factor_trigger: timing_liuyangtuo_chongming]` `[role: 主干]` 流羊陀冲命时机为流羊陀冲命的时机。 → 《卷四》
- `[ns_zwds_j4_157]` `[trigger: 擎羊天使时机]` `[factor_trigger: timing_qingyang_tianshi]` `[role: 主干]` 擎羊天使时机为擎羊天使的时机。 → 《卷四》
- `[ns_zwds_j4_158]` `[trigger: 七杀冲逢时机]` `[factor_trigger: timing_qisha_chongfeng]` `[role: 主干]` 七杀冲逢时机为七杀冲逢的时机。 → 《卷四》
- `[ns_zwds_j4_159]` `[trigger: 三十后时机]` `[factor_trigger: timing_sanshi_hou]` `[role: 主干]` 三十后时机为三十后的时机。 → 《卷四》
- `[ns_zwds_j4_160]` `[trigger: 上下时机]` `[factor_trigger: timing_shangxia]` `[role: 主干]` 上下时机为上下的时机。 → 《卷四》"""
    normalized_text_zh: str = """"""
    subject: str = "兄弟宫诸星论"
    factor_refs: list = ['palace_siblings', 'state_miaowang', 'state_xiandi', 'group_liusha', 'star_doujun', 'source_ref', 'rel_xiongdi_001', 'star_ziwei', 'rel_xiongdi_002', 'group_liusha', 'rel_xiongdi_003', 'group_jixing', 'evi_xiongdi_001', 'star_ziwei', 'rule_xiongdi_ziwei', 'evi_xiongdi_002', 'group_liusha', 'rule_xiongdi_sha', 'concept_siblings', 'concept_mutual_support']
    
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
        l1_anchor="zw_v1.0.0_兄弟宫诸星论_001_L1",
    )
    version: str = "1.0.0"
