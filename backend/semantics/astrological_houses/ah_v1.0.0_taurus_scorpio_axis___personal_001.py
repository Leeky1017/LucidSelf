"""
Auto-generated semantic module for astrological_houses
Generated at: 2025-12-05T13:30:20.333858
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
    semantic_id="ah_v1.0.0_taurus_scorpio_axis___personal_001",
    book_id="astrological_houses",
    engine_id="astro"
)
class TaurusScorpioAxisPersonal(SemanticEntry):
    """
    #### Source Text

"The Taurus type discovers true nature through productivity. There may be thorough...
    """
    
    original_text: str = """#### Source Text

"The Taurus type discovers true nature through productivity. There may be thorough identification with both the process of production and the person whose needs this process satisfies. In Scorpio, sexual activity has a personalized character—meeting human needs, answering individual yearnings, possessive in a personal sense and subject to perversions but also transmutation. The Scorpio Ascendant person will often seek to fulfill his role in society by drawing power from persons close to him. These people enjoy the use of social power and identification with the need of their people."

#### English Paraphrase (Primary Language)

The Taurus/Scorpio axis represents the polarity between personal production and transformative interpenetration. Taurus rising discovers identity through productivity—thorough identification with the creative process and its products, leading to pride in accomplishments but potential self-centeredness. Scorpio Descendant partners provide broader social vision and conscious, controlled approach to productivity. When Scorpio rises, the individual fulfills social role by drawing vital forces from intimate partners—numerous political leaders (Disraeli, Gandhi, Lenin, Stalin, Mussolini) had Scorpio rising. They enjoy social power identification with collective needs, but require Taurus partners for concrete results and grounded productivity.

#### Complete Chinese Interpretation (Secondary Language)

金牛/天蝎轴代表个人生产与转化性融合之间的极性。

**金牛上升**：
- 通过生产力发现身份
- 与创造过程及其产物彻底认同
- 导致对成就的自豪，但可能有自我中心倾向
- 需要天蝎式伴侣提供更广阔的社会视野

**天蝎上升**：
- 通过从亲密伴侣汲取生命力来履行社会角色
- 众多政治领袖（迪斯雷利、甘地、列宁、斯大林、墨索里尼）都是天蝎上升
- 享受与集体需求认同的社会权力
- 需要金牛式伴侣提供具体成果和扎实的生产力

**性的双重含义**：
- 金牛：生物性、本能性、生殖功能
- 天蝎：人格化、心理性、可能变态也可能升华

#### Core Points

- **Fixed signs**: Stabilization and concentration of energy
- **Taurus rising**: Identity through productivity, pride in accomplishments
- **Scorpio balancing**: Broader social vision, conscious control
- **Scorpio rising**: Drawing power from intimates, political leadership
- **Taurus partner needed**: Concrete results, grounded productivity
- **Sexual polarity**: Biological instinct (Taurus) vs psychological transformation (Scorpio)"""
    normalized_text_zh: str = """"""
    subject: str = "Taurus/Scorpio Axis - Personal Production vs Shared Transformation"
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
        l1_anchor="ah_v1.0.0_taurus_scorpio_axis___personal_001_L1",
    )
    version: str = "1.0.0"
