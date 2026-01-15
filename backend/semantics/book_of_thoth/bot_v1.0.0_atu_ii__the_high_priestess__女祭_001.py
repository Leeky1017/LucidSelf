"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.044562
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
    semantic_id="bot_v1.0.0_atu_ii__the_high_priestess__女祭_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class AtuIiTheHighPriestess女祭(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Gimel (ג) | Hebrew letter "Camel" | Crossing the Abyss |
| Veil of Light | Luminous concealment | Truth hidden in brilliance |
| Eternal Virgin | Isis/Artemis form | Pure spiritual receptivity |
| Moon | Reflective planet | Intuition, subconscious |

**Source Text**:
> "This card is referred to the letter Gimel, which means a Camel... The card represents the most spiritual form of Isis the Eternal Virgin; the Artemis of the Greeks. She is clothed only in the luminous veil of light... She is the truth behind the veil of light. She is the soul of light... The High Priestess is the first card which connects the Supernal Triad with the Hexad; and her path... makes a direct connection between the Father in his highest aspect, and the Son in his most perfect manifestation." (Book of Thoth, The High Priestess)

**Qabalistic Correspondences**:
- **Hebrew Letter**: Gimel (ג, value 3) - "Camel"
- **Path**: Connects Kether (Crown) to Tiphareth (Beauty) - The 13th Path
- **Planet**: Moon ☽
- **Element**: Water (emotional/subconscious realm)

**English Paraphrase**:
The High Priestess is the archetype of **Pure Intuition** and **Spiritual Mystery**, representing the Eternal Virgin—Isis or Artemis in her most exalted form. Unlike the fertile Empress, the Priestess embodies the **Moon's** cold, reflective, virginal power that connects the highest divinity (Kether) directly to the human heart-center (Tiphareth). She is clothed in the "Veil of Light" which both conceals and reveals the Spirit; this luminous veil is the illusion of form that prevents direct apprehension of the absolute. The **Camel** (Gimel) symbolizes a vehicle for crossing the spiritual desert or Abyss—capable of carrying the soul through barren wasteland without external sustenance. She is entirely self-sufficient, representing the independence of the inner spiritual life. At the base of the card, nascent forms (crystals, seeds) symbolize the beginnings of manifestation emerging from pure potential.

**完整中文诠释**:
女祭司（The High Priestess）是**纯粹直觉**与**灵性奥秘**的原型，代表着永恒童贞女（Eternal Virgin）——伊西斯（Isis）或阿尔忒弥斯（Artemis）最崇高的形态。与多产的皇后不同，女祭司体现了**月亮**那冷峻、反射性、童贞的力量，她将最高神性（Kether，至高王冠）直接连接到人类的心灵中心（Tiphareth，美之所在）。她披着"光之面纱"（Veil of Light），这面纱既隐藏又揭示着灵性（Spirit）；这道光辉的面纱是形式的幻象，阻止了对绝对真理的直接领悟。**骆驼**（Gimel）象征着穿越灵性沙漠或深渊的载具——能够在不依赖外部支持的情况下，载着灵魂穿越贫瘠荒野。她完全自给自足，代表着内在灵性生活的独立性。在卡牌底部，新生的形态（晶体、种子）象征着从纯粹潜能中涌现的显化之始。

**Core Points**:
- **Intuitive Bridge**: The direct link between Divine Source (Kether) and Human Soul (Tiphareth)
- **Veiled Mystery**: Truth hidden behind dazzling brilliance of light/form
- **Receptive Power**: The power of silence, waiting, and inner reflection
- **Virgin Potential**: Self-sufficient spiritual purity requiring no external fertilization

**Detailed Explanation**:
The High Priestess sits between the pillars of manifestation, holding the scroll of hidden wisdom (Tora). Her bow is both weapon (Artemis the Huntress) and musical instrument (harmony through vibration). The Veil of Light is paradoxical—light usually reveals, but here it conceals the Spirit behind its blinding brilliance. The Path of Gimel crosses the Abyss, making her the Guardian of the Threshold to the Supernal realms. She represents the subconscious mind receiving impressions from the divine (descending) and aspirations from the human (ascending).

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: The Priestess represents Isis/Artemis in virginal form, distinct from the Empress's fertility. Gimel (Camel) symbolizes the soul's vehicle across the spiritual Abyss. The Veil of Light paradoxically conceals by its brilliance. Harris depicts nascent forms (crystals, seeds) emerging from potential.
- **中文**: 女祭司代表伊西斯/阿尔忒弥斯的童贞形态，与皇后的生育力不同。Gimel（骆驼）象征灵魂跨越灵性深渊的载具。光之面纱矛盾地通过其耀眼光芒而隐藏。Harris描绘了从潜能中涌现的新生形态（晶体、种子）。

**Narrative Snippets**:
- `[ns_thoth_035]` `[trigger: priestess_veil_light]` `[factor_trigger: tarot_priestess AND tarot_veil]` `[role: 主干]` The Priestess is clothed in the Veil of Light—a luminous veil that paradoxically hides Spirit behind its very brilliance. → English Paraphrase
- `[ns_thoth_036]` `[trigger: gimel_camel_abyss]` `[factor_trigger: tarot_gimel AND tarot_abyss]` `[role: 主干依赖]` Gimel, the Camel, symbolizes the soul's vehicle across the spiritual Abyss—able to cross barren desert without external support. → English Paraphrase
- `[ns_thoth_037]` `[trigger: priestess_intuitive_bridge]` `[factor_trigger: tarot_priestess AND tarot_intuition]` `[role: 主干依赖]` The High Priestess forms a direct bridge from Kether to Tiphareth—pure intuition linking highest divinity with the human heart. → English Paraphrase
- `[ns_thoth_038]` `[trigger: eternal_virgin]` `[factor_trigger: tarot_virgin AND tarot_isis]` `[role: 总结]` As Eternal Virgin (Isis/Artemis), she embodies self-sufficient spiritual purity, distinct from the Empress's fertile motherhood. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "ATU II: The High Priestess (女祭司)"
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
        l1_anchor="bot_v1.0.0_atu_ii__the_high_priestess__女祭_001_L1",
    )
    version: str = "1.0.0"
