"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.192779
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
    semantic_id="tb_v1.0.0_exemplification_of_prorogation_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class ExemplificationOfProrogation(SemanticEntry):
    """
    **Source Text** (Lines 5984-6218):
> In order to exemplify the foregoing instructions, let the first...
    """
    
    original_text: str = """**Source Text** (Lines 5984-6218):
> In order to exemplify the foregoing instructions, let the first point of Aries be supposed as the preceding place, and the first point in Gemini the succeeding... The times must be multiplied by the horary magnitude... Whatever proportion the temporal hours bear to the quadrant, the same proportion, out of the excess of times, is to be added or deducted.

**English Paraphrase (Primary Language)**:
Ptolemy provides **worked examples** of prorogation calculations:

**Example 1**: Prorogator at ASC (0° Aries)
- Succeeding degree: 0° Gemini
- Latitude: 14-hour longest day (Alexandria ~30°N)
- Horary magnitude: 17 equatorial times
- Calculate times of ascension between degrees

**Example 2**: Prorogator at MC
- Use right ascension times
- Simpler calculation than ASC

**Example 3**: Prorogator at DSC
- Use descension times
- Account for opposite signs rising

**Example 4**: Prorogator between angles
- Interpolate proportionally between angle values
- Use horary proportion method

**Complete Chinese Interpretation (Secondary Language)**:
托勒密提供了主限计算的**实例**：

**例1**：主限星在上升（白羊0°）
- 后续度数：双子0°
- 纬度：14小时最长日（亚历山大约30°N）
- 时辰幅度：17赤道时
- 计算度数之间的上升时间

**例2**：主限星在中天
- 使用赤经时间
- 比上升计算更简单

**例3**：主限星在下降
- 使用下降时间
- 考虑对面星座上升

**例4**：主限星在角宫之间
- 在角宫值之间按比例插值
- 使用时辰比例方法

**Core Points**:
- Worked examples for each angular position
- Horary magnitude varies by latitude
- Interpolation for intermediate positions
- Technical precision required

**Narrative Snippets**:
- `[ns_tetra_iii026]` `[trigger: prorogation_example]` `[factor_trigger: astro_calculation_method]` `[role: 主干]` Ptolemy provides worked examples for prorogation calculation at each angular position. → Source Text III.15
- `[ns_tetra_iii_pc]` `[trigger: prorogation_calc]` `[factor_trigger: prorogation_calc]` `[role: 主干]` Prorogation calculation: multiply times of ascension between degrees by horary magnitude to determine years of life. → Source Text III.15"""
    normalized_text_zh: str = """"""
    subject: str = "Exemplification of Prorogation (Chapter XV)"
    factor_refs: list = ['engine_id', 'prorogation_calc', 'astrology_classical', 'source_ref', 'rel_iii_026', 'prorogation_calc', 'determining', 'evi_iii_026', 'prorogation_calc', 'rule_prorogation_calc', 'concept_calculation', 'prorogation_calc', 'analytical_thinking']
    
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
        book_id="tetrabiblos",
        chapter="",
        l1_anchor="tb_v1.0.0_exemplification_of_prorogation_001_L1",
    )
    version: str = "1.0.0"
