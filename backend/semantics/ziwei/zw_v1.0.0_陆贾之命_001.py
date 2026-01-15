"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699409
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
    semantic_id="zw_v1.0.0_陆贾之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 陆贾之命(SemanticEntry):
    """
    - 分字分词释义：

  - **双禄朝垣**：两禄星同来朝拱命宫，主财禄叠加与资源丰厚。
  - **左右巨日拱照**：左辅右彼与巨门太阳同来拱照，主贵人扶持兼具谋略与口才。
  - **禄主缠于弱...
    """
    
    original_text: str = """- 分字分词释义：

  - **双禄朝垣**：两禄星同来朝拱命宫，主财禄叠加与资源丰厚。
  - **左右巨日拱照**：左辅右彼与巨门太阳同来拱照，主贵人扶持兼具谋略与口才。
  - **禄主缠于弱地**：禄星落入落陷或受制宫位，财禄虽来却不稳固、易失。
  - **火星劫空在命**：火星与地劫或空亡同守命宫，主突发灾厄与结构性损害。
  - **半天折翅**：比喻命局虽有飞腾之势，却因凶星而中途受挫。
  - **限岁俱到陷地**：大限与小限同时行至落陷之宫，激活本命凶曜。
  - **阳男土五局**：陆贾命盘的五行局数，土五局主厚重谋略。

- **原文（source_text）**：  
  陆贾之命。阳男土五局。双禄朝垣，左右巨日拱照，只嫌禄主缠于弱地，因此发，不主财无。且火星劫空在命，半天折翅之论，限岁俱到陷地，小限又且重并，故四十四岁难全命也。

- **规范化释义（primary_lang_explained）**：  
  陆贾命局属阳男土五局，命宫得双禄朝垣，又有左右辅弼与巨门、太阳拱照，本来具备「既富且贵」的潜能：既能得财禄，又能在朝中以谋略与口才侍从出入。然而原文指出「禄主缠于弱地」，说明禄星多落在力量不足或受制之宫位，财禄虽来，却带有不稳与易失的隐忧。再加上火星、地劫同守命宫，如同飞鸟折翼，只要大限、小限与流年轮番行至落陷之地，原有富贵格局便会被不断侵蚀。至四十四岁前后，大限与小限同临陷地并与火劫呼应，命主难以全身而退，成为「一度显发而福不耐久」的典型命例。

- **完整对等诠释（secondary_lang_full）**：  
  Lu Jia is described as a Yang Earth native of the Fifth Configuration. With two Lu stars converging on the Life palace and the Sun and Ju Men supported by Left and Right Assistants, his natal pattern promises both wealth and proximity to power. In contemporary language, this is someone who can accumulate resources and move in courtly or advisory circles through eloquence and strategy. Yet the text immediately qualifies these promises: the Salary stars are said to be "entangled in weak places," so their support is unstable and easily compromised. Fire Star and Earth Robber sit in the Life palace itself, like a bird flying with a damaged wing. As major, minor and annual periods successively move into fallen regions, the structure that once upheld his prosperity is gradually hollowed out. Around the age of forty‑four, when these periods converge in debility and resonate with the natal malefics, the native can no longer preserve his life, illustrating a pattern of success that cannot be kept.

- **核心要点**：  
  1. 双禄朝垣并得左右、巨日拱照，本具富贵兼收的上等潜力。  
  2. 禄星缠于弱地且命宫带火劫，使财禄与地位难以长久稳固。  
  3. 当限运多行陷地并激活本命凶曜时，原本光鲜的格局会在中年前后迅速折损。

- **叙事素材（narrative_snippets）**：
  - **双禄富贵**："双禄朝垣，左右巨日拱照"，陆贾命主原具既富且贵之势，有财有位。
  - **半天折翅**："柰嫌禄主缠于弱地……且火星劫空在命，半天折翅之论"，禄在弱地又遇火劫空亡，使盛名难久。
  - **限运入陷**："限岁俱到陷地，小限又且重并"，大限小限连番行陷地，激活本命火劫，成为四十四岁折寿的时间窗口。
  - **现代应用**：对靠资源与人脉起家的策士而言，当事业高峰叠加身体透支与高风险投资年份时，应主动收缩战线、保全根基，而非继续加码扩张。"""
    normalized_text_zh: str = """"""
    subject: str = "陆贾之命"
    factor_refs: list = ['pattern_shuanglu_chaoyuan', 'pattern_zuoyou_juri', 'defect_luzhu_ruodi', 'malefic_huoxing_jiekong', 'metaphor_bantian_zhechi', 'timing_xiannsui_xiandi']
    
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
        l1_anchor="zw_v1.0.0_陆贾之命_001_L1",
    )
    version: str = "1.0.0"
