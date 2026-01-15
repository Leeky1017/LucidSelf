"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.725447
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
    semantic_id="zw_v1.0.0_斗数准绳总论_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 斗数准绳总论(SemanticEntry):
    """
    - 原文（source_text）：

  命居生旺，定富贵，各有其宜；身坐空亡，论荣枯，专求其要。紫微帝座在南极，不能施功；天府令星在南地，专能为福。天机七杀同宫，也善三分；太阴火铃同位，反成十恶。...
    """
    
    original_text: str = """- 原文（source_text）：

  命居生旺，定富贵，各有其宜；身坐空亡，论荣枯，专求其要。紫微帝座在南极，不能施功；天府令星在南地，专能为福。天机七杀同宫，也善三分；太阴火铃同位，反成十恶。贪狼为善宿，入庙不凶；巨门为恶曜，得垣尤美。诸凶在紧要之卿，最宜制伏；擎羊在身命之位，却受孤单。若见杀星倒限，最为至凶，福荫临之，庶几可解大厄。抵在人之机变，更加作意之推详：辨生克制化，以定穷通；看好恶正偏，以言祸福。官星居于福地，近贵营财；福星居于官宫，却成无成。身命得星为要，限度遇吉为荣。若言子媳有无，专在擎羊；耗杀逢之则害，妻妾亦然。相貌逢凶，必带破相；疾厄逢忌，定有病羸。须言定数以求玄，更在同年之相合。总为纲颂，用作准绳.

- 原注（原文注解，可无则省略小节）：

  本篇以“准绳”名之，旨在提出一套统摄全盘的断命原则，而非零散歌诀。大意在于：以身命宫之生旺与空亡定格局上限，以官福位置与凶星制化察日用祸福，以限运吉凶与机变人事观应期，合而为“富贵贫贱、荣枯得失”的总纲。

- 分字分词释义：

  - **命居生旺**：身命宫或主星落在生、旺、临官等强势之地，先天承载力足，较易发挥格局。
  - **身坐空亡**：身命宫或关键星曜落空亡，承接力不足，一生多奔波、落差与虚耗之感。
  - **杀星倒限**：大限、小限或流年运行到本命杀曜所主之宫位或对冲之地，凶性被集中激活的阶段。
  - **官星居于福地**：官禄、权位相关星曜落在得地、和顺之宫，多主因近贵或制度资源而得利。
  - **福星居于官宫**：本应主享福的星曜反落入官禄宫，象征福力被事务与责任消耗，难得身心安顿。
  - **子媳有无专在擎羊**：论子女、儿媳有无与顺逆，需特别观察擎羊在子女宫、夫妻宫等处的落点与制化情形。
  - **相貌逢凶 / 疾厄逢忌**：相貌宫多凶星多主破相或形象受损；疾厄宫见忌星多主久病、虚弱或隐疾。
  - **定数与同年相合**：除个体命局之外，还应参考同年生人整体命例，以校正过度绝对化或偏差的判断。

- 规范化释义（primary_lang_explained）：

  本篇说明：断一盘命局，必须有一套可反复验证的“准绳”。首先看身命宫是否居生旺之地：若身命生旺，便如立于坚实之地，虽不必尽贵，然多有发挥空间，富贵各有其宜；若身坐空亡，则如立于虚空，同样的机会与努力，往往难以完全承接，荣枯成败常有落差，需要特别寻找可用之处。

  其次，看主星与凶星在重要宫位上的组合：紫微、天府各有所宜之地；天机七杀同宫，在得地时尚有三分善果；太阴同火铃，则柔和之水被烈火所逼，转为“十恶”之象。贪狼本为善宿，入庙则可成妙用；巨门本为恶曜，然得垣则反显其用。诸凶若落在身命、官禄、财帛、夫妻、子女等紧要之宫，须有吉星制伏；擎羊在身命，往往孤克，需要仰赖福德与吉限缓解。断命时，应先辨生克制化，以定穷通，再看好恶正偏，以言祸福。

  又看官星与福星之位置：官星居于福地，多主因近贵营财而得利；福星居于官宫，则常见劳心劳力而难安享清福。关于子媳与妻妾之顺逆，则要特别观察擎羊与耗杀在子女宫、夫妻宫的组合。相貌宫逢凶，多主破相或形象受损；疾厄宫逢忌，多主病羸或慢性隐疾。最后强调：一切判断仍须放回“定数”与“同年相合”的整体视角之中，才不至于偏颇。

- 完整对等诠释（secondary_lang_full）：

  This chapter lays out a set of practical guidelines—"plumb lines"—for reading a Ziwei Doushu chart in a consistent and verifiable way. It begins with the state of the Life and Body palaces. When these cores stand in growing or prosperous phases, the chart is like a house built on solid ground: even if the overall pattern is only moderate, there is room to realise what is promised. When the Life or Body palace falls into a void or severely weakened place, the same opportunities and effort are harder to hold; gains and losses feel more erratic, and much attention has to be paid to where one's limited carrying capacity should be invested.

  The text then examines how principal stars and malefics combine in key houses. Ziwei and Tianfu each have positions where they can truly function; Tianji together with Qisha, when dignified, can still yield courage, adaptability and effective action, even if risk is present. By contrast, the Moon joined with fiery malefics like Huoxing or Lingxing often shows gentle, reflective qualities being driven into tense, anxious or extreme states. Tanlang, though often treated as a problematic pleasure star, becomes useful when in temple; Jumen, though labelled an "argument star", can become talent for speech, advocacy or research when properly placed. Malefics in the axis of Life, Career, Wealth, Marriage or Children must be checked for benefic control; Qingyang on the Life palace tends toward isolation and strain unless supported by Fortune and virtue stars.

  The guideline then turns to the placement of official and fortune stars. When career‑related stars stand in gentle, well‑supported houses, people often gain through proximity to power and institutional resources. When fortune stars are dragged into the Career palace, however, the energy that could have been used for ease and enjoyment is spent on responsibility and workload, producing lives that look successful from the outside but do not feel restful from within. For matters of offspring and marriage, the focus is on how Qingyang and depletion stars fall in the Children and Spouse houses. Heavy affliction here does not automatically mean "no children" or "certain divorce", but it does indicate areas where more conscious effort, communication and boundary‑setting will be required. Finally, configurations in the Appearance and Illness houses warn of vulnerability to injury, scarring or chronic weakness; in modern terms, these are prompts to strengthen safety habits and health management rather than fatalistic verdicts.

- 核心要点：

  - 以身命宫生旺或空亡，决定先天格局的“承载上限”。
  - 以限运吉凶与杀星倒限，决定结构能否、何时与如何兑现。
  - 以官星与福星位置（是否错位）解释“有成就但不安乐 / 有福气却难成就”的差异。
  - 以擎羊与耗杀在子女、夫妻等宫的组合，评估嗣续与婚姻的风险与压力点。
  - 以相貌宫与疾厄宫的凶忌情况，为外貌与健康风险提供明确指示。

- 详细解说：

  1. **身命生旺与空亡：结构上限与落差感**  
     “命居生旺，定富贵各有其宜”说明：身命宫在生旺之地，如同房屋地基扎实，再大的结构也有可能承载；即使整个命局只是中等配置，也较容易“把能有的东西拿到手”。而“身坐空亡”则如立于虚空，同样的格局与机会，往往难以完全落地，容易出现“看起来不差，却屡屡落空”的体验。本条并非简单判空亡为绝对凶，而是提醒：空亡意味着承接力不足，后天选择与外缘就显得更为关键。

  2. **主星与凶星的组合层级**  
     文中举出紫微、天府、天机七杀、太阴火铃、贪狼、巨门等典型组合，强调“星性要看位置与配合”。天机七杀同宫，若在得地宫垣，多主机变果断且敢作敢为，虽有风险，但仍可成事，故曰“善三分”；太阴与火铃同位，则柔和之水被烈火煎熬，容易转化为偏激、焦虑乃至暗病。贪狼入庙则多主多才多艺、社交活跃；巨门得垣则本为“是非之曜”却能化为口才、辩护或研究之长。

  3. **紧要宫中的制化思路与杀星倒限**  
     “诸凶在紧要之卿，最宜制伏；擎羊在身命之位，却受孤单”指出：身命、官禄、财帛、夫妻、子女等为人生主轴，凶星落于此处必须看是否有吉星制化。杀星倒限时，若限运与流年持续触发这些宫位，又缺乏足够吉曜缓冲，就容易在事业、财务、婚姻、子女或健康上出现阶段性重压甚至事故；若有福德与贵人星照临，则多为“大险而不死”或“经由打击而转机”的情形。

  4. **官福错位与主观幸福感**  
     “官星居于福地，近贵营财；福星居于官宫，却成无成”点出：官星与福星不只是吉星，还牵涉“成就”与“幸福感”的不同维度。官星在福地时，多主因接近权力与资源中心而获得机会；福星被推入官宫，则本应安享清福的能量被消耗在事务与责任上，常见“外人看来不错、本人却不轻松”的状态。此类命局并非一定不好，但适合在职业选择与生活节奏上主动留白，避免把全部精力押在事业指标上。

  5. **擎羊、耗杀与嗣续、婚姻结构**  
     “若言子媳有无，专在擎羊；耗杀逢之则害，妻妾亦然”说明：擎羊落在子女宫、夫妻宫并与耗杀相会，是嗣续与伴侣关系风险的重要信号。具体应验方式可以是迟子、少子、养子、子女负担重、婚姻多波折等；若有吉星制化且限运得宜，则多为“有折腾、有压力但仍能维系”的状况。本段强调的是“结构性风险提示”，而不是简单的“有无”判决。

  6. **相貌与疾厄宫：从象数到现代健康管理**  
     “相貌逢凶，必带破相；疾厄逢忌，定有病羸”在古代多被视为定断句。现代视角下，更适合作为安全与健康管理的预警：相貌宫凶重的人，可在运动、交通与危险环境中提高防护意识；疾厄宫忌重者，应更重视体检、作息与慢性病管理。本篇的精神是“见险则虑、未病先防”，而非宣判宿命。
    - 提供“本命结构 → 限运兑现”的判断流程，用以解释同一格局在不同人身上为何有不同结果。
    - 说明“格局上限”和“现实走势”之间的差异：某些命局基础好但运程坎坷，反之亦然。
    - 为工程侧提供权重框架：基础分（身命与官福结构）+ 时间修正分（限运与倒限）+ 关键宫位加减分（嗣续、婚姻、健康等）。
  - **必要条件**：
    - 需要完整的十二宫星位、庙旺空亡与吉凶分类，至少明确身命宫、官禄宫、福德宫、夫妻宫、子女宫、相貌宫与疾厄宫等关键宫位。
    - 必须具备大运或主要限运信息，方可应用“倒限”“遇吉为荣”等时间相关判断。
  - **增强条件**：
    - 结合大量命例，对“身命空亡而官福错位”“擎羊合耗杀在嗣续宫”“相貌宫凶重 + 疾厄逢忌”等结构进行统计验证。
    - 在推理系统中引入关键宫位权重与时间窗口参数，提升预测稳定性与可解释性。
  - **失效条件**：
    - 缺乏限运、生旺与空亡等信息，仅有星名与少量宫位时，本条准绳无法正确展开。
    - 若只凭「某星在某宫必富贵/必大祸」之类歌诀代替结构分析，则与本篇精神相违，本条视为失效。
  - **多层解释**：
    - 字面义：总结断命时应优先关注的结构与顺序：身命 → 官福 → 凶星制化 → 限运。
    - 象征义：把命局视为「材料强度（本命）+ 外力时间（运程）」的系统，而非单点标签。
    - 现实义：有助于构建「风险与机遇并存」的生涯、家庭与健康规划建议，而非单一吉凶宣判。
    - 心理义：提醒命主在接纳先天限制的同时，更重视关键时间点的选择与心态调整，避免把所有结果归咎于「命不好」。

- 叙事素材（narrative_snippets）：

  - **生旺富贵**："命居生旺，定富贵各有其宜"，身命宫生旺为格局承载力的基础保障。
  - **空亡荣枯**："身坐空亡，论荣枯专求其要"，空亡主承接力不足，需特别寻找可用之处。
  - **制化思路**："诸凶在紧要之卿，最宜制伏"，凶星需有吉星制化方能减轻凶性。
  - **官福错位**："官星居于福地，近贵营财；福星居于官宫，却成无成"，官福错位影响主观幸福感。
  - **倒限至凶**："若见杀星倒限，最为至凶"，限运与本命凶曜重叠为最危险时期。
  - **现代应用**：本条准绳可作为命理分析的判断流程框架，从结构到时间，层层递进。

  **L2 叙事素材层（规范格式）**：

  - `[ns_zwds_j1_105]` `[trigger: 生旺状态]` `[factor_trigger: state_shengwang]` `[role: 主干]` 生旺状态为身命宫处于强势阶段，承载力足，格局易发挥。 → 《斗数准绳》"命居生旺，定富贵"
  - `[ns_zwds_j1_106]` `[trigger: 倒限时机]` `[factor_trigger: time_daoxian]` `[role: 主干]` 倒限为限运与本命凶曜重叠的危险时期，凶性集中放大。 → 《斗数准绳》"杀星倒限，最为至凶"
  - `[ns_zwds_j1_107]` `[trigger: 二限时机]` `[factor_trigger: time_erxian]` `[role: 主干]` 二限为大限与小限重叠之年，吉凶加倍应验。 → 《斗数准绳》限运
  - `[ns_zwds_j1_108]` `[trigger: 流年太岁]` `[factor_trigger: system_liuniantaisui]` `[role: 主干]` 流年太岁为年运之主，冲照命宫主当年动荡变化。 → 《斗数准绳》限运
  - `[ns_zwds_j1_109]` `[trigger: 十二岁时机]` `[factor_trigger: system_shiershisuoji]` `[role: 主干]` 十二岁为小限完成一周的关键节点，主童年运势总结。 → 《斗数准绳》
  - `[ns_zwds_j1_110]` `[trigger: 太岁神煞]` `[factor_trigger: system_taishui12shensha]` `[role: 主干]` 太岁神煞为流年十二神煞，主年运细节吉凶。 → 《斗数准绳》
  - `[ns_zwds_j1_111]` `[trigger: 主星组合]` `[factor_trigger: star_combo]` `[role: 主干]` 主星组合为命盘核心星曜的相互配置，决定格局高低。 → 《斗数准绳》
  - `[ns_zwds_j1_112]` `[trigger: 主星位置]` `[factor_trigger: star_position]` `[role: 主干]` 主星位置为星曜所在宫位，决定星性发挥方向。 → 《斗数准绳》
  - `[ns_zwds_j1_113]` `[trigger: 主星数量]` `[factor_trigger: star_zhu]` `[role: 主干]` 主星数量为命宫主星的多寡，影响格局复杂度。 → 《斗数准绳》
  - `[ns_zwds_j1_114]` `[trigger: 主星入庙]` `[factor_trigger: star_zhuxing]` `[role: 主干]` 主星入庙为主星处于庙旺之地，力量纯正易发挥。 → 《斗数准绳》
  - `[ns_zwds_j1_115]` `[trigger: 吉星数量]` `[factor_trigger: star_ji_count]` `[role: 主干]` 吉星数量为命盘吉曜的多寡，影响福泽厚薄。 → 《斗数准绳》
  - `[ns_zwds_j1_116]` `[trigger: 凶星数量]` `[factor_trigger: star_xiong_count]` `[role: 主干]` 凶星数量为命盘凶曜的多寡，影响风险程度。 → 《斗数准绳》
  - `[ns_zwds_j1_117]` `[trigger: 煞星群组]` `[factor_trigger: star_sha]` `[role: 主干]` 煞星群组为擎羊、陀罗、火星、铃星等凶煞的统称。 → 《斗数准绳》
  - `[ns_zwds_j1_118]` `[trigger: 血气疾类型]` `[factor_trigger: type_xueqiji]` `[role: 条件分支]` 血气疾为疾厄宫见巨门等星主血气不调之疾。 → 《斗数准绳》
  - `[ns_zwds_j1_119]` `[trigger: 文武类型]` `[factor_trigger: type_wenwu]` `[role: 条件分支]` 文武类型为官禄宫星曜配置决定从文从武。 → 《斗数准绳》
  - `[ns_zwds_j1_120]` `[trigger: 因妻得贵]` `[factor_trigger: effect_yinqidegui]` `[role: 结果]` 因妻得贵为夫妻宫太阳庙旺主因配偶而提升事业。 → 《斗数准绳》"""
    normalized_text_zh: str = """"""
    subject: str = "斗数准绳总论"
    factor_refs: list = ['state_shengwang', 'state_kongwang', 'time_daoxian', 'star_guan', 'star_fu', 'star_qingyang']
    
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
        l1_anchor="zw_v1.0.0_斗数准绳总论_001_L1",
    )
    version: str = "1.0.0"
