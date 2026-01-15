"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.523663
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
    semantic_id="zpzq_v1.0.0_水同生木而印有偏正_金同克木而局有官煞_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 水同生木而印有偏正金同克木而局有官煞(SemanticEntry):
    """
    - **原文（source_text）**：
  然以五行而统论之，则水木相生，金木相克。以五行之阴阳而分配之，则生克之中，又有异同。此所以水同生木，而印有偏正；金同克木，而局有官煞也。印绶之中，偏正...
    """
    
    original_text: str = """- **原文（source_text）**：
  然以五行而统论之，则水木相生，金木相克。以五行之阴阳而分配之，则生克之中，又有异同。此所以水同生木，而印有偏正；金同克木，而局有官煞也。印绶之中，偏正相似，生克之殊，可置勿论；而相克之内，一官一煞，淑慝判然，其理不可不细详也。即以甲乙庚辛言之。甲者，阳木也，木之生气也；乙者，阴木也，木之形质也。庚者，阳金也，秋天肃杀之气也；辛者，阴金也，人间五金之质也。木之生气，寄于木而行于天，故逢秋天为官，而乙则反是，庚官而辛杀也。又以丙丁庚辛言之。丙者，阳火也，融和之气也；丁者，阴火也，薪传之火也。秋天肃杀之气，逢阳和而克去，而人间之金，不畏阳和，此庚以丙为杀，而辛以丙为官也。人间金铁之质，逢薪传之火而立化，而肃杀之气，不畏薪传之火。此所以辛以丁为杀，而庚以丁为官也。即此以推，而余者以相克可知矣。

- 原注（原文注解）：
  　　此段由五行总论进入阴阳细分，明确"水同生木而印有偏正、金同克木而局有官煞"的十神分化原理，以甲乙庚辛、丙丁庚辛为例详细说明气质配对规律，为后文十神取用奠定基础。

- 分字分词释义：
  - 以五行而统论之：从五行的总体关系来看。
  - 水木相生，金木相克：水生木，金克木，这是五行层面的粗略关系。
  - 以五行之阴阳而分配之：进一步按阴阳细分每一行。
  - 生克之中，又有异同：同样是生或克，因阴阳配对不同而有差异。
  - 水同生木，而印有偏正：水都能生木，但壬水生甲木为偏印，癸水生甲木为正印（以甲木日主为例）。
  - 金同克木，而局有官煞：金都能克木，但庚金克甲木为偏官（七煞），辛金克甲木为正官。
  - 印绶之中，偏正相似：正印与偏印的功能较为相近，都是生助日主。
  - 生克之殊，可置勿论：在印绶的生克功能上，偏正的差异可以暂且不论。
  - 相克之内，一官一煞：在克的关系中，正官与七煞的差异极大。
  - 淑慝判然：善（正官）与恶（七煞）性质截然分明。
  - 甲者，阳木也，木之生气也：甲木是阳木，代表木的生发之气。
  - 乙者，阴木也，木之形质也：乙木是阴木，代表木的具体形质。
  - 庚者，阳金也，秋天肃杀之气也：庚金是阳金，代表秋天的肃杀之气。
  - 辛者，阴金也，人间五金之质也：辛金是阴金，代表人间金属之质。
  - 木之生气，寄于木而行于天：甲木的生气寄托在木中，运行于天空间。
  - 逢秋天为官：甲木遇到庚金（秋天之气），为正官关系（阳见阳为煞，但此处指气象层面）。
  - 乙则反是，庚官而辛杀：乙木则相反，庚金为正官，辛金为七煞。
  - 丙者，阳火也，融和之气也：丙火是阳火，代表融和之气。
  - 丁者，阴火也，薪传之火也：丁火是阴火，代表薪柴传承之火。
  - 秋天肃杀之气，逢阳和而克去：庚金（秋天肃杀之气）遇到丙火（阳和之气）而被克制。
  - 人间之金，不畏阳和：辛金（人间金属）不怕丙火（阳和之气）。
  - 庚以丙为杀，而辛以丙为官：庚金见丙火为七煞，辛金见丙火为正官。
  - 人间金铁之质，逢薪传之火而立化：辛金（人间金铁）遇到丁火（薪传之火）立即融化。
  - 肃杀之气，不畏薪传之火：庚金（肃杀之气）不怕丁火（薪传之火）。
  - 辛以丁为杀，而庚以丁为官：辛金见丁火为七煞，庚金见丁火为正官。
  - 即此以推，而余者以相克可知矣：按照这个规律类推，其他天干的官煞关系都可以知道了。

- 核心要点：
  - **同是生克，阴阳配对不同，吉凶性质亦异**：这是十神理论的根基。
  - **官煞之别尤为重要**：官为善（淑）、煞为恶（慝），性质截然，必须细辨。
  - **气与质的配对逻辑**：阳干多主气象，阴干多主形质；气遇气为官（阳和之气克秋肃之气），质遇质为煞（薪传之火化金铁之质）。

- **规范化释义（primary_lang_explained）**：
  如果从五行的总体关系来看，水生木、金克木，这很简单。但如果进一步按阴阳细分，同样是生或克，因为阴阳配对不同，就会产生差异。所以水都能生木，但有正印偏印之分；金都能克木，但有正官七煞之别。在印绶这一类中，正印与偏印的功能比较相似，都是生助日主，生克的差异可以暂时不论；但在相克这一类中，正官与七煞的差异极大，一个是善（正官），一个是恶（七煞），性质截然分明，必须仔细辨别。就拿甲乙庚辛来说：甲木是阳木，代表木的生发之气；乙木是阴木，代表木的具体形质。庚金是阳金，代表秋天的肃杀之气；辛金是阴金，代表人间金属之质。甲木的生气运行于天空间，遇到秋天的肃杀之气（庚金）成为正官关系；而乙木则相反，庚金是正官，辛金是七煞。再以丙丁庚辛来说：丙火是阳火，代表融和之气；丁火是阴火，代表薪柴传承之火。秋天的肃杀之气（庚金）遇到融和之气（丙火）会被克制，但人间的金属（辛金）不怕融和之气，所以庚金见丙火为七煞，辛金见丙火为正官。人间的金铁（辛金）遇到薪传之火（丁火）会立即融化，但肃杀之气（庚金）不怕薪传之火，所以辛金见丁火为七煞，庚金见丁火为正官。按照这个规律类推，其他天干的官煞关系都可以知道了。
 - **完整对等诠释（secondary_lang_full）**：  
  In broad terms, Water always generates Wood and Metal always restrains Wood. Once we divide each element into its yin and yang forms, however, the same act of generating or controlling splits into different Ten-God roles. When Water nourishes Wood, it can appear as Proper Resource, steadily supporting the Day Master in a direct and orthodox way, or as Indirect Resource, whose help comes through oblique, consuming or unstable channels. When Metal checks Wood, it can appear as Direct Officer, symbolising legitimate authority and measured restraint, or as Seven Killings, symbolising harsh, pressing and risky force. Within the Resource group the contrast is secondary because both types ultimately feed the self; within the controlling group the contrast is decisive—one tends toward order and moral rightness, the other toward danger—so the line between them must be drawn with great care.

  The pairing logic becomes clearer if we look at specific stems. Jia Wood represents the rising, expansive qi side of Wood, while Yi Wood represents its concrete body and substance. Geng Metal represents the stern autumnal qi of cutting and punishment, while Xin Metal represents worked metal as a tangible material. When qi confronts qi—Jia facing Geng—the result is a relatively balanced Officer relationship, in which autumnal discipline channels spring vitality. When substance confronts substance—Yi facing Geng or Xin—the clash is more brutal and tends toward Killing. With Fire the contrast is similar. Bing Fire is the broad, harmonising warmth of the sun, whereas Ding Fire is the focused flame of a lamp or hearth. Geng, as cutting autumn qi, is more easily moderated by Bing’s wide warmth and so can be read as Officer there, while its encounter with Ding tends to be too severe and is read as Killing. Xin, solid metal, can be melted by Ding’s small but intense flame, a Killing-type interaction, yet may simply be refined rather than destroyed by Bing’s expansive heat, an Officer-type interaction. By tracing these yin–yang and qi–substance pairings across all the stems, we can systematically work out which encounters give Direct Officer and which give Seven Killings.

- 详细解说：
  - 十神不是五行的简单重复，而是"五行×阴阳×气质"的三维展开。
  - 阳干偏重"气象"（如甲木之生气、庚金之肃杀气、丙火之阳和气），阴干偏重"形质"（如乙木之形质、辛金之金铁质、丁火之薪传火）。
  - "气遇气"与"质遇质"的配对逻辑，决定了官煞的分野：气象层面的克制偏温和（为官），形质层面的克制偏激烈（为煞）。

- 核心要点：
  - 论日干不仅看"属哪一行"，还要看"属阴属阳""偏气偏质"。
  - 官煞必须先分清，否则吉凶易倒置：正官为贵，七煞为凶（未制服时）。
  - 在具体判断中，要结合日主的阴阳与气质，看对方是"气克气"还是"质克质"，从而判断是官还是煞。

- 应用推演：
  1) 确定日主的阴阳与气质倾向（如甲木偏气、乙木偏质）。
  2) 找出局中克日主的五行（如金克木）。
  3) 进一步细分该五行的阴阳（如庚金、辛金）。
  4) 根据阴阳配对判断是正官还是七煞（如甲见庚为偏官煞、甲见辛为正官）。
  5) 在格局与用神判断中，正官与七煞的取用方式截然不同。

- 反例与边界：
  - 只按五行粗看"金克木"，不分阴阳，难入精微，容易把正官与七煞混为一谈。
  - 把"气"与"质"理解成抽象形容，而不落实到十神配对上，会失去本段的核心价值。
  - 机械记忆"甲见庚为煞、甲见辛为官"而不理解背后的气质配对逻辑，容易在变格中出错。

- 小例（示意）：
  - 甲木日主，见庚金七煞，需要丙火制煞或壬水化煞，否则煞重身轻危险；见辛金正官，则喜财生官、印护官，成就贵格。
  - 乙木日主，见辛金七煞，需要丙火制煞；见庚金正官，则喜财生官、印护官。

- 校勘与字词辨析：
  - "淑慝判然"："淑"为善，"慝"为恶，形容正官与七煞性质截然对立。
  - "木之生气，寄于木而行于天"：各本用字大致相同，强调甲木的"气"属性与"在天"层面。
  - "即此以推，而余者以相克可知矣"：授权读者触类旁通，不必逐一列举所有十干的官煞关系。


- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_143]` `[trigger: 用神成败]` `[factor_trigger: yongshen_status IN (cheng, bai) AND chengzhong_youbai AND baizhong_youcheng]` `[role: 主干]` 用神有成有败，成中有败，败中有成。 → 《子平真诠·论用神成败救应》#成败
  - `[ns_zpzy_144]` `[trigger: 救应之道]` `[factor_trigger: (chengzhong_youbai AND yizi_kejiu) OR (baizhong_youcheng AND yizi_kepo)]` `[role: 主干]` 成中有败，一字可救；败中有成，一字可破。 → 《子平真诠·论用神成败救应》#救应
  - `[ns_zpzy_145]` `[trigger: 救应之法]` `[factor_trigger: (guan_feng_shang AND touyin_yijie) OR (cai_feng_jie AND toushi_yihua)]` `[role: 主干]` 官逢伤而透印以解，财逢劫而透食以化。 → 《子平真诠·论用神成败救应》#救应
  - `[ns_zpzy_146]` `[trigger: 成败互转]` `[factor_trigger: (chengge AND yizi_po_ji_bai) OR (baige AND yizi_jiu_ji_cheng)]` `[role: 主干]` 成格者一字破之即败，败格者一字救之即成。 → 《子平真诠·论用神成败救应》#互转
  - `[ns_zpzy_147]` `[trigger: 用神为纲]` `[factor_trigger: bazi_yongshen AND zhuanqiu_yueling]` `[role: 主干]` 八字用神，专求月令。 → 《子平真诠》#论用神
  - `[ns_zpzy_148]` `[trigger: 月令司权]` `[factor_trigger: yueling_siquan AND tigang_zhi_fu]` `[role: 主干]` 月令司权，提纲之府。 → 《子平真诠》#论用神
  - `[ns_zpzy_149]` `[trigger: 用神取法]` `[factor_trigger: yongshen_qufa AND yi_yueling_wei_zhu]` `[role: 主干]` 用神取法，以月令为主。 → 《子平真诠》#论用神
  - `[ns_zpzy_150]` `[trigger: 六合之情]` `[factor_trigger: liuhe=(zi_chou_tu, yin_hai_mu)]` `[role: 主干]` 子丑合土，寅亥合木。 → 《子平真诠》#上卷
  - `[ns_zpzy_151]` `[trigger: 天干透出]` `[factor_trigger: dizhi_canggan AND tougan_weiyong]` `[role: 主干]` 地支藏干，透干为用。 → 《子平真诠》#上卷
  - `[ns_zpzy_152]` `[trigger: 透藏分别]` `[factor_trigger: tougan_xianyong AND cangzhi_ancang]` `[role: 主干]` 透干显用，藏支暗藏。 → 《子平真诠》#上卷
  - `[ns_zpzy_153]` `[trigger: 虚实有分]` `[factor_trigger: (xu_zhe AND wugen=true) OR (shi_zhe AND yougen=true)]` `[role: 主干]` 虚者无根，实者有根。 → 《子平真诠》#上卷
  - `[ns_zpzy_154]` `[trigger: 轻重权衡]` `[factor_trigger: qingzhong_quanheng AND jixiong_dingduo]` `[role: 主干]` 轻重权衡，吉凶定夺。 → 《子平真诠》#上卷
  - `[ns_zpzy_155]` `[trigger: 太过不及]` `[factor_trigger: (taiguo=true OR buji=true) AND result=fei_zhonghe]` `[role: 主干]` 太过不及，皆非中和。 → 《子平真诠》#上卷
  - `[ns_zpzy_156]` `[trigger: 合化有成]` `[factor_trigger: hehua_youcheng=true AND geju_bianhua]` `[role: 主干]` 合化有成，格局变化。 → 《子平真诠》#上卷"""
    normalized_text_zh: str = """"""
    subject: str = "水同生木而印有偏正，金同克木而局有官煞"
    factor_refs: list = ['shishen', 'zhengguan', 'qisha', 'zhengyin', 'pianyin', 'shute_panran', 'susha_zhiqi', 'ronghe_zhiqi']
    
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
        book_id="zipingzhenquan",
        chapter="",
        l1_anchor="zpzq_v1.0.0_水同生木而印有偏正_金同克木而局有官煞_001_L1",
    )
    version: str = "1.0.0"
