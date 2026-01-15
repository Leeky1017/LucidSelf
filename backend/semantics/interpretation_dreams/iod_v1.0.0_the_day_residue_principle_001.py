"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.475488
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
    semantic_id="iod_v1.0.0_the_day_residue_principle_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class TheDayResiduePrinciple(SemanticEntry):
    """
    **Source Text**:
"If I now consult my own experience concerning the source of the elements which app...
    """
    
    original_text: str = """**Source Text**:
"If I now consult my own experience concerning the source of the elements which appear in the dream, I must at once express the opinion that some reference to the experiences of the day which has most recently passed is to be found in every dream."

"I am, therefore, of the opinion that the stimulus for every dream is to be found among those experiences 'upon which one has not yet slept' for a night."

"There are three peculiarities of recollection in dreams: 1. That the dream distinctly prefers impressions of the few days preceding; 2. That it makes its selection according to principles other than those of our waking memory, in that it recalls not what is essential and important, but what is subordinate and disregarded; 3. That it has at its disposal the earliest impressions of our childhood."

**Key Term Analysis**:

| Term | Definition | Significance |
|------|-----------|---------------|
| Day Residue | Material from the day preceding the dream | Primary dream stimulus |
| Recent Impressions | Experiences from past 24-48 hours | Trigger for dream formation |
| Indifferent Material | Trivial, overlooked experiences | Preferred by dream-work |
| Dream Stimulus | The trigger that sets off dream formation | Entry point for analysis |
| Not Yet Slept Upon | Experiences requiring psychic processing | Why recent matters |

**English Paraphrase (Primary Language)**:

Freud establishes a fundamental **empirical principle**: every dream contains reference to experiences from the **preceding day**. This "day residue" (Tagesrest) is so reliable that analysts can begin interpretation by asking: "What happened yesterday?"

But the dream's selection is **counterintuitive**: it prefers the **trivial and overlooked** rather than the important and memorable. A patient may dream about a briefly glimpsed book cover rather than a major life decision. This "indifferent material" serves as a **vehicle** for deeper concerns—its very insignificance makes it useful for disguise.

The principle that dreams draw from material "upon which one has not yet slept" suggests dreams serve a **processing function**. The psyche cannot rest until recent experiences have been integrated—dreams are part of this integration.

Three peculiarities of dream memory:
1. **Temporal preference**: Recent over remote (but remote can connect via association)
2. **Value inversion**: Trivial over important
3. **Childhood access**: Earliest memories available

**Complete Chinese Interpretation (Secondary Language)**:

弗洛伊德确立了一个基本的**经验原则**：每个梦都包含对**前一天**经历的参照。这种"日间残余"（Tagesrest）如此可靠，以至于分析师可以从询问"昨天发生了什么？"开始释梦。

但梦的选择是**反直觉的**：它偏好**琐碎和被忽视的**而非重要和值得记忆的。患者可能梦到一眼瞥见的书封面，而非重大人生决定。这种"无关紧要的材料"作为更深层关切的**载体**——其无足轻重恰恰使其有利于伪装。

梦从"尚未被睡过"的材料中提取的原则表明，梦服务于**处理功能**。心灵无法安息直到近期经验被整合——梦是这种整合的一部分。

梦的记忆三大特点：
1. **时间偏好**：近期优于远期（但远期可通过联想连接）
2. **价值反转**：琐碎优于重要
3. **童年通道**：最早记忆可被调用

**Core Points**:

- Every dream contains day residue (past 24 hours)
- Dream prefers trivial/indifferent material over significant
- Value inversion: what waking ignores, dream selects
- Day residue = vehicle for deeper unconscious content
- "Not yet slept upon" = requiring psychic processing
- Childhood memories also accessible through association chains

**Detailed Explanation**:

The **day residue principle** has major clinical utility. When analyzing dreams, always start with: "What happened yesterday?" The trivial detail that triggered the dream serves as an **associative bridge** to deeper material.

The preference for **indifferent material** is strategic. If dreams used emotionally charged recent events directly, the censor would block them. Instead, dreams select neutral fragments that can **carry** emotional charge from elsewhere. The book cover glimpsed is neutral—but it connects associatively to charged material about education, ambition, or a specific person.

**Value inversion** means analysts must not dismiss trivial dream elements. The peripheral detail the dreamer barely mentions may be the key—its very "unimportance" made it useful to the dream-work.

The **childhood access** peculiarity explains why dreams can resurrect memories believed lost. Early experiences remain in psychic archives; dreams can reach them when current experiences activate connecting associations.

**Textual Criticism & Variant Analysis (Bilingual)**:

- **English**: "Day residue" (German: Tagesrest) captures the idea of leftover material requiring processing. Some translators use "day's residues" (plural) to emphasize multiple fragments.
- **中文**: "日间残余"保留了需要处理的剩余材料概念。有时译为"当日残留"或"白天残渣"，后者更突出未消化的特征。

**Narrative Snippets**:

- `[ns_freud_src_001]` `[trigger: day_residue]` `[factor_trigger: dream_day_residue AND day_residue AND dream_formation AND displacement]` `[role: 主干]` Some reference to the experiences of the day which has most recently passed is to be found in every dream—the stimulus for every dream is found among experiences upon which one has not yet slept. → Freud Ch.V #Sources
- `[ns_freud_src_002]` `[trigger: indifferent_material]` `[factor_trigger: indifferent_material AND dream_displacement]` `[role: 主干依赖]` The dream makes its selection according to principles other than waking memory—it recalls not what is essential and important, but what is subordinate and disregarded. → Freud Ch.V #Sources
- `[ns_freud_src_003]` `[trigger: value_inversion]` `[factor_trigger: dream_day_residue AND value_inversion]` `[role: 条件分支]` Trivial day residue serves as vehicle for deeper concerns—its very insignificance makes it useful for the dream-work's disguise function. → Freud Ch.V #Sources
- `[ns_freud_src_010]` `[trigger: three_peculiarities]` `[factor_trigger: dream_memory AND dream_selection AND association_chain]` `[role: 条件分支]` Three peculiarities of dream memory: temporal preference (recent), value inversion (trivial over important), and childhood access (earliest memories available). → Freud Ch.V #Sources"""
    normalized_text_zh: str = """"""
    subject: str = "The Day Residue Principle"
    factor_refs: list = ['day_residue', 'indifferent_material', 'value_inversion', 'new_candidate']
    
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
        l1_anchor="iod_v1.0.0_the_day_residue_principle_001_L1",
    )
    version: str = "1.0.0"
