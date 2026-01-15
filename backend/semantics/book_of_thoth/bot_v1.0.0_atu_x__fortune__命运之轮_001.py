"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.044597
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
    semantic_id="bot_v1.0.0_atu_x__fortune__命运之轮_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class AtuXFortune命运之轮(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Kaph (כ) | Hebrew letter "Palm" | Receiving/giving fortune |
| Jupiter | Planet of expansion | Fortune, opportunity |
| Three Creatures | Hermanubis/Sphinx/Typhon | Creation/preservation/destruction |
| ROTA/TARO | Wheel/Tarot anagram | Interconnected meanings |

**Source Text**:
> "This card represents the Universe in its aspect of continual change... The three figures on the wheel are the three forms of energy: Hermanubis ascending (creation), Sphinx stable at top (preservation), Typhon descending (destruction)... The ten spokes of the wheel refer to the ten Sephiroth... The letters on the wheel spell ROTA (wheel) and TARO, and also TORA (law) and ORAT (speaks), ATOR (Hathor, Venus)..." (Book of Thoth, Fortune)

**Qabalistic Correspondences**:
- **Hebrew Letter**: Kaph (כ, value 20) - "Palm/Hand"
- **Path**: Connects Chesed (Mercy) to Netzach (Victory) - The 21st Path
- **Planet**: Jupiter ♃ (expansion, fortune, cycles)
- **Element**: Fire (in some attributions)

**English Paraphrase**:
Fortune represents the **universal law of cycles and change**—the ever-turning wheel that raises and lowers all things. The wheel bears three figures: **Hermanubis** (dog-headed, ascending—creation phase), **Sphinx** (human-headed, stable at apex—preservation), and **Typhon** (serpent-headed, descending—destruction). These represent the eternal cycle of manifestation. Jupiter's influence brings expansion and opportunity, but also reminds us that all fortune is impermanent. The **ten spokes** correspond to the ten Sephiroth, showing how cosmic cycles permeate all levels of existence. The letters spell multiple words (ROTA/wheel, TARO, TORA/law, ORAT/speaks), revealing interconnected meanings. This is **karma as physics**, not morality—natural law where what rises must fall, what falls must rise.

**完整中文诠释**:
命运之轮代表着**宇宙循环与变化的普遍法则**——不断旋转的轮盘将万物升起又降落。轮上有三个形象：**赫曼努比斯**（狗头，上升中——创造阶段）、**斯芬克斯**（人头，稳定于顶点——保存阶段）、**提丰**（蛇头，下降中——毁灭阶段）。它们代表着显化的永恒循环。木星的影响带来扩展与机遇，但也提醒我们所有财运都是无常的。**十根辐条**对应着十个Sephiroth（生命之树的十个质点），展示宇宙循环如何渗透所有存在层次。轮上的字母拼出多个单词（ROTA/轮子、TARO、TORA/律法、ORAT/说话），揭示相互关联的含义。这是**业力作为物理学**而非道德——自然法则中上升的必然下降，下降的必然上升。

**Core Points**:
- **Universal Cycles**: Three phases (creation-preservation-destruction) eternally rotating
- **Jupiter Fortune**: Expansion and opportunity, but impermanent
- **Karma as Physics**: Natural law of cause-effect, not moral judgment
- **Ten Sephiroth**: Cycles operate at all cosmic levels

**Detailed Explanation**:
The path from Chesed (expansive mercy) to Netzach (enduring victory) shows how fortune flows from abundance to manifestation. The **Palm** (Kaph) represents the hand that both receives and gives—fortune flows through us. The multiple word-spellings (ROTA/TARO/TORA/ORAT) reveal the unity of wheel, tarot, law, and speech—all manifestations of the same cosmic principle. Understanding cycles brings wisdom; resisting them brings suffering.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Fortune's three creatures represent eternal creation-preservation-destruction cycle. The ten spokes correspond to ten Sephiroth. Multiple word-spellings (ROTA/TARO/TORA/ORAT) reveal interconnected cosmic principles. Jupiter brings expansion but not permanence. Karma here is physics, not morality.
- **中文**: 命运之轮的三个生物代表永恒的创造-保存-毁灭循环。十根辐条对应十个Sephiroth。多重拼写（ROTA/TARO/TORA/ORAT）揭示相互关联的宇宙原则。木星带来扩张但非永恒。此处业力是物理学而非道德。

**Narrative Snippets**:
- `[ns_thoth_047]` `[trigger: fortune_three_creatures]` `[factor_trigger: tarot_fortune AND tarot_cycle]` `[role: 主干]` Three creatures on the wheel—Hermanubis ascending (creation), Sphinx stable (preservation), Typhon descending (destruction)—represent the eternal cycle of manifestation. → English Paraphrase
- `[ns_thoth_048]` `[trigger: fortune_jupiter]` `[factor_trigger: tarot_fortune AND tarot_jupiter]` `[role: 主干依赖]` Jupiter's influence brings expansion and opportunity, but also reminds us that all fortune is impermanent. → English Paraphrase
- `[ns_thoth_049]` `[trigger: rota_taro]` `[factor_trigger: tarot_rota AND tarot_cosmic_unity]` `[role: 主干依赖]` The letters spell multiple words (ROTA/wheel, TARO, TORA/law, ORAT/speaks)—interconnected meanings revealing cosmic unity. → English Paraphrase
- `[ns_thoth_050]` `[trigger: karma_physics_fortune]` `[factor_trigger: tarot_karma AND tarot_natural_law]` `[role: 总结]` This is karma as physics, not morality—natural law where what rises must fall, what falls must rise. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "ATU X: Fortune (命运之轮)"
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
        l1_anchor="bot_v1.0.0_atu_x__fortune__命运之轮_001_L1",
    )
    version: str = "1.0.0"
