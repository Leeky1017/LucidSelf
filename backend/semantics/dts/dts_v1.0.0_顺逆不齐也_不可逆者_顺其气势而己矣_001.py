"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997503
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
    semantic_id="dts_v1.0.0_顺逆不齐也_不可逆者_顺其气势而己矣_001",
    book_id="dts",
    engine_id="bazi"
)
class 顺逆不齐也不可逆者顺其气势而己矣(SemanticEntry):
    """
    - **原文（source_text）**：
  顺逆不齐也，不可逆者，顺其气势而己矣。

- 原注（原文注解）（意旨）：
  刚柔、源流、权势、气机诸端，凡已成势者，可顺不可逆。

- 分字分词释义...
    """
    
    original_text: str = """- **原文（source_text）**：
  顺逆不齐也，不可逆者，顺其气势而己矣。

- 原注（原文注解）（意旨）：
  刚柔、源流、权势、气机诸端，凡已成势者，可顺不可逆。

- 分字分词释义：
  - 顺：顺应其势而行。
  - 逆：违逆其势而强行改变。
  - 气势：局中五行流行所形成的总体方向与力量。

- **规范化释义（primary_lang_explained）**：
  已成之势应顺势而为，逆之多凶；未成之势则可因势利导，以用神为纽带，设法引向所喜之方。所谓“不可逆者”，是指大势已定、力量集中之处，不宜硬作反向操作；顺其气势，同时在细部做调节，才是真正的取用之道。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 顺逆 | Flow-Reverse (Shun-Ni) | 顺势与逆势 | Following and opposing flow | shunni | existing |
| 气势 | Qi Momentum | 五行大势 | Overall momentum of 5-elements | qishi | new_candidate |
| 不可逆 | Cannot be Reversed | 势大不可挡 | Momentum too strong to oppose | bukeni | new_candidate |
| 顺其气势 | Follow Qi Momentum | 顺势而为 | Act according to the flow | shun_qiqishi | new_candidate |
| 已成势 | Established Momentum | 局势已定 | Structure is fixed | yichengshi | new_candidate |
| 未成势 | Unformed Momentum | 局势未定 | Structure not yet fixed | weichengshi | new_candidate |


- **次语种完整诠释（secondary_lang_full）**:  
  Shun-Ni (Flow-Reverse) theory: Shun is following the flow, Ni is reversing it. "Cannot be reversed" (不可逆) means when the Qi momentum (气势) is established, one must follow it. If the momentum is not yet formed, one can guide it. The key is to recognize the established power and align with it."""
    normalized_text_zh: str = """"""
    subject: str = "顺逆不齐也，不可逆者，顺其气势而己矣。"
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
        l1_anchor="dts_v1.0.0_顺逆不齐也_不可逆者_顺其气势而己矣_001_L1",
    )
    version: str = "1.0.0"
