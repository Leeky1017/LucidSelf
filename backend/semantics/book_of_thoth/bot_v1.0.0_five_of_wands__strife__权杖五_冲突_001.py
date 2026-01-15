"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.088831
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
    semantic_id="bot_v1.0.0_five_of_wands__strife__权杖五_冲突_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class FiveOfWandsStrife权杖五冲突(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Geburah in Fire | Severity in Fire | Volcanic force |
| Saturn in Leo | Restriction + fire | Embittered energy |
| Adept Wands | Hierarchical symbols | Authority control |
| Volcanic Energy | Unlimited scope | Tameless force |

**Title**: Lord of Strife (冲突之主)
**Qabalistic**: Geburah in Fire (火中之严厉)
**Astrological**: Saturn in Leo (土星入狮子座)

**Source Text**:
> "This card is referred to Geburah of the suit of Fire. Geburah itself being fiery, it is a purely active force. It is ruled also by Saturn and Leo. ... Saturn tends to weigh it down and to embitter it. There is no limit to the scope of this volcanic energy. ... The symbol represents the wand of the Chief Adept... two wands of the Second... and two wands of the Third... This card would be thoroughly disastrous [without hierarchy]."

**English Paraphrase**:
**Volcanic Disturbance** - Corresponds to Geburah (Severity/Strength) in Fire, a purely active, potentially violent force. Ruled by **Saturn in Leo**: Saturn (restriction/weight) embitters the fiery nature of Leo, causing **volcanic energy** and strife. The symbol shows the wands of the Chief, Major, and Minor Adepts (Phoenix and Lotus wands), implying that this energy is **controlled by hierarchy**. Without this structure, the conflict would be disastrous. It represents struggle, tension, and the "tameless irrational energy" mitigated only by superior authority.

**Core**: **Restricted Energy** - Struggle, conflict, frustration, heavy energy (Saturn) trying to explode (Leo/Fire), necessary friction.

**Chinese Explanation**:
**权杖五（冲突）**对应火元素中的Geburah（严厉/力量）。由于Geburah本身属火，这是一种纯粹的主动力量。对应**土星在狮子座**：土星的沉重与限制使狮子座的火能量变得苦涩，导致**火山般的爆发力**。这代表没有限制的能量冲突。图像展示了最高、第二和第三级Adepts（大能者）的权杖（凤凰与莲花），暗示这种冲突通过**层级权威**来管理；若无此结构，将是灾难性的。它象征斗争、紧张以及被压抑的激烈能量。

**In Readings**: Conflict, struggle, hassle, frustration, volcanic energy, quarrel, competition, obstacles to be overcome.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Five of Wands shows Saturn embittering Leo's fire, creating volcanic strife. Geburah's severity adds fierce intensity. Adept wand hierarchy prevents total disaster. Energy is "tameless" but controlled by authority.
- **中文**: Crowley的权杖五展示土星使狮子之火变得苦涩，创造火山般冲突。Geburah的严厉增添猛烈强度。大能者权杖层级阻止全面灾难。能量"不可驯服"但受权威控制。

**Narrative Snippets**:
- `[ns_thoth_wands_013]` `[trigger: five_wands_strife]` `[factor_trigger: thoth_wands_five]` `[role: 主干]` Five of Wands = Lord of Strife—Geburah in Fire; purely active volcanic force; no limit to scope. → Core
- `[ns_thoth_wands_014]` `[trigger: saturn_leo_bitter]` `[factor_trigger: thoth_wands_five AND planet_saturn_leo]` `[role: 条件分支]` Saturn in Leo—weighs down and embitters fire; tameless irrational energy. → Astrological
- `[ns_thoth_wands_015]` `[trigger: adept_wands]` `[factor_trigger: thoth_wands_five AND symbol_adept_wands]` `[role: 条件分支]` Chief/Major/Minor Adept wands (Phoenix & Lotus)—hierarchy controls conflict; without it: disaster. → Visual"""
    normalized_text_zh: str = """"""
    subject: str = "Five of Wands: Strife (权杖五：冲突)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_wands_five_001', 'tarot_volcanic_energy', 'rel_wands_five_002', 'tarot_controlled_conflict', 'l1_anchor', 'confidence', 'evi_wands_five_001', 'evi_wands_five_002', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_wands_five_001', 'tarot_wands_five', 'astro_saturn_leo']
    
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
        l1_anchor="bot_v1.0.0_five_of_wands__strife__权杖五_冲突_001_L1",
    )
    version: str = "1.0.0"
