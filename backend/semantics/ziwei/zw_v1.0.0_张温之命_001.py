"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699701
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
    semantic_id="zw_v1.0.0_张温之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 张温之命(SemanticEntry):
    """
    - 分字分词释义：

  - **魁钺夹命**：天魁、天钺分列命宫两侧，主贵人提携与荣誉机会。
  - **日月反背**：日月未能正向照命，反而形成背离，主光源不足或方向不对。
  - **苗而不秀*...
    """
    
    original_text: str = """- 分字分词释义：

  - **魁钺夹命**：天魁、天钺分列命宫两侧，主贵人提携与荣誉机会。
  - **日月反背**：日月未能正向照命，反而形成背离，主光源不足或方向不对。
  - **苗而不秀**：资质并非全无，却难以开花结果，主有潜力而不成器。
  - **科名陷于凶神**：科名之气被凶星压制，主功名难以取得。
  - **限步又不遂**：大限小限多不顺利，主行运阻塞。
  - **怨限**：因行运不顺而对运限心生怨尤的状态。
  - **阴男土五局**：张温命盘的五行局数，土五局主厚重持平。

- **原文（source_text）**：  
  张温之命。阴男土五局。魁钺夹命，本为富贵，日月反背，苖而不秀，科名陷于凶神，是因不头其文也，且限步又不遂，因此怨限，三十一岁而死。

- **规范化释义（primary_lang_explained）**：  
  张温之命为阴男土五局，命局得天魁、天钺夹命，本是富贵之象，应有贵人提携与科名机会。但日月反背，难以正面照拱命垣，「苗而不秀」，形容资质并非全无，却难以开花结果；科名之气陷入凶神之所，是「贵气有源而不成器」的结构。  
  再加上行运「限步又不遂」，即大运、小运多不就，令命主对自身怀才不遇与运程阻滞心生怨尤，「怨限」二字点出心理层面的扭结。终在三十一岁而死，寿命明显短于一般富贵格可承载的长度，形成「贵星夹命却终不得善展，反以怨限早折」的命例。

- **完整对等诠释（secondary_lang_full）**：  
  Zhang Wen’s chart is that of a Yin Earth native in the Fifth Configuration. With Tian Kui and Tian Yue flanking the Life palace, the native is in principle marked for patronage and honour; yet the Sun and Moon "turn their backs" rather than properly illuminating the chart. The image of "sprouts that do not blossom" suggests talent and opportunity that fail to mature, while "examination qi engulfed by malefic stars" indicates that scholarly prospects are swallowed by adverse forces.  
  The text further states that his "steps of fortune do not proceed," so that both major and minor periods frustrate advancement. Resentment towards fate accumulates—"blaming the limits"—and this psychological knot mirrors the structural blockage. Death at thirty‑one underscores how the potential promised by noble flanking stars can be cut short when supportive luminaries are reversed and transits remain unsupportive. The case illustrates a pattern of thwarted promise and early closure.

- **核心要点**：  
  1. 魁钺夹命本为贵格，但日月反背、科名陷于凶神，使「苗而不秀」。  
  2. 行运多不顺利，命主易对运势心生怨尤，「怨限」加深内在耗损。  
  3. 三十一岁早亡，呈现贵星在位却难以落地、终致短寿的命局。"""
    normalized_text_zh: str = """"""
    subject: str = "张温之命"
    factor_refs: list = ['pattern_kuiyue_jiaming', 'malefic_riyue_fanbei', 'quality_miao_buxiu', 'malefic_keming_xian', 'timing_xianbu_busui', 'quality_yuanxian']
    
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
        l1_anchor="zw_v1.0.0_张温之命_001_L1",
    )
    version: str = "1.0.0"
