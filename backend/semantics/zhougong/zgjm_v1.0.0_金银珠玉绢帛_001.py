"""
Auto-generated semantic module for zhougong
Generated at: 2025-12-05T13:30:19.864359
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
    semantic_id="zgjm_v1.0.0_金银珠玉绢帛_001",
    book_id="zhougong",
    engine_id="dream"
)
class 金银珠玉绢帛(SemanticEntry):
    """
    - **原文（source_text）**：

  【类名】

  金银珠玉绢帛。

  【条文】

  金银宝者，主富贵。
  金银珠玉，大吉利。
  金银杯皿，有贵孕。

  金银作铛器，大吉。
...
    """
    
    original_text: str = """- **原文（source_text）**：

  【类名】

  金银珠玉绢帛。

  【条文】

  金银宝者，主富贵。
  金银珠玉，大吉利。
  金银杯皿，有贵孕。

  金银作铛器，大吉。
  玉积如山，大富贵。
  得金玉环，生贵子。

  铜铛，主有口舌至。
  珠玉满怀，主大凶。
  得玉碗器物，皆吉。

  见铁器物，主得财。
  铅与钖者，主得财。
  得铜物，主大富贵。

  镶嵌器物，疾病去。
  还人钱物，疾病去。
  拾得钱物，皆大吉。

  钱春夏吉，秋冬凶。
  家中分财，主离败。
  赠彩帛者，主有权。

  贵人赐绫锦，官至。
  人赐绢帛，大吉昌。
  与人丝帛，大凶恶。

  得他人麻布衣，凶。
  得布帛，远亲来至。
  与人衣服，官事至。

  寻丝绢，主进入口。
  纺绩者，主寿命长。
  经络者，主被人辱。

  箱器，主口舌之事。

- 分字分词释义：

  - **金银珠玉绢帛**：本类总纲，涵盖贵金属、珠宝、玉器、钱币以及布帛衣物等，象征**财富形态、资源流动与人际赠予**。
  - **金银宝者主富贵；金银珠玉大吉利；金银杯皿有贵孕；玉积如山大富贵；得金玉环生贵子**：金银珠玉的丰厚积聚，多主富贵隆盛、贵子贵孕。
  - **金银作铛器大吉；得玉碗器物皆吉**：贵重金玉化为日用器皿，象征财富能转化为实际生活品质，主吉。
  - **铜铛主有口舌至；珠玉满怀主大凶**：铜铛敲击易出声，象征口舌纷争；珠玉满怀则有“负担过重、招人妒害”之象，反主大凶。
  - **见铁器物主得财；铅与钖者主得财；得铜物主大富贵**：铁、铅、锡、铜等常见金属与劳作、工艺相关，多主通过劳动与技巧得财。
  - **镶嵌器物疾病去；还人钱物疾病去；拾得钱物皆大吉**：器物修整、归还钱物与拾得钱财，皆与“修复关系与流动财富”有关，多主病退与吉庆。
  - **钱春夏吉秋冬凶**：钱财之梦在春夏主吉、秋冬主凶，提示财利与时令、气候及整体环境相关。
  - **家中分财主离败；赠彩帛者主有权**：家中分财多主分家、离散；彩帛赠予则象征权力与恩宠的下赐。
  - **贵人赐绫锦官至；人赐绢帛大吉昌；与人丝帛大凶恶**：自上而下的赐予多主升官与吉昌；反之主动送出丝帛则有“泄财、牵连是非”之象。
  - **得他人麻布衣凶；得布帛远亲来至；与人衣服官事至**：麻布粗衣多与丧服与辛劳有关；布帛则象征亲缘往来与衣食资源；衣物互赠则可能牵及官非。
  - **寻丝绢主进入口；纺绩者主寿命长；经络者主被人辱**：丝绢与纺织活动象征谋生与劳作；经络则有“被束缚、受辱”之意。
  - **箱器主口舌之事**：箱器为装物之具，亦可象征秘密与封存之事，主有口舌、争执或隐藏议题。

- **规范化释义（primary_lang_explained）**：

  本类以金银珠玉、铜铁铅锡以及绢帛衣物为主，描述财富、物质资源与人际赠予在梦中的象征：

  - 见金银珠玉丰厚、玉如山积，多主富贵与贵子；若珠玉满怀，则须警惕因财富过盛而生的妒害与祸端。
  - 见铁器、铜器与铅锡之属，多主通过劳作与技艺获得踏实之财。
  - 钱财之梦需看时令与流向：春夏见钱多主吉利，秋冬则可能预示财务紧缩；还人钱物与拾得钱物，多与病退、债了与运势转好有关。
  - 彩帛、绫锦与衣服的赠受，象征权力、恩宠与人际责任的传递：由上赐下多主升迁与荣宠，自己向外大量赠送则要防泄财与是非。
  - 纺绩与经络则点出：靠勤劳编织生活者，寿命多长；若被经络所缚，则易受制于人，甚至蒙羞。

