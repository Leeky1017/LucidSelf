"""
Auto-generated semantic module for zhougong
Generated at: 2025-12-05T13:30:19.864270
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
    semantic_id="zgjm_v1.0.0_身体面目齿发_001",
    book_id="zhougong",
    engine_id="dream"
)
class 身体面目齿发(SemanticEntry):
    """
    - **原文（source_text）**：

  【类名】

  身体面目齿发。

  【条文】

  自身白衣，人所谋。
  梳头洗面，百忧去。
  身拜尊长，大吉昌。

  身上汗出，主凶恶。
...
    """
    
    original_text: str = """- **原文（source_text）**：

  【类名】

  身体面目齿发。

  【条文】

  自身白衣，人所谋。
  梳头洗面，百忧去。
  身拜尊长，大吉昌。

  身上汗出，主凶恶。
  身病虫生，得军职。
  身上虫行，病患安。

  绳索系身，长命吉。
  枷锁临身，病欲来。
  身成肥瘦，皆为凶。

  面对官者，主大吉。
  露体无衣，大吉利。
  妇人披头，有私情。

  头白，主长命大吉。
  头生两角，有争竞。
  头秃发落，皆凶事。

  面生疮黑，主子凶。
  头须白落，忧子孙。
  头须再生，主长命。

  沐浴迁官，疾病除。
  洗手洗足，旧病除。
  照镜明，吉；暗者，凶。

  破镜照人，主分散。
  手足脓血出，大吉。
  屎尿污人，大吉亨。

  露头披发，主人谋。
  披发盖面，官讼至。
  剃头剪发，家内凶。

  眉与发齐，禄位至。
  齿自落者，父母凶。
  齿落更生，子孙兴。

- 分字分词释义：

  - **身体面目齿发**：本类总纲，涵盖身体姿态、皮肤、面容、头发与牙齿等一切“人之形貌”。
  - **自身白衣，人所谋**：身着素白衣物，多与丧服、清贫相关，古人以为易遭他人谋算或利用，需要自保。
  - **梳头洗面，百忧去；身拜尊长，大吉昌**：梳洗整理，象征理顺思绪；拜见尊长，主得长辈庇佑与提携。
  - **身上汗出，主凶恶**：汗出不止，多联想到病重、惊惧或劳损过度。
  - **身病虫生，得军职；身上虫行，病患安**：梦中见身体上生虫、虫行，原书反作吉解：前者主得军职、掌兵事，后者主病邪渐离、病患安宁。
  - **绳索系身，长命吉；枷锁临身，病欲来**：绳索系身偏向“有所拘束而仍在阳世”，主长命；枷锁则近刑具，暗示疾病或官司将临。
  - **身成肥瘦，皆为凶**：极端肥胖或极端消瘦，象征体质失衡与运势偏颇。
  - **面对官者，主大吉**：敢于正面对官，主心正事直，有望得官府、上级认可。
  - **露体无衣，大吉利**：裸露无衣，在本书多解作“无所隐瞒”，主得意外之利，而非单纯羞耻。
  - **妇人披头，有私情；露头披发，主人谋；披发盖面，官讼至**：头发散乱、遮面分别暗示情感秘密、人事谋划与官司牵连。
  - **头白、头须白落／再生**：白头多与长寿相连；头须白落忧子孙，再生则主恢复元气与寿命延长。
  - **头生两角，有争竞**：梦中头生角，象征对抗、冲突与竞争。
  - **面生疮黑，主子凶**：面部生疮、发黑，古人多联想到子女受累或为子女操心。
  - **沐浴迁官、洗手洗足**：清洗身体与手足，主旧病去除、身心更新，并为职位变动铺路。
  - **照镜明，吉；暗者，凶**：镜明则自知、关系清晰为吉；镜暗或破镜则象征视野受阻、关系破裂。
  - **破镜照人，主分散**：镜破则主关系破裂、人心分散。
  - **手足脓血出，大吉；屎尿污人，大吉亨**：脓血与秽污在此皆作“邪气、毒素排出”解，主旧患排尽、财福可通。
  - **剃头剪发，家内凶；眉与发齐，禄位至**：剃发剪发象征削减、损耗，多主家内不安；眉发齐整则为仪容庄重，利于仕途与禄位。
  - **齿自落者，父母凶；齿落更生，子孙兴**：牙齿自落多牵连父母安危；若落后复生，则为“老去新来”，子孙与后继者兴起之象。

