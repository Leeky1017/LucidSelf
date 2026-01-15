"""
Auto-generated semantic module for zhougong
Generated at: 2025-12-05T13:30:19.877739
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
    semantic_id="zgjm_v1.0.0_文书笔砚兵器_001",
    book_id="zhougong",
    engine_id="dream"
)
class 文书笔砚兵器(SemanticEntry):
    """
    - **原文（source_text）**：

  【类名】

  文书笔砚兵器。

  【条文】

  各色经书，大富贵。
  五色纸者，大益财。
  吞五色纸，诗书进。

  几上有书，禄位至。
...
    """
    
    original_text: str = """- **原文（source_text）**：

  【类名】

  文书笔砚兵器。

  【条文】

  各色经书，大富贵。
  五色纸者，大益财。
  吞五色纸，诗书进。

  几上有书，禄位至。
  诗文书写字，大吉。
  有人教书，大富贵。

  见读书者，主聪明。
  观人读书，生贵子。
  得历日者，中黄甲。

  封书信者，主通达。
  手弄笔砚，主远信。
  人与墨者，文章进。

  人将己笔，文章退。
  他人送笔，主才进。
  君王队伍，有异名。

  得大赦者，宅舍凶。
  就人卜易，主疾病。
  受人纸钱，主大吉。

  公座移动，主迁官。
  受职上官，财物来。
  佩印公爵，主大吉。

  佩印执节，主移居。
  佩印信者，名誉出。
  缓印改迁，生贵子。

  棋子，主添丁进口。
  打球者，主得虚名。
  兵马入城，福禄至。

  率众破贼，所求得。
  在军阵中，主大吉。
  将卒随行，主喜事。

  征人初出，事未成。
  征人回者，主疾病。
  见军兵败，主凶事。

  己射人，必主远行。
  人射己，有行人至。
  持弓矢者，主大吉。

  挽弓断弦，主凶恶。
  人送弓弩，得人力。
  弩弦难上，兄弟散。

  弓弩相斗，主争论。
  戈钺有光，禄位至。
  披甲仗剑，得高官。

- 分字分词释义：

  - **文书笔砚兵器**：本类总纲，前半围绕经书、纸张、笔砚、印信与官职，后半转入兵马、征战、箭矢与兵器，整体关乎**学业文章、科第官职与军旅权力**。
  - **各色经书大富贵；五色纸者大益财；吞五色纸诗书进**：经书与五色纸皆象征文化与科举资源，多主富贵与财益；吞五色纸，喻将知识内化，故“诗书进”。
  - **几上有书禄位至；诗文书写字大吉；有人教书大富贵**：案几上有书，预示与文职、禄位相关；写诗作文与书写，均使文章之气活跃，大吉；受人教书，则事业与才名有贵人相助，大富贵。
  - **见读书者主聪明；观人读书生贵子；得历日者中黄甲**：读书之人象征聪明才智，观之则主自身聪明；观人读书、生贵子；得历日（黄历）则喻掌握时机，有中黄甲（科举优等）之象。
  - **封书信主通达；手弄笔砚主远信；人与墨者文章进**：书信与笔砚皆与文字往来有关，主通达远信与文章进益。
  - **人将己笔文章退；他人送笔主才进；君王队伍有异名**：他人夺走自己的笔，象征表达与文采受损，故文章退；他人相送之笔，则才华获助而进；君王队伍有异名，则与军职或特殊功名相关。
  - **得大赦者宅舍凶；就人卜易主疾病；受人纸钱主大吉**：大赦看似好事，但梦中反主宅舍有凶变；就人卜易，则多为忧心所致，主疾病；受人纸钱，则为阴阳界赐福象征，主大吉.
  - **公座移动主迁官；受职上官财物来；佩印公爵主大吉；佩印执节主移居；佩印信者名誉出；缓印改迁生贵子**：公座、受职、佩印、执节与缓印改迁，皆与官职、迁调与名誉相关，多主迁官、移居与名誉外显.
  - **棋子主添丁进口；打球者主得虚名；兵马入城福禄至；率众破贼所求得；在军阵中主大吉；将卒随行主喜事**：棋子与添丁进口相连；打球则虚名多于实利；兵马入城、率众破贼与军阵得胜，多主福禄与所求皆得；随行将卒则有喜事.
  - **征人初出事未成；征人回者主疾病；见军兵败主凶事**：征人初出，多事未成；征人归来，则带回疾病忧患；军兵败，则主凶事与挫折.
  - **己射人必主远行；人射己有行人至；持弓矢者主大吉；挽弓断弦主凶恶；人送弓弩得人力；弩弦难上兄弟散；弓弩相斗主争论；戈钺有光禄位至；披甲仗剑得高官**：弓矢与戈钺一类兵器，多指行动力与武职，或凶恶争斗，或禄位高官，须依具体景象区别.

