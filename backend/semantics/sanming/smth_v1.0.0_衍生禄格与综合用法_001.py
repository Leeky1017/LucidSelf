"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101323
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
    semantic_id="smth_v1.0.0_衍生禄格与综合用法_001",
    book_id="sanming",
    engine_id="bazi"
)
class 衍生禄格与综合用法(SemanticEntry):
    """
    - **原文（source_text）**：
  有生成禄，甲乙人得甲寅、乙卯之类。有名位禄，甲人见丙寅之类。有真禄，甲人见丙或己，乙人见己或午之类，皆为贵格。有进退真禄：戊辰见丁巳、戊午见丁巳，丙辰...
    """
    
    original_text: str = """- **原文（source_text）**：
  有生成禄，甲乙人得甲寅、乙卯之类。有名位禄，甲人见丙寅之类。有真禄，甲人见丙或己，乙人见己或午之类，皆为贵格。有进退真禄：戊辰见丁巳、戊午见丁巳，丙辰见癸巳、丙午见癸巳，癸亥见甲子、癸丑见甲子，壬戌见癸亥、壬子见癸亥；进则平易，退则艰难，更带福神，可作贵命，怕重见。有禄值会合，甲禄寅而得庚戌之类。有食神带禄：壬食甲而得甲寅，癸食乙而得乙卯，戊食庚而得庚申，己食辛而得辛酉，主吉。有食神合禄：甲食丙得丙申、丙寅，乙食丁得丁未、丁卯，庚食壬得壬辰、壬子，辛食癸得癸巳、癸丑八位，俱主吉。有禄头财，为缛煞：甲人见戊寅，乙人见己卯之类，主人富有声望。有禄头鬼，为赤口煞：甲人见庚寅，乙人见辛卯之类，主口舌刑责。

- **分字分词释义**：
  - **生成禄 / 名位禄 / 真禄**：分别强调「生养之禄」「官位之禄」「纯正无杂之禄」。
  - **进退真禄**：有进亦有退，进时顺利，退时艰难，带福神则可贵。
  - **禄值会合**：禄位与他支会合成局，加强某一类象。
  - **食神带禄 / 食神合禄**：食神与禄位同时出现，主才华与福禄俱备。
  - **禄头财 / 禄头鬼**：禄上见财为缛煞，多富多名；禄上见鬼为赤口，多口舌刑责。

- **规范化释义（primary_lang_explained）**：
  末段列出多种特殊禄格：
  - 生成禄、名位禄、真禄，分别对应不同侧重的贵格形态；
  - 进退真禄说明同一配置在不同运程方位上进退之别，进则平易，退则艰难，如不重见且带福神，可作贵命；
  - 禄值会合、食神带禄、食神合禄，则强调禄与食神、会局结合时，才华与禄位相互加持；
  - 禄头财为缛煞，象征富有声望；禄头鬼为赤口煞，多主口舌是非与刑责之患。

- **核心要点**：
  - 生成禄、名位禄、真禄共同刻画「禄与身份/职位」的不同组合形式，是对基础禄位的精细分层，用来描述资源基础、职位来源与纯度的差异。
  - 进退真禄强调「方位与时机」：同一结构在向前与向后不同运程中呈现明显难易差异，适合作为发展曲线中「进退转换点」的标记，而非静态贵格标签。
  - 食神带禄/合禄把「才华输出」与「禄位平台」连接起来，用于描述「以才成名、以禄承载」的格局，是才华与资源互相加乘的关键结构。
  - 禄头财与禄头鬼分别提示「声望与物质缀饰」与「口舌刑责」两种附加效应，属于禄上附加标签而非独立格局，应与原格局与用神同看。

- **详细解说**：
  1) 以本卷前 1–11 条「十干禄」为基础，为命局标注每一干的本禄支，以及是否形成「见禄」「坐禄」「寄禄」等基础禄结构；
  2) 在此基础上，识别是否出现生成禄、名位禄、真禄、进退真禄等组合，并为每种结构打上子标签（如 `shengcheng_lu`, `mingwei_lu`, `zhen_lu`, `jintui_zhen_lu`），用于后续规则调用；
  3) 进一步识别食神带禄、食神合禄、禄头财、禄头鬼等组合，将它们编码为针对「才华—资源—风险」的修饰特征，而不是用来单独决定贵贱高下；
  4) 在职业与发展路径建模中，将各类禄格主要用于调整「资源平台质量」「声望密度」与「口舌/纠纷风险」等中层指标，再与整体格局、用神与行运综合评估终局走向。

- 反例与边界：
  - 不宜见任一「贵格」名目（如真禄、进退真禄）便断为极贵，在现实中仍需格局清纯、用神得力、行运相扶，才能体现其上限；
  - 若整体局势混浊、凶煞过重，即便名义上有多种禄格并见，现实往往只是「在高压结构中勉力维持」，不可简单套用古代高官叙事；
  - 在现代社会，许多「禄头财」更常表现为高曝光、高消费与形象负担，而非纯粹财富享受，模型应以「资源与负担并存」来表达；
  - 对于无明显禄格而整体配置良好的命局，不宜因为「缺少名目」而矮化其发展潜力，禄格只是结构标签之一。

- 小例（示意）：
  - 某甲日命，命局既有甲禄寅，又见丙寅成名位禄兼食神带禄、禄头财结构，系统可解读为「以才学与专业输出叠加禄位平台」的格局，并提示其在公众形象与物质配置上兼具机会与压力；
  - 某壬日命，命局仅见食神合禄而无其它强禄格，整体格局中等偏清，系统则将其视为「才华可被禄位托举但上限有限」的结构，建议在稳健平台上长期深耕而非强求极端跃迁。"""
    normalized_text_zh: str = """"""
    subject: str = "衍生禄格与综合用法"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_43', 'bazi_semantic', 'bazi_structure_factor_44', 'bazi_semantic', 'bazi_structure_factor_45', 'bazi_semantic', 'bazi_relation_shishen_1', 'bazi_semantic', 'bazi_state_factor_104', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_衍生禄格与综合用法_001_L1",
    )
    version: str = "1.0.0"
