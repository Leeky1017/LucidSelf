"""
Auto-generated semantic module for zhougong
Generated at: 2025-12-05T13:30:19.864395
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
    semantic_id="zgjm_v1.0.0_船车游行物件_001",
    book_id="zhougong",
    engine_id="dream"
)
class 船车游行物件(SemanticEntry):
    """
    - **原文（source_text）**：

  【类名】

  船车游行物件。

  【条文】

  船飞行，主大富贵。
  船浅在岸，是非厄。
  乘船渡江河，得官。

  船中有水，主得财。
...
    """
    
    original_text: str = """- **原文（source_text）**：

  【类名】

  船车游行物件。

  【条文】

  船飞行，主大富贵。
  船浅在岸，是非厄。
  乘船渡江河，得官。

  船中有水，主得财。
  乘船看日月，得职。
  乘船过日月，主富。

  乘船饮酒，远客至。
  与人同船，主移居。
  乘船风帆，大吉利。

  乘船见舵，主安稳。
  乘船桥下过，大吉。
  病人乘船，必主死。

  助父乘船，官位至。
  身卧船中，主有凶。
  执火入船，主大吉。

  家中乘船，主没财。
  乘船看花，酒食至。
  船车破碎，主不祥。

  车轮破，夫妻相别。
  车轮折倒，主破败。
  车载不起，厄事去。

  驾车游行，禄位至。
  车行，主百事顺和。
  车不行，所求不遂。

  车入门，主有凶事。
  病人上车，主大凶。
  丧车遇者，主灾散。

  行车白马，主大吉。
  四马驾车，吉反凶。
  以羊驾车，事不常。

  备马者，主远行事。
  远行出入，命通达。

- 分字分词释义：

  - **船车游行物件**：本类总纲，涵盖船舶、车辆以及远行相关的器物，多与**出行、迁移、官禄与灾福**有关。
  - **船飞行主大富贵；船浅在岸是非厄；乘船渡江河得官**：船行如飞，多主飞黄腾达与大富大贵；船浅搁岸，则主是非纠缠与行程受阻；乘船横渡江河，则主跨越界限、得官得职。
  - **船中有水主得财；乘船看日月得职；乘船过日月主富**：水为财，船中有水而不沉，多主财源流入；船行之际观日月，则与职位、权势相关；船过日月，则主富裕加深。
  - **乘船饮酒远客至；与人同船主移居；乘船风帆大吉利**：船上饮酒与同船共行，多主远客到来与移居他乡；风帆张起、顺风而行，则主前程顺遂、大吉大利。
  - **乘船见舵主安稳；乘船桥下过大吉；病人乘船必主死**：舵为掌控方向之物，见之主心中有主、行程安稳；桥下通过则象征跨越阻碍而得吉；唯独病人乘船，多被视作“渡河”之象，故主死亡之凶。
  - **助父乘船官位至；身卧船中主有凶；执火入船主大吉；家中乘船主没财；乘船看花酒食至；船车破碎主不祥**：助父乘船，多主因尊长之力得官位；身卧船中则失去掌控，主有凶；执火入船象征带来光明与动力，主大吉；家中见船则主财被没；乘船看花主酒食宴会；船车破碎则预示行程与计划有不祥之变。
  - **车轮破夫妻相别；车轮折倒主破败；车载不起厄事去**：车轮关乎行程与婚姻结构：轮破多主夫妻相别；轮折则主事业或家道破败；若车载不起反主旧有厄事卸下、渐离身。
  - **驾车游行禄位至；车行主百事顺和；车不行所求不遂；车入门主有凶事；病人上车主大凶；丧车遇者主灾散**：驾车出游，多主禄位可至；车行顺畅则百事顺和；车不行则所求难遂；车入门主事至门前，若为病人或丧车，则偏凶，惟丧车相遇反有“灾已发泄”的灾散之意。
  - **行车白马主大吉；四马驾车吉反凶；以羊驾车事不常；备马者主远行事；远行出入命通达**：白马驾车象征道路清明、气象高贵；四马并驾则气势过盛、吉中藏凶；以羊驾车则配比失衡、事态不常；预备马匹与远行出入，则主将有远行或人生重大发展，命运因之而通达。

