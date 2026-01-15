"""
Auto-generated semantic module for astrological_houses
Generated at: 2025-12-05T13:30:20.333746
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
    semantic_id="ah_v1.0.0_house_6___crisis_transformatio_001",
    book_id="astrological_houses",
    engine_id="astro"
)
class House6CrisisTransformatio(SemanticEntry):
    """
    #### Source Text

"The sixth house represents everything dealing with personal crises and the way to...
    """
    
    original_text: str = """#### Source Text

"The sixth house represents everything dealing with personal crises and the way to meet them. It shows how an individual can grow and become transformed. The essential question is: How can I best orient myself to an oncoming crisis? The real problem is what the individual does with his experience of failure and the results of defeat. A man's true inner worth is often revealed when he has to face experiences of inadequacy, lack, or defeat. This is where discipleship comes in—being subjected to the contagion of example from an individual who not only has the skill but is able to use it in times of crisis. The message of the sixth house is: Be ye transformed!"

#### English Paraphrase (Primary Language)

Rudhyar reframes the sixth house from mundane concerns of work and health to the profound arena of crisis, transformation, and discipleship. Following fifth house self-expression, every individual encounters the gap between aspiration and achievement—the realization of inadequacy. The sixth house determines whether this recognition leads to growth or defeat. True transformation requires not merely technical skill but the capacity to use that skill under pressure. This is why discipleship matters: the master transmits not just knowledge but the power to transform one's approach to life itself. Illness, employment, service—all traditional sixth house matters—are contexts for this transformative process. The cadent nature indicates transition: either integration into a higher level of relationship (seventh house) or regression into shadow.

#### Complete Chinese Interpretation (Secondary Language)

鲁迪亚将第六宫从日常的工作和健康问题重新框架为危机、转化和门徒关系的深刻领域。在第五宫自我表达之后，每个人都会遇到抱负与成就之间的差距——对不足的认识。

**第六宫的核心主题**：
- **危机作为机遇**：不足的认识可以导致成长或失败
- **门徒关系**：真正的转化需要大师传递的力量，不仅是技术知识
- **服务作为治愈**：真正的服务是自我中心的唯一治愈方法
- **疾病作为信息**：身体症状往往反映心理/精神需要修正

第六宫决定了这种认识是否导致成长或失败。第六宫的信息是："要被转化！"作为果宫/衰宫，它表示过渡：要么整合到更高层次的关系（第七宫），要么退化到阴影中。

#### Core Points

- **Crisis as opportunity**: Inadequacy recognition can lead to growth or defeat
- **Discipleship**: Master transmits power to transform, not just techniques
- **Service as cure**: True service heals egocentricity
- **Illness as message**: Physical symptoms reflect psychological/spiritual needs
- **Transformation imperative**: "Be ye transformed!" is the sixth house message
- **Cadent transition**: Bridge between personal (H1-6) and relational (H7-12) hemispheres

#### Narrative Snippets

- `[ns_houses_h6_001]` `[trigger: house_6]` `[factor_trigger: house_6 AND inadequacy]` `[role: 主干]` The sixth house represents everything dealing with personal crises and shows how an individual can grow and become transformed. → House 6 Source
- `[ns_houses_h6_002]` `[trigger: house_6 AND astro_service]` `[factor_trigger: house_6 AND astro_house_1]` `[role: 条件分支]` True discipleship means being subjected to the contagion of example from a master who can use skill in times of crisis—receiving power to transform one's approach to life. → House 6 Source"""
    normalized_text_zh: str = """"""
    subject: str = "House 6 - Crisis/Transformation (Cadent)"
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
        l1_anchor="ah_v1.0.0_house_6___crisis_transformatio_001_L1",
    )
    version: str = "1.0.0"