- **规范化释义（primary_lang_explained）**：

  本类通过经书、纸张、笔砚、印信与兵马、弓矢等意象，呈现的是**一个人通过文字与武力两条路线追求名誉、官职与福禄**的各种可能：

  - 经书、五色纸、书写与读书者，指向学习、科举与文职上的进退，以及贵子与聪明的象征.
  - 书信、笔砚与纸钱，则把注意力放在“信息流与阴阳往还”上，主通达、远信与大吉.
  - 佩印、公座与受职，串起官场位次的变动，或迁官、移居，或名誉外显.
  - 棋子、打球与兵马、军阵，则将注意力移向博弈、虚名与实战之功，既有福禄至，也有凶事与败军.
  - 弓矢、弓弩与戈钺，则集中描绘个人行动力、远行、争论乃至高官禄位的多种走向.

- 核心要点：

  - **看文书与经书：学业与科举**：经书、五色纸、读书与教书，多与学业精进、科举中第与贵子有关.
  - **看笔砚与书信：沟通与声名**：封书、弄笔砚、人与墨与送笔，指向沟通顺畅与文章才名的进退.
  - **看印信与公座：官职与迁调**：公座移动、受职、佩印与缓印改迁，多主迁官、移居与名誉外显.
  - **看棋子、打球与兵马：虚名与实功**：棋子与添丁、打球与虚名、兵马与福禄、破贼与所求得，分别呈现不同层次的“名与实”.
  - **看弓矢与军阵：远行、争论与禄位**：射人、被射与持弓矢，涉及远行与来客；军阵胜败与戈钺有光，则在凶事与高官之间分野.

