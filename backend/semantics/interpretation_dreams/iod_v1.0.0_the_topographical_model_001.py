"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.465579
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
    semantic_id="iod_v1.0.0_the_topographical_model_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class TheTopographicalModel(SemanticEntry):
    """
    **Source Text**:
"The unconscious is the larger circle which includes within itself the smaller circ...
    """
    
    original_text: str = """**Source Text**:
"The unconscious is the larger circle which includes within itself the smaller circle of the conscious; everything conscious has its preliminary step in the unconscious, whereas the unconscious may stop with this step and still claim full value as a psychic activity. Properly speaking, the unconscious is the real psychic; its inner nature is just as unknown to us as the reality of the external world."

"When we say that an unconscious idea strives for transference into the foreconscious in order later to penetrate consciousness, we do not mean that a second idea is to be formed situated in a new locality... we replace a topical mode of presentation by a dynamic; it is not the psychic formation that appears to us as the moving factor but the innervation of the same."

"Everything that can become an object of our internal perception is virtual, like the image in the telescope produced by the passage of the rays of light."

**Key Term Analysis**:

| Term | Definition | Significance |
|------|-----------|---------------|
| Unconscious | Larger circle containing consciousness | The "real psychic" |
| Consciousness | Smaller circle within unconscious | Sensory surface |
| Topographical Model | Spatial metaphor for psychic systems | First structural model |
| Dynamic View | Energy/cathexis perspective | Complements topography |
| Virtual Image | Perception as construction | Telescope metaphor |
| Real Psychic | Unconscious as fundamental reality | Revolutionary claim |

**English Paraphrase (Primary Language)**:

Section (f) presents Freud's most famous formulation: **the unconscious is the larger circle** containing the smaller circle of consciousness. "Everything conscious has its preliminary step in the unconscious, whereas the unconscious may stop with this step and still claim full value as a psychic activity."

This inverts traditional psychology: consciousness is not the whole of mind but a **limited surface**. "Properly speaking, the unconscious is the real psychic"—its nature is as unknown to us as external reality itself.

Freud then refines his **topographical model**: when we say ideas "move" between systems, we don't mean physical relocation. The metaphor is **dynamic, not spatial**: what changes is the **energy cathexis** attached to ideas, not their location. The telescope image captures this: what we perceive internally is "virtual, like the image in the telescope"—a construction, not direct access to psychic reality.

This section establishes the **primacy of the unconscious**: consciousness is derivative, secondary, partial. The unconscious is the foundation of psychic life.

**Complete Chinese Interpretation (Secondary Language)**:

(f)部分呈现弗洛伊德最著名的表述：**无意识是更大的圆**，包含意识这个更小的圆。"一切意识都有其在无意识中的初步阶段，而无意识可以停留在这一阶段，仍然拥有完整的心理活动价值。"

这颠覆了传统心理学：意识不是心灵的全部，而是一个**有限的表面**。"严格来说，无意识才是真正的心理现实"——其本质对我们来说像外部现实一样是未知的。

然后弗洛伊德精炼了他的**拓扑模型**：当我们说观念在系统之间"移动"时，我们不是指物理位置的改变。这个隐喻是**动态的，而非空间的**：改变的是附着于观念的**能量贯注**，而非其位置。望远镜意象捕捉了这一点：我们内在知觉的是"虚像，如同望远镜中的影像"——一种建构，而非对心理现实的直接接触。

这一部分确立了**无意识的首要地位**：意识是派生的、次要的、部分的。无意识是心理生活的基础。

**Core Points**:

- Unconscious = larger circle; consciousness = smaller circle within
- Everything conscious has preliminary step in unconscious
- "The unconscious is the real psychic"
- Topographical model: systems as regions
- Dynamic view: cathexis/energy changes, not locations
- Telescope metaphor: perception is construction (virtual image)
- Consciousness is surface; unconscious is foundation

**Detailed Explanation**:

This is Freud's **epistemological revolution**: the "real" psyche is not what we experience consciously but the vast unconscious substrate. Consciousness is like the tip of the iceberg—visible but not representative of the whole.

The **larger circle metaphor** has become iconic. Consciousness is not merely "accompanied by" unconscious processes; it **emerges from** them. Every conscious thought was first unconscious; the reverse is not true. This gives the unconscious **logical priority**.

The **dynamic correction** to topography is crucial. Early readers mistook Freud's systems (Ucs., Pcs., Cs.) for brain locations. Freud clarifies: these are **functional systems**, not places. What "moves" between them is **cathexis** (energy investment), not ideas themselves. An idea doesn't relocate; its energy state changes.

The **telescope metaphor** anticipates constructivism: we don't perceive psychic reality directly any more than we see objects directly. Consciousness is a **sensory surface** that receives transformed products of unconscious processing. What we introspect is already processed, already "interpreted" by the psychic apparatus.

**Textual Criticism & Variant Analysis (Bilingual)**:

- **English**: "The unconscious is the real psychic" (German: Das Unbewußte ist das eigentlich reale Psychische) became Freud's most quoted formulation.
- **中文**: "无意识是真正的心理现实"（德语：Das Unbewußte ist das eigentlich reale Psychische）成为弗洛伊德最常被引用的表述。这一命题对20世纪哲学、文学、艺术产生了革命性影响。

**Narrative Snippets**:

- `[ns_freud_psy_013]` `[trigger: larger_circle]` `[factor_trigger: dream_unconscious]` `[role: 主干]` The unconscious is the larger circle which includes the smaller circle of consciousness—everything conscious has its preliminary step in the unconscious. → Freud Ch.VII #Unconscious
- `[ns_freud_psy_014]` `[trigger: real_psychic]` `[factor_trigger: dream_unconscious]` `[role: 主干依赖]` Properly speaking, the unconscious is the real psychic; its inner nature is just as unknown to us as the reality of the external world. → Freud Ch.VII #Unconscious
- `[ns_freud_psy_015]` `[trigger: dynamic_view]` `[factor_trigger: dream_topographical_model]` `[role: 条件分支]` We replace a topical mode of presentation by a dynamic—it is not the psychic formation that moves but the cathexis; perception is virtual like the telescope image. → Freud Ch.VII #Unconscious"""
    normalized_text_zh: str = """"""
    subject: str = "The Topographical Model"
    factor_refs: list = ['system_ucs', 'system_cs', 'larger_circle', 'real_psychic', 'virtual_image']
    
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
        l1_anchor="iod_v1.0.0_the_topographical_model_001_L1",
    )
    version: str = "1.0.0"
