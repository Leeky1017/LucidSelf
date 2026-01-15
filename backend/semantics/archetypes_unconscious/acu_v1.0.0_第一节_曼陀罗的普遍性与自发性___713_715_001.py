"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.521875
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
    semantic_id="acu_v1.0.0_第一节_曼陀罗的普遍性与自发性___713_715_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 第一节曼陀罗的普遍性与自发性713715(SemanticEntry):
    """
    **原文** (¶713-715, 行10769-10850):

> [713] 曼陀罗（梵语意为"圆"）是一种在东方和西方都广泛存在的宗教象征。在东方，它主要用于冥想，作为精神集中的工具。在西方，...
    """
    
    original_text: str = """**原文** (¶713-715, 行10769-10850):

> [713] 曼陀罗（梵语意为"圆"）是一种在东方和西方都广泛存在的宗教象征。在东方，它主要用于冥想，作为精神集中的工具。在西方，它出现在中世纪的教堂艺术中，特别是玫瑰窗...
>
> [714] 然而，曼陀罗不仅是历史现象。它们也自发地出现在现代人的梦境和幻想中，特别是在心理危机或个体化过程中...
>
> [715] 曼陀罗的出现通常与秩序、平衡和整体感有关。它们似乎表达了心灵对完整性和中心化的渴望。

**英文释义**:

曼陀罗 = 梵语"圆"。东方：冥想工具，精神集中。西方：中世纪教堂艺术（玫瑰窗）。不仅是历史现象——自发出现于现代人梦境/幻想。特别在心理危机或个体化过程中。出现与秩序、平衡、整体感相关。表达心灵对完整性和中心化的渴望。

**完整中文诠释**:

**曼陀罗的跨文化存在**：
- 东方：冥想工具，精神集中
- 西方：中世纪教堂艺术（特别是玫瑰窗）
- 藏传佛教：沙曼陀罗
- 印度教：神圣几何

**自发性**：
- 不仅是历史/宗教现象
- 自发出现于现代人梦境和幻想
- 特别在心理危机时
- 个体化过程中频繁出现

**心理意义**：
- 与秩序、平衡、整体感相关
- 表达对完整性的渴望
- 表达对中心化的渴望
- 是心灵的自然产物

**核心要点**:
- 曼陀罗跨文化普遍存在
- 自发出现于现代人心理过程
- 表达对完整性和中心化的渴望
- 心灵的自然产物，非学习所得

**叙事片段**:
- `[ns_cw9i_XI_001]` `[trigger: 曼陀罗普遍性]` `[factor_trigger: jung_mandala AND jung_universality]` `[role: 主干]` 曼陀罗东西方普遍存在——自发出现于现代人梦境，表达对完整性和中心化的渴望。→ ¶713-715
- `[ns_cw9i_XI_002]` `[trigger: mandala_cross_cultural]` `[factor_trigger: jung_mandala AND cultural_forms]` `[role: 条件分支]` East: meditation tool; West: rose windows; spontaneous in modern dreams/fantasies. → Cross-cultural
- `[ns_cw9i_XI_003]` `[trigger: psychological_crisis]` `[factor_trigger: jung_mandala AND individuation]` `[role: 条件分支]` Particularly during psychological crisis or individuation process; relates to order/balance/wholeness. → Emergence"""
    normalized_text_zh: str = """"""
    subject: str = "第一节：曼陀罗的普遍性与自发性 (¶713-715)"
    factor_refs: list = ['mandala_universal', 'spontaneous_emergence', 'wholeness_longing']
    
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
        book_id="archetypes_unconscious",
        chapter="",
        l1_anchor="acu_v1.0.0_第一节_曼陀罗的普遍性与自发性___713_715_001_L1",
    )
    version: str = "1.0.0"
