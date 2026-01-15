"""
Auto-generated semantic module for astrological_houses
Generated at: 2025-12-05T13:30:20.333879
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
    semantic_id="ah_v1.0.0_cancer_capricorn_axis___person_001",
    book_id="astrological_houses",
    engine_id="astro"
)
class CancerCapricornAxisPerson(SemanticEntry):
    """
    #### Source Text

"In Cancer the Day-force is at the acme of its power. Cancer represents the stabil...
    """
    
    original_text: str = """#### Source Text

"In Cancer the Day-force is at the acme of its power. Cancer represents the stabilizing power of a home—life energies being focused. The Cancer type strives for concrete realization of Unity at the root of all experience, which may lead to mystical realizations. Capricorn deals with large-scale political or managerial institutions of a complex national state. The Cancer Ascendant person trusts more in personal power and the dynamic power of love; the Capricorn Ascendant resorts to large impersonal or superpersonal concepts or techniques of organization. Carl Jung had a Capricorn Ascendant—his depth psychology stresses the power of archetypes of the collective unconscious."

#### English Paraphrase (Primary Language)

The Cancer/Capricorn axis represents the polarity between personal integration and social/institutional achievement—both solstitial signs where one force is maximally dominant. Cancer rising creates concern with definite, personally focused goals—issues are sharply definable and involve individual personalities. This person trusts personal power and the dynamic power of love. Capricorn rising leads to discovering identity through activities integrating distant factors or basic antagonisms, using logical systems or legal instrumentalities. Jung (Capricorn Ascendant) stressed archetypes over personal feelings; Adler (Cancer Ascendant) emphasized personal will-to-power compensating for inferiority. The axis represents the fourth house (private integration) / tenth house (public achievement) polarity at its most essential level.

#### Complete Chinese Interpretation (Secondary Language)

巨蟹/摩羯轴代表个人整合与社会/制度成就之间的极性——两者都是夏至/冬至星座，一种力量最大程度地主导。

**巨蟹上升**：
- 关注明确的、以个人为焦点的目标
- 问题尖锐可定义，涉及个人人格
- 信任个人力量和爱的动态力量
- 阿德勒（巨蟹上升）强调补偿自卑的个人意志力

**摩羯上升**：
- 通过整合远距因素或基本对立的活动发现身份
- 使用逻辑系统或法律工具
- 诉诸大型非个人或超个人概念/组织技术
- 荣格（摩羯上升）强调集体无意识原型的力量超过个人情感

**轴线的核心张力**：
- 个人vs制度
- 爱的力量vs组织的力量
- 家庭整合vs社会成就
- 母性统一vs父性结构

#### Core Points

- **Solstitial signs**: Maximum dominance of one force
- **Cancer rising**: Personal focus, trust in love's power, sharp definition
- **Capricorn balancing**: Large-scale integration, institutional frameworks
- **Capricorn rising**: Identity through superpersonal organization
- **Cancer partner needed**: Personal concretization, emotional grounding
- **Jung vs Adler**: Archetype-oriented vs will-to-power oriented psychology"""
    normalized_text_zh: str = """"""
    subject: str = "Cancer/Capricorn Axis - Personal Integration vs Social Achievement"
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
        l1_anchor="ah_v1.0.0_cancer_capricorn_axis___person_001_L1",
    )
    version: str = "1.0.0"
