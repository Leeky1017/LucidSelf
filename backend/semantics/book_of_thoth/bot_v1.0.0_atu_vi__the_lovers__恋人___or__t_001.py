"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.044637
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
    semantic_id="bot_v1.0.0_atu_vi__the_lovers__恋人___or__t_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class AtuViTheLovers恋人OrT(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Zain (ז) | Hebrew letter "Sword" | Analysis, division |
| Solve et Coagula | Dissolve and coagulate | Alchemical maxim |
| Royal Marriage | King + Queen union | Sacred coniunctio |
| Orphic Egg | World-creation potential | New life from union |

**Source Text**:
> "This card and its twin, XIV, Art, are the most obscure and difficult of the Atu... Atu VI refers to Gemini, ruled by Mercury. It means The Twins. The Hebrew letter corresponding is Zain, which means a Sword, and the framework of the card is therefore the Arch of Swords, beneath which the Royal Marriage takes place. The Sword is primarily an engine of division. In the intellectual world... it represents analysis. This card and Atu XIV together compose the comprehensive alchemical maxim: Solve et coagula... This card is consequently one of the most fundamental cards in the Tarot. It is the first card in which more than one figure appears." (Book of Thoth, The Lovers or The Brothers)

**Qabalistic Correspondences**:
- **Hebrew Letter**: Zain (ז, value 7) - "Sword"
- **Path**: Connects Binah (Understanding) to Tiphareth (Beauty) - The 17th Path
- **Zodiac**: Gemini ♊ (The Twins)
- **Planet**: Mercury (ruler)
- **Element**: Air (intellectual realm)
- **Secret Title**: "The Children of the Voice, the Oracle of the Mighty Gods"

**English Paraphrase**:
The Lovers is the archetype of **Analysis and Synthesis**, representing the alchemical maxim **"Solve et Coagula"** (Dissolve and Coagulate). Unlike the Rider-Waite version depicting choice, this card shows the **Royal Marriage**—the sacred union of opposites beneath an Arch of Swords. The central figures are the Black King and White Queen in alchemical wedding, officiated by a hooded Hermit figure. Above them, Cupid (blindfolded) shoots his arrow, indicating that love transcends rational sight—it is an intuitive, not intellectual, union. The **Orphic Egg** entwined by a serpent at the base represents the potential for new creation emerging from the marriage of opposites. Gemini, ruled by Mercury, emphasizes the dual nature: the Sword (Zain) divides to analyze, yet division is the prerequisite for conscious reunion at a higher level. The card's alternative title "The Brothers" references the Cain-Abel mystery—the original creation myth involving necessary separation and sacrifice.

**完整中文诠释**:
恋人（The Lovers）是**分析与综合**的原型，代表着炼金术格言**"溶解与凝固"（Solve et Coagula）**。与韦特版本描绘选择不同，这张牌展示的是**皇室婚礼**——对立面在剑之拱门下的神圣结合。中心人物是黑王与白后的炼金术婚礼，由一位戴兜帽的隐者人物主持。在他们上方，蒙眼的丘比特射出箭矢，表明爱超越了理性视觉——这是一种直觉的而非智性的结合。底部被蛇缠绕的**奥菲斯之卵**（Orphic Egg）代表着从对立面婚姻中涌现的新创造潜能。双子座由水星掌管，强调了二元本质：剑（Zain）分割以分析，然而分割是在更高层次上有意识重聚的前提。这张牌的另一标题"兄弟"（The Brothers）引用了该隐-亚伯之谜——涉及必要的分离与牺牲的原初创世神话。

**Core Points**:
- **Solve et Coagula**: The dual alchemical process of dissolving and reuniting
- **Royal Marriage**: Union of King (Sulphur) and Queen (Mercury/Salt) producing the Philosophical Child
- **Analysis Before Synthesis**: Division by the Sword (intellect) enables conscious higher union
- **Twins/Brothers**: Duality as necessary stage in cosmic creation

**Detailed Explanation**:
The path of Zain descends from Binah (the Great Mother, form-giver) to Tiphareth (the Son, harmonized center), showing how division from the Mother-source enables individual consciousness to emerge. The Sword represents Mercury's analytical function—breaking down to understand. Yet Gemini is also about communication, the Voice (hence "Children of the Voice")—through language we separate reality into categories, but also through language we can consciously reunite them. The blindfolded Cupid indicates that the highest union is not achieved through logic but through love's intuitive wisdom. The Orphic Egg contains the World-Serpent Ophion, symbolizing that from cosmic division (the Sword's cut) emerges the potential for rebirth.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Lovers differs radically from RWS's choice imagery. This card shows alchemical Royal Marriage, not romantic choice. Zain (Sword) emphasizes analysis before synthesis. The "Brothers" title references Cain-Abel mystery. Paired with ATU XIV Art to complete "Solve et Coagula".
- **中文**: Crowley的恋人与RWS的选择意象根本不同。此牌展示炼金术皇室婚礼而非浪漫选择。Zain（剑）强调综合前的分析。“兄弟”标题引用该隐-亚伯之谜。与ATU XIV艺术配对完成“溶解与凝聚”。

**Narrative Snippets**:
- `[ns_thoth_059]` `[trigger: lovers_royal_marriage]` `[factor_trigger: tarot_lovers AND tarot_sacred_union]` `[role: 主干]` The Lovers shows the Royal Marriage—sacred union of opposites beneath an Arch of Swords, not romantic choice. → English Paraphrase
- `[ns_thoth_060]` `[trigger: zain_sword_analysis]` `[factor_trigger: tarot_zain AND tarot_analysis]` `[role: 主干依赖]` The Sword (Zain) divides to analyze—division is the prerequisite for conscious reunion at a higher level. → English Paraphrase
- `[ns_thoth_061]` `[trigger: solve_coagula_lovers]` `[factor_trigger: tarot_solve_coagula AND tarot_lovers]` `[role: 主干依赖]` Solve et Coagula: this card and ATU XIV Art together compose the comprehensive alchemical maxim. → English Paraphrase
- `[ns_thoth_062]` `[trigger: orphic_egg]` `[factor_trigger: tarot_orphic_egg AND tarot_creation]` `[role: 总结]` The Orphic Egg entwined by a serpent represents the potential for new creation emerging from the marriage of opposites. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "ATU VI: The Lovers (恋人) [or: The Brothers]"
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
        l1_anchor="bot_v1.0.0_atu_vi__the_lovers__恋人___or__t_001_L1",
    )
    version: str = "1.0.0"
