"""
Auto-generated semantic module for llewellyns_dreams
Generated at: 2025-12-05T13:30:20.386805
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
    semantic_id="ld_v1.0.0_masculine_feminine_principles_001",
    book_id="llewellyns_dreams",
    engine_id="dream"
)
class MasculineFemininePrinciples(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Masculine/Feminine | Beh...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Masculine/Feminine | Behavioral modalities | Not gender |
| Doing vs Being | Action vs process | Yang/Yin |
| Animus/Anima | Contra-gender aspects | Integration |
| Dynamic Balance | Harmonious interplay | Wholeness |

**Source Text** (Paraphrased):
> "Masculine and feminine principles are behavioral modalities, not gender. Masculine = doing, action, decisiveness, goal-orientation. Feminine = being, creativity, nurturance, receptivity. Wholeness requires balanced expression. Dream work reveals imbalance: over-masculine = burnout, over-feminine = passivity. Both principles exist in all people regardless of biological sex."

**English Paraphrase**:
**Masculine/Feminine**: behavioral modes not gender identity. **Masculine** = DOING (action, decisiveness, linear thinking, Yang). **Feminine** = BEING (creativity, receptivity, circular thinking, Yin). **Integration = wholeness**: balanced psyche. **Over-masculine** = driven/burned out; **Over-feminine** = passive/overwhelmed. Dreams diagnose imbalance and invite correction.

**Complete Chinese Interpretation**:
**阴阳原则**：行为模式非性别认同。**阳性**=行动（行动、决断、线性思维、阳）。**阴性**=存在（创造、接纳、循环思维、阴）。**整合=完整性**：平衡心灵。**过阳**=驱动/倦怠；**过阴**=被动/淹没。梦诊断失衡并邀请纠正。

#### Core Points

- **Behavioral Modalities Not Gender**: Masculine and feminine are behavioral modes, not gender identity.
- **Doing vs Being**: Masculine = doing/action/linear; Feminine = being/creativity/circular.
- **Both Exist in All**: Both principles exist in all people regardless of biological sex.
- **Imbalance Diagnosis**: Over-masculine = burnout; Over-feminine = passivity—dreams diagnose imbalance.
- **Integration = Wholeness**: Balanced expression of both principles creates psychic wholeness.

#### Detailed Explanation

Masculine and feminine principles are behavioral modalities, not gender. Masculine = doing, action, decisiveness, goal-orientation (Yang). Feminine = being, creativity, nurturance, receptivity (Yin). Wholeness requires balanced expression of both. Dream work reveals imbalance: over-masculine leads to driven/burned out states; over-feminine leads to passive/overwhelmed states. Both principles exist in all people regardless of biological sex. Dreams diagnose the current balance and invite correction toward integration."""
    normalized_text_zh: str = """"""
    subject: str = "Masculine/Feminine Principles"
    factor_refs: list = ['psych_masc_fem_principle', 'psych_doing_being', 'psych_archetype_animusanima', 'psych_dynamic_balance']
    
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
        l1_anchor="ld_v1.0.0_masculine_feminine_principles_001_L1",
    )
    version: str = "1.0.0"
