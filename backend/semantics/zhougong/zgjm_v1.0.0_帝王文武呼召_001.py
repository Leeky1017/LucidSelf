"""
Auto-generated semantic module for zhougong
Generated at: 2025-12-05T13:30:19.864320
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
    semantic_id="zgjm_v1.0.0_帝王文武呼召_001",
    book_id="zhougong",
    engine_id="dream"
)
class 帝王文武呼召(SemanticEntry):
    """
    - **原文（source_text）**：

  【类名】

  帝王文武呼召。

  【条文】

  帝王宣召，有惊喜。
  后妃呼召，饮有疾。
  太子召，大喜吉利。

  天子赐坐，有财吉。
...
    """
    
    original_text: str = """- **原文（source_text）**：

  【类名】

  帝王文武呼召。

  【条文】

  帝王宣召，有惊喜。
  后妃呼召，饮有疾。
  太子召，大喜吉利。

  天子赐坐，有财吉。
  见老君言，有仙分。
  拜佛欲动，大有财。

  看火上陈事，大吉。
  神佛嗔怒，皆不吉。
  王侯并坐，大吉利。

  来见贵人，不得凶。
  与圣贤说话，大吉。
  使命入门，大吉利。

  白衣召作，便死亡。
  拜尊长者，有吉庆。
  先祖考言，求食吉。

  人云大好者，即凶。
  人云死者，得长命。
  人在外呼之，招凶。

  我欲共汝去，大凶。
  人云不用汝，大吉。
  与恶人言，主口舌。

  被杀害，吉；伏藏，凶。
  身生羽翼，飞大吉。
  身逃去，得脱病去。

  与人交易，主有疾。
  贫穷兵居，主大吉。
  合伴同行，凶事至。

  一切贵人，皆吉祥。

- 分字分词释义：

  - **帝王文武呼召**：本类总纲，统摄帝王、后妃、太子、王侯、贵人，以及神佛仙真与先祖的“呼召与言语”，主要映照**权力与命令、贵人缘分、生死消息与口舌是非**。
  - **帝王宣召，有惊喜；太子召，大喜吉利**：帝王、太子亲自宣召，多主仕途或人生节点有突然的好转机会，带有“非比寻常”的惊喜色彩。
  - **后妃呼召，饮有疾**：被后妃呼唤入内饮宴，古解多主宴饮、情欲之事致病，提示“近色伤身”“饮食失节”的隐忧。
  - **天子赐坐，有财吉；王侯并坐，大吉利**：受天子赐坐、与王侯同席而坐，皆为“同列权位”的吉象，多主受重用、得财得势。
  - **见老君言，有仙分；拜佛欲动，大有财**：与太上老君交谈、向佛礼拜而有行动，多主与修行、福报相关：
    - “有仙分”偏向性情超脱、与修道有缘；
    - “大有财”则是以福德换财利之象。
  - **看火上陈事，大吉；神佛嗔怒，皆不吉**：
    - “火上陈事”多解为在神前或灯火前陈诉事由，得神明见察，主大吉；
    - 若梦中神佛震怒，则是违礼、失德之征，凶意明显。
  - **来见贵人不得凶；与圣贤说话大吉；使命入门大吉利**：
    - 主动来见贵人，多主有贵人可依；
    - 与圣贤谈话，象征得教诲与指引；
    - 接受使命入门，则为正式受托之象。
  - **白衣召作便死亡；人在外呼之招凶；我欲共汝去大凶**：
    - “白衣召作”常被视为“白衣使者”召人，主死亡之凶；
    - 在外被人呼唤同行，多为被牵连入不利局势；
    - 有人邀你“共去”而梦感不安，多从凶占。
  - **拜尊长者有吉庆；先祖考言求食吉**：
    - 拜见尊长，多主得其祝福与支持；
    - 先祖开口言语求食，为典型祭祀之象，提醒梦者祭奠供养，可得吉庆。
  - **人云大好者即凶；人云死者得长命**：为“言语相反”的两句，古人认为：
    - 他人轻言大好，反恐其中藏凶；
    - 若梦中闻人言“你将死”，反主长命，属于“极言而反”之占法。
  - **人云不用汝大吉**：他人说“暂不用你”，反主不被卷入当下凶局，得以远祸全身。
  - **与恶人言主口舌**：与品行恶劣者言语往来，主招惹是非与口舌官非。
  - **被杀害吉；伏藏凶**：
    - “被杀害”反占为吉，常解作“旧我被除、灾祸止于此身”；
    - “伏藏”则主匿迹藏形、积压问题，反为凶兆。
  - **身生羽翼飞大吉；身逃去得脱病去**：
    - 羽翼生而能飞，象征超脱困境与提升层次；
    - 身逃去则是摆脱灾病与牢系之象。
  - **与人交易主有疾；贫穷兵居主大吉；合伴同行凶事至**：
    - 交易之梦在本类偏凶，多与劳神奔波、疾病牵累相关；
    - “贫穷兵居”反言居于简陋兵舍，远离奢靡，反主大吉；
    - 合伴同行则提示“同伴共赴险地”，凶事易至。
  - **一切贵人皆吉祥**：总括本类，凡真贵人之护持，多属吉象，但仍须分辨真伪与善恶。

