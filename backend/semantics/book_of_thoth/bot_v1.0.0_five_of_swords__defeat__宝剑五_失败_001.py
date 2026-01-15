"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.076458
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
    semantic_id="bot_v1.0.0_five_of_swords__defeat__宝剑五_失败_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class FiveOfSwordsDefeat宝剑五失败(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Geburah in Air | Severity in Air | Disruption |
| Venus in Aquarius | Soft idealism | Enfeebles will |
| Inverted Pentagram | Matter over spirit | Defeat symbol |
| Broken Swords | Damaged weapons | Mental collapse |

**Title**: Lord of Defeat (失败之主)
**Qabalistic**: Geburah in Air (气中之严厉)
**Astrological**: Venus in Aquarius (金星入宝瓶座)

**Source Text**:
> "Geburah, as always, produces disruption; but as Venus here rules Aquarius, weakness rather than excess of strength seems the cause of disaster. The intellect has been enfeebled by sentiment. The defeat is due to pacifism. Treachery also may be implied. The hilts of the swords form the inverted pentagram... none of the hilts resembles any of the others, and their blades are crooked or broken. They give the impression of drooping; only the lowest of the swords points upwards, and this is the least effective of the weapons. The rose of the previous card has been altogether disintegrated."

**English Paraphrase**:
**Enfeebled Intellect** – Corresponds to Geburah (Severity/Strength) in Air. Geburah usually brings sharp force, but here **Venus in Aquarius** weakens the martial quality: softness, sentiment or people‑pleasing undermine clear, firm thinking. The inverted pentagram formed by the sword hilts shows matter or lower desire dominating spirit. The blades are crooked, broken, drooping; the rose of Truce is destroyed. This is **Defeat**: the mind surrenders from weakness, avoidance, or betrayal, not from noble renunciation.

**Core**: **Mental Collapse** – Humiliation, hollow victory, self‑sabotage, surrender to fear or manipulation.

**Chinese Explanation**:
**宝剑五（失败）**对应空气元素中的**Geburah（严厉/破坏之力）**，但这里的失败并非来自“力量过强”，而是来自**力量的衰弱与软化**。统治星为**金星入宝瓶座**：理性本应冷静决断，却被**情绪、讨好、避免冲突的倾向**所削弱。剑柄形成倒五芒星，象征**物质/欲望压过精神**；剑刃扭曲、折断、下垂，上一张牌中的玫瑰已完全瓦解。这张牌代表的失败，是一种**心智被消磨、软弱妥协、甚至背叛自我的失败**，而非光荣的退让。

**In Readings**: Defeat, humiliation, treachery, self‑betrayal, toxic compromise, giving up too soon, hollow success for the wrong side.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Five of Swords shows Geburah disrupting but Venus in Aquarius causes weakness not excess. Inverted pentagram shows matter dominating. Swords crooked and broken. Rose destroyed.
- **中文**: Crowley的宝剑五展示Geburah破坏但金星入宝瓶导致软弱而非过度。倒五芒星显示物质主导。剑弯曲断裂。玫瑰被毁。

**Narrative Snippets**:
- `[ns_thoth_swords_013]` `[trigger: five_swords_defeat]` `[factor_trigger: thoth_swords_five]` `[role: 主干]` Five of Swords = Lord of Defeat—Geburah disrupts but weakness causes disaster, not excess. → Core
- `[ns_thoth_swords_014]` `[trigger: venus_aquarius_weak]` `[factor_trigger: thoth_swords_five AND planet_venus_aquarius]` `[role: 条件分支]` Venus in Aquarius—intellect enfeebled by sentiment; defeat due to pacifism/treachery. → Astrological
- `[ns_thoth_swords_015]` `[trigger: inverted_pentagram_swords]` `[factor_trigger: thoth_swords_five AND symbol_inverted_pentagram]` `[role: 条件分支]` Sword hilts form inverted pentagram—matter over spirit; blades crooked/broken; rose destroyed. → Visual"""
    normalized_text_zh: str = """"""
    subject: str = "Five of Swords: Defeat (宝剑五：失败)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_swords_five_001', 'tarot_mental_collapse', 'rel_swords_five_002', 'tarot_self_sabotage', 'l1_anchor', 'confidence', 'evi_swords_five_001', 'evi_swords_five_002', 'tarot_inverted_pentagram', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_swords_five_001', 'tarot_swords_five', 'astro_venus_aquarius']
    
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
        l1_anchor="bot_v1.0.0_five_of_swords__defeat__宝剑五_失败_001_L1",
    )
    version: str = "1.0.0"