- 详细解说：

  **（一）经书、纸张与学业科第**

  - “各色经书大富贵；五色纸者大益财；吞五色纸诗书进”：
    - 经书与纸张都是知识承载物，各色经书象征多方涉猎，主大富贵；
    - 五色纸则与礼制与文书相关，主益财；
    - 吞五色纸，喻将知识与文运吸纳入身，故诗书进.

  **（二）案几、读书与黄甲**

  - “几上有书禄位至；诗文书写字大吉；有人教书大富贵；见读书者主聪明；观人读书生贵子；得历日者中黄甲”：
    - 几上有书，说明家中有文气，禄位可期；
    - 写诗作文与书写，均使文章之气活跃，大吉；
    - 有人教书，则事业与才名有贵人相助，大富贵；
    - 见读书者，象征自身聪明；观人读书，则寓子女读书生贵子；
    - 得历日者，则象征把握时令节气，有中黄甲（科举优等）之象.

  **（三）笔砚、纸钱与印信：沟通与阴阳之门**

  - “封书信者主通达；手弄笔砚主远信；人与墨者文章进；人将己笔文章退；他人送笔主才进；得大赦者宅舍凶；就人卜易主疾病；受人纸钱主大吉”：
    - 封书与弄笔砚，皆指书写与通讯，主通达远信；
    - 人与墨者，文章进；人将己笔，则表达渠道受限，文章退；
    - 他人送笔，才华获加持，主才进；
    - 得大赦者，虽免罪，却多缘于先有罪事，梦中反主宅舍凶；
    - 就人卜易，多是忧心求问，主疾病；
    - 受人纸钱，则含阴阳界赐度之意，主大吉.

  **（四）公座、佩印与棋局：禄位与虚实名声**

  - “公座移动主迁官；受职上官财物来；佩印公爵主大吉；佩印执节主移居；佩印信者名誉出；缓印改迁生贵子；棋子主添丁进口；打球者主得虚名”：
    - 公座移动，意味着职务变动，主迁官；
    - 受职与上官财物，皆指禄位与俸禄的实际到来；
    - 佩印公爵与执节，分别象征权力与军令，多主大吉与移居；
    - 佩印信者，则名誉发于外；
    - 缓印改迁，多主职位调整后反得贵子；
    - 棋子则与“子”与“局”相关，主添丁进口；
    - 打球者则偏向娱乐之名，主得虚名.

  **（五）兵马、征战与弓矢**

  - “兵马入城福禄至；率众破贼所求得；在军阵中主大吉；将卒随行主喜事；征人初出事未成；征人回者主疾病；见军兵败主凶事”：
    - 兵马入城，多主凯旋与福禄至；
    - 率众破贼，则所求多得；
    - 军阵得胜，大吉；将卒随行，多有喜事；
    - 然而征人初出，事未成；征人回，则带回疾病忧患；
    - 见军兵败，则主凶事.
  - “己射人必主远行；人射己有行人至；持弓矢者主大吉；挽弓断弦主凶恶；人送弓弩得人力；弩弦难上兄弟散；弓弩相斗主争论；戈钺有光禄位至；披甲仗剑得高官”：
    - 己射人，象征主动出击，必主远行；
    - 人射己，则外来之力临身，有行人至；
    - 持弓矢者，主大吉，指有行动与武力之备；
    - 挽弓断弦，则弦断于紧张之时，主凶恶；
    - 人送弓弩，则得他人助力；
    - 弩弦难上，则兄弟之间难以同心，主散；
    - 弓弩相斗，则争论不止；
    - 戈钺有光，象征武职显达，禄位至；
    - 披甲仗剑，则得高官.



- **完整对等诠释（secondary_lang_full）**：

  This category traces two main pathways through which a person pursues reputation, office, and fortune. The first is the "civil" track of books, papers, writing tools, and official documents; the second is the "martial" track of troops, weapons, and direct force. Dreams of scriptures, colored papers, books on the desk, writing poetry, or being taught by a teacher point to study, examinations, and advancement through learning.

  Letters, inkstones, brushes, and sealed documents highlight the flow of information and the management of one's name. Sealing a letter or playing with brush and ink suggests smooth communication and distant news arriving; receiving ink or pens from others indicates that one’s talent is being recognized and supported. Conversely, having one's own pen taken away warns that the ability to express oneself or to maintain literary prestige is being weakened. Official seats, seals, and ceremonial tallies represent concrete positions and authority: movement of the official seat, receiving a post, or wearing seals and insignia often foretells transfers, promotions, relocation, and the public display of rank.

  Chess pieces, ball games, troops entering a city, battle lines, and flashing halberds shift the focus toward competition and force. Chess pieces allude both to strategic play and to children entering the household; ball games tend toward reputation that is more show than substance. Troops marching into a city, leading forces to defeat bandits, and standing in victorious formations symbolize solid achievements, rewards, and the fulfillment of desires. Bows, crossbows, arrows, and shining weapons describe the dreamer’s capacity to act at a distance, defend or attack, and win high office through martial merit. Taken together, the civil images of writing and documents and the martial images of soldiers and arms show how words and weapons, communication and force, jointly map out the ways a person may gain or lose power, status, and support.

- 核心要点：

  - **看文书与经书：学业与科举**：经书、五色纸、读书与教书，多与学业精进、科举中第与贵子有关.
  - **看笔砚与书信：沟通与声名**：封书、弄笔砚、人与墨与送笔，指向沟通顺畅与文章才名的进退.
  - **看印信与公座：官职与迁调**：公座移动、受职、佩印与缓印改迁，多主迁官、移居与名誉外显.
  - **看棋子、打球与兵马：虚名与实功**：棋子与添丁、打球与虚名、兵马与福禄、破贼与所求得，分别呈现不同层次的“名与实”.
  - **看弓矢与军阵：远行、争论与禄位**：射人、被射与持弓矢，涉及远行与来客；军阵胜败与戈钺有光，则在凶事与高官之间分野.

