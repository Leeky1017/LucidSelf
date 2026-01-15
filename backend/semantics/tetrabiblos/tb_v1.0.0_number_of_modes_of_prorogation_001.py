"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.192768
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
    semantic_id="tb_v1.0.0_number_of_modes_of_prorogation_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class NumberOfModesOfProrogation(SemanticEntry):
    """
    **Source Text** (Lines 5711-5982):
> When the prorogator has been determined, it is also necessary t...
    """
    
    original_text: str = """**Source Text** (Lines 5711-5982):
> When the prorogator has been determined, it is also necessary to take into consideration the two modes of prorogation: one into succeeding signs, under the projection of rays; and when the prorogator is in an oriental place (between MC and ASC), this mode only is used. The other extends into signs preceding the prorogator, according to horary proportion; when the prorogator is between MC and DSC, both modes are adopted.

**English Paraphrase (Primary Language)**:
**Two modes of prorogation**:

1. **Direct motion** (into succeeding signs): "Projection of rays"
   - Used when prorogator is **oriental** (between MC and ASC)
   - Only this mode applies

2. **Converse motion** (into preceding signs): "Horary proportion"
   - Used when prorogator is **occidental** (between MC and DSC)
   - Both modes apply in this case

**Anæretic degrees**:
- In converse prorogation: Only the **occidental horizon** (DSC) is strictly anæretic
- Malefics (Saturn, Mars) in quartile/opposition shorten life
- Benefics (Jupiter, Venus) in aspect extend life

**Calculation**: Each equatorial degree = one year of life.

**Complete Chinese Interpretation (Secondary Language)**:
**两种主限模式**：

1. **直接运动**（进入后续星座）："光线投射"
   - 当主限星在**东方**（中天和上升之间）时使用
   - 仅适用此模式

2. **逆向运动**（进入前面星座）："时辰比例"
   - 当主限星在**西方**（中天和下降之间）时使用
   - 两种模式都适用

**截寿度数**：
- 在逆向主限中：仅**西方地平线**（下降）是严格截寿的
- 凶星（土星、火星）在四分/对分缩短寿命
- 吉星（木星、金星）在相位延长寿命

**计算**：每赤道度数 = 一年寿命。

**Core Points**:
- Two modes: direct and converse
- Oriental prorogator = direct only
- Occidental prorogator = both modes
- DSC is primary anæretic in converse
- Equatorial degree = one year

**Narrative Snippets**:
- `[ns_tetra_iii025]` `[trigger: prorogation_modes]` `[factor_trigger: astro_direction_mode]` `[role: 主干]` Two modes of prorogation: direct (oriental) and converse (occidental)—DSC is primary anæretic. → Source Text III.14
- `[ns_tetra_iii_pp]` `[trigger: prorogator_position]` `[factor_trigger: prorogator_position]` `[role: 条件分支]` Prorogator position (oriental or occidental) determines direction mode: oriental directs forward only, occidental directs both ways. → Source Text III.14"""
    normalized_text_zh: str = """"""
    subject: str = "Number of Modes of Prorogation (Chapter XIV)"
    factor_refs: list = ['engine_id', 'prorogation_direct', 'astrology_classical', 'prorogation_converse', 'astrology_classical', 'anaeretic', 'astrology_classical', 'source_ref', 'rel_iii_025', 'astro_direction_mode', 'mode_selection', 'evi_iii_025', 'direction_mode', 'rule_direction_mode', 'concept_direction', 'prorogation_mode', 'life_trajectory']
    
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
        l1_anchor="tb_v1.0.0_number_of_modes_of_prorogation_001_L1",
    )
    version: str = "1.0.0"
