"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699555
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
    semantic_id="zw_v1.0.0_李太白命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 李太白命(SemanticEntry):
    """
    - 分字分词释义：

  - **天魁天钺**：代表贵人、提携与名望的两颗吉星。
  - **权禄生逢**：权星与禄星在命局中同时得用，主权势与俸禄兼得。
  - **左右加曾**：左辅右彼加会命宫，...
    """
    
    original_text: str = """- 分字分词释义：

  - **天魁天钺**：代表贵人、提携与名望的两颗吉星。
  - **权禄生逢**：权星与禄星在命局中同时得用，主权势与俸禄兼得。
  - **左右加曾**：左辅右彼加会命宫，主富贵与贵人扶持。
  - **空劫在命垣**：天空、地劫同在命宫或三方，主虚耗落空、寿元难长。
  - **天罗地网**：象征被困、缠绕与难以脱身的格局。
  - **文垂后世**：文采与声名可垂后世，以作品名世。
  - **阳男水二局**：李太白命盘的五行局数，水二局主智慧才情。

- **原文（source_text）**：  
  李太白命。阳男水二苟。天魁天钺，世称李白文垂，权禄生逢，欣然入相，左右加曾，富贵终身。只柰空劫在命垣，寿不长久。大小二限，天罗地网，是以凶也。

- **规范化释义（primary_lang_explained）**：  
  李太白命为阳男水二局，命宫得天魁、天钺拱照，配合权、禄生逢，再加左右辅弼同来，是典型「贵人星 + 权禄 + 左右」齐集的文贵命，一生以文名天下，富贵不绝。「世称李白文垂」点出其文采与声名可垂后世，从命理结构上即为天魁、天钺、文星与权禄合力所成。  
  然而，命垣带空劫，预示寿元难以极长，容易在某些阶段遭遇突如其来的折损。原文又言「大小二限，天罗地网，是以凶也」，说明当大限、小限同时行至天罗地网之地时，空劫与罗网重叠，一方面象征环境中阻塞缠绕、人事与处境多有羁绊，另一方面也暗示身体与气数遭强力牵扯，难以安然度过。此命例借李白之名，呈现的是「文名极盛而寿不及高龄」的才子命结构。

- **完整对等诠释（secondary_lang_full）**：  
  Li Taibai’s chart is that of a Yang Water native in the Second Configuration. Tian Kui and Tian Yue lend exalted support, while Power and Lu stars arise in his favour, and Left and Right Assistants gather around the Life palace. This alignment of noble stars, authority, stipends and assistants typifies a literary nobleman whose achievements and reputation endure—hence the phrase "Li Bai, whose writings remain for posterity." Structurally, the chart concentrates both honour and artistic brilliance.  
  Yet the Life sector is also marked by Kong and Jie, indicating vulnerability in matters of longevity and stability. When both major and minor periods move into the regions of the Celestial Net and Earthly Snare, these void and entangling influences compound. Externally, this suggests situations of constraint, entrapment or repeated obstruction; internally, it points to a life force that can be abruptly depleted rather than gently fading. The example, using the figure of Li Bai, thus illustrates a pattern where towering literary fame coexists with a lifespan that does not reach extreme old age.

- **核心要点**：  
  1. 天魁天钺配合权禄与左右，是文采卓越、名垂后世的文贵命格。  
  2. 命垣空劫与后期天罗地网限运，使寿元难以极长，易在重压之年折损。  
  3. 呈现「才名极盛而寿略短」的典型才子命结构，可为类似命局提供对照。

- **叙事素材（narrative_snippets）**：
  - **文垂千古**："天魁天钺，世称李白文垂"，天魁天钺加持，使李太白以诗名流传千载。
  - **权禄左右**："权禄生逢，欣然入相，左右加曾，富贵终身"，权禄与左右同来，既有入相之资，也不乏现实富贵享用。
  - **空劫罗网**："只柰空劫在命垣，寿不长久。大小二限，天罗地网，是以凶也"，空劫加天罗地网，象征才华与生命在重重束缚中消耗。
  - **现代应用**：对极具天赋、靠作品与声誉立身者而言，若命垣见空劫又逢罗网重限，应避免长期沉溺于透支身心的创作或放纵生活，学会为身体和精神预留恢复空间，才能让才华活得更久。"""
    normalized_text_zh: str = """"""
    subject: str = "李太白命"
    factor_refs: list = ['star_tiankui_tianyue', 'pattern_quanlu_shengfeng', 'pattern_zuoyou_jiahui', 'malefic_kongjie_mingyuan', 'malefic_tianluodiwang', 'result_wenchui']
    
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
        l1_anchor="zw_v1.0.0_李太白命_001_L1",
    )
    version: str = "1.0.0"
