"""
Auto-generated semantic module for astrological_houses
Generated at: 2025-12-05T13:30:20.333696
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
    semantic_id="ah_v1.0.0_house_2___possessions_resource_001",
    book_id="astrological_houses",
    engine_id="astro"
)
class House2PossessionsResource(SemanticEntry):
    """
    #### Source Text

"The second house is associated with possessions and money—symbol of the capacity ...
    """
    
    original_text: str = """#### Source Text

"The second house is associated with possessions and money—symbol of the capacity to own whatever a person needs or desires. The concept of possession is complex; it has several levels of meaning. What is really at stake is the problem of ownership, what is meant whenever an individual uses the words 'mine' and 'my own.' The body is the first and fundamental possession of the self. It provides the means for the gradual actualization of the potentialities inherent in the field of selfhood. The proper use of possessions leads to the revelation, exteriorization, and fulfillment of one's individuality. Possessions should be used. Unused capacities or wealth are impediments to human growth. The individual should impress the rhythm of his individuality upon what he owns; he should dedicate what he has to what he is, for it is being which alone gives meaning to having."

#### English Paraphrase (Primary Language)

Rudhyar transforms the conventional understanding of the second house from mere financial matters to a profound philosophy of ownership and resource management at multiple levels. The most fundamental possession is the physical body itself—the vehicle through which all birth potentials can be actualized. Beyond the body, possessions extend to inherited faculties, psychological capacities, and eventually to material wealth and social resources. The critical insight is that ownership without purposeful use is spiritually empty. Possessions derive meaning only through their dedication to the expression of individual destiny. The succedent nature of this house emphasizes utilization: how one manages and deploys available resources determines whether birth potential becomes actual achievement. At the highest level, the individual realizes that even the self is a possession to be surrendered to humanity's evolution.

#### Complete Chinese Interpretation (Secondary Language)

鲁迪亚将第二宫从单纯的财务事项转化为关于所有权和资源管理的深刻哲学。最根本的所有物是身体本身——通过它，所有出生潜能才能被实现。身体之外，所有物延伸到遗传能力、心理才能，最终到物质财富和社会资源。

**所有权的三层次**：
1. **生物层**：身体、本能、遗传特质——这是"我的"的最原始意义
2. **社会层**：金钱、财产、获取能力——满足需求和欲望的手段
3. **精神层**：将所有物奉献给人类进化——最终的超越

关键洞见是：没有目的性使用的所有权在精神上是空虚的。所有物只有通过奉献给个人命运的表达才能获得意义。续宫的性质强调利用：如何管理和部署可用资源决定了出生潜能能否转化为实际成就。在最高层次，个体意识到即使自我也是应当献给人类进化的所有物。

#### Core Points

- **Body as primary possession**: Physical vehicle for actualizing birth potential
- **Multi-level ownership**: Biological → Social → Spiritual progression
- **Use imperative**: Unused resources impede growth; management is key
- **Individuation through resources**: Impress individual rhythm upon possessions
- **Being over having**: Ownership meaningful only through purposeful dedication
- **Succedent function**: Bridge between identity (H1) and environment (H3)

#### Narrative Snippets

- `[ns_houses_h2_001]` `[trigger: house_2]` `[factor_trigger: house_2 AND first_house]` `[role: 主干]` The body is the first and fundamental possession of the self—it provides the means for actualizing potentialities inherent in selfhood. → House 2 Source
- `[ns_houses_h2_002]` `[trigger: house_2 AND astro_ownership]` `[factor_trigger: house_2 AND ego]` `[role: 主干依赖]` The proper use of possessions leads to revelation and fulfillment of individuality; one should dedicate what he has to what he is. → House 2 Source
- `[ns_houses_h2_003]` `[trigger: house_2 AND astro_spiritual]` `[factor_trigger: house_2 AND discipleship]` `[role: 总结]` At the highest level, the individual realizes he himself is the ultimate possession to surrender on the altar of human evolution. → House 2 Source"""
    normalized_text_zh: str = """"""
    subject: str = "House 2 - Possessions/Resources (Succedent)"
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
        l1_anchor="ah_v1.0.0_house_2___possessions_resource_001_L1",
    )
    version: str = "1.0.0"
