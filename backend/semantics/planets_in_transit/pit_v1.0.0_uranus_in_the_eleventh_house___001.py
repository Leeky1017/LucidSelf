"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.206892
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
    semantic_id="pit_v1.0.0_uranus_in_the_eleventh_house___001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class UranusInTheEleventhHouse(SemanticEntry):
    """
    **Source Text** (Lines 14773-14796):
> Potential revolution in hopes and expectations. See that new ...
    """
    
    original_text: str = """**Source Text** (Lines 14773-14796):
> Potential revolution in hopes and expectations. See that new and different lifestyles possible. Won't settle for as little as before. Also house of friends and group activities—attracted to new kinds of friends who challenge old ways. Even long-time friends may challenge you with new experiences. Friends may get into upsetting situations. May need to rebel against group pressures—feel others trying to make you into something you're not. Need to establish yourself as individual against their pressure. If friends conservative, situation worse—may look for new friends fitting better. We identify with groups and expectations conditioned by them. Either seek new freedom through groups or rebel against their standards. Uranus has natural affiliation with 11H (Aquarius). One of more favorable transits if willing to be flexible.

**English Paraphrase**: Revolution in hopes and expectations. Won't settle for less. Attracted to new friends challenging old ways. May rebel against group pressures. Establish individuality. Uranus naturally affiliated with 11H—favorable transit if flexible.

**Complete Chinese Interpretation**: 希望和期望的革命。不会满足于更少。被挑战旧方式的新朋友吸引。可能反抗群体压力。建立个性。天王星与第十一宫天然关联——如果灵活则是有利的行运。

**Narrative Snippets**:
- `[ns_pit_ur011]` `[trigger: uranus_transit_house_11]` `[factor_trigger: astro_transit_uranus AND astro_house_11]` `[role: 主干]` Revolution in hopes. New friends. May rebel against groups. Favorable if flexible. → PIT Ch11 Uranus-11H"""
    normalized_text_zh: str = """"""
    subject: str = "Uranus in the Eleventh House (天王星过境第十一宫)"
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
        l1_anchor="pit_v1.0.0_uranus_in_the_eleventh_house___001_L1",
    )
    version: str = "1.0.0"
