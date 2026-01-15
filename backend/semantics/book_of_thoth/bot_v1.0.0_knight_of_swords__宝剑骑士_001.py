"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.076566
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
    semantic_id="bot_v1.0.0_knight_of_swords__宝剑骑士_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class KnightOfSwords宝剑骑士(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Fire of Air | Storm wind | Violent thought |
| Maddened Steed | Wild mount | Uncontrolled rush |
| Revolving Wing | Spinning crest | Perpetual motion |
| Spirit of Tempest | Storm being | Destructive force |

**Title**: Lord of the Winds and the Breezes (风与疾风之主)
**Elemental**: The Fiery part of Air (气中之火)
**Zodiac**: 21° Taurus to 20° Gemini (金牛座21度至双子座20度)

**Source Text**:
> "The Knight of Swords represents the fiery part of Air; he is the wind, the storm. He represents the violent power of motion applied to an apparently manageable element. He rules from the 21st degree of Taurus to the 20th degree of Gemini. He is a warrior helmed, and for his crest he bears a revolving wing. Mounted upon a maddened steed, he drives down the Heavens, the Spirit of the Tempest. In one hand is a sword, in the other a poniard. He represents the idea of attack... activity and skill, subtlety and cleverness... prey of his idea, which comes to him as an inspiration without reflection. If ill-dignified... incapable of decision or purpose... 'Chimaera bombinans in vacuo'."

**English Paraphrase**:
**Storm of Mind** – Represents the **Fiery part of Air**: the wind and storm, violent motion of thought. He rides a maddened steed, bearing a sword and dagger, with a revolving wing‑crest helmet, crashing through the heavens like the **Spirit of the Tempest**. Psychologically, he is activity, skill, subtlety and cleverness – the mind seized by a brilliant idea and rushing to act **without reflection**. Positively, this is swift decision, daring argument, incisive strategy; negatively, it is scattered aggression, empty rhetoric, and attacks without purpose – a "chimaera buzzing in a void".

**Core**: **Aggressive Intellect** – Quick thinking, fierce debate, decisive action, but also rashness and over‑attack.

**Chinese Explanation**:
**宝剑骑士**代表**气中之火**：风暴般的心智能量。他骑着疯狂奔腾的战马，手持剑与短匕，头盔上是一只不断旋转的翅膀，如同**暴风之灵**从天而降。性格上，他极具**行动力、技巧、机智与聪明**，常常被某个突如其来的念头点燃，随即立刻付诸行动，而**来不及深入思考后果**。正向时，这带来**快速决断、犀利辩论、果断出击**；失衡时，则变成**散乱的攻击、空洞的言辞、为攻击而攻击**——仿佛"在虚空中嗡嗡乱叫的奇美拉"。他提醒人：锋利的理性也需要中心与方向，否则只是把一切撕裂。

**In Readings**: Sudden decisions, sharp words, bold moves, mental or verbal attack, urgent communication; or, rashness, cruelty in speech, pointless argument.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Knight of Swords is Fire of Air - storm and violent wind. Maddened steed charges heaven. Inspiration without reflection. If ill-dignified: "chimaera buzzing in a void".
- **中文**: Crowley的宝剑骑士是气中之火—风暴与狂风。疯狂战马冲击天空。灯感无反思。如果失衡："在虚空中嗡鸣的奇美拉"。

**Narrative Snippets**:
- `[ns_thoth_swords_031]` `[trigger: knight_swords_thoth]` `[factor_trigger: thoth_swords_knight]` `[role: 主干]` Knight of Swords = Fire of Air—wind and storm; violent power of motion; Spirit of Tempest. → Core
- `[ns_thoth_swords_032]` `[trigger: maddened_steed]` `[factor_trigger: thoth_swords_knight AND symbol_steed]` `[role: 条件分支]` Maddened steed, revolving wing crest—activity, skill, subtlety; prey of idea without reflection. → Visual
- `[ns_thoth_swords_033]` `[trigger: chimaera_void]` `[factor_trigger: thoth_swords_knight AND state_ill_dignified]` `[role: 条件分支]` If ill-dignified: "Chimaera bombinans in vacuo"—empty noise, attack without purpose. → Shadow"""
    normalized_text_zh: str = """"""
    subject: str = "Knight of Swords (宝剑骑士)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_swords_knight_001', 'tarot_storm_attack', 'rel_swords_knight_002', 'tarot_empty_aggression', 'l1_anchor', 'confidence', 'evi_swords_knight_001', 'evi_swords_knight_002', 'tarot_chimaera', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_swords_knight_001', 'tarot_swords_knight', 'astro_gemini']
    
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
        l1_anchor="bot_v1.0.0_knight_of_swords__宝剑骑士_001_L1",
    )
    version: str = "1.0.0"
