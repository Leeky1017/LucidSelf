"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.044649
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
    semantic_id="bot_v1.0.0_atu_vii__the_chariot__战车_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class AtuViiTheChariot战车(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Cheth (ח) | Hebrew letter "Fence" | Protective enclosure |
| Holy Grail | Sacred vessel | Contains divine essence |
| Cancer | Cardinal water sign | Protective initiation |
| No Reins | Will without force | Victory by character |

**Source Text**:
> "This card is attributed to Cancer... The Charioteer carries the Holy Grail... He wears armour constructed of scales like those of the crab... Around him are the four Kerubic figures... Yet the Charioteer is actually not moving at all; it is the whole Universe that is proceeding in obedience to his Will... There are no reins... Victory is by the force of character alone." (Book of Thoth, The Chariot)

**Qabalistic Correspondences**:
- **Hebrew Letter**: Cheth (ח, value 8) - "Fence/Enclosure"
- **Path**: Connects Binah (Understanding) to Geburah (Severity) - The 18th Path
- **Zodiac**: Cancer ♋ (The Crab)
- **Element**: Water (emotional realm, protective)

**English Paraphrase**:
The Chariot is the archetype of **Victory Through Will**, not through force. The Charioteer stands motionless yet triumphant, carrying the **Holy Grail** (container of divine essence). He wears armor made of crab shells (Cancer's protective nature), and is surrounded by the four Kerubic beasts (Bull, Lion, Eagle, Man) representing the four elements. Critically, **there are no reins**—the universe moves in obedience to his will, not through external control. The **Fence** (Cheth) represents protective enclosure: the ego as a necessary vessel that contains and carries the divine blood. This is victory of spirit descending into matter while maintaining integrity. Cancer's cardinal water energy initiates emotional mastery—not by suppressing feelings but by directing them through unwavering intent.

**完整中文诠释**:
战车（The Chariot）是**通过意志获胜**的原型，而非通过武力。战车手静止不动却凯旋而归，手持**圣杯**（神圣本质的容器）。他身披蟹壳制成的盔甲（巨蟹座的保护本质），周围环绕着四圣兽（牛、狮、鹰、人），代表四大元素。关键在于**没有缰绳**——宇宙服从他的意志而移动，而非通过外部控制。**围栏**（Cheth）代表保护性围合：自我作为必需的容器，容纳并承载神圣之血。这是灵性降入物质同时保持完整性的胜利。巨蟹座的本位水能量开启情感掌控——不是通过压制感受，而是通过坚定不移的意图来引导它们。

**Core Points**:
- **Victory Through Stillness**: Triumph achieved by unwavering will, universe moves around the still center
- **Holy Grail Bearer**: The ego as sacred vessel containing divine essence
- **No Reins Needed**: Control through alignment with cosmic will, not force
- **Fence as Protection**: Cheth's enclosure protects the sacred cargo

**Detailed Explanation**:
The path from Binah (Great Mother, form-giver) to Geburah (Severity, Mars-force) shows how protective maternal energy channels into disciplined power. Cancer's water is not passive—it's cardinal, initiating. The four sphinxes are deliberately mismatched colors, showing that mastering the elements doesn't mean making them uniform but directing their diverse energies toward one aim. The crab armor is both shield and symbol: Cancer's hard shell protects the soft vulnerability within, just as the ego protects the divine spark.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Chariot emphasizes victory through aligned will, not force (no reins). The Holy Grail is explicitly present (vs RWS). Cheth (Fence) represents protective ego containing divine essence. Cancer's cardinal water initiates emotional mastery. Harris depicts stillness at the center while universe moves.
- **中文**: Crowley的战车强调通过对齐意志而非武力获胜（无缰绳）。圣杯明确存在（对比RWS）。Cheth（围栏）代表容纳神圣本质的保护性自我。巨蟹座的本位水开启情感掌控。Harris描绘中心静止而宇宙移动。

**Narrative Snippets**:
- `[ns_thoth_063]` `[trigger: chariot_will_victory]` `[factor_trigger: tarot_chariot AND tarot_victory]` `[role: 主干]` Victory is by the force of character alone—the Charioteer stands motionless yet triumphant, the universe moves in obedience to his will. → English Paraphrase
- `[ns_thoth_064]` `[trigger: no_reins]` `[factor_trigger: tarot_control AND tarot_alignment]` `[role: 主干依赖]` There are no reins—control through alignment with cosmic will, not external manipulation. → English Paraphrase
- `[ns_thoth_065]` `[trigger: holy_grail_chariot]` `[factor_trigger: tarot_grail AND tarot_ego]` `[role: 主干依赖]` The Charioteer carries the Holy Grail—the ego as sacred vessel containing divine essence. → English Paraphrase
- `[ns_thoth_066]` `[trigger: cheth_fence]` `[factor_trigger: tarot_cheth AND tarot_containment]` `[role: 总结]` Cheth (Fence) represents protective enclosure: the ego as necessary vessel that contains and carries the divine blood. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "ATU VII: The Chariot (战车)"
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
        l1_anchor="bot_v1.0.0_atu_vii__the_chariot__战车_001_L1",
    )
    version: str = "1.0.0"