- 核心要点：

  - **看财富形态：金玉 vs 铜铁**
    - 金银珠玉代表显赫之财与声望，多主富贵与贵子；
    - 铜铁等常见金属则象征劳动所得的稳实之财。
  - **看钱财流向：得、还、分**
    - 拾得钱物与还人钱物，多主病退与心安；
    - 家中分财，多与家族结构调整、分家离败相关。
  - **看赠受关系：赐与、施与**
    - 贵人赐绫锦、他人赠绢帛，多主权力与恩典降临；
    - 自己向外大量赠送丝帛与衣服，则易泄财并牵连官事。
  - **看衣布质地：绫锦 vs 麻布**
    - 绫锦绢帛多为荣华之象，麻布则与丧服、劳苦相关，得之反主凶。
  - **看劳作方式：纺绩与经络**
    - 纺绩象征踏实劳作与长久积累；
    - 经络则提醒警惕被制度或他人羞辱、束缚。

- 详细解说：

  **（一）金银珠玉：显赫之财与其阴影**

  - “金银宝者主富贵”“金银珠玉大吉利”“玉积如山大富贵”“得金玉环生贵子”皆将金玉之象与富贵、子嗣相连：
    - 金银代表外在荣耀与名利；
    - 玉则偏于内在品格与高贵气质。
  - “金银杯皿有贵孕”“金银作铛器大吉”：
    - 当金银化为实用器具，象征财富被合理运用，而非空置；
    - 与“贵孕”相连，则可解作孕育贵子或孕育贵重事业。
  - “铜铛主有口舌至”“珠玉满怀主大凶”：
    - 铜铛易鸣，象征话题、舆论与争议；
    - 珠玉满怀则是“财多惹祸”的典型，以过度执着于财富为戒。

  **（二）诸金属与钱财：劳动与时令之衡**

  - “见铁器物主得财”“铅与钖者主得财”“得铜物主大富贵”：
    - 铁、铅、锡与铜多用于工具与器具，梦见之主通过技艺与劳作得财，而非凭空横财。
  - “镶嵌器物疾病去”“还人钱物疾病去”“拾得钱物皆大吉”：
    - 器物修饰与归还钱物，象征修补关系与偿还债务，因而有病退与心安之象；
    - 拾得钱财，则象征意外机缘与资源的无心之得。
  - “钱春夏吉秋冬凶”：
    - 春夏万物生长，现金多主投资与扩张机会；
    - 秋冬收敛肃杀，梦钱反主紧缩与压力，提醒量入为出。

  **（三）布帛衣物：恩泽与责任的包装**

  - “赠彩帛者主有权”“贵人赐绫锦官至”“人赐绢帛大吉昌”：
    - 彩帛与绫锦是礼仪中常见的赏赐之物，象征权力、地位与荣宠的外在表现。
  - “与人丝帛大凶恶”“与人衣服官事至”：
    - 自己向外赠送丝帛或衣服，可能涉及复杂的人情债或利益输送，故古书多视为牵连官事与是非之兆。
  - “得他人麻布衣凶”“得布帛远亲来至”：
    - 麻布常与丧服、苦役相连，得之反主忧患；
    - 普通布帛则象征亲人往来与生活所需，主有远亲来访或支持。

  **（四）纺绩与箱器：日常劳作与隐秘议题**

  - “寻丝绢主进入口”“纺绩者主寿命长”：
    - 寻找丝绢象征主动谋生机会与入口；
    - 纺绩则是枯燥而长久的劳作，古人以此喻“长寿与长期积累”。
  - “经络者主被人辱”：
    - 经络本为织物经纬，亦可象征被束缚与被操控，故主被人辱、身不由己。
  - “箱器主口舌之事”：
    - 箱器收纳物品，亦收纳秘密与证据；
    - 梦中出现，往往预示围绕“所藏之物”产生议论与争执。

