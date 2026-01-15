"""
Auto-generated semantic module for zhougong
Generated at: 2025-12-05T13:30:19.877699
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
    semantic_id="zgjm_v1.0.0_饮食酒肉瓜菜_001",
    book_id="zhougong",
    engine_id="dream"
)
class 饮食酒肉瓜菜(SemanticEntry):
    """
    - **原文（source_text）**：
  
   【类名】
  
   饮食酒肉瓜菜。

  【条文】

  人请饮酒，主长命。
  与人饮酒，有口舌。
  与人吃会，富贵至。

  筵会客人...
    """
    
    original_text: str = """- **原文（source_text）**：
  
   【类名】
  
   饮食酒肉瓜菜。

  【条文】

  人请饮酒，主长命。
  与人饮酒，有口舌。
  与人吃会，富贵至。

  筵会客人，家欲破。
  饮酒者，主哭泣事。
  饮酒至醉，主疾病。

  贵人赐宴，主疾病。
  与贵人对饮，大吉。
  人请吃酥酪，主喜。

  与人吃乳，尊亲至。
  与人吃蜜，大吉利。
  呕吐者，病人主瘥。

  食水者，主得大利。
  死人食者，主疾病。
  食牛肉于堂上，吉。

  食犬肉，主有争讼。
  食猪肉，主疾病至。
  刀割猪肉，主生病。

  食生肉，凶；熟肉，吉。
  食自死肉，主别离。
  食鹅肉，主妾疾病。

  食鸡鸭等肉，皆吉。
  食馒头，主口舌散。
  见馒头未食，主气。

  食烂瓜，主生疾病。
  食饼、食饭，心不遂。
  食瓜子，主生贵子。

  食柿、食柑，主疾病。
  食柿桃，离而复合。
  食枣者，主生贵子。

  食桑椹，主生贵子。
  食粟者，主有分离。
  食梨者，主失财帛。

  食一切菜者，凶至。
  食茄者，主妻有子。
  食葱韭，主有争斗。

  食薤者，有重伤至。
  食蒜者，主灾害至。
  食菜见菜黄，主凶。

  食油、盐、酱、酸、豉，吉。

- 分字分词释义：

  - **饮食酒肉瓜菜**：本类总纲，涵盖酒、肉、饼饭、水果与蔬菜等饮食之物，象征**身体状态、情绪宣泄与财福损益**。
  - **人请饮酒主长命；与人饮酒有口舌；与人吃会富贵至**：被人相邀饮酒，多主人情往来中得长久之益；与人对饮过多，则易起口舌；与人同席吃会，则主因人脉宴会而得富贵机会。
  - **筵会客人家欲破；饮酒者主哭泣事；饮酒至醉主疾病**：筵席上的人多，易有花费与是非，故家欲破；饮酒本可助兴，过度则与哭泣与疾病相连.
  - **贵人赐宴主疾病；与贵人对饮大吉；人请吃酥酪主喜**：被贵人赐宴，表面光彩，内里劳神耗气，故主疾病；与贵人平等对饮，则主关系和谐、大吉；酥酪为丰腴之品，多主喜讯与福泽.
  - **与人吃乳尊亲至；与人吃蜜大吉利；呕吐者病人主瘥**：乳与蜜皆为滋养之物，与人共食多主尊亲或贵人到来，以及顺利康复；呕吐则为排出之象，故病者主瘥.
  - **食水者主得大利；死人食者主疾病；食牛肉于堂上吉**：饮水象征本源与清洁，主大利；死人食物或与死人同食，则主疾病；堂上食牛肉，多主庄重之宴与厚实之福.
  - **食犬肉主有争讼；食猪肉主疾病至；刀割猪肉主生病**：犬为守卫，食犬肉多应于争讼与官非；猪肉肥腻，过食则主疾病；刀割猪肉则强调病源之主动寻来.
  - **食生肉凶熟肉吉；食自死肉主别离；食鹅肉主妾疾病**：生肉未熟，象凶险与隐患；熟肉则主事已成熟可用；自死之肉则象征不祥来源，主别离；鹅肉被系于妾媵之象，主妾疾病.
  - **食鸡鸭等肉皆吉；食馒头主口舌散；见馒头未食主气**：鸡鸭为常见家禽，肉食多吉；馒头本为口腹之欲，吃之可散口舌之争，见而未食则多主怨气与不平.
  - **食烂瓜主生疾病；食饼食饭心不遂；食瓜子主生贵子**：烂瓜不宜入口，故主病；饼饭不合心意，则心不遂；瓜子多籽，象征子嗣，故主生贵子.
  - **食柿食柑主疾病；食柿桃离而复合；食枣、桑椹主生贵子**：柿与柑性偏湿冷，多主小病；“柿桃离而复合”以谐音与果性表示分合之变；枣与桑椹常被视为补血生子之物，故多主生贵子.
  - **食粟者主有分离；食梨者主失财帛**：“粟”谐“疏”，多主分离与疏远；“梨”谐“离”，故主失财与离散.
  - **食一切菜者凶至；食茄者主妻有子；食葱韭主有争斗；食薤、蒜者主重伤与灾害；食菜见菜黄主凶；食油盐酱酸豉吉**：蔬菜虽为日常之食，但在梦中大量出现往往与清苦与身体虚弱相关；茄与子多被连用，故主妻有子；葱韭味辛，多主争斗；薤与蒜味更烈，主重伤与灾害；菜黄则象征枯败，主凶；油盐酱酸豉为调味之物，象征生活有滋有味，多主吉.

