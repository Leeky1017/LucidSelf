"""
Auto-generated semantic module for zhougong
Generated at: 2025-12-05T13:30:19.864370
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
    semantic_id="zgjm_v1.0.0_镜环钗钏梳篦_001",
    book_id="zhougong",
    engine_id="dream"
)
class 镜环钗钏梳篦(SemanticEntry):
    """
    - **原文（source_text）**：

  【类名】

  镜环钗钏梳篦。

  【条文】

  明镜者吉，暗者凶。
  拾得镜者，招好妻。
  将镜自照，远信至。

  镜照他人，妻妾凶。
...
    """
    
    original_text: str = """- **原文（source_text）**：

  【类名】

  镜环钗钏梳篦。

  【条文】

  明镜者吉，暗者凶。
  拾得镜者，招好妻。
  将镜自照，远信至。

  镜照他人，妻妾凶。
  得他人镜，有贵子。
  他人弄己镜，妻凶。

  镜破，主夫妻离别。
  金钗动，有远行事。
  金钿成双，增爱妾。

  钗钏相敲，妻别凶。
  金钗耀，主生贵子。
  花钗，妻妾有奸佞。

  银钏，夫妻主相殴。
  花压，妻妾生外心。
  人与梳篦，得美妾。

  牙木梳，旧事尽去。
  见篦子，贵人提携。
  得篦子者，美女至。

  刷牙者，病患不生。
  得胭脂粉，主生女。
  见脂粉，主大财利。

  得粉仆，妻生娇女。
  手帕者，主口舌事。
  针线得者，百事就。

- 分字分词释义：

  - **镜环钗钏梳篦**：本类总纲，涵盖镜子、头面环饰（镜环）、钗钏钿等首饰，以及梳篦、牙刷、脂粉、手帕与针线等修饰整理之物，多与**自我形象、男女情爱与妻妾内外之事**相关。
  - **明镜者吉，暗者凶**：明镜可照见本来面目，象征自知与关系清明，为吉；暗镜模糊不明，多主误会、隐情与判断失真。
  - **拾得镜者，招好妻；将镜自照，远信至**：拾得好镜，多主遇良缘或得能映照自己的伴侣；手持明镜自照，则将自身形象投向远方，故主远方来信或远人消息。
  - **镜照他人，妻妾凶；得他人镜，有贵子；他人弄己镜，妻凶**：镜与他人之间的互动，象征第三者介入与关系焦点转移：照他人或被他人把玩己镜，皆使正缘受损；惟得他人镜而生贵子，偏向“外缘得子”或因旁系资源得贵子之象。
  - **镜破，主夫妻离别**：镜为照形之具，亦象征夫妻合照之“合一”状态；镜破，则象征关系裂痕难以弥合。
  - **金钗动有远行事；金钿成双增爱妾；钗钏相敲妻别凶**：钗、钿、钏本为妇人首饰：动、成双或相敲，分别指涉远行之事、偏重妾媵与夫妻别离的隐忧。
  - **金钗耀主生贵子；花钗妻妾有奸佞；银钏夫妻主相殴**：金钗光耀，多主贵子与喜庆；花钗与银钏则提醒：外表华艳与腕上束饰皆易引发心机与争执，故有奸佞与相殴之象。
  - **牙木梳旧事尽去；见篦子贵人提携；得篦子者美女至**：牙梳、木梳、篦子皆为齿密之梳，用以梳理发髻与虱卵，象征对旧事与细碎烦恼的清理；篦子由人所赠，多主贵人或美貌女子到来。
  - **刷牙者病患不生**：牙齿为咀嚼之具，刷牙洁净口腔，多主预防疾病与积患，象征“从入口处清理病源”。
  - **得胭脂粉主生女；见脂粉主大财利；得粉仆妻生娇女**：脂粉既关女子妆饰，又关生活细腻程度：得之或见之，多主生女、得财，或得温婉贴身之人相助。
  - **手帕者主口舌事；针线得者百事就**：手帕用于拭泪拭汗、遮掩面容，多主口舌是非与情绪波动；针线则象征缝补与整合，主经手之事终能缝合成就。

- **规范化释义（primary_lang_explained）**：

  本类通过镜、钗、钏、梳篦与脂粉等物，描绘的是一个人如何**看见自己、打理外在形象，并处理感情与婚姻关系**：

  - 镜若明亮，象征自知与关系晴朗；镜若昏暗或破裂，则象征误解、隐情与重大裂痕。
  - 钗钿与钏镯多围绕妻妾、妾媵与远行之事：动、成双与相敲，对应行役在外、感情结构复杂与夫妻别离的隐忧。
  - 梳篦与刷牙则强调“梳理与清理”：旧事尽去、病患不生，都是在暗示通过整理与清洁，来告别旧有烦恼与病源。
  - 脂粉与“粉仆”牵连生女、娇妾与财利，一方面提示柔情与享乐，另一方面也提醒注意情感债与物质欲望。
  - 手帕与针线则分别指向“情绪与口舌”以及“缝补与完成”，提示在情感和事务上，一边要谨慎言语，一边要有耐心修补。

