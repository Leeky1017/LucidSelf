"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.044623
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
    semantic_id="bot_v1.0.0_atu_ix__the_hermit__隐士_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class AtuIxTheHermit隐士(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Yod (י) | Hebrew letter "Hand" | Seed of creation |
| Virgo | Mutable earth sign | Analytical discrimination |
| Lamp | Inner truth | Protected wisdom |
| Cerberus | Three-headed guardian | Threshold keeper |

**Source Text**:
> "This card is attributed to Yod, the foundation and father of all the letters... Yod means 'hand', the agent of creation... The card is referred to Virgo... The Hermit bears the Lamp of Truth, protected by his mantle... Behind him is the three-headed dog Cerberus... He is completely veiled; he is the Ancient One." (Book of Thoth, The Hermit)

**Qabalistic Correspondences**:
- **Hebrew Letter**: Yod (י, value 10) - "Hand"
- **Path**: Connects Chesed (Mercy) to Tiphareth (Beauty) - The 20th Path
- **Zodiac**: Virgo ♍ (The Virgin)
- **Element**: Earth (mutable earth—analytical, discriminating)

**English Paraphrase**:
The Hermit is the archetype of **inner wisdom through withdrawal**. He represents the **solitary seeker** who must retreat from external distractions to find the light within. The **Lamp** he carries is the inner truth, carefully protected beneath his mantle—wisdom that can only be discovered through introspection. **Yod** (the smallest Hebrew letter) symbolizes the seed point of creation, the primal spark from which all emerges. As "hand," Yod represents the agent of creation—the hand that grasps truth. Virgo's analytical nature is expressed through careful discrimination: sorting truth from illusion through patient examination. The **three-headed dog Cerberus** behind him guards the threshold between conscious and unconscious realms. The Hermit is "completely veiled"—the Ancient One, the Wise Old Man who has turned inward to discover the eternal.

**完整中文诠释**:
隐士是**通过退隐获得内在智慧**的原型。他代表着**孤独的寻道者**，必须从外部干扰中退避才能找到内在之光。他携带的**灯盏**是内在真理，小心地保护在斗篷之下——只能通过内省才能发现的智慧。**Yod**（最小的希伯来字母）象征着创造的种子点，万物从中涌现的原初火花。作为"手"，Yod代表创造的媒介——掌握真理的手。处女座的分析本质通过仔细的辨别来表达：通过耐心审视将真理从幻象中分离。他身后的**三头犬刻耳柏洛斯**守护着意识与无意识领域之间的门槛。隐士"完全被遮蔽"——远古智者，向内探寻以发现永恒的智慧老人。

**Core Points**:
- **Inner Light**: Truth found through withdrawal and introspection
- **Yod as Seed**: Smallest letter containing all potential, hand grasping wisdom
- **Virgo Discrimination**: Analytical sorting of truth from illusion
- **Cerberus Guardian**: Threshold between conscious and unconscious

**Detailed Explanation**:
The path from Chesed (expansive mercy) to Tiphareth (centered beauty) shows wisdom descending from abundance to human consciousness. Virgo's mutable earth is not static—it analyzes, refines, discriminates. The Hermit's lamp is shielded from wind (external influences), showing that inner truth must be protected during the seeking phase. The "Ancient One" represents timeless wisdom accessible only through solitude.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Hermit emphasizes Yod (smallest letter, seed of creation) and Virgo's analytical discrimination. The shielded lamp shows protected inner truth. Cerberus guards the threshold between conscious and unconscious. Harris depicts the "Ancient One" veiled completely, indicating timeless wisdom beyond form.
- **中文**: Crowley的隐士强调Yod（最小字母，创造种子）和处女座的分析辨别。被遮蔽的灯盏显示受保护的内在真理。刻耳柏洛斯守护意识与无意识之间的门槛。Harris将"远古智者"完全遮蔽描绘，表示超越形式的永恒智慧。

**Narrative Snippets**:
- `[ns_thoth_055]` `[trigger: hermit_inner_light]` `[factor_trigger: tarot_hermit AND tarot_inner_light]` `[role: 主干]` The Hermit carries the Lamp of Truth protected beneath his mantle—wisdom that can only be discovered through introspection. → English Paraphrase
- `[ns_thoth_056]` `[trigger: yod_seed]` `[factor_trigger: tarot_yod AND tarot_seed]` `[role: 主干依赖]` Yod (smallest Hebrew letter) symbolizes the seed point of creation, the primal spark from which all emerges. → English Paraphrase
- `[ns_thoth_057]` `[trigger: virgo_discrimination]` `[factor_trigger: tarot_virgo AND tarot_discrimination]` `[role: 主干依赖]` Virgo's analytical nature is expressed through careful discrimination: sorting truth from illusion through patient examination. → English Paraphrase
- `[ns_thoth_058]` `[trigger: cerberus_threshold]` `[factor_trigger: tarot_cerberus AND tarot_threshold]` `[role: 总结]` The three-headed dog Cerberus guards the threshold between conscious and unconscious realms—the Ancient One has crossed within. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "ATU IX: The Hermit (隐士)"
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
        l1_anchor="bot_v1.0.0_atu_ix__the_hermit__隐士_001_L1",
    )
    version: str = "1.0.0"
