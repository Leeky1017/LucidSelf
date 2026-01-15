"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.725492
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
    semantic_id="zw_v1.0.0_增补太微赋_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 增补太微赋(SemanticEntry):
    """
    - 原文（source_text）：

  前后两凶神谓：两邻加侮，尚可撑持；同室与谋，最难隄防。片火焚天马，重羊逐禄存，劫空亲戚无常，权禄行藏靡定。君子哉魁钺，小人也羊铃，凶不皆凶，吉无纯吉，主强宾...
    """
    
    original_text: str = """- 原文（source_text）：

  前后两凶神谓：两邻加侮，尚可撑持；同室与谋，最难隄防。片火焚天马，重羊逐禄存，劫空亲戚无常，权禄行藏靡定。君子哉魁钺，小人也羊铃，凶不皆凶，吉无纯吉，主强宾弱，可保无虞，主弱宾强，凶危立见，主宾得失两相宜。运限命身当互见，身命最嫌羊陀七杀遇之未免为凶。二限甚忌贪破巨廉，逢之定然作祸，命遇魁昌常得贵，限逢紫府定财多。凡视女人之命先观天子二宫，若值杀星，定三嫁而心不足。或逢羊孛，虽啼哭而泪不干。若观男命，始以福财为主，再审迁移何如。二限相因吉凶同断，限逢吉曜，平生动用和谐；命坐凶乡，一世求谋龃龉。廉禄临身，女得纯阴贞洁之德；同梁守命，男得纯阳中正之心。君子命中亦有羊陀火铃，小人命内岂无科禄权星，要看得垣失垣，专论入庙失庙。若论小儿，详推童限。小儿命坐凶乡，三五岁必然夭折；更有限逢恶杀，五七岁必主灾亡。文昌文曲天魁秀，不读诗书也可人，多学少成，只为擎羊逢劫杀。为人好讼，盖因太岁遇官符。命之理微，熟察星辰之变化；数之理远，细详格局之兴衰。北极加凶杀，为道为僧；羊陀遇恶星，为奴为仆。如武破廉贪，固深谋而贵题，加羊陀空劫，反小志以孤寒。限辅星旺，限虽弱而不弱；命临吉地，命虽凶而不凶。断桥截空，大小难行；卯酉二空，聪明发福。命身遇紫府，叠积金银；二主逢劫空，衣食不足，谋而不遂。命限遇入擎羊，东作西成。限身遭逢辅相，科权禄拱，定为柱桂之高人；空劫羊铃，作九流之术士。情怀畅舒，昌曲命身；诡诈浮虚，羊陀陷地。天机天梁擎羊会，早有刑而晚见孤；贪狼武曲廉贞逢，少受贫而后享福。此皆斗数之奥妙，学者宜熟思之。

- 原注：

  本篇题作"增补太微赋"，在原《太微赋》基础上再次"增补"细则，特别强调"主强宾弱"与"主弱宾强"的力量对比、童限小儿的凶险、以及诸多格局的兴衰判断。全篇口诀密集，是实务推命的重要补充。

- 分字分词释义：

  - **前后两凶神**：指凶星在命宫前后两宫（即迁移与福德等）夹制，为"两邻加侮"。
  - **两邻加侮，尚可撑持**：凶星在邻宫夹制，虽有压力但尚能应对。
  - **同室与谋，最难隄防**：凶星与主星同宫，直接内耗，最难防范。
  - **片火焚天马**：火星与天马同宫，主奔波劳碌、焚心之象。
  - **重羊逐禄存**：擎羊与禄存同宫或对冲，主破财、劳碌。
  - **主强宾弱vs主弱宾强**：主星（命主、身主）与宾星（辅佐星）的力量对比，决定格局成败。
  - **天子二宫**：指夫妻宫与子女宫，女命最重视的两个宫位。
  - **童限**：幼童时期的大限，通常指12岁前的限运。
  - **断桥截空**：特殊的空亡组合，主大运小运难以顺遂。
  - **卯酉二空**：地支卯酉为特殊空亡位，主聪明但发福不稳。
  - **柱桂之高人**：科甲及第、位列朝堂的高士。

- 规范化释义（primary_lang_explained）：

  本条开篇强调凶星的位置关系："两邻加侮"（凶星在邻宫夹制）尚可撑持，"同室与谋"（凶星与主星同宫）最难防范。片火焚天马，主奔波劳碌；重羊逐禄存，主破财辛苦；劫空使亲戚关系无常，权禄使行藏靡定。

  魁钺为君子之星，羊铃为小人之曜，但"凶不皆凶、吉无纯吉"，关键看"主强宾弱"还是"主弱宾强"：主星强而宾星弱，可保无虞；主星弱而宾星强，凶危立见。运限、命身需要互相参看，身命最嫌羊陀七杀，二限最忌贪破巨廉。

  女命先观夫妻、子女二宫：若值杀星，定三嫁而心不足；或逢羊孛，虽啼哭而泪不干。男命始以福德、财帛为主，再审迁移宫。限逢吉曜则平生和谐，命坐凶乡则一世龃龉。

  小儿命坐凶乡，三五岁必夭；限逢恶杀，五七岁必灾。文昌文曲天魁秀，不读诗书也可人；多学少成，只为擎羊逢劫杀。为人好讼，盖因太岁遇官符。

  北极加凶杀，宜为僧道；羊陀遇恶星，为奴为仆。武破廉贪若配置得当，可成深谋贵格；加羊陀空劫，反成小志孤寒。限辅星旺，限虽弱而不弱；命临吉地，命虽凶而不凶。

  天机天梁擎羊会，早刑而晚孤；贪狼武曲廉贞逢，少贫而后福。此皆斗数奥妙，学者宜熟思。

- 完整对等诠释（secondary_lang_full）：

  This chapter supplements the original Taiwei Ode by turning its broad principles into finer, case‑based rules. It starts from the placement of malefic stars. When malefics sit in the neighbouring houses that flank the Life palace—“two neighbours insulting”—pressure is present but the core star can still stand; when malefics share the same house with the main significator—"sharing a room and plotting"—the conflict becomes internal, subtle and difficult to defend against. Images such as "a sliver of fire burning the Heavenly Horse" or "Goat Blade chasing Lu‑cun" describe concrete patterns of overwork, restless travel and financial loss; combinations with Jie‑kong suggest unstable kinship ties, while fluctuating power‑and‑salary stars speak of unsettled public roles.

  A central refrain is that no star is absolutely good or bad: "malefics are not purely harmful, benefics are not purely good." What matters is whether the main star is stronger than its guests or vice versa. When the core Life and Body significators are dignified, even harsh companions like Yang, Tuo or fiery malefics can be turned into courage, drive and disciplined pressure—"main strong, guests weak". When the main star is fallen or over‑controlled, even clusters of noble assistants, examination and office stars may fail to produce stable outcomes—"main weak, guests strong". The chapter therefore urges the reader to always compare host and guest strength, and to read timing cycles and natal structure together rather than separately.

  The text then differentiates focus by gender as framed in its historical context: women’s charts are judged first from the Spouse and Children houses, while men’s charts emphasise Fortune, Wealth and Move houses. Modern readers can generalise this into relational versus career‑mobility emphasis. Childhood limits are highlighted as especially fragile: children whose Life palace lies in hostile terrain and whose early periods are repeatedly struck by heavy malefics are portrayed as facing concentrated risk, which in contemporary practice translates into a call for careful health, safety and emotional support in early years. A wide range of further patterns—Northern Pole with malefics suggesting a monastic or marginal path, Yang and malefics indicating servitude, dignified combinations of Wuqu, Pojun, Lianzhen and Tanlang marking deep‑strategy noble careers when well supported, or turning into cold, poor lives when combined with Void and Goat Blade—illustrate how structure and environment can tilt the same core energies toward very different outcomes. Altogether, the essay teaches a dialectical approach: distinguish neighbour versus same‑house afflictions, host versus guest strength, and fragile versus robust life‑stages, then judge fortune and misfortune accordingly.

- 核心要点：

  1. **主强宾弱vs主弱宾强**：强调主星与宾星的力量对比，决定格局成败的核心法则。
  2. **两邻加侮vs同室与谋**：凶星在邻宫尚可应对，凶星同宫则内耗难防。
  3. **女命重夫子、男命重福财**：女命看夫妻子女，男命看福德财帛迁移。
  4. **童限凶险**：小儿命坐凶乡，三五岁必夭；限逢恶杀，五七岁必灾。
  5. **格局兴衰的辩证法**：君子命中亦有羊陀火铃，小人命内岂无科禄权星，关键看得垣失垣、入庙失庙。

- 详细解说：

  1. **"两邻加侮"vs"同室与谋"的区别**  
     "两邻加侮"指凶星在命宫的前后两宫（如迁移、福德等）夹制，虽有压力但主星尚能独立应对。"同室与谋"则指凶星与主星同宫，直接内耗，最难防范。这是对凶星位置关系的精细区分，提醒命师不能只看"有没有凶星"，还要看凶星在哪个位置。

  2. **"主强宾弱"vs"主弱宾强"的核心法则**  
     本条最核心的理念是"主强宾弱，可保无虞；主弱宾强，凶危立见"。主星指命主、身主等核心星曜，宾星指辅佐、夹拱之星。若主星力量强大（入庙、得地、有助），即便宾星为凶，也能化凶为用；反之，若主星力量微弱（失陷、受制），即便宾星为吉，也难以真正成吉。这是对前文"吉凶互藏"理念的进一步深化。

  3. **女命重夫子、男命重福财**  
     "凡视女人之命，先观天子二宫"，即夫妻宫与子女宫，这是古代女性命理中最重视的两个宫位。男命则"始以福财为主，再审迁移何如"，即福德、财帛、迁移三宫为重点。这反映了传统社会的性别分工观念，在现代解读中，可将女命的夫子二宫扩展为"关系与成就"，男命的福财迁移扩展为"事业与流动"。

  4. **童限的脆弱性与风险**  
     "小儿命坐凶乡，三五岁必然夭折；更有限逢恶杀，五七岁必主灾亡。"这是对童限凶险的严重警告。在古代医疗条件有限的情况下，幼儿夭折率极高，命理体系中对童限的高度重视，既有统计基础，也有风险预警的现实意义。在现代社会，虽然医疗条件大幅改善，但对童限遇凶的命盘，仍应提醒家长格外关注幼儿的健康与安全。

  5. **格局兴衰的辩证法**  
     "君子命中亦有羊陀火铃，小人命内岂无科禄权星，要看得垣失垣，专论入庙失庙。"再次强调：不能简单以"有吉星"或"有凶星"来判断一个人的格局，而要看这些星曜是否得地、是否入庙、是否与主星相配。这是对机械套用星曜标签的批判，也是对辩证思维的倡导。

- 校勘与字词辨析：

  - **"天子二宫"**：部分版本作"夫子二宫"，皆指夫妻宫与子女宫，本稿从原文"天子"，在释义中明确为夫妻与子女。
  - **"柱桂之高人"**：部分版本作"折桂""攀桂"，皆指科甲及第，本稿从原文"柱桂"，取"柱石之臣、折桂之才"双重含义。
  - **"龃龉"**：上下牙齿不齐，引申为不顺遂、多波折。

- 叙事素材（narrative_snippets）：

  - **主宾法则**："主强宾弱，可保无虞；主弱宾强，凶危立见"，此为判断吉凶的核心法则——主星强则能化凶为用。
  - **凶星位置**："两邻加侮，尚可无虞；同室与谋，必不可逃"，凶星夹命与凶星同宫的危险程度不同。
  - **女命重夫子**："凡视女人之命，先观天子二宫"，古代女命以夫妻宫、子女宫为首要判断。
  - **童限凶险**："小儿命坐凶乡，三五岁必然夭折"，童限遇凶需格外关注幼儿健康与安全。
  - **辩证判断**："君子命中亦有羊陀火铃，小人命内岂无科禄权星"，不能简单以有无吉凶星判断格局。
  - **现代应用**：本条可作为命盘分析的"主宾法则"框架——先定主星强弱，再看宾星配合，辩证看待吉凶。

  **L2 叙事素材层（规范格式）**：

  - `[ns_zwds_j1_139]` `[trigger: 女命类型]` `[factor_trigger: type_nvming]` `[role: 主干]` 女命以夫妻宫、子女宫为首要判断宫位。 → 《增补太微赋》"女人之命，先观天子二宫"
  - `[ns_zwds_j1_140]` `[trigger: 男命类型]` `[factor_trigger: type_nanming]` `[role: 主干]` 男命以福德、财帛、迁移三宫为重点判断宫位。 → 《增补太微赋》
  - `[ns_zwds_j1_141]` `[trigger: 阳男阴女]` `[factor_trigger: type_yangnanyinnv]` `[role: 条件分支]` 阳男阴女为阳年生男、阴年生女的命局类型。 → 《增补太微赋》
  - `[ns_zwds_j1_142]` `[trigger: 阴男阳女]` `[factor_trigger: type_yinnanyangnu]` `[role: 条件分支]` 阴男阳女为阴年生男、阳年生女的命局类型。 → 《增补太微赋》
  - `[ns_zwds_j1_143]` `[trigger: 凶险不佳结果]` `[factor_trigger: result_xiong]` `[role: 结果]` 凶险结果为命盘整体配置偏凶的判断。 → 《增补太微赋》
  - `[ns_zwds_j1_144]` `[trigger: 吉利结果]` `[factor_trigger: result_ji]` `[role: 结果]` 吉利结果为命盘整体配置偏吉的判断。 → 《增补太微赋》
  - `[ns_zwds_j1_145]` `[trigger: 贤达结果]` `[factor_trigger: result_xianda]` `[role: 结果]` 贤达结果为德才兼备、品行端正的判断。 → 《增补太微赋》
  - `[ns_zwds_j1_146]` `[trigger: 富厚结果]` `[factor_trigger: result_fuhou]` `[role: 结果]` 富厚结果为财富丰厚、生活优渥的判断。 → 《增补太微赋》
  - `[ns_zwds_j1_147]` `[trigger: 贵显结果]` `[factor_trigger: result_guixian]` `[role: 结果]` 贵显结果为地位显赫、身份尊贵的判断。 → 《增补太微赋》
  - `[ns_zwds_j1_148]` `[trigger: 孤克结果]` `[factor_trigger: result_guke]` `[role: 结果]` 孤克结果为六亲缘薄、孤独无依的判断。 → 《增补太微赋》
  - `[ns_zwds_j1_149]` `[trigger: 刑伤结果]` `[factor_trigger: result_xingshang]` `[role: 结果]` 刑伤结果为遭受刑罚、身体伤残的判断。 → 《增补太微赋》
  - `[ns_zwds_j1_150]` `[trigger: 夭折结果]` `[factor_trigger: result_yaoshou]` `[role: 结果]` 夭折结果为早亡短寿的判断。 → 《增补太微赋》"三五岁必然夭折"
  - `[ns_zwds_j1_151]` `[trigger: 灾亡结果]` `[factor_trigger: result_zaiwang]` `[role: 结果]` 灾亡结果为因灾祸而亡的判断。 → 《增补太微赋》"五七岁必主灾亡"
  - `[ns_zwds_j1_152]` `[trigger: 凶险位置组合]` `[factor_trigger: xiongxian_cengci]` `[role: 条件分支]` 凶险层次由凶星位置关系决定，同宫最凶，夹命次之。 → 《增补太微赋》"两邻加侮""同室与谋"
  - `[ns_zwds_j1_153]` `[trigger: 主星组合模式]` `[factor_trigger: xiongxing_zuhe]` `[role: 主干]` 凶星组合为多个凶星同宫或夹拱的配置模式。 → 《增补太微赋》
  - `[ns_zwds_j1_154]` `[trigger: 凶星聚集]` `[factor_trigger: xiongxing_juji]` `[role: 条件分支]` 凶星聚集为多个凶星集中在关键宫位的状态。 → 《增补太微赋》"""
    normalized_text_zh: str = """"""
    subject: str = "增补太微赋"
    factor_refs: list = ['star_zhu', 'star_bin', 'combo_lianglin_jiawu', 'combo_tongshi_yumou', 'time_tongxian']
    
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
        l1_anchor="zw_v1.0.0_增补太微赋_001_L1",
    )
    version: str = "1.0.0"