- **规范化释义（primary_lang_explained）**：

  本类通过酒席、肉食、水果与蔬菜的不同组合，来映照**饮食习惯、身体健康、情绪宣泄与财福损益**的状态：

  - 酒：少量为助兴与人情往来，多主长命与吉；过多则与哭泣、疾病、家业耗损相连，尤其是“饮至大醉".
  - 肉：熟肉、鸡鸭等常见肉类多主吉；生肉、自死肉与过肥之猪肉则易引动疾病、别离与争讼.
  - 乳、蜜、水与酥酪：多主滋养、亲人来临与喜讯，亦与康复与大利相关.
  - 瓜果与主“子”的食物：瓜子、枣、桑椹等多主生子与贵子；柿柑则偏向小病；柿桃则含离合之象.
  - 菜类与辛辣：一切菜若只见菜而无肉，多被视作清苦与虚弱之象，故凶；其中茄与“茄子多籽”相连，葱韭味辛，多主争斗；薤与蒜味更烈，主重伤与灾害；菜黄则象征枯败，主凶；油盐酱酸豉则代表生活滋味，主吉.

- **完整对等诠释（secondary_lang_full）**：

  This category reads food and drink as a mirror of the body’s condition, emotional release, and the flow of fortune and loss. Invitations to drink, shared banquets, rich meats, plain breads, fruits, and vegetables each mark a different way that nourishment and excess show up in the dream. Being invited to drink or share a feast suggests being welcomed into networks of support and long‑lasting benefit; yet crowded banquets, overdrinking, or wine that ends in tears point to waste, illness, and relationships strained by overindulgence. When nobles host the feast, the dream hints at the hidden cost of status—the fatigue and pressure that can translate into sickness even beneath a glittering surface.

  Meat, dairy, and sweets describe how resources are taken in and transformed. Cooked meats and familiar poultry signal usable energy and everyday blessings, while raw flesh, meat from animals that died on their own, or overly fatty pork embody hidden dangers, quarrels, separation, and disease. Milk, cream, honey, and clear water stand for gentle nourishment, affection from elders, and the arrival of good news or recovery; vomiting in a dream, though unpleasant, can mark the expulsion of stored‑up toxins and the easing of a sick person’s condition. Eating food associated with the dead or taking what belongs to the other world, however, warns of contact with illness or the need to respect invisible boundaries.

  Grains, fruits, and vegetables speak to fertility, frustration, and the subtle play between abundance and lack. Seeds, dates, mulberries, and other many‑seeded or blood‑nourishing foods echo the hope for children and especially for distinguished offspring, while puns on staple foods like millet and pears carry hints of separation and financial loss. Soft breads and staple dishes that leave the dreamer unsatisfied show desires that cannot easily be met. Large amounts of plain vegetables, especially yellowing or withered greens, indicate hardship, weakness, or a life stripped of richness; pungent scallions, leeks, and strong bulbs such as garlic and chive point toward quarrels, injury, and looming trouble. Altogether, this category teaches that what is eaten, who offers it, and in what state it appears reveal how a person is nourishing or exhausting themselves—whether they are drawing in support, leaking fortune, or standing at the edge between comfort and deprivation.


  - **看酒：被请与自饮、浅饮与大醉**：受邀饮酒偏吉，自饮或饮至大醉则要防哭泣、疾病与家业耗散.
  - **看肉：熟与生、常见与自死**：熟肉与常见禽肉偏吉；生肉、自死肉与刺杀猪肉则偏凶，涉及病、争讼与别离.
  - **看滋养之物：乳、蜜、水与酥酪**：多主滋养、亲人来临与喜讯，亦与康复与大利相关.
  - **看“子”与“离”的谐音暗示**：瓜子、枣、桑椹主生子与贵子；粟与梨则分别指向分离与失财.
  - **看菜与辛辣：清苦或争斗与灾害**：蔬菜过多而缺肉，象征清苦与虚弱；葱韭薤蒜则分别映照争斗、重伤与灾害；菜黄则为衰败之象.

