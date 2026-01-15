"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997814
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
    semantic_id="dts_v1.0.0_何知其人富_财气通门户_001",
    book_id="dts",
    engine_id="bazi"
)
class 何知其人富财气通门户(SemanticEntry):
    """
    - 分字分词释义：
  - 何知：如何判断、凭什么知道。
  - 其人富：此人富裕、财富充裕。
  - 财气：财星之气、财运流通。
  - 通门户：畅通入门、能实际落定。

- 原注（原文注解）：
 ...
    """
    
    original_text: str = """- 分字分词释义：
  - 何知：如何判断、凭什么知道。
  - 其人富：此人富裕、财富充裕。
  - 财气：财星之气、财运流通。
  - 通门户：畅通入门、能实际落定。

- 原注（原文注解）：
 　　财旺身强、官卫财、财能坏印/生官、伤财通、暗成财局等，皆"财气通门户"。

- 规范化释义（primary_lang_explained）：
  判断一人是否富足，要看"财气是否通门户"：财星有根有源，身能任财，又能与官印形成良性循环，使财富有进入、有累积，有实际落点，而非虚浮之财。

- **核心要点**：
  - 富在“财有路、身能任、格局能守”；
  - 财须与官印构成可持续的生用关系；
  - 忌空财、漏财、耗财，只见数字不见门第。

- 详细解说：
  “财气通门户”涵盖三个层面：一是财源通畅，如有稳定产业、渠道或专业变现能力；二是门户得所，财富能化为门第与资源，而非一掷即空；三是结构配合得当，官能卫财、印能护身，使人既能运用财富，又不至被财所累。命局中若见财星得地而不受重克，并与身、官、印之间形成良性循环，多主可聚可守之富。

- 校勘与字词辨析：
  - “门户”：既指家门气象，也指产业、组织、品牌等可见的承载形态。

- **次语种完整诠释（secondary_lang_full）**：  
  We know a person is wealthy when Wealth qi forms clear channels and gates: Wealth stars are rooted, flow smoothly toward the body, and are linked to Officer and Resource in a way that builds houses, businesses, land, or other tangible bases. Money does not just pass through the hands but settles into structures that can be guarded and grown."""
    normalized_text_zh: str = """"""
    subject: str = "何知其人富，财气通门户。"
    factor_refs: list = ['wealth_grade', 'cai_xing', 'wealth_flow', 'gate_config', 'wealth_flow']
    
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
        l1_anchor="dts_v1.0.0_何知其人富_财气通门户_001_L1",
    )
    version: str = "1.0.0"
