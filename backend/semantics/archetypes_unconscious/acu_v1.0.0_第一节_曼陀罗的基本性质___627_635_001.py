"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.559097
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
    semantic_id="acu_v1.0.0_第一节_曼陀罗的基本性质___627_635_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 第一节曼陀罗的基本性质627635(SemanticEntry):
    """
    **原文概要** (¶627-635):

> 曼陀罗是梵语，意为"圆"。在宗教实践和心理学中，它指的是圆形图像，通常包含四分法或其倍数的结构。曼陀罗自发地出现在梦境、幻想和积极想象中。它们代表自性—...
    """
    
    original_text: str = """**原文概要** (¶627-635):

> 曼陀罗是梵语，意为"圆"。在宗教实践和心理学中，它指的是圆形图像，通常包含四分法或其倍数的结构。曼陀罗自发地出现在梦境、幻想和积极想象中。它们代表自性——人格的整体性，包括意识和无意识。曼陀罗的出现通常表示心理整合的需要或过程。

**英文释义**:

曼陀罗 = 梵语"圆"。宗教+心理学意义：圆形图像，四分法结构。自发出现于梦境、幻想、积极想象。代表自性（人格整体，意识+无意识）。出现表示心理整合需要/过程。中心点（bindu）= 自性核心。保护圆 = 对抗分裂。

**完整中文诠释**:

**曼陀罗定义**：
- 梵语"mandala" = 圆
- 宗教实践中：冥想工具、神圣空间
- 心理学中：自性的象征表达

**基本结构**：
- 圆形（保护边界）
- 四分法或其倍数（4、8、12、16等）
- 中心点（bindu）= 自性核心

**心理功能**：
- 代表自性（人格整体）
- 整合意识与无意识
- 提供心理秩序对抗混乱
- 保护圆 = 防止人格分裂

**出现时机**：
- 心理危机或转折点
- 个体化过程中
- 自发出现（非刻意制造）

**核心要点**:
- 曼陀罗 = 圆 = 自性象征
- 四分法是基本结构
- 自发出现于心理转折点
- 功能：整合、保护、秩序

**叙事片段**:
- `[ns_cw9i_X_001]` `[trigger: 曼陀罗定义]` `[factor_trigger: jung_mandala AND jung_self]` `[role: 主干]` 曼陀罗是圆形图像，代表自性——人格整体，自发出现于心理转折点，提供整合与保护。→ ¶627-635"""
    normalized_text_zh: str = """"""
    subject: str = "第一节：曼陀罗的基本性质 (¶627-635)"
    factor_refs: list = ['mandala_definition', 'quaternity_structure', 'protective_circle', 'bindu']
    
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
        l1_anchor="acu_v1.0.0_第一节_曼陀罗的基本性质___627_635_001_L1",
    )
    version: str = "1.0.0"
