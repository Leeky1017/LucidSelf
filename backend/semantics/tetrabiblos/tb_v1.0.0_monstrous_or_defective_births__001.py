"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.192707
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
    semantic_id="tb_v1.0.0_monstrous_or_defective_births__001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class MonstrousOrDefectiveBirths(SemanticEntry):
    """
    **Source Text** (Lines 5369-5437):
> The same places are to be considered in inquiring into the prob...
    """
    
    original_text: str = """**Source Text** (Lines 5369-5437):
> The same places are to be considered in inquiring into the probability of a monstrous or defective birth. At a birth of this description, the luminaries are either cadent from the ascendant, or not configurated with it; while the angles are occupied by the malefics. If all the places in which the rulers of the luminaries, and the Moon herself and Mercury are situated, should be totally inconjunct with the preceding new or full Moon and its ruler, the birth will be monstrous. If the luminaries be in quadrupedal or bestial signs while two malefics are in angles, the birth will not be human.

**English Paraphrase (Primary Language)**:
**Monstrous/defective births** occur when:
- Luminaries are cadent from ASC or unconfigured with it
- Malefics occupy angles
- Moon/Mercury/luminary rulers are inconjunct the prenatal lunation

**Degrees of abnormality**:
- If luminaries in bestial signs + malefics angular without benefic support = non-human birth
- If luminaries in human signs + malefics angular + no benefic = human but defective
- Jupiter/Venus support = veiled defect (hermaphrodites, speech impediments)
- Mercury alone supporting = deaf and dumb but clever

**Complete Chinese Interpretation (Secondary Language)**:
**畸形/缺陷出生**发生在：
- 发光体从上升点陷落或与其无配置
- 凶星占据角宫
- 月亮/水星/发光体主星与产前朔望无相位

**异常程度**：
- 发光体在兽形星座 + 凶星角宫无吉星支持 = 非人类出生
- 发光体在人形星座 + 凶星角宫 + 无吉星 = 人类但有缺陷
- 木星/金星支持 = 隐藏缺陷（阴阳人、言语障碍）
- 仅水星支持 = 聋哑但聪明

**Core Points**:
- Luminaries cadent/unconfigured = abnormal birth risk
- Malefics angular = severity indicator
- Sign shape (human/bestial) determines degree
- Benefic support mitigates severity

**Narrative Snippets**:
- `[ns_tetra_iii_020]` `[trigger: monstrous_birth]` `[factor_trigger: astro_birth_defect]` `[role: 主干]` Monstrous births occur when luminaries are cadent from ASC while malefics occupy angles. → Source Text III.9
- `[ns_ptolemy_iii_035]` `[trigger: bestial_signs]` `[factor_trigger: astro_sign_bestial AND astro_birth]` `[role: 条件分支]` If luminaries in bestial signs with malefics angular without benefic support, the birth will not be human. → Severity
- `[ns_ptolemy_iii_036]` `[trigger: benefic_mitigation]` `[factor_trigger: astro_benefic AND astro_birth_defect]` `[role: 条件分支]` Jupiter/Venus support mitigates to veiled defects; Mercury alone = deaf and dumb but clever. → Mitigation
- `[ns_tetra_iii_lp]` `[trigger: luminary_position]` `[factor_trigger: luminary_position]` `[role: 条件分支]` Luminary position (angular, succedent, cadent) determines birth normalcy—cadent luminaries with angular malefics indicate defect risk. → Source Text III.9"""
    normalized_text_zh: str = """"""
    subject: str = "Monstrous or Defective Births (Chapter IX)"
    factor_refs: list = ['engine_id', 'birth_defect', 'astrology_classical', 'source_ref', 'rel_iii_020', 'astro_birth_defect', 'warning', 'evi_iii_020', 'birth_defect', 'rule_monstrous', 'concept_defect', 'birth_defect', 'congenital']
    
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
        l1_anchor="tb_v1.0.0_monstrous_or_defective_births__001_L1",
    )
    version: str = "1.0.0"
