"""
Auto-generated semantic module for astrological_houses
Generated at: 2025-12-05T13:30:20.333847
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
    semantic_id="ah_v1.0.0_aries_libra_axis___individual__001",
    book_id="astrological_houses",
    engine_id="astro"
)
class AriesLibraAxisIndividual(SemanticEntry):
    """
    #### Source Text

"Aries represents straightforward movement toward a concrete, personalized state o...
    """
    
    original_text: str = """#### Source Text

"Aries represents straightforward movement toward a concrete, personalized state of existence. If Aries is rising, the child's latent consciousness is stamped with impulsive and impetuous eagerness to assert uniqueness of destiny. The Aries Ascendant may tend to romanticize selfhood—full of yearnings for anything that mirrors the essential self. Libra represents movement toward development of social-cultural consciousness, the eagerness for 'I' to interact with 'Thou.' Because Aries stimulates typical adolescent yearning for self-expression and assertion of uniqueness, it requires as a balancing force a sense of social values."

#### English Paraphrase (Primary Language)

The Aries/Libra axis represents the polarity between individual assertion and social integration. Aries rising creates impulsive eagerness to assert unique destiny—the spirit of adolescence, compensating for insecurity with apparent aggression. This person needs Libra partnerships providing social values, group ideals, or noble causes as contexts for self-assertion. When Libra rises, the individual becomes a field for collective urges and group ideals—discovering identity through social role and partnership. The Libra Ascendant person needs individualistic, self-actualizing partners to help find themselves through relationship. Both signs are equinoctial—Day-force and Night-force in balance but dynamic tension.

#### Complete Chinese Interpretation (Secondary Language)

白羊/天秤轴代表个人主张与社会整合之间的极性。

**白羊上升**：
- 冲动地渴望主张独特命运
- 青春期精神——以明显的攻击性补偿内心不安全感
- 需要天秤式伙伴关系：社会价值、群体理想、崇高事业作为自我主张的背景

**天秤上升**：
- 成为集体冲动和群体理想的运作场
- 通过社会角色和伙伴关系发现身份
- 需要个人主义、自我实现型伴侣帮助通过关系找到自我

两个星座都是分点星座——日力和夜力平衡但处于动态张力中。这一轴线的核心主题是：个体如何在社会背景中定义自我？

#### Core Points

- **Equinoctial signs**: Day/Night forces in balance but dynamic tension
- **Aries rising**: Impulsive self-assertion, adolescent spirit, compensatory aggression
- **Libra balancing**: Social values provide context for individual assertion
- **Libra rising**: Identity through social role, group participation
- **Aries partner needed**: Individualistic catalyst for Libra's group orientation
- **Core tension**: Individual uniqueness vs collective standards"""
    normalized_text_zh: str = """"""
    subject: str = "Aries/Libra Axis - Individual Initiative vs Social Values"
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
        l1_anchor="ah_v1.0.0_aries_libra_axis___individual__001_L1",
    )
    version: str = "1.0.0"
