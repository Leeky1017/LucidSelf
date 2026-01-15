"""
Auto-generated semantic module for zhougong
Generated at: 2025-12-05T13:30:19.877721
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
    semantic_id="zgjm_v1.0.0_冢墓棺椁迎送_001",
    book_id="zhougong",
    engine_id="dream"
)
class 冢墓棺椁迎送(SemanticEntry):
    """
    - **原文（source_text）**：

  【类名】

  冢墓棺椁迎送。

  【条文】

  冢墓高者，大吉利。
  新冢棺椁，主忧除。
  冢墓上有云气，吉。

  冢墓门开，百事吉。
...
    """
    
    original_text: str = """- **原文（source_text）**：

  【类名】

  冢墓棺椁迎送。

  【条文】

  冢墓高者，大吉利。
  新冢棺椁，主忧除。
  冢墓上有云气，吉。

  冢墓门开，百事吉。
  冢墓上明，吉；暗，凶。
  冢墓生树，吉；折，凶。

  冢墓上开花，大吉。
  棺自出墓中，大吉。
  抬棺入宅，禄位至。

  死人出棺外，客至。
  开棺与死人言，凶。
  棺殓死人，主得财。

  见棺水上，大得财。
  空远无人，主远行。

- 分字分词释义：

  - **冢墓棺椁迎送**：本类总纲，“冢墓”指坟冢与墓地，“棺椁”指棺与外椁，“迎送”指丧葬礼中的迎来送往。整体围绕**祖坟气象、棺柩动静与丧葬迎送所示之吉凶**。
  - **冢墓高者大吉利；新冢棺椁主忧除；冢墓上有云气吉**：冢墓高起，象征基业与气势高昂，多主大吉；新冢与新棺椁多与新近丧事相关，梦中反主忧患消除；冢墓上有云气，多指祥瑞之气，主吉.
  - **冢墓门开百事吉；冢墓上明吉暗凶；冢墓生树吉折凶**：墓门打开象征阻隔除去，百事皆通；冢上光明则吉，昏暗则凶；冢上生树象征后代兴旺，折则有伤损之兆.
  - **冢墓上开花大吉；棺自出墓中大吉；抬棺入宅禄位至**：坟上花开，多主家运与后代发达；棺自墓中出，古解为旧事翻出反而见吉；抬棺入宅虽象凶景，却被解作禄位临门，主仕途之升迁.
  - **死人出棺外客至；开棺与死人言凶；棺殓死人主得财**：死人出棺，象征旧缘或旧事再临，多主外客来访；开棺与死人说话，则嫌触犯幽冥之界，故凶；棺中殓死人，反主得财.
  - **见棺水上大得财；空远无人主远行**：棺在水上，象征财物随流而至，古人解作大得财；“空远无人”描绘空旷远地，多主远行或远迁.

- **规范化释义（primary_lang_explained）**：

  本类通过冢墓高低、明暗、花树生长与棺柩出入等画面，呈现的并非单纯的死亡恐惧，而是**祖坟气运、家族兴衰与人生迁移**的象征：

  - 冢墓高起、门开光明、花树繁盛，多主家运顺遂、后代兴旺、百事皆吉.
  - 冢墓昏暗、树折、与死人言语，则偏向忧患、阻滞乃至凶象，需要防范.
  - 棺柩主动移动（出墓、入宅、在水上），往往象征旧缘、旧事与财禄的重新流动，有时反主大吉与禄位至.
  - “空远无人”的远景，则提示远行迁移与离乡之象.

- 核心要点：

  - **看冢墓之势：高、低、明、暗**：高与明多吉，暗与折多凶，反映祖坟与家族整体气场的状态.
  - **看花树生长与折损**：生长与开花主兴隆与大吉，折损则主后代或关键人物有伤损.
  - **看棺柩动静与方向**：棺出墓、入宅、在水上，多与禄位与财运相关，需结合当事人现实状态理解.
  - **看与死者互动方式**：死人出棺而来，多主外客至；若主动开棺与死人言，则涉干犯禁忌，偏凶.
  - **看“空远无人”的场景**：与其说是孤寂，不如说是远行与迁移的征兆，提示有离乡或远游之机缘.

