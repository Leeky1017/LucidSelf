"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.147432
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
    semantic_id="ca_v1.0.0_lost_object_questions___findin_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class LostObjectQuestionsFindin(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------|------------|---------------|
| 2nd house | Domus II | Movable possessions | Primary lost object house |
| Elemental direction | Fire/Earth/Air/Water | Sign element indicates place type | Location method |
| Angular position | In 1st/4th/7th/10th | Object's location relative to querent | Recovery likelihood |

**Source Text** (Synthesized from Lilly Book II):
> For lost goods, examine the Lord of the 2nd house (moveable possessions). If the Lord of the 2nd be in an angle, especially the 1st or 10th, the thing is in the house. If in the 4th, it is hidden or underground. If in the 7th, another person has it. The sign shows direction and nature of place.

**English Paraphrase (Primary Language)**:

**Lost object questions** use the 2nd house (movables) or relevant house for the object type:

| House | Object Type |
|-------|-------------|
| 2nd | Personal possessions, money |
| 4th | Real estate, things in home |
| 5th | Recreational items, children's things |
| 6th | Tools, work items, small animals |

**Location indicators**:

| L2 Position | Location |
|-------------|----------|
| In 1st house | Near querent, in their space |
| In 4th house | Hidden, underground, at home |
| In 7th house | With another person |
| In 10th house | At workplace, public place |

**Sign element** indicates nature of place:
- Fire = near heat, fireplaces, kitchens
- Earth = ground level, gardens, storage
- Air = upper rooms, shelves, high places
- Water = near water, bathrooms, damp areas

**Complete Chinese Interpretation (Secondary Language)**:

**失物问题**使用第2宫（动产）或与物品类型相关的宫位：

| 宫位 | 物品类型 |
|------|----------|
| 第2宫 | 个人财物、金钱 |
| 第4宫 | 不动产、家中物品 |
| 第5宫 | 娱乐物品、孩子的东西 |
| 第6宫 | 工具、工作物品、小动物 |

**位置指示**：

| L2 位置 | 地点 |
|---------|------|
| 在第1宫 | 靠近问卜者，在其空间 |
| 在第4宫 | 隐藏、地下、在家 |
| 在第7宫 | 在他人处 |
| 在第10宫 | 在工作场所、公共场所 |

**星座元素**指示地点性质：
- 火 = 靠近热源、壁炉、厨房
- 土 = 地面层、花园、储藏室
- 风 = 上层房间、架子、高处
- 水 = 靠近水、浴室、潮湿区域

**Core Points**:
- 2nd house lord position shows location.
- Angular = findable; cadent = difficult to find.
- Sign element indicates place nature.
- Moon separating from L2 = object moved recently.

#### Narrative Snippets

- `[ns_lilly_030]` `[trigger: horary_lost_object]` `[factor_trigger: horary_2nd_house]` `[role: 主干]` For lost goods, examine the Lord of the 2nd house. If L2 be in an angle, the thing is in the house. If in the 4th, hidden or underground. If in the 7th, another person has it. → Christian Astrology Lost Objects
- `[ns_lilly_031]` `[trigger: lost_location]` `[factor_trigger: L2_position AND angular]` `[role: 主干依赖]` Angular position = findable; cadent position = difficult to find. The sign element indicates the nature of the place (fire = near heat, water = damp areas). → Christian Astrology Lost Objects
- `[ns_lilly_032]` `[trigger: object_moved]` `[factor_trigger: moon_separating_L2]` `[role: 总结]` Moon separating from L2 indicates the object has been moved recently from its original location. → Christian Astrology Lost Objects

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Lost object horary is one of the most practical applications, with high verifiability. Lilly's elemental-directional system (Fire=East, Earth=South, etc.) derives from Ptolemy. The house-position technique for locating items is Arabic in origin (via Sahl). Modern practitioners often add asteroid positions for specificity.
- **中文**: 失物占星是最实用的应用之一，可验证性高。Lilly的元素-方向系统（火=东、土=南等）源自托勒密。通过宫位定位物品的技术源自阿拉伯（通过Sahl）。现代实践者常添加小行星位置以提高精确度。"""
    normalized_text_zh: str = """"""
    subject: str = "Lost Object Questions – Finding Things"
    factor_refs: list = ['house_2_movables', 'angular_position', 'cadent_position', 'elemental_direction', 'place_nature']
    
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
        l1_anchor="ca_v1.0.0_lost_object_questions___findin_001_L1",
    )
    version: str = "1.0.0"
