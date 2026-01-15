"""
Auto-generated semantic module for collected_works
Generated at: 2025-12-05T13:30:20.574903
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
    semantic_id="cw_v1.0.0_source_text_003",
    book_id="collected_works",
    engine_id="psych"
)
class SourceText(SemanticEntry):
    """
    "Individuation means becoming an 'in-dividual,' and, in so far as 'individuality' embraces our inner...
    """
    
    original_text: str = """"Individuation means becoming an 'in-dividual,' and, in so far as 'individuality' embraces our innermost, last, and incomparable uniqueness, it also implies becoming one's own self. We could therefore translate individuation as 'coming to selfhood' or 'self-realization.' The aim of individuation is nothing less than to divest the self of the false wrappings of the persona on the one hand, and the suggestive power of primordial images on the other."

#### English Paraphrase (Primary Language)

**Individuation** is Jung's term for the lifelong psychological process of **becoming who you truly are**—integrating all aspects of psyche (conscious/unconscious, personal/collective) into unified whole. Not "individualism" (ego inflation) but becoming an "**in-dividual**"—undivided, integrated self.

**The process**:
1. **Youth (First Half of Life)**: Ego development, persona building, adaptation to collective
   - Focus: External achievement, fitting in, building identity
   - Necessary foundation but incomplete
   
2. **Mid-life Crisis**: Persona no longer satisfies, symptoms emerge (depression, meaninglessness, dreams intensify)
   - Trigger: Realization that outer success ≠ inner fulfillment
   - Call: Unconscious demands attention
   
3. **Second Half of Life**: Turn inward, engage unconscious, integrate shadow/anima-animus
   - Shadow work: Accept rejected parts of self
   - Anima/Animus integration: Relate to contrasexual inner figure
   - Archetype encounter: Engage transpersonal dimension

4. **Self-Realization**: Not completion but ongoing process of becoming more whole
   - Self emerges as regulating center (not ego)
   - Personality becomes more authentic, less identified with persona
   - Access to transpersonal wisdom through integrated unconscious

**Two dangers**:
- **Persona identification**: Remaining stuck in social mask, never discovering authentic self
- **Archetypal inflation**: Identifying with archetype, losing ego boundaries (psychosis risk)

**The goal**: Neither ego-inflation nor ego-dissolution but **ego-Self axis**—conscious ego relating appropriately to larger Self, maintaining distinction while in dialogue.

**Not for everyone**: Jung emphasized individuation is calling for few, not mass program. Requires:
- Sufficient ego strength (neurosis < psychosis risk)
- Life crisis creating pressure
- Cultural context supporting inner work
- Often requires analysis/guidance

**Social paradox**: Process makes you MORE individual (unique) yet MORE connected (to collective unconscious, humanity). By becoming fully yourself, you connect to transpersonal dimension shared by all.

#### Complete Chinese Interpretation (Secondary Language)

完整中文诠释：个体化并不是“变得特别自我”、“与世界决裂”的过程，而是一个贯穿一生的**心理成熟与整合进程**：从仅仅围绕自我与人格面具运作，逐步学会与无意识、与集体层面的心灵现实建立对话，最终成为一个既独特又与整体相连的“无分裂之人（in-dividual）”。在前半生，我们主要在建立自我与面具——读书、择业、成家、在社会里找到位置；到了中年，许多人突然感到“外在一切都还不错，却说不出哪里不对劲”，抑郁、空虚感、强烈而怪异的梦境开始出现，这正是个体化召唤意识**转向内在**的信号。

从荣格视角看，真正的个体化至少包含几个关键工作：其一是**阴影整合**——承认并逐步收回那些被我们自己打入黑名单的性格面向；其二是与**阿尼玛/阿尼姆斯**建立比较成熟的关系，不再把内在异性完全投射在伴侣身上，而能在自己心灵里与这位“内在他者”对话；其三是逐渐觉察自我并非心灵唯一中心，而是更大整体（本我/大我）中的一部分，学会让自我围绕本我调节轴运转，而非试图膨胀成“唯一的主人”。

个体化的悖论在于：它一方面让人变得**极度个别化**——不再单纯用集体期待来定义自己，敢于成为与众不同的“这一个”；另一方面，又使人**更加连结于整体**——因为只有当你不再完全被人格面具和文化规范操控时，才可能真正感受到集体无意识那一层“人类共同命运”的脉动。于是，一个完成较多个体化工作的人，既不会轻易淹没在群众情绪中，也不会高高在上地抽离世界，而是能以独特的姿态参与人类整体的心理进化。

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Individuation | Becoming undivided | Jung's life goal |
| Ego-Self Axis | Conscious-unconscious relation | Central relationship |
| Shadow Integration | Accept rejected self | Essential work |
| Mid-life Crisis | Turning point | Triggers inward turn |

#### Core Points

- **Becoming undivided**: Integration of all psyche aspects into whole
- **First half**: Ego development, persona building, outer adaptation
- **Mid-life turn**: Crisis triggers inward turn to unconscious
- **Second half**: Shadow work, anima/animus, archetype engagement
- **Goal**: Ego-Self axis not ego-inflation or dissolution
- **Two dangers**: Persona identification or archetypal inflation
- **Paradox**: More individual yet more connected to collective

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Individuation: Lifelong process of psychological wholeness. Not individualism but becoming "in-dividual" (undivided). Two halves of life structure. Ego-Self axis as goal. Two dangers: persona identification and archetypal inflation.
- **中文**: 个体化:终身心理完整过程。非个人主义而是成为"不可分割的个体"。人生两半结构。自我-本我轴为目标。两种危险:人格面具认同和原型膨胀。

**Narrative Snippets**:
- `[ns_jung_012]` `[trigger: individuation_definition]` `[factor_trigger: jung_individuation AND jung_self_realization]` `[role: 主干]` Individuation means becoming an 'in-dividual'—becoming one's own self, self-realization. → Source Text
- `[ns_jung_013]` `[trigger: false_wrappings]` `[factor_trigger: jung_persona AND jung_primordial]` `[role: 主干依赖]` The aim is to divest the self of false wrappings of persona and the suggestive power of primordial images. → Source Text
- `[ns_jung_014]` `[trigger: midlife_crisis]` `[factor_trigger: jung_midlife AND jung_turn_inward]` `[role: 条件分支]` Mid-life crisis triggers inward turn when persona no longer satisfies and unconscious demands attention. → English Paraphrase
- `[ns_jung_015]` `[trigger: ego_self_axis]` `[factor_trigger: jung_ego AND jung_self]` `[role: 总结]` Goal is ego-Self axis—conscious ego relating appropriately to larger Self, maintaining distinction while in dialogue. → English Paraphrase
- `[ns_jung_016]` `[trigger: individuation_paradox]` `[factor_trigger: jung_individual AND jung_collective]` `[role: 主干]` Process makes you MORE individual (unique) yet MORE connected (to collective unconscious, humanity). → English Paraphrase"""
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
        book_id="collected_works",
        chapter="",
        l1_anchor="cw_v1.0.0_source_text_003_L1",
    )
    version: str = "1.0.0"
