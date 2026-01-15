"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.460896
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
    semantic_id="iod_v1.0.0_chapter_iv__distortion_in_drea_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class ChapterIvDistortionInDrea(SemanticEntry):
    """
    ### Core Mechanism: Dream Censorship and Distortion

**Source Text** (from Chapter IV opening):
"Why...
    """
    
    original_text: str = """### Core Mechanism: Dream Censorship and Distortion

**Source Text** (from Chapter IV opening):
"Why does not the dream say directly what it means? As a matter of fact, even the dream of Irma's injection does not at first give the impression of representing a wish of the dreamer's as fulfilled. The reader will not have received such an impression, and even I myself was not aware of the fact until I had undertaken the analysis. The fact here recognized might be of universal applicability. Wherever a wish-fulfillment is unrecognizable and concealed, there must be present a feeling of repulsion towards this wish, and in consequence of this repulsion the wish is unable to gain expression except in a disfigured state."

**English Paraphrase**:

**Dream Distortion** = transformation process that disguises unconscious wishes to bypass **censorship** — a psychic force that blocks unacceptable wishes from direct expression.

**Core Points**:
- Dreams don't directly state their meaning because of **internal censorship**
- Unacceptable wishes (sexual, aggressive, socially forbidden) must be **disguised**
- Distortion = compromise between:
  - **Unconscious wish** (demanding expression)
  - **Censoring agency** (moral/social standards of ego)

**Complete Chinese Interpretation (Secondary Language)**:

梦的**扭曲**，是整套梦之工作的核心结果：原本要求直接表达的无意识愿望，在遇到内在的“审查机关”时，不能以原貌出现，只能被改写成一种自我与道德尚能接受的形式。许多愿望带有强烈的性与攻击成分，或触及对重要他人的敌意、报复与嫉妒，这些内容一旦赤裸呈现，立刻会引发焦虑、愧疚或羞耻，甚至把人从梦中惊醒。扭曲机制正是在这样的张力场中，承担“既要满足，又要遮掩”的双重任务。

从动力学的角度看，扭曲是**两股力量妥协的产物**：一边是坚持要上升的无意识愿望，一边是代表现实与道德标准的审查力量。为了通过检查，梦的工作不得不动用各种技术——把多个思想压缩进一个形象（凝缩），把情感重量从真正关键之处移到琐碎细节上（移置），用看似无害的意象来指代禁忌主题（象征化），甚至用“说反话”的方式表达真实立场（反向表征）。于是，表面看来梦好像只是在围绕一些无足轻重的小事打转，实际上这些小事恰恰是欲望与审查短兵相接的前线。

正因为有扭曲存在，我们在第一眼往往**看不到任何愿望满足**，甚至觉得梦在反驳或惩罚自己。对弗洛伊德而言，这种“不像愿望”的感觉本身，就是审查成功的证据——凡是最危险、最难承认的愿望，才需要被扭曲得最厉害。释梦的任务，就是顺着这些荒诞断裂、不成比例的情绪和情节，往回追踪那股被伪装的欲求，以及站在对立面上的审查力量。

### Detailed Explanation

**Why distortion is necessary**:
1. **Repulsion/repression**: Ego finds certain wishes morally repugnant
2. **Sleep protection**: Undisguised forbidden wishes would wake the dreamer
3. **Compromise formation**: Dream allows partial wish satisfaction while maintaining sleep

**The censorship mechanism**:
- Operates like **political censorship** of press
- Deletes, alters, disguises objectionable content
- More **intelligent** forms: displacement, symbolization, secondary revision
- Strength varies: weak in children (transparent wishes), strong in neurotics

**Evidence for censorship**:
- Dreams of **shame/embarrassment** (nakedness dreams) = censorship partially failed
- **Anxiety dreams** = censorship inadequate, wish breaks through but arouses fear
- Successful censorship = bland, forgettable dreams

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Censorship | Psychic force blocking wishes | Creates distortion |
| Distortion | Disguise mechanism | Compromise formation |
| Repulsion | Ego rejects wish | Why disguise needed |
| Sleep Protection | Disguise maintains sleep | Functional purpose |

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Dream Distortion: Compromise between unconscious wish and censoring agency. Mechanisms include condensation, displacement, symbolization. More distortion=more threatening wish. Censorship operates like political censorship.
- **中文**: 梦的扭曲:无意识愿望与审查机关之间的妥协。机制包括凝缩、移置、象征化。扭曲越多=愿望越威胁性。审查如同政治审查运作。

**Narrative Snippets**:
- `[ns_freud_ch4_001]` `[trigger: dream_distortion]` `[factor_trigger: dream_censorship]` `[role: 主干]` Dream distortion = compromise between unconscious wish and censoring agency. → Core
- `[ns_freud_ch4_002]` `[trigger: censorship_mechanism]` `[factor_trigger: dream_censorship AND ego_defense]` `[role: 条件分支]` Censorship operates like political censorship; deletes, alters, disguises objectionable content. → Mechanism
- `[ns_freud_ch4_003]` `[trigger: distortion_strength]` `[factor_trigger: dream_censorship AND wish_threat]` `[role: 条件分支]` More distortion = more threatening wish; successful censorship = bland, forgettable dreams. → Principle"""
    normalized_text_zh: str = """"""
    subject: str = "Chapter IV: Distortion in Dreams (Selected Key Examples)"
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
        l1_anchor="iod_v1.0.0_chapter_iv__distortion_in_drea_001_L1",
    )
    version: str = "1.0.0"
