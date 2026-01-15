"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997821
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
    semantic_id="dts_v1.0.0_何知其人贫_财神终不真_001",
    book_id="dts",
    engine_id="bazi"
)
class 何知其人贫财神终不真(SemanticEntry):
    """
    - 分字分词释义：
  - 何知：如何判断、凭什么知道。
  - 其人贫：此人贫困、经济窘迫。
  - 财神：财星之神。
  - 终不真：始终不真实、有名无实。

- 原注（原文注解）：
 　　伤轻财...
    """
    
    original_text: str = """- 分字分词释义：
  - 何知：如何判断、凭什么知道。
  - 其人贫：此人贫困、经济窘迫。
  - 财神：财星之神。
  - 终不真：始终不真实、有名无实。

- 原注（原文注解）：
 　　伤轻财重、财轻官重、伤重印轻、财重劫轻等，皆"财神不真"。

- 规范化释义（primary_lang_explained）：
  论一个人是否贫困，则看"财神是否为真"：财星若被伤官、比劫、官煚等反复争夺，或本身根气不足、位置偏颇，即使表面有财名，终究难以长久聚敛，多见钱来易去、劳而少获之象。

- **核心要点**：
  - 财神不真，多在“有名无实”或“聚之即散”；
  - 结构上常见财与伤、印、劫之间失衡争夺；
  - 需结合岁运，看是否有阶段性翻转机会。

- 详细解说：
  本条从反面说明：并非见财即富。若财星过轻而官重，易为官事所累；财过重而身弱，则为财所役；伤重印轻，则才华自耗、难以化为稳定收入；财重劫轻，则多见被亲友同类所分食。命局若长期处于这种“财神不真”的结构，再遇耗财之运，往往终身奔波、积蓄有限，只能以“手上有过钱、身边留不住”来概括。

- 校勘与字词辨析：
  - “终不真”：强调的是长期走势，而非短期一时的贫富波动。

- **次语种完整诠释（secondary_lang_full）**：  
  We know a person is poor when the Wealth god is never truly solid: Wealth is weak, easily injured by Output, stolen by Peers, or controlled by Officer without proper return. Such people may touch money, but their income is unstable, leaks away through obligations and conflicts, and rarely crystallises into lasting assets."""
    normalized_text_zh: str = """"""
    subject: str = "何知其人贫，财神终不真。"
    factor_refs: list = []
    
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
        book_id="dts",
        chapter="",
        l1_anchor="dts_v1.0.0_何知其人贫_财神终不真_001_L1",
    )
    version: str = "1.0.0"
