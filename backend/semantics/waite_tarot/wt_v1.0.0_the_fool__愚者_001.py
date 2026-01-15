"""
Auto-generated semantic module for waite_tarot
Generated at: 2025-12-05T13:30:19.952831
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
    semantic_id="wt_v1.0.0_the_fool__愚者_001",
    book_id="waite_tarot",
    engine_id="tarot"
)
class TheFool愚者(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Spirit Seeking Experience | First emanation | Journey outward |
| Prince of Other World | Travels through this | Divine origin |
| Most Speaking Symbol | Maximum eloquence | Reversing confusions |
| Sub-conscious Memories | Wallet's dim signs | Hidden knowledge |

**Number**: 0 (unnumbered) | **Element**: Air | **Path**: Kether to Chokmah

**Source Text** (condensed):
> "Light step, earth's trammels have little power... young man at brink of precipice with no terror, as if angels uphold him. Prince of other world on travels through this one. Sun behind knows whence/whither/return. He is spirit in search of experience. Reverses all confusions. Journey outward, first emanation, graces and passivity of spirit. Wallet with dim signs = sub-conscious memories. Most speaking of all symbols."

**Core**: **Spirit Seeking Experience** – First emanation, journey outward, passivity/grace, prince of other world, angels uphold, sub-conscious memories, most eloquent symbol.

**Chinese**: **愚者（寻求经验的灵性）**——第一放射，向外旅程，灵性的恩典与被动性，另世界王子在此世旅行，天使托住，潜意识记忆（钱包暗淡符号），最会说话的符号。

**Bilingual Terms**: Spirit in Search of Experience (寻求经验的灵性) | First Emanation (第一放射) | Prince of Other World (另世界王子) | Most Speaking Symbol (最会说话的符号)

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Waite: "Spirit in search of experience." "Prince of other world on travels through this one." "Sun behind knows whence/whither/return." "Wallet with dim signs = sub-conscious memories." "Most speaking of all symbols."
- **中文**: 韦特："寻求经验的灵性"。"另世界王子在此世旅行"。"身后太阳知道从何/往何/回归"。"钱包暗淡符号=潜意识记忆"。"所有符号中最会说话的"。

**Narrative Snippets**:
- `[ns_waite_082]` `[trigger: fool_spirit]` `[factor_trigger: tarot_fool AND spirit_experience]` `[role: 主干]` He is the spirit in search of experience—first emanation, journey outward, graces and passivity of spirit. → Core
- `[ns_waite_083]` `[trigger: fool_prince]` `[factor_trigger: tarot_fool AND other_world]` `[role: 条件分支]` Prince of the other world on travels through this one—sun behind knows whence, whither, and return. → Origin
- `[ns_waite_084]` `[trigger: fool_symbol]` `[factor_trigger: tarot_fool AND eloquent_symbol]` `[role: 条件分支]` The most speaking of all symbols—reverses all confusions, wallet with dim signs holds sub-conscious memories. → Eloquence"""
    normalized_text_zh: str = """"""
    subject: str = "The Fool (愚者)"
    factor_refs: list = ['tarot_fool', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'tarot_fool', 'tarot_semantic', 'new_candidate', 'tarot_semantic', 'new_candidate', 'tarot_semantic', 'new_candidate', 'tarot_semantic', 'new_candidate', 'tarot_semantic', 'new_candidate', 'tarot_semantic', 'source_ref', 'rel_waite_064', 'tarot_fool', 'completing', 'rel_waite_065', 'tarot_fool', 'descending', 'rel_waite_066', 'tarot_fool', 'protecting', 'evi_waite_043', 'tarot_fool', 'rule_waite_fool_spirit', 'evi_waite_044', 'tarot_fool', 'rule_waite_fool_prince', 'concept_spirit_seeking', 'planet_uranus', 'individuation_start', 'concept_protected_innocence', 'unconscious_trust']
    
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
        book_id="waite_tarot",
        chapter="",
        l1_anchor="wt_v1.0.0_the_fool__愚者_001_L1",
    )
    version: str = "1.0.0"
