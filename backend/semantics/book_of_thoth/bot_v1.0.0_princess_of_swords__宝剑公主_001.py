"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.076611
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
    semantic_id="bot_v1.0.0_princess_of_swords__宝剑公主_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class PrincessOfSwords宝剑公主(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Earth of Air | Fixed volatile | Idea into matter |
| Medusa Helm | Terrifying clarity | Protective power |
| Barren Altar | Profaned sacred | Demands redress |
| Minerva/Artemis | Wisdom + hunt | Warrior maiden |

**Title**: Princess of the Rushing Winds, Lotus of the Palace of Air (疾风公主，气之宫殿之莲)
**Elemental**: The Earthy part of Air (气中之土)
**Rule**: Quadrant around North Pole (北极周围象限)

**Source Text**:
> "The Princess of Swords represents the earthy part of Air, the fixation of the volatile. She brings about the materialization of Idea. She represents the influence of Heaven upon Earth. She partakes of the characteristics of Minerva and Artemis, and there is some suggestion of the Valkyrie. She represents to some extent the anger of the Gods... she appears helmed, with serpent-haired Medusa for her crest. She stands in front of a barren altar as if to avenge its profanation, and she stabs downward with her sword. The heaven and the clouds, which are her home, seem angry... Her logic is destructive... great practical wisdom and subtlety in material things... very adroit in the settlement of controversies."

**English Paraphrase**:
**Fixing Ideas into Form** – Represents the **Earthy part of Air**: the fixation of the volatile, bringing **ideas down into matter**. She is linked with **Minerva and Artemis**, and hints of a Valkyrie – warrior‑maiden of intelligent justice. Wearing a helm crested with **Medusa's head**, she stands before a barren altar, stabbing downward as if avenging its profanation. The clouds around her seem angry. She is sharp, incisive and practical: able to use logic to cut through confusion and to manage real‑world controversies with great skill. Yet her logic can also be **destructive**, and when ill‑dignified she becomes harsh, anxious, and trapped in low cunning.

**Core**: **Incisive Realism** – Bringing analysis into concrete action, problem‑solving, exposing corruption, but with risk of harshness.

**Chinese Explanation**:
**宝剑公主**代表**气中之土**，即把**轻盈多变的观念固定下来、落实到现实**的能力。她兼具**密涅瓦（智慧女神）**与**阿耳忒弥斯（狩猎女神）**的特质，并带有女武神的影子：冷静、敏锐、擅长在现实冲突中作出判断。她头戴以**美杜莎之首**为顶饰的头盔，站在一座荒芜祭坛前，手中宝剑直刺向下，像是在为被亵渎的神圣秩序报仇。她所处的天空与云层也显得愤怒。正位时，她拥有**极强的现实判断力和争议处理能力**，能用理性和语言为真相辩护，或拆穿谎言与不公。失衡时，她的理性变成**破坏性的挑剔与焦虑**，在琐碎算计与低级狡诈中耗损自己，也伤害他人。

**In Readings**: Practical problem‑solver, sharp‑tongued advocate, exposing lies, dealing with legal or intellectual conflicts; or, nit‑picking, anxiety, harsh criticism, scheming.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Princess of Swords is Earth of Air - fixation of volatile. Medusa helm shows terrifying clarity. Stabs downward at barren altar. Minerva/Artemis/Valkyrie archetype. Logic can be destructive.
- **中文**: Crowley的宝剑公主是气中之土—固定挥发之物。美杜莎头盔显示可怕清明。向下刺向荒芜祭坛。密涅瓦/阿耳忽弥斯/女武神原型。逻辑可能具破坏性。

**Narrative Snippets**:
- `[ns_thoth_swords_040]` `[trigger: princess_swords_thoth]` `[factor_trigger: thoth_swords_princess]` `[role: 主干]` Princess of Swords = Earth of Air—fixation of volatile; materialization of Idea; Minerva/Artemis. → Core
- `[ns_thoth_swords_041]` `[trigger: medusa_helm]` `[factor_trigger: thoth_swords_princess AND symbol_medusa]` `[role: 条件分支]` Medusa helm, barren altar—stabs downward to avenge profanation; angry clouds surround. → Visual
- `[ns_thoth_swords_042]` `[trigger: practical_wisdom]` `[factor_trigger: thoth_swords_princess AND state_character]` `[role: 条件分支]` Great practical wisdom and subtlety; adroit in settling controversies; logic can be destructive. → Character"""
    normalized_text_zh: str = """"""
    subject: str = "Princess of Swords (宝剑公主)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_princess_swords_earth', 'earth_of_air', 'rel_princess_swords_avenge', 'clarity', 'princess_swords_fix']
    
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
        l1_anchor="bot_v1.0.0_princess_of_swords__宝剑公主_001_L1",
    )
    version: str = "1.0.0"
