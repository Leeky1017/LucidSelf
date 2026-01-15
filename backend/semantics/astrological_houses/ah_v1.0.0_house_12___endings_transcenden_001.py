"""
Auto-generated semantic module for astrological_houses
Generated at: 2025-12-05T13:30:20.333811
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
    semantic_id="ah_v1.0.0_house_12___endings_transcenden_001",
    book_id="astrological_houses",
    engine_id="astro"
)
class House12EndingsTranscenden(SemanticEntry):
    """
    #### Source Text

"The twelfth house closes the cycle of human experience. In it the individual eith...
    """
    
    original_text: str = """#### Source Text

"The twelfth house closes the cycle of human experience. In it the individual either consolidates successes into the seed of a new cycle, or meets the accumulated results of failures. Memories of the past crowd over the threshold—Angels of Light beckoning to the beyond, or dark Guardians of the Threshold shaped by frustrations, fears, and sins. The individual must face this compound entity which he himself has created. Yet there must always be a new cycle. The darkness can be borne if man realizes that only by letting go of the lesser is it possible to be born into the greater. The twelfth house contains the seed of rebirth. The collective power of memories—what is called karma—may be so great that it stifles individual Identity, or the confrontations may be met successfully and the Tone of the new cycle rings out clearly."

#### English Paraphrase (Primary Language)

The twelfth house represents the completion and dissolution necessary for rebirth. Here the individual confronts the accumulated karma of the entire cycle—both personal and collective. This is the house of institutions (hospitals, prisons, monasteries) because they represent contexts where individual identity is submerged in collective processes. The "Guardian of the Threshold" must be faced—the compound entity created by all unresolved experiences. At the deepest level, this house connects individual fate to collective destiny: what the individual experiences as fate often originates in society's karma. The twelfth house contains the seed of the next cycle—what is released here conditions the Ascendant's new beginning. The great choice is between being overwhelmed by accumulated darkness or consciously integrating it to clear the way for authentic rebirth.

#### Complete Chinese Interpretation (Secondary Language)

第十二宫代表重生所必需的完成和消解。这里个体面对整个周期积累的业力——个人的和集体的。这是机构（医院、监狱、修道院）的宫位，因为它们代表个体身份淹没在集体过程中的背景。

**第十二宫的双重面向**：
- **阴暗面**：业力、恐惧、无意识、监禁、自我毁灭
- **光明面**：灵性解脱、神秘经验、与宇宙合一、种子

"门槛守护者"必须被面对——由所有未解决经验创造的复合实体。在最深层次，这个宫位将个人命运与集体命运连接：个人经历为命运的往往起源于社会的业力。第十二宫包含下一个周期的种子——这里释放的条件化上升点的新开始。伟大的选择是被积累的黑暗淹没，还是有意识地整合它以为真实重生清路。

#### Core Points

- **Cycle completion**: Consolidation of successes or confrontation with failures
- **Karma confrontation**: Accumulated memories as Angels or Guardians
- **Institutional connection**: Hospitals, prisons, monasteries as dissolution contexts
- **Collective karma**: Individual fate connected to society's destiny
- **Seed of rebirth**: What is released here conditions next cycle's Ascendant
- **Integration choice**: Overwhelm or conscious integration of accumulated past

#### Narrative Snippets

- `[ns_houses_h12_001]` `[trigger: house_12]` `[factor_trigger: house_12 AND past]` `[role: 主干]` The twelfth house closes the cycle—the individual either consolidates successes into seed for new cycle, or meets accumulated results of failures as Guardian of the Threshold. → House 12 Source
- `[ns_houses_h12_002]` `[trigger: house_12 AND astro_rebirth]` `[factor_trigger: house_12 AND transformation]` `[role: 总结]` The twelfth house contains the seed of rebirth—only by letting go of the lesser is it possible to be born into the greater, as the Tone of the new cycle rings out clearly. → House 12 Source"""
    normalized_text_zh: str = """"""
    subject: str = "House 12 - Endings/Transcendence (Cadent)"
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
        l1_anchor="ah_v1.0.0_house_12___endings_transcenden_001_L1",
    )
    version: str = "1.0.0"
