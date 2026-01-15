"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997680
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
    semantic_id="dts_v1.0.0_知孝子奉亲之方_始能克谐大顺之风_001",
    book_id="dts",
    engine_id="bazi"
)
class 知孝子奉亲之方始能克谐大顺之风(SemanticEntry):
    """
    - **原文（source_text）**：
  知孝子奉亲之方，始能克谐大顺之风。

- 原注（原文注解）：
  　　日主为子，生我为母（印绶）……要安其母，用金生水，用土生金，则子母之情顺矣。

...
    """
    
    original_text: str = """- **原文（source_text）**：
  知孝子奉亲之方，始能克谐大顺之风。

- 原注（原文注解）：
  　　日主为子，生我为母（印绶）……要安其母，用金生水，用土生金，则子母之情顺矣。

- **规范化释义（primary_lang_explained）**：
  子众母衰，当安母（以金生水、土生金），则情顺。

- 分字分词释义：
  - 孝子奉亲：子（身）安其母（印）。
  - 大顺：家道和谐之象。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 孝子奉亲 | Filial Child Serves Parent | 子旺母弱 | Strong Child serves Weak Mother | xiaozi_fengqin | new_candidate |
| 克谐 | Able to Harmonize | 能够和谐 | Achieve harmony | kexie | new_candidate |
| 大顺 | Great Smoothness | 大顺之风 | Great harmony | dashun | new_candidate |
| 奉亲 | Serve Parent | 奉养印绶 | Nourish Resource | fengqin | new_candidate |
| 顺静 | Smooth and Quiet | 安详顺静 | Peaceful | shunjing | new_candidate |


- **次语种完整诠释（secondary_lang_full）**:  
  Mu-Zi (Mother-Child) theory: "Filial Child Serves Parent" (Xiao-Zi Feng-Qin). Child (Daymaster/Output) is strong, Mother (Resource) is weak. Must secure the Mother (e.g., use Metal/Water) to achieve "Great Harmony" (Da-Shun)."""
    normalized_text_zh: str = """"""
    subject: str = "知孝子奉亲之方，始能克谐大顺之风。"
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
        l1_anchor="dts_v1.0.0_知孝子奉亲之方_始能克谐大顺之风_001_L1",
    )
    version: str = "1.0.0"
