"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.465589
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
    semantic_id="zpzq_v1.0.0_四墓杂气与_刑冲开库_之辨_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 四墓杂气与刑冲开库之辨(SemanticEntry):
    """
    - **原文（source_text）**：
  十七、论墓库刑冲之说。
  辰戌丑未，最喜刑冲，财官入库，不冲不发——此说，虽俗书盛称之，然子平先生造命，无是说也。夫杂气透干会支，岂不甚美？又何劳刑...
    """
    
    original_text: str = """- **原文（source_text）**：
  十七、论墓库刑冲之说。
  辰戌丑未，最喜刑冲，财官入库，不冲不发——此说，虽俗书盛称之，然子平先生造命，无是说也。夫杂气透干会支，岂不甚美？又何劳刑冲乎？假如甲生辰月，戊土透，岂非偏财？申子会，岂非印绶？若戊土不透，即辰戌相冲，财格犹不甚清也。至于透壬为印，辰戌相冲，将以累印，谓之冲开印库，可乎？

  况四库之中，虽五行俱有，而终以土为主。土冲则灵，金木水火，岂取胜以四库之冲而动乎？故财官属土，冲则库启，如甲用戊财而辰戌冲，壬用己官而丑未冲之类是也。然终以戊己干头为清用，干既透，即不冲而亦得也。至于财官为水，冲则反累，如己生辰月，壬透为财，戌冲，则劫动，何益之有？丁生辰月，透壬为官，戌冲，则伤官，岂能无害？其可谓之逢冲而壬水之财库官库开乎？

  今人不知此理，甚有以出库为投库。如丁生辰月，壬官透干，不以为库内之壬干头透出，而反为干头之壬逢辰入库，求戌以冲土，不顾其官之伤。更有可笑者，月令本非四墓，别有用神，年月日时中一带四墓，便求刑冲；日临四库，不以为身坐库根，而以为身主入库，求冲以解。种种谬论，令人掩耳。

  然亦有逢冲而发者，何也？如官最忌冲，而癸生辰月，透戊为官，与戌相冲，不见破格；四库喜冲，不为不足。却不知子午卯酉之类，二者相仇，乃冲克之冲；而四墓土自为冲，乃冲动之冲，非冲克之冲也。然既以土为官，何害于事乎？

  是故四墓不忌刑冲，刑冲未必成格，其理甚明，人自不察耳。

- 原注（原文注解）：
  　　本章专门驳正坊间流行的“墓库刑冲开库”之说，重点在于：
  - 四墓（辰戌丑未）本为杂气之库，其美在于“杂气透干会支”，而不在于“必须刑冲开库”；
  - 俗书所谓“财官入库，不冲不发”，在子平原法中并无其说；
  - 真正重要的是：
    - **库中之用神是否透干成用？**
    - **支间会局是否使杂气成清格？**
    - **刑冲到底是“冲动”还是“冲克”？冲到谁？**

  于是作者分几步加以澄清：
  1) 以甲生辰月为例：
     - 若辰中戊土透干，即成偏财，用不在“冲库”而在“透干”；
     - 若支中申子会局成水，又成一层印绶；
     - 若戊不透、壬为印透干，辰戌相冲反累印，岂可说是“冲开印库”？
  2) 说明四库“以土为主”的性质：
     - 四库虽兼五行，然终以土为主；
     - 土冲则灵，金木水火并非靠库冲动才有力量；
     - 财官若本属土，冲动土库可视作“动用”，但前提仍在干透成用。
  3) 警告对“水财、水官入库”的误用：
     - 若财官为水，如己生辰月壬透为财，戌冲则劫动；
     - 丁生辰月壬透为官，戌冲则伤官——这一类冲反而破格，绝非“冲开财库官库”。
  4) 批评“出库当投库”“一带四墓求冲”的谬论：
     - 有人将干上透出的库中之神当作“投库”，反求冲库以“解出”，完全忽略冲克本身对用神的伤害；
     - 有人见年月日时中多见四墓，便到处求刑冲，不论月令用神所依为何，皆属本末倒置。
  5) 最后指出：
     - 四墓“喜冲”指的是土气被冲动，有时能发挥作用；
     - 但须分清：子午卯酉等为“冲克之冲”，四墓自互冲多为“冲动之冲”；
     - 若以土为官，土之冲动未必坏事；若以水为财官，却被冲动之土牵连，往往是坏事。

- 分字分词释义：
  - 四墓（四库）：辰、戌、丑、未四支，既是“库”，亦称“墓”，为气之收藏处。
  - 杂气：辰中藏戊癸乙、戌中藏戊辛丁等，一支之内多干杂处，故名杂气。
  - 财官入库不冲不发：俗说，认为财官入库必须刑冲才能“发”；本章明确否定之。
  - 杂气透干会支：库中所藏之干透出天干，支间又会局成势，是成格的关键。
  - 冲气：四墓自相冲动，激发库中之气运转。
  - 冲克：如子午、卯酉相冲，带有强烈克伐之意。
  - 出库 / 投库：俗命书用语，将干透之库中神当作“出库”；误把行运遇库视作“投库”。
  - 库启：库中气机被调动、发动之意，不等同于“冲破”。
  - 月劫用官：以月令劫财为用或为辅助，而官星为主用者之格局。
 
- **规范化释义（primary_lang_explained）**：
  本章的核心，是提醒我们**不要简单以“冲库开库即发”为判断依据**，而应回到“杂气透干会支”的原理，看用神是否真正得力。

  作者首先指出：“辰戌丑未最喜刑冲，财官入库不冲不发”这一说法，在俗命书中流行甚广，但在子平原法中并无此语。真正美妙的，是四墓中杂气能透干、能会支，成其清格，而不是靠刑冲硬“打开”库门。

  于是以甲生辰月为例：
  - 若辰中戊土透干，偏财已“出库”成用，不需再用辰戌相冲；
  - 若支成申子会局为水，又可成一层印绶，亦不仰赖库冲；
  - 若戊不透而壬透为印，此时辰戌相冲，实际上是冲击印星，反而累印，怎可说是“冲开印库”？

  接着说明四库“终以土为主”的性质：
  - 四库虽含五行之气，但主轴在土；
  - 土被冲动，金木水火并非因此自然得力；
  - 若用神正好是戊己土（如甲用戊财、壬用己官），冲动土库有时可视为“库启”，但前提仍然在戊己透干为清用，冲只是一种“动用”之象，而非成格之本；
  - 若财官为水，如己生辰月壬透为财、丁生辰月壬透为官，戌冲则只会激发劫财或伤官之力，破坏原有结构，绝不能称为“开财库”或“开官库”。

  然后作者批评两类常见误解：
  - 一类是“出库当投库”：
    - 如丁生辰月，壬官透干，按理应视为库中之壬已从辰透出为官；
    - 有人却把它当成“干头壬再入辰库”，硬求戌冲土来“开库”，不顾辰戌冲对官星本身的损伤，这是颠倒因果。
  - 另一类是“一带四墓、遍求刑冲”：
    - 月令本非四墓而另有用神，只因其它柱多见辰戌丑未，便误以为“满盘皆库”，到处寻找刑冲；
    - 日元坐库，本是“身坐根”的象征，却被说成“入墓须冲”，要靠刑冲才算“解困”，同样是严重误读。

  末段承认“亦有逢冲而发”的例子，但马上加以界定：
  - 癸生辰月、戊透为官，与戌相冲并未破格，可说是“库喜冲”；
  - 这里所谓“喜冲”的，是四墓土本身被冲动，而非官星被克伤；
  - 子午卯酉之间是“冲克之冲”，多主互相克伐；四墓之间多属“冲动之冲”，偏于激发库中土气；
  - 若土本为官星，被适度冲动未必为害；若用神在水而土被冲激，则往往牵累水，用神反受其害。

- **完整对等诠释（secondary_lang_full）**：  
  This chapter challenges the popular slogan that the Four Tomb branches "like" to be clashed and that Wealth or Officer stored there will never manifest unless the storehouse is "opened" by collision. In authentic Ziping method, the beauty of Chen, Xu, Chou and Wei lies in their mixed qi emerging cleanly through stem transparency and branch assemblies, not in violent clashes. Using the example of a Jia Day Master born in a Chen month, the author explains that if the hidden Wu Earth in Chen has already surfaced as a Wealth stem, and if the branches further assemble a water bureau to support Resource, then the pattern is already complete—there is no need to rely on a Chen–Xu clash. If Wu does not surface and Ren appears instead as Resource, a Chen–Xu clash simply batters that Resource rather than "opening an ink store"; what is really being struck is the Useful God itself.

  The text then stresses that, although the Four Tombs contain all five elements, they are in essence Earth. When Earth itself is the Useful God (for example, Wu or Ji acting as Wealth or Officer), moderate activation of Tomb Earth by mutual clashes can sometimes be read as "storage being stirred" and timing being triggered—but even then, the root requirement is that Earth has already emerged clearly in the stems. Clashes cannot create usefulness out of nothing. By contrast, when Water is the Wealth or Officer, having Tomb Earth branches collide usually just awakens Rob Wealth or Hurting Officer factors and drags down the Water we rely on. Treating every appearance of Tomb branches in the chart or in transits as if the whole life is "locked in a storehouse that must be broken open" is therefore a serious misunderstanding: a Day Master sitting on a Tomb is normally sitting on roots, not being buried alive. The author distinguishes carefully between clashes that merely move Earth qi within the Tomb system and clashes that actively attack the Useful God, urging readers to return to concrete stem–branch structure—who is hidden, who has surfaced, and who is actually being clashed—instead of worshipping the vague idea of "opening the storehouse".

- 详细解说：
  - 本章进一步打破“神煞名称决定吉凶”的迷思：
    - 四墓杂气的用法，与前一章“杂气取用”的思想相连：
    - 真正的关键不在“冲不冲”，而在“透不透”“会不会”“有情无情”；
    - 刑冲只是动态变化的一种形式，不应被神化为“开库发福”的万能钥匙。
  - “冲气”与“冲克”的区分极为重要：
    - 冲气：同类之气相互振动，使库中之气运转，多见于四墓互冲；
    - 冲克：不同五行相互克伐，多见于子午、卯酉等正冲.
  - 真正值得关注的“逢冲而发”，多半有前提：
    - 原局用神已透干成用，冲只是增加动象或推动原有格局兑现；
    - 或冲动的是忌神、劫财等，使其由静转动，减轻其危害。

- 核心要点：
  - 观察四墓之冲，须回答三问：
    1) 库中何神为用？是否已透干或会局？
    2) 刑冲所达之处，是用神、相神，还是忌神、杂气？
    3) 此冲属“冲气”还是“冲克”？
  - 四墓“喜冲”，应理解为“土气宜动”，而非“非冲不发”；
  - 对一切“出库、投库、开库”之类术语，均应回到具体干支结构来重新审视。

- 应用推演：
  1) 遇到辰戌丑未为月令时，先按前章方法确定杂气中哪一干为用；
  2) 检查干支是否已透出此用神或形成会局，评估其清浊；
  3) 再查看命局与岁运中的刑冲，标记冲到的支位与其中十神属性；
  4) 对冲用神与相神的情形，视为潜在破格点；对冲忌神或劫财的情形，则视情况可能转吉；
  5) 不因见“库与库相冲”就自动判为“开库而发”，而要结合透干、会局与有情无情综合判断。

- 反例与边界：
  - 见财官入库即断“非冲不发”，忽视库中用神早已透干成用；
  - 把日坐四库一概视作“入墓”，不分身有根与身困乏；
  - 把四墓互冲与子午卯酉互冲混为一谈，不分冲气与冲克；
  - 见少数“逢冲而发”命例就上纲成普遍规律，不看前后条件。

- 小例（示意）：
  - 一命甲生辰月，戊透为偏财、申子会为印，虽辰戌相冲，冲动的主要是库中土气而非用神本身，运至冲辰之岁，不过财印更为忙碌，而非所谓“忽然发财”；
  - 另一命己生辰月，壬透为财，戌冲则劫动，若运再行比劫，财来财去、终难积累，就是“误把冲库当发库”的典型反例。

- 校勘与字词辨析：
  - 原文中对“财官入库不冲不发”的说法，明显以俗说为靶子，本精校在释义中将作者反驳的逻辑展开，以免断章取义；
  - “子午卯酉之类，二者相仇，乃冲克之冲，而四墓土自为冲，乃冲动之冲”一句，为全章要领所在，建议读者熟记，以利后文对刑冲的进一步理解。


- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_312]` `[trigger: 墓库真义]` `[factor_trigger: branch IN (chen, xu, chou, wei) AND muku=true AND tougan_huizhi_sheng_yu_xingchong]` `[role: 主干]` 辰戌丑未四墓库，透干会支胜于刑冲。 → 《子平真诠·论墓库刑冲之说》#墓库
  - `[ns_zpzy_313]` `[trigger: 透干取用]` `[factor_trigger: zaqi_tougan_huizhi AND qibu_shenmei AND heyao_xingchong]` `[role: 主干]` 杂气透干会支岂不甚美，又何劳刑冲？ → 《子平真诠·论墓库刑冲之说》#透干
  - `[ns_zpzy_314]` `[trigger: 冲库有别]` `[factor_trigger: (caiguan_shutu AND chong_ze_ku_qi) OR (caiguan_shu_shui AND chong_ze_fan_lei)]` `[role: 主干]` 财官属土冲则库启，属水冲则反累。 → 《子平真诠·论墓库刑冲之说》#冲库
  - `[ns_zpzy_315]` `[trigger: 杂气透干]` `[factor_trigger: zaqi_yueling AND tougan_huizhi AND fang_neng_cheng_ge]` `[role: 主干]` 杂气月令，透干会支方能成格。 → 《子平真诠·论墓库刑冲之说》#杂气
  - `[ns_zpzy_316]` `[trigger: 库门开启]` `[factor_trigger: zaqi_feng_chong AND kumen_fang_kai]` `[role: 主干]` 杂气逢冲，库门方开。 → 《子平真诠·论墓库刑冲之说》#开库
  - `[ns_zpzy_317]` `[trigger: 库冲之辨]` `[factor_trigger: simu_feng_chong AND xu_bian_ku_kai_ku_bi]` `[role: 主干]` 四墓逢冲，须辨库开库闭。 → 《子平真诠》#中卷
  - `[ns_zpzy_318]` `[trigger: 冲开库门]` `[factor_trigger: chong_kai_kumen AND caiguan_shi_xian]` `[role: 主干]` 冲开库门，财官始显。 → 《子平真诠》#中卷
  - `[ns_zpzy_319]` `[trigger: 库中藏干]` `[factor_trigger: kuzhong_canggan AND tougan_fang_yong]` `[role: 主干]` 库中藏干，透干方用。 → 《子平真诠》#中卷
  - `[ns_zpzy_320]` `[trigger: 刑冲破害]` `[factor_trigger: xingchong_pohai AND ge_you_qingzhong]` `[role: 主干]` 刑冲破害，各有轻重。 → 《子平真诠》#中卷
  - `[ns_zpzy_321]` `[trigger: 墓库收藏]` `[factor_trigger: muku_shoucang AND xu_chongkai_fang_xian]` `[role: 主干]` 墓库收藏，须冲开方显。 → 《子平真诠》#中卷
  - `[ns_zpzy_322]` `[trigger: 辰为水库]` `[factor_trigger: chen=shuiku AND feng_chong_ze_shui_yi]` `[role: 主干]` 辰为水库，逢冲则水溢。 → 《子平真诠》#中卷
  - `[ns_zpzy_323]` `[trigger: 戌为火库]` `[factor_trigger: xu=huoku AND feng_chong_ze_huo_wang]` `[role: 主干]` 戌为火库，逢冲则火旺。 → 《子平真诠》#中卷
  - `[ns_zpzy_324]` `[trigger: 丑为金库]` `[factor_trigger: chou=jinku AND feng_chong_ze_jin_xian]` `[role: 主干]` 丑为金库，逢冲则金显。 → 《子平真诠》#中卷
  - `[ns_zpzy_325]` `[trigger: 格成格破]` `[factor_trigger: (gecheng=true AND result=ji) OR (gepo=true AND result=xiong)]` `[role: 主干]` 格成则吉，格破则凶。 → 《子平真诠》#中卷
  - `[ns_zpzy_326]` `[trigger: 日主强弱]` `[factor_trigger: rizhu_qiangruo AND ding_geju_zhi_ji]` `[role: 主干]` 日主强弱，定格局之基。 → 《子平真诠》#中卷"""
    normalized_text_zh: str = """"""
    subject: str = "四墓杂气与“刑冲开库”之辨"
    factor_refs: list = ['four_tombs', 'mixed_qi', 'tougan', 'huizhi', 'chong_movement', 'chong_control', 'kuqi', 'chuku']
    
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
        l1_anchor="zpzq_v1.0.0_四墓杂气与_刑冲开库_之辨_001_L1",
    )
    version: str = "1.0.0"
