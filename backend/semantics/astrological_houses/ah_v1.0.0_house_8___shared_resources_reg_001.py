"""
Auto-generated semantic module for astrological_houses
Generated at: 2025-12-05T13:30:20.333769
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
    semantic_id="ah_v1.0.0_house_8___shared_resources_reg_001",
    book_id="astrological_houses",
    engine_id="astro"
)
class House8SharedResourcesReg(SemanticEntry):
    """
    #### Source Text

"The eighth house refers to the possessions of the relationship—what is available ...
    """
    
    original_text: str = """#### Source Text

"The eighth house refers to the possessions of the relationship—what is available to the relationship to become an operative factor in society. The eighth house deals with business proper because any type of business implies some kind of contract involving at least two persons. Three basic factors are implied: trust, management, and responsibility. The eighth house is a very important house, hard to interpret. It is in terms of eighth house experiences that a person has to make perhaps the deepest and most vital choices. These choices affect not only the individual but society as a whole. The Existentialist philosophers are right in saying that every man is responsible for the whole of mankind."

#### English Paraphrase (Primary Language)

The eighth house represents what relationship produces and how those products are managed. Unlike second house personal possessions, eighth house resources belong to the partnership itself—the "plus value" generated through cooperation. This includes business dealings, sexual exchange, and the fruits of any sustained relationship. Rudhyar identifies three essential factors: trust (the foundation of all partnership), management (wise use of shared resources), and responsibility (accountability for how resources affect the larger whole). This is where the individual confronts death and regeneration—the death of ego-illusions and potential rebirth through surrender to relationship's transformative power. Ritual and business alike operate in this house, both structured processes for generating and channeling collective power.

#### Complete Chinese Interpretation (Secondary Language)

第八宫代表关系产生什么以及如何管理这些产物。与第二宫的个人所有物不同，第八宫资源属于伙伴关系本身——通过合作产生的"附加价值"。

**第八宫的三大要素**：
1. **信任**：所有伙伴关系的基础
2. **管理**：共享资源的明智使用
3. **责任**：对资源如何影响更大整体负责

这里个体面对死亡和再生——自我幻觉的死亡和通过臣服于关系转化力量的潜在重生。仪式和商业都在这个宫位运作，两者都是产生和引导集体力量的结构化过程。这是一个非常重要的宫位，难以解读——在第八宫经验中，个人必须做出也许是最深刻和最关键的选择。

#### Core Points

- **Relationship's possessions**: Plus value generated through cooperation
- **Trust-management-responsibility**: Three pillars of eighth house
- **Business as relationship**: All commerce implies partnership and contract
- **Death and regeneration**: Ego-death and potential rebirth through surrender
- **Ritual significance**: Structured processes for collective power
- **Universal responsibility**: Individual choices affect all of mankind

#### Narrative Snippets

- `[ns_houses_h8_001]` `[trigger: house_8]` `[factor_trigger: house_8 AND transformation]` `[role: 主干]` The eighth house refers to the possessions of the relationship—what is available to become an operative factor in society, based on trust, management, and responsibility. → House 8 Source
- `[ns_houses_h8_002]` `[trigger: house_8 AND astro_responsibility]` `[factor_trigger: house_8 AND society]` `[role: 总结]` In eighth house experiences a person makes the deepest choices affecting not only the individual but society—every man is responsible for the whole of mankind. → House 8 Source"""
    normalized_text_zh: str = """"""
    subject: str = "House 8 - Shared Resources/Regeneration (Succedent)"
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
        book_id="astrological_houses",
        chapter="",
        l1_anchor="ah_v1.0.0_house_8___shared_resources_reg_001_L1",
    )
    version: str = "1.0.0"