- 详细解说：

  **（一）酒席与人情：从长命到家欲破**

  - “人请饮酒主长命；与人饮酒有口舌；与人吃会富贵至；筵会客人家欲破；饮酒者主哭泣事；饮酒至醉主疾病；贵人赐宴主疾病；与贵人对饮大吉；人请吃酥酪主喜”：
    - 受邀饮酒与吃会，多是在社会关系网络中被承认与接纳，故有长命与富贵之象；
    - 然而酒席同时也暗藏开销与是非，客人多则家欲破，饮酒多则易哭泣与疾病；
    - 被贵人赐宴虽显荣耀，却往往伴随劳心劳神与应酬压力，故主疾病；
    - 与贵人平等对饮则偏向真诚相交，反而大吉；
    - 酥酪等细致饮食则多主喜讯与身心愉悦.

  **（二）乳、蜜与呕吐：滋养与排浊**

  - “与人吃乳尊亲至；与人吃蜜大吉利；呕吐者病人主瘥”：
    - 乳象征母性与长辈之爱，与人共食乳，多主尊亲到来与家族扶助；
    - 蜜甘而不腻，梦中常指顺利与大吉利；
    - 呕吐则是将污浊之物排出体外，故病人梦此多主病情好转.

  **（三）肉食与争讼、疾病与别离**

  - “食牛肉于堂上吉；食犬肉主有争讼；食猪肉主疾病至；刀割猪肉主生病；食生肉凶熟肉吉；食自死肉主别离；食鹅肉主妾疾病；食鸡鸭等肉皆吉”：
    - 牛肉常被视为厚重、稳实之肉，于堂上食之，多主庄重场合中的福泽与安稳；
    - 犬肉与争讼相连，提示“咬来咬去”的官非与是非；
    - 猪肉肥腻，过食损身，故主疾病，甚至主动“刀割”亦主自招病源；
    - 生肉代表潜在的危险与不洁，熟肉则为可安全使用的资源；
    - 自死肉来源不祥，主别离与不测；
    - 鹅与妾媵相连，梦食鹅肉多主妾有疾病；
    - 鸡鸭等肉为日常可食之物，多主吉.

  **（四）谷物与瓜果：子嗣与心愿**

  - “食馒头主口舌散；见馒头未食主气；食烂瓜主生疾病；食饼食饭心不遂；食瓜子主生贵子；食柿食柑主疾病；食柿桃离而复合；食枣者主生贵子；食桑椹主生贵子；食粟者主有分离；食梨者主失财帛”：
    - 馒头既是口腹享受，又与“口舌”谐象：吃了则口舌散，见而未食则心中有气；
    - 烂瓜与不洁之物相似，主生疾病；
    - 饼饭不遂口味，象征现实欲望与内心不合，故心不遂；
    - 瓜子、枣、桑椹因“多子”与“补血生子”的传统观念，多主生贵子；
    - 柿与柑性寒或湿，多主小病；
    - 柿桃离而复合，则用“离”“核”等象意，表达感情或关系上的一离一合；
    - 粟与梨则借音寓“疏”“离”，指向疏远与失财.

  **（五）蔬菜与辛辣：清苦、争斗与灾害**

  - “食一切菜者凶至；食茄者主妻有子；食葱韭主有争斗；食薤者有重伤至；食蒜者主灾害至；食菜见菜黄主凶；食油盐酱酸豉吉”：
    - “一切菜”多指清苦饮食，缺乏油水，主生活清苦与身体虚弱，故凶；
    - 茄与“茄子多籽”相连，故主妻有子；
    - 葱韭味辛、气冲，象征争斗与不和；
    - 薤与蒜辛辣更甚，主重伤与灾害，提示需防意外或激烈冲突；
  - 菜色发黄则为枯败之象，多主凶；
  - 油盐酱酸豉则使饮食有滋有味，象征生活调和有度，故主吉.



