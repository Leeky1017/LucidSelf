"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.206762
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
    semantic_id="pit_v1.0.0_uranus_in_the_seventh_house__天_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class UranusInTheSeventhHouse天(SemanticEntry):
    """
    **Source Text** (Lines 14629-14663):
> Extremely difficult if in close relationship not working well...
    """
    
    original_text: str = """**Source Text** (Lines 14629-14663):
> Extremely difficult if in close relationship not working well. Can go along with unsatisfactory relationship for years, but when Uranus comes, tensions become intolerable. Often coincides with marital breakup or end of shaky partnership. Reasonably secure partnership will weather the storm. Even in best relationship, time to make needed changes. May see new relationship as escape from routine—wild, improbable, unstable love affair. Seventh also house of open enemies—conflicts more frequent. May become involved in disruptive legal encounters. Energy experienced through intimate encounters. If relationships disrupted against your will, you're sending unconscious signals. If you see what changes need to be made, won't suffer especially. New experience gives greater mastery. If resist change and view as threat, increase violence of Uranian energies. Relationships trying to teach you something—let them.

**English Paraphrase**: Difficult for unsatisfactory relationships. May coincide with breakup. Secure partnerships weather it. May seek new relationship as escape. Conflicts more frequent. Legal issues possible. See what changes needed—resistance increases violence of energy. Let relationships teach you.

**Complete Chinese Interpretation**: 对不满意的关系困难。可能与分手同时发生。稳固的伙伴关系能度过。可能寻求新关系作为逃避。冲突更频繁。可能有法律问题。看看需要什么改变——抵抗会增加能量的暴力。让关系教导你。

**Narrative Snippets**:
- `[ns_pit_ur007]` `[trigger: uranus_transit_house_7]` `[factor_trigger: astro_transit_uranus AND astro_house_7]` `[role: 主干]` Difficult for unsatisfactory relationships. May break up. Resistance increases violence. Let relationships teach. → PIT Ch11 Uranus-7H"""
    normalized_text_zh: str = """"""
    subject: str = "Uranus in the Seventh House (天王星过境第七宫)"
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
        l1_anchor="pit_v1.0.0_uranus_in_the_seventh_house__天_001_L1",
    )
    version: str = "1.0.0"
