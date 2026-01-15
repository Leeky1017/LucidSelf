"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238169
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
    semantic_id="ap_v1.0.0_entry_1__personality_definitio_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry1PersonalityDefinitio(SemanticEntry):
    """
    **Source Text** (Lines 8646-8768):
> We defined "personality" as "a synthesis of patterns of behavio...
    """
    
    original_text: str = """**Source Text** (Lines 8646-8768):
> We defined "personality" as "a synthesis of patterns of behavior; as the sum total of all the outer motions and emotions of the human being..." Personality, to us and presumably to men like General Smuts and most modern psychologists, is the whole human being in operation...
>
> The Sun, however, should not be considered as the symbol of the Self. It represents the power of the Self; but the Self itself is not only power. It is power in relation to form... the Self, if its nature can at all be ascertained astrologically, is the relation between the Sun and the axes, horizon and meridian.

**Key Term Analysis**:
- **Personality**: `synthesis of behavior patterns` / `whole human being in operation` / `not outer vs inner`
- **Sun as power**: `represents power of Self` / `not Self itself` / `integrating energy`
- **Self astrologically**: `relation Sun to axes` / `horizon and meridian`
- **Central fixation**: `Dr. Bates eye concept` / `psychological parallel`

**English Paraphrase (Primary Language)**:
Personality = "synthesis of patterns of behavior," the whole human being in operation. NOT outer being vs individuality.

The Sun represents the **power** of the Self—not the Self itself. "The Self is the relation between the Sun and the axes, horizon and meridian." The Sun's house-position shows the phase of selfhood and life period where integrative power operates most strongly.

**Complete Chinese Interpretation (Secondary Language)**:
人格 = "行为模式的综合"，运作中的完整人。不是外在存在vs个性。

太阳代表自性的**力量**——而非自性本身。"自性是太阳与轴线、地平线和子午线之间的关系。"太阳的宫位显示自性和生命阶段中整合力量最强烈运作的相位。

**Narrative Snippets**:
- `[ns_aop_175]` `[trigger: personality_def]` `[factor_trigger: astro_personality_definition]` `[role: 主干]` Personality = synthesis of behavior patterns, whole human being in operation. → L8648-8666
- `[ns_aop_176]` `[trigger: sun_integrator]` `[factor_trigger: astro_sun_as_integrator]` `[role: 总结]` Sun = power of Self (not Self itself); Self = relation Sun to axes. → L8811-8823"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 1: Personality Definition and the Sun as Integrator"
    factor_refs: list = ['personality_def', 'sun_integrator']
    
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
        l1_anchor="ap_v1.0.0_entry_1__personality_definitio_001_L1",
    )
    version: str = "1.0.0"
