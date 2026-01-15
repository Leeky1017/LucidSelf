"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559541
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
    semantic_id="yhzp_v1.0.0_四言独步_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 四言独步(SemanticEntry):
    """
    - **原文（source_text）**：  
  四言独步。  
  先天何处，后天何处，要知来处，便知去处；四柱排定，三才次分，年干为本，配合元辰；神煞相绊，轻重较量，先观月令，论格推详；以日为...
    """
    
    original_text: str = """- **原文（source_text）**：  
  四言独步。  
  先天何处，后天何处，要知来处，便知去处；四柱排定，三才次分，年干为本，配合元辰；神煞相绊，轻重较量，先观月令，论格推详；以日为主，专论财官，分其贵贱，妙法多端；独则易取，乱则难明，去留舒配，论格要精。日主高强，月提得令；用财为物，表实为正。年根为主，月令为中；日生百刻，时旺时空。干与支同，损财伤妻。身支年同，破荡祖基。月令见禄，不住祖屋；一见财官，自然发福。用火愁水，用木愁金；轻重能分，祸福自真。五行生旺，不怕休囚；东南西北，数尽方休。寅申巳亥，四生之局；用物身强，遇之发福。辰戌丑未，四墓之局；人元三用，透旺为真。子午卯酉，四败之局；男犯兴衰，女犯孤独。进气退气，命物相争；进气不死，退气不生。财官临库，不冲不发。四柱干支，喜行相合。提纲有用，最怕刑冲；冲运则缓，冲用则凶。三奇透露，日主专强；其根有用，福禄荣昌。十干化神，有影无形；无中生有，福禄难凭。十恶大败，格中大忌；若遇财官，反成富贵。格格推详，以杀为重；化杀为权，何愁损用。杀不离印，印不离杀；杀印相生，功名显达。官杀重逢，制伏有功；如行帝旺（阳刃），遇之不凶。时杀无根，杀旺取贵。时杀多根，杀旺不利。八月官星（甲木见酉为官），大忌卯丁；卯丁克破，有情无情。印绶根轻，旺中显达。印绶根深，旺中不发。印绶比肩，喜行财乡。印无比肩，忌见财伤。先财后印，反成其福。先印后财，反成其辱。财官印绶，大忌比肩；伤官七杀，反助为权。伤官用财，死宫有子。伤官无财，子宫有死。时上偏财，怕逢兄弟。月印逢财，比肩不忌。伤官见官，格中反忌；不损用神，何愁官至。拱禄拱贵，填实则凶；提纲有用，论之不同。月令财官，遇之发福；禄位高强，比肩夺福。日禄归时，青云得路。庚日申（甲申）时，透财归禄。壬骑龙背，见戌无情；寅多则富，辰多则荣。天元一气，地物相同；人命逢此，位列三公。八字连珠，支神有用；造化逢之，名利必重。日德金神，月逢土旺；虽有轻名，祖业漂荡。金神带杀，身旺为奇；更行火地，名利当时。甲日金神，偏宜火制。乙日金神，何劳火制。六甲生春，时犯金神；水乡不发，土重名真。甲乙丑月，时带金神；月干见杀，双目不明。甲寅重重，二巳刑杀；终身必损，遇之难发。六甲寅月，透财时节；西北行程，九流立业。乙日卯月，金神刚烈；富贵比肩，旺横死绝。天干二丙，地支全寅；更行生印，死见祸临。火旺二寅，月令水金；火乡有救，见土刑身。巳日月戌，火神无气；多水多金，眼昏目闭。年干会火，日时会金；己干用印，官彻名清。秋金生午，二庚火丙；到丑伤情，逢离顺境。庚金坐午，辛金生未；透杀两停，冬生最贵。辛金月辰，庚金丑库；逆数清孤，顺行豪富。辛逢卯日，年月见酉；时带朝阳，为僧行丑。辛金亥日，月逢临戌；水运初行，须防目疾。辛金生酉，财官用印；顺行南方，名利必振。辛金坐巳，官印遇禄；顺行南方，贵显荣福。辛金逢离，透土何虑；无土伤身，寿元不住。月生四季，日主庚辛；何愁主弱，旺地成名。辛金逢火，见土成刑。阳金遇火，透土成名。壬生午位，禄马同乡；重重遇火，格局高强。（玄武当权格）壬癸多金，生于酉申；土旺则贵，火旺则贫。癸向巳宫，财官拘印；运至南方，利名必振。（玄武当权格）癸日己亥，杀财透露；地合伤官，有劳无富。癸日申提，卯寅岁时；年杀月劫，林下孤凄。癸日干己，阴杀重逢；无官相混，名利必通。伤官之格，女人最忌；带印带财，反为富贵。杀多有制，女人必贵。官星犯重，浊滥淫类。官星桃花，福禄堪夸。杀星桃花，朝劫暮巴。庚日申时，柱中金局；支无会合，伤官劫妻。癸日寅提，寅时亥月；莫犯提纲，祸福难推。甲日干（亥）提，见杀喜比；金水栽根，忌行卯未。戊己丑月，比肩透出；宜金入局，忌逢午未。壬癸坎宫，支逢午戌；干头比肩，东行为吉。甲乙震（卯）宫，卯多须夭；逆顺运行，子申发福。庚辛巳月，金生火旺；比劫栽根，西行成象。丙丁酉月，比肩不忌；火入离宫，比肩一例。曲直丑月，带印多金。壬癸丑月，土厚多金。食神生旺，胜似财官；浊之则贱，清之则垣。此法玄玄，识得成仙；学者宝授，千金莫传。（身弱论附）阳木无根，生于丑月；水多转贵，金多则折。乙木无根，生临丑月；金多转贵，火土则折。丙火无根，子申全见；无制无生，此身贫贱。六甲坐申，三重见子；运至北方，须防横死。丙临申位，阳水大忌；有制身强，旺成名利。己入亥月，怕逢阴木；月逢印生，自然成福。己日逢杀，印旺财伏；运转东南，贵高财足。壬寅壬戌，阳土透露；不混官星，名崇显禄。阴水无根，火乡有贵。阳水无根，火乡即畏。丁酉阴柔，不怕多水；比肩透露，格中返忌。戊寅日主，何愁杀旺；露火成名，水来漂荡。庚午日主，支火炎炎；见土取贵，见水为嫌。辛金身弱，卯提入格。癸酉主衰，见财成格。癸巳无根，火土重见；透财名彰，露根则贱。（弃命从财格）


- **分字分词释义**：
  - **先天何处后天何处要知来处便知去处**：先天后天皆需明了，知来处则知去处。
  - **以日为主专论财官分其贵贱**：以日干为主，专论财官分贵贱。
  - **独则易取乱则难明去留舒配论格要精**：独则易取，乱则难明，去留配合需精准。
  - **用火愁水用木愁金轻重能分祸福自真**：用火怕水，用木怕金，轻重分明则祸福自真。
  - **进气不死退气不生**：进气不死，退气不生。
  - **财官临库不冲不发**：财官入库不冲则不发。
  - **杀不离印印不离杀杀印相生功名显达**：杀印相生不离，功名显达。
  - **先财后印反成其福先印后财反成其辱**：先财后印成福，先印后财成辱。
  - **天元一气位列三公**：天干一气，可至三公。
  - **四生四墓四败**：寅申巳亥四生，辰戌丑未四墓，子午卯酉四败。
- **规范化释义（primary_lang_explained）**：  
  《四言独步》以四言口诀形式总括子平命理的核心法则与速断技法，是实务判命的"总纲与速查手册"。**总论框架**：先天后天、四柱三才、年干为本配元辰；神煞轻重先观月令论格推详；以日为主专论财官分贵贱；独易取乱难明，去留舒配论格要精。**月令与用神**：日主高强月提得令用财为物；年根月令日生时旺；用火愁水用木愁金，轻重能分祸福自真。**四生四墓四败**：寅申巳亥四生局用物身强遇之发福；辰戌丑未四墓局人元三用透旺为真；子午卯酉四败局男犯兴衰女犯孤独。**进退与库冲**：进气不死退气不生；财官临库不冲不发；提纲有用最怕刑冲。**杀印财官组合**：杀不离印印不离杀杀印相生功名显达；先财后印反成其福，先印后财反成其辱；伤官见官格中反忌不损用神何愁官至。**特殊格局**：拱禄拱贵填实则凶；日禄归时青云得路；天元一气位列三公；金神带杀身旺为奇更行火地名利当时。**十干细论**：详述甲乙丙丁戊己庚辛壬癸各干在不同月令与配置下的吉凶（如庚金坐午辛金生未透杀两停冬生最贵、壬生午位禄马同乡重重遇火格局高强等）。**女命与身弱**：伤官之格女人最忌带印带财反为富贵；杀多有制女人必贵；官星犯重浊滥淫类。身弱论附论各干无根或身弱时的特殊处理（如阳木无根生于丑月水多转贵金多则折、癸巳无根火土重见透财名彰露根则贱等弃命从财从杀的前导）。

- **完整对等诠释（secondary_lang_full）**：  
  **Four-Character Ode**: A comprehensive compendium of Zi Ping core principles and quick judgment techniques in four-character verse format—the master manual for practical fate analysis. **Framework Overview**: Understanding Prior-Heaven and Post-Heaven positions; Four Pillars arranged, Three Powers divided in sequence; Year Stem as foundation matching Original Spirit. Spirit-Sha weights must first observe Month Command, then discuss pattern details. Take Day Master as central focus, specifically discussing Wealth-Officer to distinguish nobility; singular configurations are easily grasped, chaotic ones are difficult to clarify—retention-discarding-adjustment-matching requires precise pattern analysis. **Month Command and Use God**: When Day Master is strong and Month gains Command, using Wealth serves as substance with solidity representing correctness. Year root serves as main foundation, Month Command as center; Day born in hundred increments, Hour vigorous or void. Using Fire fears Water, using Wood fears Metal—when weights are clearly distinguished, fortune-misfortune naturally reveals truth. **Four Sheng/Mu/Bai Bureaus**: Yin-Shen-Si-Hai constitute Four Sheng bureaus—when use-object and body are both strong, encountering these brings prosperity. Chen-Xu-Chou-Wei constitute Four Mu bureaus—when three Human Elements are utilized and transparency-vigor are true. Zi-Wu-Mao-You constitute Four Bai bureaus—males encounter ups-downs, females encounter solitude. **Advance-Retreat and Storehouse-Clash**: Advancing qi does not bring death, retreating qi does not bring life. When Wealth-Officer occupy storage, without clashing they won't manifest. Month Command having utility most fears punishment-clash. **Killing-Seal-Wealth-Officer Combinations**: Killing never separates from Seal, Seal never separates from Killing—Killing-Seal mutual generation achieves merit and fame. First Wealth later Seal paradoxically brings fortune; first Seal later Wealth paradoxically brings disgrace. Injury-Officer seeing Officer is pattern taboo—yet if not damaging use-god, why fear Officer arrival. **Special Patterns**: Arched-Salary-Arched-Noble when filled-solid brings fierceness. Day Salary returns Time gains azure-cloud path. Heaven Element unified in one qi achieves ministerial rank. Metal Spirit combined with Killing when body vigorous becomes extraordinary—additionally traveling Fire region gains fame and profit at that time. **Ten Stems Detail**: Exhaustive treatment of Jia-Yi-Bing-Ding-Wu-Ji-Geng-Xin-Ren-Gui stems in various month commands and configurations (e.g., Geng Metal sitting Noon, Xin Metal born Wei with transparent Killing both balanced—winter birth most noble; Ren born at Noon position with Salary-Horse in same location, repeatedly encountering Fire creates elevated pattern, etc.). **Female Fate and Body-Weak**: Injury-Officer pattern for females most taboo—yet combined with Seal or Wealth paradoxically brings wealth-nobility. Killings abundant yet controlled, females certainly noble. Officer Stars repeatedly appearing brings turbid promiscuity. Body-Weak discussion addresses each stem's rootless or body-weak special handling (e.g., Yang Wood rootless born in Ugly Month—abundant Water transforms to nobility, abundant Metal brings breaking; Gui-Si rootless with Fire-Earth heavily present and transparent Wealth achieves fame, but if roots are exposed then baseness results—serving as prelude to Abandon-Self-Follow patterns).

- **核心要点**：  
  - 以四言口诀总括子平命理核心法则：月令为纲、日主为主、财官为用、杀印相生等  
  - 涵盖四生四墓四败、进退气、库冲、十神组合、特殊格局等全面技法  
  - 详述十干在不同月令与配置下的吉凶判断（如金神、玄武当权格等）  
  - 包含女命与身弱论，为弃命从财从杀理论做铺垫

- **详细解说**：  《四言独步》以四言口诀形式总括子平命理核心法则。**总论框架**——"先天何处，后天何处，要知来处，便知去处"；"以日为主，专论财官，分其贵贱"确立判命框架。**月令用神**——"日主高强，月提得令"；"用火愁水，用木愁金，轻重能分，祸福自真"揭示月令与用神的关系。**四生四墓四败**——"寅申巳亥，四生之局；辰戌丑未，四墓之局；子午卯酉，四败之局"阐述地支分类。**进退库冲**——"进气不死，退气不生"；"财官临库，不冲不发"揭示进退与库冲之理。**杀印财官**——"杀不离印，印不离杀，杀印相生，功名显达"；"先财后印，反成其福；先印后财，反成其辱"阐述十神组合的顺序影响。**特殊格局**——"天元一气，位列三公"；"金神带杀，身旺为奇"揭示特殊格局的贵格。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_477]` `[trigger: 先天后天]` `[factor_trigger: xiantian_houtian AND laichi_quchu AND ri_weizhu AND caiguan_guijian AND anchong_qugui AND angui]` `[role: 主干]` 先天何处后天何处要知来处便知去处；以日为主专论财官分其贵贱。 → 《渊海子平·四言独步》
  - `[ns_yhzp_478]` `[trigger: 用火愁水]` `[factor_trigger: yonghuo_choushui AND yongmu_choujin AND qingzhong_nengfen]` `[role: 条件分支]` 用火愁水用木愁金；轻重能分祸福自真。 → 《渊海子平·四言独步》
  - `[ns_yhzp_479]` `[trigger: 四生四墓]` `[factor_trigger: yinshen_sihai_sisheng AND chenxu_chouwei_simu AND ziwu_maoyou_sibai AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 主干依赖]` 寅申巳亥四生之局；辰戌丑未四墓之局；子午卯酉四败之局。 → 《渊海子平·四言独步》
  - `[ns_yhzp_480]` `[trigger: 进气退气]` `[factor_trigger: jinqi_busi AND tuiqi_busheng AND caiguan_linku_buchong_bufa AND buchong_bufa AND caiguan_linku]` `[role: 条件分支]` 进气不死退气不生；财官临库不冲不发。 → 《渊海子平·四言独步》
  - `[ns_yhzp_481]` `[trigger: 杀印相生]` `[factor_trigger: sha_buli_yin AND yin_buli_sha AND shayin_xiangsheng_gongming AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 杀不离印印不离杀；杀印相生功名显达。 → 《渊海子平·四言独步》
  - `[ns_yhzp_482]` `[trigger: 先财后印]` `[factor_trigger: xiancai_houyin_chengfu AND xianyin_houcai_chengru AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 先财后印反成其福；先印后财反成其辱。 → 《渊海子平·四言独步》
  - `[ns_yhzp_483]` `[trigger: 天元一气]` `[factor_trigger: tianyuan_yiqi_weilie_sangong AND jinshen_daisha_shenwang_weiqi]` `[role: 条件分支]` 天元一气位列三公；金神带杀身旺为奇；特殊格局。 → 《渊海子平·四言独步》
  - `[ns_yhzp_484]` `[trigger: 四言独步纲领]` `[factor_trigger: siyan_dubu AND yueling_yongshen AND sisheng_simu AND shayin_xiangsheng AND teshu_geju AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 总结]` 四言独步以月令用神、四生四墓、杀印相生、特殊格局为核心，总括子平命理法则。 → 《渊海子平·四言独步》"""
    normalized_text_zh: str = """"""
    subject: str = "四言独步"
    factor_refs: list = ['four_character_ode', 'four_sheng_mu_bai', 'advancing_retreating_qi', 'killing_seal_generation', 'heaven_element_unity']
    
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
        book_id="yuanhaiziping",
        chapter="",
        l1_anchor="yhzp_v1.0.0_四言独步_001_L1",
    )
    version: str = "1.0.0"