- 详细解说：

  **（一）冢墓高低与门开：家族气场与百事通塞**

  - “冢墓高者大吉利；冢墓门开百事吉”：
    - 冢墓高起，象征地势与气势俱高，古人认为与祖上积德与后代兴盛相关，故大吉利；
    - 冢墓门开，则原本封闭之处得以畅通，百事吉，常被解为阻滞解除、道路打通.

  **（二）冢上明暗、云气与树木：兴旺与忧患**

  - “冢墓上明吉暗凶；冢墓上有云气吉；冢墓生树吉折凶”：
    - 冢上光明，象征阳气充足与家运通达，故吉；
    - 冢上昏暗，则阴气郁结，易有疾病或阻滞，故凶；
    - 冢上云气，多被视为祥瑞或祖先护佑，故吉；
    - 生树则象征生机与后代，折则警示子孙或骨干之人有损.

  **（三）花开与棺动：旧事再起与禄位临门**

  - “冢墓上开花大吉；棺自出墓中大吉；抬棺入宅禄位至”：
    - 冢上开花，将死亡之地与花开相连，偏向“枯木逢春”式的大吉；
    - 棺自出墓中，看似惊悚，实则被解作旧事重提后反得其利；
    - 抬棺入宅虽是不祥之景，却象征权柄与禄位进入家门，古解主禄位至.

  **（四）死人出棺与言语：外客与禁忌**

  - “死人出棺外客至；开棺与死人言凶；棺殓死人主得财”：
    - 死人出棺，多喻迟来或久未联络之人再次出现，故解为外客至；
    - 开棺与死人言，则主动触犯生死界限，古人视之为大凶，提示不可轻犯禁忌；
    - 棺中殓死人则象征事物归位与安顿，反主得财.

  **（五）棺在水上与空远无人：财与远行**

  - “见棺水上大得财；空远无人主远行”：
    - 棺在水上漂流，可理解为承载财物之舟，古解大得财，提示财运随势而来；
    - 空远无人则是远方之景，多主远行、迁徙或外出发展.


- **完整对等诠释（secondary_lang_full）**：

  This category gathers dreams involving graves, tomb mounds, coffins, and funeral processions. Rather than dwelling only on fear of death, it treats the height, brightness, and vitality of the tomb, as well as the movement of coffins, as images of ancestral fortune, family flourishing or decline, and major life transitions.

  Raised and well‑formed tombs, open tomb gates, clear light around the grave, and flowers or trees flourishing on the mound all point to strong roots and an auspicious family field. Such dreams suggest that the lineage is supported, obstacles are being removed, and descendants may prosper. New tombs and new coffins, although seemingly ominous, are often read as signs that recent worries or grief can now be laid to rest and transformed.

  The way coffins move is especially important. A coffin rising out of the grave, entering the house, or floating upon water indicates that something previously buried is coming back into play—old matters reopening, ancestral merit becoming active, or opportunities and wealth arriving. Carrying a coffin into the home can paradoxically signify rank and salary entering the household, while a coffin on the water suggests large gains flowing in from outside.

  Encounters with the dead reflect how the dreamer relates to what is past. The dead emerging from coffins or being spoken to directly can warn against overstepping the boundary between life and death, hinting at disputes, illness, or entanglement in unresolved issues. An empty, distant landscape with no one present, by contrast, often foreshadows travel, relocation, or a phase of life spent far from one's original home. Overall, this category teaches that images of tombs and coffins are less about literal death and more about the condition of family foundations and the cycles of ending, renewal, and movement in a person's fate.

