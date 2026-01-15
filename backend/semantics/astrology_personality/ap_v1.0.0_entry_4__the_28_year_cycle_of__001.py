"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238101
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
    semantic_id="ap_v1.0.0_entry_4__the_28_year_cycle_of__001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry4The28YearCycleOf(SemanticEntry):
    """
    **Source Text** (Lines 7555-7706):
> The Unfolding of the Individual Self... the wheel of houses is ...
    """
    
    original_text: str = """**Source Text** (Lines 7555-7706):
> The Unfolding of the Individual Self... the wheel of houses is inherently to be interpreted in terms of becoming rather than of static being. It is a time-pattern; a pattern of unfoldment...
>
> The symbolism of these "three days" is susceptible of an infinite number of applications... Each day represents... a cycle of rotation of man's individual self around its spiritual axis...
>
> This 28-year cycle can be plotted out on the birth-chart... When the Ascendant is reached again the first cycle of twenty-eight years is closed, and the second begins, ending with the 56th year; the third 28th year cycle follows, coming to a close at the age of 84, which marks the theoretical and symbolical completion of man's inner temple.

**Key Term Analysis**:
- **28-year cycle**: `one "day" of individuation` / `rotation of self around spiritual axis`
- **Three cycles (84 years)**: `0-28 (body/race-self)` / `28-56 (soul/individual-self)` / `56-84 (spirit/universal-self)`
- **7-year subdivisions**: `each quarter = 7 years` / `progressive development of functions`
- **Temple building**: `foundation (body)` / `first story (soul)` / `dome (spirit)`

**English Paraphrase (Primary Language)**:
The houses represent "becoming," not static being—a time-pattern. Each 28-year cycle = one "day" of individuation. Three cycles (84 years total = Uranus cycle):
- **0-28**: Body/race-self (foundation)
- **28-56**: Soul/individual-self (first story)  
- **56-84**: Spirit/universal-self (dome)

At 84, "the theoretical and symbolical completion of man's inner temple."

**Complete Chinese Interpretation (Secondary Language)**:
宫位代表"成为"而非静态存在——一种时间模式。每个28年周期=个体化的一"天"。三个周期（共84年=天王星周期）：
- **0-28**：身体/种族自我（地基）
- **28-56**：灵魂/个体自我（一层）
- **56-84**：精神/宇宙自我（穹顶）

在84岁，"人类内在神殿的理论和象征性完成。"

**Narrative Snippets**:
- `[ns_aop_161]` `[trigger: 28_year_cycle]` `[factor_trigger: astro_cycle_28]` `[role: 主干]` 28-year cycle: one "day" of individuation, rotation around spiritual axis. → L7571-7576
- `[ns_aop_162]` `[trigger: three_births]` `[factor_trigger: astro_three_births AND astro_84_temple]` `[role: 主干依赖]` Three births: body (0-28), soul (28-56), spirit (56-84) = 84 years total. → L7643-7670"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 4: The 28-Year Cycle of Individuation"
    factor_refs: list = ['cycle_28', 'three_births']
    
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
        l1_anchor="ap_v1.0.0_entry_4__the_28_year_cycle_of__001_L1",
    )
    version: str = "1.0.0"
