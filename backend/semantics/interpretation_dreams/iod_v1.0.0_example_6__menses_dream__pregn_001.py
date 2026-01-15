"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.460965
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
    semantic_id="iod_v1.0.0_example_6__menses_dream__pregn_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class Example6MensesDreamPregn(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Representation by Opposite | Wish via contradiction | Key mechanism |
| Symbolic Reversal | Menses = no pregnancy | Denial wish |
| Negation | Signals opposite truth | Interpretive clue |
| Reaction Formation | Unacceptable→opposite | Defense mechanism |

**Source Text** (Friend's wife):
"My wife asked me to tell you that she dreamt yesterday that she was having her menses."

**Analysis**:
- **Manifest content**: Having menstrual period
- **True meaning**: Menses have **stopped** (opposite of manifest)
- **Latent wish**: Enjoy freedom longer before "discomforts of motherhood"
- **Symbolic reversal**: Dream represents wish by its **opposite**
- **Social function**: "Clever way of giving notice of her first pregnancy"

**Key Mechanism**: **Representation by Opposite** (反向表征)
- Dream can express wish through its **contradiction**
- Saying "menses" = denial of pregnancy = **wish not to be pregnant yet**
- **Negation in dreams**: Often signals the opposite truth
- Related to **reaction formation**: Unconscious transforms unacceptable wish into its opposite

**Complete Chinese Interpretation (Secondary Language)**:

“月经梦”看似再平常不过：一位朋友转述妻子的梦，说她梦见自己在来月经。如果按显梦理解，只是一次平常的生理现象；但在具体语境中，这位妻子正好处在可能怀孕的阶段，而事实上，她已经停经并确认怀孕。于是，这个梦的真正含义反而是：**“我并没有怀孕（我还在来月经）”**——即以表面上的否定，表达对现实状态的抗拒与拖延愿望。

在心理层面，这个梦揭示了所谓**反向表征**机制：当某个愿望在意识中难以被承认时，无意识可能通过说出它的“反面”来间接表达。梦里说“我正在来月经”，其潜台词恰恰是“我事实上没有来月经，而且我在意这件事”；在这之下，又叠加着更细腻的情感——一方面，对成为母亲的期待与社会性兴奋，另一方面，对即将失去自由、身体负担加重、身份角色被改写的隐秘抗拒。

从社会功能上看，这个梦也被弗洛伊德戏称为一种“巧妙的怀孕通知方式”：以看似否定的方式，向他人暗示自己已进入全新人生阶段。更广泛地说，这一例子说明：**梦中的否定、相反陈述往往是解读时最需要重视的线索**，它们常常不是简单的“不”，而是反向形成、防御和愿望交织后的复杂产物。

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Menses Dream: Representation by opposite. Manifest=having period, Latent=pregnancy/no period. Symbolic reversal expresses wish not to be pregnant yet. Negation in dreams signals opposite truth.
- **中文**: 月经梦:反向表征。显梦=来月经,潜梦=怀孕/没来月经。象征逆转表达不想怀孕的愿望。梦中否定信号相反真理。

**Narrative Snippets**:
- `[ns_freud_ex_016]` `[trigger: representation_opposite]` `[factor_trigger: dream_work_reversal]` `[role: 主干]` Menses Dream: wish expressed through contradiction; manifest opposite of latent. → Example
- `[ns_freud_ex_017]` `[trigger: symbolic_reversal]` `[factor_trigger: dream_work_reversal AND symbolism]` `[role: 条件分支]` Menses = denial of pregnancy = wish not to be pregnant yet. → Mechanism
- `[ns_freud_ex_018]` `[trigger: negation_clue]` `[factor_trigger: dream_work_reversal AND interpretation]` `[role: 条件分支]` Negation in dreams often signals opposite truth; key interpretive clue. → Principle"""
    normalized_text_zh: str = """"""
    subject: str = "Example 6: Menses Dream (Pregnancy Announcement)"
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
        l1_anchor="iod_v1.0.0_example_6__menses_dream__pregn_001_L1",
    )
    version: str = "1.0.0"