- **规范化释义（primary_lang_explained）**：

  本类围绕“身体和面貌”，通过衣着、体态、毛发、牙齿等细节，来占断一个人**健康状态、家庭关系与社会角色**的起落。

  整体来看：

  - **整饬、清洁、礼敬，多主吉**：梳头洗面、沐浴、洗手洗足、拜见尊长、眉发齐整，往往象征身心整顿、去旧迎新，配合得当便有官运、健康与人际之利。
  - **极端、失衡与破裂，多主凶**：身体忽然极肥极瘦、面生疮黑、头秃发落、破镜照人，皆指健康或关系层面已有严重失衡，需要尽早调整。
  - **毛发与牙齿，重在“老幼交替”之象**：头白与头须再生多偏向长寿与恢复；牙落则偏向父母衰损，而再生则主子孙兴起，提示代际更替。
  - **污秽与虫行，在本书中多被视为“排出旧病”或“破旧立新”**：屎尿污人、手足脓血出、虫行身上，皆以“邪出正安”视之，而非简单不洁。

- 核心要点：

  - **看“整理与污秽”的方向**：
    - 能主动梳洗、沐浴、洗手洗足，多主自我整顿、健康好转；
    - 看似污秽（屎尿、脓血）若以“排出”为主，则反而偏吉。
  - **看“头发、眉发与露体”的状态**：
    - 头白而整、眉与发齐，多主长寿与禄位；
    - 披发、遮面、露头披发，则多与阴谋、官讼、情感秘密相关。
  - **看“牙齿与面相”的变化”**：
    - 面生疮黑要警惕子女与家庭负担；
    - 齿自落要注意父母健康；
    - 齿落复生则是子孙与新生力量上升的象征。
  - **看“束缚与军职”的象征**：
    - 绳索系身尚属人间之系，多主长命与受约束的安稳；
    - 枷锁则接近刑具，多与病与讼相关；
    - 身病虫生而得军职，提示某些“带险而有功”的岗位，要重视身心代价。

- 详细解说：

  **（一）衣着、梳洗与礼敬：修整自我与承接庇护**

  - “自身白衣，人所谋”提示：身穿素白，并非单纯清雅，而是容易被视为软弱或与丧事相连，因此需提防他人谋算与利用。
  - “梳头洗面，百忧去；身拜尊长，大吉昌”则强调另一种姿态：愿意整理自己、面对镜中之人，并且向上行礼、寻求指导，多半有利于舒解忧愁、获得长辈或上级的支持。

  **（二）身体状态与虫行：病与职的两面性**

  - “身上汗出，主凶恶”多与高热、惊惧或重劳相关，现实中应特别注意身体负荷与情绪压力。
  - “身病虫生，得军职；身上虫行，病患安”在现代读来颇怪，然古人以虫行身体为“邪去正存”的象征：
    - 对求仕、习武者，多主进入军旅或高压岗位，需要以纪律和风险承担换取前程；
    - 对病者，则主病根有机会排出，但过程未必舒适。

  **（三）束缚、刑具与极端体态：限制与失衡**

  - “绳索系身，长命吉”中，绳索虽束身，却仍在阳间，是“有所约束而得以延命”的象；适合理解为自律、规矩、生活节奏的束缚反而带来安全。
  - “枷锁临身，病欲来”则跨向“刑具领域”，预示健康、名誉或自由有被限制的风险。
  - “身成肥瘦，皆为凶”提醒：无论过度肥胖还是过度消瘦，都是身体平衡失控的象征，应警惕饮食、作息与长期压力对身体的消耗。

  **（四）头发、披发与官讼、情事**

  - “妇人披头，有私情；露头披发，主人谋；披发盖面，官讼至”将发象与人际、官非联系：
    - 披头散发多指情绪波动与礼法失序，妇人梦之，易与情感秘密、外缘牵连；
    - 露头披发而不整，多主周围有人谋算自己，或自己筹谋未光明；
    - 披发盖面则更进一步，暗示事情进入“难以直面”的官司或纠纷阶段。

  **（五）头白、面黑与须发再生：寿夭与子孙**

  - “头白，主长命大吉”“头须再生，主长命”延续传统“白首为寿”的观念，强调时间积累与经验反成福源。
  - “面生疮黑，主子凶；头须白落，忧子孙”则指出：面色与胡须若在梦中呈现衰败之象，多与对子女、后辈的担心与牵累相关。

  **（六）沐浴、洗手洗足与镜象：自我更新与自我认知**

  - “沐浴迁官，疾病除；洗手洗足，旧病除”皆属“洗旧迎新”，宜配合现实中的生活方式调整与求医问药，勿以梦代替实际行动。
  - “照镜明，吉；暗者，凶”强调“看清自己与局势”的重要性：
    - 镜明则自知与他人印象一致，利于决策；
    - 镜暗则可能象征自我认知模糊、环境信息不全。
  - “破镜照人，主分散”则指关系中的裂痕已经显现，需考虑是否重建、修补，或坦然承认各走各路。

  **（七）污秽与血脓：邪出正安的古象**

  - “手足脓血出，大吉；屎尿污人，大吉亨”在现代感受上较为冲突，本书却多以“秽尽则清”理解：
    - 手足脓血排出，象征积郁深久的病邪或情绪得以释放；
    - 屎尿污人，则是“财气、食禄之象”在古解梦中的一贯用法，暗指物质层面的充盈。
  - 解读时需结合现实：若身体确有疾病迹象，应以就医为先，梦象仅供心理与象意参考。

  **（八）牙齿脱落与再生：代际与支柱的变换**

  - “齿自落者，父母凶；齿落更生，子孙兴”：
    - 前者多被视作父母或家中长辈的健康、寿算告急之象，宜多加关怀与陪伴；
    - 后者则象征旧一代渐退、新一代上场，子孙与后继者日渐兴盛。
  - 在现实层面，也可理解为“旧支撑结构松动，新支点正在生长”，提醒梦者为未来做承接与传承上的准备。

  
  
  
