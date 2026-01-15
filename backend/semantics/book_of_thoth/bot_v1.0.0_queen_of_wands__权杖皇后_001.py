"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.088927
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
    semantic_id="bot_v1.0.0_queen_of_wands__权杖皇后_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class QueenOfWands权杖皇后(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Water of Fire | Fluid fire aspect | Adaptability |
| Leopard | Wild attendant | Grace + savagery |
| Pinecone Wand | Bacchic symbol | Ecstasy mysteries |
| Calm Authority | Radiant command | Magnetic presence |

**Title**: The Queen of the Thrones of Flame (火焰宝座的皇后)
**Elemental**: The Watery part of Fire (火中之水)
**Zodiac**: 21° Pisces to 20° Aries

**Source Text**:
> "The Queen of Wands represents the watery part of Fire, its fluidity and colour. ... Her crown is topped with the winged globe and rayed with flame. ... She bears a wand... topped with a cone suggestive of the mysteries of Bacchus. She is attended by a couchant leopard... Adaptability, persistent energy, calm authority... She is kindly and generous, but impatient of opposition."

**English Paraphrase**:
**Magnetic Authority** - Represents the **Watery part of Fire** (fluidity, color, reflection). Rules from late Pisces to Aries. She sits on a throne of flame, bearing a wand with a Bacchic cone (pinecone) and attended by a leopard. Qualities: **Adaptability, persistent energy, calm authority**, attractiveness. She has immense capacity for friendship and love but on her own terms. If ill-dignified: snobbery, vanity, brooding, and sudden savagery ("breaks her jaw" when she misses a bite).

**Core**: **Radiant Confidence** - Attraction, adaptability, social power, command through presence, steady fire.

**Chinese Explanation**:
**权杖皇后**代表**火中之水**（火的流动性和色彩）。掌管双鱼座21度到白羊座20度。她坐在火焰宝座上，手持顶端有松果（巴克斯奥秘）的权杖，身旁有一只卧着的豹子。品质：**适应性、持久的能量、冷静的权威**、吸引力。她有巨大的友谊和爱的能力，但必须由她主动。如果能量不佳：势利、虚荣、阴郁，以及突然的野蛮（"咬空时会咬碎自己的下巴"）。

**In Readings**: Independence, charm, adaptability, social success, authoritative woman, generosity, vanity.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Queen of Wands represents Water of Fire (fluidity, color). Leopard symbolizes wild grace and latent savagery. Pinecone wand hints at Bacchic ecstasy. Kindly but impatient of opposition.
- **中文**: Crowley的权杖皇后代表火中之水（流动性、色彩）。豹子象征野性优雅和潜伏野蛮。松果权杖暗示酒神式狂喜。亲切但对对立不耐烦。

**Narrative Snippets**:
- `[ns_thoth_wands_034]` `[trigger: queen_wands_thoth]` `[factor_trigger: thoth_wands_queen]` `[role: 主干]` Queen of Wands = Water of Fire—fluidity and color; adaptability, persistent energy, calm authority. → Core
- `[ns_thoth_wands_035]` `[trigger: leopard_pinecone]` `[factor_trigger: thoth_wands_queen AND symbol_leopard]` `[role: 条件分支]` Couchant leopard attendant; pinecone (Bacchic) wand—wild grace with latent savagery. → Visual
- `[ns_thoth_wands_036]` `[trigger: impatient_opposition]` `[factor_trigger: thoth_wands_queen AND state_character]` `[role: 条件分支]` Kindly and generous, but impatient of opposition—breaks her jaw when she misses a bite. → Character"""
    normalized_text_zh: str = """"""
    subject: str = "Queen of Wands (权杖皇后)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_thoth_wands_queen', 'thoth_wands_queen', 'expressing', 'evi_thoth_wands_queen', 'thoth_wands_queen', 'rule_thoth_wands_queen', 'concept_thoth_wands_queen', 'decan_zodiac', 'archetype']
    
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
        l1_anchor="bot_v1.0.0_queen_of_wands__权杖皇后_001_L1",
    )
    version: str = "1.0.0"
