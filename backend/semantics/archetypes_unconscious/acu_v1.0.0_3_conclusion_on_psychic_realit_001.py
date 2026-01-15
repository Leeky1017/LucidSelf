"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.491746
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
    semantic_id="acu_v1.0.0_3_conclusion_on_psychic_realit_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 3ConclusionOnPsychicRealit(SemanticEntry):
    """
    **Source Text** (¶195-198, Lines 3220-3280):

> [195] The psyche is an extremely complex phenomenon—...
    """
    
    original_text: str = """**Source Text** (¶195-198, Lines 3220-3280):

> [195] The psyche is an extremely complex phenomenon—it is not easy to make clear to oneself that the "soul" or "psyche" is no mere figure of speech but an empirical reality. The psyche is not just a matter of concepts, but living reality with powers of its own.
>
> [198] The archetype is purely formal, empty in itself—it is a "facultas praeformandi," a possibility of representation given a priori. But when it becomes conscious and is filled with individual experience, it becomes the image—vivid, living, and overwhelming. What we call "image" is the result of subjective and objective factors.

**English Paraphrase**:
- Psyche = empirical reality, not figure of speech
- Psyche has living powers of its own
- Archetype = purely formal, empty (facultas praeformandi)
- Filled with individual experience → becomes vivid image
- Image = result of subjective + objective factors

**中文诠释**:
- 心灵 = 经验现实，非修辞
- 心灵有自己的活力量
- 原型 = 纯形式的、空的（预形成能力）
- 填入个人经验 → 成为生动意象
- 意象 = 主观+客观因素的结果

**Narrative Snippets**:
- `[ns_cw9i_III_195]` `[trigger: psyche_reality]` `[factor_trigger: jung_psyche AND jung_reality]` `[role: 主干]` Psyche is empirical reality with powers of its own—not mere figure of speech. → ¶195
- `[ns_cw9i_III_198]` `[trigger: archetype_formal]` `[factor_trigger: jung_archetype AND jung_image]` `[role: 总结]` Archetype = purely formal (facultas praeformandi); filled with experience becomes vivid image. → ¶198"""
    normalized_text_zh: str = """"""
    subject: str = "3 Conclusion on Psychic Reality (¶195-198)"
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
        book_id="archetypes_unconscious",
        chapter="",
        l1_anchor="acu_v1.0.0_3_conclusion_on_psychic_realit_001_L1",
    )
    version: str = "1.0.0"