- **完整对等诠释（secondary_lang_full）**：

  This category gathers dream omens relating to gold, silver, pearls, jade, silk, and fine fabrics. These images map onto **wealth, status symbols, precious relationships, and material fortune**.

  The core interpretive principle centers on acquisition, loss, and condition of these valuables: obtaining gold or jade generally portends incoming wealth and elevated status; losing precious items warns of financial setback or relationship loss. Bright, lustrous gems indicate favorable fortune; tarnished or broken valuables suggest declining circumstances. Silk and fine fabrics relate to social status and reputation—wearing them suggests honor, while torn garments warn of disgrace.

  **Key interpretive axes**:
  - **Gold and silver**: acquiring brings wealth and good fortune; losing warns of financial troubles; the condition (bright vs. tarnished) affects the interpretation.
  - **Pearls and jade**: receiving pearls often relates to gaining wisdom or precious relationships; jade symbolizes virtue and integrity; broken jade warns of damaged reputation.
  - **Silk and fabrics**: fine silk indicates honor and social advancement; tattered cloth suggests poverty or loss of status; colors carry additional symbolic meaning.
  - **Exchange and gifting**: receiving valuables as gifts generally auspicious; giving away one's treasures may indicate sacrifice or loss of fortune.

- 校勘与字词辨析：

  - 本类原文中“铅与钖者”一语，“钖”字亦作“锡”，本稿据底本录“钖”，在释义中统一视作锡类金属，不再分殊。
  - “钱春夏吉秋冬凶”所言时令，与今人财务运行节奏未必完全一致，L1 层仍忠实记载，在白话中仅作时代语境说明。
  - 关于“珠玉满怀主大凶”“与人丝帛大凶恶”等较为偏激之语，本稿遵原文判为凶，同时在详细解说中提示“财多惹祸、情债难清”的象征意涵，供后续高阶语义层再作调和。
  - “经络者主被人辱”之“经络”，原本多与织造有关，不必与中医经络混同，本稿在释义中按“被束缚、被牵扯”解释。

  - **English**：
    - In "铅与钖者," the character "钖" is also written as "锡." This edition follows the base text as "钖," treating it uniformly as tin-type metal in the interpretation without further distinction.
    - The seasonal reference in "钱春夏吉秋冬凶" may not align with modern financial rhythms. The L1 layer records faithfully, providing only historical context explanation in the vernacular.
    - Regarding more extreme phrases like "珠玉满怀主大凶" and "与人丝帛大凶恶," this edition follows the original text's judgment of misfortune while suggesting in the detailed commentary the symbolic implications of "wealth attracting disaster, emotional debts hard to clear," allowing for reconciliation in higher semantic layers.
    - In "经络者主被人辱," the term "经络" originally relates to weaving and textile production, not to be confused with Traditional Chinese Medicine meridians. This edition interprets it as "being bound or entangled."



