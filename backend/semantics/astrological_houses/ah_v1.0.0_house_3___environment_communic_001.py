"""
Auto-generated semantic module for astrological_houses
Generated at: 2025-12-05T13:30:20.333709
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
    semantic_id="ah_v1.0.0_house_3___environment_communic_001",
    book_id="astrological_houses",
    engine_id="astro"
)
class House3EnvironmentCommunic(SemanticEntry):
    """
    #### Source Text

"The third house refers to the earliest environment of the newborn and the growing...
    """
    
    original_text: str = """#### Source Text

"The third house refers to the earliest environment of the newborn and the growing child's relationship to it. The relationship of the child to his environment is basic in the formation of character and responses to life. Any organism must first conquer its 'living space.' It is on this challenge that the development of the nervous system is based. Intelligence means the capacity to come to terms with any environment—first physical, then psychic—and therefore to adjust to its demands and eventually to transform it. The third house refers to the development of intelligence and eventually of analytical intellect and empirical science. Third house 'understanding' is characteristically empirical; it is behaviorist, pragmatic, technique-oriented. It simply wants to know the 'how to' of doing things for practical reasons."

#### English Paraphrase (Primary Language)

The third house represents the individual's encounter with immediate environment and the development of intelligence as a survival mechanism. Every child must discover the boundaries of their "living space"—how far they can extend before meeting resistance. This process develops the nervous system and forms the foundation of intelligence. Rudhyar distinguishes third house intelligence from ninth house understanding: the third house is empirical, practical, and technique-oriented—concerned with "how to" rather than "why." It is the mind of the specialist, not the generalist. As a cadent house, it represents the transition phase where knowledge accumulated must be integrated (fourth house) or risk becoming psychologically toxic through unassimilated data overload.

#### Complete Chinese Interpretation (Secondary Language)

第三宫代表个体与直接环境的遭遇，以及作为生存机制的智力发展。每个孩子必须发现其"生活空间"的边界——能延伸多远才会遇到阻力。这一过程发展神经系统，形成智力的基础。

**第三宫vs第九宫心智**：
- **第三宫**：经验性、实用性、技术导向——关注"如何做"
- **第九宫**：理论性、概括性、哲学导向——关注"为什么"

第三宫是专家的心智，不是通才的心智。作为果宫/衰宫，它代表过渡阶段：积累的知识必须被整合（第四宫），否则会因未消化的数据超载而变得有害。鲁迪亚警告：我们当前社会崇拜知识，特别是技术和各种"操作指南"类信息，但如果缺乏整合，智识可能膨胀，充满无法吸收的无意义数据。

#### Core Points

- **Environment as teacher**: Early surroundings shape character and responses
- **Intelligence defined**: Capacity to come to terms with environment
- **Empirical focus**: Practical, technique-oriented, "how to" knowledge
- **Specialist mind**: Contrasts with ninth house generalist/philosopher
- **Cadent warning**: Unintegrated knowledge becomes toxic
- **Nervous system**: Physical correlate of environmental adaptation

#### Narrative Snippets

- `[ns_houses_h3_001]` `[trigger: house_3]` `[factor_trigger: house_3 AND past]` `[role: 主干]` Intelligence is the capacity to come to terms with any environment—first physical, then psychic—and to adjust to its demands and eventually transform it. → House 3 Source
- `[ns_houses_h3_002]` `[trigger: house_3 AND astro_mind]` `[factor_trigger: house_3 AND point_of_self]` `[role: 条件分支]` Third house understanding is empirical, behaviorist, pragmatic—the mind of the specialist wanting to know 'how to' for practical reasons. → House 3 Source"""
    normalized_text_zh: str = """"""
    subject: str = "House 3 - Environment/Communication (Cadent)"
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
        l1_anchor="ah_v1.0.0_house_3___environment_communic_001_L1",
    )
    version: str = "1.0.0"
