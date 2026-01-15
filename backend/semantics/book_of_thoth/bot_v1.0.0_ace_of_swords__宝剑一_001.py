"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.076355
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
    semantic_id="bot_v1.0.0_ace_of_swords__宝剑一_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class AceOfSwords宝剑一(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Kether in Air | Crown in Air | Primordial intellect |
| Ruach | Integrating mind | Human consciousness |
| Vau | Third letter YHVH | Linking principle |
| Sword of Magus | Cutting blade | Discrimination |

**Title**: The Root of the Powers of Air (气之力量的根源)
**Qabalistic**: Kether in Air (气中之冠)
**Astrological**: Root of Air signs (Gemini, Libra, Aquarius)

**Source Text**:
> "The Ace of Swords is the primordial Energy of Air, the Essence of the Vau of Tetragrammaton, the integration of the Ruach. Air is the result of the conjunction of Fire and Water; thus it lacks the purity of its superiors in the male hierarchy, Fire, Sol and the Phallus. But for this same reason it is the first card directly to be apprehended by the normal consciousness of Mankind. ... In nature, the obvious symbol of Air is the Wind 'which bloweth whithersoever it listeth'."

**English Paraphrase**:
**Primordial Intellect** – This card embodies the pure, original **energy of Air**. It is the **Vau** of the Tetragrammaton, the integrating principle of **Ruach** (Mind). Air arises from the conjunction of Fire and Water, so it is less pure than either but more directly accessible to ordinary consciousness. It is the **Sword of the Magus**: the cutting power of discrimination, analysis, definition and naming. As Wind, it blows where it will, carrying thought, speech and ideas. In its highest form it is clear reason; in its degenerate form, it becomes sterile logic and mental cruelty.

**Core**: **Mental Clarity & Discrimination** – Idea, intellect, analysis, decision, the power to cut through confusion.

**Chinese Explanation**:
**宝剑一**代表空气元素的**原初能量**，是四大元素中最贴近人类日常意识的层面。它对应四字神名中的**Vau**，也就是**Ruach（心智/理性）**的整合之力。空气源自火与水的结合，因此不如火或水那样“纯粹”，却正因如此，更容易被普通意识直接体验。画面中的剑象征**魔术师之剑**——用来**分割、区分、命名与分析**的理性工具，像风一般随处吹拂，带来思想、语言与观念的流动。正向时，它代表清晰的判断力与洞察力；失衡时，则可能堕落为**过度理性、冷酷的逻辑、言语伤害**。

**In Readings**: New ideas, intellectual breakthroughs, decisions, truth, clarity, arguments, sharp words, the beginning of a mental cycle.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Ace of Swords is primordial Air energy, Vau of Tetragrammaton. Air arises from Fire-Water conjunction. Sword of Magus cuts and discriminates. Wind blows where it will.
- **中文**: Crowley的宝剑一是原初空气能量，四字神名的Vau。空气源于火-水结合。魔术师之剑切割和辨别。风随意吹拂。

**Narrative Snippets**:
- `[ns_thoth_swords_001]` `[trigger: ace_swords_thoth]` `[factor_trigger: thoth_swords_ace]` `[role: 主干]` Ace of Swords = primordial Air energy; Vau of Tetragrammaton; integration of Ruach (Mind). → Core
- `[ns_thoth_swords_002]` `[trigger: sword_magus]` `[factor_trigger: thoth_swords_ace AND symbol_sword]` `[role: 条件分支]` Sword of the Magus—cutting power of discrimination, analysis, definition, naming. → Symbolism
- `[ns_thoth_swords_003]` `[trigger: fire_water_conjunction]` `[factor_trigger: thoth_swords_ace AND element_air]` `[role: 条件分支]` Air from Fire-Water conjunction—less pure but first directly apprehended by normal consciousness. → Nature"""
    normalized_text_zh: str = """"""
    subject: str = "Ace of Swords (宝剑一)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_swords_ace_001', 'tarot_primordial_intellect', 'rel_swords_ace_002', 'tarot_integrating_mind', 'l1_anchor', 'confidence', 'evi_swords_ace_001', 'evi_swords_ace_002', 'tarot_primordial_intellect', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_swords_ace_001', 'tarot_swords_ace', 'astro_air_signs']
    
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
        l1_anchor="bot_v1.0.0_ace_of_swords__宝剑一_001_L1",
    )
    version: str = "1.0.0"
