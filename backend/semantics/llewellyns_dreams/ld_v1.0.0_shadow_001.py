"""
Auto-generated semantic module for llewellyns_dreams
Generated at: 2025-12-05T13:30:20.386792
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
    semantic_id="ld_v1.0.0_shadow_001",
    book_id="llewellyns_dreams",
    engine_id="dream"
)
class Shadow(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Shadow | Dark/rejected a...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Shadow | Dark/rejected aspects | Demanding integration |
| Nightmare as Invitation | Dark dreams = growth | Not punishment |
| Contrary-to-Nature | Shadow signals | Wrong gender/color |
| Unlived Potential | Positive in shadow | Paradox of shadow |

**Source Text** (Paraphrased):
> "Shadow contains dark, rejected, socially unacceptable aspects relegated to unconscious. Murderous rage, shame, forbidden desires—qualities incompatible with self-image pushed into shadow. Nightmares and dark dreams are shadow calling for integration. Dreams in darkness, dangerous settings, or 'contrary-to-nature' elements signal shadow. Exploration, though frightening, expands wisdom. Shadow is not evil but unlived potential—contains suppressed creativity and power alongside rage/shame."

**English Paraphrase**:
**Shadow**: dark/rejected aspects in unconscious. Contains socially unacceptable impulses (rage, greed, lust), shameful qualities (weakness, dependence), forbidden desires, opposite-gender aspects. **Nightmare = shadow's voice**—invitation to integration not punishment. **Shadow signals**: darkness settings, danger/threat, contrary-to-nature features. **Paradox**: Shadow contains not only "negative" but **unlived positive potential**—creativity, power, passion suppressed alongside rage/shame.

**Complete Chinese Interpretation**:
**阴影**：黑暗/被拒面向在无意识中。包含社会不可接受冲动（暴怒、贪婪、欲望）、羞耻品质（软弱、依赖）、禁忌欲望、异性面向。**噩梦=阴影之声**——整合邀请非惩罚。**阴影信号**：黑暗场景、危险/威胁、反自然特征。**悖论**：阴影不仅含"负面"还有**未活出正面潜能**——创造力、力量、激情与暴怒/羞耻一道被压抑。

#### Core Points

- **Dark/Rejected Aspects**: Shadow contains socially unacceptable impulses (rage, greed, lust), shameful qualities, forbidden desires.
- **Nightmare as Invitation**: Nightmares and dark dreams are shadow calling for integration—growth opportunity, not punishment.
- **Contrary-to-Nature Signals**: Darkness settings, danger/threat, contrary-to-nature features signal shadow presence.
- **Unlived Positive Potential**: Paradox—shadow contains not only "negative" but unlived creativity, power, passion.
- **Integration Expands Wisdom**: Exploration of shadow, though frightening, expands wisdom and wholeness.

#### Detailed Explanation

Shadow contains dark, rejected, socially unacceptable aspects relegated to the unconscious. Murderous rage, shame, forbidden desires—qualities incompatible with self-image are pushed into shadow. Nightmares and dark dreams are shadow calling for integration—an invitation to growth, not punishment. Dreams in darkness, dangerous settings, or with "contrary-to-nature" elements signal shadow presence. The paradox is that shadow contains not only "negative" qualities but unlived positive potential—creativity, power, passion suppressed alongside rage and shame. Shadow is not evil but unintegrated, demanding acknowledgment for wholeness."""
    normalized_text_zh: str = """"""
    subject: str = "Shadow"
    factor_refs: list = ['psych_archetype_shadow', 'dream_nightmare_invitation', 'dream_contrary_nature', 'psych_unlived_potential']
    
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
        l1_anchor="ld_v1.0.0_shadow_001_L1",
    )
    version: str = "1.0.0"
