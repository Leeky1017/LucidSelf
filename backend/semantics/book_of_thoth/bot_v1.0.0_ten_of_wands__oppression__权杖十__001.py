"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.088902
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
    semantic_id="bot_v1.0.0_ten_of_wands__oppression__权杖十__001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class TenOfWandsOppression权杖十(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Malkuth in Fire | Kingdom in Fire | Detached force |
| Saturn in Sagittarius | Heavy + swift clash | Greatest antipathy |
| Blind Force | Spiritless will | Self-devouring |
| Prison Bars | Crossed wands | Oppression symbol |

**Title**: Lord of Oppression (压迫之主)
**Qabalistic**: Malkuth in Fire (火中之王国)
**Astrological**: Saturn in Sagittarius (土星入射手座)

**Source Text**:
> "The number Ten refers to Malkuth... detached from its spiritual sources. It is become a blind Force; so, the most violent form of that particular energy... The card also refers to the influence of Saturn in Sagittarius. Here is the greatest antipathy. ... The whole picture suggests Oppression and repression. It is a stupid and obstinate cruelty from which there is no escape. It is a Will which has not understood anything beyond its dull purpose..."

**English Paraphrase**:
**Overwhelming Burden** - Corresponds to Malkuth (Kingdom/Earth) in Fire. Here, the force is **detached from spiritual sources** and becomes a blind, violent energy. Ruled by **Saturn in Sagittarius**, creating the greatest antipathy (heavy/slow Saturn vs swift/light Sagittarius). The wands are crossed bars, looking like claws/prison bars. It represents **Oppression**, repression, and stupid, obstinate cruelty. It is Will that has become a burden to itself, "lust of result" leading to self-devouring.

**Core**: **Crushing Weight** - Force detached from source, burden, cruelty, overextension, will turning against itself, failure through success.

**Chinese Explanation**:
**权杖十（压迫）**对应火元素中的Malkuth（王国/物质）。在此，力量**与灵性源头脱节**，变成盲目、暴力的能量。对应**土星在射手座**，形成巨大的反差（土星的重/慢 vs 射手座的轻/快）。权杖变成了交叉的栅栏或爪子。这代表**压迫**、压抑以及愚蠢顽固的残酷。这是未能理解其目的之外任何事物的意志，因"对结果的贪欲"（lust of result）而自我吞噬。

**In Readings**: Oppression, heavy burden, overextension, cruelty, blocked energy, working too hard without spirit, blind force.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Ten of Wands shows force completely detached from spiritual source. Saturn in Sagittarius creates greatest antipathy. Wands become prison bars/claws. "Lust of result" causes self-devouring. Malkuth in Fire is blind, violent energy.
- **中文**: Crowley的权杖十展示力量完全与灵性源头脱节。土星入射手创造最大对立。权杖变成监狱栏杆/爪子。"对结果的贪欲"导致自我吞噬。火中之Malkuth是盲目暴力能量。

**Narrative Snippets**:
- `[ns_thoth_wands_028]` `[trigger: ten_wands_oppression]` `[factor_trigger: thoth_wands_ten]` `[role: 主干]` Ten of Wands = Lord of Oppression—Malkuth in Fire; force detached from spiritual sources; blind. → Core
- `[ns_thoth_wands_029]` `[trigger: saturn_sagittarius]` `[factor_trigger: thoth_wands_ten AND planet_saturn_sagittarius]` `[role: 条件分支]` Saturn in Sagittarius—greatest antipathy; heavy restriction on swift fire; stupid cruelty. → Astrological
- `[ns_thoth_wands_030]` `[trigger: bars_claws]` `[factor_trigger: thoth_wands_ten AND symbol_bars]` `[role: 条件分支]` Wands as bars/claws—prison symbol; "lust of result" causes self-devouring; obstinate will. → Visual"""
    normalized_text_zh: str = """"""
    subject: str = "Ten of Wands: Oppression (权杖十：压迫)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_wands_ten_001', 'tarot_blind_force', 'rel_wands_ten_002', 'tarot_self_devouring', 'l1_anchor', 'confidence', 'evi_wands_ten_001', 'evi_wands_ten_002', 'tarot_lust_result', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_wands_ten_001', 'tarot_wands_ten', 'astro_saturn_sagittarius']
    
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
        l1_anchor="bot_v1.0.0_ten_of_wands__oppression__权杖十__001_L1",
    )
    version: str = "1.0.0"
