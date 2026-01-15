"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.063747
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
    semantic_id="bot_v1.0.0_knight_of_disks__钱币骑士_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class KnightOfDisks钱币骑士(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Fire of Earth | Internal heat | Slow growth |
| Flail | Threshing tool | Agricultural labor |
| Shire Horse | Draft animal | Stable strength |
| Smouldering Fire | Gradual warmth | Patient process |

**Title**: Lord of the Wide and Fertile Land (广袤沃土之主)
**Elemental**: The Fiery part of Earth (土中之火)
**Zodiac**: 21° Leo to 20° Virgo (狮子座21度至处女座20度)

**Source Text**:
> "The Knight of Disks represents the fiery part of Earth, and refers in particular to the phenomena of mountains, earthquakes, and gravitation; but it also represents the activity of Earth regarded as the producer of Life... He is armed with a flail. The disk which he bears... represents nutrition... a shire horse, solidly planted on all four feet... He rides through the fertile land... Those whom he symbolizes tend to be dull, heavy and preoccupied with material things. They are laborious and patient, but would have little intellectual grasp... Their success... is due to instinct, to imitation of Nature. They lack initiative; their fire is the smouldering fire of the process of growth."

**English Paraphrase**:
**Steady Cultivation** – **Fire of Earth**: mountains, earthquakes, gravity, Earth as life-producer. Wields flail (agriculture), rides shire horse solidly planted, through fertile fields. Archetype of **laborer/farmer**: patient, hard-working, instinctive, close to nature, but dull, limited vision. Fire is slow smoldering growth, not dramatic flame. Negatively: slavish, unable to think beyond immediate material concerns, resentful but passive.

**Core**: **Practical Labor** – Agriculture, physical work, patient effort, limited vision and initiative.

**Chinese Explanation**:
**钱币骑士**代表**土中之火**：山脉、地震、重力，大地作为生命生产者。手持连枷，骑役马（四脚稳立），穿过肥沃耕地。**劳动者/农夫**原型：耐心、勤劳、本能、亲近自然，但迟钝、视野有限。火是缓慢闷烧的生长，非戏剧性火焰。负向：奴性、无法超越眼前物质思考、怨恨但消极。

**In Readings**: Hard worker, farmer, laborer, patient effort, practical but unimaginative; or dull, stubborn, slavish person.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Knight of Disks is Fire of Earth - mountains, earthquakes, gravitation. Wields flail, rides shire horse through fertile fields. Laborious, patient, instinctive. Fire is smoldering growth, not dramatic flame.
- **中文**: Crowley的钱币骑士是土中之火—山脉、地震、引力。挥舞连枷，骑役马穿越肥沃田野。勤劳、耐心、本能。火是闷烧生长，而非戏剧性火焰。

**Narrative Snippets**:
- `[ns_thoth_disks_031]` `[trigger: knight_disks_thoth]` `[factor_trigger: thoth_disks_knight]` `[role: 主干]` Knight of Disks = Fire of Earth—mountains, earthquakes, gravitation; Earth as life-producer. → Core
- `[ns_thoth_disks_032]` `[trigger: flail_shire_horse]` `[factor_trigger: thoth_disks_knight AND symbol_flail]` `[role: 条件分支]` Flail weapon, shire horse solidly planted—laborious, patient, instinctive agricultural worker. → Visual
- `[ns_thoth_disks_033]` `[trigger: smouldering_growth]` `[factor_trigger: thoth_disks_knight AND state_character]` `[role: 条件分支]` Fire is smouldering growth, not dramatic flame; success due to imitation of Nature. → Character"""
    normalized_text_zh: str = """"""
    subject: str = "Knight of Disks (钱币骑士)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_disks_knight_001', 'tarot_patient_labor', 'rel_disks_knight_002', 'tarot_agricultural_work', 'l1_anchor', 'confidence', 'evi_disks_knight_001', 'evi_disks_knight_002', 'tarot_patient_labor', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_disks_knight_001', 'tarot_disks_knight', 'astro_virgo']
    
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
        l1_anchor="bot_v1.0.0_knight_of_disks__钱币骑士_001_L1",
    )
    version: str = "1.0.0"
