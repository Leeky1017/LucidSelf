"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699838
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
    semantic_id="zw_v1.0.0_裴应章命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 裴应章命(SemanticEntry):
    """
    - 分字分词释义：

  - **鸿居午位**：文星居于午宫，主文章名望。
  - **官资清显**：官位清正且等级显赫。
  - **朝堂科权禄加会**：科星、权星、禄星同会于朝堂官场，主仕途顺遂与...
    """
    
    original_text: str = """- 分字分词释义：

  - **鸿居午位**：文星居于午宫，主文章名望。
  - **官资清显**：官位清正且等级显赫。
  - **朝堂科权禄加会**：科星、权星、禄星同会于朝堂官场，主仕途顺遂与富贵。
  - **富贵双全**：财富与地位兼具且较为稳定。
  - **位登二品**：位至二品高官。
  - **阴男水二局**：裴应章命盘的五行局数，水二局主智慧清显。

- **原文（source_text）**：  
  裴应章命。阴男水二局。鿄居午位，官资清显，朝堂科权禄加会，富贵双全，位登二品。

- **规范化释义（primary_lang_explained）**：  
  裴应章命为阴男水二局，「鿄居午位」暗指曲昌类文星居于午宫，主文章名望；再加上朝堂中科星、权星、禄星同加会，是「科权禄会合而文名清显」的格局，一生多主富贵双全，位登二品的清显高官。原文未详述其夭折或重凶，整体趋向稳定、端正的仕途生涯。  
  「应章」二字亦可理解为「应和典章制度」，呼应其以礼法、文治立身的官僚形象——在制度与文书体系中承担关键角色，而非以边功或奇险著称。

- **完整对等诠释（secondary_lang_full）**：  
  Pei Yingzhang’s chart is that of a Yin Water native in the Second Configuration. With literary stars occupying Wu and "official rank pure and evident," and Ke, Quan and Lu converging at the court, the pattern describes a refined civil official: wealth and rank are "both complete," and he attains second‑rank office. The text does not emphasise sudden catastrophe or heavy affliction, suggesting a relatively steady bureaucratic career.  
  His name "Ying Zhang"—"answering to the statutes"—echoes a life spent upholding rules, documents and institutions. The chart stands as an example of a clean, orderly civil‑service destiny, where success is defined more by integrity and procedure than by drama.

- **核心要点**：  
  1. 文星居午、科权禄加会，是清显文官与富贵双全的格局。  
  2. 仕途以礼法与制度为核心，偏重文治与行政而非武功。  
  3. 原文未言重凶或早折，整体呈现平稳上升并保持清名的命途。"""
    normalized_text_zh: str = """"""
    subject: str = "裴应章命"
    factor_refs: list = ['star_wenxing_juwu', 'quality_guanzi_qingxian', 'pattern_chaotang_kequanlu', 'quality_fugui_shuangquan', 'quality_wei_erpin']
    
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
        l1_anchor="zw_v1.0.0_裴应章命_001_L1",
    )
    version: str = "1.0.0"
