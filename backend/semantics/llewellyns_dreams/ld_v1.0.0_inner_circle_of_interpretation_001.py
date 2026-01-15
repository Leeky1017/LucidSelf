"""
Auto-generated semantic module for llewellyns_dreams
Generated at: 2025-12-05T13:30:20.386838
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
    semantic_id="ld_v1.0.0_inner_circle_of_interpretation_001",
    book_id="llewellyns_dreams",
    engine_id="dream"
)
class InnerCircleOfInterpretation(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Inner Circle | Self-refl...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Inner Circle | Self-reflection only | All as self |
| Outer vs Inner | Others vs self-aspects | Interpretation choice |
| Empowering Principle | Focus on self | Can change |
| Self-Revelation | Maximum insight | Inner work priority |

**Source Text** (Paraphrased):
> "Lennox's method works only from the perspective of self-reflection—all dream elements as aspects of dreamer's consciousness. This does not negate outer relationships exist, but prioritizes inner work for maximum self-revelation. Dreams may reflect relationships, but their best value lies in self-investigation. Dream about difficult spouse = not spouse analysis but self-aspect exploration. What does 'difficult spouse' represent in my psyche? This inner circle keeps interpretation empowering rather than projecting responsibility outward."

**English Paraphrase**:
**Inner circle of interpretation**: Lennox framework—work **only from self-reflection perspective**, all elements as consciousness aspects. Does not deny outer reality but **prioritizes inner work** for maximum self-revelation. Example: Dream about difficult spouse ≠ analysis of spouse (outer circle) = self-aspect exploration (inner circle). "What does 'difficult spouse' represent in my psyche?" **Empowering principle**: Keeps interpretation focused on what dreamer can change (self) rather than projecting onto others (disempowering).

**Complete Chinese Interpretation**:
**内圈诠释**：Lennox框架——仅从**自我反思视角**工作，所有元素作为意识面相。不否定外部现实但**优先内在工作**最大自我揭示。例：梦困难配偶≠分析配偶（外圈）=自我面相探索（内圈）。"'困难配偶'在我心理代表什么？"**赋权原则**：保持诠释聚焦于梦者可改变者（自我）而非投射于他人（去权）。

#### Core Points

- **Self-Reflection Only**: Lennox's method works only from the perspective of self-reflection—all elements as consciousness aspects.
- **Inner Work Priority**: Does not negate outer reality but prioritizes inner work for maximum self-revelation.
- **Empowering Principle**: Keeps interpretation focused on what dreamer can change (self) rather than projecting outward.
- **Self-Aspect Exploration**: Dream about difficult spouse = not spouse analysis but "What does this represent in my psyche?"
- **Projection Withdrawal**: Recognizing outer figures as self-aspects, not literal others.

#### Detailed Explanation

Lennox's method works only from the perspective of self-reflection—all dream elements as aspects of the dreamer's consciousness. This does not negate that outer relationships exist, but prioritizes inner work for maximum self-revelation. Dreams may reflect relationships, but their best value lies in self-investigation. Dream about difficult spouse = not spouse analysis (outer circle) but self-aspect exploration (inner circle): "What does 'difficult spouse' represent in my psyche?" This inner circle keeps interpretation empowering—focused on what the dreamer can change (self)—rather than projecting responsibility outward (disempowering)."""
    normalized_text_zh: str = """"""
    subject: str = "Inner Circle of Interpretation"
    factor_refs: list = ['dream_inner_circle', 'psych_self_reflection', 'psych_empowerment', 'psych_projection_withdrawal']
    
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
        l1_anchor="ld_v1.0.0_inner_circle_of_interpretation_001_L1",
    )
    version: str = "1.0.0"
