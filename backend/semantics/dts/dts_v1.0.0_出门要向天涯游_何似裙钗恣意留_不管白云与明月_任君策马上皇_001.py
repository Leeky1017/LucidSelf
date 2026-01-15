"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997739
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
    semantic_id="dts_v1.0.0_出门要向天涯游_何似裙钗恣意留_不管白云与明月_任君策马上皇_001",
    book_id="dts",
    engine_id="bazi"
)
class 出门要向天涯游何似裙钗恣意留不管白云与明月任君策马上皇(SemanticEntry):
    """
    - **原文（source_text）**：
  出门要向天涯游，何似裙钗恣意留，不管白云与明月，任君策马上皇州。

- 原注（原文注解）：
  　　本欲发奋有为，而日主有合，不顾用神；用神有合，不顾...
    """
    
    original_text: str = """- **原文（source_text）**：
  出门要向天涯游，何似裙钗恣意留，不管白云与明月，任君策马上皇州。

- 原注（原文注解）：
  　　本欲发奋有为，而日主有合，不顾用神；用神有合，不顾日主……皆“有情而反无情”。若能“日主弃闲神而驰骤、用神随日主而驱策”，则“无情而有情”，乃可成其志。

- **规范化释义（primary_lang_explained）**：
  论“情与志”的羁绊解法：弃牵绊、循用神而行。

- 分字分词释义：
  - 情：合绊之情、感性牵引。
  - 志：用神之志、功用之向。
  - 策马：专注奔赴主线之喻。

- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 绊神 | Entangled God (Ban-Shen) | 羁绊之神 | Binding element | banshen | existing |
| 裙钗 | Skirt/Hairpin (Sentiment) | 儿女情长 | Sentimental ties | qunchai | new_candidate |
| 恣意留 | Willfully Detain | 随意挽留 | Hold back | ziyiliu | new_candidate |
| 策马 | Whip the Horse | 奋进 | Gallop forward | cema | new_candidate |
| 皇州 | Imperial City (Success) | 功名之地 | Place of success | huangzhou | new_candidate |
| 有情反无情 | Affection Turns Heartless | 因情坏事 | Love ruins purpose | youqing_fanwuqing | new_candidate |

- **次语种完整诠释（secondary_lang_full）**:  
  Ban-Shen (Entangled God) theory: "Want to Roam the World" (Chu-Men Yao-Xiang Tian-Ya-You), but "Held Back by Skirt/Hairpin" (Qun-Chai Zi-Yi-Liu). Sentimental Ties (Qing) bind the Will (Zhi). Must abandon Idle Gods/Entanglements and ride the Use God to the "Imperial City" (Huang-Zhou)."""
    normalized_text_zh: str = """"""
    subject: str = "出门要向天涯游，何似裙钗恣意留，不管白云与明月，任君策马上皇州。"
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
        l1_anchor="dts_v1.0.0_出门要向天涯游_何似裙钗恣意留_不管白云与明月_任君策马上皇_001_L1",
    )
    version: str = "1.0.0"
