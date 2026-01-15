"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.237980
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
    semantic_id="pit_v1.0.0_pluto_in_the_sixth_house__冥王星过_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class PlutoInTheSixthHouse冥王星过(SemanticEntry):
    """
    **Source Text** (Lines 18916-18947):
> Be very careful of health—likely to overstrain physically and...
    """
    
    original_text: str = """**Source Text** (Lines 18916-18947):
> Be very careful of health—likely to overstrain physically and pay inadequate attention to body's needs. Physical condition you haven't attended to may reach critical point. At most severe: complete physical breakdown—but only if completely ignore health needs. Can also indicate complete physical regeneration—adopt careful regimen to rebuild body. Good time for yoga or physical-spiritual body culture. Examine diet and how body reacts. Be careful of fad diets assuming everyone's needs identical or based solely on religious principles. Poor diet can lead to breakdown. Sixth also concerns work. Great changes in work—possibly complete change of job or career. May be difficult period of tension—Pluto creates tension with people in job, particularly bosses. May be compelled to look elsewhere. May change jobs frequently as you cast about for proper situation—may take years. May get into Plutonian work: tearing down to build anew, regenerative therapies, secret or subversive elements, secret projects.

**English Paraphrase**: Be careful of health—overstrain possible. Neglected conditions may reach crisis. Can indicate regeneration—yoga, diet examination good. Work may change completely—tension with bosses. May change jobs frequently seeking right fit. May work in Plutonian fields.

**Complete Chinese Interpretation**: 小心健康——可能过度劳累。被忽视的状况可能达到危机。可以表示重生——瑜伽、饮食检查好。工作可能完全改变——与老板的紧张。可能频繁换工作寻找合适的。可能在冥王星领域工作。

**Narrative Snippets**:
- `[ns_pit_pl006]` `[trigger: pluto_transit_house_6]` `[factor_trigger: astro_transit_pluto AND astro_house_6]` `[role: 主干]` Health attention critical. Work transforms—tension with authority. May find Plutonian work. → PIT Ch13 Pluto-6H"""
    normalized_text_zh: str = """"""
    subject: str = "Pluto in the Sixth House (冥王星过境第六宫)"
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
        l1_anchor="pit_v1.0.0_pluto_in_the_sixth_house__冥王星过_001_L1",
    )
    version: str = "1.0.0"
