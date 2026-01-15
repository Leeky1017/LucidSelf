"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.469012
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
    semantic_id="iod_v1.0.0_manifest_vs_latent_content___t_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class ManifestVsLatentContentT(SemanticEntry):
    """
    **Source Text**:
"All previous attempts to solve the problems of the dream have been based directly ...
    """
    
    original_text: str = """**Source Text**:
"All previous attempts to solve the problems of the dream have been based directly upon the manifest dream content as it is retained in the memory... We alone are in possession of new data; for us a new psychic material intervenes between the dream content and the results of our investigations: and this is the latent dream content or the dream thoughts which are obtained by our method."

"We regard the dream thoughts and the dream content as two representations of the same meaning in two different languages; or to express it better, the dream content appears to us as a translation of the dream thoughts into another form of expression, whose signs and laws of composition we are to learn by comparing the original with the translation."

"Now the dream is a picture-puzzle (rebus) of this sort, and our predecessors in the field of dream interpretation have made the mistake of judging the rebus as an artistic composition. As such it appears nonsensical and worthless."

**Key Term Analysis**:

| Term | Definition | Significance |
|------|-----------|---------------|
| Manifest Content | The dream as remembered and reported | Surface level, requires decoding |
| Latent Content | Hidden dream-thoughts behind manifest content | True meaning, unconscious wishes |
| Dream-Work | Transformation process from latent to manifest | Core mechanism of dream formation |
| Rebus | Picture-puzzle where images represent sounds/words | Key analogy for dream interpretation |
| Translation | Dream as translation between two languages | Methodological principle |

**English Paraphrase (Primary Language)**:

Freud establishes the **fundamental distinction** that defines psychoanalytic dream interpretation: the difference between **manifest content** (the dream as remembered) and **latent content** (the hidden thoughts behind the dream). All previous dream theories worked only with manifest content; psychoanalysis introduces a new layer of data.

The revolutionary insight is that **dream and dream-thoughts are the same meaning in two different languages**. The dream is not nonsense but a **translation** whose rules must be learned. Freud's crucial analogy is the **rebus** (picture-puzzle): if you see a picture of a house with a boat on its roof and a headless running figure, judging it as a painting produces only "nonsensical." But treating each image as representing a syllable or word reveals meaningful expression.

This rebus principle means dreams must be read **sign by sign**, not as coherent narratives. Previous interpreters failed because they judged the dream as an "artistic composition" rather than a code to be deciphered.

**Complete Chinese Interpretation (Secondary Language)**:

弗洛伊德确立了定义精神分析释梦的**根本区分**：**显性内容**（梦境如同被记忆的那样）与**隐性内容**（梦境背后的隐藏思想）之间的差异。所有先前的梦理论仅处理显性内容；精神分析引入了新的数据层。

革命性洞见在于：**梦与梦思是同一含义的两种不同语言表达**。梦不是胡言乱语，而是需要学习其规则的**翻译**。弗洛伊德的关键类比是**图谜**（rebus）：如果你看到一张图，房顶上有船，还有一个无头奔跑的人形，把它当作绘画来评判只会得出"荒谬无价值"的结论。但如果把每个图像当作代表音节或词语的符号，就能揭示出有意义的表达。

这一图谜原则意味着梦必须**逐符号阅读**，而非作为连贯叙事。先前的解释者之所以失败，是因为他们把梦当作"艺术作品"而非需要破解的密码。

**Core Points**:

- Manifest content is surface; latent content is depth
- Dream = translation between two languages (thoughts → images)
- Rebus analogy: read signs, not pictures
- Previous theories failed by treating dreams as compositions
- Dream-work is the transformation mechanism

**Detailed Explanation**:

This opening establishes Freud's **epistemological break** with previous dream science. Where earlier researchers asked "what does this dream mean?" (treating meaning as self-evident), Freud asks "how was this dream produced?" (treating meaning as hidden and requiring excavation).

The **two-language model** has profound implications. If dreams are translations, then interpretation is **reverse translation**—moving from the picture-language back to the thought-language. This requires learning the "grammar" of dream formation: condensation, displacement, symbolization, and secondary elaboration.

The **rebus principle** is not merely an analogy but a method. Each dream element must be treated as a **signifier** whose meaning is determined by its relation to other elements and to the dreamer's associations, not by its visual appearance. A boat on a roof is not "nonsensical"—it may represent the syllable "boat" or evoke associations to water, travel, instability, etc.

This principle explains why **symbolic dictionaries fail**. Dreams are not coded messages with fixed keys but personal translations requiring the dreamer's associations to decode.

**Textual Criticism & Variant Analysis (Bilingual)**:

- **English**: Freud's rebus analogy appears throughout his work and became foundational for later structural linguistics (Lacan). The German "Bilderrätsel" (picture-riddle) captures the ludic quality better than English "rebus."
- **中文**: 弗洛伊德的图谜类比贯穿其著作，后来成为结构主义语言学（拉康）的基础。德语"Bilderrätsel"（图画谜语）比英语"rebus"更能捕捉其游戏性质。本译文保留"图谜"而非音译，以突出其方法论意义。

**Narrative Snippets**:

- `[ns_freud_dw_001]` `[trigger: dream_interpretation_method]` `[factor_trigger: dream_manifest_content AND dream_latent_content AND manifest_content AND latent_content AND two_language_model]` `[role: 主干]` The dream content appears to us as a translation of the dream thoughts into another form of expression, whose signs and laws of composition we are to learn by comparing the original with the translation. → Freud Ch.VI #Condensation
- `[ns_freud_dw_002]` `[trigger: dream_is_rebus]` `[factor_trigger: rebus_principle AND symbolization]` `[role: 主干依赖]` The dream is a picture-puzzle (rebus), and our predecessors have made the mistake of judging it as an artistic composition. As such it appears nonsensical and worthless. → Freud Ch.VI #Condensation
- `[ns_freud_dw_003]` `[trigger: manifest_vs_latent]` `[factor_trigger: dream_manifest_content]` `[role: 条件分支]` All previous attempts to solve the problems of the dream have been based directly upon the manifest dream content—we alone possess the latent dream content as new psychic material. → Freud Ch.VI #Condensation"""
    normalized_text_zh: str = """"""
    subject: str = "Manifest vs Latent Content - The Rebus Principle"
    factor_refs: list = ['manifest_content', 'latent_content', 'dream_work', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="iod_v1.0.0_manifest_vs_latent_content___t_001_L1",
    )
    version: str = "1.0.0"
