"""
Auto-generated semantic module for astrological_houses
Generated at: 2025-12-05T13:30:20.333735
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
    semantic_id="ah_v1.0.0_house_5___self_expression_crea_001",
    book_id="astrological_houses",
    engine_id="astro"
)
class House5SelfExpressionCrea(SemanticEntry):
    """
    #### Source Text

"In the fifth house what has been integrated in the fourth house produces potentia...
    """
    
    original_text: str = """#### Source Text

"In the fifth house what has been integrated in the fourth house produces potential energy. Power becomes available for use. Creativity is referred to the fifth house because to create is to impress upon one's community characteristics of one's own personality. It is to make one's own mark upon society. Giving birth to a child is the biological way; producing art, founding institutions, leading nations—all exteriorize the power of the creator. The fifth house has been associated with gambling, love affairs, and childbearing. The test of the fifth house involves the ability to act out one's innermost nature in terms of purity of motive. To be pure is to be exclusively what one is as a unique individual in terms of one's destiny."

#### English Paraphrase (Primary Language)

The fifth house represents the release and expression of the power accumulated through fourth house integration. This is where personality becomes creative force—impressing itself upon the world. Rudhyar distinguishes biological creativity (procreation) from cultural creativity (art, institutions, leadership), but both share the essential quality of exteriorizing inner power. The fifth house is associated with pleasure, romance, gambling, and children because all involve risk-taking self-projection. The great test here is purity of motive: acting from one's essential nature rather than ego-driven desires. Pure action expresses the actor's intrinsic character and rhythm without personal concern for results—what the Bhagavad-Gita calls karma yoga.

#### Complete Chinese Interpretation (Secondary Language)

第五宫代表通过第四宫整合积累的力量的释放和表达。这里人格成为创造性力量——在世界上留下印记。

**创造力的层次**：
- **生物层**：生育子女——为人类种族服务
- **文化层**：艺术、制度、领导——为社会服务
- **精神层**：作为宇宙力量的透明透镜——服务于进化

第五宫与快乐、浪漫、赌博和子女相关，因为所有这些都涉及冒险的自我投射。伟大的考验是动机的纯粹：从本质自然而非自我驱动的欲望行动。纯粹的行动表达行动者的内在特性和节奏，不关心结果——《薄伽梵歌》所说的业瑜伽。

#### Core Points

- **Power release**: Fourth house integration generates fifth house creative energy
- **Creativity defined**: Impressing personality characteristics upon community
- **Biological vs cultural**: Procreation and artistic creation share essential nature
- **Risk and projection**: Romance, gambling, children all involve self-extension
- **Purity test**: Acting from essential nature without ego-concern for results
- **Sun's house**: Solar energy, individuality, self-expression, drama

#### Narrative Snippets

- `[ns_houses_h5_001]` `[trigger: house_5]` `[factor_trigger: house_5 AND House_Philosophy_12H_20]` `[role: 主干]` Creativity is referred to the fifth house because to create is to impress upon one's community characteristics of one's own personality—to make one's mark upon society. → House 5 Source
- `[ns_houses_h5_002]` `[trigger: house_5 AND astro_purity]` `[factor_trigger: house_5 AND House_Philosophy_12H_6]` `[role: 条件分支]` The fifth house test involves purity of motive—to be pure is to be exclusively what one is as a unique individual in terms of one's destiny. → House 5 Source"""
    normalized_text_zh: str = """"""
    subject: str = "House 5 - Self-Expression/Creativity (Succedent)"
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
        l1_anchor="ah_v1.0.0_house_5___self_expression_crea_001_L1",
    )
    version: str = "1.0.0"
