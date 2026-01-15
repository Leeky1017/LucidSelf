"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.044673
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
    semantic_id="bot_v1.0.0_atu_xvi__the_tower__塔_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class AtuXviTheTower塔(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Peh (פ) | Hebrew letter "Mouth" | Word of truth |
| Eye of Shiva | Third eye destroyer | Annihilates illusion |
| Mars | Planet of destruction | Purifying force |
| Lightning | Sudden revelation | Shatters complacency |

**Source Text**:
> "This card represents the destruction of the world by Fire... The Eye of Horus or of Shiva opens... It corresponds to the letter Peh, which means 'mouth'... Mars is here in his most destructive aspect... The Tower is struck by lightning from above, and figures are falling from it... This is the necessary destruction of all that is outgrown, crystallized, or stagnant." (Book of Thoth, The Tower)

**Qabalistic Correspondences**:
- **Hebrew Letter**: Peh (פ, value 80) - "Mouth"
- **Path**: Connects Netzach (Victory) to Hod (Splendor) - The 27th Path
- **Planet**: Mars ♂ (destruction, war, force)
- **Element**: Fire (purifying, consuming)

**English Paraphrase**:
The Tower represents **sudden and necessary destruction of false structures**. The Eye of Shiva (or Horus) opens to annihilate illusion and stagnation. This is Mars in his most destructive aspect—not malicious but purifying, a **war against the crystallized ego and dead belief systems**. The Tower (symbolizing the rigid structure of false beliefs) is struck by lightning, its occupants falling as the prison of form shatters. The **Dove** (spirit) and **Serpent** (force) escape upward, liberated by destruction. **Peh** ("mouth") represents the Word of Truth that shatters complacency—the revelation that cannot be denied, the sudden realization that demolishes outdated worldviews. This is not accidental disaster but necessary clearing of what has become solidified, lifeless, and blocking evolution.

**完整中文诠释**:
塔代表着**突然且必要的虚假结构毁灭**。湿婆（或荷鲁斯）之眼睁开以摧毁幻象与停滞。这是火星最具破坏性的面向——并非恶意而是净化，是对**僵化自我与死亡信仰系统的战争**。塔（象征着虚假信念的刚性结构）被闪电击中，其居住者坠落，形式的监狱破碎。**鸽子**（灵性）与**蛇**（力量）向上逃逸，被毁灭所解放。**Peh**（"嘴"）代表粉碎自满的真理之言——无法否认的启示，摧毁过时世界观的突然觉醒。这不是意外灾难，而是对已僵化、无生命、阻碍进化之物的必要清理。

**Core Points**:
- **Necessary Destruction**: Not random disaster but purposeful purging of dead forms
- **Eye of Shiva**: Divine destruction that clears way for creation
- **Mars Purification**: War against false structures, not against truth
- **Liberation**: Dove and Serpent freed when prison collapses

**Detailed Explanation**:
The path from Netzach (Venus, emotion/instinct) to Hod (Mercury, intellect) shows how emotional attachments and mental rigidity must be shattered for true understanding. The Tower represents humanity's tendency to build false securities—beliefs, identities, structures that once served but now constrain. Mars strikes with lightning precision at exactly what needs to fall. The **Eye of Shiva** is the third eye opening—sudden awakening that sees through all illusion. When it opens, the false must be destroyed. The mouth (Peh) speaks the word that cannot be unheard—truth that demolishes comfortable lies.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Tower emphasizes necessary destruction, not random disaster. Eye of Shiva opens to annihilate illusion. Peh (Mouth) speaks truth that shatters. Mars purifies rather than destroys capriciously. Harris depicts Dove and Serpent freed when prison collapses.
- **中文**: Crowley的塔强调必要的毁灭而非随机灾难。湿婆之眼睁开消灭幻象。Peh（嘴）说出粉碎一切的真理。火星净化而非任意毁灭。Harris描绘鸽子和蛇在监狱崩塌时获释。

**Narrative Snippets**:
- `[ns_thoth_071]` `[trigger: tower_necessary_destruction]` `[factor_trigger: tarot_tower AND tarot_destruction]` `[role: 主干]` The Tower represents sudden and necessary destruction of false structures—not random disaster but purposeful purging of what has become solidified and blocks evolution. → English Paraphrase
- `[ns_thoth_072]` `[trigger: eye_of_shiva]` `[factor_trigger: tarot_shiva AND tarot_annihilation]` `[role: 主干依赖]` The Eye of Shiva opens to annihilate illusion—sudden awakening that sees through and destroys all false forms. → English Paraphrase
- `[ns_thoth_073]` `[trigger: peh_mouth_truth]` `[factor_trigger: tarot_peh AND tarot_truth]` `[role: 主干依赖]` Peh (Mouth) speaks the word of truth that shatters—revelation that cannot be denied, demolishing comfortable lies. → English Paraphrase
- `[ns_thoth_074]` `[trigger: dove_serpent_freed]` `[factor_trigger: tarot_dove AND tarot_serpent]` `[role: 总结]` Dove (spirit) and Serpent (force) escape upward, liberated when the prison of form collapses. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "ATU XVI: The Tower (塔)"
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
        l1_anchor="bot_v1.0.0_atu_xvi__the_tower__塔_001_L1",
    )
    version: str = "1.0.0"
