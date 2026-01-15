"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.309748
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
    semantic_id="pit_v1.0.0_jupiter_in_the_third_house__木星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class JupiterInTheThirdHouse木星(SemanticEntry):
    """
    **Source Text** (Lines 10224-10258):
> Increase contacts in immediate surroundings. Don't have to go...
    """
    
    original_text: str = """**Source Text** (Lines 10224-10258):
> Increase contacts in immediate surroundings. Don't have to go far to find expanding experiences. Opportunity for advanced training. Concern with communication, may do writing. Extended travel may be necessary. Relationships with relatives very good. Old thought patterns broadened. Thinking less limited by prejudices. Attitude more generous, understanding, tolerant. Plans for future larger and more expansive. Communication with others better than usual.

**English Paraphrase**: Increase local contacts. Expanding experiences nearby. Training opportunities. May write. Good with relatives. Thinking broadened, less prejudiced. More tolerant. Plans larger. Communication better.

**Complete Chinese Interpretation**: 增加本地联系。附近的扩展体验。培训机会。可能写作。与亲戚关系好。思维拓宽，减少偏见。更宽容。计划更大。沟通更好。

**Narrative Snippets**:
- `[ns_pit_ju003]` `[trigger: jupiter_transit_house_3]` `[factor_trigger: astro_transit_jupiter AND astro_house_3]` `[role: 主干]` Expand local contacts. Training opportunities. Thinking broadened. Communication better. → PIT Ch9 Jupiter-3H"""
    normalized_text_zh: str = """"""
    subject: str = "Jupiter in the Third House (木星过境第三宫)"
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
        l1_anchor="pit_v1.0.0_jupiter_in_the_third_house__木星_001_L1",
    )
    version: str = "1.0.0"
