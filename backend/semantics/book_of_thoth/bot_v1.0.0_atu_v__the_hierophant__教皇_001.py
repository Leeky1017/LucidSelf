"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.044610
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
    semantic_id="bot_v1.0.0_atu_v__the_hierophant__教皇_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class AtuVTheHierophant教皇(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Vau (ו) | Hebrew letter "Nail" | Joining micro/macrocosm |
| Taurus | Fixed earth sign | Stable tradition |
| Four Kerubs | Guardian beasts | Shrine protectors |
| Aeonic Priest | 2000-year cycle | Era-defining teacher |

**Source Text**:
> "This card is referred to the letter Vau, which means a Nail... The card is referred to Taurus... the Throne of the Hierophant is surrounded by elephants, which are of the nature of Taurus; and he is actually seated upon a bull. Around him are the four beasts or Kerubs... for these are the guardians of every shrine. But the main reference is to the particular arcanum which is the principal business, the essential, of all magical work; the uniting of the microcosm with the macrocosm... It is the aeon of Horus, of the Child... the rhythm of the Hierophant is such that he moves only at intervals of 2,000 years." (Book of Thoth, The Hierophant)

**Qabalistic Correspondences**:
- **Hebrew Letter**: Vau (ו, value 6) - "Nail"
- **Path**: Connects Chokmah (Wisdom) to Chesed (Mercy) - The 16th Path
- **Zodiac**: Taurus ♉ (Bull)
- **Planet**: Venus (ruler), Moon (exalted)
- **Element**: Earth (strongest, most balanced form)

**English Paraphrase**:
The Hierophant is the archetype of **Tradition**, **Teaching**, and **Initiation**, representing Taurus as the grounded, stable transmitter of sacred wisdom. He is the **Keeper of Mysteries** who bridges the gap between the divine (macrocosm) and the human (microcosm) through established institutions and initiatory rites. The **Nail** (Vau) symbolizes that which fixes, connects, and holds together—the fastening principle that secures spiritual truths to earthly transmission. He sits enthroned upon a bull, surrounded by elephants (Taurus nature: patient, massive, unstoppable strength), with the four Kerubim (Bull, Lion, Eagle, Man) guarding the shrine at each corner. Before him is a transparent oriel displaying a **hexagram** (macrocosm) containing a **pentagram** (microcosm, the dancing Child Horus), symbolizing the magical operation of uniting above and below. The **Scarlet Woman** stands armed with a sword—Venus in the New Aeon, no longer passive but militant. The Hierophant's wand bears three interlaced rings representing the three Aeons (Isis, Osiris, Horus) operating on deep indigo (Saturn, Lord of Time).

**完整中文诠释**:
教皇（The Hierophant）是**传统**、**教导**与**启蒙**的原型，代表着金牛座（Taurus）作为扎根大地的、稳定的神圣智慧传递者。他是**奥秘守护者**（Keeper of Mysteries），通过既定的机构与启蒙仪式在神圣（宏观宇宙）与人类（微观宇宙）之间架起桥梁。**钉子**（Vau）象征着固定、连接与结合的原则——将灵性真理稳固地钉在尘世传承之上的紧固装置。他端坐于公牛之上，周围环绕着大象（金牛座本性：耐心、巨大、不可阻挡的力量），四个圣兽（Kerubim：牛、狮、鹰、人）守护着圣坛的四个角落。在他面前是透明的凸窗，展示着一个**六芒星**（宏观宇宙），其中包含一个**五角星**（微观宇宙，舞蹈的童子荷鲁斯），象征着将"上与下"结合的魔法操作。**猩红女人**（Scarlet Woman）手持宝剑站立——新纪元中的金星，不再被动而是战斗性的。教皇的权杖上有三个交织的环，代表三个纪元（伊西斯、奥西里斯、荷鲁斯）运作于深靛蓝色（土星，时间之主）之上。

**Core Points**:
- **Uniting Microcosm and Macrocosm**: The central magical operation of bridging human and divine
- **Aeon of the Child**: New Thelemic current replacing the "Dying God" formula
- **2,000-Year Rhythm**: The Hierophant moves only at epochal intervals (Aeons)
- **Tradition as Living Transmission**: Not dead dogma but active initiation

**Detailed Explanation**:
The path of Vau connects Chokmah (the creative Word) with Chesed (the organizing mercy), representing how divine wisdom is crystallized into stable, teachable form. Taurus as the Bull Kerub represents Earth at its strongest—neither the scattered earth of Virgo nor the crystallized earth of Capricorn, but the fertile, stable ground of spring growth. The nine nails at the top fix the oriel (Moon's influence, exalted in Taurus). The Scarlet Woman represents the New Aeon formula from Liber AL: "Let the woman be girt with a sword before me" (III:11). The dancing Child in the pentagram is Horus, the crowned and conquering child, whose innocent wantonness carries a mysterious, even sinister edge—the Hierophant appears to enjoy "a very secret joke at somebody's expense," referencing the Pasiphae legend (origin of all Bull-god myths).

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Hierophant integrates New Aeon symbolism (Horus child, Scarlet Woman with sword) into traditional Taurus/Venus imagery. Vau (Nail) joins micro/macrocosm. The 2000-year rhythm marks aeonic shifts. Four Kerubs guard the shrine. Harris depicts both tradition and Thelemic innovation.
- **中文**: Crowley的教皇将新纪元象征（荷鲁斯孩童、持剑猩红女人）融入传统金牛/金星意象。Vau（钉子）连接小宇宙/大宇宙。2000年节律标记纪元转换。四圣兽守护圣堂。Harris同时描绘传统与泰勒玛创新。

**Narrative Snippets**:
- `[ns_thoth_051]` `[trigger: hierophant_bridge]` `[factor_trigger: tarot_hierophant AND tarot_bridge]` `[role: 主干]` The Hierophant bridges macrocosm and microcosm—the central magical operation, uniting divine and human through established initiatory rites. → English Paraphrase
- `[ns_thoth_052]` `[trigger: vau_nail]` `[factor_trigger: tarot_vau AND tarot_connection]` `[role: 主干依赖]` Vau (Nail) is the fastening principle that secures spiritual truths to earthly transmission—the fixed connection between realms. → English Paraphrase
- `[ns_thoth_053]` `[trigger: aeon_rhythm]` `[factor_trigger: tarot_aeon AND tarot_rhythm]` `[role: 主干依赖]` The Hierophant moves only at intervals of 2,000 years—his rhythm marks epochal shifts (Isis→Osiris→Horus). → English Paraphrase
- `[ns_thoth_054]` `[trigger: scarlet_woman_sword]` `[factor_trigger: tarot_scarlet_woman AND tarot_venus]` `[role: 总结]` The Scarlet Woman stands armed with a sword—Venus in the New Aeon, no longer passive but militant. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "ATU V: The Hierophant (教皇)"
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
        l1_anchor="bot_v1.0.0_atu_v__the_hierophant__教皇_001_L1",
    )
    version: str = "1.0.0"
