"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699400
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
    semantic_id="zw_v1.0.0_赵奢之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 赵奢之命(SemanticEntry):
    """
    - 分字分词释义：

  - **科禄拱照**：科星与禄星同来拱照命宫，主富贵声扬。
  - **左右惜朝**：左辅右彼拱照命宫如朝臣辅佐，主终身福厚。
  - **大限入巳宫**：大限行至巳宫，为金...
    """
    
    original_text: str = """- 分字分词释义：

  - **科禄拱照**：科星与禄星同来拱照命宫，主富贵声扬。
  - **左右惜朝**：左辅右彼拱照命宫如朝臣辅佐，主终身福厚。
  - **大限入巳宫**：大限行至巳宫，为金局不利之火地。
  - **太岁逢忌**：太岁年干化忌落入命宫或关键宫位，激活当年负面因子。
  - **三方陀忌冲照**：三方陀罗与化忌同冲命宫，主凶险。
  - **流羊流陀冲命**：流年擎羊与流年陀罗同时冲击命宫，形成极凶年份。
  - **阳男金四局**：赵奢命盘的五行局数，金四局主刚断武勇。

- **原文（source_text）**：  
  赵奢之命。阳男金四局。科禄拱照，富贵声扬，左右惜朝，终身福厚，只四十三岁，大限入巳宫，庚子年太岁逢忌，三方陀忌冲照，又流羊、流陀冲命，小限入地网，日月陷地，故凶。

- **规范化释义（primary_lang_explained）**：  
  赵奢此命出自阳男金四局，命宫受科星与禄星拱照，再加左右辅弼朝垣，本身是典型的富贵武臣格局：早年科名可立，仕途有贵人相助，名声与实际权位都不算空泛，因此原文称其「富贵声扬，终身福厚」。然而命局也埋下寿命上的隐忧——中年前后，大限行至巳宫，对本局并不有利；四十三岁庚子年，太岁化忌并与三方陀忌、流羊、流陀等重凶相冲，小限又入天罗地网之地，日月同时陷地，多重凶象交集，最终使此富贵之命在中年遭遇致命一击，难以高寿。

- **完整对等诠释（secondary_lang_full）**：  
  This example presents the chart of a martial noble such as Zhao She. As a Yang male of the Metal Fourth Configuration, his Life palace is flanked by the Academic and Salary stars, while Left and Right Assistants converge like ministers at court. In static terms this is a classic pattern of honour and wealth: examinations go well, patronage is strong, and his public reputation matches his rank and stipends. Yet the chart also carries a built‑in warning about lifespan. Around his early forties the major period moves into Si, a region unfavourable to his original setup. In the geng‑zi year, the Annual Tai Sui takes on a taboo transformation and is struck by triplicity Robber configurations; transiting Yang Blade and Tuo Luo also attack the Life palace. At the same time the minor period falls into the Net of Heaven and Earth and both Sun and Moon are in debility. Under this pile‑up of malefics the otherwise brilliant structure cannot hold, and the native meets an untimely or violent end in midlife.

- **核心要点**：  
  1. 科禄拱命、左右朝垣，构成上等富贵格局，主早发名位与俸禄。  
  2. 大限、小限与太岁一旦同时行至陷地，又遇羊、陀等重凶合击，足以改写寿命走向。  
  3. 命局再贵，也必须结合限运与流年评估中年前后的生死关口。

- **叙事素材（narrative_snippets）**：
  - **武臣富贵**："科禄拱照，富贵声扬，左右惜朝，终身福厚"，赵奢命主以武功立名、富贵显赫。
  - **中年凶关**："只四十三岁，大限入巳宫，庚子年太岁逢忌，三方陀忌冲照，又流羊、流陀冲命"，中年大限、小限与太岁同临陷地，为寿命转折点。
  - **日月陷地**："小限入地网，日月陷地，故凶"，天罗地网配日月陷地，象征光芒被困、势难久长。
  - **现代应用**：位高权重的实务型将领，遇到科禄贵格被多重杀星冲击的年份，应主动回避前线与高危冲突，把侧重点转向训练、筹划而非亲临火线。"""
    normalized_text_zh: str = """"""
    subject: str = "赵奢之命"
    factor_refs: list = ['pattern_kelu_gongzhao', 'pattern_zuoyou_chaoyuan', 'timing_daxian_sigong', 'timing_taisui_fengji', 'timing_liuyangtuo_chongming', 'timing_xiaoxian_diwang', 'malefic_riyue_xiandi']
    
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
        l1_anchor="zw_v1.0.0_赵奢之命_001_L1",
    )
    version: str = "1.0.0"