- **规范化释义（primary_lang_explained）**：

  本类以“帝王文武呼召”为纲，收摄了**帝王贵人、尊长先祖、神佛仙真以及各类言语召唤**的梦象。其核心在于：

  - 谁在呼召你（帝王、贵人、白衣、恶人）；
  - 以何种语气与内容呼唤（大好、死亡、不用汝）；
  - 在什么场合与位置被召（宫廷、神前、门内门外）。

  大体而言：

  - **受帝王、王侯、尊长、圣贤与先祖和善召见，主得贵人扶持与家门荫庇。**
  - **受神佛嘉许、火前陈事者，多主福德增长与财名并进；若神佛震怒，则为戒惕之梦。**
  - **被白衣、恶人或在外暗中呼唤，多与凶事牵连、生死消息与口舌官非相关。**
  - **被杀、长翅高飞、逃脱之梦，多为“以险解险”的象，旧祸既终，新局将开。**

- 核心要点：

  - **看“召唤者身份”——帝王贵人 vs 白衣恶人：**
    - 帝王、太子、王侯、尊长与圣贤之召，多主承命、受教与得势；
    - 白衣召作、恶人相呼、多在外呼之，则提示被牵向凶险之境。
  - **看“言语内容”——大好与死亡的反占：**
    - 直言“大好”反主恐有隐藏之凶；
    - 言“将死”反主长命，是古籍中典型的“反言占法”；
    - 人云“不用汝”，反为远祸之吉象。
  - **看“所在场域”——宫廷、神前、门内门外：**
    - 在宫殿、尊长或神佛之前受召，多属正式场域，重在命分与福德；
    - 门外被呼唤或暗中招呼，则多与意外招灾、卷入事变相关。
  - **看“自身状态”——被杀、长翅、逃脱：**
    - 被杀反吉、身生羽翼、身逃去，皆指“旧局结束、新局开启”，多与病愈、脱险、转运有关；
    - 伏藏不出，则为“避而不解”的凶象。
  - **看“日常往来”——交易、贫居、合伴：**
    - 交易多劳神，反映健康受损或忧患增多；
    - 贫居兵舍、清苦处反得清吉；
    - 轻率合伴同行，特别是去向不明之处，则是“同赴凶地”的象征。

