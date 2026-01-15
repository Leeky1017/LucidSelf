"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997674
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
    semantic_id="dts_v1.0.0_知慈母恤孤之道_方有瓜瓞无疆之庆_001",
    book_id="dts",
    engine_id="bazi"
)
class 知慈母恤孤之道方有瓜瓞无疆之庆(SemanticEntry):
    """
    - **原文（source_text）**：
  知慈母恤孤之道，方有瓜瓞无疆之庆。

- 原注（原文注解）：
  　　日主为母，所生为子（食伤）……母旺子孤，要助其子，行火运，方有瓜瓞绵绵之庆矣。
...
    """
    
    original_text: str = """- **原文（source_text）**：
  知慈母恤孤之道，方有瓜瓞无疆之庆。

- 原注（原文注解）：
  　　日主为母，所生为子（食伤）……母旺子孤，要助其子，行火运，方有瓜瓞绵绵之庆矣。

- **规范化释义（primary_lang_explained）**：
  母旺子孤，当助子（行火运、生土资财等）以成其用。

- 分字分词释义：
  - 母：印绶。
  - 恤孤：母旺子孤之象。
  - 瓜瓞：子嗣繁衍。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 母子 | Mother-Child (Mu-Zi) | 印与食伤 | Resource and Output | muzi | existing |
| 慈母恤孤 | Benevolent Mother Pities Orphan | 母旺子弱 | Strong Mother, Weak Child | cimu_xugu | new_candidate |
| 瓜瓞无疆 | Endless Succession | 子孙绵延 | Endless offspring/success | guadie_wujiang | new_candidate |
| 恤孤 | Pity the Orphan | 扶持弱子 | Support the weak child | xugu | new_candidate |
| 庆 | Celebration/Blessing | 吉庆 | Auspiciousness | qing | new_candidate |


- **次语种完整诠释（secondary_lang_full）**:  
  Mu-Zi (Mother-Child) theory: "Benevolent Mother Pities Orphan" (Ci-Mu Xu-Gu). Mother (Resource) is strong, Child (Output) is weak. Must support the Child (e.g., with Fire/Output) to ensure endless succession (Gua-Die Wu-Jiang)."""
    normalized_text_zh: str = """"""
    subject: str = "知慈母恤孤之道，方有瓜瓞无疆之庆。"
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
        l1_anchor="dts_v1.0.0_知慈母恤孤之道_方有瓜瓞无疆之庆_001_L1",
    )
    version: str = "1.0.0"
