"""
Auto-generated semantic module for llewellyns_dreams
Generated at: 2025-12-05T13:30:20.386931
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
    semantic_id="ld_v1.0.0_chase_being_chased_001",
    book_id="llewellyns_dreams",
    engine_id="dream"
)
class ChaseBeingChased(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Being Chased | Shadow av...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Being Chased | Shadow avoidance | Anxiety pattern |
| Pursuer Identity | What avoided | Monster/authority/animal |
| Turning to Face | Integration moment | Confrontation |
| Endless Chase | Continued avoidance | Unresolved |

**Source Text** (Paraphrased):
> "Being chased represents avoiding confrontation with shadow aspects. What chases you = part of self you run from. Common anxiety dream = unresolved issue demanding attention. Turning to face pursuer = shadow integration beginning. Never catching what you chase = pursuing aspect of self not yet ready to embody."

**English Paraphrase**:
**Being chased**: **avoiding confrontation** with shadow aspects. What chases you = part of self you run from (use adjectives to identify). **Pursuer identity** matters: Monster = feared shadow, Authority figure = internalized judgment, Animal = instinct rejected. **Turning to face** = integration beginning; **Running endlessly** = continued avoidance. **Chasing others** (less common) = pursuing aspect not yet ready to embody.

**Complete Chinese Interpretation**:
**被追逐**：**逃避对抗**阴影面相。追你之物=你逃离的自我部分（用形容词识别）。**追逐者身份**重要：怪物=被恐惧阴影、权威人物=内化评判、动物=被拒本能。**转身面对**=整合开始；**无尽奔跑**=持续逃避。**追逐他人**（较少见）=追求尚未准备体现的面相。

#### Core Points

- **Shadow Avoidance**: Being chased represents avoiding confrontation with shadow aspects.
- **Pursuer = Self-Part**: What chases you = part of self you run from (use adjectives to identify).
- **Pursuer Identity**: Monster = feared shadow; Authority = internalized judgment; Animal = rejected instinct.
- **Turning to Face**: Confronting pursuer = shadow integration beginning.
- **Common Anxiety Dream**: One of the most common stress-response dreams.

#### Detailed Explanation

Being chased represents avoiding confrontation with shadow aspects. What chases you = part of self you run from (use adjectives to identify). Pursuer identity matters: Monster = feared shadow, Authority figure = internalized judgment, Animal = instinct rejected. Turning to face the pursuer = shadow integration beginning. Running endlessly = continued avoidance. Chasing others (less common) = pursuing aspect of self not yet ready to embody."""
    normalized_text_zh: str = """"""
    subject: str = "Chase/Being Chased"
    factor_refs: list = ['dream_symbol_chased', 'psych_shadow_avoidance', 'dream_pursuer_identity', 'psych_turning_to_face']
    
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
        l1_anchor="ld_v1.0.0_chase_being_chased_001_L1",
    )
    version: str = "1.0.0"
