"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.477405
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
    semantic_id="iod_v1.0.0_1_free_association_technique_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class 1FreeAssociationTechnique(SemanticEntry):
    """
    **Source Text**:
"I have come to think differently. I must insist that the dream actually has signif...
    """
    
    original_text: str = """**Source Text**:
"I have come to think differently. I must insist that the dream actually has significance, and that a scientific procedure in dream interpretation is possible."

"For this a certain psychic preparation of the patient is necessary. The double effort is made with him: to stimulate his attention for his psychic perceptions and to eliminate the critique with which he is ordinarily in the habit of viewing the thoughts which come to the surface."

"He must be told that the success of the psychoanalysis depends upon his noticing and telling everything that passes through his mind, and that he must not allow himself to suppress one idea because it seems unimportant or irrelevant, or another because it seems nonsensical."

"The first step now teaches us that not the dream as a whole, but only the parts of its contents separately, may be made the object of our attention. If I ask a patient: 'What occurs to you in connection with this dream?'—as a rule he is unable to fix upon anything. I must present the dream to him piece by piece."

**Key Term Analysis**:

| Term | Definition | Significance |
|------|-----------|---------------|
| Free Association | 自由联想 | Report all thoughts without censorship | Core psychoanalytic technique |
| Eliminate Critique | 消除批评 | Suspend judgment | Overcome internal censor |
| Piece by Piece | 逐片分析 | Analyze each element separately | Not dream as whole |
| Background Thoughts | 背景思想 | Associations to each element | Reveal latent content |
| Psychic Preparation | 心理准备 | Patient's receptive state | Prerequisite for analysis |

**English Paraphrase (Primary Language)**:

Freud's method requires a **specific psychic preparation**. The patient must:

1. **Stimulate attention** to their own psychic perceptions
2. **Eliminate the critique** normally applied to emerging thoughts
3. **Report everything** that comes to mind—nothing is too trivial, absurd, or embarrassing

This is **free association** (freie Assoziation): letting the mind wander from each dream element while reporting all thoughts without selection or censorship.

The critical innovation: the dream is analyzed **piece by piece**, not as a whole. Ask not "What does this dream mean?" but "What occurs to you in connection with THIS element?" Each fragment yields its own chain of associations—the **background thoughts** (Hintergedanken).

This method differs from traditional approaches:
- It is **teachable** (not dependent on genius)
- It respects **individual meaning** (not universal keys)
- It follows **associative chains** (not fixed translations)
- It **empowers the dreamer** (their associations, not analyst's interpretation)

**Complete Chinese Interpretation (Secondary Language)**:

弗洛伊德的方法需要**特定的心理准备**。患者必须：

1. **激发注意力**关注自己的心理知觉
2. **消除批评**通常应用于涌现思想的批判
3. **报告一切**浮现在脑海中的——没有什么太琐碎、荒谬或尴尬

这就是**自由联想**（freie Assoziation）：让心灵从每个梦境元素出发自由游走，同时报告所有思想，不加选择或审查。

关键创新：梦是**逐片分析**的，而非作为整体。不要问"这个梦意味着什么？"而要问"关于这个元素，你想到什么？"每个片段产生自己的联想链——**背景思想**（Hintergedanken）。

这种方法不同于传统方法：
- 它是**可教授的**（不依赖天才）
- 它尊重**个人意义**（不是普遍密钥）
- 它遵循**联想链**（不是固定翻译）
- 它**赋权梦者**（他们的联想，而非分析师的解释）

**Narrative Snippets**:

- `[ns_freud_method_006]` `[trigger: free_association]` `[factor_trigger: dream_method AND dream_association AND free_association]` `[role: 主干]` The psychoanalytic method requires eliminating critique of emerging thoughts—the patient must notice and tell everything that passes through his mind, suppressing nothing as unimportant or nonsensical. → Freud Ch.II #Method
- `[ns_freud_method_007]` `[trigger: piece_by_piece]` `[factor_trigger: piece_by_piece AND background_thoughts]` `[role: 主干]` The dream is analyzed piece by piece, not as a whole—for each fragment, ask "What occurs to you?" and follow the chain of background thoughts. → Freud Ch.II #Method
- `[ns_freud_method_008]` `[trigger: schiller_quote]` `[factor_trigger: dream_method AND dream_creativity]` `[role: 条件分支]` Schiller to Koerner: "The intelligence has withdrawn its watchers from the gates, the ideas rush in pell-mell"—free association parallels poetic creation by suspending critical judgment. → Freud Ch.II #Method"""
    normalized_text_zh: str = """"""
    subject: str = "1 Free Association Technique"
    factor_refs: list = ['free_association', 'eliminate_critique', 'piece_by_piece', 'background_thoughts', 'psychic_preparation']
    
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
        l1_anchor="iod_v1.0.0_1_free_association_technique_001_L1",
    )
    version: str = "1.0.0"
