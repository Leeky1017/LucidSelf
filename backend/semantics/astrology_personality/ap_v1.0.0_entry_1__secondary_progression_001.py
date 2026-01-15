"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238338
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
    semantic_id="ap_v1.0.0_entry_1__secondary_progression_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry1SecondaryProgression(SemanticEntry):
    """
    **Source Text** (Lines 14353-14427):
> Secondary Progressions: These progressions are the most gener...
    """
    
    original_text: str = """**Source Text** (Lines 14353-14427):
> Secondary Progressions: These progressions are the most generally used today... What they measure primarily are changes in the relation Earth-to-Sun; that is, in the relation of organism to organizing life-principle...
>
> Secondary progressions are calculated with reference to the apparent motion of the Sun, and the solar day—from noon to noon—is the basic unit. One such unit is said to equal one year of life...
>
> What is shown in the "progressed Sun" is the manner in which the process of personality-integration is carried on after birth... Solar progressions deal therefore with the development of the Self-in-manifestation.

**Key Term Analysis**:
- **Secondary progressions**: `most generally used` / `Earth-to-Sun relation` / `organism to life-principle`
- **Progressed Sun**: `personality integration` / `Self-in-manifestation` / `alchemical Great Work`
- **Solar factor**: `integration dominant` / `vital principle` / `Self within personality`
- **Progressed Moon**: `concrete events` / `karma cycles` / `outer changes`

**English Paraphrase (Primary Language)**:
Secondary progressions = "most generally used today." Measure "changes in Earth-to-Sun relation" = organism to organizing life-principle.

Progressed Sun shows "how personality-integration is carried on after birth"—the "development of Self-in-manifestation." The "alchemical Great Work."

Progressed Moon = "most specifically refers to concrete events"—karma cycles, outer changes, passing over house cusps.

**Complete Chinese Interpretation (Secondary Language)**:
次限推运 = "今天最普遍使用的"。测量"地球-太阳关系的变化" = 有机体与组织生命原则。

推运太阳显示"出生后人格整合如何进行"——"自性在显化中的发展"。"炼金术的伟大工作"。

推运月亮 = "最具体地指具体事件"——业力周期、外在变化、穿过宫位尖端。

**Narrative Snippets**:
- `[ns_aop_213]` `[trigger: secondary_prog]` `[factor_trigger: astro_secondary_method AND astro_prog_sun AND astro_sun]` `[role: 主干]` Secondary progressions: Earth-to-Sun changes; progressed Sun = personality integration. → L14357-14391
- `[ns_aop_214]` `[trigger: progressed_moon]` `[factor_trigger: astro_moon_prog AND astro_prog_moon]` `[role: 主干依赖]` Progressed Moon = concrete events, karma cycles, outer changes. → L14408-14414"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 1: Secondary Progressions - Solar Factor"
    factor_refs: list = ['prog_sun', 'prog_moon']
    
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
        l1_anchor="ap_v1.0.0_entry_1__secondary_progression_001_L1",
    )
    version: str = "1.0.0"
