"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.088873
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
    semantic_id="bot_v1.0.0_eight_of_wands__swiftness__权杖八_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class EightOfWandsSwiftness权杖八(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Hod in Fire | Splendour in Fire | Subtilized energy |
| Mercury in Sagittarius | Communication + fire | Swift message |
| Electrical Rays | Light-speed force | Transformed wands |
| Rainbow Spectrum | Pure light | Mathematical physics |

**Title**: Lord of Swiftness (迅速之主)
**Qabalistic**: Hod in Fire (火中之光辉)
**Astrological**: Mercury in Sagittarius (水星入射手座)

**Source Text**:
> "The remaining three cards of the suit belong to Sagittarius... subtilizing of the Fiery energy. ... Mercury rules the card... message of the original Will. The card also refers to Hod, splendour, in the suit of Fire... speech, light, electricity. The pictorial representation... shows the Light-wands turned into electrical rays... energy of high velocity... master-key to modern mathematical physics."

**English Paraphrase**:
**High Velocity Energy** - Corresponds to Hod (Intellect/Splendour) in Fire, representing the **subtilization** of fiery energy into light and electricity. Ruled by **Mercury in Sagittarius**, it brings down the message of the original Will. The wands have transformed into **electrical rays**, vibrating with high velocity. Above shines a rainbow, symbolizing the spectrum of pure light. It represents speed, communication, and energy that has transcended mere flame to become **intelligible geometrical form** (mathematical physics).

**Core**: **Swift Communication** - Speed, electricity, light, rapid processing, intellectual fire, messages, lack of heat but high energy.

**Chinese Explanation**:
**权杖八（迅速）**对应火元素中的Hod（光辉/智力），代表火能量的**精微化**，转化为光和电。对应**水星在射手座**，传递原始意志的信息。权杖变成了**电射线**，以高速振动。上方闪耀着彩虹，象征纯光的光谱。它代表速度、交流以及超越了单纯火焰、变成**可理解的几何形式**（数学物理）的能量。这是没有热量但极具速度的高能状态。

**In Readings**: Swiftness, speed, rapid communication, electricity, sudden action, messages, travel, high-frequency energy.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Eight of Wands shows fire subtilized into electricity and light. Mercury in Sagittarius brings message of original Will. Wands become electrical rays. Rainbow represents modern mathematical physics.
- **中文**: Crowley的权杖八展示火被精微化为电和光。水星入射手带来原始意志的信息。权杖变成电射线。彩虹代表现代数学物理。

**Narrative Snippets**:
- `[ns_thoth_wands_022]` `[trigger: eight_wands_swiftness]` `[factor_trigger: thoth_wands_eight]` `[role: 主干]` Eight of Wands = Lord of Swiftness—Hod in Fire; fire subtilized into light and electricity. → Core
- `[ns_thoth_wands_023]` `[trigger: mercury_sagittarius]` `[factor_trigger: thoth_wands_eight AND planet_mercury_sagittarius]` `[role: 条件分支]` Mercury in Sagittarius—message of original Will; high-velocity energy transmission. → Astrological
- `[ns_thoth_wands_024]` `[trigger: electrical_rays]` `[factor_trigger: thoth_wands_eight AND symbol_electrical]` `[role: 条件分支]` Wands become electrical rays; rainbow spectrum above—mathematical physics; speed without heat. → Visual"""
    normalized_text_zh: str = """"""
    subject: str = "Eight of Wands: Swiftness (权杖八：迅速)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_wands_eight_001', 'tarot_subtilized_energy', 'rel_wands_eight_002', 'tarot_high_velocity', 'l1_anchor', 'confidence', 'evi_wands_eight_001', 'evi_wands_eight_002', 'tarot_high_velocity', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_wands_eight_001', 'tarot_wands_eight', 'astro_mercury_sagittarius']
    
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
        l1_anchor="bot_v1.0.0_eight_of_wands__swiftness__权杖八_001_L1",
    )
    version: str = "1.0.0"