- 校勘与字词辨析：

  - 本类原文多为"三句并列"体，如"冢墓高者大吉利　冢墓门开百事吉　冢墓上明吉利来"，本稿在 L1 层按句意拆分为独立句，并加标点，严格保留原有词序与字形。
  - "冢墓"与"坟墓"在本类中混用，本稿据底本保留原用字，不统一为现代"坟墓"。
  - "棺椁"二字，"棺"为内层，"椁"为外层，本稿按古礼制理解，不改作现代"棺材"。
  - "开棺与死人言主凶"句，本稿理解为"开启已封之棺与死者对话"之意，在详细解说中补充"阴阳界限被打破"的象征意涵。
  - 诸如"迎丧者主得财""见死亡尊长大吉"等看似反常之语，本稿在 L1 层保留原判词，在详细解说中以"旧局终结、祖先庇佑"等象征意涵补充说明。

  - **English**：
    - The original text in this category mostly follows the "three parallel phrases" format, e.g. "冢墓高者大吉利　冢墓门开百事吉　冢墓上明吉利来." This edition splits them by meaning into independent sentences at the L1 layer, adding punctuation while strictly preserving the original word order and character forms.
    - The terms "冢墓" and "坟墓" are used interchangeably in this category. This edition preserves the original characters per the base text without unifying them to the modern "坟墓."
    - For "棺椁," the "棺" is the inner coffin and "椁" is the outer casket. This edition understands them according to ancient ritual conventions, not changing to modern "棺材."
    - The phrase "开棺与死人言主凶" is understood as "opening a sealed coffin to converse with the deceased," supplemented in the detailed commentary with the symbolic meaning of "boundaries between yin and yang being broken."
    - Seemingly contradictory phrases like "迎丧者主得财" and "见死亡尊长大吉" are preserved in original verdict form at the L1 layer, with symbolic meanings like "old situations ending, ancestral blessings" supplemented in the detailed commentary.



