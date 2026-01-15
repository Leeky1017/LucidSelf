"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.182579
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
    semantic_id="tb_v1.0.0_the_four_angles__chapter_xiii_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class TheFourAnglesChapterXiii(SemanticEntry):
    """
    **Source Text** (Lines 2043-2084):
> The angles are the four cardinal points of the horizon... the e...
    """
    
    original_text: str = """**Source Text** (Lines 2043-2084):
> The angles are the four cardinal points of the horizon... the eastern point, or angle of the ascendant, is chiefly dry in its nature; because, on the Sun's arrival therein, the damps occasioned by the night begin to be dried up... The southern point, or angle of the mid-heaven, is the most hot... The western point, or occidental angle, is moist; because, when the Sun is there, the moisture, which had been overpowered during the day, recommences its operation... The northern point, or angle of the lower heaven, is the most cold...

**English Paraphrase (Primary Language)**:
Ptolemy assigns elemental qualities to the **four angles**:
- **Ascendant (East)**: Dry—sunrise dries nocturnal moisture
- **Midheaven (South)**: Hot—Sun at meridian, maximum heat
- **Descendant (West)**: Moist—sunset allows moisture to return
- **IC (North)**: Cold—midnight, maximum cold

This creates a framework where angular placement modifies planetary expression by adding the angle's quality to the planet's inherent quality. Stars are stronger when their quality matches the angle's quality (fire planet at MC), weaker when contrary (fire planet at IC).

**Complete Chinese Interpretation (Secondary Language)**:
托勒密为**四角**分配元素属性：
- **上升点（东）**：干燥——日出干燥夜间湿气
- **中天（南）**：炎热——太阳在子午线，最大热量
- **下降点（西）**：湿润——日落允许湿气返回
- **天底（北）**：寒冷——午夜，最大寒冷

这创造了一个框架，其中角度位置通过将角度的属性添加到行星的固有属性来修改行星表达。当行星的属性与角度的属性匹配时（火性行星在中天），更强；当相反时（火性行星在天底），更弱。

**Core Points**:
- Ascendant = Dry (sunrise dries damp)
- Midheaven = Hot (Sun at meridian)
- Descendant = Moist (sunset releases moisture)
- IC = Cold (midnight)
- Angular quality modifies planetary expression
- Matching qualities strengthen; contrary qualities weaken

**Narrative Snippets**:
- `[ns_tetra_i040]` `[trigger: angle_quality]` `[factor_trigger: astro_house_angle AND angle_quality]` `[role: 主干]` The four angles have distinct qualities: Ascendant is dry, Midheaven hot, Descendant moist, IC cold. → Source Text I.13
- `[ns_tetra_i041]` `[trigger: quality_interaction]` `[factor_trigger: astro_planet_angle_interaction]` `[role: 条件分支]` Stars are more efficacious when their quality matches the angle's; less so when contrary qualities are mixed. → Source Text I.13

**Textual Criticism**: N/A: Standard angular doctrine."""
    normalized_text_zh: str = """"""
    subject: str = "The Four Angles (Chapter XIII)"
    factor_refs: list = ['angle_quality', 'engine_id', 'house_angle', 'astrology_classical', 'source_ref', 'rel_i_015', 'house_angle', 'amplifying', 'evi_i_011', 'house_angle', 'rule_angle_quality', 'concept_angle', 'house_angle', 'orientation']
    
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
        l1_anchor="tb_v1.0.0_the_four_angles__chapter_xiii_001_L1",
    )
    version: str = "1.0.0"
