"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.027419
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
    semantic_id="bot_v1.0.0_knight_of_cups__圣杯骑士_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class KnightOfCups圣杯骑士(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Fire of Water | Passionate flow | Swift dissolution |
| Crab from Cup | Cancer symbol | Cardinal Water |
| Peacock | Iridescent totem | Water's brilliance |
| Romantic Surge | Emotional rush | Charming but unstable |

**Title**: Lord of the Waves and the Waters (波涛与诸水之主)
**Elemental**: The Fiery part of Water (水中之火)
**Zodiac**: 21° Aquarius to 20° Pisces (宝瓶座21度至双鱼座20度)

**Source Text**:
> "The Knight of Cups represents the fiery part of Water, the swift passionate attack of rain and springs; more intimately, Water's power of solution. He rules the Heavens from the 21st degree of Aquarius to the 20th degree of Pisces. He is a warrior partly clad in armour... his helmet is surmounted by an eagle, and his chariot, which resembles a shell, is also drawn by an eagle... In his right hand he bears a cup from which issues a crab, the cardinal sign of Water... His totem is the peacock, for one of the stigmata of water in its most active form is brilliance."

**English Paraphrase**:
**Passionate Flow** - Represents the **Fiery part of Water**: the swift, passionate rush of rain and springs, and Water's power of dissolution. He rides a leaping white horse, clad in winged black armour, bearing a cup from which a **crab** (Cancer) emerges as a sign of cardinal Water. His totem **peacock** shows Water's brilliance and iridescence. Psychologically, he is graceful, impressionable, and easily enthused, but not enduring. Positively, he brings romantic inspiration and movement; negatively, he can become sensual, idle, untruthful, or self-dissolving ("his name is writ in water").

**Core**: **Romantic Surge** - Swift emotional movement, charm, seduction, idealized love, but with risk of instability and escapism.

**Chinese Explanation**:
**圣杯骑士**代表**水中之火**（水的热情/突发动力），如骤雨、泉水倾泻，以及水的**溶解能力**。他乘坐跳跃的白马，身披带翼的黑色铠甲，手持圣杯，其中伸出代表本位水象的**巨蟹**。他的图腾是**孔雀**，象征水在最活跃形态下的绚烂与荧光。性格上，他优雅、感性、极易受外界吸引而燃起热情，却往往缺乏持久力。正位时，他带来浪漫灵感、感情邀约或心灵的柔软流动；失衡时，则可能流于**感官享乐、懒散、不诚实**，像那句"他的名字写在水上"——不稳定、不可靠、难以承诺。

**In Readings**: Romantic offer, invitation, travel over water, artistic inspiration, emotional message; or, if ill-dignified, escapism, addiction, unreliability.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Knight of Cups is Fire of Water - swift passionate flow. Crab from cup shows cardinal Water. Peacock totem represents Water's brilliance. "His name is writ in water" warns of instability.
- **中文**: Crowley的圣杯骑士是水中之火—迅速热情流动。杯中之蟹显示本位水。孔雀图腾代表水的绚丽。"他的名字写在水上"警告不稳定。

**Narrative Snippets**:
- `[ns_thoth_cups_031]` `[trigger: knight_cups_thoth]` `[factor_trigger: thoth_cups_knight]` `[role: 主干]` Knight of Cups = Fire of Water—swift passionate attack of rain/springs; Water's power of dissolution. → Core
- `[ns_thoth_cups_032]` `[trigger: crab_from_cup]` `[factor_trigger: thoth_cups_knight AND symbol_crab]` `[role: 条件分支]` Crab issues from cup—cardinal Water sign (Cancer); romantic invitation with dissolving power. → Visual
- `[ns_thoth_cups_033]` `[trigger: peacock_brilliance]` `[factor_trigger: thoth_cups_knight AND symbol_peacock]` `[role: 条件分支]` Peacock totem—Water's brilliance in active form; graceful but not enduring; "name writ in water". → Symbolism"""
    normalized_text_zh: str = """"""
    subject: str = "Knight of Cups (圣杯骑士)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_thoth_cups_knight', 'thoth_cups_knight', 'expressing', 'evi_thoth_cups_knight', 'thoth_cups_knight', 'rule_thoth_cups_knight', 'concept_thoth_cups_knight', 'decan_zodiac', 'archetype']
    
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
        l1_anchor="bot_v1.0.0_knight_of_cups__圣杯骑士_001_L1",
    )
    version: str = "1.0.0"
