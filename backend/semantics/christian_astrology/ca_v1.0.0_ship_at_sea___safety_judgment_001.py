"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.147486
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
    semantic_id="ca_v1.0.0_ship_at_sea___safety_judgment_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class ShipAtSeaSafetyJudgment(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------|------------|---------------|
| 1st House (Ship) | Ship itself | The vessel and its condition | Ship's safety |
| Moon | Universal co-sig | Movement and change | Journey progress |
| 9th House | Long voyage | Sea travel house | Voyage conditions |
| Malefics | Saturn/Mars | Dangerous planets | Threats at sea |

**Source Text** (Synthesized from Lilly Book II, pp. 157-165):
> Of a Ship at Sea, her safety or destruction: The Ascendant and the Moon are Significators of the Ship and her Lading. The Lord of the Ascendant signifies the Mariners; if he be an Infortune, the Mariners are knaves. If the Lord of the Ascendant or Moon be joined to an Infortune in angles, the Ship shall be in great danger. If the Lord of the Ascendant or Moon be joined to fortunate Planets, and these in good houses, the Ship shall come safe.

**English Paraphrase (Primary Language)**:

**Ship Safety Questions** use specific house assignments:

| Element | Significator |
|---------|--------------|
| Ship itself | Ascendant + Moon |
| Cargo/lading | Moon |
| Mariners/crew | Lord of 1st |
| Voyage conditions | 9th house |
| Danger | Malefics in angles |

**Judgment Criteria**:
- L1/Moon joined to benefics in good houses = safe voyage
- L1/Moon joined to malefics in angles = great danger
- L1 afflicted by Saturn/Mars = ship endangered
- Moon void = journey cancelled or inconclusive

**完整中文诠释**：船只安全问题使用特定宫位分配。船本身=上升+月亮；货物=月亮；船员=L1；航程条件=第9宫；危险=凶星在角宫。判断标准：L1/月亮与吉星在好宫位=安全航行；L1/月亮与凶星在角宫=极大危险；L1被土星/火星克=船有危险；月亮空亡=航程取消或无结论。

#### Core Points

- **Ship = ASC + Moon**: Dual significator for vessel
- **Crew = L1**: Ruler shows mariners' condition
- **Benefic connection = safety**: Jupiter/Venus aspects protect
- **Malefic in angles = danger**: Saturn/Mars threaten voyage

**Narrative Snippets**:
- `[ns_lilly_ship_001]` `[trigger: ship_safety]` `[factor_trigger: L1_Moon_benefic AND astro_ship_safety]` `[role: 主干]` L1 or Moon joined to fortunate planets in good houses = ship comes safe. → Christian Astrology Ship
- `[ns_lilly_ship_002]` `[trigger: ship_danger]` `[factor_trigger: L1_Moon_malefic_angular AND astro_ship_danger]` `[role: 主干依赖]` L1 or Moon joined to infortune in angles = ship in great danger. → Christian Astrology Ship
- `[ns_lilly_ship_003]` `[trigger: crew_quality]` `[factor_trigger: L1_nature AND astro_crew_quality]` `[role: 条件分支]` If L1 be an infortune, the mariners are knaves (unreliable). → Christian Astrology Ship

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Ship horary was critically important in 17th-century maritime England. Lilly includes multiple actual ship cases with outcomes recorded. The method treats the ship as a "living entity" with ASC representing its body. Modern practitioners adapt for air travel.
- **中文**: 船只卜卦在17世纪海事英国极为重要。Lilly包含多个实际船只案例并记录结果。该方法将船视为"活实体"，上升代表其身体。现代实践者将此法改编用于航空旅行。"""
    normalized_text_zh: str = """"""
    subject: str = "Ship at Sea – Safety Judgment"
    factor_refs: list = ['ship_significator', 'maritime_safety', 'angular_malefic']
    
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
        book_id="christian_astrology",
        chapter="",
        l1_anchor="ca_v1.0.0_ship_at_sea___safety_judgment_001_L1",
    )
    version: str = "1.0.0"
