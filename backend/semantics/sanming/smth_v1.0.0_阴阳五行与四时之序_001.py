"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227367
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
    semantic_id="smth_v1.0.0_阴阳五行与四时之序_001",
    book_id="sanming",
    engine_id="bazi"
)
class 阴阳五行与四时之序(SemanticEntry):
    """
    - **原文（source_text）**：
  夫天地未立，道本天地。天地既立，则太极之理，散在万事，由是而五行生焉。五行一阴阳，五殊二实无余欠也；阴阳一太极，精粗本末，无彼此也。五行质具于地，而气...
    """
    
    original_text: str = """- **原文（source_text）**：
  夫天地未立，道本天地。天地既立，则太极之理，散在万事，由是而五行生焉。五行一阴阳，五殊二实无余欠也；阴阳一太极，精粗本末，无彼此也。五行质具于地，而气形于天。以质而语，其生之序，则水、火、木、金、土，而水木阳也，火金阴也。又统而言之，则气阳而质阴也；又错而言之，则动阳而静阴也。五行之变，至不可穷，然无适而非太极之本然也。柏齐何子曰：五行一阴阳，阴阳一太极。周子固谓阴太极不外乎阴阳，阳不外乎五行矣。自今论之。水，水也，火火也，金木水火，土之交变也。土，地也。天安在乎？有地而无天，谓造化全可乎？若以谓天，即太极，故朱子以上天之载释太极，天道流行释阴阳。观易曰：易有太极，是生两仪，两仪生四象，四象生八卦，八卦之中，有乾有坤，则天地皆太极之分体明矣。以天为太极之全体，而地为天之分体，岂不误甚也哉！其说似有理也。夫五行之生，各一其性，四时之行，亦有其序：春以生之，夏以长之，秋以肃之，冬以藏之。春而夏，夏而秋，秋而冬，冬而复春，而相循无穷。盖五行异质，四时异气，而皆不外乎阴阳；阴阳异位，动静异时，而皆不离乎太极。至于所以为太极者，又无声臭之可言，是性之本体然也。

- **分字分词释义**：
  - **五行一阴阳**：五行只是阴阳在形质上的五种表现方式 / 阴阳展开为五行 / 本质同一
  - **质具于地，气形于天**：质地偏向地 / 气机偏向天 / 天地构成可见世界
  - **水火木金土之序**：以质之先后言 / 非通常相生相克之序 / 生成序列
  - **四时之行**：春生、夏长、秋肃、冬藏 / 循环无穷 / 时间节律
  - **得时**：五行符合当下节气 / 旺相休囚死之判定依据 / 月令为准
  - **生长收藏**：四时的功能特征 / 生命周期的四个阶段 / 循环往复

- **规范化释义（primary_lang_explained）**：
  这一段把前文的太极、阴阳落到五行与四时：太极之理散在万事，由阴阳而为五行，由五行而布于四时。五行本是一阴阳之行，四时则是阴阳在时间上的节律：春夏秋冬循环往复，但从未走出太极—阴阳这一总纲。所以，讨论任何一柱、一局的五行强弱，最终都要放回到「它在整个阴阳节律中的位置」来理解。

- **完整对等诠释（secondary_lang_full）**：
  Here the focus shifts from Taiji and Yin-Yang down to the concrete levels of the Five Elements and the four seasons. The principle of Taiji diffuses into all affairs, appears first as Yin and Yang, then as the Five Elements, and finally as the seasonal cycle. The Five Elements are simply Yin-Yang viewed as substantive qualities, while the seasons are Yin-Yang as temporal rhythm: spring, summer, autumn and winter rotate without ever stepping outside the Taiji-Yin-Yang framework. When we judge the strength or weakness of any element in a natal pillar, we must therefore place it within this seasonal rhythm instead of counting elements in isolation.

- **核心要点**：
  - 五行是阴阳的形质展开，四时是阴阳的时间节律
  - 五行之用必须放在四时流行之中考察，不可抽象孤立
  - 命局中任何一行的旺衰，都只是阴阳整体节律在那一点上的表现
  - 春生夏长秋肃冬藏是判断五行强弱的时间背景

- 应用推演（操作顺序）：
  1) 立局时先定「季节—四时」的主旋律：判断命造所处之月令、节气，是偏春生、夏长、秋肃、冬藏中的哪一段；
  2) 在此基础上再看五行分布：某行若得时、得地，则为顺应四时之气；反之则多为逆势或孤立之象；
  3) 断用神时，把「顺四时」作为重要权重：同样是用火，夏月与冬月的意义和剂量完全不同；
  4) 推岁运时，先看运与原局四时节律的配合：是锦上添花、雪中送炭，还是反向冲击，使原局节律失衡；
  5) 在实践层面，将这一节转化为一套「四时/节气权重」表，用于调整各类规则的优先级和强度。

- 反例与边界：
  - 只看「元素数量」：例如简单以「木多金少」之类定吉凶，而完全忽略当下节气是否本就需要木旺或金肃，这是脱离四时的静态五行观；
  - 把「春生夏长秋肃冬藏」机械套用到每一个命造，而不看具体纬度、时代与生活方式（如现代城市与古代农耕的差异），会让四时的判定过于僵硬；
  - 反过来，只谈心理、性格，不肯承认五行与四时在身体与环境层面确有节律制约，也会丢失本段所强调的「气机—时序」维度；
  - 在工程实现中，如果仅以公历月份粗暴映射四时，而不考虑节气边界，就容易在临界日产生大量反例，应在数据层面精确到节气乃至更细的时间分辨率。

- 小例（示意）：
  - 某命局火土偏弱而金水偏盛，生于春夏之间，又居于阳光充足之地，从事教育与内容创作，此即「所禀之性」与「所处之气」同调，人物生成倾向于外放生长；若迁居寒地、久处封闭空间，其气机可能一度郁结，此时调运与修为方向宜偏向「舒展」而非再压抑；
  - 在命理知识库中，将不同地域/时代的典型人物样本按「气类 + 职类」聚类，能更好地体现「同一阴阳五行之气，在不同条件下凝聚为迥异人物」这一节所讲的思想。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_014]` `[trigger: 五行阴阳统一]` `[factor_trigger: five_elements=yinyang_manifestation]` `[role: 主干]` 五行一阴阳，阴阳一太极。 → 《三命通会》卷一#五行四时条
  - `[ns_smth_015]` `[trigger: 四时节律]` `[factor_trigger: four_seasons=cycle_rhythm]` `[role: 主干依赖]` 春以生之，夏以长之，秋以肃之，冬以藏之。 → 《三命通会》卷一#五行四时条
  - `[ns_smth_016]` `[trigger: 五行质气分布]` `[factor_trigger: five_elements_distribution=heaven_earth]` `[role: 主干依赖]` 五行质具于地，而气形于天。 → 《三命通会》卷一#五行四时条
  - `[ns_smth_017]` `[trigger: 四时循环]` `[factor_trigger: seasonal_cycle=endless]` `[role: 例外处理]` 冬而复春，而相循无穷。 → 《三命通会》卷一#五行四时条
  - `[ns_smth_575]` `[trigger: 从格成立]` `[factor_trigger: congge_chengli]` `[role: 条件分支]` 从格成立主大富贵。 → 《三命通会》卷一
  - `[ns_smth_576]` `[trigger: 从格类型]` `[factor_trigger: congge_leixing]` `[role: 条件分支]` 从格类型定高低。 → 《三命通会》卷一
  - `[ns_smth_577]` `[trigger: 从格强度]` `[factor_trigger: congge_qiangdu]` `[role: 条件分支]` 从格强度高主大贵。 → 《三命通会》卷一
  - `[ns_smth_578]` `[trigger: 从杀格]` `[factor_trigger: congshage]` `[role: 条件分支]` 从杀格主武贵。 → 《三命通会》卷一
  - `[ns_smth_579]` `[trigger: 从势格成立]` `[factor_trigger: congshige_chengli]` `[role: 条件分支]` 从势格成立主贵显。 → 《三命通会》卷一
  - `[ns_smth_580]` `[trigger: 从旺格成立]` `[factor_trigger: congwangge_chengli]` `[role: 条件分支]` 从旺格成立主专一。 → 《三命通会》卷一
  - `[ns_smth_581]` `[trigger: 从弱格成立]` `[factor_trigger: congruoge_chengli]` `[role: 条件分支]` 从弱格成立主依附。 → 《三命通会》卷一
  - `[ns_smth_582]` `[trigger: 从财格成立]` `[factor_trigger: congcaige_chengli]` `[role: 条件分支]` 从财格成立主大富。 → 《三命通会》卷一
  - `[ns_smth_583]` `[trigger: 从儿格成立]` `[factor_trigger: congerge_chengli]` `[role: 条件分支]` 从儿格成立主学艺。 → 《三命通会》卷一
  - `[ns_smth_584]` `[trigger: 从官格成立]` `[factor_trigger: congguange_chengli]` `[role: 条件分支]` 从官格成立主仕途。 → 《三命通会》卷一
  - `[ns_smth_585]` `[trigger: 从印格成立]` `[factor_trigger: congyinge_chengli]` `[role: 条件分支]` 从印格成立主学问。 → 《三命通会》卷一
  - `[ns_smth_586]` `[trigger: 当令得时]` `[factor_trigger: dangling_deshi]` `[role: 条件分支]` 当令得时主旺相。 → 《三命通会》卷一
  - `[ns_smth_587]` `[trigger: 得地通根]` `[factor_trigger: dedi_tonggen]` `[role: 条件分支]` 得地通根主有力。 → 《三命通会》卷一
  - `[ns_smth_588]` `[trigger: 得禄归位]` `[factor_trigger: delu_guiwei]` `[role: 条件分支]` 得禄归位主食禄。 → 《三命通会》卷一
  - `[ns_smth_589]` `[trigger: 得气得位]` `[factor_trigger: deqi_dewei]` `[role: 条件分支]` 得气得位主旺强。 → 《三命通会》卷一
  - `[ns_smth_590]` `[trigger: 得生得助]` `[factor_trigger: desheng_dezhu]` `[role: 条件分支]` 得生得助主有情。 → 《三命通会》卷一
  - `[ns_smth_591]` `[trigger: 得时得势]` `[factor_trigger: deshi_deshi]` `[role: 条件分支]` 得时得势主发达。 → 《三命通会》卷一
  - `[ns_smth_592]` `[trigger: 得用得力]` `[factor_trigger: deyong_deli]` `[role: 条件分支]` 得用得力主成就。 → 《三命通会》卷一
  - `[ns_smth_593]` `[trigger: 地支藏干]` `[factor_trigger: dizhi_canggan]` `[role: 主干]` 地支藏干为根气。 → 《三命通会》卷一
  - `[ns_smth_594]` `[trigger: 地支关系]` `[factor_trigger: dizhi_guanxi]` `[role: 主干]` 地支关系定刑冲合害。 → 《三命通会》卷一
  - `[ns_smth_595]` `[trigger: 地支力量]` `[factor_trigger: dizhi_liliang]` `[role: 条件分支]` 地支力量决定根基。 → 《三命通会》卷一
  - `[ns_smth_596]` `[trigger: 地支配合]` `[factor_trigger: dizhi_peihe]` `[role: 条件分支]` 地支配合定吉凶。 → 《三命通会》卷一
  - `[ns_smth_597]` `[trigger: 地支气]` `[factor_trigger: dizhi_qi]` `[role: 主干]` 地支气为本气余气。 → 《三命通会》卷一
  - `[ns_smth_598]` `[trigger: 地支五行]` `[factor_trigger: dizhi_wuxing]` `[role: 主干]` 地支五行定方位。 → 《三命通会》卷一
  - `[ns_smth_599]` `[trigger: 地支状态]` `[factor_trigger: dizhi_zhuangtai]` `[role: 条件分支]` 地支状态定旺衰。 → 《三命通会》卷一"""
    normalized_text_zh: str = """"""
    subject: str = "阴阳五行与四时之序"
    factor_refs: list = ['four_seasons', 'five_elements', 'birth_growth_harvest_storage', 'in_season']
    
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
        l1_anchor="smth_v1.0.0_阴阳五行与四时之序_001_L1",
    )
    version: str = "1.0.0"
