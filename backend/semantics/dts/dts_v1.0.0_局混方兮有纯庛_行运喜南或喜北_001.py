"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997331
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
    semantic_id="dts_v1.0.0_局混方兮有纯庛_行运喜南或喜北_001",
    book_id="dts",
    engine_id="bazi"
)
class 局混方兮有纯庛行运喜南或喜北(SemanticEntry):
    """
    - **原文（source_text）**：
  局混方兮有纯庛，行运喜南或喜北。

- 原注（原文注解）：
  　　如亥卯未木局，混一寅辰，则太强，行运南北，则有纯疵，不能俱利。

- **L2-术...
    """
    
    original_text: str = """- **原文（source_text）**：
  局混方兮有纯庛，行运喜南或喜北。

- 原注（原文注解）：
  　　如亥卯未木局，混一寅辰，则太强，行运南北，则有纯疵，不能俱利。

- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 局混方 | Ju Mixed with Fang | 三合局混杂方气 | Trinity assembly mixed with directional qi | juhunfang | new_candidate |
| 纯庛 | Purity and Flaw | 纯正与瑕疵并存 | Coexistence of purity and flaw | chunci | new_candidate |
| 喜南或喜北 | Favor South or North | 行运需择一方向 | Transit luck must favor one direction | xi_nan_bei | new_candidate |
| 难两全 | Cannot Benefit Both | 难以两端俱利 | Cannot benefit from both directions | nan_liangquan | new_candidate |
| 取舍 | Trade-off | 必须做出选择 | Making a necessary choice | qushe | new_candidate |

<!-- L2_BEGIN -->

- 分字分词释义：
  - 局混方：三合局中混杂一方之气（或反之）。
  - 纯庛：纯正与瑕疵（偏盛之病）并存。
  - 行运喜南或喜北：行运方向需择一而利，难两全。

- **规范化释义（primary_lang_explained）**：
  局与方混杂，会出现“纯与疵”的失衡，行运多需择一而利，难两全。

- **次语种完整诠释（secondary_lang_full）**:  
  When a trinity assembly is mixed with a directional Fang of the same element, the result is powerful but uneven. One side of the structure is clean and well-formed, while another side carries the flaw of excess. In such charts it is hard to have both ends prosper at once: major luck along one axis – for example, a southern versus northern route – will line up with the purer side and bring benefit, while the opposite axis tends to trigger the overloaded, problematic side. The teaching is that strength alone is not enough; you must recognise where the pattern is most balanced and choose that direction, instead of trying to make every path equally favourable."""
    normalized_text_zh: str = """- 局混方：三合局中混杂一方之气（或反之）。"""
    subject: str = "局混方兮有纯庛，行运喜南或喜北。"
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
        l1_anchor="dts_v1.0.0_局混方兮有纯庛_行运喜南或喜北_001_L1",
    )
    version: str = "1.0.0"
