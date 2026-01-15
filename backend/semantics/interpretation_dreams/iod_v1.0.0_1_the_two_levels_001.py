"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.471236
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
    semantic_id="iod_v1.0.0_1_the_two_levels_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class 1TheTwoLevels(SemanticEntry):
    """
    **Source Text**:
"We have now established two new things: first, that the dream content is much brie...
    """
    
    original_text: str = """**Source Text**:
"We have now established two new things: first, that the dream content is much briefer than the dream thoughts of which it is the substitute; and secondly, that dream distortion is the work of a censorship directed against unacceptable wish-impulses."

"We will therefore distinguish between the manifest dream content, which is given in the dream itself, and the latent dream thoughts, which we infer by interpretation. The relation between manifest and latent dream-material is the work of the dream-distortion (Traumentstellung)."

"The manifest content of the dream is the disguised substitute for the unconscious dream thoughts, and this disguising is the work of the ego's defenses."

**Key Term Analysis**:

| Term | Definition | Significance |
|------|-----------|---------------|
| Manifest Content | 显梦内容 | What dreamer remembers | Surface level |
| Latent Thoughts | 隐梦思想 | What dream really means | Hidden level |
| Dream-Work | 梦工作 | Process manifest → latent | Transformation |
| Traumentstellung | 梦的伪装 | German: dream distortion | Technical term |
| Briefer | 更简短 | Manifest < Latent | Condensation evidence |

**English Paraphrase (Primary Language)**:

Freud establishes the fundamental distinction:

**Manifest Content** (显梦内容): The dream as remembered and reported—the surface narrative, the images, the sequence of events. This is what the dreamer tells.

**Latent Content** (隐梦思想): The underlying thoughts, wishes, and conflicts that the dream expresses in disguised form. This is what interpretation reveals.

The **dream-work** (Traumarbeit) is the process that transforms latent into manifest. It includes:
- **Condensation**: Many latent elements compressed into few manifest images
- **Displacement**: Emotional charge moved from important to trivial elements
- **Symbolization**: Abstract thoughts represented by concrete images
- **Secondary revision**: Dreamer's attempt to make dream coherent on waking

The manifest content is always **briefer** than latent thoughts—condensation compresses rich material into sparse images. This is why a short dream can yield pages of associations.

**Complete Chinese Interpretation (Secondary Language)**:

弗洛伊德确立了根本区分：

**显梦内容**（Manifest Content）：被记住和报告的梦——表面叙事、图像、事件序列。这是梦者所述。

**隐梦内容**（Latent Thoughts）：梦以伪装形式表达的潜在思想、愿望和冲突。这是解释所揭示的。

**梦工作**（Traumarbeit）是将隐梦转化为显梦的过程。它包括：
- **凝缩**：许多隐梦元素压缩成少数显梦意象
- **移置**：情感负荷从重要元素移到琐碎元素
- **象征化**：抽象思想用具体意象表示
- **二次修饰**：梦者醒来时试图使梦连贯

显梦内容总是比隐梦思想**更简短**——凝缩将丰富材料压缩成稀疏意象。这就是为什么一个短梦能产生数页联想。

**Narrative Snippets**:

- `[ns_freud_dist_007]` `[trigger: manifest_latent]` `[factor_trigger: dream_manifest AND dream_latent AND manifest_content AND latent_content AND interpretation]` `[role: 主干]` Fundamental distinction: manifest content (what dreamer remembers) vs. latent thoughts (what dream really means)—dream distortion transforms the latter into the former. → Freud Ch.IV #Content
- `[ns_freud_dist_008]` `[trigger: dream_work]` `[factor_trigger: latent_to_manifest AND dream_transformation AND dream_work]` `[role: 主干]` Dream-work (Traumarbeit) transforms latent into manifest through condensation, displacement, symbolization, and secondary revision. → Freud Ch.IV #Content
- `[ns_freud_dist_009]` `[trigger: briefer]` `[factor_trigger: dream_condensation AND dream_manifest]` `[role: 条件分支]` The manifest content is much briefer than latent thoughts—condensation compresses rich material into sparse images, so a short dream yields pages of associations. → Freud Ch.IV #Content
- `[ns_freud_dist_010]` `[trigger: disguised_substitute]` `[factor_trigger: dream_distortion AND dream_defense]` `[role: 总结]` The manifest content is the disguised substitute for unconscious dream thoughts—this disguising is the work of the ego's defenses. → Freud Ch.IV #Content"""
    normalized_text_zh: str = """"""
    subject: str = "1 The Two Levels"
    factor_refs: list = ['dream_censor', 'manifest_content', 'latent_content', 'dream_work', 'distortion', 'political_analogy']
    
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
        l1_anchor="iod_v1.0.0_1_the_two_levels_001_L1",
    )
    version: str = "1.0.0"
