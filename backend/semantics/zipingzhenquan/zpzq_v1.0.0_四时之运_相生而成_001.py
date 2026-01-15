"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.523649
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
    semantic_id="zpzq_v1.0.0_四时之运_相生而成_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 四时之运相生而成(SemanticEntry):
    """
    - **原文（source_text）**：
  四时之运，相生而成，故木生火，火生土，土生金，金生水，水复生木，即相生之序，循环迭运，而时行不匮。然而有生又必有克，生而不克，则四时亦不成矣。克者，所...
    """
    
    original_text: str = """- **原文（source_text）**：
  四时之运，相生而成，故木生火，火生土，土生金，金生水，水复生木，即相生之序，循环迭运，而时行不匮。然而有生又必有克，生而不克，则四时亦不成矣。克者，所以节而止之，使之收敛，以为发泄之机，故曰"天地节而四时成"。即以木论，木盛于夏，杀于秋，杀者，使发泄于外者藏收内，是杀正所以为生，大易以收剑为性情之实，以兑为万物所说，至哉言乎！譬如人之养生，固以饮食为生，然使时时饮食，而不使稍饥以待将来，人寿其能久乎？是以四时之运，生与克同用，克与生同功。

- 原注（原文注解）：
  　　此段总论生克在四时运行中的互补调节关系，明确"生与克同用、克与生同功"的天地法则，为后文十神吉凶论提供哲学基础。

- 分字分词释义：
  - 四时之运：春夏秋冬的四季运行节律。
  - 相生而成：五行依相生链条（木→火→土→金→水→木）循环成就四时。
  - 循环迭运：生生不息地交替运行。
  - 时行不匮：时令流转永不竭尽。
  - 有生必有克：只有生的力量，没有克的节制，则四时也无法成立。
  - 节而止之：克的作用是调节与制止，使过盛者收敛。
  - 收敛以为发泄之机：通过收敛（克）储备能量，为下一轮发泄（生）做准备。
  - 天地节而四时成：《易经》语，天地有节制才能成就四时运行。
  - 木盛于夏，杀于秋：木在夏季繁茂，被秋金所杀。
  - 杀正所以为生：杀（克）的作用正是为了生，把外散的能量收敛于内。
  - 大易以收剑为性情之实：《周易》把收敛兑卦视为万物性情的真实呈现。
  - 兑为万物所说：兑卦（秋金）是万物欢悦之时（收获成就）。
  - 譬如人之养生：以人的养生做比喻。
  - 稍饥以待将来：适度饥饿等待下一餐，才能长久养生。

- **规范化释义（primary_lang_explained）**：
  四季的运转，是靠五行相生来成就的：木生火，火生土，土生金，金生水，水又生木，如此循环往复，时序不绝。然而有生就必有克，若只有生而无克，则四季也不能成立。克的作用是节制与收敛，让过于发散的能量归藏于内，为下一轮发泄做准备。故《周易》说"天地节而四时成"。以木为例：木旺于夏，被秋金所杀。这个"杀"正是使木外发的能量收归于内的手段，所以"杀正所以为生"。《周易》把收敛视为万物性情的真实呈现，把兑卦比作万物欢悦——因为秋收是成就而非毁灭。这就像人养生，固然要吃饭才能活，但若时时进食、不稍饥等待，反而短寿。因此四时运行中，生与克同功同用。

- **完整对等诠释（secondary_lang_full）**：
  The rotation of the Four Seasons is accomplished through the mutual generation of the Five Elements: Wood generates Fire, Fire generates Earth, Earth generates Metal, Metal generates Water, and Water regenerates Wood, cycling endlessly so that the seasons never cease. Yet where there is generation, there must also be control; without control, the Four Seasons themselves could not be established. Control's function is to restrain and gather in, allowing energy that has been dispersed to be stored internally, preparing for the next cycle of release. Thus the Book of Changes states, "When Heaven and Earth establish limits, the Four Seasons come into being." Take Wood as an example: Wood flourishes in summer and is "killed" (controlled) by autumn Metal. This "killing" is precisely what causes Wood's outward expansion to be collected inward—hence "killing is actually for the sake of generating." The Book of Changes regards this gathering-in as the authentic expression of all things' nature, and calls the Dui hexagram (autumn Metal) the "joy of all beings"—because autumn harvest is fulfillment, not destruction. It is like nourishing life: certainly one must eat to survive, but if one eats constantly without allowing some hunger to build, longevity will be impossible. Therefore, in the operation of the Four Seasons, generation and control work together with equal merit.

- 核心要点：
  - 取用神既要安排"生的渠道"，也要安排"克的闸门"。
  - 判断格局不能只看"有生无克"或"有克无生"，而要看"生克是否平衡、是否得时"。
  - 在"财生官、官生印、印生身、身生食、食生财"的顺行配置中，必须有"克"的调节点，否则流转太快反而失衡。


- **详细解说**：
  本段承接上文"一气→阴阳→四象→五行"的生成次第，进一步说明四时运转与五行生克的关系。春木、夏火、秋金、冬水按季节轮替，而土居中央调和承载。生克并非对立：生是延续气机，克是收敛节制，二者"同功于成岁"。木盛于夏是因火助其发散，而秋金之"杀"反能使木气收敛归根，保存生机。故"杀者，使发泄于外者藏收于内"——克的真正功能是让过度的外张回归内敛，以待来春再发。这一哲理贯穿全书：看命不能只讲生旺、回避克泄，而要看整体平衡。

- 应用推演：
  1) 判断局中是"生多克少"还是"克多生少"。
  2) 若生多克少，取克神为用（如木旺取金为用）。
  3) 若克多生少，取生神为用（如金多取火制金、或取水泄金）。
  4) 检查生克链条是否有"节而止之"的环节，确保不失控。

- 反例与边界：
  - 只讲"喜生忌克"、把克一概看成坏事，是最常见的机械错误。
  - 把"生克同功"理解成"生克无差别"，也是误读——生克各有角色，不能颠倒，只是说都不可或缺。

- 小例（示意）：
  - 木旺之局，如无金克制，则木气过散而无收敛，难成大器；有金克木，则木有节制，方能"有进有退"成栋梁。
  - 火炎之局，如无水克制，则火势失控而燥烈伤人；有水调候，则火有节制，方能"温而不烈"成文明。

- 校勘与字词辨析：
  - "大易以收剑为性情之实"：各本多作"收剑"，今本作"收敛"，义同。"性情之实"指真实的性情状态，非虚饰。
  - "兑为万物所说"："说"通"悦"，指欢悦。兑卦为秋金，万物收成之时，故为欢悦。


- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_130]` `[trigger: 用神定义]` `[factor_trigger: yongshen_definition AND yueling=jing AND bage=wei]` `[role: 主干]` 用神者，月令为经，八格为纬。 → 《子平真诠·论用神》#定义
  - `[ns_zpzy_131]` `[trigger: 月令取用]` `[factor_trigger: yueling_tigang AND yongshen_qushe_xiankan_yueling]` `[role: 主干]` 月令提纲，用神取舍必先看月令。 → 《子平真诠·论用神》#月令
  - `[ns_zpzy_132]` `[trigger: 八格归纳]` `[factor_trigger: bage_list=(zhengguan, cai, yin, shi, pianguan, shangguan, yangren, jianlu)]` `[role: 主干]` 正官财印食，偏官伤官阳刃建禄。 → 《子平真诠·论用神》#八格
  - `[ns_zpzy_133]` `[trigger: 用神为纲]` `[factor_trigger: bazi_yongshen AND zhuanqiu_yueling]` `[role: 主干]` 八字用神，专求月令。 → 《子平真诠》#论用神
  - `[ns_zpzy_134]` `[trigger: 月令司权]` `[factor_trigger: yueling_siquan AND tigang_zhi_fu]` `[role: 主干]` 月令司权，提纲之府。 → 《子平真诠》#论用神
  - `[ns_zpzy_135]` `[trigger: 用神取法]` `[factor_trigger: yongshen_qufa AND yi_yueling_wei_zhu]` `[role: 主干]` 用神取法，以月令为主。 → 《子平真诠》#论用神
  - `[ns_zpzy_136]` `[trigger: 三合成局]` `[factor_trigger: sanhe=(shen_zi_chen_shui, yin_wu_xu_huo)]` `[role: 主干]` 申子辰合水，寅午戌合火。 → 《子平真诠》#上卷
  - `[ns_zpzy_137]` `[trigger: 三会成方]` `[factor_trigger: sanhui=(hai_zi_chou_shui, yin_mao_chen_mu)]` `[role: 主干]` 亥子丑会水，寅卯辰会木。 → 《子平真诠》#上卷
  - `[ns_zpzy_138]` `[trigger: 三才定位]` `[factor_trigger: sancai=(tian, di, ren) AND ge_you_dingwei]` `[role: 主干]` 天地人三才，各有定位。 → 《子平真诠》#上卷
  - `[ns_zpzy_139]` `[trigger: 四柱配合]` `[factor_trigger: sizhu=(nian, yue, ri, shi) AND peihe]` `[role: 主干]` 年月日时，四柱配合。 → 《子平真诠》#上卷
  - `[ns_zpzy_140]` `[trigger: 干支同论]` `[factor_trigger: tiangan_dizhi AND tongcan_helun]` `[role: 主干]` 天干地支，同参合论。 → 《子平真诠》#上卷
  - `[ns_zpzy_141]` `[trigger: 无病无药]` `[factor_trigger: wubing=true AND wuyao=true AND result=pingchang_zhiren]` `[role: 主干]` 无病无药，平常之人。 → 《子平真诠》#上卷
  - `[ns_zpzy_142]` `[trigger: 刑冲无情]` `[factor_trigger: xingchong_wuqing=true AND result=poge_baiju]` `[role: 主干]` 刑冲无情，破格败局。 → 《子平真诠》#上卷"""
    normalized_text_zh: str = """"""
    subject: str = "四时之运，相生而成"
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
        book_id="zipingzhenquan",
        chapter="",
        l1_anchor="zpzq_v1.0.0_四时之运_相生而成_001_L1",
    )
    version: str = "1.0.0"
