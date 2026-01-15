"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699468
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
    semantic_id="zw_v1.0.0_取子陵命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 取子陵命(SemanticEntry):
    """
    - 分字分词释义：

  - **太阳居午**：太阳落在午宫得地，主光明外向、贵气彰显。
  - **无杀凑**：命宫未被诸杀星冲凑，吉象得以完整发挥。
  - **左右扶持福不轻**：左辅右彼同来扶...
    """
    
    original_text: str = """- 分字分词释义：

  - **太阳居午**：太阳落在午宫得地，主光明外向、贵气彰显。
  - **无杀凑**：命宫未被诸杀星冲凑，吉象得以完整发挥。
  - **左右扶持福不轻**：左辅右彼同来扶持，主福气深厚。
  - **文昌同科禄**：文昌与科星禄星同会，主才学与名利兼得。
  - **富贵双全寿至终**：富贵完整且寿命自然终结。
  - **大限天伤小限天使**：大限行至天伤、小限行至天使，标记终局阶段。
  - **阴男土五局**：子陵命盘的五行局数，土五局主厚重安稳。

- **原文（source_text）**：  
  取子陵命。阴男土五局。太阳居午，无杀凑，左右扶持福不轻，因有文昌同科禄，富贵双全，寿至终。七十三岁，大限天伤，小限天使不吉，损寿。

- **规范化释义（primary_lang_explained）**：  
  子陵命为阴男土五局，太阳居午且无诸杀星会凑，命宫得左右扶持，本身已具「光明正大、福厚安稳」之象。再加文昌同科禄，既有学问才情，又有实在俸禄与地位，故原文以「富贵双全，寿至终」总结，大意为此命一生衣食无忧、名利兼得，并无过早的折损之忧。  
  但原文仍细标出七十三岁的大运与小运结构：大限行至天伤之地，小限又在天使之宫，两者皆带有伤损与告终的意味。所谓「损寿」，并非骤然短折，而是指进入高龄后，命势渐趋衰弱，最终在这一阶段完成寿命终点。此命例可视作「富贵而得终寿」的对照范本：即便有天伤、天使之类的损寿配置，其作用是划出自然终点，而非中道崩折。

- **完整对等诠释（secondary_lang_full）**：  
  Zi Ling’s chart belongs to a Yin Earth native of the Fifth Configuration. The Sun sits in Wu without hostile stars crowding it, and the Life palace receives support from Left and Right Assistants. This already suggests a bright, upright character with substantial good fortune. When Wen Chang and the Academic star Ke join in, talent and learning are matched by rank and stipends, so the text sums it up as "wealth and honour in both hands, lifespan brought to its natural close." In other words, this is a life that is prosperous, respected and fundamentally secure.  
  The text nevertheless singles out the structure around age seventy‑three: the major period moves into the region of Tian Shang, while the minor period passes through Tian Shi. Both carry overtones of injury, closure and the drawing of a line under affairs. Here "shortening life" does not mean a dramatic truncation in midlife, but rather the natural waning of vitality in old age and the marking of a full‑span conclusion. As a case, it offers a counterpoint to many "cut‑short" examples, illustrating what it looks like when a well‑endowed life completes its course with both wealth and honour intact.

- **核心要点**：  
  1. 太阳居午无杀、左右扶持，加上文昌与科禄，构成富贵双全、性情光明的命局。  
  2. 原文「寿至终」强调此命虽有损寿配置，但整体属自然终寿而非中道夭折。  
  3. 七十三岁大限天伤、小限天使，标出人生的收束阶段，是「高龄完成寿命」的关键年份。

- **叙事素材（narrative_snippets）**：
  - **富贵双全**："太阳居午，无杀凑，左右扶持福不轻，因有文昌同科禄，富贵双全，寿至终"，子陵命主兼具名利与终寿。
  - **光明性情**：太阳居午且左右同来，多主性情光明磊落、待人以诚。
  - **晚景收束**："七十三岁，大限天伤，小限天使不吉，损寿"，天伤天使并见，标记人生自然收束的阶段，而非横祸折寿。
  - **现代应用**：此类命局适合作为「长期规划」范本——在中年前后稳步经营事业积累，晚年则提早安排退休与健康管理，让生命能在相对平和的节奏中走向收束，而非被临时意外打断。"""
    normalized_text_zh: str = """"""
    subject: str = "取子陵命"
    factor_refs: list = ['star_taiyang_juwu', 'condition_wushacou', 'pattern_wenchang_kelu', 'result_shouzhizhong', 'star_tianshang', 'star_tianshi']
    
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
        l1_anchor="zw_v1.0.0_取子陵命_001_L1",
    )
    version: str = "1.0.0"