- **完整对等诠释（secondary_lang_full）**：

  This category gathers dreams about one's own body, face, hair, and teeth. It treats changes in appearance and bodily sensations as a map of health, emotional burden, generational shifts, and how a person sees themselves in the eyes of others.

  Acts of washing and grooming—combing the hair, washing the face, bathing, washing hands and feet—symbolize consciously putting one's life in order. In dreams they point to worries being relieved, old ailments easing, and the possibility of promotion when combined with respectful gestures toward elders or superiors. By contrast, extremes in body shape, profuse sweating, dark lesions on the face, or sudden baldness indicate imbalance, over‑strain, and hidden problems that need attention.

  Hair and teeth are read through the lens of time and lineage. White hair and the regrowth of beard or hair suggest longevity and the return of vitality, while hair falling out, sparse brows, or messy hair covering the face warn of depleted energy, anxiety about children, or disputes and lawsuits. Teeth falling out by themselves point to danger or decline for parents and older relatives; if new teeth grow back, the emphasis shifts to the rise of children and grandchildren, and to new pillars of support emerging as the old ones give way.

  Images of filth and insects follow the classic "impurity expelled, balance restored" logic of traditional dream interpretation. Pus and blood flowing from the hands and feet, or being splashed with excrement and urine, do not literally encourage unclean behavior; instead they stand for deeply embedded toxins, grievances, and stagnation being forced out so that life can move again, often accompanied by material gain. Worms appearing on or moving across the body can mean either burdensome duties in harsh environments (such as military service) or the gradual departure of illness, depending on the dreamer's real situation. Ropes binding the body hint at strict discipline that prolongs life, whereas heavy restraints such as stocks foreshadow sickness or entanglement in official trouble.

- 校勘与字词辨析：

  - 原文多以三句连写呈现，如“自身白衣人所谋　梳头洗面百忧去　身拜尊长大吉昌”等。本稿在 L1 层将其拆分为三条独立句式，并加逗号、句号，仅为阅读便利，不改动原有词序与用字。
  - “身病虫生得军职　身上虫行病患安”等句，今人或觉不洁，本稿在释义中仍据原书从“邪气外泄”的角度作吉解，不额外引申现代医学含义。
  - “屎尿污人大吉亨”沿袭古梦书一贯解法，本稿仅在白话中简述其“财禄充沛”之象，不鼓励以不卫生之事求吉。
  - “露体无衣大吉利”一条，L1 层忠实记录原意，不以现代伦理评判取代古书象意，后续 L2/L3 层可再加入心理与社会语境的解释。

  - **English**：
    - The original text presents entries in groups of three consecutive phrases, e.g. "自身白衣人所谋　梳头洗面百忧去　身拜尊长大吉昌." This edition splits them into three independent sentences with commas and periods for reading convenience, without altering the original word order or characters.
    - Phrases like "身病虫生得军职" and "身上虫行病患安" may seem unclean to modern readers; this edition interprets them according to the original text's perspective of "evil energy being expelled," offering auspicious readings without extending modern medical meanings.
    - "屎尿污人大吉亨" follows the consistent interpretation of ancient dream books; the vernacular explanation briefly describes its symbolism of "abundant wealth and fortune," without encouraging unsanitary practices for seeking good luck.
    - The entry "露体无衣大吉利" is faithfully recorded at the L1 layer without replacing the ancient symbolic meaning with modern ethical judgments; psychological and social context interpretations can be added in subsequent L2/L3 layers.



