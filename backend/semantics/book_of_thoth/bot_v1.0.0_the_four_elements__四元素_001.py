"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.049523
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
    semantic_id="bot_v1.0.0_the_four_elements__四元素_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class TheFourElements四元素(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Fire (Shin ש) | Active energy | Will, spirit, Wands |
| Water (Mem מ) | Passive receptivity | Emotion, Cups |
| Air (Aleph א) | Mediation | Intellect, Swords |
| Earth (Tau ת) | Crystallization | Matter, Disks |
| Three Mother Letters | Shin, Mem, Aleph | Primary elements |

**Source Text**:
> "The Ancients conceived of Fire, Water and Air as pure elements. They were connected with the three qualities of Being, Knowledge and Bliss... The alchemists had three similar principles of energy, of which all existing phenomena are composed: Sulphur, Mercury and Salt. This Sulphur is Activity, Energy, Desire; Mercury is Fluidity, Intelligence, the power of Transmission; Salt is the vehicle of these two forms of energy. ... These elements are represented in the Hebrew alphabet by the letters Shin, Mem and Aleph. The Qabalists call them the Three Mother Letters. ... these three elements... can only manifest in sensible experience by impinging upon the senses, crystallising out in a fourth element which they call 'Earth', represented by the last letter of the alphabet, Tau."

**English Paraphrase**:

The **Four Elements** are not physical substances but **modes of energy**:

**Three Mother Letters (Primary Elements)**:
- **Fire (Shin ש)**: **Sulphur** in alchemy. Activity, energy, desire, will. The **active principle**. Corresponds to **Sat** (Being) in Vedanta, **Rajas** (Activity) in the Gunas.
- **Water (Mem מ)**: **Salt** in alchemy. Receptivity, emotion, the womb. The **passive principle**. Corresponds to **Tamas** (Darkness/Inertia) in the Gunas.
- **Air (Aleph א)**: **Mercury** in alchemy. Fluidity, intelligence, transmission, mediation. Corresponds to **Chit** (Thought) in Vedanta, **Sattvas** (Calm) in the Gunas.

**The Fourth Element**:
- **Earth (Tau ת)**: The **crystallization** of the other three. The three pure elements only become sensible (experienceable) when they "solidify" into Earth. Earth is the **Daughter** of the Tetragrammaton—the final manifestation.

**Tarot Application**:
- **Wands = Fire**: Will, spirit, creative energy
- **Cups = Water**: Emotions, relationships, the unconscious
- **Swords = Air**: Intellect, conflict, communication
- **Disks = Earth**: Matter, money, the physical world

**完整中文诠释**：

**四元素**不是物理物质，而是**能量模式**：

**三母字母（主要元素）**：
- **火（Shin ש）**：炼金术中的**硫磺**。活动、能量、欲望、意志。**主动原则**。对应吠檀多的**Sat**（存在）、三德的**Rajas**（活动）。
- **水（Mem מ）**：炼金术中的**盐**。接受性、情感、子宫。**被动原则**。对应三德的**Tamas**（黑暗/惰性）。
- **气（Aleph א）**：炼金术中的**水银**。流动性、智力、传输、中介。对应吠檀多的**Chit**（思想）、三德的**Sattvas**（平静）。

**第四元素**：
- **土（Tau ת）**：其他三者的**结晶**。三种纯元素只有在"固化"为土时才变得可感知（可体验）。土是四字神名的**女儿**——最终显化。

**塔罗应用**：
- **权杖 = 火**：意志、精神、创造能量
- **圣杯 = 水**：情感、关系、潜意识
- **宝剑 = 气**：智力、冲突、交流
- **钱币 = 土**：物质、金钱、物理世界

#### Core Points

- The **Four Elements** are modes of energy, not physical substances—"Water" means receptivity/emotion, not H₂O.
- **Three Mother Letters** (Shin/Mem/Aleph = Fire/Water/Air) are the primary spiritual elements; **Earth (Tau)** is their crystallization.
- Alchemical correspondence: Fire=Sulphur, Water=Salt, Air=Mercury.
- Vedantic correspondence: Fire=Sat (Being), Water=Tamas, Air=Chit (Thought); or Rajas/Tamas/Sattvas.
- The **four Tarot suits** embody these elements: Wands/Fire, Cups/Water, Swords/Air, Disks/Earth.

**Narrative Snippets**:
- `[ns_thoth_theory_007]` `[trigger: four_elements]` `[factor_trigger: tarot_element AND tarot_energy]` `[role: 主干]` The Four Elements are modes of energy: Fire (activity), Water (receptivity), Air (mediation), Earth (crystallization). → English Paraphrase
- `[ns_thoth_theory_008]` `[trigger: mother_letters]` `[factor_trigger: tarot_hebrew AND tarot_element]` `[role: 主干依赖]` The Three Mother Letters (Shin, Mem, Aleph) represent the primary spiritual elements that crystallize into Earth. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "The Four Elements (四元素)"
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
        book_id="book_of_thoth",
        chapter="",
        l1_anchor="bot_v1.0.0_the_four_elements__四元素_001_L1",
    )
    version: str = "1.0.0"