- **完整对等诠释（secondary_lang_full）**：

  This category centers on dreams of eating and drinking—wine, meat, grains, fruit, and vegetables—and reads them as signs of how resources, nourishment, and social exchange are flowing in a person's life. Food and drink in dreams are not only about appetite; they reveal whether the dreamer is being adequately nourished in body and circumstance, or experiencing lack, excess, or imbalance.

  When the dream presents ample wine and meat, banquets, being invited to drink, or sharing feasts with others, it points to rich resources and strong social ties. These images suggest that material support, cooperation, and goodwill are available, and that the dreamer may enjoy prosperity, successful collaborations, or occasions for celebration. Being invited to drink, receiving food, or attending a feast often means being recognized and included by others.

  By contrast, scenes of eating only plain vegetables, lacking oil and richness, or seeing vegetables turn yellow indicate hardship, fatigue, or a sparse living situation. Spicy and sharp flavors such as scallions, leeks, or strong garlic mirror quarrels, conflicts, and potentially wounding words; certain vegetables associated with bitterness or pallor warn of illness or misfortune. Dreams in which food is insufficient or tasteless highlight a sense of not being properly nourished—whether in finances, relationships, or emotional life.

  Seasonings like oil, salt, sauces, and fermented condiments represent the art of moderation and balance. When they appear in the right measure, they transform plain food into something satisfying, symbolizing a life where basic needs are met and flavored by enjoyment and harmony. Overall, this category teaches that abundance, variety, and shared meals forecast supportive networks and good fortune, whereas thin, harsh, or joyless eating points to depletion, friction, or the need to adjust how one is feeding themselves and others on all levels.

