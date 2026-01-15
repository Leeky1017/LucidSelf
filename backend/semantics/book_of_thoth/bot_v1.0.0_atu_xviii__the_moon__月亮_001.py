"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.044696
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
    semantic_id="bot_v1.0.0_atu_xviii__the_moon__月亮_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class AtuXviiiTheMoon月亮(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Qoph (ק) | Hebrew letter "Back of Head" | Unconscious realm |
| Anubis | Egyptian jackal god | Psychopomp guardian |
| Kephra | Scarab beetle | Sun through underworld |
| Dark Night | Soul's shadow crisis | Transformation passage |

**Source Text**:
> "This is the card of the threshold, the gateway to the abyss... The Moon is the waning moon, dark and treacherous... Two jackals (Anubis forms) guard the path... Below, the scarab beetle (Kephra) carries the sun through the darkness of the underworld... This represents the path of biological consciousness evolving from water (fish) to land (dog/jackal) to air (eagle/ibis)." (Book of Thoth, The Moon)

**Qabalistic Correspondences**:
- **Hebrew Letter**: Qoph (ק, value 100) - "Back of Head" (occipital lobe, unconscious)
- **Path**: Connects Netzach (Victory) to Malkuth (Kingdom) - The 29th Path
- **Zodiac**: Pisces ♓ (The Fish)
- **Element**: Water (unconscious, emotional, psychic)

**English Paraphrase**:
The Moon represents **confrontation with the unconscious and the Dark Night of the Soul**. This is the threshold of the Abyss—the dangerous passage where consciousness must navigate illusion, fear, and shadow. The **waning moon** casts deceptive shadows; reality becomes fluid and uncertain. **Anubis** (in jackal form) guards the gate—the psychopomp who guides souls through death's realm. The **scarab beetle** (Kephra) carries the hidden sun through the underworld, representing the journey of consciousness through darkness toward rebirth. This path shows **biological evolution**: from fish (water/unconscious) to jackal (land/instinct) to ibis (air/spirit). Pisces dissolves boundaries, making all things fluid and mutable. This is dangerous territory—deception, fear, psychic vulnerability—but also the necessary gateway to transformation and rebirth.

**完整中文诠释**:
月亮代表着**与无意识的对峙和灵魂的暗夜**。这是深渊的门槛——意识必须穿越幻象、恐惧和阴影的危险通道。**下弦月**投下欺骗性的阴影；现实变得流动和不确定。**阿努比斯**（豺狼形态）守卫着大门——引导灵魂穿越死亡领域的灵魂摆渡者。**圣甲虫**（凯普拉）携带隐藏的太阳穿过冥界，代表着意识通过黑暗走向重生的旅程。这条路径展示了**生物进化**：从鱼（水/无意识）到豺狼（陆/本能）到朱鹭（空/灵性）。双鱼座溶解边界，使万物流动可变。这是危险的领域——欺骗、恐惧、心灵脆弱——但也是通往转化和重生的必要门户。

**Core Points**:
- **Dark Threshold**: Gateway to the abyss, confronting unconscious shadow
- **Waning Moon**: Deceptive light, fluid reality, psychic danger
- **Anubis Guardian**: Psychopomp guiding through death/transformation
- **Kephra Journey**: Sun through underworld, consciousness through darkness to rebirth

**Detailed Explanation**:
The path from Netzach (Venus, instinctual victory) to Malkuth (material world) shows how consciousness must descend through the watery depths of the unconscious to fully manifest. **Qoph** (back of head) represents the occipital lobe—visual processing and dreams, where reality becomes mutable. The Moon is the **last major trial** before manifestation in the World. Pisces energy dissolves all fixed forms, making everything fluid—hence the danger of losing oneself in illusion. But this dissolution is necessary: the rigid ego-structures must liquefy before they can be reformed.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Moon emphasizes dark threshold and evolutionary ascent (fish→jackal→ibis). Qoph (Back of Head) represents unconscious processing. Anubis guards death's threshold. Kephra carries hidden sun through underworld. Pisces dissolves fixed forms.
- **中文**: Crowley的月亮强调黑暗门槛和进化上升（鱼→豺狼→朱鹮）。Qoph（后脑勺）代表无意识处理。阿努比斯守护死亡门槛。凯普拉携带隐藏的太阳穿越冒界。双鱼座溶解固定形式。

**Narrative Snippets**:
- `[ns_thoth_079]` `[trigger: moon_dark_threshold]` `[factor_trigger: tarot_moon AND tarot_unconscious]` `[role: 主干]` The Moon represents confrontation with the unconscious and the Dark Night of the Soul—the dangerous threshold where consciousness navigates illusion, fear, and shadow. → English Paraphrase
- `[ns_thoth_080]` `[trigger: anubis_guardian]` `[factor_trigger: tarot_anubis AND tarot_psychopomp]` `[role: 主干依赖]` Anubis in jackal form guards the gate—the psychopomp who guides souls through death's realm toward transformation. → English Paraphrase
- `[ns_thoth_081]` `[trigger: kephra_sun]` `[factor_trigger: tarot_kephra AND tarot_rebirth]` `[role: 主干依赖]` The scarab beetle Kephra carries the hidden sun through the underworld, representing the journey of consciousness through darkness toward rebirth. → English Paraphrase
- `[ns_thoth_082]` `[trigger: evolutionary_path]` `[factor_trigger: tarot_evolution AND tarot_consciousness]` `[role: 总结]` This path shows biological evolution: from fish (water/unconscious) to jackal (land/instinct) to ibis (air/spirit)—consciousness ascending. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "ATU XVIII: The Moon (月亮)"
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
        l1_anchor="bot_v1.0.0_atu_xviii__the_moon__月亮_001_L1",
    )
    version: str = "1.0.0"
