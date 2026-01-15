"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.994803
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
    semantic_id="pt_v1.0.0_chapter_2__cups__water_element_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class Chapter2CupsWaterElement(SemanticEntry):
    """
    **Source Framework**:

Cups represent the **Water element** - emotion, intuition, love, imagination,...
    """
    
    original_text: str = """**Source Framework**:

Cups represent the **Water element** - emotion, intuition, love, imagination, and the receptive principle. Where Wands are about **what we do**, Cups are about **what we are** at the deepest level.

**Core Water Symbolism**:
- **Formlessness**: Adapts to container, flows around obstacles
- **Depth**: Surface may be calm while depths remain mysterious
- **Receptivity**: Opens to receive rather than pushing forward
- **Connection**: All rivers flow to same ocean (unity of being)
- **Nurturing**: Softens and enables growth (seed needs water)

**Cups as Life Domain**:
- **Emotions**: Full spectrum from joy to grief
- **Relationships**: Love, friendship, family bonds
- **Imagination**: Dreams, visions, creative inspiration
- **Intuition**: Inner knowing beyond rational thought
- **Spirituality**: Direct experience of unity with life

**Fire vs Water Dynamic**:
- **Wands (Fire)**: Doing, action, ego, separation, optimism
- **Cups (Water)**: Being, feeling, soul, connection, depth
- **Complementary**: Life needs both sun and rain
- **Danger**: Fire evaporates water, flood drowns fire
- **Integration**: Hermaphrodite symbol, six-pointed star (fire ▲ + water ▽)

**Shadow Side of Cups**:
- Overwhelming emotion, loss of boundaries
- Illusion, fantasy disconnected from reality
- Passivity becoming stagnation
- Drowning in feeling, inability to act

**完整中文诠释**:
**圣杯**代表**水元素**——情感、直觉、爱、想象力、接纳原则。权杖关乎**我们所做**（action），圣杯关乎**我们在最深层次所是**（being）。**水之核心象征**：**无形**（适应容器，流过障碍）；**深度**（表面可能平静而深处保持神秘）；**接纳**（打开接收而非向前推进）；**连接**（所有河流汇入同一海洋=存在的统一）；**滋养**（软化并使成长可能，种子需要水）。**圣杯生活领域**：**情感**（从喜悦到悲伤的完整光谱），**关系**（爱情、友谊、家庭纽带），**想象力**（梦境、愿景、创意灵感），**直觉**（超越理性思考的内在知晓），**灵性**（与生命统一的直接经验）。**火vs水动态**：**权杖（火）**=做、行动、自我、分离、乐观；**圣杯（水）**=是、感受、灵魂、连接、深度；**互补**（生活需要阳光也需要雨水）；**危险**（火蒸发水，洪水淹没火）；**整合**（雌雄同体符号，六角星=火▲+水▽）。**阴影面**：情感淹没、边界丧失，幻觉、脱离现实的幻想，被动变成停滞，溺于感受、无法行动。**Rider-Waite创新**：如权杖，圣杯牌展示**情感生活的场景**而非抽象图案，使心理解读成为可能。

**Rider-Waite Innovation**: Like Wands, Cups cards show **scenes of emotional life** rather than abstract patterns, making psychological interpretation possible.

**Narrative Snippets**:
- `[ns_78deg_209]` `[trigger: cups_water_element]` `[factor_trigger: suit_cups AND element_water]` `[role: 主干]` Cups represent the Water element—emotion, intuition, love, imagination, the receptive principle; where Wands are what we do, Cups are what we are at the deepest level. → Source Framework
- `[ns_78deg_210]` `[trigger: water_formlessness]` `[factor_trigger: element_water AND quality_formless]` `[role: 主干依赖]` Water's formlessness—adapts to container, flows around obstacles; depth where surface may be calm while depths remain mysterious. → Core Water Symbolism
- `[ns_78deg_211]` `[trigger: cups_connection]` `[factor_trigger: suit_cups AND state_connection]` `[role: 条件分支]` All rivers flow into same ocean—the unity of existence; water connects what fire separates; relationship, empathy, shared feeling. → Core Water Symbolism
- `[ns_78deg_212]` `[trigger: fire_water_dynamic]` `[factor_trigger: element_fire AND element_water]` `[role: 条件分支]` Fire evaporates water, flood drowns fire—complementary dangers; yet life needs both sun and rain; integration through the six-pointed star. → Fire vs Water Dynamic
- `[ns_78deg_213]` `[trigger: cups_shadow]` `[factor_trigger: suit_cups AND shadow_aspect]` `[role: 例外处理]` Shadow side: overwhelming emotion, loss of boundaries; illusion disconnected from reality; passivity becoming stagnation; drowning in feeling. → Shadow Side
- `[ns_78deg_214]` `[trigger: cups_life_domain]` `[factor_trigger: suit_cups AND domain_emotion]` `[role: 总结]` Cups govern emotions (joy to sorrow), relationships (love, friendship, family), imagination (dreams, visions), intuition (inner knowing), and spiritual unity. → Cups Life Domains"""
    normalized_text_zh: str = """"""
    subject: str = "Chapter 2: Cups (Water Element) - Introduction"
    factor_refs: list = ['force', 'existing', 'bond', 'existing', 'faculty', 'existing', 'capacity', 'existing', 'state', 'existing', 'shadow', 'existing']
    
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
        book_id="pollack_tarot",
        chapter="",
        l1_anchor="pt_v1.0.0_chapter_2__cups__water_element_001_L1",
    )
    version: str = "1.0.0"
