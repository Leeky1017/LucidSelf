"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.288023
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
    semantic_id="pit_v1.0.0_mars_in_the_seventh_house__火星过_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MarsInTheSeventhHouse火星过(SemanticEntry):
    """
    **Source Text** (Lines 8433-8461):
> Tension but can be used creatively. If unconscious, conflicts w...
    """
    
    original_text: str = """**Source Text** (Lines 8433-8461):
> Tension but can be used creatively. If unconscious, conflicts with spouse/partners/coworkers. Seventh house: intimate cooperation vs open enemies. Find it difficult to compromise. Positive: bring out repressed grievances, clearing of the air. If harmony exists, put great energy into working through partnership. Use energies most efficiently through partnership. Avoid unnecessary conflicts. Can signify legal conflicts—try to compromise.

**English Paraphrase**: Tension—creative or destructive. Conflicts with partners if unconscious. Difficult to compromise. Positive: air grievances, clear the air. Work through partnership. Avoid unnecessary conflicts. Possible legal issues.

**Complete Chinese Interpretation**: 紧张——创造性或破坏性。如果无意识则与伴侣冲突。难以妥协。积极：发泄不满，澄清。通过伙伴关系工作。避免不必要的冲突。可能的法律问题。

**Narrative Snippets**:
- `[ns_pit_ma007]` `[trigger: mars_transit_house_7]` `[factor_trigger: astro_transit_mars AND astro_house_7]` `[role: 主干]` Tension with partners—creative or destructive. Air grievances. Work through partnership. → PIT Ch8 Mars-7H"""
    normalized_text_zh: str = """"""
    subject: str = "Mars in the Seventh House (火星过境第七宫)"
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
        l1_anchor="pit_v1.0.0_mars_in_the_seventh_house__火星过_001_L1",
    )
    version: str = "1.0.0"