- 核心要点：

  - **看镜：明、暗与破**——明则吉、暗则凶、破则离，直接映射自知程度与夫妻关系的完整与否。
  - **看钗钏：动静与成双**——动与相敲多主行役与争执；成双与耀目则主荣宠与贵子，但也容易引入感情结构的复杂化。
  - **看梳篦与刷牙：整理与清洁**——主动梳理与清洁，是对旧事与病患的“主动处理”，多主先劳后安。
  - **看脂粉与粉仆：柔情与欲望**——脂粉之梦多主女子、财利与享乐，也提示对享乐与形象投入的适度把握。
  - **看手帕与针线：口舌与缝补**——有手帕则有泪与言语要收拾；得针线则预示具备缝补裂痕、成就诸事的能力。

- 详细解说：

  **（一）镜像关系：自我与他人的投射**

  - “明镜者吉，暗者凶；拾得镜者，招好妻；将镜自照，远信至”三条，勾勒出镜在自我与外缘之间的桥梁：
    - 明镜如同一面清晰的自我认知；
    - 拾得好镜意味着获得能照见自己优劣的伴侣或友人；
    - 自照则是将注意力回到自身，故主来自远方的回应与信息。
  - “镜照他人，妻妾凶；得他人镜，有贵子；他人弄己镜，妻凶”则刻画了当镜在三方之间流转时，关系结构如何受影响：
    - 当镜不再用来照自己或伴侣，而是照向他人时，易引发外遇、妒忌与失衡；
    - 得他人之镜而得贵子，则可视为外缘带来的子嗣或资源；
    - 他人把玩己镜，则象征有人介入自己的亲密关系，需要警惕。
  - “镜破，主夫妻离别”更是以“破镜”直指关系破裂：梦中若见镜破而心中不安，现实中宜及早沟通与修补。

  **（二）钗钿钏与花压：华饰之下的心机与别离**

  - “金钗动，有远行事；金钿成双，增爱妾；钗钏相敲，妻别凶；金钗耀，主生贵子；花钗，妻妾有奸佞；银钏，夫妻主相殴；花压，妻妾生外心”一组，将首饰之动静与成双，化为情感结构的指示：
    - 钗动与花压多主心绪不安、外缘牵动；
    - 钿成双、金钗耀则偏向荣宠、贵子与宠爱偏重某一方；
    - 钗钏相敲与银钏相殴，则是争执、冲突与夫妻相别的象。
  - 现代视角下，可将这些理解为：在外在装饰、身份标签与感情需求的交错中，关系容易出现偏心、竞争与暗中较量，需要双方保持坦诚与界限。

  **（三）梳篦与刷牙：从外在到入口的清理**

  - “牙木梳，旧事尽去；见篦子，贵人提携；得篦子者，美女至；刷牙者，病患不生”显示：
    - 梳篦一方面梳理头发与虱卵，另一方面也象征整理旧日牵挂与烦恼；
    - 刷牙则从入口处净化，将未来可能的病源与污秽事先扫除。
  - 梦中若见梳篦与刷牙并现，可理解为梦者正处于一个“清理旧事、修整自我”的阶段，有利于之后迎接新的关系与机会。

  **（四）脂粉、粉仆与手帕：情绪、柔情与口舌**

  - “得胭脂粉主生女；见脂粉主大财利；得粉仆妻生娇女；手帕者主口舌事”一组，既有柔情蜜意，也有口舌纷争：
    - 脂粉与粉仆侧重女性化、柔软与享乐之面，主生女、娇妾与财利；
    - 手帕则更多指向眼泪、叹息与需要擦拭之处，预示有口舌与情绪需要处理。
  - 现实中，可理解为：在追求精致生活与情感体验时，也要同时关注沟通品质与界限，以免因小事滋生争执。

  **（五）针线：缝补与成事的耐心功夫**

  - “针线得者，百事就”强调的是一种缓慢而细致的完成方式：
    - 不是依靠一次性的大动作，而是靠一针一线的连续努力；
    - 对应现实中的长期协商、修补与精细工作。
  - 梦中得针线者，往往提示：只要愿意投入这种“针线式”的细致工夫，现实中的关系与事业皆有机会缝补与成就。



 - **完整对等诠释（secondary_lang_full）**：

  This category gathers dream omens relating to mirrors, rings, hairpins, bracelets, combs, and other personal ornaments. These images map onto **self-image, marital relationships, personal grooming, and intimate connections**.

  The core interpretive principle focuses on the condition and use of these intimate objects: clear mirrors that reflect truly indicate self-knowledge and clarity; broken or dim mirrors warn of marital troubles or self-deception. Intact rings and bracelets symbolize unbroken bonds and commitments; broken jewelry warns of relationship rupture. Combs and hairpins relate to personal order and domestic harmony—smooth combing suggests orderly life; broken combs or lost hairpins indicate domestic discord or partner troubles.

  **Key interpretive axes**:
  - **Mirrors**: clarity indicates truthful self-reflection and good fortune; broken mirrors traditionally warn of marital separation; dim mirrors suggest confusion or deception.
  - **Rings and bracelets**: complete circles symbolize wholeness and committed relationships; broken or lost rings warn of broken bonds; receiving rings often portends marriage or important commitments.
  - **Hairpins and ornaments**: intact hairpins indicate stable relationships; breaking or losing hairpins warns of separation from spouse or partner; elaborate ornaments relate to social status.
  - **Combs**: successful combing indicates orderly domestic life; tangled hair or broken combs suggest family troubles; combing another's hair indicates intimate care.
  - **Fullness or emptiness**: storerooms filled with goods promise prosperity; empty rooms suggest poverty or loss.- 校勘与字词辨析：

  - 本类原文多以三句并列连写，如“明镜者吉暗者凶　拾得镜者招好妻　将镜自照远信至”，本稿在 L1 层拆为三句并加标点，以便现代阅读，同时严格保留字序。
  - “金钿成双增爱妾”之“钿”，各本或作“鈿”，本稿据底本从简录作“钿”，在释义中按成双之华饰理解，不再赘述形制。
  - “得粉仆妻生娇女”一句，“粉仆”一作“粉扑”，本稿依底本保留“粉仆”二字，在释义中按与脂粉相关之仆役或器物解释。
  - 诸如“妻妾有奸佞”“妻妾生外心”等语，带有浓厚时代性与性别偏见，本稿在 L1 层保留原判词，同时在详细解说中转化为“感情结构复杂、心机与外缘牵连”等较中性的表达，为后续高阶语义层留下调整空间。

  - **English**：
    - The original text presents entries in groups of three parallel phrases, e.g. "明镜者吉暗者凶　拾得镜者招好妻　将镜自照远信至." This edition splits them into three sentences with punctuation at the L1 layer for modern reading convenience while strictly preserving character order.
    - In "金钿成双增爱妾," the character "钿" appears in some editions as "鈿." This edition follows the base text using the simplified "钿," interpreting it as paired ornamental jewelry without elaborating on specific forms.
    - In "得粉仆妻生娇女," the term "粉仆" appears in some versions as "粉扑." This edition preserves "粉仆" per the base text, interpreting it as servants or objects related to cosmetic powder.
    - Phrases such as "妻妾有奸佞" and "妻妾生外心" carry strong period-specific characteristics and gender biases. The L1 layer preserves the original verdict while transforming it in the detailed commentary to more neutral expressions like "complex emotional structures, scheming and external entanglements," leaving room for adjustment in higher semantic layers.



