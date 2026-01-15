"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.636722
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
    semantic_id="zw_v1.0.0_疾厄宫诸星论_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 疾厄宫诸星论(SemanticEntry):
    """
    #### 原文（断句）：

疾厄宫诸星论。凡看疾厄，先看命宫星曜落陷、加煞如何；又看疾厄宫星曜庙旺、落陷，以定一生疾病轻重。星曜庙旺者，灾少；陷地加羊陀火铃空劫等煞，多主襁褓多灾、头面破相、血气之疾、...
    """
    
    original_text: str = """#### 原文（断句）：

疾厄宫诸星论。凡看疾厄，先看命宫星曜落陷、加煞如何；又看疾厄宫星曜庙旺、落陷，以定一生疾病轻重。星曜庙旺者，灾少；陷地加羊陀火铃空劫等煞，多主襁褓多灾、头面破相、血气之疾、下部之疾、痨伤疯疾，或手足残废。吉星会照，虽有疾而得救；凶星重重，无制无化，则主暗疾缠绵、终身病苦。

#### 分字分词释义：

- **疾厄宫**：十二宫之一，主健康状况、体质强弱、疾病类型与伤残风险。
- **襁褓多灾**：襁褓指婴儿期，形容命主自幼体弱、多病或多伤。
- **血气之疾**：血液循环、气机运行方面的疾病，可泛指心血管、血液、气虚气滞等问题。
- **下部之疾**：腰部以下的疾病，包括腰腿、足部、生殖泌尿等部位病症。
- **痨伤/痨症**：古代对消耗性、慢性消瘦类疾病的总称，如肺痨等，可泛指慢性虚损病。
- **疮癞**：皮肤疮疡、慢性皮肤病等。
- **疯疾**：古籍中对精神失常、癫狂之类疾病的统称，可类比现代严重精神疾病。
- **心气疾**：与心神、情志、气机相关的疾病，可涉及焦虑、抑郁、心悸等身心失调问题。
- **暗疾**：不易为外人察觉、久藏不愈或涉及隐私部位与心理层面的疾病。
- **伤残**：因病或外伤导致肢体功能永久性受损，如手足伤残、破相等。

#### 规范化释义（primary_lang_explained）：

疾厄宫专门论断命主的健康状态与疾病风险。判断时，首先要配合命宫一起看：命宫星曜若落陷又多煞，则整体体质偏弱，即使疾厄宫尚可，也要多加留意；若命宫稳健、疾厄宫星曜庙旺，则多主一生灾少病轻。其次，看疾厄宫本身星曜是庙旺还是陷地，并观察羊陀火铃空劫等煞星是否会聚：庙旺又得吉星拱照，多主小病小灾、遇险有救；落陷再逢诸煞，则主自幼多病、头面破相、血气不和、下部之疾，严重者甚至有疯疾与伤残之忧。

不同星曜入疾厄宫，还有各自偏应的病象：有的主皮肤浮肿、疮疡之类外在疾病；有的主血气、心气、内分泌类内在问题；有的主头目、四肢伤残；有的主少年时期多灾，长大后渐平；也有主暗疾隐忧、痨伤缠绵难愈者。若吉星会照，则即便有病也多能逢凶化吉；若煞星重重无制，则需警惕慢性病、复发性疾病与难以完全康复的状况。
 
#### 完整对等诠释（secondary_lang_full·5疾厄宫）：

The Health Palace concentrates the chart’s statements about physical and psychological vulnerability: where the body is strong, where it is more fragile, what kinds of illnesses are likely to recur, and how easily one recovers from setbacks. Interpretation always begins by pairing this house with the Life Palace. A robust Life Palace with a moderately afflicted Health Palace may describe someone who occasionally falls seriously ill or suffers accidents but generally bounces back. When both houses are weak and heavily besieged by malefics, the implication is a constitution that needs constant care, a life marked by frequent ailments or a higher probability of chronic or disabling conditions.

Each star emphasizes different organ systems or types of disease: some incline toward skin eruptions and surface inflammations, others toward blood and circulation issues, the lower body and reproductive organs, or the head, eyes and nervous system. Harsh stars and malefic clusters here are not a sentence but a warning label: they call for earlier check‑ups, more attention to lifestyle and stress, and taking small signals seriously before they accumulate into major problems. Benefic stars or noble helpers in the Health Palace act like protective factors—skilled doctors, timely diagnoses, access to good care, or simply a strong will to recover—so that even when illness appears, there is rescue and eventual healing. In a contemporary reading, this house is best used as a guide for preventative medicine and mind–body hygiene rather than fatalistic prediction: it suggests where to be gentler with oneself, which habits to build, and how to integrate emotional wellbeing into the care of the body.

#### 核心要点（整理）：

1. **诊断顺序**：先综合命宫与疾厄宫——命宫定体质根基，疾厄宫定显性病象，再参考三方四正有无吉凶星会照。
2. **疾病类型映射**：不同星曜对应不同疾病倾向（皮肤、血气、下部、头目、精神等），可粗分为外伤类、内科类、慢性虚损类与精神类。
3. **严重程度分级**：庙旺加吉主灾少且易愈；陷地加煞主灾多且反复；若煞重无制，则有暗疾、伤残、疯疾等严重情况。
4. **时间层次差异**：部分星曜主"襁褓多灾"或幼年多病，随年龄增长渐趋平稳；亦有中年以后才显的慢性疾病倾向。
5. **预防与调理**：通过疾厄宫可以了解身体弱点，提示命主在相应器官系统上多做检查与保养，从生活方式与情志调节入手，做到"未病先防"。

#### 详细解说：

1. **命宫与疾厄宫的联动**：
   命宫代表整体生命力与抗压性，疾厄宫代表具体病象与发病部位。命宫强而疾厄宫弱，往往表现为偶有重病但恢复力尚佳；命宫弱而疾厄宫也弱，则应格外重视整体体质与基础代谢问题。

2. **星曜与部位的对应关系**（概括）：
   - 紫微、天府等帝星守疾厄，多主灾少、遇险有救；
   - 巨门、天梁多主血气与下部疾，亦关乎消化与代谢；
   - 太阳、太阴主头目、眼目与视力，以及阴阳失调相关问题；
   - 武曲、七杀、破军等刚烈之星，多主外伤、疮癞、手足伤残；
   - 羊陀火铃空劫等煞星，则将原有病象推向更严重层级，如疯疾、残疾、久病不愈等。

3. **吉凶星的调和与放大作用**：
   吉星（如天魁、天钺、左右、昌曲）会照疾厄宫，往往主"临灾有救"——即便有病，也能得到及时救治或贵人相助，减少后遗症；凶煞重而无制，则疾病易反复、迁延不愈，甚至留下终身损伤。

4. **现代视角下的疾厄宫**：
   古人多从"痨伤、疯疾、疮癞"等角度叙述，现代可以延伸到慢性疾病（如心血管、代谢综合征）、身心疾病（焦虑抑郁、躯体化）、职业病（久坐、劳损）等。同时要强调：疾厄宫只能提供"倾向性"提示，不能替代医学诊断，不可据此延误就医。

5. **身心一体的理解**：
   "心气疾"、"疯疾"这些古词，提醒我们疾病不止是身体层面的损伤，也包括情绪与精神的失衡。疾厄宫煞重者，更要关注压力管理、情绪疏导与睡眠质量，而不仅仅是器官检查。

#### 校勘与字词辨析：

- **襁褓**：指婴儿期，原文"襁褓多灾"强调早年体弱多病。
- **痨伤/痨症**：泛指消耗性、虚损性慢性疾病，不局限于某一具体病名。
- **疯疾**：古代对精神类重大疾病的统称，现代可类比重度精神障碍或严重情绪失调。
- **心气疾**："心"不仅指心脏，也指心神与情志，"心气疾"兼有身心两层含义。
- **下部疾**：通常指腰部以下疾病，包括腰腿骨骼、下肢血管以及生殖泌尿系统问题。
- **浓血之厄**：可理解为血液粘稠度高或血行不畅一类问题，容易带来心血管风险。
- **伤残**：指肢体或感官功能长期或永久性受损，非一时小伤。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："天府太阴守疾厄，一生少病身康泰，纵有灾殃遇贵救，晚年安乐享天年。"此句常用于吉星守疾厄宫的平安格局描述。
- **反面叙事**："羊陀火铃冲疾厄，幼年多灾头面破，若非瘫痪便残疾，终身病苦难解脱。"此句警示煞星重临疾厄宫的严重健康风险。
- **现代转化**：某命主疾厄宫天同太阴同宫无煞，一生体质平和，少有大病。另一命主疾厄宫巨门陀罗同宫，幼年多灾，成年后患甲状腺疾病，经手术后康复。此例验证"巨门主口舌咽喉"的部位映射，也说明现代医学可以有效干预。"""
    normalized_text_zh: str = """"""
    subject: str = "疾厄宫诸星论"
    factor_refs: list = ['palace_health', 'pattern_qiangbaozai', 'type_xueqiji', 'type_anji', 'type_fengji', 'source_ref', 'rel_jie_001', 'star_ziwei', 'rel_jie_002', 'star_jumen', 'rel_jie_003', 'group_liusha', 'evi_jie_001', 'star_ziwei', 'rule_jie_ziwei', 'evi_jie_002', 'type_fengji', 'rule_jie_fengji', 'concept_health', 'concept_illness']
    
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
        l1_anchor="zw_v1.0.0_疾厄宫诸星论_001_L1",
    )
    version: str = "1.0.0"
