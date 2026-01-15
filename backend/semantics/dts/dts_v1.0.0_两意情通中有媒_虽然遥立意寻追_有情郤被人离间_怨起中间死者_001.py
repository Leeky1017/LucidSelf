"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997609
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
    semantic_id="dts_v1.0.0_两意情通中有媒_虽然遥立意寻追_有情郤被人离间_怨起中间死者_001",
    book_id="dts",
    engine_id="bazi"
)
class 两意情通中有媒虽然遥立意寻追有情郤被人离间怨起中间死者(SemanticEntry):
    """
    - **原文（source_text）**：
  两意情通中有媒，虽然遥立意寻追。有情郤被人离间，怨起中间死者灰。

- 原注（原文注解）：
  　　喜神合神，两情相通，又引用神生化，如有媒矣……忌神...
    """
    
    original_text: str = """- **原文（source_text）**：
  两意情通中有媒，虽然遥立意寻追。有情郤被人离间，怨起中间死者灰。

- 原注（原文注解）：
  　　喜神合神，两情相通，又引用神生化，如有媒矣……忌神离间，求合不得，则恩反成怨。

- **规范化释义（primary_lang_explained）**：
  合生为“恩”，离间为“怨”。通关者可合，忌神强则反。

- 分字分词释义：
  - 情通：两意相契，路径畅通。
  - 媒：引介之神（通关/化神）。
  - 离间：以忌神或冲刑破其合生。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 恩怨 | Gratitude-Resentment (En-Yuan) | 恩情与怨恨 | Connection and estrangement | enyuan | existing |
| 两意情通 | Two Intentions Connected | 彼此有情 | Mutually affectionate | liangyi_qingtong | new_candidate |
| 媒 | Mediator (Mei) | 通关之神 | Connecting God | mei | new_candidate |
| 离间 | Estrange (Li-Jian) | 从中破坏 | Divide and disrupt | lijian | new_candidate |
| 死者灰 | Ashes of the Dead | 彻底破裂 | Complete destruction | sizhe_hui | new_candidate |
| 遥立 | Standing Afar | 远隔相望 | Standing at distance | yaoli | new_candidate |


- **次语种完整诠释（secondary_lang_full）**:  
  En-Yuan (Gratitude-Resentment) theory: Two intentions connect via a Mediator (Mei), creating Gratitude (En). If estranged by a divider (Li-Jian), Gratitude turns to Resentment (Yuan). Success depends on the Mediator; failure on the Divider (Interruption/Clash)."""
    normalized_text_zh: str = """"""
    subject: str = "两意情通中有媒，虽然遥立意寻追，有情郤被人离间，怨起中间死者灰。"
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
        l1_anchor="dts_v1.0.0_两意情通中有媒_虽然遥立意寻追_有情郤被人离间_怨起中间死者_001_L1",
    )
    version: str = "1.0.0"
