"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.995080
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
    semantic_id="pt_v1.0.0_chapter_4__pentacles__earth_el_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class Chapter4PentaclesEarthEl(SemanticEntry):
    """
    **Source Framework**:

Pentacles represent the **Earth element** - the physical world, body, work, n...
    """
    
    original_text: str = """**Source Framework**:

Pentacles represent the **Earth element** - the physical world, body, work, nature, and **material manifestation**. Where Wands=action, Cups=feeling, Swords=thought, Pentacles are **being grounded in physical reality**.

**Core Earth Symbolism**:
- **Grounding**: Necessary foundation for spiritual experience
- **Creation manifest**: Physical world as product of divine force
- **Mundane magic**: Ordinary life possesses greater magic than other elements
- **Balance**: Rabbi Akiba entered Paradise safely by balancing elements in Earth
- **Firmness**: Carries firmer reality, less prone to confusion than other elements

**Pentacles as Life Domain**:
- **Material world**: Money, work, practical matters
- **Nature**: Love for physical world, beauty of creation
- **Body**: Health, physicality, sensory experience
- **Manifestation**: Making ideas real in tangible form
- **Security**: Stability, resources, comfort

**Cultural Paradox**:
- **Western culture despises physical**: "Ashes to ashes, dust to dust" - clay as humiliation
- **Tarot perspective**: Physical world is **end result of creative force**, like painting from conception
- **Spiritual grounding**: Must begin and return to physical - **or lose ourselves** in purely spiritual realms

**The Four Rabbis Tale** (Qabalistic):
- **Ben Azai**: Too much Fire → burned out (ecstasy killed him)
- **Ben Zoma**: Too much Water → went mad (overwhelmed by emotion)
- **Ben Abuysh**: Too much Air → became apostate (took everything too literally)
- **Akiba**: Balanced in Earth → entered and left Paradise in peace
- **Lesson**: Earth element **balances and grounds** other elements

**Pentacles Dual Nature**:
- **Positive**: Beauty of nature, joy of satisfying work, grounding for mysticism, creative discipline
- **Negative**: Materialism, forgetting anything else exists, miserliness, stagnation

**Magic of the Mundane**:
- **Paradox**: Day-to-day life's very mundaneness ensures it possesses **greater 'magic'** than other elements
- **Gate cards**: Pentacles contains more Gates than any suit - physical opens doors to spiritual
- **Religious leaders**: Earth signs predominate in charts (Ronnie Dreyer study)

**完整中文诠释**:
**星币**代表**土元素**——物质世界、身体、工作、自然、**物质显化**。权杖=行动，圣杯=感受，宝剑=思想，星币=**扎根于物质现实的存在**。**土之核心象征**：**接地**（灵性经验的必要基础）；**创造显化**（物质世界作为神圣力量的产物）；**平凡魔法**（日常生活拥有比其他元素更大魔法）；**平衡**（Rabbi Akiba通过土平衡元素安全进入天堂）；**坚固**（承载更坚固现实，不易混淆）。**星币生活领域**：**物质世界**（金钱、工作、实际事务），**自然**（对物质世界的爱，创造之美），**身体**（健康、肉体性、感官经验），**显化**（使想法在有形形式中真实），**安全**（稳定、资源、舒适）。**文化悖论**：**西方文化轻视物质**（"灰归灰土归土"——黏土作为羞辱）；**塔罗视角**：物质世界是**创造力的最终结果**，如画作来自构思；**灵性接地**：必须始于并回归于物质——**否则在纯灵性领域迷失**。**四拉比故事**（卡巴拉）：**Ben Azai**（太多火→燃尽，狂喜杀死他），**Ben Zoma**（太多水→发疯，被情感淹没），**Ben Abuysh**（太多风→成叛教者，过于字面理解），**Akiba**（平衡于土→平安进出天堂）。**教训**：土元素**平衡并接地**其他元素。**平凡之魔法**：**悖论**：日常生活的平凡性本身确保它拥有**比其他元素更大"魔法"**。**门户牌**：星币包含比任何花色更多门户——物质开启通向灵性的门。**宗教领袖**：土相在命盘中占主导（Ronnie Dreyer研究）。**Rider-Waite创新**：增加**自然维度**到传统钱币（金钱/工作焦点），扎根于对物质世界的爱，而非仅劳动。

**Rider-Waite Innovation**: Added **nature dimension** to traditional Coins (money/work focus), grounding in love for physical world, not just labor.

**Narrative Snippets**:
- `[ns_78deg_284]` `[trigger: pentacles_intro]` `[factor_trigger: tarot_pentacles AND element_earth]` `[role: 主干]` Pentacles represent Earth element—material world, body, work, nature, physical manifestation; Wands=action, Cups=feeling, Swords=thinking, Pentacles=grounded existence. → Overview
- `[ns_78deg_285]` `[trigger: earth_grounding]` `[factor_trigger: tarot_pentacles AND principle_grounding]` `[role: 主干依赖]` Core Earth symbolism: necessary foundation for spiritual experience; mundane magic—ordinary life possesses greater 'magic' than other elements; firmness carries reality. → Core Earth Symbolism
- `[ns_78deg_286]` `[trigger: four_rabbis]` `[factor_trigger: tarot_pentacles AND narrative_rabbis]` `[role: 条件分支]` Four Rabbis tale: Ben Azai (too much Fire) burned out, Ben Zoma (Water) went mad, Ben Abuysh (Air) apostatized; only Akiba balanced in Earth entered Paradise safely. → The Four Rabbis Tale
- `[ns_78deg_287]` `[trigger: pentacles_dual]` `[factor_trigger: tarot_pentacles AND polarity_dual]` `[role: 条件分支]` Pentacles dual nature: positive (nature beauty, satisfying work, grounding mysticism) vs negative (materialism, forgetting spirit, miserliness, stagnation). → Pentacles Dual Nature
- `[ns_78deg_288]` `[trigger: mundane_magic]` `[factor_trigger: tarot_pentacles AND principle_mundane_magic]` `[role: 条件分支]` Paradox: day-to-day life's mundaneness ensures it possesses greater 'magic' than other elements; Pentacles contains more Gate cards—physical opens doors to spiritual. → Magic of the Mundane
- `[ns_78deg_289]` `[trigger: physical_creative_force]` `[factor_trigger: tarot_pentacles AND principle_manifestation]` `[role: 总结]` Physical world is end result of creative force, like painting from conception; must begin and return to physical—or lose ourselves in purely spiritual realms. → Cultural Paradox"""
    normalized_text_zh: str = """"""
    subject: str = "Chapter 4: Pentacles (Earth Element) - Introduction"
    factor_refs: list = ['process', 'existing', 'principle', 'existing', 'domain', 'existing', 'domain', 'existing', 'paradox', 'existing', 'shadow', 'existing']
    
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
        l1_anchor="pt_v1.0.0_chapter_4__pentacles__earth_el_001_L1",
    )
    version: str = "1.0.0"
