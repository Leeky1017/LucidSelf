"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.465654
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
    semantic_id="zpzq_v1.0.0_星辰与格局_不主成败_只作点缀_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 星辰与格局不主成败只作点缀(SemanticEntry):
    """
    - **原文（source_text）**：
  二十一、论星辰无关格局。
  八字格局，专以月令配四柱，至于星辰好歹，既不能为生克之用，又何以操成败之权？况于局有碍，即财官美物，尚不能济，何论吉星？...
    """
    
    original_text: str = """- **原文（source_text）**：
  二十一、论星辰无关格局。
  八字格局，专以月令配四柱，至于星辰好歹，既不能为生克之用，又何以操成败之权？况于局有碍，即财官美物，尚不能济，何论吉星？于局有用，即七煞伤官，何谓凶神乎？是以格局既成，即使满盘孤辰入煞，何损其贵？格局既破，即使满盘天德贵人，何以为功？今人不知轻重，见是吉星，遂致拋却用神，不管四柱，妄论贵贱，谬谈祸福，甚可笑也。

  况书中所云禄贵，往往指正官而言，不是禄堂人贵人。如正财得伤贵为奇，伤贵也，伤官乃生财之具，正财得之，所以为奇，若指贵人，则伤贵为何物乎？又若因得禄而避位，得禄者，得官也，运得官乡，宜乎进爵，然如财用伤官食神，运透官则格条，正官运又遇官则重，凡此之类，只可避位也。若作禄堂，不独无是理，抑且得禄避位，文法上下相顾。古人作书，何至不通若是！

  又若女命，有云“贵众，则舞裙歌扇”。贵众者，官众也，女以官为夫，正夫岂可叠出乎？一女众夫，舞裙歌扇，理固然也。若作贵人，乃是天星，并非夫主，何碍于众，而必为娼妓乎？

  然星辰命书，亦有谈及，不善看书者执之也。如“贵人头上带财官，门充驰马”，盖财官如人美貌，贵人如人衣服，貌之美者，衣服美则现。其实财官成格，即非贵人头上，怕不门充驰马！又局清贵，又带二德，必受荣封。若专主二德，则何不竟云带二德受两国之封，而秘先曰无煞乎？若云命逢险格，柱有二德，逢凶有救，右免于危，则亦有之，然终无关于格局之贵贱也。

- 原注（原文注解）：
  　　本章用较为犀利的语气，纠正一个常见误区：**八字格局的贵贱，根本不取决于“天乙贵人、文昌、华盖”等星辰，而在于月令用神配四柱的格局本身。**
  - 第一段总论：
    - 八字论格局，“专以月令配四柱”——以月令用神为纲，四柱生克为目；
    - 各种星辰好坏（吉星、凶星）本身既不能参与主干生克，也就无从操纵成败之权；
    - 若格局本身有碍，即使有再多“财官美物”，尚且难济，何况一点吉星名号？
    - 反之，若格局本身有用，即使见七煞、伤官这些在星辰系统中常被称为“凶神”的，也不妨其为用。
    - 结论是：格局既成，即使满盘孤辰寡宿之类，不损其贵；格局既破，即使满盘天德贵人之类，也难有实功。
  - 第二段举“禄贵、贵人”之例：
    - 古书所谓“禄贵”，往往指的就是“正官得禄”的情况，并非真有一个抽象“禄贵星”；
    - “正财得伤贵为奇”，贵的是伤官本身，因伤官为生财之具，正财得之能成奇局；若硬把“贵”归到贵人星上，则“伤贵”不成其意；
    - 又如“因得禄而避位”，所谓“得禄者，得官也”，本是说运到官乡，当以谨慎自处；若把“禄”当贵人星来解，把整句话拉成“得贵人反要避位”，则文句上下不贯，既悖原意又不合语法。
  - 第三段谈“女命贵众则舞裙歌扇”：
    - “贵众”指官星多，女命以官为夫，官多则夫多，舞裙歌扇乃一女众夫之喻；
    - 若误解为“贵人多则舞裙歌扇”，则把“官众”错读成“贵人多”，完全离题。
  - 最后一段承认星辰命书亦有其用，但强调：
    - 如“贵人头上带财官，门充驰马”，其理在于“财官为貌、贵人为衣”，吉局本在财官，用贵人只是点缀形象；
    - 又如“局清贵又带二德，必受荣封”，本是说格局清贵，再有二德相辅，则荣封更稳；若只抓“二德”而不论格局，便失去主次；
    - 若说“命逢险格，柱有二德，逢凶有救，免于危”，则属于“在险格中有救应”的范畴，仍然是围绕格局，而非纯凭星辰决定贵贱。

- 分字分词释义：
  - 星辰：在命书中指天乙、月德、天德、文昌、华盖、咸池等各类神煞星曜。
  - 格局：以月令用神为核心、四柱生克结构为骨架的整体命理构造。
  - 孤辰入煞：常见凶星组合名，在此作为“满盘凶星”的代称。
  - 天德贵人：传统吉星之一，主和气与救应。
  - 禄贵：多指“得禄之官”，即正官得禄位。
  - 禄堂：部分命书中虚构的“禄堂贵人”等说法。
  - 贵众：官星众多，女命以官为夫，故多官即多夫。
  - 舞裙歌扇：形容依附富贵、出入歌舞场所之象，原文用以比喻多夫。
  - 二德：天德、月德二星，常被视为救应之神。
  - 险格：结构险峻之格局，如煞刃、伤官七煞等。

- **规范化释义（primary_lang_explained）**：
  本章的目标，是把“星辰吉凶”从主角位置拉回配角位置：
  - 命局贵贱的根本在于格局；
  - 星辰只是“衣服与装饰”，可以增色，但不能代替骨架。

  作者先从原则上说：
  - 八字论格，只看月令用神和四柱生克；
  - 各种星辰无力改变主干五行的生克结构，自然难以“操成败之权”；
  - 若格局本身已破，再多吉星也难以挽救大局；
  - 若格局本身清贵，再多凶星点缀，也难以摧毁其根本。

  接着用“禄贵”“伤贵”等传统说法举反例：
  - “正财得伤贵为奇”，其实是在说伤官为贵，因为伤官是生财之具，让正财格中更具生机；
  - 若硬说“贵”在贵人星，而忽略伤官与财之间的实在生克关系，就会把整段话读得不伦不类；
  - 又如“得禄避位”，本意是“运到官乡，不宜再贪官”，属于格局与运的关系；
  - 若把“禄”当作独立星神，便会产生“得贵人反而要躲”的荒谬结论，与原文上下不成文理。

  对女命“贵众则舞裙歌扇”的说明，更是典型：
  - 女命以官星为夫星，官多固然多夫，出入歌舞场所也成象理所当然；
  - 若把“贵众”理解为贵人星多，则变成“贵人多则为娼”的怪论，与原意完全不符。

  最后一段承认：
  - 星辰命书并非全无可取，而在于“有人不善看书而执之”；
  - “贵人头上带财官，门充驰马”一句，是用“财官为貌、贵人为衣”来比喻：若财官格成，再有贵人、驿马点缀，其外在表现自然光鲜；
  - “局清贵又带二德必受荣封”亦然：局清贵是前提，二德只是锦上添花；
 - **完整对等诠释（secondary_lang_full）**：  
  Whether a life turns out noble or base is determined by the Month-Branch framework and the useful gods it carries, not by how many so-called auspicious or inauspicious stars are written on the chart. A structure that is clearly established remains noble even if the star names look fierce, while a broken framework stays lowly even if it is surrounded by many "nobleman" indicators. Terms such as "Lu" and "Gui" ultimately refer back to Officer-type configurations, and "many Gui" in a woman's chart means many Officer connections, not a crowd of nobleman stars turning her into a courtesan.

  - 在险格中见二德而“逢凶有救、免于危”，也仍然是在“险格框架下”的救应，并不改变格局本身的贵贱属性。

- 详细解说：
  - 命理体系中，“用神—格局”是骨架，“星辰—神煞”是衣饰：
    - 衣饰可以修饰与提示某些细节，但不能取代躯干；
    - 真正的高下贵贱，仍然要看骨架是否端正、气血是否流通。
  - 本章反对的，是把“好听的星名”当作决策依据的做法：
    - 见吉星就妄言贵、见凶星就妄言祸，完全不顾格局；
    - 为迎合“喜闻乐见”的心理，放弃严谨的格局判断。
  - 对现代工程化而言，本章的启示是：
    - 模型的核心特征应是用神与格局结构，星辰可以作为次级特征、解释性标签，而不能作为主要决策变量。

- 核心要点：
  - 先格局、后星辰：
    1) 先定月令用神与格局成败；
    2) 再看星辰吉凶如何“修饰”与“救应”；
    3) 切勿颠倒主次，以星辰取代格局。
  - 格局成而星多凶，不损其贵；格局破而星多吉，难挽其败。
  - “禄贵、伤贵、贵众”等旧语，多是格局用神的别称或格局结果的形容，不应被误读为抽象星辰。

- 应用推演：
  1) 在分析命局时，先完全不看星辰，只用用神与格局系统判断贵贱高下；
  2) 在此基础上，再添加星辰因素，解释“何以逢凶有救”“何以外在表现某些特征”；
  3) 对遇到大量“吉星”“凶星”而格局一般的命局，提醒自己：星为饰、格为骨，不可被星名带偏；
  4) 在系统实现中，将星辰类特征权重置于格局之后，避免模型被“星辰表象”主导决策。

- 反例与边界：
  - 只凭天乙、文昌、红鸾等星辰多寡判断贵贱，而不看格局结构；
  - 看到书中“禄贵”“贵众”等字样，便以为是“贵人星”多，而不理解其本意在官星与格局；
  - 完全否定星辰的存在价值，忽略其在“救应与细节解释”上的辅助作用。

- 小例（示意）：
  - 一命格局清贵，却兼带孤辰寡宿、亡神等凶星，实际人生中虽有情感孤独感，却不妨其事业与品级，这是“格成星凶而不损骨”的例子；
  - 另一命格局破败，却满盘吉星，现实中多有机会、资源的表象，却常常“有头无尾”“遇贵无成”，则是“星美而骨不立”的例证。

- 校勘与字词辨析：
  - “禄贵”“伤贵”“贵众”等词，在不同命书中写法不一，本精校依据上下文统一按“格局用神之别称”理解，并在此说明；
  - “门充驰马”“二德”“舞裙歌扇”等辞，在古籍中多有出现，本章主要用以比喻，不必逐字拘泥于星名列表.


- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_360]` `[trigger: 第20章要点]` `[factor_trigger: chapter=20 AND hexin_lunshu]` `[role: 主干]` 本章核心论述。 → 《子平真诠》#中卷第20章
  - `[ns_zpzy_361]` `[trigger: 星辰不论]` `[factor_trigger: shensha_xingchen AND bu_ru_zhengge_zhi_lun]` `[role: 主干]` 神煞星辰，不入正格之论。 → 《子平真诠》#中卷
  - `[ns_zpzy_362]` `[trigger: 辰戌丑未]` `[factor_trigger: branch IN (chen, xu, chou, wei) AND simu_ku]` `[role: 主干]` 辰戌丑未为四墓库。 → 《子平真诠》#中卷
  - `[ns_zpzy_363]` `[trigger: 冲开库门]` `[factor_trigger: chong_kai_kumen AND caiguan_shi_xian]` `[role: 主干]` 冲开库门，财官始显。 → 《子平真诠》#中卷
  - `[ns_zpzy_364]` `[trigger: 库中藏干]` `[factor_trigger: kuzhong_canggan AND tougan_fang_yong]` `[role: 主干]` 库中藏干，透干方用。 → 《子平真诠》#中卷
  - `[ns_zpzy_365]` `[trigger: 吉神太过]` `[factor_trigger: jishen_tai_guo AND fan_cheng_qi_hai]` `[role: 主干]` 吉神太过，反成其害。 → 《子平真诠》#中卷
  - `[ns_zpzy_366]` `[trigger: 凶神得用]` `[factor_trigger: xiongshen_deyong AND fan_cheng_qi_fu]` `[role: 主干]` 凶神得用，反成其福。 → 《子平真诠》#中卷
  - `[ns_zpzy_367]` `[trigger: 财旺克印]` `[factor_trigger: cai_wang_ke_yin AND xueye_nan_cheng]` `[role: 主干]` 财旺克印，学业难成。 → 《子平真诠》#中卷
  - `[ns_zpzy_368]` `[trigger: 官旺生印]` `[factor_trigger: guan_wang_sheng_yin AND guiqi_tiancheng]` `[role: 主干]` 官旺生印，贵气天成。 → 《子平真诠》#中卷
  - `[ns_zpzy_369]` `[trigger: 印旺生身]` `[factor_trigger: yin_wang_sheng_shen AND shen_qiang_neng_ren]` `[role: 主干]` 印旺生身，身强能任。 → 《子平真诠》#中卷
  - `[ns_zpzy_370]` `[trigger: 喜神来助]` `[factor_trigger: xishen_laizhu=true AND result=shishi_shunsui]` `[role: 主干]` 喜神来助，事事顺遂。 → 《子平真诠》#中卷
  - `[ns_zpzy_371]` `[trigger: 天干主动]` `[factor_trigger: tiangan_zhu_dong AND ying_su_er_xian]` `[role: 主干]` 天干主动，应速而显。 → 《子平真诠》#中卷"""
    normalized_text_zh: str = """"""
    subject: str = "星辰与格局：不主成败，只作点缀"
    factor_refs: list = []
    
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
        l1_anchor="zpzq_v1.0.0_星辰与格局_不主成败_只作点缀_001_L1",
    )
    version: str = "1.0.0"
