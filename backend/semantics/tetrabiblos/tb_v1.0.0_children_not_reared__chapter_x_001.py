"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.192719
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
    semantic_id="tb_v1.0.0_children_not_reared__chapter_x_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class ChildrenNotRearedChapterX(SemanticEntry):
    """
    **Source Text** (Lines 5440-5533):
> The question is whether the child will or will not be reared. T...
    """
    
    original_text: str = """**Source Text** (Lines 5440-5533):
> The question is whether the child will or will not be reared. This inquiry is distinct from duration of life. If either luminary be in an angle, and one malefic be in conjunction with it, or equally distant from each luminary (forming triangle apex), while no benefic partakes in configuration and luminary rulers are in places controlled by malefics—the child will not be susceptible of nurture but will immediately perish. Mars is exceedingly pernicious when succedent to Sun; Saturn when succedent to Moon.

**English Paraphrase (Primary Language)**:
**Infant mortality** (whether child will be reared) is judged separately from longevity:

**Death indicators**:
- Luminary angular + malefic conjunct or equidistant from both luminaries
- No benefic configuration
- Luminary rulers in malefic-controlled places
- Mars succedent to Sun; Saturn succedent to Moon = especially deadly

**Survival conditions**:
- If malefics cast rays *after* luminaries but benefics *before* = child abandoned but adopted, will live
- If benefics elevated above malefics = good adoption
- If malefics elevated = miserable servitude

**Complete Chinese Interpretation (Secondary Language)**:
**婴儿死亡**（孩子是否会被抚养）与寿命分开判断：

**死亡指标**：
- 发光体在角宫 + 凶星合相或与两发光体等距
- 无吉星配置
- 发光体主星在凶星控制的位置
- 火星在太阳之后继；土星在月亮之后继 = 尤其致命

**存活条件**：
- 凶星在发光体*之后*投射光线但吉星*之前* = 孩子被遗弃但被收养，会存活
- 吉星高于凶星 = 好的收养
- 凶星高于 = 悲惨的奴役

**Core Points**:
- Distinct from longevity inquiry (< 1 year)
- Malefic-luminary configuration = immediate death risk
- Mars harmful to Sun; Saturn to Moon
- Benefic intervention = survival but possibly abandonment

**Narrative Snippets**:
- `[ns_tetra_iii_021]` `[trigger: not_reared]` `[factor_trigger: astro_infant_mortality]` `[role: 主干]` Children not reared when malefics configure with angular luminaries without benefic intervention. → Source Text III.10
- `[ns_tetra_iii_lum]` `[trigger: luminary]` `[factor_trigger: luminary]` `[role: 主干]` Luminaries (Sun and Moon) are the lights of the chart—their angular position and malefic configurations determine infant viability. → Source Text III.10
- `[ns_tetra_iii_mp]` `[trigger: malefic_planet]` `[factor_trigger: malefic_planet]` `[role: 条件分支]` Malefic planets (Saturn and Mars) in hostile configuration with luminaries: Mars threatens Sun, Saturn threatens Moon. → Source Text III.10"""
    normalized_text_zh: str = """"""
    subject: str = "Children Not Reared (Chapter X)"
    factor_refs: list = ['engine_id', 'infant_mortality', 'astrology_classical', 'source_ref', 'rel_iii_021', 'malefic_planet', 'fatal', 'evi_iii_021', 'infant_mortality', 'rule_infant_death', 'concept_nurture', 'infant_mortality', 'attachment']
    
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
        l1_anchor="tb_v1.0.0_children_not_reared__chapter_x_001_L1",
    )
    version: str = "1.0.0"