- **叙事素材（narrative_snippets）**：

  - `[ns_zgjm_398]` `[trigger: 梦见明镜者]` `[factor_trigger: dream_bright_mirror]` `[role: 主干]` 明镜者吉，暗者凶。 → 《周公解梦·镜环钗钏梳篦》
  - `[ns_zgjm_399]` `[trigger: 梦见拾得镜者]` `[factor_trigger: dream_find_mirror]` `[role: 主干]` 拾得镜者，招好妻。 → 《周公解梦·镜环钗钏梳篦》
  - `[ns_zgjm_400]` `[trigger: 梦见将镜自照]` `[factor_trigger: dream_mirror_self]` `[role: 主干]` 将镜自照，远信至。 → 《周公解梦·镜环钗钏梳篦》
  - `[ns_zgjm_401]` `[trigger: 梦见镜照他人]` `[factor_trigger: dream_mirror_other]` `[role: 主干]` 镜照他人，妻妾凶。 → 《周公解梦·镜环钗钏梳篦》
  - `[ns_zgjm_402]` `[trigger: 梦见得他人镜]` `[factor_trigger: dream_get_mirror]` `[role: 主干]` 得他人镜，有贵子。 → 《周公解梦·镜环钗钏梳篦》
  - `[ns_zgjm_403]` `[trigger: 梦见他人弄己镜]` `[factor_trigger: dream_other_mirror]` `[role: 主干]` 他人弄己镜，妻凶。 → 《周公解梦·镜环钗钏梳篦》
  - `[ns_zgjm_404]` `[trigger: 梦见镜破]` `[factor_trigger: dream_mirror_break]` `[role: 主干]` 镜破，主夫妻离别。 → 《周公解梦·镜环钗钏梳篦》
  - `[ns_zgjm_405]` `[trigger: 梦见金钗动]` `[factor_trigger: dream_hairpin_move]` `[role: 主干]` 金钗动，有远行事。 → 《周公解梦·镜环钗钏梳篦》
  - `[ns_zgjm_406]` `[trigger: 梦见金钿成双]` `[factor_trigger: dream_ornament_pair]` `[role: 主干]` 金钿成双，增爱妾。 → 《周公解梦·镜环钗钏梳篦》
  - `[ns_zgjm_407]` `[trigger: 梦见钗钏相敲]` `[factor_trigger: dream_hairpin_clash]` `[role: 主干]` 钗钏相敲，妻别凶。 → 《周公解梦·镜环钗钏梳篦》
  - `[ns_zgjm_408]` `[trigger: 梦见金钗耀]` `[factor_trigger: dream_hairpin_shine]` `[role: 主干]` 金钗耀，主生贵子。 → 《周公解梦·镜环钗钏梳篦》
  - `[ns_zgjm_409]` `[trigger: 梦见花钗]` `[factor_trigger: dream_flower_hairpin]` `[role: 主干]` 花钗，妻妾有奸佞。 → 《周公解梦·镜环钗钏梳篦》
  - `[ns_zgjm_410]` `[trigger: 梦见银钏]` `[factor_trigger: dream_silver_bracelet]` `[role: 主干]` 银钏，夫妻主相殴。 → 《周公解梦·镜环钗钏梳篦》
  - `[ns_zgjm_411]` `[trigger: 梦见花压妻妾]` `[factor_trigger: dream_flower_press]` `[role: 主干]` 花压妻妾，生外心。 → 《周公解梦·镜环钗钏梳篦》
  - `[ns_zgjm_412]` `[trigger: 梦见人与梳篦]` `[factor_trigger: dream_give_comb]` `[role: 主干]` 人与梳篦，得美妾。 → 《周公解梦·镜环钗钏梳篦》
  - `[ns_zgjm_413]` `[trigger: 梦见牙木梳]` `[factor_trigger: dream_tooth_comb]` `[role: 主干]` 牙木梳，旧事尽去。 → 《周公解梦·镜环钗钏梳篦》
  - `[ns_zgjm_414]` `[trigger: 梦见见篦子]` `[factor_trigger: dream_see_comb]` `[role: 主干]` 见篦子，贵人提携。 → 《周公解梦·镜环钗钏梳篦》
  - `[ns_zgjm_415]` `[trigger: 梦见得篦子者]` `[factor_trigger: dream_get_comb]` `[role: 主干]` 得篦子者，美女至。 → 《周公解梦·镜环钗钏梳篦》
  - `[ns_zgjm_416]` `[trigger: 梦见刷牙者]` `[factor_trigger: dream_brush_teeth]` `[role: 主干]` 刷牙者，病患不生。 → 《周公解梦·镜环钗钏梳篦》
  - `[ns_zgjm_417]` `[trigger: 梦见得胭脂粉]` `[factor_trigger: dream_get_rouge]` `[role: 主干]` 得胭脂粉，主生女。 → 《周公解梦·镜环钗钏梳篦》
  - `[ns_zgjm_418]` `[trigger: 梦见见脂粉]` `[factor_trigger: dream_see_powder]` `[role: 主干]` 见脂粉，主大财利。 → 《周公解梦·镜环钗钏梳篦》
  - `[ns_zgjm_419]` `[trigger: 梦见得粉仆]` `[factor_trigger: dream_get_powder]` `[role: 主干]` 得粉仆，妻生娇女。 → 《周公解梦·镜环钗钏梳篦》
  - `[ns_zgjm_420]` `[trigger: 梦见手帕者]` `[factor_trigger: dream_handkerchief]` `[role: 主干]` 手帕者，主口舌事。 → 《周公解梦·镜环钗钏梳篦》
  - `[ns_zgjm_421]` `[trigger: 梦见针线得者]` `[factor_trigger: dream_needle_thread]` `[role: 主干]` 针线得者，百事就。 → 《周公解梦·镜环钗钏梳篦》

---"""
    normalized_text_zh: str = """"""
    subject: str = "镜环钗钏梳篦"
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
        l1_anchor="zgjm_v1.0.0_镜环钗钏梳篦_001_L1",
    )
    version: str = "1.0.0"