- 详细解说：

  **（一）经书、纸张与学业科第**

  - “各色经书大富贵；五色纸者大益财；吞五色纸诗书进”：
    - 经书与纸张都是知识承载物，各色经书象征多方涉猎，主大富贵；
    - 五色纸则与礼制与文书相关，主益财；
    - 吞五色纸，喻将知识与文运吸纳入身，故诗书进.

  **（二）案几、读书与黄甲**

  - “几上有书禄位至；诗文书写字大吉；有人教书大富贵；见读书者主聪明；观人读书生贵子；得历日者中黄甲”：
    - 几上有书，说明家中有文气，禄位可期；
    - 写诗作文与书写，均使文章之气活跃，大吉；
    - 有人教书，则事业与才名有贵人相助，大富贵；
    - 见读书者，象征自身聪明；观人读书，则寓子女读书生贵子；
    - 得历日者，则象征把握时令节气，有中黄甲（科举优等）之象.

  **（三）笔砚、纸钱与印信：沟通与阴阳之门**

  - “封书信者主通达；手弄笔砚主远信；人与墨者文章进；人将己笔文章退；他人送笔主才进；得大赦者宅舍凶；就人卜易主疾病；受人纸钱主大吉”：
    - 封书与弄笔砚，皆指书写与通讯，主通达远信；
    - 人与墨者，文章进；人将己笔，则表达渠道受限，文章退；
    - 他人送笔，才华获加持，主才进；
    - 得大赦者，虽免罪，却多缘于先有罪事，梦中反主宅舍凶；
    - 就人卜易，多是忧心求问，主疾病；
    - 受人纸钱，则含阴阳界赐度之意，主大吉.

  **（四）公座、佩印与棋局：禄位与虚实名声**

  - “公座移动主迁官；受职上官财物来；佩印公爵主大吉；佩印执节主移居；佩印信者名誉出；缓印改迁生贵子；棋子主添丁进口；打球者主得虚名”：
    - 公座移动，意味着职务变动，主迁官；
    - 受职与上官财物，皆指禄位与俸禄的实际到来；
    - 佩印公爵与执节，分别象征权力与军令，多主大吉与移居；
    - 佩印信者，则名誉发于外；
    - 缓印改迁，多主职位调整后反得贵子；
    - 棋子则与“子”与“局”相关，主添丁进口；
    - 打球者则偏向娱乐之名，主得虚名.

  **（五）兵马、征战与弓矢**

  - “兵马入城福禄至；率众破贼所求得；在军阵中主大吉；将卒随行主喜事；征人初出事未成；征人回者主疾病；见军兵败主凶事”：
    - 兵马入城，多主凯旋与福禄至；
    - 率众破贼，则所求多得；
    - 军阵得胜，大吉；将卒随行，多有喜事；
    - 然而征人初出，事未成；征人回，则带回疾病忧患；
    - 见军兵败，则主凶事.
  - “己射人必主远行；人射己有行人至；持弓矢者主大吉；挽弓断弦主凶恶；人送弓弩得人力；弩弦难上兄弟散；弓弩相斗主争论；戈钺有光禄位至；披甲仗剑得高官”：
    - 己射人，象征主动出击，必主远行；
    - 人射己，则外来之力临身，有行人至；
    - 持弓矢者，主大吉，指有行动与武力之备；
    - 挽弓断弦，则弦断于紧张之时，主凶恶；
    - 人送弓弩，则得他人助力；
    - 弩弦难上，则兄弟之间难以同心，主散；
    - 弓弩相斗，则争论不止；
    - 戈钺有光，象征武职显达，禄位至；
    - 披甲仗剑，则得高官.



