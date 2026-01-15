"""
Auto-generated semantic module for astrological_houses
Generated at: 2025-12-05T13:30:20.333801
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
    semantic_id="ah_v1.0.0_house_11___vision_community__s_001",
    book_id="astrological_houses",
    engine_id="astro"
)
class House11VisionCommunityS(SemanticEntry):
    """
    #### Source Text

"The eleventh house deals with forms which the powers manifesting in the tenth hou...
    """
    
    original_text: str = """#### Source Text

"The eleventh house deals with forms which the powers manifesting in the tenth house may take as they are released. In the eleventh house the power of society, of the collectivity or group, is released through the individual. It is creation not of the individual—as in the fifth house—but through the individual. The eleventh house is where every individual's star of destiny becomes a vibrant source of power in actual operation. Traditional astrology speaks feebly of 'hopes and wishes.' How weak a conception! It is one of the most vibrant of all houses—the seed of a new day, the communion of the few who together constitute the seed of transformation."

#### English Paraphrase (Primary Language)

The eleventh house represents the release of collective power through the individual who has achieved social integration. Unlike fifth house creativity which expresses individual personality, eleventh house creativity channels the power of the Whole through the person serving as transparent lens. This is where visionary ideals form—the seed of future cycles. Rudhyar criticizes the traditional "hopes and wishes" interpretation as impoverished. The eleventh house is about friends united by shared purpose, reformers and revolutionaries, and the creative vision that can transform society. Success and failure alike must be used wisely—the succedent nature emphasizes that achievement (tenth house) is meaningless without creative application toward new tomorrows.

#### Complete Chinese Interpretation (Secondary Language)

第十一宫代表集体力量通过已实现社会整合的个体的释放。与表达个人人格的第五宫创造力不同，第十一宫创造力通过服务于更大整体的人作为透明透镜来引导。

**第五宫vs第十一宫**：
- **第五宫**：个人创造——个体的创造力
- **第十一宫**：通过个人的创造——整体通过个体的创造力

这里是幻象理想形成的地方——未来周期的种子。鲁迪亚批评传统的"希望和愿望"解释过于贫乏。第十一宫是关于因共同目的而团结的朋友、改革者和革命者，以及能够转化社会的创造性愿景。成功和失败都必须被明智地使用——续宫性质强调成就（第十宫）如果没有朝向新明天的创造性应用就毫无意义。

#### Core Points

- **Collective through individual**: Whole creates through the person, not of them
- **Visionary function**: Seeds of future cycles, transformative ideals
- **Friends by purpose**: Companions united by shared orientation, not personal attachment
- **Success/failure use**: Both must be creatively applied toward new tomorrows
- **Star activation**: Individual's star of destiny becomes operative power
- **Reformation potential**: House of reformers, revolutionaries, iconoclasts

#### Narrative Snippets

- `[ns_houses_h11_001]` `[trigger: house_11]` `[factor_trigger: house_11 AND whole]` `[role: 主干]` In the eleventh house the power of society is released through the individual—it is creation not of the individual but through them, as the Whole works through a clear lens. → House 11 Source
- `[ns_houses_h11_002]` `[trigger: house_11 AND astro_vision]` `[factor_trigger: house_11 AND society]` `[role: 条件分支]` The eleventh house is where the seed of a new day forms—the communion of the few who together constitute the seed of transformation for society. → House 11 Source"""
    normalized_text_zh: str = """"""
    subject: str = "House 11 - Vision/Community (Succedent)"
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
        l1_anchor="ah_v1.0.0_house_11___vision_community__s_001_L1",
    )
    version: str = "1.0.0"
