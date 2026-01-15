"""
Auto-generated semantic module for llewellyns_dreams
Generated at: 2025-12-05T13:30:20.386950
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
    semantic_id="ld_v1.0.0_mother_figure_001",
    book_id="llewellyns_dreams",
    engine_id="dream"
)
class MotherFigure(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Mother Figure | Nurturin...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Mother Figure | Nurturing/devouring | Character aspect |
| Positive Mother | Care/nourishment | Healthy self-care |
| Negative Mother | Smothering/control | Self-sabotage |
| Internalized Nurturance | Self-care quality | Not literal mother |

**Source Text** (Paraphrased):
> "Mother figure represents nurturing/devouring character aspect. Positive mother = care, nourishment, unconditional love aspect. Negative mother = smothering, controlling, dependency-creating aspect. Use 3-adjective technique to determine which operating. Dream mother rarely about actual mother but about internalized nurturing (or lack thereof)."
#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Father Figure | Authority/structure | Character aspect |
| Positive Father | Guidance/protection | Healthy discipline |
| Negative Father | Rigid/judgmental | Self-criticism |
| Internalized Authority | Self-discipline | Not literal father |

**Source Text** (Paraphrased):
> "Father figure represents authority/structure character aspect. Positive father = guidance, protection, empowerment, healthy boundaries, supportive authority. Negative father = rigid control, judgment, oppressive authority, harsh criticism, abandonment. Apply 3-adjective method. Rarely about actual father—about internalized authority and structure quality."

**English Paraphrase**:
**Father figure**: **authority/structure character aspect**. **Positive father** = guidance, protection, empowerment, healthy boundaries, supportive authority (adjectives: wise, protective, encouraging). **Negative father** = rigid control, harsh judgment, oppressive authority, critical, abandoning (adjectives: critical, controlling, distant). Apply adjective method. Rarely about actual father—about **internalized authority** and how self provides structure/discipline.

**Complete Chinese Interpretation**:
**父亲人物**：**权威/结构人格面相**。**正面父亲**=指导、保护、赋权、健康边界、支持性权威（形容词：智慧、保护、鼓励）。**负面父亲**=僵化控制、苛刻评判、压迫权威、批判、遗弃（形容词：批判、控制、疏远）。应用形容词法。罕关实际父亲——关于**内化的权威**及自我如何提供结构/纪律。

#### Core Points

- **Authority/Structure Aspect**: Father figure represents authority/structure character aspect.
- **Positive Father**: Guidance, protection, empowerment, healthy boundaries (wise, protective, encouraging).
- **Negative Father**: Rigid control, harsh judgment, oppressive authority (critical, controlling, distant).
- **3-Adjective Method**: Apply adjective method to identify which father aspect active.
- **Internalized Authority**: About how self provides structure/discipline, rarely about actual father.

#### Detailed Explanation

Father figure represents authority/structure character aspect. Positive father = guidance, protection, empowerment, healthy boundaries, supportive authority (adjectives: wise, protective, encouraging). Negative father = rigid control, harsh judgment, oppressive authority, critical, abandoning (adjectives: critical, controlling, distant). Apply the adjective method to identify. Rarely about actual father but about internalized authority and how self provides structure/discipline."""
    normalized_text_zh: str = """"""
    subject: str = "Mother Figure"
    factor_refs: list = ['psych_archetype_father', 'psych_positive_father', 'psych_negative_father', 'psych_internalized_authority']
    
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
        l1_anchor="ld_v1.0.0_mother_figure_001_L1",
    )
    version: str = "1.0.0"
