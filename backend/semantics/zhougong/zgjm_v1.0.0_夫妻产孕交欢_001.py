"""
Auto-generated semantic module for zhougong
Generated at: 2025-12-05T13:30:19.877655
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
    semantic_id="zgjm_v1.0.0_夫妻产孕交欢_001",
    book_id="zhougong",
    engine_id="dream"
)
class 夫妻产孕交欢(SemanticEntry):
    """
    - **原文（source_text）**：

  【类名】

  夫妻产孕交欢。

  【条文】

  夫妻宴会，主相别。
  夫妻相骂，主病患。
  夫妻分钗，主离别。

  夫妻相打，欲和会。
...
    """
    
    original_text: str = """- **原文（source_text）**：

  【类名】

  夫妻产孕交欢。

  【条文】

  夫妻宴会，主相别。
  夫妻相骂，主病患。
  夫妻分钗，主离别。

  夫妻相打，欲和会。
  同妇人行，主失财。
  抱妇人，主有喜事。

  与妇人交，有邪祟。
  与妇人共坐，大吉。
  抱夫，主大得财喜。

  妇人与夫入水，吉。
  夫妻各与梳头，吉。
  夫妻相拜，主分散。

  交接男子，主失财。
  妻著锦衣，生贵子。
  妻有孕，主外私情。

  见妇人阴，主口舌。
  妇人赤身，主大吉。
  男子裸体，命通达。

  兄弟分别，口舌临。
  抱小儿女，主口舌。
  小儿死者，主口舌。

  新生男女，主大吉。
  见嫁娶及孝，主凶。
  男子化为尼姑，凶。

- 分字分词释义：

  - **夫妻产孕交欢**：本类总纲，涉及夫妻宴会、争吵、交欢、怀孕与亲属互动等，多指**婚姻关系的亲疏、情欲往来的正偏以及子嗣与家庭结构的起伏**。
  - **夫妻宴会主相别；夫妻相骂主病患；夫妻分钗主离别**：宴会往往在阶段节点出现，梦中夫妻设宴，反多主阶段性结束或暂别；相骂则伤气伤情，主病患；分钗象征拆分配偶饰物，主离别。
  - **夫妻相打欲和会**：相打并非终局，而是激烈冲突后的和会契机，古人以之为“欲和会”，提示矛盾爆发后反而有机会重建共识。
  - **同妇人行主失财；抱妇人主有喜事；与妇人交有邪祟；与妇人共坐大吉；抱夫主大得财喜**：与妇人的各种接触（同行、拥抱、交欢、共坐），在古人解梦框架中，将“正当情感交流”与“邪祟外缘”区分开来，分别对应喜事与失财、邪祟。
  - **妇人与夫入水吉；夫妻各与梳头吉；夫妻相拜主分散**：夫妇同入水象征共渡境遇；互为梳头象征体贴与整理；相拜则偏向礼成而散，故主分散。
  - **交接男子主失财；妻著锦衣生贵子；妻有孕主外私情**：与男子交接耗损自身资源，故主失财；妻着锦衣多主所生子贵；妻有孕则有外缘牵连之象，古人解为“外私情”，今可视作感情结构复杂。
  - **见妇人阴主口舌；妇人赤身主大吉；男子裸体命通达**：妇人阴与赤身皆涉及赤裸与真实，但前者易引起口舌与议论，后者则象征无所隐瞒与坦然，故主大吉；男子裸体则为命途通达之象。
  - **兄弟分别口舌临；抱小儿女主口舌；小儿死者主口舌**：兄弟分别、抱小儿女与小儿死亡，皆牵涉亲情与牵挂，故多主口舌纷争与心中挂碍。
  - **新生男女主大吉；见嫁娶及孝主凶；男子化为尼姑凶**：新生儿象征新的希望与延续，为大吉；梦中同时见嫁娶与孝服则喜丧交杂，主凶；男子化为尼姑则象征角色与性情极端转变的象征，多为不吉。

