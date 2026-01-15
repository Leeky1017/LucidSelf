"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.636691
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
    semantic_id="zw_v1.0.0_子女宫诸星论_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 子女宫诸星论(SemanticEntry):
    """
    #### 原文（断句）：

子女宫诸星论。凡看子女，先看本宫星宿主有几子；若加羊陀火铃空劫耗忌，主生子女有刑克。次看对宫有冲刑否。如本宫无星曜，专看对宫有何星宿主有几子。若善星贵星守子女宫，必主其人生...
    """
    
    original_text: str = """#### 原文（断句）：

子女宫诸星论。凡看子女，先看本宫星宿主有几子；若加羊陀火铃空劫耗忌，主生子女有刑克。次看对宫有冲刑否。如本宫无星曜，专看对宫有何星宿主有几子。若善星贵星守子女宫，必主其人生子昌盛贵题。若恶星又同刑杀守子女宫，不见刑克，主生强横破荡之子。又看三方四正，得南斗星多主多生男，北斗星多主多生女。若太阳落在阳宫主先生男，太阴落在阴宫主先生女。专看刑杀守本宫，无制化相生必然绝祀。

**口诀**：日生最怕太阴临，夜生最怕太阳照。此星若在儿女宫，教君到老无儿叫。

【以下各星详断从略】

#### 分字分词释义：

- **子女宫**：十二宫之一，专论子女数量、资质、孝顺、缘分厚薄及生育顺序。
- **刑克**：父母与子女之间的刑克关系，包括子女夭折、不孝、疏离、不肖等。
- **对宫**：与子女宫相对的宫位即田宅宫，需观察有无冲刑。
- **昌盛贵题**："昌盛"指子女众多且兴旺，"贵题"指子女有功名贵气、金榜题名。
- **强横破荡**：子女性格强横霸道、败家破产、不守祖业。
- **南斗星/北斗星**：紫微斗数将十四主星分为南北二斗。南斗星主阳性、主生男；北斗星主阴性、主生女。
- **阳宫/阴宫**：十二宫分阴阳，子寅辰午申戌为阳宫，丑卯巳未酉亥为阴宫。
- **绝祀**：断绝香火、无子嗣继承家业。
- **螟蛉之子**：养子、义子，非亲生子女。
- **庶出/偏室生**：庶子女，非正妻所生的子女（古代侧室、小妾所生）。
- **贵子**：有才华、有功名、能光宗耀祖的子女。
- **送终**：子女能为父母养老送终，尽孝道。

#### 规范化释义（primary_lang_explained）：

子女宫专门论断命主的子女状况。判断方法有五层：首先看子女宫本宫有何星曜，决定基础子女数量；若加煞星则有刑克。其次看对宫（田宅宫）有无冲刑。若本宫无星曜，则借对宫星曜判断。第三看星曜吉凶：吉星贵星守则子女昌盛贵显，凶星刑杀守则子女强横败家（即使数量不少）。第四看三方四正星曜的南北斗分布：南斗星多主多生男孩，北斗星多主多生女孩。第五看太阳太阴的宫位：太阳在阳宫主先生男，太阴在阴宫主先生女。特别注意：若刑杀重重守本宫而无制化，必然绝祀无后。

有一条重要口诀：日生人（白天出生）最怕太阴临子女宫，夜生人（晚上出生）最怕太阳照子女宫，这两种情况都主子女缘分薄弱甚至无子。

各星入子女宫的情况：紫微主三男二女；天机主二人或庶出多；太阳庙旺主三男二女且晚子贵；武曲主一子或侧室生；天同主五子；天府主五人；太阴主三女二男且先女后男。加吉星则增多且有贵子，加煞星则减少甚至绝祀。
 
#### 完整对等诠释（secondary_lang_full·3子女宫）：

The Children Palace focuses on how the chart handles lineage: how many children are likely, what mix of sons and daughters they may be, how capable or wayward they tend to be, and how deep or fragile the bond with them is. The classical method works in five layers. First, the star or stars sitting directly in the palace provide a base estimate for number and quality: imperial and treasury stars point to more offspring, often with at least one distinguished child; gentle benefics promise warmth and continuity; harsh, solitary stars compress the number down to one or even none. Second, the opposite house, tied to property and family estate, is checked for clashes or support, on the logic that a shaky household foundation makes it harder for descendants to thrive.

Third, if the Children Palace itself is empty, the chart "borrows" its description from the opposite house, following the broader rule that an empty house takes on the nature of its counterpart. Fourth, the distribution of the Southern and Northern Dipper stars across the triad of related houses is used as a symbolic measure of how the chart leans toward sons versus daughters. Finally, the Sun and Moon, together with whether the native was born by day or by night, refine the picture: harmonious pairings of day‑birth with the Sun or night‑birth with the Moon in this palace deepen connection and ease, while mismatched configurations signal thin offspring karma or a conscious choice not to have children. Strong afflictions here do not just imply "no heirs" in a literal sense; in modern terms they can also describe strained parent–child relationships, children who go their own way, or life paths where creative projects, students or adopted children become the main vehicles of legacy.

#### 核心要点：

1. **五层判断法**：本宫星曜（定基数）→对宫冲刑（看影响）→空宫借对（无星则借）→三方四正（定男女）→日生夜生（阴阳配合）。
2. **南北斗定性别**：南斗星多主生男（如紫微、天府、武曲、贪狼、七杀、破军），北斗星多主生女（如天机、太阳、天同、太阴、巨门、天相、天梁）。
3. **阴阳宫位配合**：太阳落阳宫主先生男，太阴落阴宫主先生女；反之则先生女或先生男。日生人忌太阴临子女宫，夜生人忌太阳照子女宫，否则子女稀少。
4. **贵子与不肖之分**：庙旺吉星主子女贵显成器，陷地煞星主子女不肖败家。"昌盛贵题"与"强横破荡"是两个极端。
5. **螟蛉与庶出现象**：某些星曜（如禄存、武曲、天机）特别主养子或庶出子女多，这在古代多妻制社会是重要判断。
6. **绝祀危机**：刑杀守本宫无制化，或羊陀火铃空劫全照，易绝嗣无后。现代应用时可理解为子女缘分极薄或选择不生育。

#### 详细解说：

子女宫是六亲宫中判断方法最复杂的一个，因为涉及数量、性别、顺序、资质、孝顺、缘分等多个维度。紫微斗数发展出一套系统的"子女判断五层法"：

**第一层：本宫星曜定基数**
不同主星入子女宫，子女基础数量不同。帝星（紫微、天府）主五人左右；福星（天同、太阴）也主四五人；孤克星（七杀、破军、武曲）主一人或孤单；智星（天机）主二人或庶出多。这个基数是在古代多子多福的社会背景下统计出来的经验值。

**第二层：对宫冲刑看影响**
子女宫的对宫是田宅宫，代表家业与祖产。若田宅宫有凶星或刑克，会影响子女宫，因为古人认为"家业不兴则子嗣难继"。

**第三层：空宫借对定性**
若子女宫无星曜（空宫），则借对宫（田宅宫）的星曜来判断。这是紫微斗数"借星安宫"的通用法则。

**第四层：南北斗定性别**
这是子女宫特有的判断法。紫微斗数将十四主星分为南北二斗，南斗主阳主动主男性，北斗主阴主静主女性。看子女宫及三方四正（财帛宫、疾厄宫）的南北斗星数量对比，多者为主。

**第五层：日夜生阴阳配**
这是最精细的判断。命主的出生时间（日生或夜生）与子女宫的太阳太阴位置，必须阴阳配合。日生人（阳）忌太阴（阴）临子女宫，夜生人（阴）忌太阳（阳）照子女宫，这叫"日月失配"，主子女缘薄。

**现代应用的调整**：
1. **数量判断淡化**：现代社会计划生育，子女数量更多取决于个人选择而非命理。但可以将"子女数量"理解为"子女缘分深浅"。
2. **性别偏好消除**：古代重男轻女，现代男女平等，南北斗的性别判断可以保留但不应作为价值判断。
3. **资质与缘分强化**：现代更看重子女的资质（是否成器）和亲子关系（是否孝顺）。这两方面的判断仍然有效。
4. **螟蛉与庶出现象**：古代"螟蛉"指养子，现代可扩展为继子女、领养子女、试管婴儿等非传统方式获得的子女。

#### 校勘与字词辨析：

- "贵题"一词，"题"通"题名"，指金榜题名、科举及第，引申为有功名贵气。
- "破荡"意为"败荡、破败"，形容子女败家或不守成。
- "螟蛉"典出《诗经》，原指寄生蜂将卵产在螟蛾幼虫体内，古人误以为是螟蛾收养了蜂子，遂用"螟蛉"指养子。
- "绝祀"的"祀"指祭祀、香火，"绝祀"即断绝香火传承，无子嗣。
- 原文"日生最怕太阴临，夜生最怕太阳照"是对仗工整的口诀，强调阴阳配合的重要性。
- "送终"指子女能为父母养老并料理后事，是古代孝道的重要体现。现代理解为亲子关系和睦、子女有能力赡养父母。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："天府太阴守子女，三男二女皆成器，贵子金榜高题名，晚年膝下多欢喜。"此句常用于吉星守子女宫的美好愿景，象征子女众多、有成就、孝顺和睦。
- **反面叙事**："日生太阴临子位，夜生太阳照儿宫，此星若在儿女宫，教君到老无儿送。"此句为原文中的重要口诀，警示日夜生与日月配合的关键性。
- **现代转化**：某女士命主子女宫天府庙旺加会昌曲左右，南斗星略多。实际生育两女一男，长女考入清华，次女留学剑桥，儿子从商有成。晚年三个子女轮流照顾，验证"子女昌盛贵显"的论断。

**L2 叙事素材层（规范格式）**：

- `[ns_zwds_j4_017]` `[trigger: 子女宫论断]` `[factor_trigger: palace_zinv]` `[role: 主干]` 子女宫主论子女数量、资质与亲子关系。 → 《卷四》子女宫
- `[ns_zwds_j4_018]` `[trigger: 子女昌盛]` `[factor_trigger: zinv_changsheng]` `[role: 结果]` 子女昌盛为子女众多有成就的吉利结果。 → 《卷四》"三男二女皆成器"
- `[ns_zwds_j4_019]` `[trigger: 贵子题名]` `[factor_trigger: result_guizi_timing]` `[role: 结果]` 贵子题名为子女金榜题名的贵显结果。 → 《卷四》"贵子金榜高题名"
- `[ns_zwds_j4_020]` `[trigger: 无儿送终]` `[factor_trigger: result_wuersongzhong]` `[role: 结果]` 无儿送终为晚年无子嗣养老的凶险结果。 → 《卷四》"教君到老无儿送"
- `[ns_zwds_j4_021]` `[trigger: 日月失配]` `[factor_trigger: riyue_shipei]` `[role: 条件分支]` 日月失配为日生太阴临或夜生太阳照的不利配置。 → 《卷四》"日生最怕太阴临"
- `[ns_zwds_j4_022]` `[trigger: 南北斗定性别]` `[factor_trigger: nanbeidou_xingbie]` `[role: 主干]` 南北斗定性别为根据南北斗星判断子女性别的方法。 → 《卷四》子女宫
- `[ns_zwds_j4_023]` `[trigger: 绝祀无嗣]` `[factor_trigger: result_juesi_wusi]` `[role: 结果]` 绝祀无嗣为断绝香火无子嗣的极凶结果。 → 《卷四》"绝祀"
- `[ns_zwds_j4_024]` `[trigger: 结果富贵]` `[factor_trigger: result_fugui]` `[role: 结果]` 结果富贵为命盘整体配置主富贵的判断。 → 《卷四》
- `[ns_zwds_j4_025]` `[trigger: 结果死亡]` `[factor_trigger: result_si]` `[role: 结果]` 结果死亡为命盘主死亡凶险的判断。 → 《卷四》
- `[ns_zwds_j4_026]` `[trigger: 结果凶亡]` `[factor_trigger: result_xiongwang]` `[role: 结果]` 结果凶亡为非正常死亡的凶险结果。 → 《卷四》"""
    normalized_text_zh: str = """"""
    subject: str = "子女宫诸星论"
    factor_refs: list = ['palace_children', 'system_nanbeidou', 'state_juesi', 'pattern_mingling', 'principle_rishengyesheng', 'source_ref', 'rel_zinv_001', 'star_zhuxing', 'rel_zinv_002', 'system_nanbeidou', 'rel_zinv_003', 'principle_rishengyesheng', 'evi_zinv_001', 'system_nanbeidou', 'rule_zinv_xingbie', 'evi_zinv_002', 'principle_rishengyesheng', 'rule_zinv_riyepei', 'concept_offspring', 'concept_lineage']
    
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
        l1_anchor="zw_v1.0.0_子女宫诸星论_001_L1",
    )
    version: str = "1.0.0"
