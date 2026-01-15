"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.206864
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
    semantic_id="pit_v1.0.0_uranus_in_the_tenth_house__天王星_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class UranusInTheTenthHouse天王星(SemanticEntry):
    """
    **Source Text** (Lines 14737-14770):
> Radical change in professional life, change of profession, or...
    """
    
    original_text: str = """**Source Text** (Lines 14737-14770):
> Radical change in professional life, change of profession, or conflict with authority figures possible. Way you express identity in world, status, reputation, profession will be challenged. If stale and no longer offers new experience, great changes. People over you—bosses, employers, parents, government—seem particularly repressive. Strong desire to break free. If held down unreasonably, make changes. But caution—too hasty, encounter very repressive forces. Often operates benevolently—sudden new opportunities in work, new techniques, revolutionary new enterprise, unbeaten paths. May change field altogether. Work must provide stimulation or becomes oppressive. If in responsible position, hard to discharge responsibility. May be tempted to quit and start new direction. May be best response though not safest. Dangerous to repress Uranian energies. Can signify drastic fall from power—reflection of unexpressed reluctance to have it. May affect social status. Examine who you are and make necessary changes. Don't wait for lightning to strike.

**English Paraphrase**: Radical professional change. Identity, status, reputation challenged. Conflict with authority possible. Often provides sudden new opportunities. Work must provide stimulation. May be tempted to quit. Can signify fall from power. Examine yourself and make changes—don't wait.

**Complete Chinese Interpretation**: 彻底的职业变化。身份、地位、声誉受挑战。可能与权威冲突。通常提供突然的新机会。工作必须提供刺激。可能想辞职。可能预示权力的陨落。审视自己并做出改变——不要等待。

**Narrative Snippets**:
- `[ns_pit_ur010]` `[trigger: uranus_transit_house_10]` `[factor_trigger: astro_transit_uranus AND astro_house_10]` `[role: 主干]` Radical professional change. Authority conflicts. Sudden new opportunities. Don't wait—make changes. → PIT Ch11 Uranus-10H"""
    normalized_text_zh: str = """"""
    subject: str = "Uranus in the Tenth House (天王星过境第十宫)"
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
        l1_anchor="pit_v1.0.0_uranus_in_the_tenth_house__天王星_001_L1",
    )
    version: str = "1.0.0"
