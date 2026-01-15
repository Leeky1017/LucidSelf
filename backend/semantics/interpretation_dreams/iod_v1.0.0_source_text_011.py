"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.482457
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
    semantic_id="iod_v1.0.0_source_text_011",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class SourceText(SemanticEntry):
    """
    "We call the psychical process which is alone admitted by the first system the primary psychical pro...
    """
    
    original_text: str = """"We call the psychical process which is alone admitted by the first system the primary psychical process; and the process which results from the inhibition imposed by the second system we call the secondary process. The primary process strives for discharge of excitation in order to establish a perceptual identity with the wished-for experience. The secondary process has abandoned this intention and has adopted another—the establishment of thought-identity. All thinking is merely a circuitous path from the memory of a gratification to an identical cathexis of the same memory, which it is hoped to attain once more by means of motor activity."

#### English Paraphrase (Primary Language)

The primary process characterizes unconscious functioning: immediate discharge of tension through hallucinatory wish-fulfillment, disregard for logic and contradiction, timelessness, replacement of external reality by psychic reality. The dream operates primarily through primary process. The secondary process characterizes conscious ego functioning: delayed gratification, logical thought, reality-testing, verbal language, contradiction-recognition, temporal ordering. The transition from primary to secondary process represents the infant's developmental achievement—learning to think rather than merely hallucinate wishes. Dreams regress from secondary to primary process, explaining their illogical, timeless, hallucinatory character. The dream-work mechanisms (condensation, displacement) exemplify primary process operation where identity is based on similarity rather than logic.

#### Complete Chinese Interpretation

在弗洛伊德的模型中，**原初过程**与**次级过程**并不是两类不同的内容，而是两套迥异的心理运作方式。原初过程是无意识系统的工作模式：一切以**立即解除紧张、幻觉性满足愿望**为目标，不顾时间顺序、不承认矛盾、也不区分外在现实与内在想象——只要内在图像能让欲望感觉“好像被满足了”，就算达成目的。梦境的荒诞、跳跃、时空错乱，正是原初过程在夜间接管心灵的表现。

次级过程则是自我与前意识的工作模式：它学会了**延迟满足**，通过现实检验与逻辑推理，为欲望寻找在现实中可行的实现路径；它尊重因果与时间顺序，使用语言与抽象概念组织经验，能够识别矛盾与不可能。婴儿成长为儿童、成人的过程，很大程度上就是从单一依赖原初过程，逐步发展出稳定的次级过程——学会“先想一想该怎么做”，而不是立刻幻觉性地“假装已经得到”。

梦的形成意味着一种**暂时性的过程倒退**：白天占主导的次级过程在夜间松手，让原初过程重新占上风。这不仅解释了梦的非逻辑、无时间感和强烈情绪，也说明为什么梦工作中会大量使用凝缩、移置等“按相似与接近而非按逻辑连接”的机制。与此同时，只要醒来后我们能重新回到次级过程，对梦加以反思而不是继续沉溺其中，这种往返本身就是健康心理运作的一部分。

#### Core Points

- **Primary process**: Unconscious, immediate discharge, hallucinatory, illogical, timeless
- **Secondary process**: Conscious/preconscious, delayed gratification, logical, verbal, temporal
- **Dreams use primary**: Regression to primitive process explaining dream characteristics
- **Developmental sequence**: Infant learns secondary from primary
- **Identity types**: Perceptual (primary) vs thought (secondary)

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Primary Process | Unconscious mode | Immediate, hallucinatory |
| Secondary Process | Conscious mode | Delayed, logical |
| Process Regression | Secondary→Primary | Dreams revert |
| Developmental Sequence | Primary→Secondary | Maturation |

#### Textual Criticism & Variant Analysis (Bilingual)
- **English**: Primary process: unconscious, immediate, hallucinatory, illogical. Secondary: conscious, delayed, logical. Dreams regress to primary. Developmental: infant learns secondary.
- **中文**: 原初过程:无意识,即时,幻觉,无逻辑。次级:意识,延迟,逻辑。梦退行到原初。发展:婴儿学习次级。"""
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
        l1_anchor="iod_v1.0.0_source_text_011_L1",
    )
    version: str = "1.0.0"
