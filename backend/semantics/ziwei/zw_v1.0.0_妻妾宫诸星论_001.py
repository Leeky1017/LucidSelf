"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.636673
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
    semantic_id="zw_v1.0.0_妻妾宫诸星论_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 妻妾宫诸星论(SemanticEntry):
    """
    #### 原文（断句）：

妻妾宫诸星论。紫微晚聘谐老，性刚。天府同谐老，天相同宜年少，破军同克二，加羊陀火铃亦刑，贪狼同有吉星免刑。天机宜年少，岳强之妻可配，夫宜长。加羊陀火铃主生离，晚娶吉。天梁同...
    """
    
    original_text: str = """#### 原文（断句）：

妻妾宫诸星论。紫微晚聘谐老，性刚。天府同谐老，天相同宜年少，破军同克二，加羊陀火铃亦刑，贪狼同有吉星免刑。天机宜年少，岳强之妻可配，夫宜长。加羊陀火铃主生离，晚娶吉。天梁同宜年长，太阴同内助美容。太阳庙迟娶吉，早娶克，因妻得贵。【以下各星详断从略】

#### 分字分词释义：

- **妻妾宫**：十二宫之一，专论婚姻状况、配偶特质、夫妻关系、婚配时机。古代有妻有妾，故名妻妾宫；现代多指配偶宫或夫妻宫。
- **晚聘谐老**：晚婚则夫妻和谐白头偕老，早婚反有刑克。
- **性刚**：配偶性格刚强、主见重、不易妥协。
- **岳强之妻**：岳家势力强盛、妻族背景显赫的妻子。
- **内助美容**：妻子容貌美丽且能持家内助，贤内助之意。
- **因妻得贵**：借助妻子的关系或资源获得贵人提携、地位提升。
- **克二/克三**：婚姻有刑克，可能二婚三婚或配偶早逝。
- **生离**：夫妻虽未丧偶但分居离异，生离死别之"生离"。
- **三度作新**：三次结婚，指婚姻重复刑克。
- **亲上成亲**：与亲族内部联姻，如表亲婚配。

#### 规范化释义（primary_lang_explained）：

妻妾宫专门论断命主的婚姻状况与配偶特质。各星曜入此宫，婚配时机、配偶年龄、夫妻和谐度皆不相同：紫微主晚婚和谐、配偶性格刚强；天机宜配年少之妻或岳家显赫的妻子；太阳庙旺宜迟娶，可因妻得贵；武曲主刑克宜迟娶，同年夫妇为佳；天同宜迟娶夫长妻少；廉贞主三度作新（三婚）；七杀、破军皆主早克，宜迟娶避刑。若加吉星（昌曲左右）则婚姻和美、配偶贤明；加煞星（羊陀火铃空劫）则主刑克生离、婚姻重复。流年斗君入妻宫，逢吉则配偶吉利，逢凶则有灾厄。
 
#### 完整对等诠释（secondary_lang_full·2妻妾宫）：

The Spouse Palace tells the story of how a person partners, what kind of spouse they tend to attract, and how smooth or complicated the marriage path will be. Different stars here map to different scripts: dignified imperial stars often point to respectable, capable partners who arrive later in life and bring stability once the native has ripened; agile, change‑oriented stars can describe charming yet restless partners, or relationships that begin early but are hard to sustain. Some configurations clearly favour marrying later, so that the sharpness of the chart’s harsh stars has time to soften; others can handle earlier unions, provided the match respects the underlying pattern of age, status and temperament suggested by the stars.

The text also stresses how age difference and family background of the spouse act as practical remedies. A native represented by quick, nervous or overly independent stars may need a more mature, steady spouse from a stronger clan to anchor them, whereas someone whose chart is already rigid and combative benefits from a gentler, younger partner who brings warmth instead of more steel. Harsh stars and heavy malefic clusters in this house warn of separation, divorce, widowhood or repeated marriages if one insists on marrying too early or ignoring the chart’s implied match pattern. When auspicious assistants and noble stars visit the Spouse Palace, they elevate the relationship into a genuine alliance: the spouse becomes a source of honour, resources and professional opportunity, and marital challenges are met with shared growth rather than fracture.

#### 核心要点：

1. **婚配时机原则**：庙旺星宜早娶（但部分帝星仍宜迟），陷弱星或孤克星必须晚娶，否则刑克严重。
2. **年龄搭配讲究**：某些星曜（如天机、天同）宜配年少之妻，某些（如巨门、天梁）宜配年长之妻，年龄差距能化解部分刑克。
3. **刑克等级判断**：煞星重者主生离死别甚至二婚三婚；吉星多者主夫妻和美白头偕老；中平星曜则视庙陷与加会吉凶而定。
4. **配偶特质映射**：星曜本身的属性直接反映配偶性格——紫微性刚、天机聪慧、太阴美容、武曲刚硬、廉贞多情、破军刚烈。
5. **流年斗君应验**：斗君入妻宫是该年婚姻运势的关键指标，逢吉主配偶有喜、关系改善，逢凶主争执灾厄、感情危机。

#### 详细解说：

妻妾宫是紫微斗数中最重要的六亲宫之一，关系命主一生婚姻幸福与否。古代命理特别强调"男命看妻财、女命看夫官"，妻宫的吉凶直接影响财运与事业，因此判断极为慎重。

**婚配时机的判断逻辑**：
1. **庙旺星**：星曜力量强盛时，理论上可以早婚，但仍需考虑星曜本身属性。例如紫微虽庙旺，但因帝星性刚，仍宜"晚聘谐老"。
2. **陷弱星**：星曜落陷时，早婚必克，必须"迟娶免刑"。例如武曲、七杀、破军这类孤克之星，若早婚则刑克极重。
3. **煞星加会**：无论主星庙陷，一旦羊陀火铃空劫加会，都主"生离"或"克二克三"，晚婚是唯一化解之道。

**年龄搭配的文化背景**：
古代婚姻讲究"郎才女貌、门当户对"，年龄差距也是重要考量。"夫长妻少"是传统主流，但某些星曜组合反而需要"妻大夫小"或"妻族显赫"来压制命主的孤克之气。例如天机主聪明善变，需要"岳强之妻"来稳定；巨门主是非口舌，需要"年长刚强之妻"来制衡。

**刑克的深层含义**：
"克"不仅指配偶早逝，更广泛的含义包括：
- 夫妻感情不和、经常争执
- 婚姻关系破裂、离婚分居
- 配偶身体不佳、长期疾病
- 婚姻对命主的事业财运产生负面影响

现代社会已废除妻妾制度，"妻妾宫"的含义可扩展为：
- 婚前看恋爱关系、择偶标准
- 婚后看夫妻相处、婚姻质量
- 婚变后看离异原因、再婚可能

**流年斗君的应用**：
斗君过度入妻宫，该年婚姻运势的判断需结合本命妻宫与流年妻宫的综合情况：
- 本命妻宫吉+流年吉→该年婚姻大吉，有结婚、添丁、夫妻共同发展的喜事
- 本命妻宫凶+流年吉→该年虽有改善但仍有隐忧，可能是"风平浪静但暗流涌动"
- 本命妻宫吉+流年凶→该年有突发矛盾但不至于破裂，需要谨慎处理
- 本命妻宫凶+流年凶→该年婚姻危机严重，可能离异、丧偶、重大争执

#### 校勘与字词辨析：

- 原文"谐老"意为"和谐到老、白头偕老"，非"皆老"之讹。
- "岳强"指岳家、妻族势力强盛，非"岳父"个人之强。
- "因妻得贵"的"贵"既指贵人扶持，也指社会地位提升，是综合性的吉象。
- "三度作新"的"度"是"次、回"之意，"作新"指"重新开始婚姻"，合起来就是"三次结婚"。
- 原文中"背克"应理解为"天生带有刑克之气"，非"背叛而克"。
- "同年夫妇也相当"中"相当"意为"合适、匹配"，年龄相近反而能化解武曲的刚克之气。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："太阳庙旺守妻宫，因妻得贵福无穷，晚娶贤妻能持家，夫荣妻贵百年同。"此句常用于太阳庙旺入妻妾宫的吉象描述，强调迟娶可免刑克、因妻得贵的正面效应。
- **反面叙事**："七杀破军临妻位，三度作新难偕老，若非生离便死别，晚婚方可免颠倒。"此句警示孤克之星守妻宫的刑克风险，提示早婚必克、晚婚可减轻。
- **现代转化**：某男士命主妻宫太阳化禄加会昌曲，28岁结婚，妻子为大学教授，婚后妻子人脉助其事业腾飞，夫妻恩爱至今。此例验证"因妻得贵、晚聘谐老"的论断。

**L2 叙事素材层（规范格式）**：

- `[ns_zwds_j4_009]` `[trigger: 妻妾宫论断]` `[factor_trigger: palace_fuqi]` `[role: 主干]` 妻妾宫主论婚配时机、配偶特质与婚姻和谐。 → 《卷四》妻妾宫
- `[ns_zwds_j4_010]` `[trigger: 因妻得贵]` `[factor_trigger: result_yinqidegui]` `[role: 结果]` 因妻得贵为因配偶而获得贵人扶持或地位提升。 → 《卷四》"因妻得贵福无穷"
- `[ns_zwds_j4_011]` `[trigger: 晚婚可免]` `[factor_trigger: timing_wanhunmianke]` `[role: 条件分支]` 晚婚可免为晚婚可减轻刑克的判断。 → 《卷四》"晚娶贤妻"
- `[ns_zwds_j4_012]` `[trigger: 三度作新]` `[factor_trigger: result_sanduzuoxin]` `[role: 结果]` 三度作新为三次结婚的婚姻模式。 → 《卷四》"三度作新难偕老"
- `[ns_zwds_j4_013]` `[trigger: 生离死别]` `[factor_trigger: result_shengliisbie]` `[role: 结果]` 生离死别为婚姻破裂或丧偶的凶险结果。 → 《卷四》"生离便死别"
- `[ns_zwds_j4_014]` `[trigger: 夫荣妻贵]` `[factor_trigger: result_furongqigui]` `[role: 结果]` 夫荣妻贵为夫妻双方都显贵的吉利结果。 → 《卷四》"夫荣妻贵百年同"
- `[ns_zwds_j4_015]` `[trigger: 配偶特质]` `[factor_trigger: peioute_tezhi]` `[role: 主干]` 配偶特质由妻妾宫星曜特性推断。 → 《卷四》妻妾宫
- `[ns_zwds_j4_016]` `[trigger: 婚姻刑克]` `[factor_trigger: hunyin_xingke]` `[role: 条件分支]` 婚姻刑克由煞星守妻宫判断。 → 《卷四》妻妾宫"""
    normalized_text_zh: str = """"""
    subject: str = "妻妾宫诸星论"
    factor_refs: list = ['palace_spouse', 'principle_wanpin', 'pattern_keersanke', 'effect_yinqidegui', 'pattern_sanduzuoxin', 'source_ref', 'rel_qiqie_001', 'state_miaowang', 'rel_qiqie_002', 'group_liusha', 'rel_qiqie_003', 'star_taiyang', 'evi_qiqie_001', 'star_ziwei', 'rule_qiqie_ziwei', 'evi_qiqie_002', 'group_liusha', 'rule_qiqie_sha', 'concept_marriage', 'concept_spouse_quality']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_妻妾宫诸星论_001_L1",
    )
    version: str = "1.0.0"
