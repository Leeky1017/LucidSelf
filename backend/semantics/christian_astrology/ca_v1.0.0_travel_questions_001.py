"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.147464
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
    semantic_id="ca_v1.0.0_travel_questions_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class TravelQuestions(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------|------------|---------------|
| 3rd house | Domus III | Short journeys, local travel | Nearby destinations |
| 9th house | Domus IX | Long journeys, foreign travel | Distant destinations |
| 7th house | Domus VII | Destination, "other place" | Where traveler goes |
| Void of course | Vacuus cursus | Moon making no aspects before sign change | Journey may not happen |

**English Paraphrase (Primary Language)**:

**Travel questions** (journeys, voyages):

| House | Meaning |
|-------|---------|
| 3rd | Short journeys (local travel) |
| 9th | Long journeys (foreign travel) |
| 1st | Traveler |
| 7th | Destination/place traveled to |

**Judgment patterns**:

| Configuration | Indication |
|--------------|------------|
| L9 well-dignified | Long journey favorable |
| L9 afflicted | Problems during journey |
| L1 applying to L9 with good aspect | Journey proceeds well |
| Malefics in 9th | Dangers on journey |
| L7 strong | Good conditions at destination |
| Moon void of course | Journey may not happen |

**Element of 9th house sign** indicates nature of journey:
- Fire = hot places, deserts
- Water = sea voyages, watery regions
- Air = high places, mountains
- Earth = fertile lands, valleys

**Complete Chinese Interpretation (Secondary Language)**:

**旅行问题**（旅程、航行）：

| 宫位 | 含义 |
|------|------|
| 第3宫 | 短途旅行（本地出行） |
| 第9宫 | 长途旅行（海外出行） |
| 第1宫 | 旅行者 |
| 第7宫 | 目的地/所去之处 |

**判断模式**：

| 配置 | 指示 |
|------|------|
| L9 有尊贵 | 长途旅行有利 |
| L9 受克 | 旅途中有问题 |
| L1 好相位趋近 L9 | 旅途顺利 |
| 凶星在第9宫 | 旅途有危险 |
| L7 强 | 目的地条件好 |
| 月亮空亡 | 旅行可能不会发生 |

**第9宫星座元素**指示旅途性质：
- 火 = 炎热地区、沙漠
- 水 = 海上航行、水域
- 风 = 高地、山区
- 土 = 肥沃土地、山谷

**Core Points**:
- 3rd = short trips, 9th = long journeys
- L9 condition shows journey quality
- 7th = destination conditions
- Sign element describes terrain

#### Narrative Snippets

- `[ns_lilly_039]` `[trigger: horary_travel]` `[factor_trigger: horary_9th_house AND astro_long_journey]` `[role: 主干]` For travel questions: 3rd house = short journeys; 9th house = long journeys. The 9th house lord's condition shows the quality of the voyage. → Christian Astrology Travel
- `[ns_lilly_040]` `[trigger: journey_quality]` `[factor_trigger: L9_condition AND astro_journey_favorability]` `[role: 主干依赖]` L9 dignified = favorable journey; L9 afflicted = problems en route. Malefics in 9th indicate dangers. 7th house shows destination conditions. → Christian Astrology Travel
- `[ns_lilly_041]` `[trigger: travel_terrain]` `[factor_trigger: sign_element_9th AND astro_terrain_type]` `[role: 总结]` Sign element on 9th cusp describes terrain: Fire = hot regions, Water = sea voyages, Air = highlands, Earth = fertile lands. → Christian Astrology Travel

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: The 3rd/9th house distinction for short/long journeys is classical (Ptolemy). In Lilly's era, "long journeys" often meant sea voyages—dangerous undertakings requiring careful horary judgment. The 7th house as destination derives from its "other place" symbolism. Modern practitioners adapt for air travel (9th house, Air element).
- **中文**: 第3宫/第9宫对应短途/长途的区分是古典的（托勒密）。在Lilly时代，"长途旅行"通常指海上航行——需要仔细占星判断的危险事业。第7宫作为目的地源于其"他处"象征。现代实践者为航空旅行调整（第9宫，风元素）。"""
    normalized_text_zh: str = """"""
    subject: str = "Travel Questions"
    factor_refs: list = ['house_3_short', 'house_9_long', 'house_7_destination', 'elemental_terrain', 'journey_quality']
    
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
        l1_anchor="ca_v1.0.0_travel_questions_001_L1",
    )
    version: str = "1.0.0"
