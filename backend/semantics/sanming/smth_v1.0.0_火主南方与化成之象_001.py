"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227462
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
    semantic_id="smth_v1.0.0_火主南方与化成之象_001",
    book_id="sanming",
    engine_id="bazi"
)
class 火主南方与化成之象(SemanticEntry):
    """
    - **原文（source_text）**：
  火主于南，应夏。火之为言化也，毁也，阳在上，阴在下；毁然盛而变化万物也。钻木取火，木所生也。然火无正体，体本木焉。出以应物，尽而复入，乃自然之气也。
...
    """
    
    original_text: str = """- **原文（source_text）**：
  火主于南，应夏。火之为言化也，毁也，阳在上，阴在下；毁然盛而变化万物也。钻木取火，木所生也。然火无正体，体本木焉。出以应物，尽而复入，乃自然之气也。

- 分字分词释义：
  - **化/毁**：化指变化、成熟，毁指焚毁、消尽，一正一反，皆火之用。
  - **火无正体**：无固定形质，多依附于燃料（木）而显现。

- **规范化释义（primary_lang_explained）**：
  火属南方，对应夏季。火的本义在于「化」和「毁」：一方面令万物成熟变化，一方面又能焚尽形体。钻木可以取火，说明火本从木中来，火自身没有固定的形体，随燃料之有无而出入，这是火的自然之气。

- **完整对等诠释（secondary_lang_full）**：

  Fire rules the South and corresponds to summer. Its nature is twofold: to transform and to consume. On the one hand it ripens and perfects things; on the other it can burn bodies to ash. That fire is drawn from wood by drilling shows that Fire is latent within Wood and depends on fuel to appear—by itself it has no fixed body. For destiny analysis, Fire stands for illumination, display, culture, enthusiasm and also expenditure and burnout. It must rest on the foundation of Wood and be supported by Earth; a lone Fire without roots tends toward empty flare‑ups, while Fire without Earth to contain it becomes a wandering blaze that harms rather than completes.

- **核心要点**：
  - 命局之火，多主明达、外显、文明、热烈，也有消耗、毁裂的一面；
  - 火离不开木之根基与土之承载，孤火无木易为虚焰，无土则易为漂焰。

- **详细解说**：
  本节阐述火的南方属性与化成机能。火主南方应夏，其义为「化/毁」——一方面令万物成熟变化，一方面又能焚尽形体。火本从木中来，自身无固定形体，随燃料之有无而出入。论命时，火旺而有木根、有土承，则为文明光明之火；孤立无根之火，则为虚火与躁动。在职业与事件分析中，火主「化成与呈现」，对应表达、传播、审美、技术落地、成果亮相等环节。

- **应用推演（操作顺序）**：
  1) 论命局之火时，先看所处节令与根基：春末夏初、有木有根之火，多为文明光明之火；孤立无根之火，多为虚火与躁动；
  2) 在职业与事件层面，火主「化成与呈现」，宜对应表达、传播、审美、技术落地、成果亮相等环节，可视作项目生命周期中的「发布/成品」阶段；
  3) 若火为用神但过弱，则需以木生火、以土承火；若火为忌神而过旺，则可借水、土调节，不宜一味抑火而伤及整体运行；
  4) 在系统设计中，将与曝光、输出、流量、展示等相关的指标，与火行象对应起来，使引擎能利用火的象意解释「为什么此阶段易见成果或败象」。

- **反例与边界**：
  - 见火旺即断为「有名有成」，忽视火旺无根、过于炎躁亦可能导致透支与烧毁；
  - 将所有与「热」相关的行业（如餐饮、能源）机械地归入火，而不区分其中金、水、土的成分，造成象意混乱；
  - 在工程实现中，用「点击量/曝光量」简单等同于火之吉凶，而不考虑内容质量与长期消耗，会扭曲火的象意；
  - 反过来，只看物理温度或现实行业，不利用火的「变化/成就」象意来抽象项目阶段，也浪费了本节提供的结构视角。

- **小例（示意）**：
  - 某命局木火通明、土略弱，适宜在有扎实基础团队中担任「表达与呈现」的角色：如讲师、演讲者、产品发布负责人等，而不宜独自承担全部基础建设；系统可据此在角色/岗位推荐中突出「前台呈现」的适配度；
  - 在项目运势分析中，把版本发布、品牌 Campaign、公开演出等节点映射为火象高峰期，并检查是否有足够「木/土」支撑，避免短期光亮、长期透支。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_045]` `[trigger: 火主南方]` `[factor_trigger: direction=south AND wuxing=fire]` `[role: 主干]` 火主于南，应夏。火之为言化也，毁也。 → 《三命通会》卷一#论五行生成
  - `[ns_smth_046]` `[trigger: 木生火]` `[factor_trigger: wuxing_shengke=wood_generates_fire]` `[role: 主干依赖]` 钻木取火，木所生也。然火无正体，体本木焉。 → 《三命通会》卷一#论五行生成
  - `[ns_smth_825]` `[trigger: 火亮平衡度]` `[factor_trigger: huoliang_pinghengdu]` `[role: 条件分支]` 火亮平衡度定强弱。 → 《三命通会》卷一
  - `[ns_smth_826]` `[trigger: 火炼金]` `[factor_trigger: huolianjin]` `[role: 条件分支]` 火炼金主成器。 → 《三命通会》卷一
  - `[ns_smth_827]` `[trigger: 火气配合适度]` `[factor_trigger: huoqi_peihe_shidu]` `[role: 条件分支]` 火气配合适度主调和。 → 《三命通会》卷一
  - `[ns_smth_828]` `[trigger: 火气炎腾]` `[factor_trigger: huoqi_yanteng]` `[role: 条件分支]` 火气炎腾主旺盛。 → 《三命通会》卷一
  - `[ns_smth_829]` `[trigger: 火轻火重]` `[factor_trigger: huoqing_huozhong]` `[role: 条件分支]` 火轻火重定强弱。 → 《三命通会》卷一
  - `[ns_smth_830]` `[trigger: 火湿得助]` `[factor_trigger: huoshi_dezhu]` `[role: 条件分支]` 火湿得助主调和。 → 《三命通会》卷一
  - `[ns_smth_831]` `[trigger: 火土财官运]` `[factor_trigger: huotu_cai_guan_yun]` `[role: 条件分支]` 火土财官运定时机。 → 《三命通会》卷一
  - `[ns_smth_832]` `[trigger: 火土过旺风险]` `[factor_trigger: huotu_guowang_risk]` `[role: 条件分支]` 火土过旺有风险。 → 《三命通会》卷一
  - `[ns_smth_833]` `[trigger: 火土配置]` `[factor_trigger: huotu_peizhi]` `[role: 条件分支]` 火土配置定格局。 → 《三命通会》卷一
  - `[ns_smth_834]` `[trigger: 火土调和]` `[factor_trigger: huotu_tiaohe]` `[role: 条件分支]` 火土调和主平衡。 → 《三命通会》卷一
  - `[ns_smth_835]` `[trigger: 火土行制风险]` `[factor_trigger: huotu_xingzhi_risk]` `[role: 条件分支]` 火土行制有风险。 → 《三命通会》卷一
  - `[ns_smth_836]` `[trigger: 火土转水]` `[factor_trigger: huotu_zhuanshui]` `[role: 条件分支]` 火土转水主变化。 → 《三命通会》卷一
  - `[ns_smth_837]` `[trigger: 火土甲杂有无]` `[factor_trigger: huotujiaza_presence]` `[role: 条件分支]` 火土甲杂有无定纯度。 → 《三命通会》卷一
  - `[ns_smth_838]` `[trigger: 火旺木焚]` `[factor_trigger: huowang_mufen]` `[role: 条件分支]` 火旺木焚主过亢。 → 《三命通会》卷一
  - `[ns_smth_839]` `[trigger: 火凶为忌]` `[factor_trigger: huoxiong_weiji]` `[role: 条件分支]` 火凶为忌主不利。 → 《三命通会》卷一
  - `[ns_smth_840]` `[trigger: 火制金身]` `[factor_trigger: huozhi_jinshen]` `[role: 条件分支]` 火制金身主克制。 → 《三命通会》卷一
  - `[ns_smth_841]` `[trigger: 皇极中央]` `[factor_trigger: imperial_ultimate_center]` `[role: 条件分支]` 皇极中央主核心。 → 《三命通会》卷一
  - `[ns_smth_842]` `[trigger: 当令]` `[factor_trigger: in_season]` `[role: 条件分支]` 当令主旺盛。 → 《三命通会》卷一
  - `[ns_smth_843]` `[trigger: 甲根强度]` `[factor_trigger: jia_root_strength]` `[role: 条件分支]` 甲根强度定有力。 → 《三命通会》卷一
  - `[ns_smth_844]` `[trigger: 甲木破库]` `[factor_trigger: jiamu_poku]` `[role: 条件分支]` 甲木破库主引发。 → 《三命通会》卷一
  - `[ns_smth_845]` `[trigger: 甲木日主]` `[factor_trigger: jiamu_rizhu]` `[role: 条件分支]` 甲木日主定类型。 → 《三命通会》卷一
  - `[ns_smth_846]` `[trigger: 建财官同气]` `[factor_trigger: jian_caiguan_tongqi]` `[role: 条件分支]` 建财官同气主有力。 → 《三命通会》卷一
  - `[ns_smth_847]` `[trigger: 建财]` `[factor_trigger: jiancai]` `[role: 条件分支]` 建财主有财。 → 《三命通会》卷一
  - `[ns_smth_848]` `[trigger: 建浮不贵]` `[factor_trigger: jianfu_bugui]` `[role: 条件分支]` 建浮不贵主虚名。 → 《三命通会》卷一
  - `[ns_smth_849]` `[trigger: 建格配置]` `[factor_trigger: jiange_config]` `[role: 条件分支]` 建格配置定格局。 → 《三命通会》卷一"""
    normalized_text_zh: str = """"""
    subject: str = "火主南方与化成之象"
    factor_refs: list = ['fire', 'transformation', 'destruction', 'formless_fire']
    
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
        l1_anchor="smth_v1.0.0_火主南方与化成之象_001_L1",
    )
    version: str = "1.0.0"