- **规范化释义（primary_lang_explained）**：

  本类通过夫妻宴会、争吵、交欢、怀孕与亲族互动等情景，描绘的是**婚姻关系的亲疏、情欲往来的正偏以及子嗣与家庭结构的起伏**：

  - 表面喜庆的宴会、嫁娶等，在梦中反而被视作“阶段终结”或“喜中藏忧”的象征，因此常主相别或凶。
  - 激烈的争吵与相打，并不必然指向破裂，有时反而预示矛盾摊开后更易和解，只是过程辛苦。
  - 与妇人的各种接触（同行、拥抱、交欢、共坐），在古人解梦框架中，将“正当情感交流”与“邪祟外缘”区分开来，分别对应喜事与失财、邪祟。
  - 对赤身与裸体的态度颇具时代色彩：妇人赤身与男子裸体反而主大吉与命通达，强调的是“坦露真相、无所遮掩”。
  - 兄弟、小儿与新生儿的出没，则集中指向亲情与对子嗣的挂念：新生则吉，死与分别则多主口舌与烦忧。

- 核心要点：

  - **看夫妻互动的形态**：宴会、分钗与相拜，多主分离或阶段性终结；相打与相骂则在病患与和会之间摇摆，需要结合现实判断。
  - **看与异性的接触方式**：同妇人行、与男子交接等，多主失财与是非；抱妇人、与妇人共坐与抱夫，多偏向喜事与财喜。
  - **看生育与子嗣征兆**：妻著锦衣、生贵子；妻有孕则有外缘牵连之虑；新生儿为大吉，小儿死亡则多主口舌与忧虑。
  - **看赤身与角色变形**：妇人赤身与男子裸体偏吉，男子化尼姑则凶，提示在“坦露”与“角色错位”之间有明显区分。

- 详细解说：

  **（一）夫妻宴会、争吵与分钗：关系的张弛**

  - “夫妻宴会主相别；夫妻相骂主病患；夫妻分钗主离别”：
    - 宴会常发生在阶段性节点，梦中夫妻宴会，被解作阶段结束或暂别；
    - 相骂则伤和气与身体，故主病患；
    - 分钗象征拆分婚姻象征物，多与实质性分手或长期冷淡有关。
  - “夫妻相打欲和会”：
    - 相打虽凶，却被解为“欲和会”，提醒冲突暴露反有利于之后的修复。

  **（二）与妇人接触：正缘与外缘**

  - “同妇人行主失财；抱妇人主有喜事；与妇人交有邪祟；与妇人共坐大吉；抱夫主大得财喜”展示了多种接触方式：
    - 同行与交接偏向牵连与耗损，分别主失财与邪祟；
    - 抱妇人与与妇人共坐偏向亲近与和合，多主喜事与安宁；
    - 抱夫则象征对配偶的依托与支持，主大得财喜。

  **（三）入水、梳头与相拜：共同渡险与礼成散席**

  - “妇人与夫入水吉；夫妻各与梳头吉；夫妻相拜主分散”：
    - 同入水喻共同经历情感或生活的起伏，属共渡之象；
    - 为对方梳头则象征照顾、整理与亲密；
    - 相拜则偏向礼数圆满之后的散席，故主分散。

  **（四）孕育与赤裸：子嗣与真相**

  - “交接男子主失财；妻著锦衣生贵子；妻有孕主外私情”：
    - 交接男子多被解作自身资源与体力的消耗，故主失财；
    - 妻着锦衣则对应尊贵之象，故主生贵子；
    - 妻有孕却被解作外私情，则是古人道德观下的警示。
  - “见妇人阴主口舌；妇人赤身主大吉；男子裸体命通达”：
    - 妇人阴象征隐私之处暴露，易惹口舌；
    - 全身赤裸则象征坦荡，梦中反为吉；
    - 男子裸体则更强调“命通达”，表达事业或人生道路敞开之象。

  **（五）兄弟与小儿：亲情与挂碍**

  - “兄弟分别口舌临；抱小儿女主口舌；小儿死者主口舌；新生男女主大吉；见嫁娶及孝主凶；男子化为尼姑凶”：
    - 兄弟分别与抱小儿、多指家庭内的牵挂和沟通不顺，故多主口舌；
    - 小儿死亡虽凶，却主要落在“口舌是非与忧虑加重”上；
    - 新生儿则象征新的希望与延续，为大吉；
    - 同梦之中见嫁娶与孝服，喜丧交集，主凶；
    - 男子化为尼姑，则是角色与性情极端转变的象征，多为不吉。



 - **完整对等诠释（secondary_lang_full）**：

  This category interprets dreams about spouses, pregnancy, sexual union, and close family bonds. Banquets, quarrels, parting hairpins, and bowing ceremonies describe how a marriage stretches and tightens over time—celebrations can secretly mark an ending, arguments may clear the air for later reconciliation, and ritual gestures can either seal unity or signal separation. Embracing one’s spouse, entering water together, or carefully combing each other’s hair emphasizes mutual support and shared experience, while ritual bows that precede separation, harsh quarrels, or seeing brothers part ways point to distance, strain, and unresolved tensions.

  Scenes of pregnancy, childbirth, and infants show how the dreamer relates to fertility, creativity, and future generations. A richly dressed wife or the birth of healthy children promises honor and continuation of the family line; newborn boys and girls are read as great blessings. By contrast, children dying, infants in danger, or pregnancy linked to suspicion of infidelity reveal anxieties about lineage, loyalty, and the stability of intimate bonds. Nakedness also reverses surface expectations: a woman or man standing unclothed can symbolize honesty, openness, and a life path unobstructed, whereas exposed genitals or bodies viewed with shame invite gossip, judgment, and social friction. Taken together, the dreams in this category show how intimacy, desire, and kinship are constantly being tested—sometimes fractured, sometimes renewed—within the fabric of everyday relationships.


