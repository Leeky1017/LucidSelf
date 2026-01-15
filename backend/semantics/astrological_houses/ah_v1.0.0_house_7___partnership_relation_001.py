"""
Auto-generated semantic module for astrological_houses
Generated at: 2025-12-05T13:30:20.333759
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
    semantic_id="ah_v1.0.0_house_7___partnership_relation_001",
    book_id="astrological_houses",
    engine_id="astro"
)
class House7PartnershipRelation(SemanticEntry):
    """
    #### Source Text

"The seventh house deals with experiences resulting from activity based no longer ...
    """
    
    original_text: str = """#### Source Text

"The seventh house deals with experiences resulting from activity based no longer primarily upon the individual self but upon sustained modes of relationship to other selves. The cooperators should feel that their operation in common serves a purpose within a larger unit of existence. Every person learns what he is by functioning together with other human beings. The quality of a person's relationship to others at the functional level is the foundation upon which he will achieve or fail to achieve whatever has been the inherent purpose of his existence. The keynote of seventh house experiences is participation. The seventh house is potentially the most dynamic of all houses. It is here that the person can be most basically transformed."

#### English Paraphrase (Primary Language)

The seventh house marks the fundamental shift from self-focused to relationship-focused existence. This is not merely about marriage or partnership but about discovering oneself through functional cooperation with others. Rudhyar emphasizes that relationship should serve purpose beyond the participants—contributing to family, society, or humanity. The Descendant principle of relatedness complements the Ascendant principle of selfhood. In the seventh house, the individual discovers their function through participation in the greater whole. This house is potentially the most dynamic because relationship is the creative force that can most fundamentally transform the person. The quality of relationship established here determines success or failure in achieving one's inherent life purpose.

#### Complete Chinese Interpretation (Secondary Language)

第七宫标志着从以自我为中心到以关系为中心的存在的根本转变。这不仅仅是关于婚姻或伙伴关系，而是关于通过与他人的功能性合作发现自己。

**第七宫的核心原则**：
- **参与作为关键词**：个体通过与他人的功能性合作学习自己是谁
- **目的性关系**：合作应该服务于超越参与者的目的
- **最具活力的宫位**：关系是能够最根本地转化人的创造性力量
- **下降点原则**：与上升点的自我原则形成互补的关系原则

这里建立的关系质量决定了实现内在生命目的的成功或失败。鲁迪亚区分了两种关系方法：仅为个人满足的"双人自我主义"，或奉献给超个人目的的共同参与。

#### Core Points

- **Participation keynote**: Self-discovery through functional cooperation
- **Purpose beyond partners**: Relationship should serve larger whole
- **Most dynamic house**: Transformation potential greatest through relationship
- **Descendant principle**: Relatedness complements Ascendant selfhood
- **Function discovery**: Individual learns who they are through partnership
- **Quality determines destiny**: Relationship quality determines life purpose achievement

#### Narrative Snippets

- `[ns_houses_h7_001]` `[trigger: house_7]` `[factor_trigger: house_7 AND other_selves]` `[role: 主干]` The seventh house deals with experiences based upon sustained modes of relationship—the cooperators should feel their operation serves a purpose within a larger unit. → House 7 Source
- `[ns_houses_h7_002]` `[trigger: house_7 AND astro_transformation]` `[factor_trigger: house_7 AND partnership]` `[role: 主干依赖]` The seventh house is potentially the most dynamic of all houses—it is here that the person can be most basically transformed through relationship. → House 7 Source"""
    normalized_text_zh: str = """"""
    subject: str = "House 7 - Partnership/Relationship (Angular - DSC)"
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
        l1_anchor="ah_v1.0.0_house_7___partnership_relation_001_L1",
    )
    version: str = "1.0.0"
