"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.469055
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
    semantic_id="iod_v1.0.0_displacement_of_psychic_intens_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class DisplacementOfPsychicIntens(SemanticEntry):
    """
    **Source Text**:
"Another relation, probably no less significant, was foreshadowed in a remark to th...
    """
    
    original_text: str = """**Source Text**:
"Another relation, probably no less significant, was foreshadowed in a remark to the effect that, not only the elements of the dream, but the psychical value of those elements which in the dream thoughts should have been essential, was displaced."

"In the dream-work we have become acquainted with a psychic force which, on the one hand, strips the elements of high psychic value of their intensity, and on the other hand, by means of over-determination, creates new values of elements that have low valence, which new values then reach the dream content."

"It is as if a mental lever had displaced the centre of gravity. Where the emphasis falls in the dream thoughts, it vanishes in the dream; and what is left behind and forms the dream content is only trivial and indifferent."

**Key Term Analysis**:

| Term | Definition | Significance |
|------|-----------|---------------|
| Displacement | Shift of psychic intensity from important to trivial elements | Second major dream-work mechanism |
| Psychic Value/Intensity | Emotional significance attached to thoughts | What gets shifted |
| Lever | Mechanical metaphor for displacement | Illustrates redistribution |
| Centre of Gravity | Location of emotional emphasis | What displacement moves |
| Trivial Elements | Minor details in manifest content | May carry displaced importance |

**English Paraphrase (Primary Language)**:

**Displacement** (Verschiebung) is the second major mechanism of dream-work. Where condensation compresses quantity, displacement redistributes **quality**—specifically, emotional intensity or "psychic value."

Freud describes displacement as a **mental lever** that shifts the "centre of gravity." What matters most in the dream-thoughts becomes **peripheral or absent** in the manifest dream; what is **trivial and indifferent** in thoughts becomes central in the dream. The dreamer wakes obsessing over minor details while the emotionally charged core goes unnoticed.

This mechanism serves **censorship**. If a wish is forbidden, its direct expression would cause anxiety. Displacement transfers the emotional charge to innocuous substitutes, allowing the forbidden thought to pass censorship in disguise. The dreamer experiences emotion about safe objects while the dangerous source remains hidden.

Displacement explains why dreams often seem **emotionally disproportionate**: intense feeling about trivial matters, indifference to what should be significant. This disproportion is diagnostic—it signals displacement and points toward hidden meaning.

**Complete Chinese Interpretation (Secondary Language)**:

**移置**（Verschiebung）是梦的工作的第二个主要机制。凝缩压缩数量，而移置重新分配**质量**——具体来说，是情感强度或"心理价值"。

弗洛伊德将移置描述为一个**心理杠杆**，移动"重心"。在梦思中最重要的东西在显性梦中变得**边缘化或缺失**；在思想中**微不足道、无关紧要**的东西在梦中变得中心化。梦者醒来时纠结于细枝末节，而情感核心却未被注意。

这一机制服务于**审查**。如果一个愿望被禁止，其直接表达会引起焦虑。移置将情感电荷转移到无害的替代物上，使被禁止的思想得以伪装通过审查。梦者对安全对象体验情感，而危险的来源仍然隐藏。

移置解释了为什么梦往往看起来**情感不成比例**：对琐事的强烈感受，对本应重要之事的漠然。这种不成比例具有诊断意义——它标示着移置，指向隐藏的含义。

**Core Points**:

- Displacement = shift of emotional intensity between elements
- Lever metaphor: centre of gravity moves
- Important thoughts → peripheral in dream; trivial thoughts → central
- Serves censorship by disguising emotional source
- Diagnostic sign: emotional disproportion in dreams

**Detailed Explanation**:

Displacement and condensation work together but do different work. Condensation handles **content** (many thoughts → one image); displacement handles **emotion** (intensity shifted between elements). A dream may condense three people into one figure AND dream_displace the emotional charge from one person to another.

The **censorship function** is crucial. Displacement is a **defense mechanism** operating during sleep. The psychic censor cannot allow direct expression of forbidden wishes; displacement provides camouflage by attaching intense feeling to innocent objects.

**Interpretive implication**: When analyzing dreams, one must **not trust the emotional distribution**. The trivial detail the dreamer barely mentions may carry the most significance. The dramatic scene described with excitement may be a decoy. The analyst follows the rule: "Where there is smoke, there is fire"—but the fire may be far from the smoke.

This connects to **free association**: the dreamer must follow associations from every element, especially the seemingly trivial ones. Displacement means the manifest emotional structure is misleading.

**Textual Criticism & Variant Analysis (Bilingual)**:

- **English**: "Displacement" captures the spatial metaphor of shifting. The German "Verschiebung" emphasizes the sliding/shoving aspect—something pushed aside.
- **中文**: "移置"准确传达了空间移动的隐喻。德语"Verschiebung"强调滑动/推移的方面——某物被推到一边。另一译法"转移"也常见，但"移置"更突出位置改变。

**Narrative Snippets**:

- `[ns_freud_dw_007]` `[trigger: displacement_mechanism]` `[factor_trigger: psychic_intensity AND dream_displacement]` `[role: 主干]` It is as if a mental lever had displaced the centre of gravity. Where the emphasis falls in the dream thoughts, it vanishes in the dream; what is left behind is only trivial and indifferent. → Freud Ch.VI #Displacement
- `[ns_freud_dw_008]` `[trigger: displacement_censorship]` `[factor_trigger: dream_displacement AND dream_censorship]` `[role: 主干依赖]` Displacement strips elements of high psychic value of their intensity, and by means of over-determination creates new values for elements of low valence. → Freud Ch.VI #Displacement
- `[ns_freud_dw_009]` `[trigger: emotional_disproportion]` `[factor_trigger: emotional_disproportion AND dream_displacement]` `[role: 条件分支]` Dreams often seem emotionally disproportionate: intense feeling about trivial matters, indifference to what should be significant. This disproportion signals displacement. → Freud Ch.VI #Displacement
- `[ns_freud_dw_022]` `[trigger: trivial_significance]` `[factor_trigger: dream_displacement AND dream_interpretation]` `[role: 条件分支]` The trivial detail the dreamer barely mentions may carry the most significance—the analyst follows: "where there is smoke, there is fire" but the fire may be far from the smoke. → Freud Ch.VI #Displacement"""
    normalized_text_zh: str = """"""
    subject: str = "Displacement of Psychic Intensity"
    factor_refs: list = ['displacement', 'psychic_intensity', 'new_candidate', 'emotional_disproportion']
    
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
        l1_anchor="iod_v1.0.0_displacement_of_psychic_intens_001_L1",
    )
    version: str = "1.0.0"
