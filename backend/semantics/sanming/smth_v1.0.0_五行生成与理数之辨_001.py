"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227407
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
    semantic_id="smth_v1.0.0_五行生成与理数之辨_001",
    book_id="sanming",
    engine_id="bazi"
)
class 五行生成与理数之辨(SemanticEntry):
    """
    - **原文（source_text）**：
  耕野子日：天一气尔，气化生水，水中滓浊，积而成土，水落士出，遂成山川。土之刚者成石，而金生焉；土之柔者生木，而火生焉。五行具，万物生，而变化无穷矣。浚...
    """
    
    original_text: str = """- **原文（source_text）**：
  耕野子日：天一气尔，气化生水，水中滓浊，积而成土，水落士出，遂成山川。土之刚者成石，而金生焉；土之柔者生木，而火生焉。五行具，万物生，而变化无穷矣。浚川子曰：天地之初，惟有阴阳二气而巳。阳则化火，阴则化水，水之渣滓，便结成地，潘滓成地，即土也，何至天五方言生土？水、火土，天地之大化，金木者，三物之所自出。金石之质，必积久而后结，生之必同于人物，谓金之气生人，得乎哉？且天地之间，无非元气之所为，其性其种，己各具。太始之先，金有金之种，木有木之种，人有人之种，物有物之种，各各完具，不相假借，不相凌犯，而谓五行递互相生，可乎？今五行家以金生水，厥类悬绝不侔，厥理颠倒失次。不知木以火为气，以水为滋，以土为宅，此天然至道。而曰水生木无土，将附木于何所？水多火灭土绝，木且死矣，夫安能生？周子惑于五行家之说，而谓五气顺布，四时行焉。不知日有进退，乃成寒暑，寒暑分平，乃成四时，于五气之布何与焉？其日春木夏火，秋金冬水，皆假合之论。土无所归，配于四季。不知土之气在天地内，何口不然，何处不有，何止流行于季月之晦？季月之晦尚有，而孟月之朔即灭，其灭也归于何所，其来也孰？为命之天一生水，乃纬书之辞，而儒者拔以入经。水火者，阴阳始生之妙物也，故一化而为火，日是也；再化而为水，雨露是也。今日天一生水，地二生火，戾于造化本然之妙，可乎？其折朱子以四时流行之气论五行，天地奇偶之数论五行，太极图阳变阴合而生水、火、木、金、土论五行。其折五行配四时，如五行家四时各主其一，舂止为木，则水火土金之气孰绝灭之？秋止为金，则水火土木之气孰留停之？土惟旺于四季，则余月之气，孰把而不使之运？又安有今日为木，明日为火，又明日为土、为金、为水乎？按王氏之说有理，而非达观之见。珞录子日以为有也，是从无而立有；以为无也，关垂象以示文。夫天凭日月五星三垣二十八宿之象，观天王会通，其立名分野，是亦人为之耳，而义象符合。至灾祥占上，或属类某事，或指见某方，应于某年月日，如探左契。虽天道玄远，亦不外人事与五行。阴阳家以十干十二支分为五行，因目凄甬会，橹与天会而为岁，月与曰会而为月。日有三十，时有十二，以人生年月日时所得干攴，立为四柱，以推一生吉匈，亦理之自然者也。王氏以春属木，而土何在？不知五行旺相、死休囚，各主其当时不当时，用事不用事而言，非为春木旺而土则无。十干十二支，错综为六十甲子，周而复始，不假安排，即造化之所在也，非为今日属木，明口属火，便非天道之自然。不思人立而天从之，人感而天应之，即天象立名分野之义天。人合一之道也。观一日有早午晏晚，自有温凉寒热气候，是金木水火土备于一口，五行之不相离如此，谓今日木，明日火，又何莫而非天道之自然也耶？且朝廷造历，颁之天下，其载一年三百六十五日，中间一年之神煞方位，每月之天行德旺，而一日之中，文有黑黄吉凶事之宜与不宜人，遵之则福，违之则祸，是果无理强造，而率天下以必从哉？又相人术，观气色之青黄赤白黑，而决祸福，应于某年月日时，青则甲乙，黄则戊巳，赤则丙丁，白则庚辛，黑则壬癸，一亳不爽，察病亦然，观《素问》可见。是干支虽所以纪目，而造化不外是也。又人之精神梦寐，预兆吉凶，占之者或以意断，或以物象，或以字解，或以音叶，皆人为之耳，正肯曾妄之耳也，而吉凶不能外焉。是有是人而后有是梦，因是梦而求是人，造化且不外，而况干支五行，自有天地，便有此理，因有此理，便生是人。人与天一也。外人以言天，外天以言人，皆诬矣。若伏羲画卦，仰观俯察，远稽近取，是得天地人物之理，而八卦所由作也。今之谈阴阳者，虽穷极天地之变，探索人物之微，彰往察来，因著知微，与天地合其德，与日月合其明，与四时合其序，与鬼神合其吉凶，亦岂能外干支五行，而别有造化，以尽天地人物之大哉？今王氏知尊易而不信阴阳家说，是知有理而不知有数也。理数合一，天人一理，神而明之，存乎其人焉耳。

- **规范化释义（primary_lang_explained）**：
  此段一方面说明五行在宇宙生成中的次序：大略自水、土而金木火具备；另一方面则批评当时流行的「金生水」「春木夏火、秋金冬水」等机械配属。作者强调：土之气遍在天地，不限于四季末月；水火之化也不只是「天一生水、地二生火」几个数字可以概括。若只是搬弄数字，而忘记天地寒暑进退、节气运行与人事应感，那么所谓五行之学就失去了根本。真正的命理，是在观察天地运行、人与天感应之中，体会理与数如何统一。

- **完整对等诠释（secondary_lang_full）**：

  This paragraph does two things at once. First, it sketches a natural sequence in which Water and Earth appear before the other elements and give rise to Metal, Wood and Fire. Second, it criticises the mechanical doctrines then in fashion, such as the slogan "Metal generates Water" or the simplistic assignment "Spring‑Wood, Summer‑Fire, Autumn‑Metal, Winter‑Water". Earth‑qi, the author insists, pervades the whole cosmos and is not confined to the last month of each season; the transformations of Water and Fire cannot be reduced to numerological formulas like "Heaven‑One produces Water, Earth‑Two produces Fire". If we only juggle numbers and ignore real cold and heat, seasonal shifts and human responses, then Five‑Element study loses its foundation. Authentic destiny work observes how heaven and earth actually move and how people resonate with them, and only then asks how principle and number line up.

- **分字分词释义**：
  - **金生水**：流行口诀，将其理解为物质性生成是误读，应视为象征性关联。
  - **假合之论**：牵强附会的机械配属，如春木夏火秋金冬水等死法。
  - **土无所归**：土气遍在，不专主一时，批评将土局限于季月末的说法。
  - **理数合一**：天道之「理」与推算之「数」不可分离，数是理的载体。

- **核心要点**：
  - 不能把「金生水」「春木夏火」之类口诀当作绝对真理，而须放回天地寒暑、节气进退的大背景里理解；
  - 干支纪日虽然是「数」，但背后承载的是天地运行之「理」，二者不可分裂；
  - 命局中的五行配置，要同时参考：天时（节气历法）、地利（环境方位）、人事（行藏善恶）。

- **应用推演（操作顺序）**：
  1) 在作命局分析或算法设计时，将「数」视为载体、「理」视为约束：任何数字化规则都要接受现实气候、地理、人事数据的检验；
  2) 读经典时，对「金生水」「土旺四季」等语句做情境化处理：标注其成说的历史背景与使用场景，而不是一概硬套到所有时代与地区；
  3) 建立「三元信息」的数据结构：将同一五行的象意分拆为「自然层（物候与气候）」「人事层（职业、关系、事件）」「修为层（德行与心理）」三层，分别建模，再由逻辑将其合一；
  4) 推运时，引入真实环境变量（行业周期、地区气候、社会制度等），以此修正单纯从干支数列推出来的结果，使「理与数」更贴近当下实际；
  5) 在知识库中为每一条口诀附上「适用边界」，并在推理引擎中把这些边界当作前置条件，而不是默认全局有效。

- **反例与边界**：
  - 完全依赖「数」而不理会现实，例如仅根据大运流年干支便断定金融危机、天灾人祸，而不参考已有的经济与气象数据；
  - 反过来，只看现实数据，完全抛弃干支与五行结构，使命理沦为一般统计学，也违背本段强调的「理数统一」；
  - 把「金生水」当作物理成因来理解，好像金属真的会生出水来，而不是把它看成某种现象与结构的象征语言；
  - 在工程实现中，若把所有经典语句都当作等权规则堆叠，而不考虑其相互冲突时的优先级与适用条件，容易导致系统输出互相矛盾的结论。

- **小例（示意）**：
  - 在设计自动断命系统时，对「金生水」设置为：仅在特定格局与节气下，用于提示「金气清、可导水气」这一类象，并要求同时满足现实中与金、水相关的职业或环境线索，方可触发相应断语；
  - 对「土旺四季」则规定：只有在处于季月、且现实环境确有「土性」特征（如基建、地产、资源型行业）时，才增强土的权重；反之则按常态权重处理。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_026]` `[trigger: 五行各具其种]` `[factor_trigger: wuxing_generation=each_has_seed]` `[role: 主干]` 金有金之种，木有木之种，人有人之种，物有物之种，各各完具，不相假借。 → 《三命通会》卷一#五行生成条
  - `[ns_smth_027]` `[trigger: 土气遍在]` `[factor_trigger: earth_omnipresence=not_limited_season]` `[role: 主干依赖]` 土之气在天地内，何处不有，何止流行于季月之晦？ → 《三命通会》卷一#五行生成条
  - `[ns_smth_028]` `[trigger: 假合之论]` `[factor_trigger: mechanical_view=false_combination]` `[role: 反例]` 其曰春木夏火，秋金冬水，皆假合之论。 → 《三命通会》卷一#五行生成条
  - `[ns_smth_029]` `[trigger: 理数统一]` `[factor_trigger: unity_principle_number=inseparable]` `[role: 主干]` 惟其理与数合，故当其可，则有不容不然者。 → 《三命通会》卷一#五行生成条
  - `[ns_smth_675]` `[trigger: 道]` `[factor_trigger: dao]` `[role: 主干]` 道为阴阳之本源。 → 《三命通会》卷一
  - `[ns_smth_676]` `[trigger: 倒冲二日类型]` `[factor_trigger: daochong_erri_leixing]` `[role: 条件分支]` 倒冲二日类型定凶吉。 → 《三命通会》卷一
  - `[ns_smth_677]` `[trigger: 刀石格有无]` `[factor_trigger: daoshi_ge_presence]` `[role: 条件分支]` 刀石格有无定格局。 → 《三命通会》卷一
  - `[ns_smth_678]` `[trigger: 倒药旺身]` `[factor_trigger: daoyao_wangshen]` `[role: 条件分支]` 倒药旺身主化解。 → 《三命通会》卷一
  - `[ns_smth_679]` `[trigger: 衍生因子]` `[factor_trigger: derived_factor]` `[role: 条件分支]` 衍生因子为延伸因素。 → 《三命通会》卷一
  - `[ns_smth_680]` `[trigger: 得时]` `[factor_trigger: deshi]` `[role: 条件分支]` 得时主旺相。 → 《三命通会》卷一
  - `[ns_smth_681]` `[trigger: 得时成局]` `[factor_trigger: deshi_chengju]` `[role: 条件分支]` 得时成局主有力。 → 《三命通会》卷一
  - `[ns_smth_682]` `[trigger: 得时旺相]` `[factor_trigger: deshi_wangxiang]` `[role: 条件分支]` 得时旺相主强盛。 → 《三命通会》卷一
  - `[ns_smth_683]` `[trigger: 得意分散]` `[factor_trigger: deyi_fensan]` `[role: 条件分支]` 得意分散主不专。 → 《三命通会》卷一
  - `[ns_smth_684]` `[trigger: 日间天气特征]` `[factor_trigger: diurnal_weather_profile]` `[role: 条件分支]` 日间天气特征影响命局。 → 《三命通会》卷一
  - `[ns_smth_685]` `[trigger: 帝旺相]` `[factor_trigger: diwang_xiang]` `[role: 条件分支]` 帝旺相主极盛。 → 《三命通会》卷一
  - `[ns_smth_686]` `[trigger: 地支辰有无]` `[factor_trigger: dizhi_chen_presence]` `[role: 条件分支]` 地支辰有无定土库。 → 《三命通会》卷一
  - `[ns_smth_687]` `[trigger: 地支丑有无]` `[factor_trigger: dizhi_chou_presence]` `[role: 条件分支]` 地支丑有无定金库。 → 《三命通会》卷一
  - `[ns_smth_688]` `[trigger: 地支亥有无]` `[factor_trigger: dizhi_hai_presence]` `[role: 条件分支]` 地支亥有无定水局。 → 《三命通会》卷一
  - `[ns_smth_689]` `[trigger: 地支亥寅午组合]` `[factor_trigger: dizhi_hai_yin_wu_set]` `[role: 条件分支]` 地支亥寅午组合定格局。 → 《三命通会》卷一
  - `[ns_smth_690]` `[trigger: 地支节当]` `[factor_trigger: dizhi_jiedang]` `[role: 条件分支]` 地支节当主应时。 → 《三命通会》卷一
  - `[ns_smth_691]` `[trigger: 地支卯有无]` `[factor_trigger: dizhi_mao_presence]` `[role: 条件分支]` 地支卯有无定木位。 → 《三命通会》卷一
  - `[ns_smth_692]` `[trigger: 地支卯午亥组合]` `[factor_trigger: dizhi_mao_wu_hai_set]` `[role: 条件分支]` 地支卯午亥组合定格局。 → 《三命通会》卷一
  - `[ns_smth_693]` `[trigger: 地支卯子申组合]` `[factor_trigger: dizhi_mao_zi_shen_set]` `[role: 条件分支]` 地支卯子申组合定格局。 → 《三命通会》卷一
  - `[ns_smth_694]` `[trigger: 地支申亥卯组合]` `[factor_trigger: dizhi_shen_hai_mao_set]` `[role: 条件分支]` 地支申亥卯组合定格局。 → 《三命通会》卷一
  - `[ns_smth_695]` `[trigger: 地支申有无]` `[factor_trigger: dizhi_shen_presence]` `[role: 条件分支]` 地支申有无定金位。 → 《三命通会》卷一
  - `[ns_smth_696]` `[trigger: 地支巳有无]` `[factor_trigger: dizhi_si_presence]` `[role: 条件分支]` 地支巳有无定火位。 → 《三命通会》卷一
  - `[ns_smth_697]` `[trigger: 地支巳申子组合]` `[factor_trigger: dizhi_si_shen_zi_set]` `[role: 条件分支]` 地支巳申子组合定格局。 → 《三命通会》卷一
  - `[ns_smth_698]` `[trigger: 地支未有无]` `[factor_trigger: dizhi_wei_presence]` `[role: 条件分支]` 地支未有无定木库。 → 《三命通会》卷一
  - `[ns_smth_699]` `[trigger: 地支午有无]` `[factor_trigger: dizhi_wu_presence]` `[role: 条件分支]` 地支午有无定火位。 → 《三命通会》卷一"""
    normalized_text_zh: str = """"""
    subject: str = "五行生成与理数之辨"
    factor_refs: list = ['unity_principle_number', 'wuxing_generation', 'false_combination', 'earth_omnipresence']
    
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
        l1_anchor="smth_v1.0.0_五行生成与理数之辨_001_L1",
    )
    version: str = "1.0.0"
