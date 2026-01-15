"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238111
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
    semantic_id="ap_v1.0.0_entry_5__seven_year_periods_an_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry5SevenYearPeriodsAn(SemanticEntry):
    """
    **Source Text** (Lines 7710-7843):
> It also verifies the ancient "occult" idea of the division of h...
    """
    
    original_text: str = """**Source Text** (Lines 7710-7843):
> It also verifies the ancient "occult" idea of the division of human life into 7-year cycles, each of which marks the unfolding of one particular aspect of the individual's character...
>
> The first seven years see the development of the power of self-awareness, or intuition... From the age of seven to that of fourteen, the feelings mature... At fourteen, true contacts with the outer world begin... At twenty-one, mind... becomes consolidated by public life...
>
> The supremely individuated personality reveals the most perfectly in its outline of character, consciousness and destiny the form of generic Man. The most individual becomes the most universal.

**Key Term Analysis**:
- **7-year cycles**: `unfoldment of character aspects` / `corresponds to house progression`
- **0-7**: `intuition, self-awareness` / `animistic stage`
- **7-14**: `feelings mature` / `creative self-expression` / `puberty crisis (6th house)`
- **14-21**: `sensation, outer world` / `sexual development` / `fear of adjustment`
- **21-28**: `thinking consolidated` / `social responsibility` / `discrimination crisis (12th house)`
- **Paradox**: `most individual = most universal` / `solar Hero, Avatar`

**English Paraphrase (Primary Language)**:
The seven-year cycles:
- **0-7**: Intuition/self-awareness develops (animistic stage)
- **7-14**: Feelings mature, creative self-expression, puberty crisis
- **14-21**: Sensation develops, outer world contact, sexual awakening
- **21-28**: Thinking consolidated, social responsibility, discrimination crisis

"The supremely individuated personality reveals... the form of generic Man. The most individual becomes the most universal."

**Complete Chinese Interpretation (Secondary Language)**:
七年周期：
- **0-7**：直觉/自我觉知发展（万物有灵阶段）
- **7-14**：感受成熟，创造性自我表达，青春期危机
- **14-21**：感官发展，外在世界接触，性觉醒
- **21-28**：思维巩固，社会责任，辨别危机

"最高度个体化的人格揭示……通用人类的形式。最个体的成为最普遍的。"

**Narrative Snippets**:
- `[ns_aop_163]` `[trigger: seven_year_cycles]` `[factor_trigger: astro_cycles_7year]` `[role: 主干]` Seven-year cycles: 0-7 intuition, 7-14 feeling, 14-21 sensation, 21-28 thinking. → L7710-7756
- `[ns_aop_164]` `[trigger: most_individual_universal]` `[factor_trigger: astro_paradox_individual AND astro_indiv_univ]` `[role: 总结]` Paradox: most individual = most universal, solar Hero, Avatar. → L7837-7842"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 5: Seven-Year Periods and Developmental Stages"
    factor_refs: list = ['cycles_7year', 'paradox_indiv']
    
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
        l1_anchor="ap_v1.0.0_entry_5__seven_year_periods_an_001_L1",
    )
    version: str = "1.0.0"