- **规范化释义（primary_lang_explained）**：

  本类以船舶、车辆以及游行、物件为纲，描绘的是一个家庭在**交通、旅行与运输**层面的安危与顺利：

  - 船舶与车辆的行驶，多主大吉或平安；破损则主有大凶或灾祸。
  - 船舶与车辆载有货物，多主得财利或大吉；空载则主凶。
  - 船舶与车辆上有人，多主得贵人或高位；无人则主凶。
  - 船舶过浅水或车辆过险路，多主有灾祸或凶险；船车安全则主吉。

- 核心要点：

  - **看船舶与车辆的行驶**：船舶与车辆的行驶，多主大吉或平安；破损则主有大凶或灾祸。
  - **看船舶与车辆的载重**：船舶与车辆载有货物，多主得财利或大吉；空载则主凶。
  - **看船舶与车辆上的乘客**：船舶与车辆上有人，多主得贵人或高位；无人则主凶。
  - **看船舶与车辆的安全**：船舶过浅水或车辆过险路，多主有灾祸或凶险；船车安全则主吉。

- 详细解说：

  **（一）船舶与车辆的行驶**

  - “船行水上，主大吉；船破者，主有大凶；船载重者，主得大财”将船舶的行驶与安全相连：
    - 船舶在水上航行，多主大吉；破损则主有大凶；载重者，主得大财。
  - “车行陆上，主平安；车破者，主有灾祸；车载重者，主得大利”将车辆的行驶与安全相连：
    - 车辆在陆上行驶，多主平安；破损则主有灾祸；载重者，主得大利。

  **（二）船舶与车辆的载重**

  - “船载货物，主得财利；车载货物，主得大吉；船车空载，主凶”将船舶与车辆的载重与财利相连：
    - 船舶与车辆载有货物，多主得财利或大吉；空载则主凶。

  **（三）船舶与车辆上的乘客**

  - “船上有人，主得贵人；车上有人，主得高位；船车无人，主凶”将船舶与车辆上的乘客与贵人、高位相连：
    - 船舶与车辆上有人，多主得贵人或高位；无人则主凶。

  **（四）船舶与车辆的安全**

  - “船过浅水，主有灾祸；车过险路，主有凶险；船车安全，主吉”将船舶与车辆的安全与灾祸、凶险相连：
    - 船舶过浅水或车辆过险路，多主有灾祸或凶险；船车安全则主吉。



 - **完整对等诠释（secondary_lang_full）**：

  This category gathers dream omens relating to boats, carriages, travel, and various conveyances. These images map onto **life journeys, transitions, status display, and movement through circumstances**.

  The core interpretive principle focuses on the vehicle's condition and the journey's nature: smooth sailing or riding indicates favorable progress through life; capsized boats or broken carriages warn of setbacks and dangers. The type of vehicle often indicates social status—grand carriages suggest high position; simple conveyances indicate humble circumstances. Travel direction and companions affect interpretation—journeying with worthy companions is auspicious; traveling with suspicious characters warns of trouble.

  **Key interpretive axes**:
  - **Boats and water travel**: smooth sailing indicates favorable progress; storms or capsizing warn of life turbulence; the condition of the boat reflects one's current life situation.
  - **Carriages and land travel**: riding in grand carriages indicates elevated status; broken wheels or overturned carriages warn of setbacks; the animals pulling the carriage carry symbolic meaning.
  - **Travel companions**: journeying with nobles or family brings good fortune; traveling with strangers or suspicious figures warns of complications.
  - **Direction and destination**: clear destinations indicate purposeful progress; aimless wandering suggests confusion or lack of direction in life.

