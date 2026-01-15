"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.113503
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
    semantic_id="tis_v1.0.0_pisces___the_mystic__mutable_w_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class PiscesTheMysticMutableW(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Mutable Water | Fluid ad...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Mutable Water | Fluid adaptation | Element |
| Transcendence | See through | Goal |
| Compassion | Feel interconnection | Gift |
| Sacred Imagination | Door to insight | Method |

**Source Text**: "Two Fishes in opposite directions—but the Ocean itself: the infinite, boundless, source of all life. Pisces has come to experience transcendence—realize world is construct of consciousness. The endpoint is reorientation: recognizing life is dream, we are dreamers."

**English Paraphrase**: **Pisces** = **Mutable Water** embodying **transcendence, compassion, and boundary dissolution**. Archetype: mystic/poet dissolving into oceanic unity.

**Core**: Let go (release attachment to objective world), meditation (turn attention to awareness itself), creativity (art/music/fantasy as reality), compassion (feel interconnection), imagination (inner worlds as real), fluidity (adapt, shift, mirror). **Shadow**: Escapism (escape through drugs/alcohol/fantasy), victimhood (passive, helpless, waiting for rescue), deception (blur boundaries, lose own truth). **Challenge**: Transcendence doesn't mean checking out; engage with life while seeing through it.

**Chinese**: 双鱼座=变动水象体现超越、慈悲和边界溶解。核心：放手、冥想、创造、慈悲、想象、流动。阴影：逃避、受害者、欺骗。挑战：超越非逃离；参与生活同时看穿它。

**East**: 双鱼↔癸水阴柔/正印慈悲 (yin water compassion)

#### Narrative Snippets

- `[ns_innersky_pisces_001]` `[trigger: sign_pisces]` `[factor_trigger: sign_pisces AND element_water]` `[role: 主干]` Two Fishes in opposite directions—but the Ocean itself: the infinite, boundless, source of all life. Pisces has come to experience transcendence—realize world is construct of consciousness. → The Inner Sky Ch.4 #Pisces
- `[ns_innersky_pisces_002]` `[trigger: sign_pisces AND astro_strength]` `[factor_trigger: astro_sign_pisces]` `[role: 主干依赖]` The endpoint is reorientation: recognizing life is dream, we are dreamers. Letting go, meditation, creativity, compassion, imagination, fluidity. → The Inner Sky Ch.4 #Pisces
- `[ns_innersky_pisces_003]` `[trigger: sign_pisces AND astro_shadow]` `[factor_trigger: astro_sign_pisces AND astro_state_dysfunction]` `[role: 条件分支]` Shadow: escapism (escape through drugs/alcohol/fantasy), victimhood (passive, helpless, waiting for rescue), deception (blur boundaries, lose own truth). → The Inner Sky Ch.4 #Pisces
- `[ns_innersky_pisces_004]` `[trigger: sign_pisces AND astro_challenge]` `[factor_trigger: astro_sign_pisces]` `[role: 总结]` Transcendence doesn't mean checking out; engage with life while seeing through it. The challenge is grounded mysticism. → The Inner Sky Ch.4 #Pisces"""
    normalized_text_zh: str = """"""
    subject: str = "Pisces - The Mystic (Mutable Water)"
    factor_refs: list = ['new_candidate', 'sign_pisces', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        book_id="the_inner_sky",
        chapter="",
        l1_anchor="tis_v1.0.0_pisces___the_mystic__mutable_w_001_L1",
    )
    version: str = "1.0.0"
