"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699513
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
    semantic_id="zw_v1.0.0_苏味道命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 苏味道命(SemanticEntry):
    """
    - 分字分词释义：

  - **科权禄拱来相会**：科星、权星、禄星同拱命宫，主名利权势兼得。
  - **左右扶持福不轻**：左辅右彼拱照命宫，主福气深厚。
  - **昌曲加曾富贵**：文昌文曲...
    """
    
    original_text: str = """- 分字分词释义：

  - **科权禄拱来相会**：科星、权星、禄星同拱命宫，主名利权势兼得。
  - **左右扶持福不轻**：左辅右彼拱照命宫，主福气深厚。
  - **昌曲加曾富贵**：文昌文曲加会，主富贵之论。
  - **同梁纯阳中正**：命有天同天梁，得纯阳中正之心。
  - **大限羊行酉地**：大限擎羊行至酉宫，主刑伤之徂。
  - **小限陀久劫三方俱见**：小限陀罗与地劫在三方同见，主灾厄。
  - **阴男金四局**：苏味道命盘的五行局数，金四局主刚断中正。

- **原文（source_text）**：  
  苏味道命。阴男金四局。秘经云：科权禄拱来相会，左右扶持福不轻。昌曲加曾富贵之论。命有同梁，得纯阳中正之心。大限羊行酉地，兼在小限陀久劫三方俱见，为灾，故亡。

- **规范化释义（primary_lang_explained）**：  
  苏味道为阴男金四局，命宫成「科权禄拱来相会」之格，左右辅弼同来扶持，再加文昌、文曲，主其人文才出众、品行端正，既有权位又不乏清誉。「命有同梁，得纯阳中正之心」，点出天同、天梁等星赋予其宽厚、公正的一面，使其在朝堂之上多以正直、持平的形象出现。  
  然而，大限行至擎羊所在酉地，小限同时见陀罗、天空、地劫等星在三方齐集，形成「羊陀久劫」等多重凶局。此时一方面象征外部局势的急剧变化与冲击，另一方面也暗示内在结构承压，难以承受高强度的政治风波或身心冲击，最终以灾亡收场。此命例呈现的是「德才兼备之相臣，终为极凶岁运所折」的图景。

- **完整对等诠释（secondary_lang_full）**：  
  Su Weidao’s chart is that of a Yin Metal native with Ke, Quan and Lu flanking the Life palace, supported by Left and Right Assistants. The addition of Wen Chang and Wen Qu points to literary distinction, while the presence of Tian Tong and Tian Liang is said to confer a "pure Yang and upright heart": a temperament inclined toward fairness, moderation and integrity. In life this would manifest as a minister known both for competence and moral standing.  
  The turning point comes when the major period moves into You, the seat of Yang Blade, while the minor period simultaneously encounters Tuo Luo, Tian Kong and Di Jie across the triad of houses. This "Yang‑Tuo with void‑robbers" configuration concentrates cutting and hollowing influences, symbolising violent external shifts and internal depletion. Under such compounded pressure, even a well‑balanced and virtuous structure may fail, leading to death through disaster or political catastrophe. The case depicts a minister whose cultivated virtues cannot ultimately shield him from an exceptionally harsh run of fate.

- **核心要点**：  
  1. 科权禄拱、左右扶持再加同梁，构成德才兼备、品行中正的相臣格局。  
  2. 命主一生以文才与公正著称，但同时身处高风险权力环境。  
  3. 大限羊行酉地，小限见陀、天空、久劫等星三方齐集，为灾亡的极凶组合。

- **叙事素材（narrative_snippets）**：
  - **科权禄拱**："秘经云：科权禄拱来相会，左右扶持福不轻"，苏味道命主以科名、权力与俸禄三者兼备而著称。
  - **同梁中正**："昌曲加曾富贵之论。命有同梁，得纯阳中正之心"，文星与同梁并见，使其在权位之上仍能保持宽厚、公正的品格。
  - **羊陀久劫**："大限羊行酉地，兼在小限陀久劫三方俱见，为灾，故亡"，擎羊、陀罗与天空、久劫三方齐集，为德相遭逢大灾的年份。
  - **现代应用**：在高位做事公正、又深处权力漩涡的实务者，应警惕当结构性风险（如组织斗争、极端事件）与个人命运高压年份重叠时，适当收缩战线、保全身心，而非单凭「我站得正」就忽视系统性的危险。"""
    normalized_text_zh: str = """"""
    subject: str = "苏味道命"
    factor_refs: list = ['pattern_kequanlu_gong', 'pattern_zuoyou_fuchi', 'pattern_tongliang', 'quality_chunyang_zhongzheng', 'timing_yangxing_youdi', 'malefic_tuo_jiu_jie_sanfang']
    
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
        l1_anchor="zw_v1.0.0_苏味道命_001_L1",
    )
    version: str = "1.0.0"