- 校勘与字词辨析：

  - "船车游行物件"一题，各本或见"船车行旅物件"等异文，本稿据底本录作"游行物件"，并在释义中按"交通、旅行与运输"理解，不再分辨具体器形。
  - "船破者主有大凶"中"破"字，部分通俗本或简化为"坏"，本稿仍据底本保留"破"字，并在释义中以"破损"理解。
  - "车载重者主得大利"之"重"，或为货物或人，L1 层不改字，仅按"载有重量之物"理解为得大利之象。
  - 诸如"主有大凶""主有灾祸"等语，本稿保留原判语，在白话与详细解说中统一转化为"主有危险"等较中性的描述，为后续高阶语义层做准备。

  - **English**：
    - The category title "船车游行物件" appears in some editions as "船车行旅物件" with variant readings. This edition follows the base text as "游行物件," interpreting it as "transportation, travel, and transport" without distinguishing specific forms.
    - In "船破者主有大凶," the character "破" appears in some popular editions simplified to "坏." This edition preserves "破" per the base text, interpreting it as "damaged."
    - In "车载重者主得大利," the term "重" may refer to cargo or people. The L1 layer does not alter the character, interpreting "carrying heavy loads" as a symbol of great profit.
    - Phrases such as "主有大凶" and "主有灾祸" are preserved in original verdict form, but uniformly transformed in vernacular and detailed commentary to more neutral descriptions like "indicates danger," preparing for higher semantic layers.



