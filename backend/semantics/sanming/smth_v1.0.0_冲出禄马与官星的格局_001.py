"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412242
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
    semantic_id="smth_v1.0.0_冲出禄马与官星的格局_001",
    book_id="sanming",
    engine_id="bazi"
)
class 冲出禄马与官星的格局(SemanticEntry):
    """
    - **原文（source_text）**：

  如甲日生人，柱无酉辛丑，有卯多冲酉，巳酉合丑为甲日正官，喜壬癸生助，忌酉辛填实，若止一卯字，再有刑合起亦为好命。乙日生人柱无申庚，却有寅冲申，子辰合...
    """
    
    original_text: str = """- **原文（source_text）**：

  如甲日生人，柱无酉辛丑，有卯多冲酉，巳酉合丑为甲日正官，喜壬癸生助，忌酉辛填实，若止一卯字，再有刑合起亦为好命。乙日生人柱无申庚，却有寅冲申，子辰合拱或巳刑出，为乙正官，喜壬癸生助，忌申庚填实。戊日生人柱无卯乙，却有酉冲卯，亥未合卯，戊得官星，喜壬癸财、丙丁印，忌见卯乙。己日生人柱无寅甲，却有申冲寅，午戌合寅即暗有官星，喜财、印，忌见寅甲。丙丁二日即倒冲禄马格，庚辛壬癸四日即飞天禄马格，以例推之。以上四干冲合，皆忌官星明露及受伤，月令得官乘旺为妙，冲神遇合，不逢羁绊，必登清贵将相公侯，缺一则减分数，破则近贵衣食，甚者贫乏，岁运喜忌同。《巫宝经》云：乙用庚与申为夫，柱无，却有子辰二字，则能合起申中之庚为乙官星，有此不必再要寅字去冲，有寅更妙，柱无子辰，乃取冲出。甲寅、乙卯、丙午、丁未、戊午、己未、庚申、辛酉、壬子、癸亥，以上十日本身健旺，冲禄元最紧，壬辰、壬戌、戊辰、己丑，冲禄则慢，其余干不用（如明神宗：癸亥、辛酉、癸亥、辛酉，主本癸亥健旺，冲出巳中丙戊禄马为癸用，却得二酉合住为妙）。

- 分字分词释义：

  - **柱无酉辛丑，有卯多冲酉**：以甲日为例，柱中不见酉、辛、丑三位明官，但若有卯木多见，卯冲酉、巳酉合丑，便可暗起甲之正官。
  - **冲出禄马**：通过地支冲合，把原本不现的禄位或官星从对宫或他宫冲出，类似“破中取用”。
  - **倒冲禄马格**：丙、丁二日，以冲出对宫禄马为格，与常规禄马不同，故名“倒冲”。
  - **飞天禄马格**：庚、辛、壬、癸四日，以支神飞临、远处冲合而成禄马，属于另一类高格。
  - **冲神遇合，不逢羁绊**：负责冲出禄马或官星的支神，须在冲后再遇合摄，且不被其他刑、冲、害阻碍。
  - **缺一则减分数，破则近贵衣食**：构成格局的关键条件若有所缺，虽仍有小贵；若被破坏严重，则仅主近贵、衣食小康甚至贫乏。
  - **乙用庚与申为夫**：引《巫宝经》言：乙日以庚金、申金为夫星（官星），若柱中无申庚而有子辰二字，则可合起申中庚金为官。
  - **冲禄元最紧 / 冲禄则慢**：十个健旺日主（甲寅等）冲禄力量最直接迅猛；壬辰、壬戌、戊辰、己丑等日则冲禄较缓，需要更多配合。

- **规范化释义（primary_lang_explained）**：

  冲合禄马这一节，总结的是一类“以冲合起官、起禄”的格局。以甲日为例：若柱中本无酉辛丑等明官，但地支多见卯木，则卯可以冲酉；若再有巳、丑等支相合，则巳酉合丑成局，暗中起出甲之正官。类似地：
  
  - 乙日无申庚，却有寅冲申、子辰合拱或巳刑出，也可因冲合而得正官；
  - 戊日无卯乙，却有酉冲卯、亥未合卯，借冲合得官；
  - 己日无寅甲，却有申冲寅、午戌合寅，同样暗起官星。
  
  在这些结构中，官星并非一开始就明明白白坐在日主旁边，而是隐藏在对宫、三合局或他支之中，需通过冲合才能显露。故原文又引申到“丙丁倒冲禄马”“庚辛壬癸飞天禄马”等：都是通过冲、合的方式，把远处或对宫的禄马位置激活。
  
  要成高格，必须满足两个条件：一是官星、禄位不能被明透或伤坏，需伏而后发；二是负责冲出的支神本身稳固、有力，不被其他刑冲害所羁绊。若月令得官乘旺、冲神遇合、无刑害羁绊，则可至将相公侯之贵；若条件稍差，则降为近贵或衣食无忧；若冲合之神被破、官星受伤，则易主贫乏劳碌。

- **完整对等诠释（secondary_lang_full）**：
  This section on "Clashing-and-Combining Salary-Horse" patterns summarises a class of charts where hidden officials and salary-horses are activated by the interplay of clashes and combinations. Taking Jia day as the first example: the chart may show no obvious You, Xin or Chou positions for Proper Official, yet many Mao branches appear. Mao clashes You, and when Si and Chou also join, Si–You–Chou can form a metal bureau that quietly raises Xin as Proper Official for Jia. Similarly, for Yi days without visible Shen or Geng, the text describes structures where Yin clashes Shen and Zi–Chen combine or arch to create a place where the official star can be taken; for Wu days without Mao or Yi, repeated You clashing Mao and Hai–Wei combining Mao can draw out the hidden official; for Ji days without Yin or Jia, repeated Shen clashing Yin and Wu–Xu combining Yin can also wake officials from concealment. In all these cases the official star does not stand openly next to the day-stem, but is drawn out of a distant palace, a three-harmony bureau or another branch by active movement.
  
  The text further extends this thinking to patterns such as "reverse-clashing salary-horse" for Bing and Ding days, or "flying salary-horse" for Geng, Xin, Ren and Gui days, where salary positions are likewise brought into use through dynamic clashes and combinations. To qualify as high-grade, two conditions are stressed. First, the officials and salary-horses must initially be hidden and uninjured: if they are already exposed on the stems or damaged by killing and Hurting Officer, there is nothing special to wake up. Second, the branches that do the clashing must themselves be strong and well rooted, and after clashing they should meet combinations that seize and stabilise the released qi rather than letting it scatter or be dragged into other formations. When the month branch provides an official in seasonal command, the clash stars are robust and unentangled, and fortune cycles reinforce rather than attack these structures, such charts can indeed reach the level of ministers and generals. If one or more conditions fail, the pattern descends step by step to lesser nobility, mere comfort, or even toil and poverty when the same clashing forces turn into sources of conflict and loss.

- 核心要点：

  - 冲合禄马的共同特征是：**官星、禄马原伏隐，通过支神冲合而显**。
  - 甲、乙、戊、己等日的例子，说明可以通过不同的冲合路径暗起正官，只要官星不露、不破。
  - 丙丁倒冲禄马、庚辛壬癸飞天禄马，属于同一系列的“冲出/飞出禄马格”，格局较高，但成格条件严格。
  - 月令得官乘旺、冲神有力而不受羁绊，是判断能否“至将相公侯”的关键指标。

- 详细解说：

  古法论禄马，重视“位”与“势”：位者禄马所居之宫，势者冲合刑会之力。常规禄马格多是“禄在本宫、马在他宫”，以禄马同乡或禄马相逢为贵；而冲合禄马则偏重“以冲出对宫之禄马”，更具动态色彩。
  
  本节逐一举出甲、乙、戊、己四日的例子，说明即使命局中表面看不到官星，只要支神之间存在合局、冲出、刑出等关系，仍可暗中成官格。这与前文子遥巳禄、丑遥巳禄的思路一脉相承：都是从“隐而未发”的位置中，将官禄之气引出，再由合局摄住，使之为我所用。
  
  判断实际命局时，除需查证日主强弱、月令得失外，更需注意两点：其一，冲合之神若被岁运再冲再破，则原本的官禄格会大打折扣，甚至反成是非争竞之源；其二，若命局本不缺官，却再以冲合方式起官，反可能形成官煞混杂或争合之象，此时宜谨慎，不可见“冲合”二字便轻率论贵。
    - **校勘与字词辨析（双语）**：
    - 原文“丙丁二日即倒冲禄马格，庚辛壬癰四日即飞天禄马格”一句，把冲合禄马与其他两类禄马格联系起来，本稿据底本保留，只在释义中略加分类说明。
  - 文中举“明神宗：癸亥、辛酉、癸亥、辛酉”一命，以证飞天禄马之用，本稿保留原例，不对史实另作考证，仅视为古人命例佐证。
  - “冲禄元最紧”“冲禄则慢”属术语用语，本稿保留原文，将其理解为“冲禄力量强/弱”的区别，并在释义中统一解释。
  - **English**：
    - The phrase linking Bing-Ding to Inverted-Clash and Geng-Xin-Ren-Gui to Flying-Heaven patterns is preserved with classification notes.
    - The historical example of Emperor Shenzong is kept as classical evidence.
    - Terms "clash-salary tight/slow" are preserved and explained as strength differences.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_013]` `[trigger: 冲合禄马]` `[factor_trigger: chonghe_luma_presence]` `[role: 主干]` 柱无酉辛丑，有卯多冲酉，巳酉合丑为甲日正官。 → 《三命通会》卷六#冲合禄马
  - `[ns_smth_06_014]` `[trigger: 将相公侯]` `[factor_trigger: chongshen_yuhe AND bu_feng_jiban]` `[role: 主干依赖]` 冲神遇合，不逢羁绊，必登清贵将相公侯。 → 《三命通会》卷六#冲合禄马
  - `[ns_smth_06_015]` `[trigger: 冲禄最紧]` `[factor_trigger: ri_zhu_jianwang AND chonglu_jin]` `[role: 条件分支]` 甲寅、乙卯、丙午...以上十日本身健旺，冲禄元最紧。 → 《三命通会》卷六#冲合禄马
  - `[ns_smth_06_016]` `[trigger: 倒冲飞天]` `[factor_trigger: daochong_luma OR feitian_luma]` `[role: 总结]` 丙丁二日即倒冲禄马格，庚辛壬癸四日即飞天禄马格。 → 《三命通会》卷六#冲合禄马"""
    normalized_text_zh: str = """"""
    subject: str = "冲出禄马与官星的格局"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_8', 'bazi_semantic', 'new_candidate', 'bazi_semantic', 'bazi_state_qiangruo', 'bazi_semantic', 'bazi_condition_factor_135', 'bazi_semantic', 'source_ref', 'rel_smth_06_010', 'chonghe_luma_presence', 'rel_smth_06_011', 'chonglu_liliang', 'rel_smth_06_012', 'zhuwu_mingguan', 'evi_smth_06_010', 'chonghe_leixing', 'rule_chonghe', 'evi_smth_06_011', 'chonglu_liliang', 'rule_chonglu', 'evi_smth_06_012', 'zhuwu_mingguan', 'rule_wuminguan', 'map_smth_06_007', 'map_smth_06_008']
    
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
        l1_anchor="smth_v1.0.0_冲出禄马与官星的格局_001_L1",
    )
    version: str = "1.0.0"
