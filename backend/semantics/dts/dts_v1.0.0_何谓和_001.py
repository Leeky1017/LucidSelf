"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997450
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
    semantic_id="dts_v1.0.0_何谓和_001",
    book_id="dts",
    engine_id="bazi"
)
class 何谓和(SemanticEntry):
    """
    - **原文（source_text）**：
  何谓和。

- **核心要点**：
  - 运岁相和，关键在“化何物”与“日主所喜”；
  - 合化成用神为“化喜”，多主有利重组；
  - 合化成忌...
    """
    
    original_text: str = """- **原文（source_text）**：
  何谓和。

- **核心要点**：
  - 运岁相和，关键在“化何物”与“日主所喜”；
  - 合化成用神为“化喜”，多主有利重组；
  - 合化成忌神为“化忌”，多主隐性风险。

- 详细解说：
  本条强调“和”并非一概为吉，而是要看运岁合化之后的新五行属于喜神阵营还是忌神阵营。乙庚化金、子丑化土等例子，若所成之金土为用，则和中有生扶与开路；若所成之气为忌，则和中反带来牵连与沉重负担。判断时必须追问：和后到底“化成了什么”。

- 校勘与字词辨析：
  - “化何物”：点明本条重心在“成何物”，而非单纯有无合和。

- 原注（原文注解）：
  　　如乙运庚年，庚运乙年，则和（乙庚化金），日主喜金则吉，日主喜木则不吉。  
  　　如子运丑年，丑运子年，则和（子丑合而化土），日主喜土则吉。喜水则不吉。

- **规范化释义（primary_lang_explained）**：
  运岁相和，关键在“化何物”与“日主所喜”。化为所喜则吉，为所忌则不吉。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 和 | Harmony (He) | 岁运相合 | Merge between Yun and Sui | tiangan_he | existing |
| 化何物 | What it Transforms Into | 合化后之五行 | Element produced after merge | hua_hewu | new_candidate |
| 化喜 | Transform into Favored | 化出喜用神 | Transform into yongshen | hua_xi | new_candidate |
| 化忌 | Transform into Disfavored | 化出忌神 | Transform into jishen | hua_ji | new_candidate |
| 乙庚化金 | Yi-Geng Transforms to Metal | 乙庚合金 | Yi and Geng merge to Metal | yigeng_huajin | new_candidate |
| 子丑化土 | Zi-Chou Transforms to Earth | 子丑合土 | Zi and Chou merge to Earth | zichou_huatu | new_candidate |


- **次语种完整诠释（secondary_lang_full）**:  
  He (Harmony) between Yun and Sui: e.g. Yi-Geng or Zi-Chou merge. Key is 化何物 what-it-transforms-into and 日主所喜 what-Self-prefers. Transform into 所喜 favored-element is lucky; transform into 所忌 disfavored-element is unlucky. Not all harmony is good; it depends on the result."""
    normalized_text_zh: str = """"""
    subject: str = "何谓和"
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
        l1_anchor="dts_v1.0.0_何谓和_001_L1",
    )
    version: str = "1.0.0"
