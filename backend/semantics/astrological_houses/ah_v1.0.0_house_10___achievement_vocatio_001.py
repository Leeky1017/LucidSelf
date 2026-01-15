"""
Auto-generated semantic module for astrological_houses
Generated at: 2025-12-05T13:30:20.333790
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
    semantic_id="ah_v1.0.0_house_10___achievement_vocatio_001",
    book_id="astrological_houses",
    engine_id="astro"
)
class House10AchievementVocatio(SemanticEntry):
    """
    #### Source Text

"The tenth house is the house of achievement. A series of developments comes to a ...
    """
    
    original_text: str = """#### Source Text

"The tenth house is the house of achievement. A series of developments comes to a head—first house potential theoretically becomes actualized fully in the tenth house. In the fourth house, power is drawn from the matrix of race, family, tradition. Tenth house power results from shared participation formed in the seventh house, become productive in the eighth, reaching understanding in the ninth. The individual is integrated into the greater whole in which he participates cooperatively. He has a place, a function, a public status. This 'office' defines his stand in the community. Any social office provides the officiant with social power. The individual and the social position are polar opposites meant to complement each other."

#### English Paraphrase (Primary Language)

The tenth house represents the culmination of the entire chart's developmental process—where first house potential achieves concrete actualization as social function. The MC (Medium Coeli) is a solar factor representing the consummation of organic and communal functions. The individual becomes integrated into the greater whole through their vocation—a calling that both expresses individual destiny and serves collective need. The key tension is between individual authenticity and institutional requirements. At the highest level, "the Mastery seeks the one who will embody its qualities"—the individual aspires upward while the archetype descends to meet them. This is the Transfiguration, where the star above blends its rays with the tone of the self within the human heart.

#### Complete Chinese Interpretation (Secondary Language)

第十宫代表整个命盘发展过程的顶点——第一宫潜能在这里实现为社会功能的具体化。MC（中天）是太阳因素，代表有机和公共功能的完成。

**第十宫的核心动态**：
- **整合**：个体通过天职整合到更大整体中
- **极性张力**：个人真实性vs制度要求
- **达成目标**：第一宫潜能在这里完全实现
- **变容**：上方的星与心中自我的音调融合

在最高层次，"大师身份寻找那个将体现其品质的人"——个体向上渴望，同时原型下降与之相遇。这是变容，天空与大地在个体化的人中合一。

#### Core Points

- **Achievement house**: Where first house potential actualizes as social function
- **MC as solar factor**: Consummation of organic and communal functions
- **Vocation concept**: Calling that expresses individual destiny while serving collective
- **Individual-office polarity**: Tension between authenticity and institutional role
- **Transfiguration**: Meeting of ascending individual and descending archetype
- **Public power**: Social office provides power that must be used responsibly

#### Narrative Snippets

- `[ns_houses_h10_001]` `[trigger: house_10]` `[factor_trigger: house_10 AND mc]` `[role: 主干]` The tenth house is the house of achievement—first house potential theoretically becomes actualized fully here through integration into the greater whole. → House 10 Source
- `[ns_houses_h10_002]` `[trigger: house_10 AND astro_vocation]` `[factor_trigger: house_10 AND first_house]` `[role: 总结]` The Mastery seeks the one who will embody its qualities—the individual aspires while the archetype descends to meet, Heaven uniting with Earth in the transfigured person. → House 10 Source"""
    normalized_text_zh: str = """"""
    subject: str = "House 10 - Achievement/Vocation (Angular - MC)"
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
        l1_anchor="ah_v1.0.0_house_10___achievement_vocatio_001_L1",
    )
    version: str = "1.0.0"
