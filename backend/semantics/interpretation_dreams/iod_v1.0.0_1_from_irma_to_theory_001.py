"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.473099
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
    semantic_id="iod_v1.0.0_1_from_irma_to_theory_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class 1FromIrmaToTheory(SemanticEntry):
    """
    **Source Text**:
"When, after passing through a narrow defile, we suddenly reach a height beyond whi...
    """
    
    original_text: str = """**Source Text**:
"When, after passing through a narrow defile, we suddenly reach a height beyond which the ways part and a rich prospect lies outspread in different directions, it is well to stop for a moment and consider whither we shall first turn our steps. We are in somewhat the same position after we have mastered this first dream interpretation."

"We find ourselves standing in the light of a sudden discovery. The dream is not comparable to the irregular sounds of a musical instrument, which, instead of being played by the hand of a musician, is struck by some external force; the dream is not meaningless, not absurd... it is a perfectly valid psychic phenomenon—actually a wish-fulfilment."

**Key Term Analysis**:

| Term | Definition | Significance |
|------|-----------|---------------|
| Wish Fulfillment | 愿望满足 | Dream's essential function | Central thesis |
| Valid Psychic Phenomenon | 有效心理现象 | Dream has meaning | vs. somatic noise |
| Narrow Defile | 狭窄隘口 | Irma analysis | Breakthrough point |
| Rich Prospect | 丰富前景 | Theory now visible | New territory |

**English Paraphrase (Primary Language)**:

Having analyzed the Irma dream, Freud announces his discovery: **dreams are wish fulfillments**. This is not metaphor but literal claim. The dream is not random neural noise but a **valid psychic phenomenon**—meaningful, purposive, interpretable.

The Irma analysis proved the specimen case. Now Freud must demonstrate the thesis holds **universally**. How can anxiety dreams, punishment dreams, nightmares be wish fulfillments? This is the challenge of Chapter IV. But first, Chapter III establishes the thesis through its **clearest cases**: children's dreams and convenience dreams.

The rhetorical strategy: prove the thesis where it's obvious, then extend to difficult cases.

**Complete Chinese Interpretation (Secondary Language)**:

分析了伊尔玛之梦后，弗洛伊德宣布他的发现：**梦是愿望的满足**。这不是隐喻而是字面主张。梦不是随机的神经噪音，而是**有效的心理现象**——有意义的、有目的的、可解释的。

伊尔玛分析证明了样本案例。现在弗洛伊德必须证明该论题**普遍**成立。焦虑梦、惩罚梦、噩梦如何能是愿望满足？这是第四章的挑战。但首先，第三章通过其**最清晰的案例**确立论题：儿童梦和便利梦。

修辞策略：在显而易见之处证明论题，然后扩展到困难案例。

**Narrative Snippets**:

- `[ns_freud_wish_001]` `[trigger: wish_thesis]` `[factor_trigger: dream_wishfulfillment AND dream_theory AND wish_fulfillment]` `[role: 主干]` The dream is not meaningless or absurd—it is a perfectly valid psychic phenomenon, actually a wish-fulfillment. This is the central thesis of dream interpretation. → Freud Ch.III #Thesis
- `[ns_freud_wish_002]` `[trigger: narrow_defile]` `[factor_trigger: dream_method AND dream_discovery]` `[role: 主干依赖]` After passing through the narrow defile of the Irma analysis, we stand in the light of sudden discovery—a rich prospect lies outspread before us. → Freud Ch.III #Thesis"""
    normalized_text_zh: str = """"""
    subject: str = "1 From Irma to Theory"
    factor_refs: list = []
    
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
        book_id="interpretation_dreams",
        chapter="",
        l1_anchor="iod_v1.0.0_1_from_irma_to_theory_001_L1",
    )
    version: str = "1.0.0"
