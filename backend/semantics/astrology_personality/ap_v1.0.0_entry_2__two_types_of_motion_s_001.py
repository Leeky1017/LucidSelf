"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237981
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
    semantic_id="ap_v1.0.0_entry_2__two_types_of_motion_s_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry2TwoTypesOfMotionS(SemanticEntry):
    """
    **Source Text** (Lines 5907-5962):
> Motion: Subjective and Objective... it is necessary to distingu...
    """
    
    original_text: str = """**Source Text** (Lines 5907-5962):
> Motion: Subjective and Objective... it is necessary to distinguish between two types of motion: Motion which does not involve displacement of the center of the being, and motion which does involve such a displacement...
>
> The first type of motion can be called "motion in time" or "subjective motion"... It symbolizes inner changes, and what Bergson calls real time or duration...
>
> The second type of motion... is definitely "motion in space" or "objective motion"... Space is a framework for the interplay of relationships of parts within a whole...
>
> Axial rotation and orbital revolution will be the two pillars upon which the temple of astrological symbolism will rest.

**Key Term Analysis**:
- **Subjective motion (axial rotation)**: `no displacement of center` / `motion in time` / `interior changes` / `individual`
- **Objective motion (orbital revolution)**: `displacement of center` / `motion in space` / `relationships` / `collective`
- **Two pillars**: `axial rotation (individual) + orbital revolution (collective)` / `temple foundation`

**English Paraphrase (Primary Language)**:
Rudhyar establishes the fundamental dualism of motion: **Subjective motion** (axial rotation) = no displacement of center, interior changes, Bergson's "duration," individual factor. **Objective motion** (orbital revolution) = displacement of center, relationships in space, collective factor.

"Axial rotation and orbital revolution will be the two pillars upon which the temple of astrological symbolism will rest."

**Complete Chinese Interpretation (Secondary Language)**:
Rudhyar建立运动的基本二元：**主观运动**（轴向旋转）=中心不位移，内在变化，柏格森的"绵延"，个体因素。**客观运动**（轨道公转）=中心位移，空间中的关系，集体因素。

"轴向旋转和轨道公转将是占星符号学殿堂所依托的两根支柱。"

**Narrative Snippets**:
- `[ns_aop_135]` `[trigger: subjective_motion]` `[factor_trigger: astro_motion_subjective]` `[role: 主干]` Subjective motion: axial rotation, no center displacement, interior changes, individual. → L5933-5939
- `[ns_aop_136]` `[trigger: objective_motion]` `[factor_trigger: astro_motion_objective]` `[role: 主干依赖]` Objective motion: orbital revolution, center displacement, relationships, collective. → L5941-5949
- `[ns_aop_137]` `[trigger: two_pillars]` `[factor_trigger: astro_two_pillars AND astro_pillars]` `[role: 总结]` Two pillars of astrological symbolism: axial rotation + orbital revolution. → L5953-5956"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 2: Two Types of Motion—Subjective and Objective"
    factor_refs: list = ['motion_subjective', 'motion_objective']
    
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
        book_id="astrology_personality",
        chapter="",
        l1_anchor="ap_v1.0.0_entry_2__two_types_of_motion_s_001_L1",
    )
    version: str = "1.0.0"