- **叙事素材（narrative_snippets）**：

  - `[ns_zgjm_250]` `[trigger: 梦见金银宝者]` `[factor_trigger: dream_gold_silver_treasure]` `[role: 主干]` 金银宝者，主富贵。 → 《周公解梦·金银珠玉绢帛》
  - `[ns_zgjm_251]` `[trigger: 梦见金银珠玉]` `[factor_trigger: dream_gold_jade]` `[role: 主干]` 金银珠玉，大吉利。 → 《周公解梦·金银珠玉绢帛》
  - `[ns_zgjm_252]` `[trigger: 梦见金银杯皿]` `[factor_trigger: dream_gold_cup]` `[role: 主干]` 金银杯皿，有贵孕。 → 《周公解梦·金银珠玉绢帛》
  - `[ns_zgjm_253]` `[trigger: 梦见金银作铛器]` `[factor_trigger: dream_gold_pot]` `[role: 主干]` 金银作铛器，大吉。 → 《周公解梦·金银珠玉绢帛》
  - `[ns_zgjm_254]` `[trigger: 梦见玉积如山]` `[factor_trigger: dream_jade_mountain]` `[role: 主干]` 玉积如山，大富贵。 → 《周公解梦·金银珠玉绢帛》
  - `[ns_zgjm_255]` `[trigger: 梦见得金玉环]` `[factor_trigger: dream_jade_ring]` `[role: 主干]` 得金玉环，生贵子。 → 《周公解梦·金银珠玉绢帛》
  - `[ns_zgjm_256]` `[trigger: 梦见铜铛]` `[factor_trigger: dream_copper_pot]` `[role: 主干]` 铜铛，主有口舌至。 → 《周公解梦·金银珠玉绢帛》
  - `[ns_zgjm_257]` `[trigger: 梦见珠玉满怀]` `[factor_trigger: dream_jade_full]` `[role: 主干]` 珠玉满怀，主大凶。 → 《周公解梦·金银珠玉绢帛》
  - `[ns_zgjm_258]` `[trigger: 梦见得玉碗器物]` `[factor_trigger: dream_jade_bowl]` `[role: 主干]` 得玉碗器物，皆吉。 → 《周公解梦·金银珠玉绢帛》
  - `[ns_zgjm_259]` `[trigger: 梦见见铁器物]` `[factor_trigger: dream_iron_item]` `[role: 主干]` 见铁器物，主得财。 → 《周公解梦·金银珠玉绢帛》
  - `[ns_zgjm_260]` `[trigger: 梦见铅与钖者]` `[factor_trigger: dream_lead_tin]` `[role: 主干]` 铅与钖者，主得财。 → 《周公解梦·金银珠玉绢帛》
  - `[ns_zgjm_261]` `[trigger: 梦见得铜物]` `[factor_trigger: dream_copper_item]` `[role: 主干]` 得铜物，主大富贵。 → 《周公解梦·金银珠玉绢帛》
  - `[ns_zgjm_262]` `[trigger: 梦见镶嵌器物]` `[factor_trigger: dream_inlay_item]` `[role: 主干]` 镶嵌器物，疾病去。 → 《周公解梦·金银珠玉绢帛》
  - `[ns_zgjm_263]` `[trigger: 梦见还人钱物]` `[factor_trigger: dream_return_money]` `[role: 主干]` 还人钱物，疾病去。 → 《周公解梦·金银珠玉绢帛》
  - `[ns_zgjm_264]` `[trigger: 梦见拾得钱物]` `[factor_trigger: dream_find_money]` `[role: 主干]` 拾得钱物，皆大吉。 → 《周公解梦·金银珠玉绢帛》
  - `[ns_zgjm_265]` `[trigger: 梦见钱春夏吉]` `[factor_trigger: dream_money_season]` `[role: 主干]` 钱春夏吉，秋冬凶。 → 《周公解梦·金银珠玉绢帛》
  - `[ns_zgjm_266]` `[trigger: 梦见家中分财]` `[factor_trigger: dream_divide_wealth]` `[role: 主干]` 家中分财，主离败。 → 《周公解梦·金银珠玉绢帛》
  - `[ns_zgjm_267]` `[trigger: 梦见赠彩帛者]` `[factor_trigger: dream_gift_silk]` `[role: 主干]` 赠彩帛者，主有权。 → 《周公解梦·金银珠玉绢帛》
  - `[ns_zgjm_268]` `[trigger: 梦见贵人赐绫锦]` `[factor_trigger: dream_noble_gift_brocade]` `[role: 主干]` 贵人赐绫锦，官至。 → 《周公解梦·金银珠玉绢帛》
  - `[ns_zgjm_269]` `[trigger: 梦见人赐绢帛]` `[factor_trigger: dream_gift_fabric]` `[role: 主干]` 人赐绢帛，大吉昌。 → 《周公解梦·金银珠玉绢帛》
  - `[ns_zgjm_270]` `[trigger: 梦见与人丝帛]` `[factor_trigger: dream_give_silk]` `[role: 主干]` 与人丝帛，大凶恶。 → 《周公解梦·金银珠玉绢帛》
  - `[ns_zgjm_271]` `[trigger: 梦见得他人麻布衣]` `[factor_trigger: dream_hemp_cloth]` `[role: 主干]` 得他人麻布衣，凶。 → 《周公解梦·金银珠玉绢帛》
  - `[ns_zgjm_272]` `[trigger: 梦见得布帛]` `[factor_trigger: dream_get_fabric]` `[role: 主干]` 得布帛，远亲来至。 → 《周公解梦·金银珠玉绢帛》
  - `[ns_zgjm_273]` `[trigger: 梦见与人衣服]` `[factor_trigger: dream_give_clothes]` `[role: 主干]` 与人衣服，官事至。 → 《周公解梦·金银珠玉绢帛》
  - `[ns_zgjm_274]` `[trigger: 梦见寻丝绢]` `[factor_trigger: dream_seek_silk]` `[role: 主干]` 寻丝绢，主进入口。 → 《周公解梦·金银珠玉绢帛》
  - `[ns_zgjm_275]` `[trigger: 梦见纺绩者]` `[factor_trigger: dream_spinning]` `[role: 主干]` 纺绩者，主寿命长。 → 《周公解梦·金银珠玉绢帛》
  - `[ns_zgjm_276]` `[trigger: 梦见经络者]` `[factor_trigger: dream_weaving]` `[role: 主干]` 经络者，主被人辱。 → 《周公解梦·金银珠玉绢帛》
  - `[ns_zgjm_277]` `[trigger: 梦见箱器]` `[factor_trigger: dream_box]` `[role: 主干]` 箱器，主口舌之事。 → 《周公解梦·金银珠玉绢帛》"""
    normalized_text_zh: str = """"""
    subject: str = "金银珠玉绢帛"
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
        l1_anchor="zgjm_v1.0.0_金银珠玉绢帛_001_L1",
    )
    version: str = "1.0.0"
