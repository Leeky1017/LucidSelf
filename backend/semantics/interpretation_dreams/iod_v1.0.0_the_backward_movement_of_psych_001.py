"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.465539
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
    semantic_id="iod_v1.0.0_the_backward_movement_of_psych_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class TheBackwardMovementOfPsych(SemanticEntry):
    """
    **Source Text** (from section context):
"Regression" describes the backward movement of psychic ener...
    """
    
    original_text: str = """**Source Text** (from section context):
"Regression" describes the backward movement of psychic energy from motor end (action) to perceptual end (hallucination). In waking life, thoughts proceed from perception toward action; in dreams, they reverse direction, producing hallucinatory revival of perceptual images.

"The dream process takes a regressive path, which is certainly not followed during waking life... The dream-work subjects the thought material to a peculiar treatment. First, it transforms thoughts into visual scenes—then follows regression."

**Key Term Analysis**:

| Term | Definition | Significance |
|------|-----------|---------------|
| Regression | Backward movement from motor to perceptual | Explains visual quality of dreams |
| Topographical Model | Psychic apparatus with spatial arrangement | Framework for regression |
| Perceptual End | Where sensory input enters | Destination of regression |
| Motor End | Where action output exits | Origin of regression |
| Hallucination | Perceptual revival without external stimulus | Product of regression |

**English Paraphrase (Primary Language)**:

**Regression** is Freud's explanation for why dreams are predominantly **visual**. He introduces a **topographical model** of the psychic apparatus with two ends: the **perceptual end** (where sensory input enters) and the **motor end** (where action output exits).

In **waking life**, psychic energy flows forward: perception → thought → action. In **dreams**, this direction **reverses**: thoughts flow backward to the perceptual end, producing **hallucinatory** revivals of visual images. This is why we "see" dreams rather than "think" them.

Regression explains several dream characteristics:
1. **Visual dominance**: Thoughts become pictures
2. **Hallucinatory quality**: Dreams seem real while occurring
3. **Timelessness**: Regression reaches earliest memory traces
4. **Primary process**: Regressive thinking uses primitive logic

The blocked motor outlet during sleep forces psychic energy backward. Unable to discharge through action, wishes find expression through perceptual hallucination.

**Complete Chinese Interpretation (Secondary Language)**:

**退行**是弗洛伊德对梦为何主要是**视觉性**的解释。他引入了心理装置的**拓扑模型**，有两端：**知觉端**（感觉输入进入处）和**运动端**（行动输出离开处）。

在**清醒生活**中，心理能量向前流动：知觉→思维→行动。在**梦中**，这一方向**逆转**：思想向后流向知觉端，产生视觉图像的**幻觉性**复活。这就是为什么我们"看到"梦而非"思考"梦。

退行解释了梦的若干特征：
1. **视觉主导**：思想变成图像
2. **幻觉质量**：梦发生时似乎真实
3. **无时间性**：退行达到最早记忆痕迹
4. **初级过程**：退行思维使用原始逻辑

睡眠期间被阻塞的运动出口迫使心理能量向后流动。无法通过行动释放，愿望通过知觉幻觉找到表达。

**Core Points**:

- Regression = backward flow from motor to perceptual end
- Topographical model: perceptual end ↔ motor end
- Waking: perception → thought → action
- Dreaming: thought → perception (reversed)
- Result: visual hallucination of wishes
- Blocked motor outlet forces backward flow

**Detailed Explanation**:

Regression is Freud's **metapsychological** explanation for dream phenomenology. The question is: why are dreams visual? Why do we experience them as perceptions rather than thoughts?

The answer lies in the **blocking of motor discharge** during sleep. In waking life, a thought leads to action—you want food, you eat. In sleep, motor pathways are blocked (sleep paralysis). The wish-energy cannot discharge forward, so it flows **backward** toward the perceptual system, producing hallucinatory satisfaction.

This explains why dreams **feel real**: they activate the perceptual system as if external stimuli were present. The regression converts thoughts back into the perceptual images from which they originally derived.

**Temporal regression** also occurs: the backward flow reaches early memory traces, explaining why childhood memories appear in dreams. The most regressive dreams touch the earliest strata of experience.

This model anticipates Freud's later structural theory and underlies the concept of **primary process** thinking—the mode of mental functioning characteristic of the unconscious.

**Textual Criticism & Variant Analysis (Bilingual)**:

- **English**: "Regression" (German: Regression) has three types in Freud: topographical, temporal, and formal. Here the focus is topographical.
- **中文**: "退行"（德语：Regression）在弗洛伊德理论中有三种类型：拓扑退行、时间退行和形式退行。此处焦点是拓扑退行。中文"退行"很好地保留了向后移动的空间意象。

**Narrative Snippets**:

- `[ns_freud_psy_005]` `[trigger: regression]` `[factor_trigger: regression AND perceptual_end]` `[role: 主干]` The dream process takes a regressive path not followed in waking life—psychic energy flows backward from motor to perceptual end, producing visual hallucination. → Freud Ch.VII #Regression
- `[ns_freud_psy_006]` `[trigger: topographical_model]` `[factor_trigger: system_ucs AND system_cs]` `[role: 主干依赖]` The psychic apparatus has two ends: perceptual (input) and motor (output). Waking flows forward; dreaming reverses direction. → Freud Ch.VII #Regression
- `[ns_freud_psy_007]` `[trigger: hallucinatory_fulfillment]` `[factor_trigger: real_psychic AND dream_abortion]` `[role: 条件分支]` Blocked motor outlet during sleep forces wishes to find expression through regression to perceptual hallucination—we "see" wish-fulfillment. → Freud Ch.VII #Regression"""
    normalized_text_zh: str = """"""
    subject: str = "The Backward Movement of Psychic Energy"
    factor_refs: list = ['regression', 'topographical_model', 'perceptual_end', 'motor_end', 'hallucinatory_satisfaction']
    
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
        l1_anchor="iod_v1.0.0_the_backward_movement_of_psych_001_L1",
    )
    version: str = "1.0.0"
