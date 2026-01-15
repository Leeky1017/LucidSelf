"""
Auto-generated semantic module for llewellyns_dreams
Generated at: 2025-12-05T13:30:20.386958
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
    semantic_id="ld_v1.0.0_fire_001",
    book_id="llewellyns_dreams",
    engine_id="dream"
)
class Fire(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Fire | Passion/transform...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Fire | Passion/transformation | Dual nature |
| Controlled Fire | Creative passion | Life-giving |
| Uncontrolled Fire | Destructive rage | Consuming |
| Purification | Burning away old | Transformation |

**Source Text** (Paraphrased):
> "Fire represents passion, transformation, destruction/creation duality. Controlled fire = creative passion, vital energy, transformation. Uncontrolled fire = destructive rage, being consumed, loss of control. Fire purifies through burning away old. Warmth vs burning = passion's expression (life-giving vs destructive)."

**English Paraphrase**:
**Fire**: **passion, transformation, destruction/creation**. **Controlled fire** = creative passion, vital energy, focused transformation, warmth, illumination. **Uncontrolled fire** = destructive rage, being consumed, wildfire of emotions, loss of control. **Fire's dual nature**: Creates (forge, hearth) and destroys (wildfire). **Purification** through burning away old/unnecessary. **Warmth vs burning** = passion expression (life-giving vs destructive).

**Complete Chinese Interpretation**:
**火**：**激情、转化、毁灭/创造**。**受控火**=创造激情、生命能量、聚焦转化、温暖、照明。**失控火**=破坏性愤怒、被吞噬、情绪野火、失控。**火的双重本质**：创造（熔炉、壁炉）与毁灭（野火）。**净化**通过燃烧旧的/不必要者。**温暖vs灼伤**=激情表达（赋予生命vs破坏）。

#### Core Points

- **Passion/Transformation**: Fire represents passion, transformation, destruction/creation duality.
- **Controlled vs Uncontrolled**: Controlled = creative passion; Uncontrolled = destructive rage.
- **Dual Nature**: Fire creates (forge, hearth) and destroys (wildfire).
- **Purification**: Burning away old/unnecessary for transformation.
- **Warmth vs Burning**: Life-giving passion vs consuming destruction.

#### Detailed Explanation

Fire represents passion, transformation, and the destruction/creation duality. Controlled fire = creative passion, vital energy, focused transformation, warmth, illumination. Uncontrolled fire = destructive rage, being consumed, wildfire of emotions, loss of control. Fire's dual nature: it creates (forge, hearth) and destroys (wildfire). Purification happens through burning away old/unnecessary. Warmth vs burning = passion expression (life-giving vs destructive)."""
    normalized_text_zh: str = """"""
    subject: str = "Fire"
    factor_refs: list = ['dream_symbol_fire', 'dream_fire_control', 'dream_fire_purification', 'dream_fire_warmth']
    
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
        book_id="llewellyns_dreams",
        chapter="",
        l1_anchor="ld_v1.0.0_fire_001_L1",
    )
    version: str = "1.0.0"
