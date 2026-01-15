"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.439639
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
    semantic_id="dvd_v1.0.0_altar_祭坛_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Altar祭坛(SemanticEntry):
    """
    ### Source Text

> **General Meaning**: A place of sacrifice.

**Dreams - Positive**: It could be th...
    """
    
    original_text: str = """### Source Text

> **General Meaning**: A place of sacrifice.

**Dreams - Positive**: It could be that the Lord is asking you to give something up. The point of a sacrifice is to yield something valuable to you. The most famous example is Abraham and Isaac. If you feel the Lord has been asking you to give something up and then you dream of an altar, it is a confirmation of what He is telling you. It is time to give that thing up to Him and let go.

**Scripture (Positive)**: Philippians 4:18 - "But I have all, and abound: I am full, having received from Epaphroditus the things which were sent from you, an odour of a sweet smell, a sacrifice acceptable, wellpleasing to God."

**Dreams - Negative**: If you are having nightmares or negative dreams of ritual sacrifice, then there is an indication that something is wrong in your spiritual life. Has there been a history of witchcraft or false religion in your family generations? If so, the Lord is exposing a generational curse that needs to be dealt with. If you wake from dreams in fear, it is demonic attack (no interpretation).

**Visions - Positive**: Death to the flesh. Giving up things that hinder your work. Laying sins and iniquity on the altar. 'Burning your bridges' as Elisha did (burned cattle and plow on altar).

**Visions - Negative**: May speak of idol worship and demonic rituals.

**See also**: Baptism, Bath, Blood, Death

### Key Terms

| Term | Definition | Significance |
|------|------------|--------------|
| Altar | Place of sacrifice | Surrender, offering |
| Sacrifice | Yielding something valuable | Obedience, letting go |
| Generational curse | Sin patterns from ancestors | Needs deliverance |

### English Paraphrase

Altar = place of sacrifice. **Positive**: God asking you to surrender something valuable—like Abraham with Isaac. Dreaming of altar confirms God's call to let go. Represents death to flesh, burning bridges (Elisha), acceptable sacrifice to God. **Negative**: Nightmare of ritual sacrifice indicates spiritual problems—possibly generational curses (witchcraft/false religion in family history) needing deliverance. Waking in fear from such dreams = demonic attack, no interpretation needed. Also can represent idol worship and demonic rituals.

### Chinese Interpretation（完整对等诠释）

祭坛 = 献祭之地。**正面**：神要求你交出有价值的东西——如亚伯拉罕献以撒。梦见祭坛确认神呼召你放手。代表向肉体死、破釜沉舟（以利沙）、蒙神悦纳的祭物。**负面**：关于祭祀仪式的噩梦表示灵性问题——可能是世代咒诅（家族中的巫术/假宗教历史）需要释放。从这类梦中惊醒恐惧 = 魔鬼攻击，无需解释。也可代表偶像崇拜和魔鬼仪式。

### Core Points

- 祭坛 = 献祭之地、交托象征
- 正面：神呼召你放下有价值的事物
- 亚伯拉罕献以撒的模式
- 代表向肉体死、破釜沉舟
- 负面：祭祀噩梦 → 灵性问题/世代咒诅
- 恐惧中醒来 = 魔鬼攻击（无解释）

### Narrative Snippets

- `[ns_dav_a016]` `[trigger: 梦祭坛]` `[factor_trigger: dream_symbol_altar]` `[role: 主干]` Altar = place of sacrifice—God asking you to surrender something valuable to Him. → Dreams Dictionary #Altar
- `[ns_dav_a017]` `[trigger: 祭坛正面]` `[factor_trigger: dream_symbol_altar AND dream_positive]` `[role: 条件分支]` Positive: Confirmation to let go, death to flesh, burning bridges like Elisha. → Dreams Dictionary #Altar
- `[ns_dav_a018]` `[trigger: 祭坛负面]` `[factor_trigger: dream_symbol_altar AND dream_negative AND generational_curse]` `[role: 条件分支]` Ritual sacrifice nightmare = spiritual problems, possibly generational curses needing deliverance. → Dreams Dictionary #Altar
- `[ns_dav_a019]` `[trigger: 祭坛恐惧]` `[factor_trigger: dream_symbol_altar AND wake_feeling]` `[role: 例外处理]` Waking in fear = demonic attack, no interpretation—needs warfare response. → Dreams Dictionary #Altar"""
    normalized_text_zh: str = """"""
    subject: str = "Altar 祭坛"
    factor_refs: list = ['dream_symbol_altar', 'concept_sacrifice', 'concept_generational_curse']
    
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
        book_id="dreams_visions_dict",
        chapter="",
        l1_anchor="dvd_v1.0.0_altar_祭坛_001_L1",
    )
    version: str = "1.0.0"
