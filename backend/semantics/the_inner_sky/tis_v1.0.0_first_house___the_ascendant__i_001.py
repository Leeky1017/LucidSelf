"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.093925
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
    semantic_id="tis_v1.0.0_first_house___the_ascendant__i_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class FirstHouseTheAscendantI(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Optimal Mask | Best-fit ...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Optimal Mask | Best-fit persona | Core concept |
| Identity Channel | Psyche→action | Function |
| Personality Vehicle | Soul's tool | Expression |
| Antidote to Madness | Coherent self | Protection |

#### Source Text

"Life requires that we have a personality—and a personality is always a role we play, always less than what we truly are. A personality is always a mask. The first house symbolizes our optimal mask, the outer expression that best serves our inner needs. It channels the totality of the birthchart into the world of action."

#### English Paraphrase

The **First House** (Ascendant) is the **mask of personality**—not a fake disguise, but the necessary vehicle for the soul to act in the world. It is the interface between the inner self and outer reality.

**Nature of the Ascendant**:
- **Optimal Mask**: The role we play that best protects and expresses our inner nature.
- **Channel for Action**: How we translate complex inner drives into simple, effective action.
- **First Impression**: What others see first; our style, demeanor, and physical presentation.
- **Antidote to Madness**: Provides a coherent identity structure so we don't feel scattered or crazy.

**Function**:
- **Simplification**: Reduces the complexity of the psyche into a manageable persona.
- **Protection**: Shields the vulnerable core (Sun/Moon) from the raw impact of the world.
- **Navigation**: How we start things, how we handle new situations.

**Mastery**:
When navigated successfully, the First House produces **clarity, decisiveness, and poise**. We feel in control of our life direction. Unsuccessful navigation leads to identity confusion, paralysis, or defensive tyranny over others.

#### Complete Chinese Interpretation

**第一宫**（上升点）是**人格面具**——并非虚假的伪装，而是灵魂在世间行动所必需的载体。它是内在自我与外在现实之间的接口。

**上升点的本质**：
- **最佳面具**：最能保护和表达我们内在本质的角色。
- **行动通道**：我们将复杂的内在驱动力转化为简单、有效行动的方式。
- **第一印象**：他人首先看到的；我们的风格、举止和身体呈现。
- **疯狂的解药**：提供连贯的身份结构，使我们不会感到涣散或疯狂。

**功能**：
- **简化**：将心灵的复杂性简化为可管理的人格面具。
- **保护**：屏蔽脆弱的核心（太阳/月亮）免受世界的直接冲击。
- **导航**：我们如何开始事物，如何处理新情况。

**掌握**：
当成功驾驭时，第一宫产生**清晰、果断和镇定**。我们感到对自己生活方向的掌控。不成功的驾驭导致身份混乱、瘫痪，或对他人进行防御性的暴政。

#### Core Points

- The Ascendant is the "optimal mask" or vehicle for the soul.
- Channels total psyche into specific action.
- Interface between inner self and outer world.
- Provides identity clarity and protection.
- East parallel: 命宫/面相/元神 (Life Palace, Physiognomy, Original Spirit).

#### Detailed Explanation

The First House represents the **interface** between inner complexity and outer expression. Forrest's "optimal mask" concept is crucial: the mask is not false or inauthentic—it is the **necessary vehicle** through which the soul engages the world. Without a coherent personality, we would be paralyzed, unable to translate inner knowing into outer action.

The Ascendant functions as a **simplification mechanism**. The total psyche is too complex to express simultaneously; the First House channels this complexity into a workable, coherent identity. This explains why people with strong first house emphasis often appear confident and decisive—they have developed effective identity vehicles.

**Successful navigation** produces clarity, decisiveness, and poise. The person knows who they are and how to present themselves. **Unsuccessful navigation** creates identity confusion, paralysis, or defensive rigidity. The person may either have no clear sense of self, or may compensate for inner uncertainty by controlling others.

#### Narrative Snippets

- `[ns_innersky_h1_001]` `[trigger: house_1_general]` `[factor_trigger: astro_house_1 AND astro_house_framework]` `[role: 主干]` Life requires that we have a personality—and a personality is always a role we play, always less than what we truly are. A personality is always a mask. → The Inner Sky Ch.7 #1H
- `[ns_innersky_h1_002]` `[trigger: house_1_function]` `[factor_trigger: astro_house_1]` `[role: 主干依赖]` The first house symbolizes our optimal mask, the outer expression that best serves our inner needs. → The Inner Sky Ch.7 #1H
- `[ns_innersky_h1_003]` `[trigger: house_1_mastery]` `[factor_trigger: astro_house_1 AND astro_state_success]` `[role: 条件分支]` The more sensitively we respond to it, the stronger and more centered we feel. It gives a sense of autonomy, of self-knowledge, of authority over one's own life. → The Inner Sky Ch.7 #1H
- `[ns_innersky_h1_004]` `[trigger: house_1_sanity]` `[factor_trigger: astro_house_1]` `[role: 主干依赖]` If we define sanity as the ability to generate a reasonable, purposeful pattern of action, then the ascendant is the antidote to madness. → The Inner Sky Ch.7 #1H
- `[ns_innersky_h1_005]` `[trigger: house_1_dysfunction]` `[factor_trigger: astro_house_1 AND astro_state_dysfunction]` `[role: 条件分支]` A person with unresolved first-house problems—whose identity and direction are unfocused—often expresses his fear as a tyranny over other people. → The Inner Sky Ch.7 #1H
- `[ns_innersky_h1_006]` `[trigger: house_1_necessity]` `[factor_trigger: astro_house_1]` `[role: 总结]` We all have social identities, "personalities." And we need them. Without them we could only stare wide-eyed out into space. Those masks are created at the ascendant. → The Inner Sky Ch.7 #1H"""
    normalized_text_zh: str = """"""
    subject: str = "First House - The Ascendant (Identity)"
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
        book_id="the_inner_sky",
        chapter="",
        l1_anchor="tis_v1.0.0_first_house___the_ascendant__i_001_L1",
    )
    version: str = "1.0.0"
