"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.309871
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
    semantic_id="pit_v1.0.0_jupiter_in_the_tenth_house__木星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class JupiterInTheTenthHouse木星(SemanticEntry):
    """
    **Source Text** (Lines 10432-10459):
> Attention turns to profession, career, status, reputation. Tr...
    """
    
    original_text: str = """**Source Text** (Lines 10432-10459):
> Attention turns to profession, career, status, reputation. Try hard to move ahead—reasonable effort should result in considerable progress. Time of getting ahead, but observe cautions. Avoid being overbearing, domineering, arrogant. Some have trouble with superiors—inflated ego. Review real accomplishments. Most people underrate achievements—likely to receive recognition. Expect promotion, public recognition, esteem. More confident about yourself. May travel for work, increased dealings with foreigners. May change to Jupiter-related field: medicine, law, higher education, travel.

**English Paraphrase**: Career and reputation focus. Move ahead with effort. Avoid inflated ego and arrogance. Most receive recognition and promotion. More confident. May travel for work or change to Jupiter-related field.

**Complete Chinese Interpretation**: 职业和声誉焦点。通过努力前进。避免膨胀的自我和傲慢。大多数人获得认可和晋升。更自信。可能因工作旅行或转入木星相关领域。

**Narrative Snippets**:
- `[ns_pit_ju010]` `[trigger: jupiter_transit_house_10]` `[factor_trigger: astro_transit_jupiter AND astro_house_10]` `[role: 主干]` Career advancement. Recognition and promotion likely. Avoid inflated ego. → PIT Ch9 Jupiter-10H"""
    normalized_text_zh: str = """"""
    subject: str = "Jupiter in the Tenth House (木星过境第十宫)"
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
        book_id="planets_in_transit",
        chapter="",
        l1_anchor="pit_v1.0.0_jupiter_in_the_tenth_house__木星_001_L1",
    )
    version: str = "1.0.0"
