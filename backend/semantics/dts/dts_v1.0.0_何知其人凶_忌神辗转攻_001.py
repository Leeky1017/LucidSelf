"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997833
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
    semantic_id="dts_v1.0.0_何知其人凶_忌神辗转攻_001",
    book_id="dts",
    engine_id="bazi"
)
class 何知其人凶忌神辗转攻(SemanticEntry):
    """
    - 分字分词释义：
  - 何知：如何判断、凭什么知道。
  - 其人凶：此人凶险、多遭危难。
  - 忌神：命局中对日主不利的神煗。
  - 辗转攻：轮番进攻、反复攻伐。

- 规范化释义（prim...
    """
    
    original_text: str = """- 分字分词释义：
  - 何知：如何判断、凭什么知道。
  - 其人凶：此人凶险、多遭危难。
  - 忌神：命局中对日主不利的神煗。
  - 辗转攻：轮番进攻、反复攻伐。

- 规范化释义（primary_lang_explained）：
  若忌神在原局与岁运中轮番得势，对用神、日主或关键结构"辗转攻伐"，而又少有喜神解救，则一生多凶险波折，大事难安。

- **核心要点**：
  - 忌神不怕一见，怕的是反复得势、轮番进攻；
  - 攻击对象多是用神、体用主线或根气所在；
  - 若缺乏制衡与转机，则凶象易累积成大祸。

- 详细解说：
  "辗转攻"一语，点出时间维度：忌神在不同运段、不同位置上接力出现，对同一弱点反复施压，如健康隐患、财务风险、关系裂痕等。命局若忌神本就成局成势，再逢岁运加力而喜神无法抵消，则往往表现为连环事故、反复破财、官非缠身等。

- 校勘与字词辨析：
  - "辗转攻"：含"轮番、不断"之意，不是一击即止。

- **次语种完整诠释（secondary_lang_full）**：  
  We know a life is fraught with misfortune when Malefic gods mount repeated attacks: in the natal chart they already threaten the body or Useful gods, and in one decade after another they are reinforced instead of restrained."""
    normalized_text_zh: str = """"""
    subject: str = "何知其人凶，忌神辗转攻。"
    factor_refs: list = ['xiong_grade', 'jishen', 'zhanzhuangong']
    
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
        l1_anchor="dts_v1.0.0_何知其人凶_忌神辗转攻_001_L1",
    )
    version: str = "1.0.0"
