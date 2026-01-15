"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264383
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
    semantic_id="smth_v1.0.0_十干五合与方位色象_嫁娶比喻与本家归宗_001",
    book_id="sanming",
    engine_id="bazi"
)
class 十干五合与方位色象嫁娶比喻与本家归宗(SemanticEntry):
    """
    - **原文（source_text）**：  
  东方甲乙木畏西方庚辛金克，甲属阳为兄，乙属阴为妹，甲兄遂将乙妹嫁金家，与庚为妻，所以乙与庚合，乙虽嫁与庚为妻，春来木旺金囚，不畏金克乙，遂归本家就...
    """
    
    original_text: str = """- **原文（source_text）**：  
  东方甲乙木畏西方庚辛金克，甲属阳为兄，乙属阴为妹，甲兄遂将乙妹嫁金家，与庚为妻，所以乙与庚合，乙虽嫁与庚为妻，春来木旺金囚，不畏金克乙，遂归本家就甲，然不免在金家怀胎，归木家产。木色青，金色白，是以春来园林木青，叶开白花。南方丙丁火畏北方壬癸水克，丙属阳为兄，丁属阴为妹。丙兄遂将丁妹嫁水家，与壬为妻，所以丁与壬合，丁虽嫁与壬为妻。夏来火旺水囚，不畏水克丁，遂归火家就丙，然不免在水家怀胎，归火家产。水色黑，火色赤。小满后，桑椹孰当有赤。中央戊巳土，畏东方甲乙木克，戊属阳为兄，己属阴为妹。戊兄遂将己妹嫁木家，与甲为妻，所以甲与己合，己虽嫁与甲为妻。六月土旺木囚，不畏木克己，遂归土家就戊，然不免在甲家怀胎，归戊家产。土色黄，木色青，所以六月甜瓜虽熟，肉黄皮青。西方庚辛金，畏南方丙丁火克，庚属阳为兄，辛属阴为妹，庚兄乃将辛妹嫁火家，与丙为妻，所以丙与辛合，辛虽嫁与丙为妻。秋来金旺火囚，不畏火克辛，乃归金家就庚，然不免在火家怀胎，归金家产。火赤金白。秋中枣熟，有半赤半白之状，枫叶丹。北方壬癸水，畏中央戊巳土克。壬属阳为兄，癸属阴为妹。壬兄乃将癸妹嫁土家，与戊为妻，所以戊与癸合，癸虽嫁与戊为妻。冬来水旺土囚，不畏土克癸，遂归水家就壬，然不免在戊家怀胎，归壬家产。水黑土黄，严冬霜雪，草木死而黄出。

- **规范化释义（primary_lang_explained）**：  
  本段通过“兄妹嫁娶”的拟人比喻，把五组干合放进五行方位与季节色象之中。东方属木，甲为阳兄、乙为阴妹，本畏西方庚辛金之克，却说甲兄将乙妹“嫁”给庚金，于是形成乙庚之合；春季木旺金囚，乙虽名嫁金家，实则仍归木本位，因而“园林木青、叶开白花”，木青金白交织。南方属火，丙为兄、丁为妹，本畏北方壬癸水；丙兄将丁妹嫁与壬水，成丁壬之合。夏季火旺水囚，丁终究归回火家，小满后桑椹由黑转赤，显出水黑火赤之象。中央戊己土畏东方木，戊兄将己妹嫁与甲木，成甲己之合；六月土旺木囚，熟瓜“肉黄皮青”，土黄木青层层相包。西方庚辛金畏南方火，庚兄将辛妹嫁丙火，成丙辛之合；秋来金旺火囚，枣色半赤半白，枫叶殷红，皆火赤金白相映。北方壬癸水畏中央戊巳土，壬兄将癸妹嫁戊土，成戊癸之合；冬来水旺土囚，冰雪封地草木枯黄，呈现水黑土黄的画面。通过“嫁而不离宗”的故事，作者说明：干合表面上有“入赘”与“出嫁”的从属关系，但在旺季之中，合干终究要“归宗于本家五行”，不可只从字面理解“谁克谁、谁属谁”。

- **完整对等诠释（secondary_lang_full）**：  
  This passage uses a series of family dramas—elder brothers marrying off their younger sisters—to make the five stem combinations vivid within the framework of directions, seasons and colors. In the East, associated with Wood, Jia is the Yang elder brother and Yi the Yin younger sister. Wood in principle fears Western Metal, yet the story says Jia marries Yi to Geng, thus creating the Yi‑Geng pairing. In spring, however, Wood prospers and Metal is imprisoned; Yi, though nominally married into the Metal household, effectively "belongs" to her Wood family, reflected in green trees bearing white blossoms. In the South, linked to Fire, Bing and Ding fear Northern Water; Bing marries Ding to Ren, forming the Ding‑Ren union, but in summer Fire flourishes while Water is constrained, so Ding essentially returns to Fire, just as dark mulberries ripen red. At the Centre, Wu and Ji Earth fear Eastern Wood; Wu marries Ji to Jia, yielding the Jia‑Ji combination, yet in the sixth month Earth is strong and Wood is confined, so ripe melons have yellow flesh wrapped in green rind—Earth‑yellow within Wood‑green. In the West, Metal fears Southern Fire; Geng marries Xin to Bing, giving the Bing‑Xin pairing, but in autumn Metal is powerful and Fire retreats, seen in red‑and‑white dates and crimson autumn leaves. In the North, Water fears Central Earth; Ren marries Gui to Wu, producing the Wu‑Gui bond, but in winter Water dominates and Earth is frozen, with blackish water under yellowed vegetation. The cumulative picture teaches that while stem combinations may suggest submission to a controlling element, seasonal strength and directional position ultimately decide where the qi truly resides and which party leads the relationship.

- **核心要点**：
  - 乙庚、丁壬、甲己、丙辛、戊癸五组合被安放在东南中西北与春夏长夏秋冬的具体场景中。
  - “兄妹嫁娶”的比喻区分了**名义从属**（嫁入他行）与**本质归属**（旺季仍归本家五行）。
  - 色象（青/白、黑/赤、黄/青、赤/白、黑/黄）把抽象干合具象化，便于记忆与理解五行归属。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_109]` `[trigger: 兄妹嫁娶]` `[factor_trigger: xiongmei_jiaqu AND yigeng_zhihe]` `[role: 主干]` 东方甲乙木畏西方庚辛金克，甲属阳为兄，乙属阴为妹，甲兄遂将乙妹嫁金家，与庚为妻。 → 《三命通会》卷十#十干五合与方位色象
  - `[ns_smth_10_110]` `[trigger: 归本家就甲]` `[factor_trigger: gui_benjia AND chunlai_muwang]` `[role: 主干依赖]` 春来木旺金囚，不畏金克乙，遂归本家就甲，然不免在金家怀胎，归木家产。 → 《三命通会》卷十#十干五合与方位色象
  - `[ns_smth_10_111]` `[trigger: 色象交织]` `[factor_trigger: sexiang_jiaozhi AND qingbai_heiqi]` `[role: 条件分支]` 木色青，金色白，是以春来园林木青，叶开白花。 → 《三命通会》卷十#十干五合与方位色象
  - `[ns_smth_10_112]` `[trigger: 严冬霜雪]` `[factor_trigger: yandong_shuangxue AND caomusi_huangchu]` `[role: 总结]` 水黑土黄，严冬霜雪，草木死而黄出。 → 《三命通会》卷十#十干五合与方位色象

- **详细解说**：  
  这一段最重要的启示，是把“谁克谁”“谁合谁”的静态关系放回到时空场景中：同样是乙庚之合，在春季木旺金囚时，乙木一方更具主导性；若换到秋金得令之时，庚辛金一方的约束力与定义力就会增强。工程化时，可以将“名义归属”与“时令归属”拆分建模：前者对应干合字面上的组合关系，后者则由时令旺衰与方位决定，二者并存而不必强行压成一个标签。比喻中“在他家怀胎，在本家生产”的写法，也提示干合常常意味着在异质环境中孕育结果，却最终由本家五行承载与落地，这对判断“成果归谁”“谁承担后果”尤为关键。

- **校勘与字词辨析（双语）**：
  - **中文**：“小满后，桑椹孰当有赤”一语，部分抄本作“半黑半赤”，本书从通行本，不影响“水黑火赤”色象之意；“甜瓜肉黄皮青”对应“土黄木青”，是中土与东方木叠加之象。
  - **English**: The kinship language of "elder brother" and "younger sister" is a mnemonic device for Yang and Yin within the same element rather than a literal social script. The seasonal images—mulberries, dates, melons, frost—serve as concrete anchors for remembering elemental dominance."""
    normalized_text_zh: str = """"""
    subject: str = "十干五合与方位色象：嫁娶比喻与本家归宗"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_十干五合与方位色象_嫁娶比喻与本家归宗_001_L1",
    )
    version: str = "1.0.0"