- 校勘与字词辨析：

  - 本类原文多为"三句并列"体，如"人请饮酒主长命　与人饮酒有口舌　与人吃会富贵至"，本稿在 L1 层按句意拆分为独立句，并加标点，严格保留原有词序与字形。
  - "酥酪"一词，本稿理解为乳制品之精华，不改作现代"奶酪"，仅在释义中以"丰腴之品"释义。
  - "食一切菜者凶至"句，"一切菜"本稿理解为"仅食蔬菜而无油水"之意，象征生活清苦，故主凶。
  - "食葱韭主有争斗"中"葱韭"皆辛辣之物，本稿按"辛辣冲人"释义，不展开具体蔬菜考证。
  - 诸如"筵会客人家欲破""饮酒者主哭泣事"等看似反常之语，本稿在 L1 层保留原判词，在详细解说中以"宴席散财、酒后失态"等象征意涵补充说明。

  - **English**：
    - The original text in this category mostly follows the "three parallel phrases" format, e.g. "人请饮酒主长命　与人饮酒有口舌　与人吃会富贵至." This edition splits them by meaning into independent sentences at the L1 layer, adding punctuation while strictly preserving the original word order and character forms.
    - The term "酥酪" is understood as the essence of dairy products, not changed to modern "cheese," interpreted simply as "rich delicacy" in the explanation.
    - In "食一切菜者凶至," the phrase "一切菜" is understood as "eating only vegetables without oil," symbolizing a life of hardship, hence inauspicious.
    - In "食葱韭主有争斗," both "葱" and "韭" are pungent items. This edition interprets them as "pungent and offensive" without detailed vegetable research.
    - Seemingly contradictory phrases like "筵会客人家欲破" and "饮酒者主哭泣事" are preserved in original verdict form at the L1 layer, with symbolic meanings like "banquets dissipating wealth, losing composure after drinking" supplemented in the detailed commentary.



