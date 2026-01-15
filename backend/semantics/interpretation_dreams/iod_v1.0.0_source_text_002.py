"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.482367
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
    semantic_id="iod_v1.0.0_source_text_002",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class SourceText(SemanticEntry):
    """
    "We must distinguish between the manifest dream-content, which we vaguely remember in the morning an...
    """
    
    original_text: str = """"We must distinguish between the manifest dream-content, which we vaguely remember in the morning and which we think we can narrate, and the latent dream-thoughts, which we must assume to exist in the unconscious. The transformation of the latter into the former, that is, the dream-work proper, is the core process we must understand if we are to make sense of dreams."

#### English Paraphrase (Primary Language)

Freud establishes a fundamental distinction between two layers of the dream: the manifest content and the latent content. The manifest dream-content is what we consciously remember and can report—the surface narrative with its images, emotions, and events as they appeared during sleep. The latent dream-thoughts are the hidden unconscious wishes, thoughts, and meanings that the dream actually expresses. These latent thoughts exist in the unconscious and are not directly accessible to awareness. The dream-work is the complex psychological process that transforms latent thoughts into manifest content—disguising, condensing, and symbolizing unconscious material to create the dream we experience and remember.

#### Complete Chinese Interpretation

在这里，弗洛伊德提出梦的两层结构：一层是我们醒来后还能叙述的**显梦内容**，一层是隐藏其后、真正具有心理意义的**潜梦思想**。显梦是一段可被记忆和讲述的故事——包含画面、情节和情绪，却常常支离破碎、前后矛盾；潜梦则是一整束有逻辑的思想与欲望链条，只是全部停留在无意识层面，无法直接被体验。

两者之间由所谓“梦的工作”相连：潜梦思想在进入睡眠意识之前，会被一系列机制加工和伪装——被凝缩、移置、象征化，并在最后被“二次修饰”，才形成我们实际经历的梦境。正是这些变形过程，使得梦在表面上看去毫无章法，像是杂乱无章的拼贴，而不是可以直接阅读的心理文本。

因此，梦的解释并不在于逐字逐句抓住显梦故事本身，而在于**逆向追溯**：从显梦出发，通过自由联想，沿着象征与情绪的线索回到那一整束潜梦思想。显梦是外壳，潜梦是内核；显梦是经审查机关允许上映的删减版，潜梦则是未经删节的原始剧本。这一“表层–深层”模型后来被推广到症状、口误、笑话和艺术等全部心理现象，成为精神分析理解心灵运作的基础框架。

#### Core Points

- **Manifest content**: Surface dream as remembered and reported, consciously accessible narrative
- **Latent content**: Hidden unconscious wishes and thoughts, true psychological meaning
- **Dream-work**: Transformation process disguising latent thoughts into manifest dream
- **Two-layer model**: Surface vs depth, appearance vs reality structure
- **Interpretation goal**: Reverse dream-work to recover latent thoughts from manifest content

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Manifest Content | Surface dream remembered | Consciously accessible |
| Latent Content | Hidden unconscious wishes | True meaning |
| Dream-work | Transformation process | Disguise mechanism |
| Two-layer Model | Surface vs depth | Core Freudian structure |

#### Textual Criticism & Variant Analysis (Bilingual)
- **English**: Manifest vs Latent content. Dream-work transforms unconscious wishes into acceptable narrative. Two-layer model: surface appearance vs hidden reality. Interpretation reverses this process.
- **中文**: 显梦vs潜梦内容。梦的工作将无意识愿望转化为可接受叙事。两层模型:表面外观vs隐藏现实。解释逆转此过程。

**Narrative Snippets**:
- `[ns_freud_005]` `[trigger: manifest_content]` `[factor_trigger: manifest_content AND latent_content]` `[role: 主干]` We must distinguish between the manifest dream-content, which we remember and narrate, and the latent dream-thoughts in the unconscious. → Source Text
- `[ns_freud_006]` `[trigger: dream_work]` `[factor_trigger: dream_work AND dream_formation]` `[role: 主干依赖]` The transformation of latent thoughts into manifest content—the dream-work proper—is the core process we must understand. → Source Text
- `[ns_freud_007]` `[trigger: two_layer]` `[factor_trigger: condensation AND displacement]` `[role: 条件分支]` Manifest is the surface narrative; latent is the hidden unconscious wishes—dreams have a two-layer structure. → English Paraphrase
- `[ns_freud_008]` `[trigger: reverse_process]` `[factor_trigger: association_chain AND free_association]` `[role: 总结]` Interpretation aims to reverse the dream-work: from manifest content, recover the latent thoughts through free association. → English Paraphrase

#### Detailed Explanation

This distinction between manifest and latent content is perhaps Freud's most important theoretical contribution to dream psychology. It establishes dreams as having a two-layer structure: what appears on the surface and what lies hidden beneath.

The manifest content is phenomenologically primary—it's what the dreamer experiences and remembers. It has narrative structure, sensory qualities, emotional tones, and often bizarre illogical elements. We can describe manifest content to others, though our memory of it often fades quickly upon waking.

The latent content, by contrast, is never directly experienced. It consists of unconscious wishes, often infantile or forbidden, along with associated thoughts, memories, and concerns. These latent thoughts are typically unacceptable to consciousness—wishes that would provoke anxiety, guilt, or shame if acknowledged. The latent content follows rational, purposeful logic (wish-fulfillment) even though the manifest dream appears irrational.

The dream-work is the crucial intermediate process—neither manifest nor latent but the transformation linking them. It employs specific mechanisms (condensation, displacement, considerations of representability, secondary revision) to disguise unacceptable latent wishes into an acceptable manifest form that allows sleep to continue. The dream-work is what makes dreams strange and seemingly meaningless, creating a compromise between the wish pressing for expression and the censorship defending against it.

Freud's interpretive method aims to reverse this process: starting from manifest content, using free association, the analyst helps recover the latent thoughts. This reversal is possible because the transformations, though complex, follow discoverable laws. The manifest content is not random but systematically related to latent thoughts through specific mechanisms.

This two-layer model became foundational not just for dream interpretation but for all psychoanalytic understanding of symptoms, slips, jokes, and art—all seen as manifest contents expressing disguised latent meanings.

---"""
    normalized_text_zh: str = """"""
    subject: str = "Source Text"
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
        l1_anchor="iod_v1.0.0_source_text_002_L1",
    )
    version: str = "1.0.0"
