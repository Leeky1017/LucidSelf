"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.063772
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
    semantic_id="bot_v1.0.0_queen_of_disks__钱币皇后_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class QueenOfDisks钱币皇后(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Water of Earth | Moist fertility | Nurturing mother |
| River through Desert | Life-bringing | Oasis creation |
| Goat on Sphere | Capricorn emblem | Great Work fertility |
| Coin Armor | Protective scales | Material ambition |

**Title**: Queen of the Thrones of Earth (土之宝座的皇后)
**Elemental**: The Watery part of Earth (土中之水)
**Zodiac**: 21° Sagittarius to 20° Capricorn (射手座21度至摩羯座20度)

**Source Text**:
> "The Queen of Disks represents the watery part of Earth, the function of that element as Mother... throned upon the life of vegetation. She contemplates the background, where a calm river winds through a sandy desert to bring to it fertility. Oases are beginning to shew themselves... Before her stands a goat upon a sphere... Her armour is composed of small scales or coins... She thus represents the ambition of matter to take part in the great work of Creation... These people are quiet, hard-working, practical, sensible, domesticated, often (in a reticent and unassuming fashion) lustful and even debauched."

**English Paraphrase**:
**The Fertile Mother** – **Water of Earth**: Earth's function as **Mother** and nurturer. Throned on vegetation, gazes at river through desert bringing fertility; oases bloom. Goat on sphere (fertility as Great Work). Coin-armor; cube-scepter with 3D hexagram; sphere-disk of loops. **Matter's ambition to participate in Creation**. Quiet, practical, hard-working, sensible, domesticated, with deep (often hidden) sensuality. Negatively: dull, servile, mechanically living.

**Core**: **Nurturing Materiality** – Motherhood, fertility, practical care, quiet strength, risk of drudgery.

**Chinese Explanation**:
**钱币皇后**代表**土中之水**：土作为**母亲**的功能。端坐植被上，凝视河流穿沙漠带来肥力；绿洲显现。山羊在球上（生育即大工作）。钱币铠甲；立方体权杖（3D六芒星）；交错环形球盘。**物质渴望参与创造之工作**。安静、务实、勤劳、明智、顾家，带有深沉（隐藏的）感官欲望。负向：迟钝、奴性、机械活着。

**In Readings**: Nurturing woman, motherhood, practical care, fertility, domesticity, sensual/earthy; or servile drudge.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Queen of Disks is Water of Earth - Earth as Mother. Throned on vegetation, gazes at river through desert. Goat on sphere. Matter's ambition to participate in Creation. Quiet, practical, hard-working with hidden sensuality.
- **中文**: Crowley的钱币皇后是土中之水—大地作为母亲。端坐植被上，凝视河流穿过沙漠。球上山羊。物质渴望参与创造。安静、务实、勤劳，带有隐藏的感官性。

**Narrative Snippets**:
- `[ns_thoth_disks_034]` `[trigger: queen_disks_thoth]` `[factor_trigger: thoth_disks_queen]` `[role: 主干]` Queen of Disks = Water of Earth—function as Mother; matter's ambition to participate in Creation. → Core
- `[ns_thoth_disks_035]` `[trigger: river_desert_goat]` `[factor_trigger: thoth_disks_queen AND symbol_river]` `[role: 条件分支]` River through desert brings fertility; goat on sphere; throned on vegetation. → Visual
- `[ns_thoth_disks_036]` `[trigger: quiet_sensual]` `[factor_trigger: thoth_disks_queen AND state_character]` `[role: 条件分支]` Quiet, hard-working, practical, sensible; often in reticent fashion lustful. → Character"""
    normalized_text_zh: str = """"""
    subject: str = "Queen of Disks (钱币皇后)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_thoth_disks_queen', 'thoth_disks_queen', 'expressing', 'evi_thoth_disks_queen', 'thoth_disks_queen', 'rule_thoth_disks_queen', 'concept_thoth_disks_queen', 'decan_zodiac', 'archetype']
    
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
        l1_anchor="bot_v1.0.0_queen_of_disks__钱币皇后_001_L1",
    )
    version: str = "1.0.0"
