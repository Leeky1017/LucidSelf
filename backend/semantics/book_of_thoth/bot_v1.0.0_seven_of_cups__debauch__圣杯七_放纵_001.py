"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.027257
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
    semantic_id="bot_v1.0.0_seven_of_cups__debauch__圣杯七_放纵_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class SevenOfCupsDebauch圣杯七放纵(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Netzach in Water | Victory in Water | Imbalanced emotion |
| Venus in Scorpio | Beauty in decay | External splendor/internal rot |
| Tiger-lilies | Poisonous flowers | Corrupted pleasure |
| Green Slime | Toxic secretion | Emotional poison |

**Title**: Lord of Debauch (放纵之主)
**Qabalistic**: Netzach in Water (水中之胜利/情感)
**Astrological**: Venus in Scorpio (金星入天蝎座)

**Source Text**:
> "This card refers to the Seven, Netzach... lack of balance... Venus in Scorpio... 'external splendour and internal corruption'. The Lotuses have become poisonous, looking like tiger-lilies; and, instead of water, green slime issues from them... Venus redoubles the influence of the number Seven. ... 'evil and averse' image of the Six... fatal ease with which a Sacrament may be profaned and prostituted."

**English Paraphrase**:
**Corrupted Emotion** - Corresponds to Netzach (Victory/Emotion) in Water. Weakness arises from imbalance. Ruled by **Venus in Scorpio**: "external splendour and internal corruption". The lotuses become poisonous **tiger-lilies**, oozing **green slime** instead of water. It represents the profanation of the sacrament (seen in the Six). It is **Debauch**, illusion, addiction, and the danger of losing contact with the Highest (Kether). "Holiest mysteries of Nature become the obscene... secrets of a guilty conscience."

**Core**: **Illusion and Addiction** - Corruption, delusion, poisoning of emotion, drug/alcohol abuse, fantasy, profanation, false pleasure.

**Chinese Explanation**:
**圣杯七（放纵）**对应水元素中的Netzach（胜利/情感）。缺乏平衡导致软弱。对应**金星在天蝎座**，象征"外表辉煌，内在腐败"。莲花变成了有毒的**卷丹**（tiger-lilies），流出的是**绿色粘液**而非清水。这代表了对（六号牌中）圣礼的亵渎。这是**放纵**、幻觉、成瘾，以及与最高处（Kether）失去联系的危险。神圣的自然奥秘变成了有罪良心的淫秽秘密。

**In Readings**: Debauchery, addiction, illusion, deception, poisoning, corruption, hallucinations, false choices.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Seven of Cups shows Venus in Scorpio as "external splendour, internal corruption". Lotuses become poisonous tiger-lilies. Green slime replaces water. Sacrament profaned into debauch.
- **中文**: Crowley的圣杯七展示金星入天蝎为"外表辉煌，内在腐败"。莲花变成有毒卷丹。绿色粘液取代水。圣礼亵渎为放纵。

**Narrative Snippets**:
- `[ns_thoth_cups_019]` `[trigger: seven_cups_debauch]` `[factor_trigger: thoth_cups_seven]` `[role: 主干]` Seven of Cups = Lord of Debauch—Venus in Scorpio: external splendour, internal corruption. → Core
- `[ns_thoth_cups_020]` `[trigger: tiger_lilies]` `[factor_trigger: thoth_cups_seven AND symbol_tiger_lily]` `[role: 条件分支]` Lotuses become poisonous tiger-lilies—green slime instead of water; sacrament profaned. → Degradation
- `[ns_thoth_cups_021]` `[trigger: guilty_conscience]` `[factor_trigger: thoth_cups_seven AND state_profanation]` `[role: 条件分支]` Holiest mysteries become obscene secrets of guilty conscience—losing Kether contact. → Warning"""
    normalized_text_zh: str = """"""
    subject: str = "Seven of Cups: Debauch (圣杯七：放纵)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_cups_seven_001', 'tarot_corrupted_pleasure', 'rel_cups_seven_002', 'tarot_profaned_sacrament', 'l1_anchor', 'confidence', 'evi_cups_seven_001', 'evi_cups_seven_002', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_cups_seven_001', 'tarot_cups_seven', 'astro_venus_scorpio']
    
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
        l1_anchor="bot_v1.0.0_seven_of_cups__debauch__圣杯七_放纵_001_L1",
    )
    version: str = "1.0.0"
