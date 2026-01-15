"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237869
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
    semantic_id="ap_v1.0.0_entry_1__jung_s_synchronistic__001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry1JungSSynchronistic(SemanticEntry):
    """
    **Source Text** (Lines 3275-3416):
> The Synchronistic Principle... Jung made these significant stat...
    """
    
    original_text: str = """**Source Text** (Lines 3275-3416):
> The Synchronistic Principle... Jung made these significant statements: "The science of the Yi King is not based on the causality principle, but on a principle (hitherto unnamed because not met with among us) which I have tentatively called the synchronistic principle... Thus I found that there are psychic parallelisms which cannot be related to each other causally, but which must be connected through another sequence of events. This connection seemed to me to be essentially provided in the fact of the relative simultaneity, therefore the expression 'synchronistic.' It seems indeed, as though time, far from being an abstraction, is a concrete continuum which contains qualities or basic conditions manifesting simultaneously in various places..."
>
> "Astrology would be a large scale example of synchronism, if it had at its disposal thoroughly tested findings... In so far as there are any really correct astrological deductions, they are not due to the effects of the constellations, but to our hypothetical time-characters. In other words, whatever is born or done this moment, has the qualities of this moment of time."

**Key Term Analysis**:
- **Synchronistic principle**: `non-causal connection` / `relative simultaneity` / `Yi King basis`
- **Time as concrete continuum**: `contains qualities` / `manifests simultaneously` / `not abstraction`
- **Astrology as synchronism**: `large-scale example` / `time-characters` / `moment's qualities`

**English Paraphrase (Primary Language)**:
Jung formulated the "synchronistic principle" from his psychological practice—a non-causal connection based on "relative simultaneity." Time is not abstraction but "a concrete continuum which contains qualities or basic conditions manifesting simultaneously in various places."

Astrology exemplifies synchronism: "whatever is born or done this moment, has the qualities of this moment of time"—not due to constellation effects, but "hypothetical time-characters." This validates Rudhyar's time-philosophy and astrology's foundation in moment-quality.

**Complete Chinese Interpretation (Secondary Language)**:
Jung从其心理学实践中形成了"共时性原则"——基于"相对同时性"的非因果联系。时间不是抽象而是"包含品质或基本条件的具体连续体，在各处同时显现"。

占星学体现共时性："在这一刻出生或完成的一切，都具有这一时刻的品质"——不是由于星座效应，而是"假设的时间特性"。这验证了Rudhyar的时间哲学和占星学以时刻品质为基础。

**Narrative Snippets**:
- `[ns_aop_111]` `[trigger: synchronistic]` `[factor_trigger: astro_synchron AND astro_sync_struct]` `[role: 主干]` Jung's synchronistic principle: non-causal connection through simultaneity, time as quality-container. → L3305-3322
- `[ns_aop_112]` `[trigger: astrology_synchronism]` `[factor_trigger: astro_sync_example AND astro_sync_struct]` `[role: 总结]` Astrology = large-scale synchronism: moment-born has moment's qualities, not constellation effects. → L3400-3416"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 1: Jung's Synchronistic Principle"
    factor_refs: list = ['astro_synchronistic', 'astro_time_char']
    
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
        book_id="astrology_personality",
        chapter="",
        l1_anchor="ap_v1.0.0_entry_1__jung_s_synchronistic__001_L1",
    )
    version: str = "1.0.0"
