"""
Auto-generated semantic module for astrological_houses
Generated at: 2025-12-05T13:30:20.333722
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
    semantic_id="ah_v1.0.0_house_4___foundation_integrati_001",
    book_id="astrological_houses",
    engine_id="astro"
)
class House4FoundationIntegrati(SemanticEntry):
    """
    #### Source Text

"The fourth house is one of the most significant, yet least truly understood secti...
    """
    
    original_text: str = """#### Source Text

"The fourth house is one of the most significant, yet least truly understood sections of the chart. It takes on global significance—not only representing productive soil and foundation for the home, but above all the center of the globe. In the fourth house the person can and should reach the experience of center—the center of his own total personality as well as the center of global humanity. Without such an experience of center, an individual can never demonstrate his human stature. The fourth house refers to the basic psychic function which Jung called feeling. It deals with integration and stabilization. Personality is more than a biopsychic organism; it can be considered an engine able to release power for work."

#### English Paraphrase (Primary Language)

Rudhyar revolutionizes understanding of the fourth house by moving beyond "home and family" to the profound concept of centeredness. Just as the Earth has a center that provides ultimate stability regardless of surface changes, so the fourth house represents the individual's capacity to find their psychological center. This is where integration occurs—where scattered experiences, knowledge, and resources coalesce into a stable personality capable of generating power. The IC (Imum Coeli) represents not merely ancestry but the deepest point of sustainment. Jung's "feeling function" operates here—the holistic response of the entire organism to life situations. At the deepest level, this house connects to the collective unconscious and the archetypes that form the foundation of human culture.

#### Complete Chinese Interpretation (Secondary Language)

鲁迪亚通过超越"家庭和家"的概念，将第四宫理解革命化为深刻的"中心性"概念。正如地球有一个中心，无论表面如何变化都提供最终稳定性，第四宫代表个体找到其心理中心的能力。

**中心性的三层含义**：
1. **土地层**：生产性土壤、家的基础、祖先传统
2. **心理层**：人格整合、稳定化、荣格的"情感功能"
3. **精神层**：全球人类中心、人类兄弟情谊的具体现实

没有中心体验，个体永远无法展现其完整的人类身份。IC（天底）代表的不仅是血统，而是最深层的支撑点。这里是整合发生的地方——分散的经验、知识和资源凝聚成能够产生力量的稳定人格。在最深层次，这个宫位连接到集体无意识和构成人类文化基础的原型。

#### Core Points

- **Center as key concept**: Psychological/spiritual centeredness, not just physical home
- **Integration function**: Where scattered elements coalesce into stable personality
- **Jung's feeling function**: Holistic organismic response to life
- **Power generation**: Integrated personality becomes "engine" for work
- **Collective connection**: Links to archetypes and collective unconscious
- **Angular significance**: One of four most powerful points in chart

#### Narrative Snippets

- `[ns_houses_h4_001]` `[trigger: house_4]` `[factor_trigger: house_4 AND mc]` `[role: 主干]` In the fourth house the person should reach the experience of center—the center of his own total personality as well as the center of global humanity. → House 4 Source
- `[ns_houses_h4_002]` `[trigger: house_4 AND astro_integration]` `[factor_trigger: house_4 AND personality]` `[role: 主干依赖]` Personality is more than a biopsychic organism; it can be considered an engine able to release power for work—this power is generated through fourth house integration. → House 4 Source
- `[ns_houses_h4_003]` `[trigger: house_4 AND astro_center]` `[factor_trigger: House_Philosophy_12H_4]` `[role: 总结]` Without the experience of center, an individual can never demonstrate his human stature—the fourth house is where integration occurs. → House 4 Source"""
    normalized_text_zh: str = """"""
    subject: str = "House 4 - Foundation/Integration (Angular - IC)"
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
        l1_anchor="ah_v1.0.0_house_4___foundation_integrati_001_L1",
    )
    version: str = "1.0.0"
