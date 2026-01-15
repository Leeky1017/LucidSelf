"""
Auto-generated semantic module for llewellyns_dreams
Generated at: 2025-12-05T13:30:20.386922
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
    semantic_id="ld_v1.0.0_animals__instinctual_energies_001",
    book_id="llewellyns_dreams",
    engine_id="dream"
)
class AnimalsInstinctualEnergies(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Animals | Instinctual en...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Animals | Instinctual energies | Archetypal patterns |
| Snake | Transformation/sexuality | Healing/danger |
| Bird | Freedom/transcendence | Spirituality |
| Animal Behavior | Energy expression | Aggressive/friendly |

**Source Text** (Paraphrased):
> "Animals represent instinctual energies and archetypal patterns. Each animal carries specific symbolic meaning: Snake = transformation/sexuality/healing/danger, Bird = freedom/spirituality/transcendence, Dog = loyalty/companionship/unconditional love, Cat = independence/feminine mystery/intuition, Bear = power/mother protection/hibernation. Animal behavior in dream shows how that instinctual energy expressing in psyche."

**English Paraphrase**:
**Animals**: **instinctual energies and archetypal patterns**. Key animals: **Snake** = transformation, sexuality, healing, kundalini energy (also danger if feared); **Bird** = freedom, spirituality, transcendence, soul; **Dog** = loyalty, companionship, unconditional love, faithfulness; **Cat** = independence, feminine mystery, intuition, self-sufficiency; **Bear** = power, mother protection, hibernation/retreat, strength. **Animal behavior** = how that energy expressing (aggressive = instinct threatening, friendly = instinct integrated).

**Complete Chinese Interpretation**:
**动物**：**本能能量与原型模式**。关键动物：**蛇**=转化、性、疗愈、昆达里尼能量（若被恐惧也危险）；**鸟**=自由、灵性、超越、灵魂；**狗**=忠诚、陪伴、无条件爱、忠实；**猫**=独立、女性神秘、直觉、自给自足；**熊**=力量、母亲保护、冬眠/退隐、强度。**动物行为**=该能量如何表达（攻击性=本能威胁、友好=本能整合）。

#### Core Points

- **Instinctual Energies**: Animals represent instinctual energies and archetypal patterns.
- **Specific Meanings**: Each animal carries specific symbolic meaning (snake=transformation, bird=freedom).
- **Animal Behavior**: How the animal behaves shows how that instinctual energy is expressing.
- **Integration Indicator**: Friendly animal = instinct integrated; threatening = instinct feared/rejected.
- **Cross-cultural**: Animals as symbols appear across all cultures with similar meanings.

#### Detailed Explanation

Animals represent instinctual energies and archetypal patterns. Each animal carries specific symbolic meaning: Snake = transformation/sexuality/healing/kundalini energy (also danger if feared); Bird = freedom/spirituality/transcendence; Dog = loyalty/companionship/unconditional love; Cat = independence/feminine mystery/intuition; Bear = power/mother protection/hibernation. Animal behavior in the dream shows how that instinctual energy is expressing in the psyche: friendly = integrated, aggressive = feared/rejected."""
    normalized_text_zh: str = """"""
    subject: str = "Animals (Instinctual Energies)"
    factor_refs: list = ['dream_symbol_animal', 'dream_symbol_snake', 'dream_symbol_bird', 'dream_symbol_dog', 'dream_symbol_cat', 'dream_symbol_bear']
    
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
        l1_anchor="ld_v1.0.0_animals__instinctual_energies_001_L1",
    )
    version: str = "1.0.0"
