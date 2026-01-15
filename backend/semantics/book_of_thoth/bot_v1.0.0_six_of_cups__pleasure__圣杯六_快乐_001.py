"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.027234
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
    semantic_id="bot_v1.0.0_six_of_cups__pleasure__圣杯六_快乐_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class SixOfCupsPleasure圣杯六快乐(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Tiphareth in Water | Beauty in Water | Harmonious flow |
| Sun in Scorpio | Life through death | Fertile putrefaction |
| Sexual Will | Sacramental desire | IX° O.T.O. secret |
| Dancing Lotuses | Flowing movement | Natural ease |

**Title**: Lord of Pleasure (快乐之主)
**Qabalistic**: Tiphareth in Water (水中之美)
**Astrological**: Sun in Scorpio (太阳入天蝎座)

**Source Text**:
> "This card shows the influence of the number Six, Tiphareth... fortified by that of the Sun... Sun on Water. ... putrefaction... is the basis of all fertility... Lotus stems are grouped in an elaborate dancing movement. ... Pleasure... implies well-being, harmony of natural forces without effort or strain... fulfilment of the sexual Will... One of the master-keys to the Gate of Initiation. ... Secret of the Ninth Degree of the O.T.O."

**English Paraphrase**:
**Sexual/Spiritual Bliss** - Corresponds to Tiphareth (Beauty) in Water, fortified by the **Sun in Scorpio**. Here, putrefaction (Scorpio) becomes the basis of fertility and life. The lotuses dance, and water gushes into the cups. "Pleasure" here is the **highest sense**: well-being, harmony of natural forces, and the **fulfillment of the sexual Will**. It hints at deep esoteric secrets (IX° O.T.O.) involving the sacramental use of pleasure/putrefaction (death/rebirth).

**Core**: **Deep Harmony** - Emotional well-being, nostalgia (in RW, but here more sexual/mystical), fertility, joy, harmony of forces.

**Chinese Explanation**:
**圣杯六（快乐）**对应水元素中的Tiphareth（美）。受**太阳在天蝎座**的影响。在此，天蝎的腐败特质成为所有生育和生命的基础。莲花茎呈现复杂的舞蹈动作，水涌入杯中。这里的"快乐"是指最高意义上的：福祉、自然力量的轻松和谐，以及**性意志的实现**。它暗示了深层的秘传知识（O.T.O.第九级），涉及将快乐/腐败作为圣礼的秘密。

**In Readings**: Pleasure, harmony, well-being, sexual fulfillment, fertility, ease, satisfaction, emotional renewal.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Six of Cups shows putrefaction as fertility basis. Sun in Scorpio brings life through death. Sexual Will fulfillment hints at IX° O.T.O. secrets. Dancing lotuses show natural harmony.
- **中文**: Crowley的圣杯六展示腐败作为生育基础。太阳入天蝎通过死亡带来生命。性意志实现暗示IX° O.T.O.秘密。跳舞莲花显示自然和谐。

**Narrative Snippets**:
- `[ns_thoth_cups_016]` `[trigger: six_cups_pleasure]` `[factor_trigger: thoth_cups_six]` `[role: 主干]` Six of Cups = Lord of Pleasure—Tiphareth in Water; Sun in Scorpio putrefaction becomes fertility basis. → Core
- `[ns_thoth_cups_017]` `[trigger: sexual_will]` `[factor_trigger: thoth_cups_six AND principle_sexual]` `[role: 条件分支]` Fulfilment of sexual Will—master-key to Initiation Gate; IX° O.T.O. secrets hinted. → Esoteric
- `[ns_thoth_cups_018]` `[trigger: dancing_lotuses]` `[factor_trigger: thoth_cups_six AND symbol_lotus]` `[role: 条件分支]` Lotus stems in elaborate dancing movement—harmony without effort or strain. → Visual"""
    normalized_text_zh: str = """"""
    subject: str = "Six of Cups: Pleasure (圣杯六：快乐)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_cups_six_001', 'tarot_emotional_harmony', 'rel_cups_six_002', 'tarot_fertile_joy', 'l1_anchor', 'confidence', 'evi_cups_six_001', 'evi_cups_six_002', 'tarot_fertile_joy', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_cups_six_001', 'tarot_cups_six', 'astro_sun_scorpio']
    
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
        l1_anchor="bot_v1.0.0_six_of_cups__pleasure__圣杯六_快乐_001_L1",
    )
    version: str = "1.0.0"
