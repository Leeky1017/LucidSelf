"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559448
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
    semantic_id="yhzp_v1.0.0_1__五行元理消息赋_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 1五行元理消息赋(SemanticEntry):
    """
    - **原文（source_text）**：
  五行元理消息赋。
  详其往圣，鉴以前贤；论生死全凭鬼谷，推消息端的徐公。阳生阴死，阳死阴生，循环逆顺，变化见矣！
  夫，阳木生亥死午，虽存亡易见；...
    """
    
    original_text: str = """- **原文（source_text）**：
  五行元理消息赋。
  详其往圣，鉴以前贤；论生死全凭鬼谷，推消息端的徐公。阳生阴死，阳死阴生，循环逆顺，变化见矣！
  夫，阳木生亥死午，虽存亡易见；阴木跨马（午）逢猪（亥），则吉凶可知；艮（寅）生丙而遇鸡（酉）死；兑（酉）生丁而逢虎（寅）伤；戊藏寅而西方（酉）没；己生酉而艮（寅）中亡；庚逢蛇（巳）而峥嵘，运见鼠（子）亦难当；辛生子死在巽（巳）地；壬生申藏于震（卯）方；兔（卯）生癸水衣禄足，运行猴（申）地见灾殃。十干生死同断，造化依此推详。
  又，详权刃双显停均，位至侯王；中途或丧或危，运扶官旺。平生为富为贵，身杀两停。大贵者，用财而不用官。当权者，用杀而不用印。印赖杀生，官因财旺。食居先，杀居后，功名两全。酉破卯，卯破午，财名双美。享福，五行归禄；寿弥，八字相停。
  晦火无光于稼穑（戊己），阴木（乙）绝气于丙丁。火虚有焰，金实无声。水泛木浮者，活木；土重金埋者，阳金（庚）。水盛则危，火明则灭。阳金（庚）得炼太过，变格奔波；阴木（乙）归垣失令，终为身弱。土重而掩火无光，逢木反为有用。水盛则木无定，若行土运方荣。五行不可太甚，八字须得中和。土止水流，全福寿；土虚木盛，必伤残；运会元辰，须当夭折。
  木盛多仁，土薄寡信，水旺居垣须有智，金坚主义却能为。金水聪明而好色，水土混杂必多愚。遐龄得于中和，夭折丧于偏枯。辰戌克制并冲，必犯刑名；子卯相刑门户，全无礼德。弃印就财明偏正，弃财就杀论刚柔。

- **分字分词释义**：
  - **阳生阴死阳死阴生**：阳干阴干在不同地支的生死位置相反。
  - **循环逆顺变化见矣**：阴阳循环顺逆，变化由此可见。
  - **权刃双显停均位至侯王**：官杀与阳刃两停平衡，可至侯王之位。
  - **大贵者用财而不用官**：大贵之命多用财不用官。
  - **当权者用杀而不用印**：当权之命多用杀不用印。
  - **五行不可太甚八字须得中和**：五行太过不及皆凶，中和为贵。
  - **土止水流全福寿**：土止水流，主福寿全。
  - **木盛多仁土薄寡信**：木旺主仁厚，土弱主少信。
  - **金水聪明而好色**：金水旺主聪明但好色。
  - **遐龄得于中和夭折丧于偏枯**：长寿因中和，夭折因偏枯。

- **规范化释义（primary_lang_explained）**：
  本篇《五行元理消息赋》从"阳生阴死、阳死阴生"的循环出发，系统说明十天干在不同地支、不同旺衰状态下的**生死消息（旺衰进退）**规律，并由此推演贵贱祸福：
  - **消息总纲**：
    - 以徐子平、鬼谷子传统为源，强调五行有"生、旺、衰、休、囚、死"等阶段，阴阳互转、循环不息。
    - 阳木、阴木、庚金、辛金、壬水等，分别在特定地支中得生、得死、得藏、得灭，以此判断十干生死与运程荣枯。
  - **权刃财杀配置**：
    - 权星（官杀）与阳刃两停，身杀平衡则富贵可期。
    - 大贵之命多用财不用官，当权之命多用杀不用印；印赖杀生，官因财旺，食居先、杀居后则功名两全。
  - **五行太甚与中和**：
    - 水盛则危、火明则灭、土重掩火、金被土埋、木被水漂等，比喻五行**太过**导致的失衡后果。
    - 最终归结为"五行不可太甚，八字须得中和"，中和则福寿绵长，偏枯则夭折丧亡。
  - **性情与五行偏胜**：
    - 木盛多仁、土薄寡信、水旺多智、金坚主义，金水聪明好色、水土混杂多愚，说明五行偏胜与性格、智力、好恶之间的对应。
  - **刑名与礼德**：
    - 辰戌相冲克制易犯刑名；子卯相刑门户无礼；弃印就财、弃财就杀，则分别见偏正刚柔之性格。

- **完整对等诠释（secondary_lang_full）**：
  **Treatise on Five-Element Cycles and Messages**:
  - **Core Idea**: This ode describes how the Five Elements and Ten Heavenly Stems move through phases of birth, prosperity, decline, and death (sheng–wang–shuai–si). Yin and Yang alternate—"Yang lives where Yin dies, Yin lives where Yang dies"—forming a continuous cycle. Fate judgment rests on reading these cycles.
  - **Life–Death Positions of the Ten Stems**: Each Stem (Yang Wood, Yin Wood, Yang Metal, Yin Metal, Yang Water, etc.) has specific branches where it is born, hidden, or dies. By tracking where a Stem currently stands (birth, peak, decline, tomb), one can infer the rise and fall of status, fortune, and danger in luck cycles.
  - **Power, Blade, Wealth, and Killing**: When authority (Officer/Killing) and Yang Blade are balanced, great rank is possible. Great nobles often "use Wealth not Officer"; those in real power "use Killing not Seal". Seal depends on Killing to generate it; Officer thrives on Wealth. If Food God comes before Killing, both fame and achievement can be attained.
  - **Excess vs. Harmony**: Extreme configurations (over-abundant Water, blazing Fire, heavy Earth burying Metal, floating Wood, etc.) symbolize imbalance and lead to instability, illness, or hardship. True longevity and stable blessing come from **central harmony** of the Five Elements, not from extremity.
  - **Character and Morality**: Surplus Wood brings benevolence; thin Earth brings lack of trust; strong Water brings intelligence; firm Metal brings righteousness. Metal–Water makes one clever but lustful; Water–Earth mixed makes one dull. Legal trouble and loss of propriety are tied to certain clash patterns (Chen–Xu conflicts, Zi–Mao punishment).

- **核心要点**：
  - 建立十天干在不同地支中的**生死消息图**，以此判断运程荣枯。
  - 权、刃、财、杀、印、食等配置，以"身杀两停"和用财/用杀为大贵之要诀。
  - 五行太过或不及皆为祸，本质结论是"五行不可太甚，八字须得中和"。
  - 五行偏胜不仅影响祸福，也直接投射到性情与礼德。

- **详细解说**：  《五行元理消息赋》以"阳生阴死，阳死阴生，循环逆顺"开篇，系统阐述十天干在不同地支的生死消息。**十干生死**——阳木生亥死午，阴木跨午逢亥；丙生寅死酉，丁生酉伤寅；戊藏寅没酉，己生酉亡寅；庚逢巳峥嵘见子难当，辛生子死巳；壬生申藏卯，癸生卯殃申。**权刃财杀**——"权刃双显停均，位至侯王"，"身杀两停"主富贵；"大贵者用财不用官，当权者用杀不用印"揭示大贵取用之法。**五行太甚**——"水盛则危，火明则灭"，"土重掩火无光"，"金坚无火凶顽"等揭示五行太过之害；"五行不可太甚，八字须得中和"为核心结论。**性情礼德**——"木盛多仁，土薄寡信，金水聪明好色，水土混杂多愚"揭示五行与性情的对应；"辰戌克制并冲必犯刑名，子卯相刑门户全无礼德"揭示刑冲与礼德的关系。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_735]` `[trigger: 阳生阴死]` `[factor_trigger: yangsheng_yinsi AND xunhuan_nishun AND shigan_shengsi AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 主干]` 阳生阴死，阳死阴生，循环逆顺，变化见矣；十干生死总纲。 → 《渊海子平·五行元理消息赋》
  - `[ns_yhzp_736]` `[trigger: 十干生死]` `[factor_trigger: yangmu_shenghai_siwu AND geng_fengsi AND shigan_shengsi_weizhi]` `[role: 主干依赖]` 阳木生亥死午；庚逢蛇而峥嵘运见鼠亦难当；十干生死位置。 → 《渊海子平·五行元理消息赋》
  - `[ns_yhzp_737]` `[trigger: 权刃两停]` `[factor_trigger: quanren_shuangxian_tingjun AND shensha_liangting AND fugui AND anchong_qugui AND angui AND houwang]` `[role: 条件分支]` 权刃双显停均位至侯王；身杀两停主富贵。 → 《渊海子平·五行元理消息赋》
  - `[ns_yhzp_738]` `[trigger: 大贵用财用杀]` `[factor_trigger: dagui_yongcai_buyongguan AND dangquan_yongsha_buyongyin AND anchong_qugui AND angui AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 大贵者用财而不用官；当权者用杀而不用印；大贵取用法。 → 《渊海子平·五行元理消息赋》
  - `[ns_yhzp_739]` `[trigger: 五行太甚]` `[factor_trigger: wuxing_bukr_taishen AND bazi_xude_zhonghe]` `[role: 例外处理]` 水盛则危火明则灭；五行不可太甚八字须得中和。 → 《渊海子平·五行元理消息赋》
  - `[ns_yhzp_740]` `[trigger: 五行性情]` `[factor_trigger: musheng_duoren AND tuba_guaxin AND jinshui_congming_haose AND mu_sheng_ren]` `[role: 条件分支]` 木盛多仁土薄寡信；金水聪明而好色；五行与性情对应。 → 《渊海子平·五行元理消息赋》
  - `[ns_yhzp_741]` `[trigger: 中和偏枯]` `[factor_trigger: xialing_yu_zhonghe AND yaozhe_yu_pianku AND fushou]` `[role: 条件分支]` 遐龄得于中和，夭折丧于偏枯；中和为寿偏枯为夭。 → 《渊海子平·五行元理消息赋》
  - `[ns_yhzp_742]` `[trigger: 五行元理消息赋纲领]` `[factor_trigger: wuxing_yuanli_xiaoxi_fu AND shigan_shengsi AND zhonghe_pianku]` `[role: 总结]` 五行元理消息赋以十干生死、权刃财杀、中和偏枯为核心，阐述五行消息之理。 → 《渊海子平·五行元理消息赋》"""
    normalized_text_zh: str = """"""
    subject: str = "1. 五行元理消息赋"
    factor_refs: list = ['waxing_waning_phases', 'yin', 'self_killing_balanced', 'excessive_elements', 'central_harmony_qi']
    
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
        book_id="yuanhaiziping",
        chapter="",
        l1_anchor="yhzp_v1.0.0_1__五行元理消息赋_001_L1",
    )
    version: str = "1.0.0"
