"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.088915
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
    semantic_id="bot_v1.0.0_knight_of_wands__权杖骑士_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class KnightOfWands权杖骑士(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Fire of Fire | Purest fire expression | Double intensity |
| Black Horse | Wild mount | Uncontrollable motion |
| Flaming Torch | Fire weapon | Lightning attack |
| Impetuosity | Rash action | No modification |

**Title**: The Prince of the Chariot of Fire (火之战车的王子)
**Elemental**: The Fiery part of Fire (火中之火)
**Zodiac**: 21° Scorpio to 20° Sagittarius

**Source Text**:
> "The Knight of Wands represents the fiery part of Fire... He is a warrior in complete armour. On his helmet for a crest he wears a black horse. In his hand he bears a flaming torch... The moral qualities... are activity, generosity, fierceness, impetuosity, pride, impulsiveness, swiftness... If wrongly energized, he is evil-minded, cruel, bigoted and brutal."

**English Paraphrase**:
**Fiery Impulse** - Represents the **Fiery part of Fire** (purest elemental expression). Rules from late Scorpio to Sagittarius. He is a warrior in armor with a black horse crest, riding a leaping black horse and carrying a flaming torch. Qualities: **Activity, fierceness, impetuosity, pride, swiftness**. He is the lightning flash. If ill-dignified, he becomes cruel, bigoted, and brutal—acting without modification or reflection.

**Core**: **Swift Action** - Impulsive energy, lightning speed, aggression, leadership, lack of endurance if blocked.

**Chinese Explanation**:
**权杖骑士**代表**火中之火**（元素的纯粹表达）。掌管天蝎座21度到射手座20度。他是全副武装的战士，头盔上有黑马饰章，骑着跳跃的黑马，手持火炬。道德品质：**活跃、猛烈、急躁、骄傲、冲动、迅速**。他是闪电。如果能量错误，他会变得邪恶、残酷、偏执和残暴——行动缺乏修正或反思。

**In Readings**: Swift action, impulsiveness, departure, aggression, creative flash, volatility, bold leadership.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Knight of Wands represents Fire of Fire (purest element). Black horse symbolizes wild, leaping motion. Flaming torch is weapon of lightning-like initiation. If wrongly energized: cruel, bigoted, brutal.
- **中文**: Crowley的权杖骑士代表火中之火（最纯元素）。黑马象征狂野跳跃运动。火炬是闪电般发动的武器。如果能量错误：残酷、偏执、野蛮。

**Narrative Snippets**:
- `[ns_thoth_wands_031]` `[trigger: knight_wands_thoth]` `[factor_trigger: thoth_wands_knight]` `[role: 主干]` Knight of Wands = Fire of Fire—fiery part of Fire; activity, fierceness, impetuosity, swiftness. → Core
- `[ns_thoth_wands_032]` `[trigger: black_horse_torch]` `[factor_trigger: thoth_wands_knight AND symbol_black_horse]` `[role: 条件分支]` Black horse crest, leaping mount; flaming torch weapon—lightning attack; no modification. → Visual
- `[ns_thoth_wands_033]` `[trigger: wrongly_energized]` `[factor_trigger: thoth_wands_knight AND state_ill_dignified]` `[role: 条件分支]` If wrongly energized: evil-minded, cruel, bigoted, brutal—fire without guidance. → Shadow"""
    normalized_text_zh: str = """"""
    subject: str = "Knight of Wands (权杖骑士)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_wands_knight_001', 'tarot_fiery_impulse', 'rel_wands_knight_002', 'tarot_lightning_attack', 'l1_anchor', 'confidence', 'evi_wands_knight_001', 'evi_wands_knight_002', 'tarot_fiery_impulse', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_wands_knight_001', 'tarot_wands_knight', 'astro_sagittarius']
    
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
        l1_anchor="bot_v1.0.0_knight_of_wands__权杖骑士_001_L1",
    )
    version: str = "1.0.0"
