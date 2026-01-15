"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.436383
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
    semantic_id="smth_v1.0.0_女命总论与夫子兴衰之纲_001",
    book_id="sanming",
    engine_id="bazi"
)
class 女命总论与夫子兴衰之纲(SemanticEntry):
    """
    - 原文（source_text）：

  论女命。

  或问：妇人何利？利在夫星。夫利，其妇必利；夫困，其妇必困。妇人从夫，先观夫星，以定出身之贵贱；再看子星，以察晚年之荣辱。官煞财得地者，夫利也...
    """
    
    original_text: str = """- 原文（source_text）：

  论女命。

  或问：妇人何利？利在夫星。夫利，其妇必利；夫困，其妇必困。妇人从夫，先观夫星，以定出身之贵贱；再看子星，以察晚年之荣辱。官煞财得地者，夫利也；食神得地者，子利也。夫利则出身富贵，一生享福；子利则晚年厚养，褒宠诰封。然亦有旺夫者，以食生财，财生官故耳，反是则否。

  女命以克我者为夫，我生者为子，皆要得时，乘生旺之气。若旺气只聚于时，亦可用官为夫，不要见煞；用煞为夫，不要见官，一位为好。有两位官星，无煞以杂之；四柱纯煞，无官以混之，俱为良妇。更得本身自旺尤佳，但旺不可太过。食为子息，引时逢旺，再得二德扶身，乃夫贵子荣之命。不宜身旺，而重叠暗藏夫神及伤官、七煞、魁罡相刑，羊刃太重，合多有情，皆主不美，岁运亦然。看有八法八格，须细详之。

- 分字分词释义：

  - **妇人何利？利在夫星**：在传统社会结构中，女命的社会地位与物质境况多系于夫星兴衰，此乃古法出发点。
  - **克我者为夫，我生者为子**：女命以克日主之官、煞为夫星，以日主所生之食、伤为子星。
  - **官煞财得地**：官星、七煞与财星得令得地，代表夫道有根、家计可托。
  - **食神得地**：食神旺而得地，象征子息有福、有养。
  - **两位官星 / 四柱纯煞**：或多官无煞杂之，或纯煞一局而不杂官，皆属“夫星纯粹”，古人以此为良妇之象。
  - **二德扶身**：多指天德、月德等吉神扶助日主，使其性情柔和而不至偏激。

- **规范化释义（primary_lang_explained）**：

  本节为女命总纲。作者首先从古代“妇人从夫”的观念出发，认为女命的利害多系于夫星：夫星得地、财星有力，则出身与婚后生活多享富贵；子星（食神）得地，则晚年有子孙承欢、得以养老。进一步则以“克我为夫、我生为子”为原则，说明如何在四柱中寻找夫星与子星，并强调：  
  - 夫星宜纯而有力，不宜杂乱冲破；  
  - 子星宜得时得地，不宜全失气；  
  - 日主自旺而不过，方能承载夫子之福。  

  同时也指出若身旺过甚、暗藏过多夫星与伤官、七煞、魁罡、羊刃等刑克之神，往往在婚姻与子嗣方面多有波折，是女命需要特别警惕之处。末段提到“八法八格”，为后文诸格局（纯、和、清、贵、浊、滥、娼、淫、旺夫克子等）的纲目。

- 核心要点：

  - 女命看夫先看夫星（官煞）与财星，先定“夫利不利”，再看子星（食神）定“子利不利”。
  - 克我者为夫、我生者为子：夫星与子星的取用顺序与男命有别。
  - 夫星以**纯而得地**为佳：要么官星一位而不见煞，要么纯煞一局而不杂官。
  - 身旺有度是前提：旺而不暴，则能承载夫子两端之福；身太弱或太强，皆易致婚姻与子嗣波动。

- 详细解说：

  1. **关于“妇人从夫”的时代背景**  
     本节写作于以宗法、男纲为中心的时代，因此强调“妇人从夫”。在今日阅读时，可将“夫星”理解为与伴侣、婚姻关系以及共同生活资源有关的象，而不必拘泥于性别单向的从属。

  2. **夫星与子星的取用逻辑**  
     - 夫星（官煞）代表伴侣、配偶一方以及与之相关的权力、资源与责任；  
     - 子星（食神、部分伤官）代表子女与由自己“生出”的成果，包括作品、学生与后辈。  
     本节强调：  
     - 女命以夫、子两端的兴衰来衡量整体福分；  
     - 夫利而子亦利，则一生多有倚靠与晚年承欢。

  3. **“良妇”与“旺夫”的结构特征**  
     - “两位官星无煞以杂，四柱纯煞无官以混”所说的，是夫星在结构上要纯，避免官煞混乱、反覆争合；  
     - 身旺适度则能承夫星之重，甚至形成“食生财、财生官”的旺夫格局：即自身能力（食神）推动财富（财星），再反过来成就伴侣与共同事业。

     - 若身旺过甚，又暗藏多重夫星，加上伤官、七煞、魁罡、羊刃等刑克之神，容易表现为感情纠结、关系强势、婚姻反覆；  
     - 若夫星太弱或被制伤严重，则伴侣端多有奔波、病困、事业不稳之虞。

  纯者一也。如纯一官星，或纯一煞星，有财有印，不值刑冲，不相混杂是也。如癸已、戊午、辛酉、丙申，本身专禄，旺不从化。辛用丙官为夫星，五月火旺夫健。丙用癸为官，坐贵见戊为食，同归禄于巳。辛金生癸水为子，引入申时长生之地。天干癸戊辛丙，水火既济；地支巳午酉申，拱夹财库，所以嫁夫为官，食天禄，夫荣子贵之命。

- 分字分词释义：

  - **纯者一也**：纯，指结构上单一、不杂乱；或纯一官，或纯一煞，而不互相混杂。
  - **纯一官星 / 纯一煞星**：全命局只一位官星或一位七煞为夫星，不再有其他官煞搅扰.
  - **有财有印，不值刑冲**：财星能生官，印星能护身，且不受刑冲破坏，为佳格关键条件.
  - **本身专禄，旺不从化**：日主自坐禄地，自身旺而不从，从而能承载夫星之力.

- **规范化释义（primary_lang_explained）**：

  “纯”格强调的是结构的单一与清楚：

  - 或只一位官星作夫，或只一位七煞作夫；
  - 命局中财星、印星相配，却不见多重官煞、刑冲混杂来破格.

  以例命癸巳、戊午、辛酉、丙申为说明：辛金自坐酉禄，身旺不从；
  - 以丙火为官为夫，五月火旺，夫健而有力；
  - 丙以癸为官，癸又见戊食，官食互资；
  - 辛金生癸水为子星，引入申时长生，子息亦得其地.

  天干癸戊辛丙水火既济，地支巳午酉申拱夹财库，因此原文以“嫁夫为官，食天禄，夫荣子贵”概其象.

- **完整对等诠释（secondary_lang_full）**：

  This pattern called "Pure" focuses on structural clarity in a woman's chart. Either a single Direct Officer or a single Seven Killings acts as the spouse star, and that lone spouse star stands at the centre of the relationship axis, without being entangled in competing candidates. Wealth and Seal stars surround it in a supportive way rather than pulling the structure apart, so that resources and protection both flow toward the marital bond.

  In the example chart Jia Water, Wu Earth, Xin Metal, and Bing Fire work together in a balanced Water–Fire configuration. Xin Metal Day Master sits on its own Lu (salary) position in You, so the self is strong enough not to collapse into dependence. Bing Fire, as the spouse star, is seasonally powerful in the fifth lunar month and receives nourishment from Wealth and support from Seal, representing a partner who is capable, visible, and able to stand in public roles. Xin Metal gives birth to Gui Water as the child star, and that child star in turn reaches its Changsheng (birth) position in Shen, indicating that the child line also has room to grow.

  Rather than promising guaranteed rank or titles, the Pure pattern describes a relationship field where the spouse role is unmixed and clearly defined, resources are not overly scattered, and both partner and children can be supported by a stable backbone. For modern readers, it points to a configuration where emotional focus and life resources converge on one primary relationship, with enough internal strength on the part of the Day Master to sustain that commitment without losing a sense of self.

- 核心要点：

  - “纯”重在**结构干净**：一官或一煞为夫，不杂乱.
  - 财、印俱备，既能生夫星，又能资身护身.
  - 日主自旺、坐禄，为能承夫、育子的前提.

- 详细解说：

  在女命判断中，“纯一夫星”多被视作婚姻关系相对单纯、重心明确的格局：

  1. **夫象集中**  
     - 只一位官或煞为夫星，象征伴侣角色相对清楚，不易出现多方纠缠；  
     - 若夫星得地有力，则多主伴侣本身有地位、有担当.

  2. **辅助星协调**  
     - 财星为夫之养分，印星为自身根气，两者齐备，则既能旺夫又不损己；  
     - 不值刑冲破害，则格局较为稳定，不容易因外界变故而大起大落.

  3. **身旺而不过**  
     - 身太弱则不能任夫星之重，身太旺又易反客为主，皆非“纯格”本意；  
     - 以身旺中和为宜，既能支持伴侣，又能保持自我.

  现代视角下，可将“纯一官 / 煞”理解为在情感与婚姻中目标明确、不多头试探；财印齐备则象征在关系中既能提供支持，又不会因过度牺牲而失去自身发展.

- 校勘与字词辨析：

  - 原例命中“水火既济、拱夹财库”的说法，本稿仅取其为水火调和、财库稳固之象，不以此作具体级别断语.
  - “嫁夫为官，食天禄，夫荣子贵”一类辞句，本稿在白话中化为“伴侣有职、有禄，子女亦有发展潜力”，以免读者误以为必然高官厚禄.
  - **English**：
    - Spirit-star (shensha) terms demystified; fortune cycle descriptions treated as developmental tendencies.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_07_009]` `[trigger: 女命总纲]` `[factor_trigger: nvming_fuxing_linian]` `[role: 主干]` 妇人何利？利在夫星。夫利，其妇必利；夫困，其妇必困。 → 《三命通会》卷七#女命总论
  - `[ns_smth_07_010]` `[trigger: 克我为夫]` `[factor_trigger: ke_wo_wei_fu AND wo_sheng_wei_zi]` `[role: 主干依赖]` 女命以克我者为夫，我生者为子，皆要得时，乘生旺之气。 → 《三命通会》卷七#女命总论
  - `[ns_smth_07_011]` `[trigger: 纯官纯煞]` `[factor_trigger: liangwei_guanxing OR chunsha_wuguan]` `[role: 条件分支]` 有两位官星，无煞以杂之；四柱纯煞，无官以混之，俱为良妇。 → 《三命通会》卷七#女命总论
  - `[ns_smth_07_012]` `[trigger: 夫贵子荣]` `[factor_trigger: fu_gui_zi_rong]` `[role: 总结]` 乃夫贵子荣之命。 → 《三命通会》卷七#女命总论"""
    normalized_text_zh: str = """"""
    subject: str = "女命总论与夫子兴衰之纲"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_89', 'bazi_semantic', 'bazi_state_day_master_zi', 'bazi_semantic', 'bazi_relation_factor_139', 'bazi_semantic', 'bazi_zi_1', 'bazi_semantic', 'source_ref', 'rel_smth_07_004', 'fuxing_jiegou_chundu', 'rel_smth_07_005', 'caiyin_zhichi', 'rel_smth_07_006', 'fuzi_fazhan_qianli', 'evi_smth_07_004', 'fuxing_jiegou_chundu', 'rule_fuxing', 'evi_smth_07_005', 'caiyin_zhichi', 'rule_caiguan', 'evi_smth_07_006', 'fuzi_fazhan_qianli', 'rule_zixing', 'map_smth_07_003', 'map_smth_07_004']
    
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
        l1_anchor="smth_v1.0.0_女命总论与夫子兴衰之纲_001_L1",
    )
    version: str = "1.0.0"
