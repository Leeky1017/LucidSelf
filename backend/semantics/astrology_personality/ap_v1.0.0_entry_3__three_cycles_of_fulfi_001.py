"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238329
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
    semantic_id="ap_v1.0.0_entry_3__three_cycles_of_fulfi_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry3ThreeCyclesOfFulfi(SemanticEntry):
    """
    **Source Text** (Lines 14205-14313):
> We have thus three cycles, each of which represents a fullnes...
    """
    
    original_text: str = """**Source Text** (Lines 14205-14313):
> We have thus three cycles, each of which represents a fullness of zodiacal experience... the sidereal day, the solar year, and the Great Polar Cycle. They refer respectively to the individual factor, the collective factor and the planetary factor...
>
> The main points to grasp in such a complex problem are: 1) that "primary directions" refer to the cycle of axial rotation of the Earth and to the individual factor in man; 2) that "secondary progressions" refer to the cycle of orbital revolution and to the collective factor in man; 3) that both are related expressions of the fact that birth does not mean the fulfillment of personality...

**Key Term Analysis**:
- **Three cycles**: `sidereal day (individual)` / `solar year (collective)` / `370-year (personality)`
- **Primary directions**: `axial rotation` / `individual factor` / `4 min = 1 year`
- **Secondary progressions**: `orbital revolution` / `collective factor` / `1 day = 1 year`
- **Transits**: `370-year cycle` / `personality factor` / `1 year = 1 year`

**English Paraphrase (Primary Language)**:
Three cycles of fulfillment:
1. **Sidereal day** → Individual factor → Primary directions (4 min = 1 year)
2. **Solar year** → Collective factor → Secondary progressions (1 day = 1 year)
3. **370-year cycle** → Personality factor → Transits (1 year = 1 year)

"Birth does not mean the fulfillment of personality"—it's a continuing process at three levels: individual, collective, organic (personality).

**Complete Chinese Interpretation (Secondary Language)**:
三个实现周期：
1. **恒星日** → 个体因素 → 主限推运（4分钟 = 1年）
2. **太阳年** → 集体因素 → 次限推运（1天 = 1年）
3. **370年周期** → 人格因素 → 过境（1年 = 1年）

"出生不意味着人格的实现"——它是一个在三个层面上持续的过程：个体、集体、有机（人格）。

**Narrative Snippets**:
- `[ns_aop_211]` `[trigger: three_cycles]` `[factor_trigger: astro_cycles_fulfillment AND astro_primary AND astro_secondary AND astro_transits]` `[role: 主干]` Three cycles: sidereal day (individual), solar year (collective), 370-year (personality). → L14230-14237
- `[ns_aop_212]` `[trigger: progression_types]` `[factor_trigger: astro_prog_types AND astro_primary AND astro_secondary]` `[role: 总结]` Primary = axial/individual; Secondary = orbital/collective; Transits = personality factor. → L14292-14308"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 3: Three Cycles of Fulfillment - Primary, Secondary, Transits"
    factor_refs: list = ['primary_dir', 'secondary_prog', 'transits']
    
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
        l1_anchor="ap_v1.0.0_entry_3__three_cycles_of_fulfi_001_L1",
    )
    version: str = "1.0.0"
