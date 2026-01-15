"""
Auto-generated semantic module for astrological_houses
Generated at: 2025-12-05T13:30:20.333684
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
    semantic_id="ah_v1.0.0_house_1___self_identity__ascen_001",
    book_id="astrological_houses",
    engine_id="astro"
)
class House1SelfIdentityAscen(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Ascendant | Birth point ...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Ascendant | Birth point | Incarnation moment |
| Self-Image | Persona/mask | What others see first |
| Angular House | Action-oriented | Maximum power |
| Aries Analog | Cardinal fire | Initiative |

#### Source Text

"The first house, marked by the Ascendant or Rising sign, represents the point of birth and the dawn of consciousness. It governs self-image, personality expression, and how others perceive you upon first encounter. As an angular house analogous to cardinal fire (Aries), it embodies personal initiative, self-assertion, and the beginning of the life journey."

#### English Paraphrase (Primary Language)

The first house, whose cusp is the Ascendant, symbolizes the moment of incarnation when spirit enters material form at birth. It rules the mask or persona we present to the world—our immediate self-expression before deeper layers are revealed. This house governs physical appearance, first impressions, and the spontaneous personality we project. As an angular house (action-oriented), it parallels Aries' cardinal fire quality, manifesting as personal initiative, courageous self-assertion, and the pioneering impulse to begin new cycles. The first house marks where individual consciousness emerges into visible existence.

#### Complete Chinese Interpretation (Secondary Language)

第一宫(上升点)代表**出生和意识黎明**——灵魂进入物质形式的时刻，自我意识首次觉醒。它掌管**自我形象**、**人格表达**、他人对你的**初见印象**。上升星座是你戴的"面具"或"窗口"，通过它你体验世界并被世界体验。第一宫显示你如何主动开始事物、你的身体类型、你的自发性表达。它不是你的本质(那是太阳)，而是你向外投射的即时存在方式——你如何"降临"到任何情境。第一宫行星着色整个人格表达。上升守护星成为命盘整体守护星，影响所有其他领域。

#### Core Points

- **Ascendant/Rising**: Point of birth, incarnation moment
- **Self-image**: Personality mask, first impressions
- **Angular house**: Action-oriented, cardinal quality
- **Aries analog**: Cardinal fire, personal initiative
- **Life journey beginning**: Emergence into existence

#### Narrative Snippets

- `[ns_rudhyar_h1_001]` `[trigger: house_1]` `[factor_trigger: House_Philosophy_12H_1 AND self]` `[role: 主干]` The first house, marked by the Ascendant, represents the point of birth and the dawn of consciousness. It governs self-image, personality expression, and how others perceive you upon first encounter. → The Astrological Houses H1
- `[ns_rudhyar_h1_002]` `[trigger: house_1 AND astro_ascendant]` `[factor_trigger: physical_body AND nervous_system]` `[role: 主干依赖]` The Ascendant symbolizes the moment of incarnation when spirit enters material form at birth. It rules the mask or persona we present to the world. → The Astrological Houses H1
- `[ns_rudhyar_h1_003]` `[trigger: house_1 AND astro_angular]` `[factor_trigger: natal_planets AND ic]` `[role: 总结]` As an angular house paralleling Aries' cardinal fire quality, the first house manifests as personal initiative, courageous self-assertion, and the pioneering impulse to begin new cycles. → The Astrological Houses H1"""
    normalized_text_zh: str = """"""
    subject: str = "House 1 - Self/Identity (Ascendant)"
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
        l1_anchor="ah_v1.0.0_house_1___self_identity__ascen_001_L1",
    )
    version: str = "1.0.0"
