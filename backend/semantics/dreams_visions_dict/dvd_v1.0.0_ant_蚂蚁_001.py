"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.439686
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
    semantic_id="dvd_v1.0.0_ant_蚂蚁_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Ant蚂蚁(SemanticEntry):
    """
    ### Source Text

> **General Meaning**: A hard worker.

**Positive** (Proverbs 6:6): "Go to the ant,...
    """
    
    original_text: str = """### Source Text

> **General Meaning**: A hard worker.

**Positive** (Proverbs 6:6): "Go to the ant, you sluggard; consider her ways, and be wise." The ant is hard-working, positive, building up. Speaks of working hard and planning ahead.

**Negative**: In personal experience, we have often seen ants and such insects as spirits of infirmity. Flies are often spoken negatively of in Scripture—connotation of contamination and uncleanliness.

**See also**: Demons, Insect, Flies

### Key Terms

| Term | Definition | Significance |
|------|------------|--------------|
| Ant | Hard worker | Diligence, planning |
| Sluggard | Lazy person | What ant teaches against |
| Spirit of infirmity | Demonic weakness | Negative interpretation |

### English Paraphrase

Ant = hard worker. **Positive**: Proverbs 6:6 uses ant as example of diligence and wisdom—working hard, planning ahead, building up. **Negative**: In spiritual vision, ants (like other insects) can represent spirits of infirmity. While spirits have no actual shape, these symbols guide what Holy Spirit is communicating. Insects generally connote contamination and uncleanliness in Scripture.

### Chinese Interpretation（完整对等诠释）

蚂蚁 = 勤劳者。**正面**：箴言6:6用蚂蚁作为勤奋和智慧的榜样——努力工作、提前计划、积极建造。**负面**：在属灵异象中，蚂蚁（如其他昆虫）可以代表疾病之灵。虽然灵没有实际形状，但这些符号引导圣灵在传达什么。在圣经中，昆虫通常意味着污染和不洁净。

### Narrative Snippets

- `[ns_dav_a033]` `[trigger: 梦蚂蚁]` `[factor_trigger: dream_symbol_ant]` `[role: 主干]` Ant = hard worker (Proverbs 6:6)—diligence, planning ahead, building up. → Dreams Dictionary #Ant
- `[ns_dav_a034]` `[trigger: 蚂蚁负面]` `[factor_trigger: dream_symbol_ant AND dream_negative]` `[role: 条件分支]` In vision, insects (including ants) can represent spirits of infirmity—contamination. → Dreams Dictionary #Ant"""
    normalized_text_zh: str = """"""
    subject: str = "Ant 蚂蚁"
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
        book_id="dreams_visions_dict",
        chapter="",
        l1_anchor="dvd_v1.0.0_ant_蚂蚁_001_L1",
    )
    version: str = "1.0.0"
