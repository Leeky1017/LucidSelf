"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.044707
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
    semantic_id="bot_v1.0.0_atu_xix__the_sun__太阳_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class AtuXixTheSun太阳(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Resh (ר) | Hebrew letter "Head" | Consciousness seat |
| Heru-Ra-Ha | Twin Horus gods | Reconciled opposites |
| Green Hill | Fertile earth | Abundant manifestation |
| Broken Wall | Transcended barriers | Freedom achieved |

**Source Text**:
> "The Sun is the Lord of Light... Two children dance hand in hand (representing Heru-Ra-Ha, the twin gods of the new aeon)... They are free from the bondage of duality... The green mound represents fertile earth, manifestation... The wall has been broken through... This is simple, direct truth - 'The Sun is the source of Life.'" (Book of Thoth, The Sun)

**Qabalistic Correspondences**:
- **Hebrew Letter**: Resh (ר, value 200) - "Head"
- **Path**: Connects Hod (Splendor) to Yesod (Foundation) - The 30th Path
- **Planet**: Sun ☉ (life, consciousness, radiance)
- **Element**: Fire (vital, illuminating)

**English Paraphrase**:
The Sun represents **liberation, joy, and conscious success** - the radiant achievement of the Great Work. The Lord of Light shines directly, illuminating all. Two children (**Heru-Ra-Ha** - the twin gods representing active and passive forms of Horus) dance freely, no longer bound by the duality that constrained earlier stages. They celebrate on a **green hill** (fertile earth, abundant life) before a **broken wall** (barriers transcended). This is recovered innocence - not the naive innocence of the Fool but the earned simplicity that comes after completing the journey. The Sun's light is direct and clear, revealing simple truth without shadow or complexity.

**完整中文诠释**:
太阳代表着**解放、喜悦与意识成功**——伟大工作的辉煌成就。光之主直接照耀，照亮一切。两个孩子（**Heru-Ra-Ha**——代表荷鲁斯主动和被动形式的孪生神灵）自由跳舞，不再受早期阶段的二元对立束缚。他们在**绿色山丘**（肥沃大地，丰盛生命）上庆祝，面对**破碎的墙**（障碍被超越）。这是恢复的天真——不是愚者的天真无邪而是完成旅程后赢得的简单。太阳的光直接而清晰，揭示简单的真理而无阴影或复杂。

**Core Points**:
- **Radiant Success**: Direct light revealing achieved clarity
- **Freed from Duality**: Children dancing beyond opposites
- **Recovered Innocence**: Earned simplicity after completing journey
- **Broken Wall**: Barriers transcended, limitations overcome

**Detailed Explanation**:
The path from Hod (Mercury, intellect) to Yesod (Moon, foundation) shows consciousness illuminating the unconscious base. The Sun follows the Moon - after navigating darkness comes clear light. **Resh** ("head") represents consciousness itself, the seat of awareness. Heru-Ra-Ha ("Horus of the Double Horizon") represents the reconciled opposites: active/passive, masculine/feminine, strength/receptivity now dancing together in harmony.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Sun represents liberation and recovered innocence. Heru-Ra-Ha (twin Horus) dance freely beyond duality. Resh (Head) symbolizes consciousness. The broken wall shows transcended barriers. Green hill represents fertile manifestation.
- **中文**: Crowley的太阳代表解放和恢复的天真。Heru-Ra-Ha（孪生荷鲁斯）在二元之外自由跳舞。Resh（头）象征意识。破碎的墙显示超越的障碍。绿色山丘代表肥沃显化。

**Narrative Snippets**:
- `[ns_thoth_083]` `[trigger: sun_liberation]` `[factor_trigger: tarot_sun AND tarot_liberation]` `[role: 主干]` The Sun represents liberation, joy, and conscious success—the radiant achievement of the Great Work, revealing simple truth without shadow. → English Paraphrase
- `[ns_thoth_084]` `[trigger: heru_ra_ha]` `[factor_trigger: tarot_heru_ra_ha AND tarot_freedom]` `[role: 主干依赖]` Two children (Heru-Ra-Ha, the twin gods) dance freely, no longer bound by the duality that constrained earlier stages. → English Paraphrase
- `[ns_thoth_085]` `[trigger: broken_wall]` `[factor_trigger: tarot_barrier AND tarot_transcendence]` `[role: 主干依赖]` The broken wall signifies barriers transcended—limitations overcome, consciousness freed from confinement. → English Paraphrase
- `[ns_thoth_086]` `[trigger: recovered_innocence]` `[factor_trigger: tarot_innocence AND tarot_completion]` `[role: 总结]` This is recovered innocence—not the naive innocence of the Fool but the earned simplicity that comes after completing the journey. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "ATU XIX: The Sun (太阳)"
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
        l1_anchor="bot_v1.0.0_atu_xix__the_sun__太阳_001_L1",
    )
    version: str = "1.0.0"