- **叙事素材（narrative_snippets）**：

  - `[ns_zgjm_592]` `[trigger: 梦见冢墓高者]` `[factor_trigger: dream_tomb_high]` `[role: 主干]` 冢墓高者，大吉利。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_593]` `[trigger: 梦见新冢棺椁]` `[factor_trigger: dream_new_tomb]` `[role: 主干]` 新冢棺椁，主忧除。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_594]` `[trigger: 梦见冢墓上有云气]` `[factor_trigger: dream_tomb_cloud]` `[role: 主干]` 冢墓上有云气，吉。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_595]` `[trigger: 梦见冢墓门开]` `[factor_trigger: dream_tomb_open]` `[role: 主干]` 冢墓门开，百事吉。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_596]` `[trigger: 梦见冢墓上明]` `[factor_trigger: dream_tomb_bright]` `[role: 主干]` 冢墓上明吉，暗凶。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_597]` `[trigger: 梦见冢墓生树]` `[factor_trigger: dream_tomb_tree]` `[role: 主干]` 冢墓生树吉，折凶。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_598]` `[trigger: 梦见冢墓上开花]` `[factor_trigger: dream_tomb_flower]` `[role: 主干]` 冢墓上开花，大吉。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_599]` `[trigger: 梦见棺自出墓中]` `[factor_trigger: dream_coffin_out]` `[role: 主干]` 棺自出墓中，大吉。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_600]` `[trigger: 梦见抬棺入宅]` `[factor_trigger: dream_coffin_enter]` `[role: 主干]` 抬棺入宅，禄位至。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_601]` `[trigger: 梦见死人出棺]` `[factor_trigger: dream_dead_coffin]` `[role: 主干]` 死人出棺，外客至。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_602]` `[trigger: 梦见开棺与死人言]` `[factor_trigger: dream_open_coffin_speak]` `[role: 主干]` 开棺与死人言，凶。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_603]` `[trigger: 梦见棺殓死人]` `[factor_trigger: dream_coffin_bury]` `[role: 主干]` 棺殓死人，主得财。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_604]` `[trigger: 梦见见棺水上]` `[factor_trigger: dream_coffin_water]` `[role: 主干]` 见棺水上，大得财。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_605]` `[trigger: 梦见空远无人]` `[factor_trigger: dream_empty_far]` `[role: 主干]` 空远无人，主远行。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_1008]` `[trigger: 梦见群斗]` `[factor_trigger: dream_fight_together]` `[role: 主干]` 梦见群斗，主有争。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_1009]` `[trigger: 梦见火明]` `[factor_trigger: dream_fire_bright]` `[role: 主干]` 梦见火明，主大吉。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_1010]` `[trigger: 梦见火烧屋]` `[factor_trigger: dream_fire_burning_house]` `[role: 主干]` 梦见火烧屋，主兴旺。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_1011]` `[trigger: 梦见鱼在水]` `[factor_trigger: dream_fish_in_water]` `[role: 主干]` 梦见鱼在水，主有财。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_1012]` `[trigger: 梦见财运]` `[factor_trigger: dream_fortune]` `[role: 主干]` 梦见财运，主得财。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_1013]` `[trigger: 梦见运转]` `[factor_trigger: dream_fortune_turn]` `[role: 主干]` 梦见运转，主转机。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_1014]` `[trigger: 梦见自由]` `[factor_trigger: dream_freedom]` `[role: 主干]` 梦见自由，主脱厄。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_1015]` `[trigger: 梦见富贵]` `[factor_trigger: dream_fugui]` `[role: 主干]` 梦见富贵，主大吉。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_1016]` `[trigger: 梦见福禄]` `[factor_trigger: dream_fulu]` `[role: 主干]` 梦见福禄，主吉祥。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_1017]` `[trigger: 梦见父母凶]` `[factor_trigger: dream_fumu_xiong]` `[role: 主干]` 梦见父母凶，主有忧。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_1018]` `[trigger: 梦见父母忧]` `[factor_trigger: dream_fumu_you]` `[role: 主干]` 梦见父母忧，主有难。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_1019]` `[trigger: 梦见丧葬]` `[factor_trigger: dream_funeral]` `[role: 主干]` 梦见丧葬，主有变。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_1020]` `[trigger: 梦见得利]` `[factor_trigger: dream_gain]` `[role: 主干]` 梦见得利，主有财。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_1021]` `[trigger: 梦见得权]` `[factor_trigger: dream_gain_power]` `[role: 主干]` 梦见得权，主升迁。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_1022]` `[trigger: 梦见得笔砚]` `[factor_trigger: dream_get_brush_inkstone]` `[role: 主干]` 梦见得笔砚，主文贵。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_1023]` `[trigger: 梦见得金器]` `[factor_trigger: dream_get_goldware]` `[role: 主干]` 梦见得金器，主大吉。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_1024]` `[trigger: 梦见得钥]` `[factor_trigger: dream_get_key]` `[role: 主干]` 梦见得钥，主有喜。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_1025]` `[trigger: 梦见得环]` `[factor_trigger: dream_get_ring]` `[role: 主干]` 梦见得环，主婚姻。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_1026]` `[trigger: 梦见得丝]` `[factor_trigger: dream_get_silk]` `[role: 主干]` 梦见得丝，主有财。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_1027]` `[trigger: 梦见得兵器]` `[factor_trigger: dream_get_weapon]` `[role: 主干]` 梦见得兵器，主有权。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_1028]` `[trigger: 梦见鬼打]` `[factor_trigger: dream_ghost_beat]` `[role: 主干]` 梦见鬼打，主大凶。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_1029]` `[trigger: 梦见鬼索食]` `[factor_trigger: dream_ghost_seeking_food]` `[role: 主干]` 梦见鬼索食，主凶兆。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_1030]` `[trigger: 梦见神女合]` `[factor_trigger: dream_goddess_union]` `[role: 主干]` 梦见神女合，主大吉。 → 《周公解梦·冢墓棺椁迎送》
  - `[ns_zgjm_1031]` `[trigger: 梦见金明]` `[factor_trigger: dream_gold_bright]` `[role: 主干]` 梦见金明，主有财。 → 《周公解梦·冢墓棺椁迎送》"""
    normalized_text_zh: str = """"""
    subject: str = "冢墓棺椁迎送"
    factor_refs: list = ['zgjm_16_tomb_high_proposal', 'zgjm_16_tomb_gate_open_proposal', 'zgjm_16_tomb_light_state_proposal', 'zgjm_16_tomb_tree_state_proposal', 'zgjm_16_tomb_blossom_proposal', 'zgjm_16_coffin_emerge_proposal', 'zgjm_16_coffin_into_house_proposal', 'zgjm_16_coffin_water_farland_proposal']
    
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
        l1_anchor="zgjm_v1.0.0_冢墓棺椁迎送_001_L1",
    )
    version: str = "1.0.0"
