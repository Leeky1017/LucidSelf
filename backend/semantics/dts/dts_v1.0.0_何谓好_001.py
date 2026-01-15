"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997456
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
    semantic_id="dts_v1.0.0_何谓好_001",
    book_id="dts",
    engine_id="bazi"
)
class 何谓好(SemanticEntry):
    """
    - **原文（source_text）**：
  何谓好。

- **核心要点**：
  - 运岁“好”指同类相宜之助，而非泛指一切顺利；
  - 日主喜阳，则庚申一类阳金之助为好；喜阴，则辛酉一类阴...
    """
    
    original_text: str = """- **原文（source_text）**：
  何谓好。

- **核心要点**：
  - 运岁“好”指同类相宜之助，而非泛指一切顺利；
  - 日主喜阳，则庚申一类阳金之助为好；喜阴，则辛酉一类阴金之助为好；
  - 仍需辨其所助为何阵营，是扶用神，还是助长忌神。

- 详细解说：
  “好”的本义，是同类力量对日主的加持，好比遇到同阵营、同频率的帮手。若日主与格局本就喜阳金，则庚申之来多为正面助力；若喜阴金或阴柔之气，则辛酉为宜。然而若相同五行已极旺，再受同类之助反成过犹不及，就不能简单以“好”字概括，仍须结合整体强弱与用神体系来权衡。

- 校勘与字词辨析：
  - “好”：此处为“相宜之好”，重在阴阳与五行属性之契合，并非主观好恶。

- 原注（原文注解）：
  　　如庚运辛年，辛运庚年，申运酉年，酉运申年，则好。  
  　　日主喜阳，则庚与为好，日主喜阴，则辛与酉为好。

- **规范化释义（primary_lang_explained）**：
  运岁“好”指同类相宜之助。日主喜阳者，庚/申之助为好；喜阴者，辛/酉之助为好。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 好 | Good (Hao) | 同类相助 | Support from same kind | hao_tongzhu | new_candidate |
| 喜阳 | Prefer Yang | 喜阳干支之助 | Prefer support from Yang stems/branches | xi_yang | new_candidate |
| 喜阴 | Prefer Yin | 喜阴干支之助 | Prefer support from Yin stems/branches | xi_yin | new_candidate |
| 庚申 | Geng/Shen | 阳金之力 | Yang Metal power | gengshen_li | new_candidate |
| 辛酉 | Xin/You | 阴金之力 | Yin Metal power | xinyou_li | new_candidate |
| 相宜 | Suitable | 恰当之助 | Appropriate support | xiang_yi | new_candidate |


- **次语种完整诠释（secondary_lang_full）**:  
  Hao (Good) means 同类相宜之助 same-kind-support. If Self prefers Yang, Geng/Shen support is good; if Self prefers Yin, Xin/You support is good. It is about matching the polarity and element needed by the Day Master."""
    normalized_text_zh: str = """"""
    subject: str = "何谓好"
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
        l1_anchor="dts_v1.0.0_何谓好_001_L1",
    )
    version: str = "1.0.0"
