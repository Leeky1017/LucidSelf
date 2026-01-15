"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.482448
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
    semantic_id="iod_v1.0.0_source_text_010",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class SourceText(SemanticEntry):
    """
    "In the dream we do not think but we experience—we hallucinate. The transformation of thoughts into ...
    """
    
    original_text: str = """"In the dream we do not think but we experience—we hallucinate. The transformation of thoughts into hallucinations is the most striking characteristic of dream-activity. The dream regresses from the thought to the perceptual images from which thought originally arose. This regression is both topographical (from conscious to unconscious systems), temporal (from present to infantile past), and formal (from logical thought to primitive wish-representation)."

#### English Paraphrase (Primary Language)

Regression in dreams operates on three levels simultaneously. Topographical regression: mental activity flows backward from consciousness through preconscious to unconscious systems rather than forward toward motor expression. Temporal regression: current thoughts connect to increasingly ancient infantile wishes and memories. Formal regression: logical, verbal, secondary-process thinking regresses to primitive, visual, primary-process modes. The dream's hallucina​tory character results from this regression—instead of thinking thoughts, the dreamer experiences perceptual images. This regression recreates the infant's original mode of wish-fulfillment: when unable to satisfy wishes in reality, the infant hallucinates satisfaction perceptually. Dreams recapitulate this primitive hallucinatory wish-fulfillment, temporarily abandoning reality-testing.

#### Complete Chinese Interpretation

在梦的活动中，**倒退**并非单一现象，而是同时发生在三个互相关联的维度。首先是**拓扑倒退**：心理能量的流向由清醒时“从内向外、指向行动”的路径，改为从意识层退回前意识，进一步下潜到无意识系统，终止于内部表征而不是外在动作。其次是**时间倒退**：当前的念头与情境，不断被牵引回更早期的人生阶段，特别是婴儿期和童年期的原始欲望与记忆。最后是**形式倒退**：原本以语言、逻辑、概念为媒介的次级过程思维，退回到以图像、感受和情境复现为主的原初过程——思维变成“看到和经历”，而不是用词语在脑中推理。

正是这三重倒退，使梦呈现出**幻觉性**：做梦时，我们不是在“思考一个愿望”，而是直接“感受到它好像实现了”——就像婴儿在无法得到乳汁时，会用吸吮动作、口部快感与想象画面来“幻觉性满足”自己的饥饿。梦在夜间重新上演了这种古老模式：现实检验暂时退居幕后，动作受肌肉抑制阻止我们真的去行动，心理则在内在舞台上把愿望以画面形式实现。

倒退一方面解释了梦的幼稚、荒诞和非逻辑性，另一方面也揭示出梦的**发育意义**：它让我们在成年后，仍然定期回到那种最原始的心灵运行方式，从而为无意识提供表达通道。只要这种倒退是可逆的——醒来后我们仍能回到以现实和逻辑为主的次级过程——它就是心理自我调节的一部分，而不是病理退行。

#### Core Points

- **Three types**: Topographical (system), temporal (age), formal (process mode)
- **Hallucination creation**: Thoughts transform into perceptual images
- **Primitive wish-fulfillment**: Recapitulates infant's hallucinatory satisfaction
- **Reality-testing suspended**: Dreams lack critical judgment of perceptions
- **Motor inhibition enables**: Sleep paralysis allows hallucination without action

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Regression | Backward movement | Three dimensions |
| Topographical | System backward | Cs→Pcs→Ucs |
| Temporal | Age backward | Present→infantile |
| Formal | Mode backward | Thought→image |

#### Textual Criticism & Variant Analysis (Bilingual)
- **English**: Regression: three types (topographical, temporal, formal). Thoughts become images. Recapitulates infant's hallucinatory satisfaction. Reality-testing suspended.
- **中文**: 退行:三种类型(拓扑,时间,形式)。思想变成图像。重演婴儿幻觉满足。现实检验暂停。"""
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
        l1_anchor="iod_v1.0.0_source_text_010_L1",
    )
    version: str = "1.0.0"