- 校勘与字词辨析：

  - “夫妻宴会主相别”一类条文，沿袭古书“喜中有警”的解梦风格，本稿在 L1 层保留原判，不对现代婚姻观作价值评判。
  - “与妇人交有邪祟”之“邪祟”，本指不正之气或鬼神干扰，L1 层不改字，在释义中以“外缘不正、心神不安”略作解释。
  - “妻有孕主外私情”一句具有明显时代偏见，本稿不改原文，在白话与详细解说中以“感情结构复杂、外缘牵连”释义，为后续高阶语义层留出调整空间。
  - “男子化为尼姑凶”句中性别与身份错位亦具强烈时代烙印，L1 层按字面保留，在解释中以“角色错位、行止乖张”来呈现其不吉含义。

  - **English**：
    - Entries like "夫妻宴会主相别" follow the ancient dream interpretation style of "warning within celebration." The L1 layer preserves the original verdict without making value judgments on modern marriage views.
    - In "与妇人交有邪祟," the term "邪祟" originally refers to improper qi or ghostly interference. The L1 layer does not alter the characters, briefly explaining it as "improper external connections, unsettled mind" in the interpretation.
    - The phrase "妻有孕主外私情" carries obvious period bias. This edition does not alter the original text, interpreting it in vernacular and detailed commentary as "complex emotional structures, external entanglements," leaving room for adjustment in higher semantic layers.
    - In "男子化为尼姑凶," the gender and identity confusion also bears strong period characteristics. The L1 layer preserves it literally, presenting its inauspicious meaning in the explanation as "role confusion, improper conduct."


