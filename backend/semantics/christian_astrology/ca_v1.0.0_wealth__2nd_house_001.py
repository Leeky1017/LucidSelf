"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.152291
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
    semantic_id="ca_v1.0.0_wealth__2nd_house_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class Wealth2ndHouse(SemanticEntry):
    """
    #### Source Text
(Lilly Book III, pp. 553-562): "Whether the Native shall be rich. Consider the Lord...
    """
    
    original_text: str = """#### Source Text
(Lilly Book III, pp. 553-562): "Whether the Native shall be rich. Consider the Lord of the 2nd, its dignity, aspects, and the Part of Fortune. Jupiter or Venus in 2nd = wealth; Saturn or Mars afflicting = poverty or loss."

#### English Paraphrase (Primary Language)

**Wealth indicators**:
- **Lord of 2nd house**: Dignified = wealth; debilitated = poverty
- **Planets in 2nd**: Jupiter/Venus = gain; Saturn/Mars = loss
- **Part of Fortune**: Well-placed = fortunate; afflicted = struggles
- **Aspects to 2nd Lord**: Benefic aspects = increase; malefic = decrease

**Means of acquiring wealth** shown by planet ruling or occupying 2nd:
- Sun = authority, government
- Moon = public, women, travel
- Mercury = trade, writing, skill
- Venus = pleasure, arts, women
- Mars = military, surgery, conflict
- Jupiter = religion, law, foreign trade
- Saturn = agriculture, mining, inheritance

#### Complete Chinese Interpretation (Secondary Language)

**财富指标**：第2宫主星尊贵=富裕，失势=贫困；第2宫内行星：木星/金星=获得，土星/火星=损失；福点良好=幸运，受克=困难；第2宫主相位：吉星相位=增加，凶星=减少。**获取财富的方式**由守护或占据第2宫的行星显示：太阳=权威/政府；月亮=公众/女性/旅行；水星=贸易/写作/技能；金星=娱乐/艺术/女性；火星=军事/外科/冲突；木星=宗教/法律/外贸；土星=农业/采矿/遗产。

**Narrative Snippets**:
- `[ns_lilly_wealth_001]` `[trigger: wealth]` `[factor_trigger: astro_wealth_level]` `[role: 主干]` Lord of 2nd dignified = wealth; debilitated = poverty or difficulty acquiring money. → CA III #Wealth
- `[ns_lilly_wealth_002]` `[trigger: wealth_means]` `[factor_trigger: astro_wealth_means]` `[role: 条件分支]` Planet ruling or in 2nd shows means: Jupiter = religion/law; Mercury = trade/writing. → CA III #Wealth
- `[ns_lilly_wealth_003]` `[trigger: lord_2nd]` `[factor_trigger: astro_lord_2nd_dignity]` `[role: 主干依赖]` Lord of 2nd house dignity determines wealth potential: dignified = rich, debilitated = poor. → English Paraphrase
- `[ns_lilly_wealth_004]` `[trigger: planet_2nd]` `[factor_trigger: astro_planet_in_2nd]` `[role: 条件分支]` Planets in 2nd house: Jupiter/Venus = gain; Saturn/Mars = loss or difficulty. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "Wealth (2nd House)"
    factor_refs: list = ['lord_2nd', 'part_of_fortune']
    
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
        l1_anchor="ca_v1.0.0_wealth__2nd_house_001_L1",
    )
    version: str = "1.0.0"