- 详细解说：

  **（一）帝王、太子与王侯之召：权力中心的召见**

  - “帝王宣召有惊喜”“太子召大喜吉利”“天子赐坐有财吉”“王侯并坐大吉利”等条，共同构成了“被权力中心看见与召见”的格局：
    - 对仕途而言，是得朝廷重视、受高位者点名之象；
    - 对平民而言，则可视为在机构、公司或集体中获得上级认可。
  - 此类梦中，若梦者神情镇定、衣冠整齐，则多主可堪其任；若战战兢兢或失仪失态，则提醒现实中需补足能力与礼数。
  - “拜尊长者有吉庆”“来见贵人不得凶”说明，对尊长与贵人的主动礼敬也会化为吉祥之兆，现实中可对应主动请教、尊师重道。

  **（二）神佛仙真与先祖呼唤：福德与戒惕并行**

  - “见老君言有仙分”“拜佛欲动大有财”“看火上陈事大吉”指向：
    - 与神佛仙真相遇而和颜悦色，多主福德加持与财名并进；
    - 于火前陈事，是把心事托付于上，得天听之象。
  - 与之相对，“神佛嗔怒皆不吉”提醒：若在梦中被神佛呵斥、怒目，则应自省最近在道德、承诺与敬畏之心上的缺失。
  - “先祖考言求食吉”则表现为祖先开口索食：
    - 一方面提醒梦者注意祭祀与孝道；
    - 另一方面也象征家族传统与资源仍可滋养后人。

  **（三）言语的反占：大好与死亡的两极转换**

  - “人云大好者即凶”警示：凡事若只闻溢美之词、不见实际支撑，反需警惕其中隐藏的风险，如骗局、泡沫或假承诺。
  - “人云死者得长命”则属于以极言反占：
    - 古人认为梦中被宣判“将死”，往往表示此一大劫在梦中象征性地演过，现实中反能延寿；
    - 但对身弱多病者，仍需结合具体状况看待，不宜完全当作放心签。
  - “人云不用汝大吉”说明，有时被排除出局反而是福：没有被卷入正在酝酿的风暴，得以全身远祸。

  **（四）白衣、恶人与在外之呼：潜在危险的信号**

  - “白衣召作便死亡”在传统中多联想到“白衣使者”“阴曹差役”，故主死亡与重凶：现实中可理解为对危险邀约、可疑机会的提醒。
  - “人在外呼之招凶”“我欲共汝去大凶”则共同指向：
    - 若在偏僻或不安之地被人呼唤同行，多主被牵连入风险事件；
    - 梦中强烈不愿意跟随，则提醒现实中要坚持自己的直觉界限。
  - “与恶人言主口舌”则更直接：与品行不端者多言谈，易生口舌、纠纷乃至官非，现实中宜择友慎言。

  **（五）生死、逃脱与日常事务：以险解险的象法**

  - “被杀害吉伏藏凶”所示：
    - 表面上遭遇极端之事，实际多为“旧祸止于此”的象征，类似“以身代灾”；
    - 伏藏则表示问题被压入地下、未得解决，易日后复燃。
  - “身生羽翼飞大吉”“身逃去得脱病去”：
    - 羽翼象征能力与自由度提升，能超越原有环境的束缚；
    - 逃脱则是从病苦、困局中脱身，宜配合现实中的积极治疗与决断。
  - “与人交易主有疾”“贫穷兵居主大吉”“合伴同行凶事至”则回到日常：
    - 交易过多、计较太重，易损气伤身；
    - 清苦兵舍虽不华丽，却多有规矩与节制，反而生吉；
    - 轻率合伴同行，特别是去向不明之处，则是“同赴凶地”的象征。



- **完整对等诠释（secondary_lang_full）**：

  This category gathers dream omens relating to summons and speech from emperors, royalty, nobles, officials, sages, ancestors, and deities. The dreams interpret **authority and command, noble patronage, life-and-death messages, and verbal disputes**.

  The core interpretive principle centers on who issues the summons (emperor, sage, white-robed messenger, or villain), what tone and words are used (declaring "great fortune" or "death"), and where the call takes place (court, shrine, inside or outside the gate). Generally, being summoned by emperors, princes, elders, sages, or ancestors in a benevolent manner portends gaining powerful backing and family blessings. Approval by deities or presenting matters before sacred flames indicates growing merit and advancing wealth and reputation; divine wrath signals a warning dream. Being called by white-robed figures, villains, or mysterious voices from outside typically links to misfortune, news of life and death, and entanglement in disputes. Dreams of being killed, sprouting wings to fly, or escaping often operate on the principle of "danger resolving danger"—the old calamity ends and a new chapter opens.

  **Key interpretive axes**:
  - **Caller's identity**: emperor, prince, elder, or sage summons indicate receiving mandates, teachings, and advancement; white-robed callers, villains, or voices from outside warn of being drawn toward peril.
  - **Content of speech**: direct praise of "great fortune" paradoxically warns of hidden danger; hearing "you will die" paradoxically portends long life—a classic "reverse-word divination" in the ancient texts; being told "you are not needed" actually means escaping disaster.
  - **Location of the call**: courts, shrines, or ancestral halls are formal domains focusing on destiny and merit; calls from outside the gate or in shadows relate to unexpected calamities or entanglement in crises.
  - **Dreamer's state**: being killed yet auspicious, growing wings, escaping—all indicate "old situation ending, new situation beginning," often linked to recovery, escape from danger, or turning fortune.- 校勘与字词辨析：

  - 原文本类多以三句连写，如“帝王宣召有惊喜　后妃呼召饮有疾　太子召大喜吉利”“人云大好者即凶　人云死者得长命　人在外呼之招凶”等，本稿在 L1 层将其拆分为独立句并加标点，仅为阅读与后续处理方便，不改动原字序与用词.
  - “白衣召作便死亡”一句，传统多以“白衣”指代阴差或丧服，本稿不作服制考证，仅从“被白衣召唤近于死域”之象释义.
  - “看火上陈事大吉”中“火上陈事”，各本或作“向火上陈事”等，今多解为在神前灯火下陈述事由，本稿按此理解，不另改字.
  - “被杀害吉伏藏凶”一语，是典型的“以险解险”与“避而不解”并列，本稿在释义与详细解说中加以阐明，仍保留原文的吉凶判断方式.
  - “贫穷兵居主大吉”表面乖张，本稿按“清苦自守、远离奢靡而得吉”的思路解释，不牵及具体历史背景.
  - “一切贵人皆吉祥”作为本类收尾语，古籍中有“贵人多吉”之倾向，本稿在 L1 层忠实记录，同时在释义中强调需分辨真伪与善恶，以便后续高阶语义层补充现代视角.

  - **English**：
    - The original text presents entries in groups of three consecutive phrases, e.g. "帝王宣召有惊喜　后妃呼召饮有疾　太子召大喜吉利" and "人云大好者即凶　人云死者得长命　人在外呼之招凶." This edition splits them into independent sentences with punctuation for reading convenience, without altering the original word order.
    - In "白衣召作便死亡," the term "白衣" traditionally refers to underworld messengers or mourning clothes. This edition does not research costume history, simply interpreting it as "being summoned by white-clad figures approaches the realm of death."
    - In "看火上陈事大吉," the phrase "火上陈事" appears in some versions as "向火上陈事," generally interpreted as presenting matters before sacred altar flames. This edition follows this understanding without changing characters.
    - The phrase "被杀害吉伏藏凶" exemplifies the parallel presentation of "danger resolving danger" and "avoidance without resolution." This edition explains it in the interpretation and detailed commentary while preserving the original's fortune-misfortune judgment style.
    - "贫穷兵居主大吉" appears contradictory on the surface. This edition interprets it as "maintaining simplicity and avoiding extravagance brings good fortune," without invoking specific historical contexts.
    - "一切贵人皆吉祥" serves as the closing statement of this category; ancient texts tend toward "noble persons bring fortune." The L1 layer faithfully records this while emphasizing in the interpretation the need to distinguish authenticity and virtue, allowing higher semantic layers to add modern perspectives.