- 校勘与字词辨析：

  - 本类原文多以“三句并列”体书写，如“各色经书大富贵　五色纸者大益财　吞五色纸诗书进”，本稿在 L1 层按意义拆分为独立句，并加标点，严格保留原有词序与字形.
  - “黄甲”典出科举榜色，本稿保留原称，在白话中以“中黄甲（科举优等）”说明，不展开典故考证.
  - “纸钱”一词兼有阴阳间流转之意，L1 层不作现代“冥币”与“现金”之分，仅在释义中以“阴阳界赐福”点出传统理解.
  - “缓印改迁”一句，“缓印”多指印信暂缓或更换，本稿理解为职务调整后反得贵子，不扩展为具体制度.
  - “缓印改迁生贵子”一句，“缓印”多指印信暂缓或更换，本稿理解为职务调整后反得贵子，不扩展为具体制度.
  - “戈钺”“弓弩”等兵器名称保留底本写法，不统一为现代兵器术语.

  - **English**：
    - The original text in this category mostly follows the "three parallel phrases" format, e.g. "各色经书大富贵　五色纸者大益财　吞五色纸诗书进." This edition splits them by meaning into independent sentences at the L1 layer, adding punctuation while strictly preserving the original word order and character forms.
    - The term "黄甲" derives from the color of imperial examination announcement scrolls. This edition preserves the original term, explaining it in vernacular as "achieving 黄甲 (top tier in imperial examinations)" without extensive allusion research.
    - The term "纸钱" carries meanings of circulation between the living and dead realms. The L1 layer does not distinguish between modern "spirit money" and "cash," only noting in the interpretation the traditional understanding of "blessings across yin and yang boundaries."
    - In "缓印改迁生贵子," the term "缓印" mostly refers to official seals being delayed or replaced. This edition understands it as "gaining a noble son after position adjustment" without expanding into specific institutional systems.
    - Weapon names like "戈钺" and "弓弩" preserve the base text writing without unifying them into modern weapon terminology.


