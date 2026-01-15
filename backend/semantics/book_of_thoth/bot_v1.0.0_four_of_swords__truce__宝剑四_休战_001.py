"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.076440
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
    semantic_id="bot_v1.0.0_four_of_swords__truce__宝剑四_休战_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class FourOfSwordsTruce宝剑四休战(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Chesed in Air | Mercy in Air | Ordered refuge |
| Jupiter in Libra | Expansion + balance | Legal harmony |
| 49-Petaled Rose | Social harmony | Compromise sheath |
| Dogma | Fixed belief | Refuge from chaos |

**Title**: Lord of Rest from Strife (纷争暂歇之主)
**Qabalistic**: Chesed in Air (气中之仁慈)
**Astrological**: Jupiter in Libra (木星入天秤座)

**Source Text**:
> "The number Four, Chesed, is here manifested in the realm of the Intellect. Chesed refers to Jupiter who rules in Libra in this decanate. The sum of these symbols is therefore without opposition; hence the card proclaims the idea of authority in the intellectual world. It is the establishment of dogma, and law concerning it. It represents a refuge from mental chaos, chosen in an arbitrary manner. It argues for convention. ... The hilts of the four Swords are at the corner of a St. Andrew's cross... points are sheathed in a rather large rose of forty-nine petals representing social harmony. Here, too, is compromise." 

**English Paraphrase**:
**Conventional Truce** – Corresponds to Chesed (Mercy/Order) in Air, ruled by **Jupiter in Libra**. This is the establishment of intellectual authority and dogma: laws, doctrines, and accepted truths that provide a **refuge from mental chaos**, but are chosen somewhat arbitrarily. Four swords form a St. Andrew's cross; their points are sheathed in a forty‑nine‑petaled rose of social harmony, symbolizing compromise and convention. This is a **Truce**: rest from struggle by accepting a framework, yet at the cost of true inquiry.

**Core**: **Rest via Structure** – Pause, stabilization, rules, treaties, but also rigidity and avoidance.

**Chinese Explanation**:
**宝剑四（休战）**对应空气元素中的**Chesed（仁慈/秩序）**，并受到**木星在天秤座**的加持。它在心智领域中代表**权威与秩序的建立**：通过教条、法律、共识性观念来缓解混乱。四把剑的剑柄位于**圣安德鲁十字**的四个端点，剑尖全部**收纳在一朵四十九瓣的大玫瑰**中，象征社会和谐与妥协。这种休战带来暂时的安定与安全感，但往往是以**接受现成结构、避免内在思考冲突**为代价。它暗示一种“靠规则维持和平”的模式：有用，却不一定是真正的解决。

**In Readings**: Rest, retreat, recovery, agreed cease‑fire, therapy, taking a break from conflict; or, mental stagnation, dogma, hiding behind rules.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Four of Swords shows Chesed establishing authority/dogma. Jupiter in Libra brings expansive justice. 49-petaled rose symbolizes social harmony. Truce is refuge chosen arbitrarily.
- **中文**: Crowley的宝剑四展示Chesed建立权威/教条。木星入天秤带来扩张性正义。四十九瓣玫瑰象征社会和谐。休战是任意选择的避难所。

**Narrative Snippets**:
- `[ns_thoth_swords_010]` `[trigger: four_swords_truce]` `[factor_trigger: thoth_swords_four]` `[role: 主干]` Four of Swords = Lord of Rest from Strife—Chesed establishes dogma/law as refuge from chaos. → Core
- `[ns_thoth_swords_011]` `[trigger: jupiter_libra_law]` `[factor_trigger: thoth_swords_four AND planet_jupiter_libra]` `[role: 条件分支]` Jupiter in Libra—expansive legal harmony; authority in intellectual world. → Astrological
- `[ns_thoth_swords_012]` `[trigger: forty_nine_rose]` `[factor_trigger: thoth_swords_four AND symbol_rose_49]` `[role: 条件分支]` 49-petaled rose sheathes sword points—social harmony through compromise; convention. → Visual"""
    normalized_text_zh: str = """"""
    subject: str = "Four of Swords: Truce (宝剑四：休战)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_swords_four_001', 'tarot_mental_refuge', 'rel_swords_four_002', 'tarot_static_peace', 'l1_anchor', 'confidence', 'evi_swords_four_001', 'evi_swords_four_002', 'tarot_convention', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_swords_four_001', 'tarot_swords_four', 'astro_jupiter_libra']
    
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
        l1_anchor="bot_v1.0.0_four_of_swords__truce__宝剑四_休战_001_L1",
    )
    version: str = "1.0.0"
