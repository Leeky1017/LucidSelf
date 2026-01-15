"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227436
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
    semantic_id="smth_v1.0.0_阴阳合体与大衍之数_001",
    book_id="sanming",
    engine_id="bazi"
)
class 阴阳合体与大衍之数(SemanticEntry):
    """
    - **原文（source_text）**：
  若考其深义，则水生于一。天地未分，万物未成之初，莫不先见于水，故《灵枢经》曰：「太一者，水之尊号，先天地之母，后万物之源。」以今验之，草木子实未就，人...
    """
    
    original_text: str = """- **原文（source_text）**：
  若考其深义，则水生于一。天地未分，万物未成之初，莫不先见于水，故《灵枢经》曰：「太一者，水之尊号，先天地之母，后万物之源。」以今验之，草木子实未就，人虫胎卵、胎胚皆水也，岂不以为一？及其水之聚而形质化，莫不备阴阳之气在中而后成。故物之小而味苦者，火之兆也；物熟则甘，土之味也；甘极而后淡，淡，本也。然人禀父母阴阳生成之化，故先生二肾，左肾属水，右肾属火。火曰命门，则火之因水而后见，故火曰次二。盖草木子实，大小虽异，其中皆有两以相合者，与人肾同，亦阴阳之兆。是以万物非阴阳合体，则不能化生也。既阴阳合体，然后而春生而秋成，故次三曰木，次四曰金。盖水有所属，火有所藏，木有所发，金有所别，莫不皆因土而后成也。故金木水火皆待土而后成。兼其土数五以成之，则水六，火七，木八，金九；土常以五之生数不可至十者，土不待十以成，是生成之数皆五以合之。明大衍之数，由是以立，则万物岂能逃其数哉？

- 分字分词释义：
  - **水生于一**：从宇宙初始看，一切先见于水，故以「一」为水之本数；
  - **命门**：肾中真火之处，以水火相依说明阴阳合体而后能生；
  - **水六火七木八金九土五**：在一至五之上，再叠加「土数五」而成六、七、八、九诸生成之数，对应万物发展的阶段。

- **规范化释义（primary_lang_explained）**：
  本段从「万物皆先见于水」谈起，说明一切生命胚胎阶段皆属水；水聚而成形后，内中自具阴阳之气，于是有火、有土。人之二肾、一水一火，正是阴阳合体的象征。进一步看，万物非阴阳合体则不能化生，水、火、木、金都需有土来承载，故又在一至五之上叠以五数，成水六、火七、木八、金九，皆出于「土数五」之运算，这便牵连到《易》学所谓「大衍之数」。

- **完整对等诠释（secondary_lang_full）**：

  Starting from the observation that "all things first appear as Water", this paragraph notes that every embryo‑like stage of life belongs to the Water phase. Once Water gathers and takes shape, Yin and Yang are already present within it, and from their interaction Fire and Earth arise. The human body mirrors this in the two kidneys, one associated with Water, the other with Fire, as a symbol of Yin–Yang united in one vessel. In a broader sense, no being can be born without such a union; Water, Fire, Wood and Metal all require Earth to carry and stabilise them. Numerically this is expressed by adding the Earth number five to the base sequence one to five, yielding "Water‑six, Fire‑seven, Wood‑eight, Metal‑nine". These are not games with digits but a way of encoding different stages in the generative process that the Yijing calls the "Great Expansion" (dayan), from latent potential through growth to full manifestation.

- **核心要点**：
  - 生命之生成，本质是阴阳合体，一切五行之用皆离不开「水火土」三者的承转；
  - 数的推演（六、七、八、九）不是纯算术，而是用来表达「五行生成阶段」的工具，对应命局中不同发展层次。

- **详细解说**：
  本节深究五行数理之源：水为一，因天地未分时万物先见于水；水聚成形后阴阳二气具于其中，遂有火、土；人之二肾左水右火，火称命门，正是阴阳合体之证。万物非阴阳合体则不能化生，故木三金四皆在水火之后。又因金木水火皆待土而成，叠加土数五，便得水六、火七、木八、金九——此即大衍之数的生成逻辑。

- **应用推演（操作顺序）**：
  1) 在看命局发展阶段（童年、青年、中年、老年）时，可类比「水六、火七、木八、金九」等数序，将一生视为从胚胎（水）到成就（金）的连续生成过程，而非割裂为几个互不相干的阶段；
  2) 设计算法时，可为事件或状态打上「生成阶段标签」：如将创业早期标为「木八」、资产沉淀期标为「金九」，以辅助解释不同阶段的风险与机遇；
  3) 在健康与身心分析中，以「水火土」三者的承转判断体质偏向：例如水弱火亢而土不承的命局，易见虚火上炎与根基不足，对应调理策略须围绕「补水、护土、节火」；
  4) 将「大衍之数」作为高层约束：无论如何细分指标与评分，都不违背生命从潜伏到显化、从生成到收成的基本节律。

- **反例与边界**：
  - 把「水六火七木八金九」当作单纯的数字游戏，到处寻找号码、车牌、手机尾号的「吉数」，而完全不联系个人的实际气机与处境；
  - 试图用大衍数直接预测具体年份的好坏，而不结合个人命局与当时的岁运环境，将宏观象数误当成微观时间表；
  - 在工程实现中，若把生成阶段简单等同于年龄段，而不考虑个人经历与发展速度的差异，会导致「阶段标签」失真；
  - 反过来，若只按外在年龄划分阶段，完全不参考命局中水火土三者的动态平衡，也会错失本节提供的一个纵向结构视角。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_036]` `[trigger: 水生于一]` `[factor_trigger: generative_stage=water_phase]` `[role: 主干]` 若考其深义，则水生于一。天地未分，万物未成之初，莫不先见于水。 → 《三命通会》卷一#论五行生成
  - `[ns_smth_037]` `[trigger: 阴阳合体]` `[factor_trigger: yinyang_union=necessary]` `[role: 主干]` 万物非阴阳合体，则不能化生也。 → 《三命通会》卷一#论五行生成
  - `[ns_smth_038]` `[trigger: 大衍之数]` `[factor_trigger: dayan_numbers=generative]` `[role: 总结]` 明大衍之数，由是以立，则万物岂能逃其数哉？ → 《三命通会》卷一#论五行生成
  - `[ns_smth_750]` `[trigger: 甘露之病]` `[factor_trigger: ganluzhibing]` `[role: 条件分支]` 甘露之病主伤身。 → 《三命通会》卷一
  - `[ns_smth_751]` `[trigger: 干支脏腑映射]` `[factor_trigger: ganzhi_zangfu_yingshe]` `[role: 条件分支]` 干支脏腑映射定健康。 → 《三命通会》卷一
  - `[ns_smth_752]` `[trigger: 干支合生克]` `[factor_trigger: ganzhihe_shengke]` `[role: 条件分支]` 干支合生克定吉凶。 → 《三命通会》卷一
  - `[ns_smth_753]` `[trigger: 高飞折损]` `[factor_trigger: gaofei_zhesun]` `[role: 条件分支]` 高飞折损主破败。 → 《三命通会》卷一
  - `[ns_smth_754]` `[trigger: 高明]` `[factor_trigger: gaoming]` `[role: 条件分支]` 高明主智慧。 → 《三命通会》卷一
  - `[ns_smth_755]` `[trigger: 高僧遇师]` `[factor_trigger: gaoseng_yushi]` `[role: 条件分支]` 高僧遇师主缘分。 → 《三命通会》卷一
  - `[ns_smth_756]` `[trigger: 各得其所]` `[factor_trigger: gede_qisuo]` `[role: 条件分支]` 各得其所主和谐。 → 《三命通会》卷一
  - `[ns_smth_757]` `[trigger: 格局大损]` `[factor_trigger: geju_dasun]` `[role: 条件分支]` 格局大损主破败。 → 《三命通会》卷一
  - `[ns_smth_758]` `[trigger: 格局框架]` `[factor_trigger: geju_kuangjia]` `[role: 条件分支]` 格局框架定整体。 → 《三命通会》卷一
  - `[ns_smth_759]` `[trigger: 格局破返货]` `[factor_trigger: geju_po_fan_huo]` `[role: 条件分支]` 格局破返货主变化。 → 《三命通会》卷一
  - `[ns_smth_760]` `[trigger: 格局心机流年]` `[factor_trigger: geju_xinji_liuunian]` `[role: 条件分支]` 格局心机流年定应期。 → 《三命通会》卷一
  - `[ns_smth_761]` `[trigger: 庚辛运标志]` `[factor_trigger: geng_xin_yun_flag]` `[role: 条件分支]` 庚辛运标志定金运。 → 《三命通会》卷一
  - `[ns_smth_762]` `[trigger: 庚申冲寅]` `[factor_trigger: gengshen_chongyin]` `[role: 条件分支]` 庚申冲寅主动荡。 → 《三命通会》卷一
  - `[ns_smth_763]` `[trigger: 庚辛铭禄风险]` `[factor_trigger: gengxin_minglu_risk]` `[role: 条件分支]` 庚辛铭禄有风险。 → 《三命通会》卷一
  - `[ns_smth_764]` `[trigger: 根基深厚]` `[factor_trigger: genji_shenhou]` `[role: 条件分支]` 根基深厚主稳固。 → 《三命通会》卷一
  - `[ns_smth_765]` `[trigger: 根据深厚]` `[factor_trigger: genju_shenhou]` `[role: 条件分支]` 根据深厚主有力。 → 《三命通会》卷一
  - `[ns_smth_766]` `[trigger: 根苗花实]` `[factor_trigger: genmiao_huashi]` `[role: 条件分支]` 根苗花实定人生阶段。 → 《三命通会》卷一
  - `[ns_smth_767]` `[trigger: 根苗花实全称]` `[factor_trigger: genmiaohuashi]` `[role: 条件分支]` 根苗花实定年月日时。 → 《三命通会》卷一
  - `[ns_smth_768]` `[trigger: 根守稳固评分]` `[factor_trigger: genshou_wengu_score]` `[role: 条件分支]` 根守稳固评分定基础。 → 《三命通会》卷一
  - `[ns_smth_769]` `[trigger: 根芽根基评分]` `[factor_trigger: genya_genji_score]` `[role: 条件分支]` 根芽根基评分定强度。 → 《三命通会》卷一
  - `[ns_smth_770]` `[trigger: 公禄公贵类型]` `[factor_trigger: gonglu_gonggui_leixing]` `[role: 条件分支]` 公禄公贵类型定贵气。 → 《三命通会》卷一
  - `[ns_smth_771]` `[trigger: 钩陈得位有无]` `[factor_trigger: gouchendewei_presence]` `[role: 条件分支]` 钩陈得位有无定格局。 → 《三命通会》卷一
  - `[ns_smth_772]` `[trigger: 官财不救]` `[factor_trigger: guancai_bujiu]` `[role: 条件分支]` 官财不救主无助。 → 《三命通会》卷一
  - `[ns_smth_773]` `[trigger: 官多无官]` `[factor_trigger: guanduo_wuguan]` `[role: 条件分支]` 官多无官主混杂。 → 《三命通会》卷一
  - `[ns_smth_774]` `[trigger: 官煞财印]` `[factor_trigger: guansha_caiyin]` `[role: 条件分支]` 官煞财印定格局。 → 《三命通会》卷一"""
    normalized_text_zh: str = """"""
    subject: str = "阴阳合体与大衍之数"
    factor_refs: list = ['yinyang_union', 'dayan_numbers', 'generative_numbers', 'mingmen_fire', 'generative_stage']
    
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
        l1_anchor="smth_v1.0.0_阴阳合体与大衍之数_001_L1",
    )
    version: str = "1.0.0"