- **叙事素材（narrative_snippets）**：

  - `[ns_zgjm_606]` `[trigger: 梦见各色经书]` `[factor_trigger: dream_scripture]` `[role: 主干]` 各色经书，大富贵。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_607]` `[trigger: 梦见五色纸者]` `[factor_trigger: dream_colored_paper]` `[role: 主干]` 五色纸者，大益财。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_608]` `[trigger: 梦见吞五色纸]` `[factor_trigger: dream_swallow_paper]` `[role: 主干]` 吞五色纸，诗书进。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_609]` `[trigger: 梦见几上有书]` `[factor_trigger: dream_book_desk]` `[role: 主干]` 几上有书，禄位至。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_610]` `[trigger: 梦见诗文书写字]` `[factor_trigger: dream_write_poem]` `[role: 主干]` 诗文书写字，大吉。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_611]` `[trigger: 梦见有人教书]` `[factor_trigger: dream_teach]` `[role: 主干]` 有人教书，大富贵。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_612]` `[trigger: 梦见见读书者]` `[factor_trigger: dream_see_read]` `[role: 主干]` 见读书者，主聪明。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_613]` `[trigger: 梦见观人读书]` `[factor_trigger: dream_watch_read]` `[role: 主干]` 观人读书，生贵子。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_614]` `[trigger: 梦见得历日者]` `[factor_trigger: dream_get_calendar]` `[role: 主干]` 得历日者，中黄甲。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_615]` `[trigger: 梦见封书信者]` `[factor_trigger: dream_seal_letter]` `[role: 主干]` 封书信者，主通达。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_616]` `[trigger: 梦见手弄笔砚]` `[factor_trigger: dream_brush_inkstone]` `[role: 主干]` 手弄笔砚，主远信。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_617]` `[trigger: 梦见人与墨者]` `[factor_trigger: dream_give_ink]` `[role: 主干]` 人与墨者，文章进。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_618]` `[trigger: 梦见人将己笔]` `[factor_trigger: dream_take_brush]` `[role: 主干]` 人将己笔，文章退。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_619]` `[trigger: 梦见他人送笔]` `[factor_trigger: dream_send_brush]` `[role: 主干]` 他人送笔，主才进。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_620]` `[trigger: 梦见君王队伍]` `[factor_trigger: dream_king_procession]` `[role: 主干]` 君王队伍，有异名。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_621]` `[trigger: 梦见得大赦者]` `[factor_trigger: dream_amnesty]` `[role: 主干]` 得大赦者，宅舍凶。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_622]` `[trigger: 梦见就人卜易]` `[factor_trigger: dream_divination]` `[role: 主干]` 就人卜易，主疾病。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_623]` `[trigger: 梦见受人纸钱]` `[factor_trigger: dream_receive_paper_money]` `[role: 主干]` 受人纸钱，主大吉。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_624]` `[trigger: 梦见公座移动]` `[factor_trigger: dream_seat_move]` `[role: 主干]` 公座移动，主迁官。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_625]` `[trigger: 梦见受职上官]` `[factor_trigger: dream_receive_position]` `[role: 主干]` 受职上官，财物来。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_626]` `[trigger: 梦见佩印公爵]` `[factor_trigger: dream_wear_seal]` `[role: 主干]` 佩印公爵，主大吉。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_627]` `[trigger: 梦见佩印执节]` `[factor_trigger: dream_seal_staff]` `[role: 主干]` 佩印执节，主移居。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_628]` `[trigger: 梦见佩印信者]` `[factor_trigger: dream_seal_letter]` `[role: 主干]` 佩印信者，名誉出。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_629]` `[trigger: 梦见缓印改迁]` `[factor_trigger: dream_delay_seal]` `[role: 主干]` 缓印改迁，生贵子。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_630]` `[trigger: 梦见棋子]` `[factor_trigger: dream_chess]` `[role: 主干]` 棋子，主添丁进口。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_631]` `[trigger: 梦见打球者]` `[factor_trigger: dream_play_ball]` `[role: 主干]` 打球者，主得虚名。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_632]` `[trigger: 梦见兵马入城]` `[factor_trigger: dream_army_enter]` `[role: 主干]` 兵马入城，福禄至。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_633]` `[trigger: 梦见率众破贼]` `[factor_trigger: dream_lead_army]` `[role: 主干]` 率众破贼，所求得。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_634]` `[trigger: 梦见在军阵中]` `[factor_trigger: dream_in_army]` `[role: 主干]` 在军阵中，主大吉。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_635]` `[trigger: 梦见将卒随行]` `[factor_trigger: dream_soldiers_follow]` `[role: 主干]` 将卒随行，主喜事。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_636]` `[trigger: 梦见征人初出]` `[factor_trigger: dream_soldier_out]` `[role: 主干]` 征人初出，事未成。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_637]` `[trigger: 梦见征人回者]` `[factor_trigger: dream_soldier_return]` `[role: 主干]` 征人回者，主疾病。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_638]` `[trigger: 梦见见军兵败]` `[factor_trigger: dream_army_defeat]` `[role: 主干]` 见军兵败，主凶事。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_639]` `[trigger: 梦见己射人]` `[factor_trigger: dream_shoot_other]` `[role: 主干]` 己射人，必主远行。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_640]` `[trigger: 梦见人射己]` `[factor_trigger: dream_shot_by]` `[role: 主干]` 人射己，有行人至。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_641]` `[trigger: 梦见持弓矢者]` `[factor_trigger: dream_hold_bow]` `[role: 主干]` 持弓矢者，主大吉。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_642]` `[trigger: 梦见挽弓断弦]` `[factor_trigger: dream_bow_break]` `[role: 主干]` 挽弓断弦，主凶恶。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_643]` `[trigger: 梦见人送弓弩]` `[factor_trigger: dream_send_bow]` `[role: 主干]` 人送弓弩，得人力。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_644]` `[trigger: 梦见弩弦难上]` `[factor_trigger: dream_crossbow_hard]` `[role: 主干]` 弩弦难上，兄弟散。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_645]` `[trigger: 梦见弓弩相斗]` `[factor_trigger: dream_bow_fight]` `[role: 主干]` 弓弩相斗，主争论。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_646]` `[trigger: 梦见戈钺有光]` `[factor_trigger: dream_halberd_shine]` `[role: 主干]` 戈钺有光，禄位至。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_647]` `[trigger: 梦见披甲仗剑]` `[factor_trigger: dream_armor_sword]` `[role: 主干]` 披甲仗剑，得高官。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_1032]` `[trigger: 梦见谷散]` `[factor_trigger: dream_grain_scatter]` `[role: 主干]` 梦见谷散，主破财。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_1033]` `[trigger: 梦见谷茂]` `[factor_trigger: dream_grain_thriving]` `[role: 主干]` 梦见谷茂，主大吉。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_1034]` `[trigger: 梦见大福]` `[factor_trigger: dream_great_fortune]` `[role: 主干]` 梦见大福，主大吉。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_1035]` `[trigger: 梦见大荣]` `[factor_trigger: dream_great_honor]` `[role: 主干]` 梦见大荣，主显达。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_1036]` `[trigger: 梦见官位]` `[factor_trigger: dream_guanwei]` `[role: 主干]` 梦见官位，主升迁。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_1037]` `[trigger: 梦见贵人]` `[factor_trigger: dream_guiren]` `[role: 主干]` 梦见贵人，主吉祥。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_1038]` `[trigger: 梦见贵人衣]` `[factor_trigger: dream_guiren_clothes]` `[role: 主干]` 梦见贵人衣，主升迁。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_1039]` `[trigger: 梦见贵人败]` `[factor_trigger: dream_guiren_fail]` `[role: 主干]` 梦见贵人败，主凶。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_1040]` `[trigger: 梦见贵子]` `[factor_trigger: dream_guizi]` `[role: 主干]` 梦见贵子，主生贵。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_1041]` `[trigger: 梦见堂陷]` `[factor_trigger: dream_hall_sink]` `[role: 主干]` 梦见堂陷，主凶兆。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_1042]` `[trigger: 梦见幸福]` `[factor_trigger: dream_happiness]` `[role: 主干]` 梦见幸福，主大吉。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_1043]` `[trigger: 梦见头白]` `[factor_trigger: dream_head_white]` `[role: 主干]` 梦见头白，主长寿。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_1044]` `[trigger: 梦见高官]` `[factor_trigger: dream_high_official]` `[role: 主干]` 梦见高官，主升迁。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_1045]` `[trigger: 梦见骑马]` `[factor_trigger: dream_horse_ride]` `[role: 主干]` 梦见骑马，主远行。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_1046]` `[trigger: 梦见房屋]` `[factor_trigger: dream_house]` `[role: 主干]` 梦见房屋，主安居。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_1047]` `[trigger: 梦见屋破]` `[factor_trigger: dream_house_break]` `[role: 主干]` 梦见屋破，主凶兆。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_1048]` `[trigger: 梦见屋高]` `[factor_trigger: dream_house_high]` `[role: 主干]` 梦见屋高，主大吉。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_1049]` `[trigger: 梦见屋新]` `[factor_trigger: dream_house_new]` `[role: 主干]` 梦见屋新，主吉祥。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_1050]` `[trigger: 梦见狩猎]` `[factor_trigger: dream_hunt]` `[role: 主干]` 梦见狩猎，主有获。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_1051]` `[trigger: 梦见恶病]` `[factor_trigger: dream_illness_severe]` `[role: 主干]` 梦见恶病，主大凶。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_1052]` `[trigger: 梦见收入]` `[factor_trigger: dream_income]` `[role: 主干]` 梦见收入，主有财。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_1053]` `[trigger: 梦见受伤]` `[factor_trigger: dream_injury]` `[role: 主干]` 梦见受伤，主凶险。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_1054]` `[trigger: 梦见吉祥]` `[factor_trigger: dream_jixiang]` `[role: 主干]` 梦见吉祥，主大吉。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_1055]` `[trigger: 梦见钥匙]` `[factor_trigger: dream_key]` `[role: 主干]` 梦见钥匙，主有喜。 → 《周公解梦·文书笔砚兵器》
  - `[ns_zgjm_1056]` `[trigger: 梦见杀人]` `[factor_trigger: dream_kill]` `[role: 主干]` 梦见杀人，主大凶。 → 《周公解梦·文书笔砚兵器》"""
    normalized_text_zh: str = """"""
    subject: str = "文书笔砚兵器"
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
        book_id="zhougong",
        chapter="",
        l1_anchor="zgjm_v1.0.0_文书笔砚兵器_001_L1",
    )
    version: str = "1.0.0"
