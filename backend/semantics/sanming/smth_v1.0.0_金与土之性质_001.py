"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227804
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
    semantic_id="smth_v1.0.0_金与土之性质_001",
    book_id="sanming",
    engine_id="bazi"
)
class 金与土之性质(SemanticEntry):
    """
    - **原文（source_text）**：
  金主于西，应秋。金之为言禁也。阴气始禁止万物而揫敛。披沙拣金，土所生也。生于土而别于土，乃自然之形也。土主于中央，兼位西南，应于长夏。土之为言吐也，含...
    """
    
    original_text: str = """- **原文（source_text）**：
  金主于西，应秋。金之为言禁也。阴气始禁止万物而揫敛。披沙拣金，土所生也。生于土而别于土，乃自然之形也。土主于中央，兼位西南，应于长夏。土之为言吐也，含吐万物，将生者出，将死者归，为万物家，故长于夏末，火所生也。土或胜水，水乃反土，自然之义也。

- **分字分词释义**：
  - **禁**：禁止、收敛之意。
  - **揫敛**：收敛聚拢。
  - **披沙拣金**：在沙土中拣选出金。
  - **吐**：吐纳、出入之意。
  - **含吐万物**：包含并吐出万物。

- **规范化释义（primary_lang_explained）**：
  金对应西方，对应秋季。所谓"金"，其本义是"禁"——阴气开始禁止万物生长，使之收敛聚拢。披开沙土可以拣出金来，说明金由土所生。金生于土中，但又区别于土而独立存在，这是自然的形态。土对应中央，兼顾西南方位，对应长夏（夏末）。所谓"土"，其本义是"吐"——含吐万物，将要生的吐出，将要死的归入，成为万物的家园，所以土气盛长于夏末，由火所生。土能够战胜水，水也能反过来制约土，这是自然的道理。

- **完整对等诠释（secondary_lang_full）**：
  Metal governs the West and corresponds to Autumn. Metal's essence means "restriction"—yin qi begins to restrict and contract all things. Sifting sand extracts metal, showing that Earth generates Metal. Metal is born from Earth yet distinct from it as a natural form. Earth governs the Center and extends to the Southwest, corresponding to late summer. Earth's essence means "expelling"—containing and expelling all things, the emerging births and returning deaths, serving as home for all, thriving in late summer as Fire generates Earth. Earth may overcome Water, yet Water may counter-restrict Earth in turn, reflecting natural balance. This depicts Metal's contractive-restrictive nature and Earth's bearing-nurturing nature with mutual checking, enabling balance through both generation and restriction rather than isolation. This establishes Metal and Earth's pivotal essential nature in destiny analysis.

- **核心要点**：
  - 金对应西方秋季，主禁止收敛；土对应中央长夏，主含吐万物
  - 金生于土而别于土；土生于火，为万物家园
  - 土或胜水，水或反土，体现自然平衡

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_131]` `[trigger: 金土之性质]` `[factor_trigger: element_metal AND element_earth]` `[role: 主干]` 金主于西，应秋。金之为言禁也，阴气始禁止万物而揚敛。土主于中央，兼位西南，应于长夏。土之为言吐也，含吐万物，为万物家。 → 《三命通会》卷一#金与土之性质

- **详细解说**：
  此条合论金土二行。金主西方秋季，本义为"禁"——阴气主导，禁止万物生长，使之收敛。金由土生，从沙土中拣选出来，虽源于土却有独立形态。土主中央，兼顾西南，对应长夏（夏末），本义为"吐"——土如母亲，含吐万物，该生的吐出，该死的归入，是万物的家园。土由火生，在夏末最盛。土与水的关系最为微妙："土或胜水"是常理（土克水），但"水乃反土"说明水多时也能反克土（水泛土流），这体现五行相克中的动态平衡。

- **校勘与字词辨析（双语）**：
  - **中文**："揫敛"，"揫"音jū，收聚之意。"含吐"指包含与吐出，非"呕吐"。
  - **English**："揫敛" (contracting) emphasizes metal's restrictive nature; "含吐" (containing and expelling) shows earth's nurturing and receiving functions, not vomiting."""
    normalized_text_zh: str = """"""
    subject: str = "金与土之性质"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_金与土之性质_001_L1",
    )
    version: str = "1.0.0"
