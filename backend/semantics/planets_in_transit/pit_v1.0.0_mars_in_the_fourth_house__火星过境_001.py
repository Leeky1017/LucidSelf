"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.287962
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
    semantic_id="pit_v1.0.0_mars_in_the_fourth_house__火星过境_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MarsInTheFourthHouse火星过境(SemanticEntry):
    """
    **Source Text** (Lines 8349-8372):
> Stirs up energies from deepest unconscious. May behave compulsi...
    """
    
    original_text: str = """**Source Text** (Lines 8349-8372):
> Stirs up energies from deepest unconscious. May behave compulsively, inappropriately. May fight about something you don't understand. Be conscious of what you are doing. Great activity at home—working hard. Strong on having surroundings exactly as you want. Domestic strife if don't agree with housemates. Living with parents particularly difficult. Disputes over land ownership. Professional activities may face opposition—keep low profile.

**English Paraphrase**: Stirs unconscious energies. May act compulsively. Great home activity but possible domestic strife. Difficulty with parents. Opposition at work—keep low profile.

**Complete Chinese Interpretation**: 激起无意识能量。可能冲动行事。家庭活动多但可能有家庭冲突。与父母困难。工作中的反对——保持低调。

**Narrative Snippets**:
- `[ns_pit_ma004]` `[trigger: mars_transit_house_4]` `[factor_trigger: astro_transit_mars AND astro_house_4]` `[role: 主干]` Stirs unconscious energies. Home activity but domestic strife possible. Keep low profile at work. → PIT Ch8 Mars-4H"""
    normalized_text_zh: str = """"""
    subject: str = "Mars in the Fourth House (火星过境第四宫)"
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
        l1_anchor="pit_v1.0.0_mars_in_the_fourth_house__火星过境_001_L1",
    )
    version: str = "1.0.0"