- **叙事素材（narrative_snippets）**：

  - `[ns_zgjm_148]` `[trigger: 梦见帝王宣召]` `[factor_trigger: dream_emperor_summon]` `[role: 主干]` 帝王宣召，有惊喜。 → 《周公解梦·帝王文武呼召》
  - `[ns_zgjm_149]` `[trigger: 梦见后妃呼召]` `[factor_trigger: dream_consort_summon]` `[role: 主干]` 后妃呼召，饮有疾。 → 《周公解梦·帝王文武呼召》
  - `[ns_zgjm_150]` `[trigger: 梦见太子召]` `[factor_trigger: dream_prince_summon]` `[role: 主干]` 太子召，大喜吉利。 → 《周公解梦·帝王文武呼召》
  - `[ns_zgjm_151]` `[trigger: 梦见天子赐坐]` `[factor_trigger: dream_emperor_seat]` `[role: 主干]` 天子赐坐，有财吉。 → 《周公解梦·帝王文武呼召》
  - `[ns_zgjm_152]` `[trigger: 梦见老君言]` `[factor_trigger: dream_laozi_speak]` `[role: 主干]` 见老君言，有仙分。 → 《周公解梦·帝王文武呼召》
  - `[ns_zgjm_153]` `[trigger: 梦见拜佛欲动]` `[factor_trigger: dream_worship_buddha]` `[role: 主干]` 拜佛欲动，大有财。 → 《周公解梦·帝王文武呼召》
  - `[ns_zgjm_154]` `[trigger: 梦见看火上陈事]` `[factor_trigger: dream_fire_petition]` `[role: 主干]` 看火上陈事，大吉。 → 《周公解梦·帝王文武呼召》
  - `[ns_zgjm_155]` `[trigger: 梦见神佛嗔怒]` `[factor_trigger: dream_deity_angry]` `[role: 主干]` 神佛嗔怒，皆不吉。 → 《周公解梦·帝王文武呼召》
  - `[ns_zgjm_156]` `[trigger: 梦见王侯并坐]` `[factor_trigger: dream_nobles_sit]` `[role: 主干]` 王侯并坐，大吉利。 → 《周公解梦·帝王文武呼召》
  - `[ns_zgjm_157]` `[trigger: 梦见来见贵人不得]` `[factor_trigger: dream_noble_reject]` `[role: 主干]` 来见贵人不得，凶。 → 《周公解梦·帝王文武呼召》
  - `[ns_zgjm_158]` `[trigger: 梦见与圣贤说话]` `[factor_trigger: dream_sage_talk]` `[role: 主干]` 与圣贤说话，大吉。 → 《周公解梦·帝王文武呼召》
  - `[ns_zgjm_159]` `[trigger: 梦见使命入门]` `[factor_trigger: dream_messenger_enter]` `[role: 主干]` 使命入门，大吉利。 → 《周公解梦·帝王文武呼召》
  - `[ns_zgjm_160]` `[trigger: 梦见白衣召作]` `[factor_trigger: dream_white_robe_call]` `[role: 主干]` 白衣召作，便死亡。 → 《周公解梦·帝王文武呼召》
  - `[ns_zgjm_161]` `[trigger: 梦见拜尊长者]` `[factor_trigger: dream_bow_elder]` `[role: 主干]` 拜尊长者，有吉庆。 → 《周公解梦·帝王文武呼召》
  - `[ns_zgjm_162]` `[trigger: 梦见先祖考言]` `[factor_trigger: dream_ancestor_speak]` `[role: 主干]` 先祖考言，求食吉。 → 《周公解梦·帝王文武呼召》
  - `[ns_zgjm_163]` `[trigger: 梦见人云大好者]` `[factor_trigger: dream_praise_bad]` `[role: 主干]` 人云大好者，即凶。 → 《周公解梦·帝王文武呼召》
  - `[ns_zgjm_164]` `[trigger: 梦见人云死者]` `[factor_trigger: dream_death_good]` `[role: 主干]` 人云死者，得长命。 → 《周公解梦·帝王文武呼召》
  - `[ns_zgjm_165]` `[trigger: 梦见人在外呼之]` `[factor_trigger: dream_outside_call]` `[role: 主干]` 人在外呼之，招凶。 → 《周公解梦·帝王文武呼召》
  - `[ns_zgjm_166]` `[trigger: 梦见我欲共汝去]` `[factor_trigger: dream_go_together]` `[role: 主干]` 我欲共汝去，大凶。 → 《周公解梦·帝王文武呼召》
  - `[ns_zgjm_167]` `[trigger: 梦见人云不用汝]` `[factor_trigger: dream_not_needed]` `[role: 主干]` 人云不用汝，大吉。 → 《周公解梦·帝王文武呼召》
  - `[ns_zgjm_168]` `[trigger: 梦见与恶人言]` `[factor_trigger: dream_villain_talk]` `[role: 主干]` 与恶人言，主口舌。 → 《周公解梦·帝王文武呼召》
  - `[ns_zgjm_169]` `[trigger: 梦见被杀害吉]` `[factor_trigger: dream_killed_good]` `[role: 主干]` 被杀害吉，伏藏凶。 → 《周公解梦·帝王文武呼召》
  - `[ns_zgjm_170]` `[trigger: 梦见身生羽翼飞]` `[factor_trigger: dream_grow_wings]` `[role: 主干]` 身生羽翼飞，大吉。 → 《周公解梦·帝王文武呼召》
  - `[ns_zgjm_171]` `[trigger: 梦见身逃去]` `[factor_trigger: dream_escape]` `[role: 主干]` 身逃去，得脱病去。 → 《周公解梦·帝王文武呼召》
  - `[ns_zgjm_172]` `[trigger: 梦见与人交易]` `[factor_trigger: dream_trade]` `[role: 主干]` 与人交易，主有疾。 → 《周公解梦·帝王文武呼召》
  - `[ns_zgjm_173]` `[trigger: 梦见贫穷兵居]` `[factor_trigger: dream_poor_soldier]` `[role: 主干]` 贫穷兵居，主大吉。 → 《周公解梦·帝王文武呼召》
  - `[ns_zgjm_174]` `[trigger: 梦见合伴同行]` `[factor_trigger: dream_travel_together]` `[role: 主干]` 合伴同行，凶事至。 → 《周公解梦·帝王文武呼召》
  - `[ns_zgjm_175]` `[trigger: 梦见一切贵人]` `[factor_trigger: dream_all_nobles]` `[role: 主干]` 一切贵人，皆吉祥。 → 《周公解梦·帝王文武呼召》"""
    normalized_text_zh: str = """"""
    subject: str = "帝王文武呼召"
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
        l1_anchor="zgjm_v1.0.0_帝王文武呼召_001_L1",
    )
    version: str = "1.0.0"
