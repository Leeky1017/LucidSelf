"""
Auto-generated semantic module for llewellyns_dreams
Generated at: 2025-12-05T13:30:20.386885
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
    semantic_id="ld_v1.0.0_flying_001",
    book_id="llewellyns_dreams",
    engine_id="dream"
)
class Flying(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Flying | Transcendence/f...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Flying | Transcendence/freedom | Universal dream |
| Effortless/Struggling | Transcendence quality | Achieved/obstacles |
| Elevated Perspective | Higher viewpoint | Above limitations |
| Spiritual Awakening | Consciousness expansion | Liberation |

**Source Text** (Paraphrased):
> "Flying represents transcendence, freedom, gaining perspective. Rising above limitations, seeing from higher viewpoint. Can indicate spiritual awakening or desire to escape earthly concerns. Effortless flight = spiritual freedom; struggling flight = trying to transcend but obstacles remain."

**English Paraphrase**:
**Flying**: **transcendence, freedom, perspective**. Rising above limitations, seeing from higher viewpoint. **Effortless flight** = spiritual freedom, transcendence achieved, liberation; **Struggling flight** = attempting transcendence but obstacles/resistance remain; **Flight height** matters = higher = more spiritual/abstract perspective. Can indicate: Spiritual awakening, Desire to escape problems, Gaining new perspective, Transcending ego limitations.

**Complete Chinese Interpretation**:
**飞行**：**超越、自由、视角**。超越限制，从更高视角看。**轻松飞行**=灵性自由、达成超越、解放；**挣扎飞行**=尝试超越但障碍/阻力仍在；**飞行高度**重要=更高=更灵性/抽象视角。可指示：灵性觉醒、渴望逃离问题、获得新视角、超越小我限制。

#### Core Points

- **Transcendence/Freedom**: Flying represents transcendence, freedom, gaining perspective.
- **Effortless vs Struggling**: Effortless flight = spiritual freedom achieved; struggling = obstacles remain.
- **Height = Perspective Level**: Higher flight = more spiritual/abstract perspective.
- **Universal Dream**: One of the most common cross-cultural dream experiences.
- **Spiritual Awakening**: Can indicate consciousness expansion, desire to escape limitations.

#### Detailed Explanation

Flying represents transcendence, freedom, and gaining perspective. It symbolizes rising above limitations and seeing from a higher viewpoint. Effortless flight = spiritual freedom, transcendence achieved, liberation. Struggling flight = attempting transcendence but obstacles/resistance remain. Flight height matters: higher = more spiritual/abstract perspective. Flying dreams can indicate spiritual awakening, desire to escape problems, gaining new perspective, or transcending ego limitations."""
    normalized_text_zh: str = """"""
    subject: str = "Flying"
    factor_refs: list = ['dream_symbol_flying', 'dream_flight_ease', 'psych_elevated_perspective', 'psych_spiritual_awakening']
    
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
        l1_anchor="ld_v1.0.0_flying_001_L1",
    )
    version: str = "1.0.0"
