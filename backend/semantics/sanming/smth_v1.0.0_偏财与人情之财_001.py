"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412659
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
    semantic_id="smth_v1.0.0_偏财与人情之财_001",
    book_id="sanming",
    engine_id="bazi"
)
class 偏财与人情之财(SemanticEntry):
    """
    - **原文（source_text）**：

  论偏财：何谓偏财？乃甲见戊、乙见己之例。非妻所带，乃众人之财也。切忌有姊妹兄弟分夺，柱无官星，祸患百出。经曰：偏财好出，亦不惧藏，唯怕分夺及落空亡，...
    """
    
    original_text: str = """- **原文（source_text）**：

  论偏财：何谓偏财？乃甲见戊、乙见己之例。非妻所带，乃众人之财也。切忌有姊妹兄弟分夺，柱无官星，祸患百出。经曰：偏财好出，亦不惧藏，唯怕分夺及落空亡，有一于此，官将不成，财将不住。如财弱，必待历旺乡而荣；财盛，无往不利，但恐身势无力，不能胜任。偏财格，主人慷慨，不甚吝财，与人有情而多诈。若是得地，不止财丰，亦能旺官，以财盛自生官，运行旺相，福禄俱臻，一遇官乡，便可发福。柱中原带官星，便作好命看；若兄弟辈出，纵入官乡，发福必渺。偏财月令所带最重，不宜柱中多逢。年上偏财生旺，月令柱中通气，主受伯叔祖考产业丰隆，或外祖产业恩养。大要日主兴隆，财星生旺，运向财旺之乡发福。若见刑冲破害、比劫分夺，或财星太衰、日主太弱，或财多生煞，皆破祖劳碌之命。凡月令有财，主少年富贵；若生时不得地，或有劫败，更运临凶地，晚年祖财破尽，终身困穷，先富后贫。若年月本无，日时带财，别无劫败冲克，则主自家成立，中晚之年大发。若柱中财多身弱，少年又径休败之地，多事频并，百不如意，中年后忽临父母之地，或三合可以助我，则勃然而兴。若少年乘旺，老来脱局，不唯守穷途而惶惶，抑且是非蜂起。以财能利己，亦能招谤故也。若四柱相生，别带贵格，不值空亡，又行旺运，三合财星，皆是贵命，其福禄浅深，随格轻重言之。又曰：凡人命有两位财，身弱不妨，元用正财，身旺发财，元用偏财，身旺脱财。又云：偏正二财，喜忌大同，唯有喜官星、不喜官星小异。有正财不若有偏财，偏财重实，其福则厚。最怕劫败比肩，在年最重，在月稍次。一名孤辰，一名逐马，主克妻害子，破财贫薄，又防阴贼小人同类相伤。柱中元犯此忌，运行财旺之地，亦可发福，再行比劫，退败而身死者有之，遭官破败者有之。

- 分字分词释义：

  - **偏财**：我克之财中，非正配、非稳定份额的部分，如甲见戊、乙见己等，多象征外来机会、人情之财、非常规收入。
  - **非妻所带，乃众人之财**：偏财不以正妻、正当俸禄为主，而多与人际往来、场合机缘有关，故易来亦易散。
  - **好出不惧藏，唯怕分夺及落空亡**：偏财宜流通，不必刻意深藏，但最怕被兄弟比劫分夺、或落在空亡之地。
  - **偏财格主人慷慨，不甚吝财**：命局偏财重者，多表现为出手大方、重情好义，但也可能带有逢场作戏、手腕灵活的一面。
  - **财弱待旺乡而荣，财盛恐身势无力**：财星太弱需等行至旺地方显；财星太盛则担忧日主不胜其负，反生祸患。

- **规范化释义（primary_lang_explained）**：

  偏财，是与人情、机会、风险更紧密相连的一类财。它既可以表现为横财、外来资源、商业机会，也可以体现为社交场合中“靠关系得利”的部分。原文提醒：

  - 一方面，得地之偏财可旺官、生机缘，甚至“富而且贵”；
  - 另一方面，偏财极怕兄弟比劫分夺、落空亡或与煞气相连，一旦失衡，则往往应在婚姻、子息、健康与信誉方面的损耗。

- 核心要点：

  - 偏财主**外缘之财、人情之财、机会之财**，宜流通、不宜滞塞。
  - 命局以偏财为用者，需身势不弱，有印比护身，否则易成“财来身退”。
  - 月令带偏财，影响多在少年与家族资源；年、日、时偏财，则分别偏向祖辈、本人努力与中晚年机缘。
  - 比劫分夺、财多生煞、落空亡等，皆是偏财的高风险配置。

- 详细解说：

  偏财与正财的差别，不仅在于“妻 / 妾”“固定收入 / 非固定收入”，更在于其背后对应的生活方式：

  - 偏财多与应酬、人情往来、商业投机、外来合作等连在一起，人也因之更具弹性与机缘；
  - 然而同样的机动性，也意味着更大的起伏：合伙不和、信誉受损、风险投资失败，都容易在偏财重者身上集中体现。

  在具体判断时，可以将偏财视为一种“社会流动性”的指标：

  - 偏财得地、官印相生时，多主能在流动中获利；
  - 偏财过多、比劫成群时，则易在纷争与人情债中耗损身心。

- **校勘与字词辨析（双语）**：

  - 文中“孤辰”“逐马”等名目，本稿在本节不展开专门星曜含义，只以“克妻害子、破财奔波”的象意略示，相关星曜另见他条。
  - 对“有正财不若有偏财，偏财重实，其福则厚”一句，本稿理解为：在同等结构下，偏财往往更贴近现实钱粮与流通机会，但前提仍是身强能任，并非简单鼓励追逐偏财。
  - **English**：
    - Not simply encouraging pursuit of indirect wealth; balanced interpretation provided.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_121]` `[trigger: 偏财定义]` `[factor_trigger: piancai_presence AND zhongren_zhicai]` `[role: 主干]` 偏财者，乃甲见戊、乙见己之例。非妻所带，乃众人之财也。 → 《三命通会》卷六#论偏财
  - `[ns_smth_06_122]` `[trigger: 恆慨不吝]` `[factor_trigger: piancai_ge AND kangkai_bulin]` `[role: 主干依赖]` 偏财格，主人恆慨，不甚吝财，与人有情而多诈。 → 《三命通会》卷六#论偏财
  - `[ns_smth_06_123]` `[trigger: 偏财好出]` `[factor_trigger: piancai_lu AND bu_ju_cang]` `[role: 条件分支]` 偏财好出，亦不惧藏，唯怕分夺及落空亡。 → 《三命通会》卷六#论偏财
  - `[ns_smth_06_124]` `[trigger: 偏财重实]` `[factor_trigger: piancai_zhong AND fuhou]` `[role: 总结]` 有正财不若有偏财，偏财重实，其福则厚。 → 《三命通会》卷六#论偏财"""
    normalized_text_zh: str = """"""
    subject: str = "偏财与人情之财"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_piancai_marker', 'bazi_semantic', 'bazi_structure_piancai', 'bazi_semantic', 'bazi_state_factor_23', 'bazi_semantic', 'bazi_state_factor_24', 'bazi_semantic', 'bazi_condition_factor_188', 'bazi_semantic', 'bazi_condition_factor_189', 'bazi_semantic', 'source_ref', 'rel_smth_06_118', 'piancai_ge_presence', 'rel_smth_06_119', 'shehui_liudongxing', 'rel_smth_06_120', 'bijie_fenduo_risk', 'evi_smth_06_118', 'piancai_ge_presence', 'rule_piancai', 'evi_smth_06_119', 'shehui_liudongxing', 'rule_liudong', 'evi_smth_06_120', 'bijie_fenduo_risk', 'rule_fenduo', 'map_smth_06_079', 'map_smth_06_080']
    
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
        l1_anchor="smth_v1.0.0_偏财与人情之财_001_L1",
    )
    version: str = "1.0.0"