- **叙事素材（narrative_snippets）**：

  - `[ns_zgjm_528]` `[trigger: 梦见夫妻宴会]` `[factor_trigger: dream_couple_banquet]` `[role: 主干]` 夫妻宴会，主相别。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_529]` `[trigger: 梦见夫妻相骂]` `[factor_trigger: dream_couple_scold]` `[role: 主干]` 夫妻相骂，主病患。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_530]` `[trigger: 梦见夫妻分钗]` `[factor_trigger: dream_couple_split]` `[role: 主干]` 夫妻分钗，主离别。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_531]` `[trigger: 梦见夫妻相打]` `[factor_trigger: dream_couple_fight]` `[role: 主干]` 夫妻相打，欲和会。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_532]` `[trigger: 梦见同妇人行]` `[factor_trigger: dream_walk_woman]` `[role: 主干]` 同妇人行，主失财。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_533]` `[trigger: 梦见抱妇人]` `[factor_trigger: dream_embrace_woman]` `[role: 主干]` 抱妇人，主有喜事。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_534]` `[trigger: 梦见与妇人交]` `[factor_trigger: dream_intercourse_woman]` `[role: 主干]` 与妇人交，有邪祟。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_535]` `[trigger: 梦见与妇人共坐]` `[factor_trigger: dream_sit_woman]` `[role: 主干]` 与妇人共坐，大吉。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_536]` `[trigger: 梦见抱夫]` `[factor_trigger: dream_embrace_husband]` `[role: 主干]` 抱夫，主大得财喜。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_537]` `[trigger: 梦见妇人与夫入水]` `[factor_trigger: dream_couple_water]` `[role: 主干]` 妇人与夫入水，吉。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_538]` `[trigger: 梦见夫妻各与梳头]` `[factor_trigger: dream_couple_comb]` `[role: 主干]` 夫妻各与梳头，吉。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_539]` `[trigger: 梦见夫妻相拜]` `[factor_trigger: dream_couple_bow]` `[role: 主干]` 夫妻相拜，主分散。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_540]` `[trigger: 梦见交接男子]` `[factor_trigger: dream_intercourse_man]` `[role: 主干]` 交接男子，主失财。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_541]` `[trigger: 梦见妻著锦衣]` `[factor_trigger: dream_wife_brocade]` `[role: 主干]` 妻著锦衣，生贵子。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_542]` `[trigger: 梦见妻有孕]` `[factor_trigger: dream_wife_pregnant]` `[role: 主干]` 妻有孕，主外私情。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_543]` `[trigger: 梦见见妇人阴]` `[factor_trigger: dream_see_woman_private]` `[role: 主干]` 见妇人阴，主口舌。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_544]` `[trigger: 梦见妇人赤身]` `[factor_trigger: dream_woman_naked]` `[role: 主干]` 妇人赤身，主大吉。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_545]` `[trigger: 梦见男子裸体]` `[factor_trigger: dream_man_naked]` `[role: 主干]` 男子裸体，命通达。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_546]` `[trigger: 梦见兄弟分别]` `[factor_trigger: dream_brother_part]` `[role: 主干]` 兄弟分别，口舌临。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_547]` `[trigger: 梦见抱小儿女]` `[factor_trigger: dream_hold_child]` `[role: 主干]` 抱小儿女，主口舌。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_548]` `[trigger: 梦见小儿死者]` `[factor_trigger: dream_child_die]` `[role: 主干]` 小儿死者，主口舌。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_549]` `[trigger: 梦见新生男女]` `[factor_trigger: dream_newborn]` `[role: 主干]` 新生男女，主大吉。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_550]` `[trigger: 梦见见嫁娶及孝]` `[factor_trigger: dream_wedding_funeral]` `[role: 主干]` 见嫁娶及孝，主凶。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_551]` `[trigger: 梦见男子化为尼姑]` `[factor_trigger: dream_man_become_nun]` `[role: 主干]` 男子化为尼姑，凶。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_960]` `[trigger: 梦见疾病]` `[factor_trigger: dream_sickness]` `[role: 主干]` 梦见疾病，主有忧。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_961]` `[trigger: 梦见唱歌]` `[factor_trigger: dream_sing]` `[role: 主干]` 梦见唱歌，主有喜。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_962]` `[trigger: 梦见蛇]` `[factor_trigger: dream_snake]` `[role: 主干]` 梦见蛇，主有财。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_963]` `[trigger: 梦见蛇咬]` `[factor_trigger: dream_snake_bite]` `[role: 主干]` 梦见蛇咬，主有忧。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_964]` `[trigger: 梦见雪]` `[factor_trigger: dream_snow]` `[role: 主干]` 梦见雪，主有财。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_965]` `[trigger: 梦见士兵]` `[factor_trigger: dream_soldier]` `[role: 主干]` 梦见士兵，主有急事。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_966]` `[trigger: 梦见儿子]` `[factor_trigger: dream_son]` `[role: 主干]` 梦见儿子，主有喜。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_967]` `[trigger: 梦见蜘蛛]` `[factor_trigger: dream_spider]` `[role: 主干]` 梦见蜘蛛，主有喜。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_968]` `[trigger: 梦见星星]` `[factor_trigger: dream_star]` `[role: 主干]` 梦见星星，主贵子。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_969]` `[trigger: 梦见偷窃]` `[factor_trigger: dream_steal]` `[role: 主干]` 梦见偷窃，主破财。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_970]` `[trigger: 梦见风暴]` `[factor_trigger: dream_storm_wind]` `[role: 主干]` 梦见风暴，主凶险。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_971]` `[trigger: 梦见陌生人]` `[factor_trigger: dream_stranger]` `[role: 主干]` 梦见陌生人，主有事。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_972]` `[trigger: 梦见太阳]` `[factor_trigger: dream_sun]` `[role: 主干]` 梦见太阳，主大吉。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_973]` `[trigger: 梦见游泳]` `[factor_trigger: dream_swim]` `[role: 主干]` 梦见游泳，主远行。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_974]` `[trigger: 梦见刀剑]` `[factor_trigger: dream_sword]` `[role: 主干]` 梦见刀剑，主有争。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_975]` `[trigger: 梦见谈话]` `[factor_trigger: dream_talk]` `[role: 主干]` 梦见谈话，主有事。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_976]` `[trigger: 梦见寺庙]` `[factor_trigger: dream_temple]` `[role: 主干]` 梦见寺庙，主有福。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_977]` `[trigger: 梦见雷电]` `[factor_trigger: dream_thunder_lightning]` `[role: 主干]` 梦见雷电，主大吉。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_978]` `[trigger: 梦见老虎]` `[factor_trigger: dream_tiger]` `[role: 主干]` 梦见老虎，主有权。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_979]` `[trigger: 梦见坟墓]` `[factor_trigger: dream_tomb]` `[role: 主干]` 梦见坟墓，主有忧。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_980]` `[trigger: 梦见旅行]` `[factor_trigger: dream_travel]` `[role: 主干]` 梦见旅行，主远行。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_981]` `[trigger: 梦见树木]` `[factor_trigger: dream_tree]` `[role: 主干]` 梦见树木，主兴旺。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_982]` `[trigger: 梦见龟]` `[factor_trigger: dream_turtle]` `[role: 主干]` 梦见龟，主长寿。 → 《周公解梦·夫妻产孕交欢》
  - `[ns_zgjm_983]` `[trigger: 梦见伞]` `[factor_trigger: dream_umbrella]` `[role: 主干]` 梦见伞，主有助。 → 《周公解梦·夫妻产孕交欢》"""
    normalized_text_zh: str = """"""
    subject: str = "夫妻产孕交欢"
    factor_refs: list = ['zgjm_14_couple_banquet_proposal', 'zgjm_14_couple_split_pin_proposal', 'zgjm_14_couple_conflict_reconcile_proposal', 'zgjm_14_wife_brocade_proposal', 'zgjm_14_wife_pregnant_anxiety_proposal', 'zgjm_14_woman_naked_proposal', 'zgjm_14_man_naked_proposal']
    
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
        l1_anchor="zgjm_v1.0.0_夫妻产孕交欢_001_L1",
    )
    version: str = "1.0.0"
