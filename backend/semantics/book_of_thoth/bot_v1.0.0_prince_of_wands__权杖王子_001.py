"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.088937
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
    semantic_id="bot_v1.0.0_prince_of_wands__权杖王子_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class PrinceOfWands权杖王子(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Air of Fire | Expanding fire | Volatilization |
| Lion Chariot | Noble vehicle | Powerful charge |
| To Mega Therion | Great Beast sigil | Crowleyan current |
| Dramatic Energy | Expressive force | Romantic action |

**Title**: The Prince of the Chariot of Fire (火之战车的王子)
**Elemental**: The Airy part of Fire (火中之气)
**Zodiac**: 21° Cancer to 20° Leo

**Source Text**:
> "The Prince of Wands represents the airy part of Fire, with its faculty of expanding and volatilising. ... He is a warrior... his arms are bare... He wears a rayed crown surmounted by a lion's head winged... On his breast is the sigil of To Mega Therion. ... Swiftness and strength. ... He states a vigorous proposition for the sake of stating it. ... essentially just, but always feels that justice is not to be attained in the intellectual world."

**English Paraphrase**:
**Expansive Energy** - Represents the **Airy part of Fire** (expansion, volatilization). Rules from late Cancer to Leo. He rides a chariot drawn by a lion, wearing the sigil of **To Mega Therion** (The Great Beast). Qualities: **Swiftness, strength, intensity**. He is noble and generous but prone to boasting and elaborate pranks. He fights against odds and wins through endurance. He is "Air" (Intellect) applied to Fire, making him romantic, dramatic, and sometimes a "symbol of Terror" due to mystery.

**Core**: **Dynamic Expression** - Expansion, drama, assertion, creativity, endurance, unpredictability, noble but volatile.

**Chinese Explanation**:
**权杖王子**代表**火中之气**（火的扩展和挥发能力）。掌管巨蟹座21度到狮子座20度。他驾驶狮子战车，胸前佩戴**To Mega Therion**（大兽）的印记。品质：**迅速、力量、强度**。他高尚大方，但倾向于吹牛和恶作剧。他对抗逆境并通过耐力获胜。他是应用于火的"气"（智力），使他浪漫、戏剧化，有时因神秘感而成为"恐怖的象征"。

**In Readings**: Impulsive action, dramatic expression, swiftness, travel, creativity, unpredictability, intense loyalty/leadership.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Prince of Wands represents Air of Fire (expansion, volatilization). Lion chariot symbolizes noble forward charge. To Mega Therion sigil links to Crowleyan magic. Generous but prone to boasting.
- **中文**: Crowley的权杖王子代表火中之气（扩张、挥发）。狮子战车象征高贵向前冲锋。To Mega Therion印记连接Crowley魔法。慰慨但容易吹牛。

**Narrative Snippets**:
- `[ns_thoth_wands_037]` `[trigger: prince_wands_thoth]` `[factor_trigger: thoth_wands_prince]` `[role: 主干]` Prince of Wands = Air of Fire—expanding and volatilizing; swiftness, strength, dramatic energy. → Core
- `[ns_thoth_wands_038]` `[trigger: lion_chariot_mega]` `[factor_trigger: thoth_wands_prince AND symbol_lion_chariot]` `[role: 条件分支]` Lion-drawn chariot; To Mega Therion sigil on breast—noble forward charge; Crowleyan current. → Visual
- `[ns_thoth_wands_039]` `[trigger: romantic_endurance]` `[factor_trigger: thoth_wands_prince AND state_character]` `[role: 条件分支]` Romantic and generous but prone to boasting; fights against odds, wins through endurance. → Character"""
    normalized_text_zh: str = """"""
    subject: str = "Prince of Wands (权杖王子)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_prince_wands_air', 'air_of_fire', 'rel_prince_wands_drama', 'dramatic_energy', 'prince_wands_expansion']
    
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
        l1_anchor="bot_v1.0.0_prince_of_wands__权杖王子_001_L1",
    )
    version: str = "1.0.0"