- **叙事素材（narrative_snippets）**：

  - `[ns_zgjm_028]` `[trigger: 梦见自身白衣]` `[factor_trigger: dream_white_clothes]` `[role: 主干]` 自身白衣，人所谋。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_029]` `[trigger: 梦见梳头洗面]` `[factor_trigger: dream_comb_wash]` `[role: 主干]` 梳头洗面，百忧去。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_030]` `[trigger: 梦见拜尊长]` `[factor_trigger: dream_bow_elder]` `[role: 主干]` 身拜尊长，大吉昌。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_031]` `[trigger: 梦见身上汗出]` `[factor_trigger: dream_sweat]` `[role: 主干]` 身上汗出，主凶恶。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_032]` `[trigger: 梦见身病虫生]` `[factor_trigger: dream_worm_body_sick]` `[role: 主干]` 身病虫生，得军职。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_033]` `[trigger: 梦见身上虫行]` `[factor_trigger: dream_worm_crawl]` `[role: 主干]` 身上虫行，病患安。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_034]` `[trigger: 梦见绳索系身]` `[factor_trigger: dream_rope_bind]` `[role: 主干]` 绳索系身，长命吉。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_035]` `[trigger: 梦见枷锁临身]` `[factor_trigger: dream_shackle]` `[role: 主干]` 枷锁临身，病欲来。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_036]` `[trigger: 梦见身成肥瘦]` `[factor_trigger: dream_body_extreme]` `[role: 主干]` 身成肥瘦，皆为凶。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_037]` `[trigger: 梦见面对官者]` `[factor_trigger: dream_face_official]` `[role: 主干]` 面对官者，主大吉。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_038]` `[trigger: 梦见露体无衣]` `[factor_trigger: dream_naked]` `[role: 主干]` 露体无衣，大吉利。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_039]` `[trigger: 梦见妇人披头]` `[factor_trigger: dream_woman_disheveled]` `[role: 主干]` 妇人披头，有私情。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_040]` `[trigger: 梦见头白]` `[factor_trigger: dream_white_hair]` `[role: 主干]` 头白，主长命大吉。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_041]` `[trigger: 梦见头生两角]` `[factor_trigger: dream_horns_head]` `[role: 主干]` 头生两角，有争竞。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_042]` `[trigger: 梦见头秃发落]` `[factor_trigger: dream_bald]` `[role: 主干]` 头秃发落，皆凶事。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_043]` `[trigger: 梦见面生疮黑]` `[factor_trigger: dream_face_sore]` `[role: 主干]` 面生疮黑，主子凶。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_044]` `[trigger: 梦见头须白落]` `[factor_trigger: dream_beard_fall]` `[role: 主干]` 头须白落，忧子孙。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_045]` `[trigger: 梦见头须再生]` `[factor_trigger: dream_beard_regrow]` `[role: 主干]` 头须再生，主长命。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_046]` `[trigger: 梦见沐浴迁官]` `[factor_trigger: dream_bath_promote]` `[role: 主干]` 沐浴迁官，疾病除。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_047]` `[trigger: 梦见洗手洗足]` `[factor_trigger: dream_wash_limbs]` `[role: 主干]` 洗手洗足，旧病除。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_048]` `[trigger: 梦见照镜明]` `[factor_trigger: dream_mirror_bright]` `[role: 主干]` 照镜明，吉；暗者，凶。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_049]` `[trigger: 梦见破镜照人]` `[factor_trigger: dream_mirror_broken]` `[role: 主干]` 破镜照人，主分散。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_050]` `[trigger: 梦见手足脓血出]` `[factor_trigger: dream_limbs_pus]` `[role: 主干]` 手足脓血出，大吉。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_051]` `[trigger: 梦见屎尿污人]` `[factor_trigger: dream_filth_on_body]` `[role: 主干]` 屎尿污人，大吉亨。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_052]` `[trigger: 梦见露头披发]` `[factor_trigger: dream_hair_loose]` `[role: 主干]` 露头披发，主人谋。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_053]` `[trigger: 梦见披发盖面]` `[factor_trigger: dream_hair_cover_face]` `[role: 主干]` 披发盖面，官讼至。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_054]` `[trigger: 梦见剃头剪发]` `[factor_trigger: dream_haircut]` `[role: 主干]` 剃头剪发，家内凶。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_055]` `[trigger: 梦见眉与发齐]` `[factor_trigger: dream_brow_hair_neat]` `[role: 主干]` 眉与发齐，禄位至。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_056]` `[trigger: 梦见齿自落]` `[factor_trigger: dream_teeth_fall]` `[role: 主干]` 齿自落者，父母凶。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_057]` `[trigger: 梦见齿落更生]` `[factor_trigger: dream_teeth_regrow]` `[role: 主干]` 齿落更生，子孙兴。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_422]` `[trigger: 梦见死]` `[factor_trigger: dream_death]` `[role: 主干]` 梦见死，主凶兆。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_423]` `[trigger: 梦见死后复生]` `[factor_trigger: dream_death_reversal]` `[role: 主干]` 梦见死后复生，主吉。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_424]` `[trigger: 梦见脏衣服]` `[factor_trigger: dream_dirty_clothes]` `[role: 主干]` 梦见脏衣服，主受辱。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_425]` `[trigger: 梦见刺青]` `[factor_trigger: dream_dirty_face]` `[role: 主干]` 梦见刺青，主有事。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_426]` `[trigger: 梦见狗咬]` `[factor_trigger: dream_dog_bite]` `[role: 主干]` 梦见狗咬，主被欺。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_427]` `[trigger: 梦见狗死]` `[factor_trigger: dream_dog_death]` `[role: 主干]` 梦见狗死，主失友。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_428]` `[trigger: 梦见狗吠]` `[factor_trigger: dream_dog_howl]` `[role: 主干]` 梦见狗吠，主有贼。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_429]` `[trigger: 梦见狗走]` `[factor_trigger: dream_dog_walk]` `[role: 主干]` 梦见狗走，主凶事。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_430]` `[trigger: 梦见白狗]` `[factor_trigger: dream_dog_white]` `[role: 主干]` 梦见白狗，主远行。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_431]` `[trigger: 梦见饮食]` `[factor_trigger: dream_drink_eat]` `[role: 主干]` 梦见饮食，主吉祥。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_432]` `[trigger: 梦见醉酒]` `[factor_trigger: dream_drunk]` `[role: 主干]` 梦见醉酒，主有忧。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_433]` `[trigger: 梦见发人]` `[factor_trigger: dream_fa_ren]` `[role: 主干]` 梦见发人，主发迹。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_434]` `[trigger: 梦见发财]` `[factor_trigger: dream_facai]` `[role: 主干]` 梦见发财，主富贵。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_435]` `[trigger: 梦见跌倒]` `[factor_trigger: dream_fall]` `[role: 主干]` 梦见跌倒，主凶险。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_436]` `[trigger: 梦见父死]` `[factor_trigger: dream_father_death]` `[role: 主干]` 梦见父死，主大凶。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_437]` `[trigger: 梦见父病]` `[factor_trigger: dream_father_sick]` `[role: 主干]` 梦见父病，主有忧。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_438]` `[trigger: 梦见父亡]` `[factor_trigger: dream_father_dead]` `[role: 主干]` 梦见父亡，主大凶。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_439]` `[trigger: 梦见肥人]` `[factor_trigger: dream_fat_person]` `[role: 主干]` 梦见肥人，主富贵。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_440]` `[trigger: 梦见宴席]` `[factor_trigger: dream_feast]` `[role: 主干]` 梦见宴席，主喜庆。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_441]` `[trigger: 梦见打仗]` `[factor_trigger: dream_fight]` `[role: 主干]` 梦见打仗，主争斗。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_442]` `[trigger: 梦见火]` `[factor_trigger: dream_fire]` `[role: 主干]` 梦见火，主发财。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_443]` `[trigger: 梦见火起]` `[factor_trigger: dream_fire_start]` `[role: 主干]` 梦见火起，主大吉。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_444]` `[trigger: 梦见鱼]` `[factor_trigger: dream_fish]` `[role: 主干]` 梦见鱼，主得财。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_445]` `[trigger: 梦见鱼跃]` `[factor_trigger: dream_fish_jump]` `[role: 主干]` 梦见鱼跃，主大吉。 → 《周公解梦·身体面目齿发》
  - `[ns_zgjm_446]` `[trigger: 梦见吃鱼]` `[factor_trigger: dream_fish_eat]` `[role: 主干]` 梦见吃鱼，主有财。 → 《周公解梦·身体面目齿发》"""
    normalized_text_zh: str = """"""
    subject: str = "身体面目齿发"
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
        l1_anchor="zgjm_v1.0.0_身体面目齿发_001_L1",
    )
    version: str = "1.0.0"