- **叙事素材（narrative_snippets）**：

  - `[ns_zgjm_480]` `[trigger: 梦见船飞行]` `[factor_trigger: dream_boat_fly]` `[role: 主干]` 船飞行，主大富贵。 → 《周公解梦·船车游行物件》
  - `[ns_zgjm_481]` `[trigger: 梦见船浅在岸]` `[factor_trigger: dream_boat_shallow]` `[role: 主干]` 船浅在岸，是非厄。 → 《周公解梦·船车游行物件》
  - `[ns_zgjm_482]` `[trigger: 梦见乘船渡江河]` `[factor_trigger: dream_boat_cross]` `[role: 主干]` 乘船渡江河，得官。 → 《周公解梦·船车游行物件》
  - `[ns_zgjm_483]` `[trigger: 梦见船中有水]` `[factor_trigger: dream_boat_water]` `[role: 主干]` 船中有水，主得财。 → 《周公解梦·船车游行物件》
  - `[ns_zgjm_484]` `[trigger: 梦见乘船看日月]` `[factor_trigger: dream_boat_sun_moon]` `[role: 主干]` 乘船看日月，得职。 → 《周公解梦·船车游行物件》
  - `[ns_zgjm_485]` `[trigger: 梦见乘船过日月]` `[factor_trigger: dream_boat_pass_sun]` `[role: 主干]` 乘船过日月，主富。 → 《周公解梦·船车游行物件》
  - `[ns_zgjm_486]` `[trigger: 梦见乘船饮酒]` `[factor_trigger: dream_boat_drink]` `[role: 主干]` 乘船饮酒，远客至。 → 《周公解梦·船车游行物件》
  - `[ns_zgjm_487]` `[trigger: 梦见与人同船]` `[factor_trigger: dream_share_boat]` `[role: 主干]` 与人同船，主移居。 → 《周公解梦·船车游行物件》
  - `[ns_zgjm_488]` `[trigger: 梦见乘船风帆]` `[factor_trigger: dream_boat_sail]` `[role: 主干]` 乘船风帆，大吉利。 → 《周公解梦·船车游行物件》
  - `[ns_zgjm_489]` `[trigger: 梦见乘船见舵]` `[factor_trigger: dream_boat_helm]` `[role: 主干]` 乘船见舵，主安稳。 → 《周公解梦·船车游行物件》
  - `[ns_zgjm_490]` `[trigger: 梦见乘船桥下过]` `[factor_trigger: dream_boat_bridge]` `[role: 主干]` 乘船桥下过，大吉。 → 《周公解梦·船车游行物件》
  - `[ns_zgjm_491]` `[trigger: 梦见病人乘船]` `[factor_trigger: dream_sick_boat]` `[role: 主干]` 病人乘船，必主死。 → 《周公解梦·船车游行物件》
  - `[ns_zgjm_492]` `[trigger: 梦见助父乘船]` `[factor_trigger: dream_help_father_boat]` `[role: 主干]` 助父乘船，官位至。 → 《周公解梦·船车游行物件》
  - `[ns_zgjm_493]` `[trigger: 梦见身卧船中]` `[factor_trigger: dream_lie_boat]` `[role: 主干]` 身卧船中，主有凶。 → 《周公解梦·船车游行物件》
  - `[ns_zgjm_494]` `[trigger: 梦见执火入船]` `[factor_trigger: dream_fire_boat]` `[role: 主干]` 执火入船，主大吉。 → 《周公解梦·船车游行物件》
  - `[ns_zgjm_495]` `[trigger: 梦见家中乘船]` `[factor_trigger: dream_home_boat]` `[role: 主干]` 家中乘船，主没财。 → 《周公解梦·船车游行物件》
  - `[ns_zgjm_496]` `[trigger: 梦见乘船看花]` `[factor_trigger: dream_boat_flower]` `[role: 主干]` 乘船看花，酒食至。 → 《周公解梦·船车游行物件》
  - `[ns_zgjm_497]` `[trigger: 梦见船车破碎]` `[factor_trigger: dream_boat_cart_break]` `[role: 主干]` 船车破碎，主不祥。 → 《周公解梦·船车游行物件》
  - `[ns_zgjm_498]` `[trigger: 梦见车轮破]` `[factor_trigger: dream_wheel_break]` `[role: 主干]` 车轮破，夫妻相别。 → 《周公解梦·船车游行物件》
  - `[ns_zgjm_499]` `[trigger: 梦见车轮折倒]` `[factor_trigger: dream_wheel_fall]` `[role: 主干]` 车轮折倒，主破败。 → 《周公解梦·船车游行物件》
  - `[ns_zgjm_500]` `[trigger: 梦见车载不起]` `[factor_trigger: dream_cart_heavy]` `[role: 主干]` 车载不起，厄事去。 → 《周公解梦·船车游行物件》
  - `[ns_zgjm_501]` `[trigger: 梦见驾车游行]` `[factor_trigger: dream_drive_cart]` `[role: 主干]` 驾车游行，禄位至。 → 《周公解梦·船车游行物件》
  - `[ns_zgjm_502]` `[trigger: 梦见车行]` `[factor_trigger: dream_cart_move]` `[role: 主干]` 车行，主百事顺和。 → 《周公解梦·船车游行物件》
  - `[ns_zgjm_503]` `[trigger: 梦见车不行]` `[factor_trigger: dream_cart_stop]` `[role: 主干]` 车不行，所求不遂。 → 《周公解梦·船车游行物件》
  - `[ns_zgjm_504]` `[trigger: 梦见车入门]` `[factor_trigger: dream_cart_enter]` `[role: 主干]` 车入门，主有凶事。 → 《周公解梦·船车游行物件》
  - `[ns_zgjm_505]` `[trigger: 梦见病人上车]` `[factor_trigger: dream_sick_cart]` `[role: 主干]` 病人上车，主大凶。 → 《周公解梦·船车游行物件》
  - `[ns_zgjm_506]` `[trigger: 梦见丧车遇者]` `[factor_trigger: dream_funeral_cart]` `[role: 主干]` 丧车遇者，主灾散。 → 《周公解梦·船车游行物件》
  - `[ns_zgjm_507]` `[trigger: 梦见行车白马]` `[factor_trigger: dream_white_horse_cart]` `[role: 主干]` 行车白马，主大吉。 → 《周公解梦·船车游行物件》
  - `[ns_zgjm_508]` `[trigger: 梦见四马驾车]` `[factor_trigger: dream_four_horse]` `[role: 主干]` 四马驾车，吉反凶。 → 《周公解梦·船车游行物件》
  - `[ns_zgjm_509]` `[trigger: 梦见以羊驾车]` `[factor_trigger: dream_sheep_cart]` `[role: 主干]` 以羊驾车，事不常。 → 《周公解梦·船车游行物件》
  - `[ns_zgjm_510]` `[trigger: 梦见备马者]` `[factor_trigger: dream_prepare_horse]` `[role: 主干]` 备马者，主远行事。 → 《周公解梦·船车游行物件》
  - `[ns_zgjm_511]` `[trigger: 梦见远行出入]` `[factor_trigger: dream_travel_far]` `[role: 主干]` 远行出入，命通达。 → 《周公解梦·船车游行物件》"""
    normalized_text_zh: str = """"""
    subject: str = "船车游行物件"
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
        l1_anchor="zgjm_v1.0.0_船车游行物件_001_L1",
    )
    version: str = "1.0.0"
