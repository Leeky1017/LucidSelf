"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.238095
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
    semantic_id="pit_v1.0.0_pluto_in_the_twelfth_house__冥王_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class PlutoInTheTwelfthHouse冥王(SemanticEntry):
    """
    **Source Text** (Lines 19107-19144):
> Many ramifications. Prepares for Pluto transiting 1H—clears a...
    """
    
    original_text: str = """**Source Text** (Lines 19107-19144):
> Many ramifications. Prepares for Pluto transiting 1H—clears away old and hidden psychic garbage prior to complete rebuilding of self. First and most importantly: psychological effects. Similar to Pluto's 4H transit—brings up deeply buried aspects and forces you to confront them. In our interaction with people we try to hide aspects we've been taught not to approve of—yet energies leak out in subversive ways, undercut conscious intentions, do ourselves in without understanding. Pluto activates these patterns to point they can't be ignored. Unconsciously motivated actions can become extremely troublesome. Although intend to act one way, suddenly find yourself acting quite differently. Extremely important to understand unconscious energies and be willing to confront "bad" aspects of yourself. Can't go through adulthood with clearly childish subconscious behavior patterns. May have to recall and relive childhood events affecting you now. Feel free to call in any therapist who seems able to reach inside. Transit activates hidden side of external life too—relationships that failed, actions and behavior you don't wish to discuss even with yourself. Consequences may come back to haunt you. Face them honestly—only then will they cease to run your life. May have alienated someone unconsciously who tries to work against you—"secret enemies," though usually not really unknown, just have to confront own guilt feelings. Bring feelings into open. Secret enemies can't work against you in open—if completely honest, they may change heart toward you. Whatever situation, necessary to confront all hidden and unpleasant aspects. By avoiding them you've created situation where they control you. Only by facing honestly without guilt can you clear them away.

**English Paraphrase**: Prepares for 1H—clears psychic garbage. Deep psychological work—confront hidden aspects. Unconsciously motivated actions troublesome. Understand "bad" parts of self. Confront childhood patterns. External hidden elements return—face honestly. "Secret enemies" lose power when brought to light. Clear away what controls you.

**Complete Chinese Interpretation**: 为第一宫做准备——清除心灵垃圾。深层心理工作——面对隐藏的方面。无意识驱动的行为令人烦恼。理解自我的"坏"部分。面对童年模式。外部隐藏元素回归——诚实面对。"秘密敌人"在被揭露时失去力量。清除控制你的东西。

**Narrative Snippets**:
- `[ns_pit_pl012]` `[trigger: pluto_transit_house_12]` `[factor_trigger: astro_transit_pluto AND astro_house_12]` `[role: 主干]` Clears psychic garbage. Confront hidden aspects. Face what controls you. Prepare for rebirth. → PIT Ch13 Pluto-12H"""
    normalized_text_zh: str = """"""
    subject: str = "Pluto in the Twelfth House (冥王星过境第十二宫)"
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
        l1_anchor="pit_v1.0.0_pluto_in_the_twelfth_house__冥王_001_L1",
    )
    version: str = "1.0.0"