- **叙事素材（narrative_snippets）**：

  - `[ns_zgjm_552]` `[trigger: 梦见人请饮酒]` `[factor_trigger: dream_invited_drink]` `[role: 主干]` 人请饮酒，主长命。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_553]` `[trigger: 梦见与人饮酒]` `[factor_trigger: dream_drink_with]` `[role: 主干]` 与人饮酒，有口舌。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_554]` `[trigger: 梦见与人吃会]` `[factor_trigger: dream_feast_together]` `[role: 主干]` 与人吃会，富贵至。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_555]` `[trigger: 梦见筵会客人]` `[factor_trigger: dream_banquet_guest]` `[role: 主干]` 筵会客人，家欲破。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_556]` `[trigger: 梦见饮酒者]` `[factor_trigger: dream_drink_alone]` `[role: 主干]` 饮酒者，主哭泣事。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_557]` `[trigger: 梦见饮酒至醉]` `[factor_trigger: dream_drunk]` `[role: 主干]` 饮酒至醉，主疾病。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_558]` `[trigger: 梦见贵人赐宴]` `[factor_trigger: dream_noble_banquet]` `[role: 主干]` 贵人赐宴，主疾病。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_559]` `[trigger: 梦见与贵人对饮]` `[factor_trigger: dream_drink_noble]` `[role: 主干]` 与贵人对饮，大吉。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_560]` `[trigger: 梦见人请吃酥酪]` `[factor_trigger: dream_eat_cheese]` `[role: 主干]` 人请吃酥酪，主喜。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_561]` `[trigger: 梦见与人吃乳]` `[factor_trigger: dream_eat_milk]` `[role: 主干]` 与人吃乳，尊亲至。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_562]` `[trigger: 梦见与人吃蜜]` `[factor_trigger: dream_eat_honey]` `[role: 主干]` 与人吃蜜，大吉利。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_563]` `[trigger: 梦见呕吐者]` `[factor_trigger: dream_vomit]` `[role: 主干]` 呕吐者，病人主瘥。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_564]` `[trigger: 梦见食水者]` `[factor_trigger: dream_drink_water]` `[role: 主干]` 食水者，主得大利。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_565]` `[trigger: 梦见死人食者]` `[factor_trigger: dream_dead_eat]` `[role: 主干]` 死人食者，主疾病。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_566]` `[trigger: 梦见食牛肉于堂上]` `[factor_trigger: dream_eat_beef]` `[role: 主干]` 食牛肉于堂上，吉。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_567]` `[trigger: 梦见食犬肉]` `[factor_trigger: dream_eat_dog]` `[role: 主干]` 食犬肉，主有争讼。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_568]` `[trigger: 梦见食猪肉]` `[factor_trigger: dream_eat_pork]` `[role: 主干]` 食猪肉，主疾病至。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_569]` `[trigger: 梦见刀割猪肉]` `[factor_trigger: dream_cut_pork]` `[role: 主干]` 刀割猪肉，主生病。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_570]` `[trigger: 梦见食生肉]` `[factor_trigger: dream_eat_raw]` `[role: 主干]` 食生肉凶，熟肉吉。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_571]` `[trigger: 梦见食自死肉]` `[factor_trigger: dream_eat_dead_meat]` `[role: 主干]` 食自死肉，主别离。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_572]` `[trigger: 梦见食鹅肉]` `[factor_trigger: dream_eat_goose]` `[role: 主干]` 食鹅肉，主妾疾病。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_573]` `[trigger: 梦见食鸡鸭等肉]` `[factor_trigger: dream_eat_poultry]` `[role: 主干]` 食鸡鸭等肉，皆吉。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_574]` `[trigger: 梦见食馒头]` `[factor_trigger: dream_eat_bun]` `[role: 主干]` 食馒头，主口舌散。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_575]` `[trigger: 梦见见馒头未食]` `[factor_trigger: dream_see_bun]` `[role: 主干]` 见馒头未食，主气。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_576]` `[trigger: 梦见食烂瓜]` `[factor_trigger: dream_eat_rotten_melon]` `[role: 主干]` 食烂瓜，主生疾病。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_577]` `[trigger: 梦见食饼食饭]` `[factor_trigger: dream_eat_cake_rice]` `[role: 主干]` 食饼食饭，心不遂。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_578]` `[trigger: 梦见食瓜子]` `[factor_trigger: dream_eat_melon_seed]` `[role: 主干]` 食瓜子，主生贵子。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_579]` `[trigger: 梦见食柿食柑]` `[factor_trigger: dream_eat_persimmon]` `[role: 主干]` 食柿食柑，主疾病。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_580]` `[trigger: 梦见食柿桃]` `[factor_trigger: dream_eat_peach]` `[role: 主干]` 食柿桃，离而复合。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_581]` `[trigger: 梦见食枣者]` `[factor_trigger: dream_eat_date]` `[role: 主干]` 食枣者，主生贵子。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_582]` `[trigger: 梦见食桑椹]` `[factor_trigger: dream_eat_mulberry]` `[role: 主干]` 食桑椹，主生贵子。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_583]` `[trigger: 梦见食粟者]` `[factor_trigger: dream_eat_millet]` `[role: 主干]` 食粟者，主有分离。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_584]` `[trigger: 梦见食梨者]` `[factor_trigger: dream_eat_pear]` `[role: 主干]` 食梨者，主失财帛。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_585]` `[trigger: 梦见食一切菜者]` `[factor_trigger: dream_eat_vegetables]` `[role: 主干]` 食一切菜者，凶至。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_586]` `[trigger: 梦见食茄者]` `[factor_trigger: dream_eat_eggplant]` `[role: 主干]` 食茄者，主妻有子。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_587]` `[trigger: 梦见食葱韭]` `[factor_trigger: dream_eat_scallion]` `[role: 主干]` 食葱韭，主有争斗。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_588]` `[trigger: 梦见食薤者]` `[factor_trigger: dream_eat_allium]` `[role: 主干]` 食薤者，有重伤至。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_589]` `[trigger: 梦见食蒜者]` `[factor_trigger: dream_eat_garlic]` `[role: 主干]` 食蒜者，主灾害至。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_590]` `[trigger: 梦见食菜见菜黄]` `[factor_trigger: dream_eat_yellow_veg]` `[role: 主干]` 食菜见菜黄，主凶。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_591]` `[trigger: 梦见食油盐酱酸豉]` `[factor_trigger: dream_eat_condiment]` `[role: 主干]` 食油盐酱酸豉，吉。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_984]` `[trigger: 梦见枯木开花]` `[factor_trigger: dream_deadwood_bloom]` `[role: 主干]` 梦见枯木开花，主子兴。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_985]` `[trigger: 梦见得财]` `[factor_trigger: dream_decai]` `[role: 主干]` 梦见得财，主有财。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_986]` `[trigger: 梦见污秽]` `[factor_trigger: dream_dirty]` `[role: 主干]` 梦见污秽，主有辱。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_987]` `[trigger: 梦见羞辱]` `[factor_trigger: dream_disgrace]` `[role: 主干]` 梦见羞辱，主受辱。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_988]` `[trigger: 梦见门开]` `[factor_trigger: dream_door_open]` `[role: 主干]` 梦见门开，主有客。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_989]` `[trigger: 梦见龙死]` `[factor_trigger: dream_dragon_death]` `[role: 主干]` 梦见龙死，主失贵。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_990]` `[trigger: 梦见龙旗]` `[factor_trigger: dream_dragon_flag]` `[role: 主干]` 梦见龙旗，主大贵。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_991]` `[trigger: 梦见龙门]` `[factor_trigger: dream_dragon_gate]` `[role: 主干]` 梦见龙门，主升迁。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_992]` `[trigger: 梦见拔剑]` `[factor_trigger: dream_draw_sword]` `[role: 主干]` 梦见拔剑，主有争。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_993]` `[trigger: 梦见干鱼复活]` `[factor_trigger: dream_dried_fish_revive]` `[role: 主干]` 梦见干鱼复活，主吉。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_994]` `[trigger: 梦见鼓声]` `[factor_trigger: dream_drum_sound]` `[role: 主干]` 梦见鼓声，主有事。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_995]` `[trigger: 梦见地裂]` `[factor_trigger: dream_earth_crack]` `[role: 主干]` 梦见地裂，主有忧。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_996]` `[trigger: 梦见地动]` `[factor_trigger: dream_earth_move]` `[role: 主干]` 梦见地动，主迁居。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_997]` `[trigger: 梦见空市]` `[factor_trigger: dream_empty_market]` `[role: 主干]` 梦见空市，主破财。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_998]` `[trigger: 梦见入市]` `[factor_trigger: dream_enter_market]` `[role: 主干]` 梦见入市，主有财。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_999]` `[trigger: 梦见入宫]` `[factor_trigger: dream_enter_palace]` `[role: 主干]` 梦见入宫，主大贵。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_1000]` `[trigger: 梦见粪污身]` `[factor_trigger: dream_excrement_body]` `[role: 主干]` 梦见粪污身，主得财。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_1001]` `[trigger: 梦见失败]` `[factor_trigger: dream_failure]` `[role: 主干]` 梦见失败，主破财。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_1002]` `[trigger: 梦见声名]` `[factor_trigger: dream_fame]` `[role: 主干]` 梦见声名，主显达。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_1003]` `[trigger: 梦见分国有]` `[factor_trigger: dream_fenguo_you]` `[role: 主干]` 梦见分国有，主有忧。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_1004]` `[trigger: 梦见分散]` `[factor_trigger: dream_fensan]` `[role: 主干]` 梦见分散，主离别。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_1005]` `[trigger: 梦见田荒]` `[factor_trigger: dream_field_barren]` `[role: 主干]` 梦见田荒，主破财。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_1006]` `[trigger: 梦见田草]` `[factor_trigger: dream_field_grass]` `[role: 主干]` 梦见田草，主有忧。 → 《周公解梦·饮食酒肉瓜菜》
  - `[ns_zgjm_1007]` `[trigger: 梦见田熟]` `[factor_trigger: dream_field_ripe]` `[role: 主干]` 梦见田熟，主大吉。 → 《周公解梦·饮食酒肉瓜菜》"""
    normalized_text_zh: str = """"""
    subject: str = "饮食酒肉瓜菜"
    factor_refs: list = ['zgjm_15_invited_drink_proposal', 'zgjm_15_drink_together_proposal', 'zgjm_15_shared_feast_proposal', 'zgjm_15_eat_carrion_meat_proposal', 'zgjm_15_eat_melon_seeds_proposal', 'zgjm_15_eat_only_vegetables_proposal', 'zgjm_15_eat_scallion_leek_proposal', 'zgjm_15_eat_seasonings_proposal']
    
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
        l1_anchor="zgjm_v1.0.0_饮食酒肉瓜菜_001_L1",
    )
    version: str = "1.0.0"
